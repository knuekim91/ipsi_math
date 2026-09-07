# -*- coding: utf-8 -*-
"""교재 PDF 의 그림을 잘라 docs/img/ 에 PNG 로 넣는다.

원본에 그림이 있는 문항은 내가 SVG 로 다시 그리지 않는다.
다시 그리면 각도나 길이가 미묘하게 달라져 문제와 어긋날 수 있기 때문이다.
설명을 위해 내가 만든 그래프는 그대로 SVG 로 그린다 (테마를 따라가야 하므로).

    python build/figcrop.py --pdf <경로> --page 121 --list
    python build/figcrop.py --pdf <경로> --page 121 --pick 0 --name TRI-D12
    python build/figcrop.py --pdf <경로> --page 121 --bbox 402,175,524,266 --name TRI-D12
"""
import argparse, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "img")
DPI = 400          # 122pt 짜리 그림이 약 680px. 화면 380px 로 줄여 쓰면 선명하다.
PAD = 8            # 그림 둘레 여백 (pt)

# 조건상자(가/나)는 그림이 아니다. 단 너비(248pt)를 꽉 채우는 둥근 사각형이 그것이다.
COLW = 248.0
CHOICE = re.compile(r"^[①-⑳]")


def grow(r, g):
    import pymupdf
    return pymupdf.Rect(r.x0 - g, r.y0 - g, r.x1 + g, r.y1 + g)


def find(pg, gap=16):
    """페이지에서 그림 덩어리를 찾는다. 조건상자는 뺀다."""
    import pymupdf
    R = pg.rect
    boxes = []
    for p in pg.get_drawings():
        r = pymupdf.Rect(p["rect"])
        if r.x0 < 0 or r.y0 < 0 or r.x1 > R.x1 or r.y1 > R.y1:
            continue                                   # 재단선 밖 장식
        if r.width > R.width * 0.8 or r.height > R.height * 0.8:
            continue                                   # 전면 괘선
        if r.width < 1 and r.height < 1:
            continue
        boxes.append(r)
    merged = True
    while merged:
        merged = False
        for i in range(len(boxes)):
            for j in range(len(boxes) - 1, i, -1):
                if grow(boxes[i], gap).intersects(boxes[j]):
                    boxes[i] = boxes[i] | boxes[j]
                    boxes.pop(j)
                    merged = True
            if merged:
                break
    figs = [r for r in boxes
            if r.width > 45 and r.height > 45 and abs(r.width - COLW) > 6]

    # 점 이름(A, B, C …)은 도형이 아니라 글자라 위 bbox 에 안 잡힌다. 끌어들인다.
    for b in pg.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                t = s["text"].strip()
                if not t or len(t) > 2 or CHOICE.match(t):
                    continue                            # 선택지 번호는 제외
                r = pymupdf.Rect(s["bbox"])
                cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
                for k, f in enumerate(figs):
                    if grow(f, 14).contains(pymupdf.Point(cx, cy)):
                        figs[k] = figs[k] | r
                        break
    return sorted(figs, key=lambda r: (round(r.y0), r.x0))


def main():
    import pymupdf
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--page", type=int, required=True, help="본문 쪽번호 (1부터)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--pick", type=int, help="--list 에서 본 번호")
    ap.add_argument("--bbox", help="x0,y0,x1,y1 로 직접 지정")
    ap.add_argument("--name", help="저장 이름 (문항 ID)")
    ap.add_argument("--dpi", type=int, default=DPI)
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    pg = doc[a.page - 1]

    if a.bbox:
        x0, y0, x1, y1 = [float(v) for v in a.bbox.split(",")]
        clip = pymupdf.Rect(x0, y0, x1, y1)
    else:
        figs = find(pg)
        if a.list or a.pick is None:
            print("본문 %d쪽에서 찾은 그림 %d개" % (a.page, len(figs)))
            for i, r in enumerate(figs):
                print("  [%d] (%.0f,%.0f)-(%.0f,%.0f)  %.0f x %.0f pt"
                      % (i, r.x0, r.y0, r.x1, r.y1, r.width, r.height))
            return
        clip = grow(figs[a.pick], PAD)

    if not a.name:
        sys.exit("--name 이 필요하다")
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    path = os.path.join(OUT, a.name + ".png")
    pix = pg.get_pixmap(clip=clip, dpi=a.dpi)
    pix.save(path)
    print("%s  %dx%d px  %.1f KB" % (path, pix.width, pix.height,
                                     os.path.getsize(path) / 1024))
    print()
    print("문항 파일에 넣을 조각:")
    print('<div class="fig"><img src="img/%s.png" width="%d" height="%d"'
          % (a.name, pix.width, pix.height))
    print('     alt="여기에 그림 설명을 한 문장으로 적는다"></div>')


if __name__ == "__main__":
    main()

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


def repeated(doc):
    """여러 쪽에 되풀이해 나오는 이미지는 머리글 장식이지 그림이 아니다."""
    from collections import Counter
    c = Counter()
    for pg in doc:
        for im in pg.get_images(full=True):
            c[im[0]] += 1
    return {x for x, n in c.items() if n > 1}


def find(doc, pno, gap=16):
    """한 쪽에서 그림 덩어리를 찾는다. 조건상자와 머리글 장식은 뺀다.

    교재(EBS)는 그림을 벡터로, 평가원 시험지는 래스터 이미지로 넣는다.
    둘 다 잡아야 하므로 두 갈래를 모두 모은 뒤 함께 합친다.
    """
    import pymupdf
    pg = doc[pno]
    R = pg.rect
    boxes = []

    # (1) 벡터로 그린 그림
    for p in pg.get_drawings():
        r = pymupdf.Rect(p["rect"])
        if r.x0 < 0 or r.y0 < 0 or r.x1 > R.x1 or r.y1 > R.y1:
            continue                                   # 재단선 밖 장식
        if r.width > R.width * 0.75 or r.height > R.height * 0.75:
            continue                                   # 단 나눔선·전면 괘선
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

    # (2) 래스터로 넣은 그림
    rep = repeated(doc)
    top = R.height * 0.18                              # 머리글 띠는 그림이 아니다
    for im in pg.get_images(full=True):
        if im[0] in rep:
            continue
        for r in pg.get_image_rects(im[0]):
            r = pymupdf.Rect(r)
            if r.width < 40 or r.height < 30 or r.y1 < top:
                continue
            figs.append(r)

    # 한 그림이 두 장으로 쪼개져 들어간 경우가 있어 다시 합친다
    merged = True
    while merged:
        merged = False
        for i in range(len(figs)):
            for j in range(len(figs) - 1, i, -1):
                if grow(figs[i], 4).intersects(figs[j]):
                    figs[i] = figs[i] | figs[j]
                    figs.pop(j)
                    merged = True
            if merged:
                break

    # 점 이름(A, B, C …)은 도형이 아니라 글자라 위 bbox 에 안 잡힌다. 끌어들인다.
    for b in pg.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            for sp in l["spans"]:
                t = sp["text"].strip()
                if not t or len(t) > 2 or CHOICE.match(t):
                    continue                            # 선택지 번호는 제외
                r = pymupdf.Rect(sp["bbox"])
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
    ap.add_argument("--color", action="store_true",
                    help="색이 들어간 그림일 때만. 기본은 회색조(용량 절반)")
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    pg = doc[a.page - 1]

    if a.bbox:
        x0, y0, x1, y1 = [float(v) for v in a.bbox.split(",")]
        clip = pymupdf.Rect(x0, y0, x1, y1)
    else:
        figs = find(doc, a.page - 1)
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
    # 수학 그림은 검은 선화다. 회색조로 뽑으면 용량이 절반이고 보기는 같다.
    cs = pymupdf.csRGB if a.color else pymupdf.csGRAY
    pix = pg.get_pixmap(clip=clip, dpi=a.dpi, colorspace=cs)
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

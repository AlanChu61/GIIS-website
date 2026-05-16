"""AP Calculus AB · Module 10 — Average Value and Area Between Curves.

Built on slide_kit (math theme = gold + cream).
Custom slides:
- 02_hook                       : bug walking east-then-west number-line visual
                                  showing NET displacement vs TOTAL distance
- 05_average_value_geometry     : parabola y = x^2 on [0,3] with shaded area
                                  and horizontal line y = 3 + rectangle showing
                                  same area = average value
- 11_area_between_intro         : two curves (parabola + line) with the region
                                  between them shaded with the accent color,
                                  labelled top/bottom and the formula
- 16_multi_crossing             : sine and cosine on [0, 2pi] with three
                                  enclosed sub-regions, each alternating top
                                  curve, illustrating the split-at-every-crossing
                                  rule
"""
import sys
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H, wrap,
    INK, MAROON, MAROON_DARK, MUTED, RED, GRID,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Calculus AB", module_num=10,
            output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 10 — Average Value and Area Between Curves",
    "~9 minutes  ·  Unit 8(a) · CHA 8.1 – 8.6",
)


# ─── 02 — hook (custom: bug walks east then west, net vs total) ──────────
def hook(img, d):
    d.text((110, 80), "A bug walks 4 m east, then 7 m west.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168),
           "Where is it now?  How far did it walk?",
           fill=MUTED, font=font("sans", 36))

    # Number line across the middle
    line_y = 470
    line_x0 = 220
    line_x1 = W - 220
    d.line([(line_x0, line_y), (line_x1, line_y)], fill=INK, width=4)

    # Compute positions. Pick a scale: 1 m = 90 px.  Start at x = (line_x0+line_x1)/2 - 200 so trip fits.
    scale = 90
    start_m = -3  # bug starts at -3 m
    start_x = line_x0 + 80
    # tick marks every 1 m from -5 to +5
    for m in range(-5, 6):
        tx = start_x + (m - start_m) * scale
        if line_x0 - 5 <= tx <= line_x1 + 5:
            d.line([(tx, line_y - 8), (tx, line_y + 8)], fill=INK, width=2)
            d.text((tx - 10, line_y + 14), str(m), fill=MUTED, font=font("sans", 22))

    # mark "start" at -3
    start_px = start_x + 0
    d.ellipse([start_px - 12, line_y - 12, start_px + 12, line_y + 12],
              fill=MAROON_DARK)
    d.text((start_px - 30, line_y - 60), "START",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # mark midpoint (after walking 4 east) at +1
    mid_m = 1
    mid_px = start_x + (mid_m - start_m) * scale
    d.ellipse([mid_px - 10, line_y - 10, mid_px + 10, line_y + 10],
              fill=deck.accent, outline=MAROON_DARK, width=3)

    # mark end (after walking 7 west from +1) at -6 ... but -6 is off our line.
    # Adjust scale so trip fits. Use the bug walks 4 east then 7 west → ends at -6 if starts at -3.
    # Easier: change start to 0, end at -3 (net 3 west), midpoint at +4. Total = 11.
    # Redo with start = 0.
    pass  # we'll rebuild below


def hook_v2(img, d):
    d.text((110, 80), "A bug walks 4 m east, then 7 m west.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168),
           "Where is it now?  How far did it actually walk?",
           fill=MUTED, font=font("sans", 36))

    # Number line
    line_y = 540
    line_x0 = 180
    line_x1 = W - 180
    d.line([(line_x0, line_y), (line_x1, line_y)], fill=INK, width=4)
    # arrowheads
    d.polygon([(line_x1, line_y), (line_x1 - 18, line_y - 10),
               (line_x1 - 18, line_y + 10)], fill=INK)
    d.polygon([(line_x0, line_y), (line_x0 + 18, line_y - 10),
               (line_x0 + 18, line_y + 10)], fill=INK)

    # bug starts at 0. Walks +4 (to x = 4). Walks -7 (to x = -3). Range needed: -5 to +5.
    scale = 130  # 1 m = 130 px → 10 m total range = 1300 px (fits in 1560)
    origin_px = (line_x0 + line_x1) // 2

    def to_px(m):
        return origin_px + m * scale

    # tick marks every 1 m from -5 to +5
    for m in range(-5, 6):
        tx = to_px(m)
        d.line([(tx, line_y - 10), (tx, line_y + 10)], fill=INK, width=2)
        lbl = str(m)
        tw = d.textlength(lbl, font=font("sans", 24))
        d.text((tx - tw / 2, line_y + 18), lbl, fill=MUTED, font=font("sans", 24))

    # start dot at 0
    sx = to_px(0)
    d.ellipse([sx - 14, line_y - 14, sx + 14, line_y + 14],
              fill=MAROON_DARK)
    d.text((sx - 38, line_y - 60), "START",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # path arrow 1: 0 → +4 (gold = east)
    ax0 = sx + 4
    ax1 = to_px(4) - 4
    arrow_y1 = line_y - 90
    d.line([(ax0, arrow_y1), (ax1, arrow_y1)], fill=deck.accent, width=8)
    d.polygon([(ax1 + 18, arrow_y1), (ax1, arrow_y1 - 14),
               (ax1, arrow_y1 + 14)], fill=deck.accent)
    d.text(((ax0 + ax1) // 2 - 50, arrow_y1 - 50), "+4 m east",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # midpoint dot at +4
    mx = to_px(4)
    d.ellipse([mx - 10, line_y - 10, mx + 10, line_y + 10],
              fill=deck.accent_light, outline=MAROON_DARK, width=3)

    # path arrow 2: +4 → -3 (maroon = west)
    bx0 = to_px(4) - 4
    bx1 = to_px(-3) + 4
    arrow_y2 = line_y - 150
    d.line([(bx0, arrow_y2), (bx1, arrow_y2)], fill=MAROON, width=8)
    d.polygon([(bx1 - 18, arrow_y2), (bx1, arrow_y2 - 14),
               (bx1, arrow_y2 + 14)], fill=MAROON)
    d.text(((bx0 + bx1) // 2 - 50, arrow_y2 - 50), "−7 m west",
           fill=MAROON, font=font("sans_bold", 30))

    # end dot at -3
    ex = to_px(-3)
    d.ellipse([ex - 14, line_y - 14, ex + 14, line_y + 14],
              fill=MAROON)
    d.text((ex - 28, line_y + 60), "END",
           fill=MAROON, font=font("sans_bold", 26))

    # Bottom comparison strip — two callout cards
    card_y = 770
    card_h = 200
    card_w = 820
    # LEFT — net displacement
    d.rounded_rectangle([110, card_y, 110 + card_w, card_y + card_h],
                        radius=20, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((140, card_y + 20), "Net displacement",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((140, card_y + 80), "= −3 m   (3 m west of start)",
           fill=INK, font=font("mono", 36))
    d.text((140, card_y + 140), "= integral of  v(t)  dt",
           fill=deck.accent, font=font("sans_bold", 28))

    # RIGHT — total distance
    d.rounded_rectangle([990, card_y, 990 + card_w, card_y + card_h],
                        radius=20, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((1020, card_y + 20), "Total distance",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((1020, card_y + 80), "= 11 m   (4 + 7)",
           fill=INK, font=font("mono", 36))
    d.text((1020, card_y + 140), "= integral of  |v(t)|  dt",
           fill=deck.accent, font=font("sans_bold", 28))


deck.custom("02_hook", hook_v2)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Average value of a function — and the divide-by-(b−a) trap.",
        "Particle motion:  net displacement ≠ total distance.",
        "Area between two curves  (including curves that cross 3+ times).",
    ],
    footnote="Every Unit 8 FRQ asks you to distinguish these.  Don't conflate them.",
)


# ─── 04 — average value (equation) ───────────────────────────────────────
deck.equation(
    "04_average_value",
    "Average value of  f  on  [a, b].",
    [
        ("              1     ⌠ b",            INK,    None),
        ("f_avg  =  ─────── · │   f(x) dx",     INK,    "DIVIDE by (b − a) — not multiply"),
        ("            b − a   ⌡ a",            INK,    None),
        ("",                                    INK,    None),
        ("(units of f, NOT units of f · x)",   MAROON, "the 1/(b−a) factor cancels the integral's width"),
    ],
)


# ─── 05 — average value geometry (custom: parabola + horizontal y=3 line) ─
def average_value_geometry(img, d):
    d.text((110, 70), "Average value = height of the same-area rectangle.",
           fill=MAROON, font=font("serif_bold", 50))
    d.text((110, 148),
           "f(x) = x²   on   [0, 3].   ∫₀³ x² dx = 9.   f_avg = 9 / 3 = 3.",
           fill=MUTED, font=font("sans", 32))

    # Plot region
    gx0, gy0 = 200, 230
    gw, gh = 980, 700
    ax_y = gy0 + gh - 60
    origin_x = gx0 + 80

    # axes
    d.line([(gx0, ax_y), (gx0 + gw, ax_y)], fill=INK, width=3)
    d.line([(origin_x, gy0), (origin_x, ax_y + 30)], fill=INK, width=3)
    d.text((gx0 + gw - 30, ax_y + 12), "x", fill=INK, font=font("serif_ital", 28))
    d.text((origin_x + 12, gy0), "y", fill=INK, font=font("serif_ital", 28))

    # Scales: x from -0.5 to 3.5; y from -0.5 to 10
    x_min, x_max = -0.5, 3.5
    y_min, y_max = -0.5, 10.5
    sx = gw / (x_max - x_min)
    sy = (ax_y - gy0 - 20) / (y_max - y_min)

    def to_px(xv, yv):
        return (gx0 + (xv - x_min) * sx, ax_y - (yv - 0) * sy)

    # x-axis ticks 0,1,2,3
    for xv in [0, 1, 2, 3]:
        px, _ = to_px(xv, 0)
        d.line([(px, ax_y - 6), (px, ax_y + 6)], fill=INK, width=2)
        d.text((px - 8, ax_y + 12), str(xv), fill=INK, font=font("sans", 24))
    # y-axis ticks 1..9
    for yv in [1, 3, 5, 7, 9]:
        _, py = to_px(0, yv)
        d.line([(origin_x - 6, py), (origin_x + 6, py)], fill=INK, width=2)
        d.text((origin_x - 38, py - 14), str(yv), fill=INK, font=font("sans", 24))

    # Shaded region under f(x) = x^2 from x=0 to x=3
    region_pts = [to_px(0, 0)]
    xv = 0
    while xv <= 3.001:
        region_pts.append(to_px(xv, xv * xv))
        xv += 0.04
    region_pts.append(to_px(3, 0))
    d.polygon(region_pts, fill=deck.accent_light)

    # Parabola outline
    parab_pts = []
    xv = -0.4
    while xv <= 3.4:
        parab_pts.append(to_px(xv, xv * xv))
        xv += 0.04
    for a_pt, b_pt in zip(parab_pts[:-1], parab_pts[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)

    # Horizontal line y = 3 (the average value) — dashed
    y3_left, y3_right = to_px(0, 3), to_px(3, 3)
    # dashed: draw segments
    dash_len = 14
    gap = 8
    x0d = y3_left[0]
    while x0d < y3_right[0]:
        x1d = min(x0d + dash_len, y3_right[0])
        d.line([(x0d, y3_left[1]), (x1d, y3_left[1])],
               fill=MAROON_DARK, width=5)
        x0d = x1d + gap

    # Rectangle outline (0,0) — (3, 3) — same base, height = average value
    r_p1 = to_px(0, 0)
    r_p2 = to_px(3, 0)
    r_p3 = to_px(3, 3)
    r_p4 = to_px(0, 3)
    d.line([r_p1, r_p2], fill=MAROON_DARK, width=4)
    d.line([r_p2, r_p3], fill=MAROON_DARK, width=4)
    d.line([r_p3, r_p4], fill=MAROON_DARK, width=4)
    d.line([r_p4, r_p1], fill=MAROON_DARK, width=4)

    # "y = 3" label
    lbl_pos = to_px(3.1, 3)
    d.text((lbl_pos[0] + 8, lbl_pos[1] - 18), "y = 3  (f_avg)",
           fill=MAROON_DARK, font=font("serif_bold", 30))

    # f(x) label near top of parabola
    fxy = to_px(2.4, 5.76)
    d.text((fxy[0] + 12, fxy[1] - 30), "f(x) = x²",
           fill=MAROON, font=font("serif_bold", 32))

    # Side card — same area note
    card_x = 1230
    d.rounded_rectangle([card_x, 270, W - 110, 740], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, 290), "Same area.",
           fill=MAROON, font=font("serif_bold", 44))
    d.text((card_x + 30, 360),
           "Under parabola:",
           fill=INK, font=font("sans_bold", 30))
    d.text((card_x + 30, 410), "∫₀³ x² dx  =  9",
           fill=INK, font=font("mono", 36))
    d.text((card_x + 30, 490), "Rectangle  3 × 3:",
           fill=INK, font=font("sans_bold", 30))
    d.text((card_x + 30, 540), "base · height  =  9",
           fill=INK, font=font("mono", 36))
    d.text((card_x + 30, 640), "→  height  =  f_avg",
           fill=MAROON, font=font("sans_bold", 32))
    d.text((card_x + 30, 685), "    =  3",
           fill=MAROON, font=font("mono", 36))


deck.custom("05_average_value_geometry", average_value_geometry)


# ─── 06 — MVT for integrals (definition) ─────────────────────────────────
deck.definition(
    "06_mvt_integrals",
    "Mean Value Theorem for Integrals.",
    "Some c in (a, b) where  f(c) = f_avg.",
    "If f is continuous on [a, b], the function actually achieves its "
    "average value somewhere strictly inside the interval.",
)


# ─── 07 — particle motion setup (equation) ───────────────────────────────
deck.equation(
    "07_particle_motion_setup",
    "Position  ↔  velocity  ↔  acceleration.",
    [
        ("s(t)   →  v(t) = s'(t)   →  a(t) = v'(t)",  INK,    "differentiate to step down"),
        ("",                                            INK,    None),
        ("v(t)  =  ∫  a(t)  dt",                       MAROON, "antidifferentiate to step up"),
        ("Δs    =  ∫ₐᵇ  v(t)  dt",                     MAROON, "change in position over [a, b]"),
    ],
)


# ─── 08 — displacement vs distance (compare) ─────────────────────────────
deck.compare(
    "08_displacement_vs_distance",
    "The Unit-8 distinction that costs the most AP points.",
    left={
        "label": "NET DISPLACEMENT",
        "color": MAROON,
        "lines": [
            "= ∫ₐᵇ  v(t)  dt",
            "",
            "Can be negative.",
            "Where the particle ENDED",
            "vs. where it started.",
        ],
        "footnote": "One signed integral.  Position change.",
    },
    right={
        "label": "TOTAL DISTANCE",
        "color": MAROON_DARK,
        "lines": [
            "= ∫ₐᵇ  |v(t)|  dt",
            "",
            "Never negative.",
            "How far the particle",
            "ACTUALLY traveled.",
        ],
        "footnote": "Split at every zero of v.  Sum the |pieces|.",
    },
)


# ─── 09 — particle example (equation) ────────────────────────────────────
deck.equation(
    "09_particle_example",
    "v(t) = t² − 4  on  [0, 3].   Net  vs.  total.",
    [
        ("∫₀³ (t² − 4) dt  =  [ t³/3 − 4t ]₀³",   INK,    "antiderivative, net displacement"),
        ("                =  9 − 12  =  −3",      MAROON, "net = −3   (ends 3 left of start)"),
        ("",                                       INK,    None),
        ("v = 0  at  t = 2.   Split:",            INK,    "for total distance, split at sign change"),
        ("∫₀² (4 − t²) dt  +  ∫₂³ (t² − 4) dt",   INK,    "absolute value piece by piece"),
        ("    16/3       +       7/3     =  23/3", MAROON, "total = 23/3   (≈ 7.67)"),
    ],
)


# ─── 10 — accumulation (definition) ──────────────────────────────────────
deck.definition(
    "10_accumulation",
    "Accumulation — integrate a rate.",
    "∫ₐᵇ  r(t) dt   =   total amount accumulated.",
    "If r(t) is a rate (gallons/min, people/hour, …) "
    "the definite integral gives total over [a, b].  "
    "Units:  (units of r) · (units of t).",
)


# ─── 11 — area between curves intro (custom: shaded region) ──────────────
def area_between_intro(img, d):
    d.text((110, 70), "Area between two curves.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158),
           "Top minus bottom.  Always.",
           fill=MUTED, font=font("sans", 36))

    # LEFT — graph with two curves and shaded region
    gx0, gy0 = 130, 240
    gw, gh = 1000, 720
    ax_y = gy0 + gh - 80
    origin_x = gx0 + 80

    # axes
    d.line([(gx0, ax_y), (gx0 + gw, ax_y)], fill=INK, width=3)
    d.line([(origin_x, gy0), (origin_x, ax_y + 30)], fill=INK, width=3)
    d.text((gx0 + gw - 30, ax_y + 12), "x", fill=INK, font=font("serif_ital", 28))
    d.text((origin_x + 12, gy0), "y", fill=INK, font=font("serif_ital", 28))

    # x from a=-0.5 to b=4.5;  curves: g(x) = top  =  -0.25(x-1.5)^2 + 5 ;  h(x) = bot = 0.4(x-1)^2 + 0.5
    x_min, x_max = -0.5, 4.5
    y_min, y_max = -0.5, 6.0
    sx = gw / (x_max - x_min)
    sy = (ax_y - gy0 - 20) / (y_max - y_min)

    def to_px(xv, yv):
        return (gx0 + (xv - x_min) * sx, ax_y - (yv - 0) * sy)

    # x-axis ticks
    for xv in [0, 1, 2, 3, 4]:
        px, _ = to_px(xv, 0)
        d.line([(px, ax_y - 6), (px, ax_y + 6)], fill=INK, width=2)
        d.text((px - 8, ax_y + 12), str(xv), fill=INK, font=font("sans", 24))
    # axis labels a, b
    a_px, _ = to_px(0.5, 0)
    b_px, _ = to_px(4.0, 0)
    d.line([(a_px, ax_y - 12), (a_px, ax_y + 16)], fill=MAROON_DARK, width=3)
    d.line([(b_px, ax_y - 12), (b_px, ax_y + 16)], fill=MAROON_DARK, width=3)
    d.text((a_px - 12, ax_y + 36), "a", fill=MAROON_DARK,
           font=font("serif_bold", 30))
    d.text((b_px - 10, ax_y + 36), "b", fill=MAROON_DARK,
           font=font("serif_bold", 30))

    # define top and bottom curves
    def top(xv):
        return -0.25 * (xv - 1.5) ** 2 + 5.0

    def bot(xv):
        return 0.4 * (xv - 1.0) ** 2 + 0.5

    # Curves only need to be plotted from a=0.5 to b=4.0 (they don't intersect in this window).
    a_val, b_val = 0.5, 4.0

    # Shaded region between curves on [a_val, b_val]
    region_pts = []
    xv = a_val
    while xv <= b_val + 0.001:
        region_pts.append(to_px(xv, top(xv)))
        xv += 0.04
    xv = b_val
    while xv >= a_val - 0.001:
        region_pts.append(to_px(xv, bot(xv)))
        xv -= 0.04
    d.polygon(region_pts, fill=deck.accent_light)

    # Hatch lines (subtle vertical stripes) for extra emphasis
    hatch_step = 28
    xv = a_val
    while xv <= b_val:
        top_pt = to_px(xv, top(xv))
        bot_pt = to_px(xv, bot(xv))
        d.line([top_pt, bot_pt], fill=deck.accent, width=1)
        xv += hatch_step / sx

    # Plot top curve (full range, slightly extended)
    pts_top = []
    xv = -0.3
    while xv <= 4.5:
        pts_top.append(to_px(xv, top(xv)))
        xv += 0.04
    for a_pt, b_pt in zip(pts_top[:-1], pts_top[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=6)

    # Plot bottom curve
    pts_bot = []
    xv = -0.3
    while xv <= 4.5:
        pts_bot.append(to_px(xv, bot(xv)))
        xv += 0.04
    for a_pt, b_pt in zip(pts_bot[:-1], pts_bot[1:]):
        d.line([a_pt, b_pt], fill=MAROON_DARK, width=6)

    # Vertical dashed boundary lines at x = a and x = b
    for xv in [a_val, b_val]:
        top_pt = to_px(xv, top(xv))
        bot_pt = to_px(xv, bot(xv))
        # dashed
        ys = top_pt[1]
        ye = bot_pt[1]
        step = 12
        y = ys
        while y < ye:
            d.line([(top_pt[0], y), (top_pt[0], min(y + step, ye))],
                   fill=MAROON_DARK, width=3)
            y += step + 6

    # Labels on curves
    top_lbl = to_px(3.6, top(3.6))
    d.text((top_lbl[0] + 14, top_lbl[1] - 30), "TOP:  y = f(x)",
           fill=MAROON, font=font("serif_bold", 30))
    bot_lbl = to_px(3.6, bot(3.6))
    d.text((bot_lbl[0] + 14, bot_lbl[1] + 10), "BOTTOM:  y = g(x)",
           fill=MAROON_DARK, font=font("serif_bold", 30))

    # RIGHT — formula card
    card_x = 1200
    d.rounded_rectangle([card_x, 270, W - 110, 740], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, 290), "Setup.",
           fill=MAROON, font=font("serif_bold", 46))
    d.text((card_x + 30, 380), "        ⌠ b",
           fill=INK, font=font("mono", 36))
    d.text((card_x + 30, 425), "A  =  │  ( f − g ) dx",
           fill=INK, font=font("mono", 36))
    d.text((card_x + 30, 470), "        ⌡ a",
           fill=INK, font=font("mono", 36))
    d.text((card_x + 30, 570),
           "TOP minus BOTTOM.",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((card_x + 30, 630),
           "Reverse it  →  sign flips.",
           fill=MUTED, font=font("sans", 30))
    d.text((card_x + 30, 680),
           "Magnitude right, setup wrong.",
           fill=MUTED, font=font("sans", 28))


deck.custom("11_area_between_intro", area_between_intro)


# ─── 12 — area example in x (equation) ───────────────────────────────────
deck.equation(
    "12_area_example_x",
    "Area between  y = x  and  y = x²  on  [0, 1].",
    [
        ("Intersections:  x = x²  →  x = 0, 1",   MUTED,  "find bounds first"),
        ("Test x = 0.5:  line = 0.5,  parab = 0.25", MUTED, "line is on top"),
        ("∫₀¹ (x − x²) dx  =  [ x²/2 − x³/3 ]₀¹",  INK,    "top minus bottom"),
        ("                 =  1/2 − 1/3  =  1/6",  MAROON, "answer"),
    ],
)


# ─── 13 — area in y (equation) ───────────────────────────────────────────
deck.equation(
    "13_area_in_y",
    "When curves are easier as  x = h(y)  →  integrate dy.",
    [
        ("x = y     and     x = y² − 2",                  INK,    "given relations"),
        ("Set equal:  y = y² − 2  →  (y−2)(y+1) = 0",    MUTED,  "y = −1, 2"),
        ("At y = 0:  line gives 0,  parab gives −2",     MUTED,  "line is on the RIGHT"),
        ("∫₋₁² ( y − (y² − 2) ) dy",                      INK,    "right minus left, dy"),
        ("       =  9 / 2",                               MAROON, "answer"),
    ],
)


# ─── 14 — pause ─────────────────────────────────────────────────────────
deck.pause(
    "14_pause1", "PAUSE  &  TRY",
    "Find the area enclosed between  y = x²  and  y = 2x.",
    "y = x²   vs   y = 2x",
    hint="Find intersections  →  identify top  →  integrate top minus bottom.  "
         "Pause.  Solve.  Press play when ready.",
)
deck.duplicate("14_pause1", "15_pause1_silence")


# ─── 16 — multi-crossing custom (sine & cosine on [0, 2π]) ───────────────
def multi_crossing(img, d):
    d.text((110, 70), "When curves cross more than twice.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 148),
           "Top and bottom SWAP at each crossing.  Split — don't integrate straight through.",
           fill=MUTED, font=font("sans", 30))

    # Plot region
    gx0, gy0 = 130, 230
    gw, gh = W - 260, 660
    ax_y = gy0 + gh // 2 + 40
    origin_x = gx0 + 30

    # x range: 0 to 2π;  y range: -1.4 to 1.4
    x_min, x_max = 0, 2 * math.pi
    y_min, y_max = -1.4, 1.4
    sx = gw / (x_max - x_min)
    sy = (gh / 2 - 30) / (y_max - 0)

    def to_px(xv, yv):
        return (gx0 + (xv - x_min) * sx, ax_y - yv * sy)

    # axes
    d.line([(gx0, ax_y), (gx0 + gw, ax_y)], fill=INK, width=3)
    d.line([(origin_x, gy0 + 20), (origin_x, gy0 + gh - 20)], fill=INK, width=3)

    # ticks at π/4, π/2, 3π/4, π, 5π/4, 3π/2, 7π/4, 2π
    xticks = [
        (math.pi / 4, "π/4"),
        (math.pi / 2, "π/2"),
        (3 * math.pi / 4, "3π/4"),
        (math.pi, "π"),
        (5 * math.pi / 4, "5π/4"),
        (3 * math.pi / 2, "3π/2"),
        (7 * math.pi / 4, "7π/4"),
        (2 * math.pi, "2π"),
    ]
    for xv, lbl in xticks:
        px, _ = to_px(xv, 0)
        d.line([(px, ax_y - 6), (px, ax_y + 6)], fill=INK, width=2)
        tw = d.textlength(lbl, font=font("sans", 22))
        d.text((px - tw / 2, ax_y + 12), lbl, fill=MUTED, font=font("sans", 22))

    # Crossings of sin and cos on [0, 2π]: π/4 and 5π/4.
    # That gives 3 sub-regions:  [0, π/4], [π/4, 5π/4], [5π/4, 2π].
    # On [0, π/4]:  cos > sin  →  top = cos, bottom = sin
    # On [π/4, 5π/4]: sin > cos  →  top = sin, bottom = cos
    # On [5π/4, 2π]:  cos > sin  →  top = cos, bottom = sin

    def shade_region(xa, xb, top_fn, bot_fn, fill_color):
        pts = []
        xv = xa
        while xv <= xb + 0.001:
            pts.append(to_px(xv, top_fn(xv)))
            xv += 0.02
        xv = xb
        while xv >= xa - 0.001:
            pts.append(to_px(xv, bot_fn(xv)))
            xv -= 0.02
        d.polygon(pts, fill=fill_color)

    shade_region(0, math.pi / 4, math.cos, math.sin, deck.accent_light)
    shade_region(math.pi / 4, 5 * math.pi / 4, math.sin, math.cos, deck.accent_light)
    shade_region(5 * math.pi / 4, 2 * math.pi, math.cos, math.sin, deck.accent_light)

    # Plot sin
    pts_sin = []
    xv = 0
    while xv <= 2 * math.pi:
        pts_sin.append(to_px(xv, math.sin(xv)))
        xv += 0.02
    for a_pt, b_pt in zip(pts_sin[:-1], pts_sin[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)

    # Plot cos
    pts_cos = []
    xv = 0
    while xv <= 2 * math.pi:
        pts_cos.append(to_px(xv, math.cos(xv)))
        xv += 0.02
    for a_pt, b_pt in zip(pts_cos[:-1], pts_cos[1:]):
        d.line([a_pt, b_pt], fill=MAROON_DARK, width=5)

    # Mark the crossings
    for xv in [math.pi / 4, 5 * math.pi / 4]:
        px, py = to_px(xv, math.sin(xv))
        d.ellipse([px - 10, py - 10, px + 10, py + 10], fill=deck.accent,
                  outline=MAROON_DARK, width=3)

    # Labels on curves
    sin_lbl = to_px(math.pi / 2 + 0.1, 0.95)
    d.text((sin_lbl[0] + 6, sin_lbl[1] - 35), "y = sin x",
           fill=MAROON, font=font("serif_bold", 26))
    cos_lbl = to_px(0.05, 1.0)
    d.text((cos_lbl[0] + 4, cos_lbl[1] - 40), "y = cos x",
           fill=MAROON_DARK, font=font("serif_bold", 26))

    # "TOP swaps" labels per region
    r1_x, _ = to_px(math.pi / 8, 0)
    d.text((r1_x - 36, ax_y - 70), "cos on top",
           fill=MAROON_DARK, font=font("sans_bold", 22))
    r2_x, _ = to_px(math.pi / 2 + math.pi / 4, 0)
    d.text((r2_x - 32, ax_y + 95), "sin on top",
           fill=MAROON, font=font("sans_bold", 22))
    r3_x, _ = to_px(3 * math.pi / 2 + math.pi / 4, 0)
    d.text((r3_x - 36, ax_y - 70), "cos on top",
           fill=MAROON_DARK, font=font("sans_bold", 22))

    # Bottom note
    d.rounded_rectangle([110, 920, W - 110, 1000], radius=18,
                        fill=deck.accent_light)
    centered(d, "Split at every crossing.  On each piece:  ∫ |top − bottom| dx.",
             font("sans_bold", 34), 940, MAROON_DARK)


deck.custom("16_multi_crossing", multi_crossing)


# ─── 17 — compare: displacement vs distance trap (compare) ──────────────
deck.compare(
    "17_compare_trap",
    "AP trap — calling  ∫ v  the 'total distance.'",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "Asked for total distance.",
            "Computed  ∫₀ᵀ  v(t)  dt.",
            "Reported the signed result.",
            "If v changed sign — answer is OFF.",
            "Negative and positive parts cancel.",
        ],
        "footnote": "Same setup as displacement.  Misread the question.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "Find all zeros of  v(t)  on [0, T].",
            "Split the integral at each zero.",
            "Take absolute value on each piece.",
            "Sum the magnitudes.",
            "→  total distance traveled.",
        ],
        "footnote": "Equivalently  ∫₀ᵀ  |v(t)|  dt.  Slow down to read the question.",
    },
)


# ─── 18 — recap ─────────────────────────────────────────────────────────
deck.recap(
    "18_recap", "Recap.",
    [
        "f_avg  =  (1/(b−a)) · ∫ₐᵇ  f(x) dx.   DIVIDE.",
        "MVT for Integrals — f hits its average somewhere in (a, b).",
        "Net displacement  =  ∫ v dt.   Total distance  =  ∫ |v| dt.",
        "Area between (in x):  ∫ₐᵇ (top − bottom) dx.",
        "Area between (in y):  ∫꜀ᵈ (right − left) dy.",
        "More than two crossings:  split at each  →  |top − bottom| per piece.",
    ],
    assignment=[
        "GIIS Unit 8a Set  —  5 area problems  +  3 particle-motion FRQs.",
        "Submit through the dashboard.  Advisor reviews within 48 hours.",
    ],
)


# ─── 19 — path ──────────────────────────────────────────────────────────
deck.path(
    "19_path",
    items=[
        ("✓",  "Watch this lesson",            "(done!)"),
        ("1.", "OpenStax Calculus Vol 2",      "Read sections 6.1 (Average Value) and 6.2 (Area Between Curves)"),
        ("2.", "Khan Academy practice",        "AP Calc AB · Unit 8 — Particle Motion & Area Between Curves"),
        ("3.", "Assignment in dashboard",      "GIIS Unit 8a Set — 5 area + 3 particle-motion FRQs"),
        ("4.", "Advisor check-in",             "Book 15 min if displacement vs. distance still feels fuzzy"),
    ],
    next_text="Next up:  Module 11 — Volumes: Cross Sections, Discs & Washers.",
)


print("AP Calc AB Module 10 slides built.")

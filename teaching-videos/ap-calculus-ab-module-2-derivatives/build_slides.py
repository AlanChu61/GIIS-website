"""AP Calculus AB · Module 2 — Differentiation: Definition and Fundamental Properties.

Built on slide_kit (math theme = gold + cream).
Custom slides:
- 02_hook    : speedometer + secant→tangent
- 03_overview: custom 3-step game plan (uses slide_kit overview)
- 07_estimating: data table + symmetric difference quotient
- 08_diff_implies_cont: 2x2 grid of differentiability failure modes
- 10_sum_and_table: 2-column custom slide
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
deck = Deck(course="AP Calculus AB", module_num=2, output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 2 — Differentiation: Definition & Fundamental Properties",
    "~10 minutes  ·  From limits to derivatives",
)


# ─── 02 — hook (custom: speedometer + secant→tangent) ────────────────────
def hook(img, d):
    d.text((110, 80), "Your speedometer is", fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "solving a limit problem.", fill=MAROON, font=font("serif_bold", 70))

    # LEFT: Speedometer
    cx, cy, r = 480, 580, 200
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=MAROON, width=8, fill=deck.card_bg)
    d.ellipse([cx - r + 30, cy - r + 30, cx + r - 30, cy + r - 30], outline=MUTED, width=3)
    for i in range(11):
        ang = math.radians(180 + i * 18)
        x1 = cx + (r - 15) * math.cos(ang)
        y1 = cy + (r - 15) * math.sin(ang)
        x2 = cx + (r - 40) * math.cos(ang)
        y2 = cy + (r - 40) * math.sin(ang)
        d.line([(x1, y1), (x2, y2)], fill=INK, width=4)
    # needle at ~60 mph (6th tick)
    needle_ang = math.radians(180 + 6 * 18)
    nx = cx + (r - 60) * math.cos(needle_ang)
    ny = cy + (r - 60) * math.sin(needle_ang)
    d.line([(cx, cy), (nx, ny)], fill=deck.accent, width=10)
    d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=MAROON)
    d.text((cx - 70, cy + 50), "60 mph", fill=MAROON_DARK, font=font("sans_bold", 42))
    d.text((cx - 110, cy + 110), "right now, this instant", fill=MUTED, font=font("sans", 26))

    # RIGHT: Secant → tangent on a position-time curve
    gx0, gy0 = 880, 340
    gw, gh = 880, 460
    # axes
    d.line([(gx0, gy0 + gh), (gx0 + gw, gy0 + gh)], fill=INK, width=3)
    d.line([(gx0, gy0), (gx0, gy0 + gh)], fill=INK, width=3)
    d.text((gx0 + gw - 30, gy0 + gh + 10), "t", fill=INK, font=font("serif_ital", 32))
    d.text((gx0 - 40, gy0 - 10), "s", fill=INK, font=font("serif_ital", 32))
    d.text((gx0 + 10, gy0 + gh - 30), "position vs. time", fill=MUTED, font=font("sans", 22))

    # the curve: simple parabola-ish position function
    pts = []
    for k in range(0, gw - 20, 6):
        xc = gx0 + 20 + k
        # s(t) = 0.0006 * (k)^2 like rising curve
        yc = gy0 + gh - 30 - int(0.00075 * (k ** 2))
        if yc < gy0 + 20:
            yc = gy0 + 20
        pts.append((xc, yc))
    for a_pt, b_pt in zip(pts[:-1], pts[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)

    # Point P (tangent point) at k=500
    def curve_pt(k):
        xc = gx0 + 20 + k
        yc = gy0 + gh - 30 - int(0.00075 * (k ** 2))
        return (xc, yc)

    P = curve_pt(500)
    # Three secant lines shrinking in
    secant_ks = [(500, 800), (500, 700), (500, 620)]
    for i, (k1, k2) in enumerate(secant_ks):
        A = curve_pt(k1)
        B = curve_pt(k2)
        # extend line a bit
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        sx = A[0] - int(dx * 0.3)
        sy = A[1] - int(dy * 0.3)
        ex = B[0] + int(dx * 0.4)
        ey = B[1] + int(dy * 0.4)
        # lighten as they shrink (i=2 is the tightest)
        shade = (180, 158, 220) if False else deck.accent_light
        d.line([(sx, sy), (ex, ey)], fill=deck.accent_light, width=3)
        # small open dot at B
        d.ellipse([B[0] - 7, B[1] - 7, B[0] + 7, B[1] + 7],
                  outline=deck.accent, width=3, fill=deck.bg)

    # Tangent line at P (slope ~ derivative at k=500)
    # slope of s(k) = 0.00075 * k^2 → ds/dk = 0.0015 * k = 0.75 at k=500
    slope = 0.0015 * 500
    tx_l, ty_l = P[0] - 220, P[1] + int(220 * slope)
    tx_r, ty_r = P[0] + 220, P[1] - int(220 * slope)
    d.line([(tx_l, ty_l), (tx_r, ty_r)], fill=MAROON_DARK, width=5)

    # P marker (filled)
    d.ellipse([P[0] - 10, P[1] - 10, P[0] + 10, P[1] + 10], fill=MAROON_DARK)
    d.text((P[0] + 16, P[1] - 8), "P", fill=MAROON_DARK, font=font("serif_bold", 32))
    d.text((P[0] + 18, P[1] + 22), "tangent", fill=MAROON_DARK, font=font("sans_bold", 22))

    # Δt label
    d.text((gx0 + 540, gy0 + gh + 38), "Δt → 0", fill=deck.accent, font=font("mono", 32))

    # Caption strip
    d.rounded_rectangle([110, 880, W - 110, 1000], radius=20, fill=deck.accent_light)
    centered(d, "Average speed over a tiny window  →  shrink the window to zero.",
             font("sans_bold", 32), 895, MAROON_DARK)
    centered(d, "That limit has a name. It's called the derivative.",
             font("serif_bold", 34), 940, MAROON_DARK)


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Average rate → instantaneous rate (it's a limit).",
        "The rule toolkit: power, product, quotient, trig / exp / log.",
        "Differentiability vs continuity — and the four failure modes.",
    ],
    footnote="Module 1 limits become Module 2 derivatives — same engine, new gear.",
)


# ─── 04 — avg rate of change (definition) ────────────────────────────────
deck.definition(
    "04_avg_rate", "Average rate of change.",
    "(f(b) − f(a)) / (b − a)",
    "Slope of the secant line through (a, f(a)) and (b, f(b)).",
)


# ─── 05 — instantaneous rate (custom: both forms + tangent line) ─────────
def inst_rate(img, d):
    d.text((110, 80), "Instantaneous rate of change at  x = a.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Shrink the secant interval to zero — and you get the tangent slope.",
           fill=MUTED, font=font("sans", 34))

    # Two limit forms in side-by-side cards
    card_y = 250
    card_h = 320
    f_eq = font("mono", 50)
    f_lbl = font("sans_bold", 30)
    f_note = font("sans", 26)

    # LEFT card — h-form
    d.rounded_rectangle([110, card_y, 940, card_y + card_h], radius=24,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((140, card_y + 25), "h-form", fill=MAROON, font=f_lbl)
    centered_x_l = (110 + 940) // 2
    line1 = "f'(a) = lim"
    line2 = "  h→0"
    line3 = "f(a+h) − f(a)"
    line4 = "─────────"
    line5 = "      h"
    d.text((140, card_y + 80), "f'(a)  =  lim", fill=INK, font=font("mono", 46))
    d.text((420, card_y + 130), "h → 0", fill=MAROON, font=font("mono", 30))
    d.text((520, card_y + 90), "f(a + h) − f(a)", fill=INK, font=font("mono", 40))
    d.line([(520, card_y + 145), (520 + 430, card_y + 145)], fill=INK, width=3)
    d.text((680, card_y + 155), "h", fill=INK, font=font("mono", 40))
    d.text((140, card_y + 240), "Plug in 'h = small'. Standard form.",
           fill=MUTED, font=f_note)

    # RIGHT card — point form
    d.rounded_rectangle([980, card_y, 1810, card_y + card_h], radius=24,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((1010, card_y + 25), "point form", fill=MAROON, font=f_lbl)
    d.text((1010, card_y + 80), "f'(a)  =  lim", fill=INK, font=font("mono", 46))
    d.text((1290, card_y + 130), "x → a", fill=MAROON, font=font("mono", 30))
    d.text((1390, card_y + 90), "f(x) − f(a)", fill=INK, font=font("mono", 40))
    d.line([(1390, card_y + 145), (1390 + 360, card_y + 145)], fill=INK, width=3)
    d.text((1520, card_y + 155), "x − a", fill=INK, font=font("mono", 40))
    d.text((1010, card_y + 240), "Often easier when x = a directly.",
           fill=MUTED, font=f_note)

    # Caption — equivalence
    centered(d, "Both forms are equivalent. Use whichever's easier.",
             font("sans_bold", 36), 620, MAROON_DARK)

    # Tangent line equation strip
    d.rounded_rectangle([110, 730, W - 110, 880], radius=20, fill=deck.accent_light)
    centered(d, "Tangent line at  x = a:",
             font("sans_bold", 34), 750, MAROON_DARK)
    centered(d, "y  =  f(a)  +  f'(a) · (x − a)",
             font("mono", 60), 800, MAROON_DARK)

    d.text((110, 910), "f'(a)  =  the instantaneous rate of change at a  =  slope of the tangent line.",
           fill=deck.accent, font=font("sans_bold", 32))


deck.custom("05_inst_rate", inst_rate)


# ─── 06 — notation (definition card) ─────────────────────────────────────
def notation(img, d):
    d.text((110, 80), "Notation — four ways to say the same thing.",
           fill=MAROON, font=font("serif_bold", 60))

    # 2x2 grid of equivalent notations
    f_n = font("mono", 80)
    notations = [
        ("f'(x)",       "function-prime"),
        ("dy/dx",       "the ratio form"),
        ("d/dx [f(x)]", "operator form"),
        ("y'",          "shorthand"),
    ]
    for i, (notn, sub) in enumerate(notations):
        row = i // 2
        col = i % 2
        x0 = 140 + col * 880
        y0 = 240 + row * 200
        d.rounded_rectangle([x0, y0, x0 + 800, y0 + 160], radius=20,
                            outline=MAROON, width=3, fill=deck.card_bg)
        d.text((x0 + 40, y0 + 25), notn, fill=INK, font=f_n)
        d.text((x0 + 40, y0 + 115), sub, fill=MUTED, font=font("sans", 28))

    # Bottom rule card
    d.rounded_rectangle([110, 720, W - 110, 950], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    centered(d, "dy/dx is the limit of  Δy / Δx.",
             font("sans_bold", 38), 740, MAROON_DARK)
    centered(d, "Not literally a fraction of two numbers —",
             font("sans", 32), 800, MAROON_DARK)
    centered(d, "but because it came from one, it inherits the algebra of fractions.",
             font("sans", 32), 845, MAROON_DARK)
    centered(d, "That's why chain rule and u-substitution work. (Coming in Module 3.)",
             font("sans_bold", 30), 900, MAROON_DARK)


deck.custom("06_notation", notation)


# ─── 07 — estimating from data (custom) ──────────────────────────────────
def estimating(img, d):
    d.text((110, 80), "Estimating f'(a) from data.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "When you only have a table of values — not a formula.",
           fill=MUTED, font=font("sans", 32))

    # Data table
    table_y = 240
    cell_h = 70
    cell_w = 180
    table_x = 140
    headers = ["x", "1.9", "1.99", "2.01", "2.1"]
    values  = ["f(x)", "8.41", "8.9401", "9.0601", "9.61"]

    # header row
    for i, h in enumerate(headers):
        x0 = table_x + i * cell_w
        d.rectangle([x0, table_y, x0 + cell_w, table_y + cell_h],
                    fill=MAROON, outline=MAROON)
        tw = d.textlength(h, font=font("sans_bold", 32))
        d.text((x0 + (cell_w - tw) / 2, table_y + 18), h,
               fill=deck.bg, font=font("sans_bold", 32))
    # value row
    for i, v in enumerate(values):
        x0 = table_x + i * cell_w
        y0 = table_y + cell_h
        d.rectangle([x0, y0, x0 + cell_w, y0 + cell_h],
                    fill=deck.card_bg, outline=MAROON, width=2)
        tw = d.textlength(v, font=font("mono", 30))
        d.text((x0 + (cell_w - tw) / 2, y0 + 20), v,
               fill=INK, font=font("mono", 30))

    # Highlight the 1.99 and 2.01 cells with an accent box (they're the symmetric pair)
    for i in [2, 3]:
        x0 = table_x + i * cell_w
        y0 = table_y + cell_h
        d.rectangle([x0, y0, x0 + cell_w, y0 + cell_h],
                    outline=deck.accent, width=5)

    # Symmetric difference quotient formula
    formula_y = 470
    centered(d, "Symmetric difference quotient at  x = 2:",
             font("sans_bold", 34), formula_y, MAROON_DARK)

    d.text((310, formula_y + 60), "f'(2)  ≈", fill=INK, font=font("mono", 44))
    d.text((620, formula_y + 60), "f(2.01) − f(1.99)", fill=INK, font=font("mono", 40))
    d.line([(620, formula_y + 115), (620 + 540, formula_y + 115)], fill=INK, width=3)
    d.text((780, formula_y + 122), "0.02", fill=INK, font=font("mono", 40))
    d.text((1220, formula_y + 60), "=", fill=INK, font=font("mono", 44))
    d.text((1280, formula_y + 60), "9.0601 − 8.9401", fill=MUTED, font=font("mono", 32))
    d.line([(1280, formula_y + 110), (1280 + 380, formula_y + 110)], fill=MUTED, width=2)
    d.text((1420, formula_y + 118), "0.02", fill=MUTED, font=font("mono", 32))

    # Result
    centered(d, "≈  6.00", font("mono", 56), formula_y + 200, MAROON)

    # Footer notes
    d.rounded_rectangle([110, 830, W - 110, 980], radius=20,
                        outline=MAROON, width=3, fill=deck.accent_light)
    centered(d, "Approximation from data — NOT the definition. The true derivative is still a limit.",
             font("sans_bold", 28), 848, MAROON_DARK)
    centered(d, "Symmetric form averages forward and backward secants — tighter estimate.",
             font("sans", 28), 892, MAROON_DARK)
    centered(d, "Units of  f'(a)  =  (units of f) / (units of x).",
             font("sans_bold", 28), 935, MAROON_DARK)


deck.custom("07_estimating", estimating)


# ─── 08 — diff implies cont (custom: 4 failure-mode mini-graphs) ─────────
def diff_implies_cont(img, d):
    d.text((110, 70), "Differentiable  ⇒  continuous.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 145), "Continuous  ⇏  differentiable.  Four ways it can fail:",
           fill=MAROON_DARK, font=font("sans", 34))

    # 2x2 grid of failure modes
    panel_w, panel_h = 800, 360
    gap = 40
    top_y = 230
    failures = [
        ("CORNER",          "y = |x|  at  x = 0",          "corner"),
        ("CUSP",            "y = x^(2/3)  at  x = 0",      "cusp"),
        ("VERTICAL TANGENT", "y = x^(1/3)  at  x = 0",      "vtan"),
        ("DISCONTINUITY",   "jump / removable / infinite", "disc"),
    ]
    for i, (title, sub, kind) in enumerate(failures):
        row = i // 2
        col = i % 2
        x0 = 130 + col * (panel_w + gap)
        y0 = top_y + row * (panel_h + 30)
        d.rounded_rectangle([x0, y0, x0 + panel_w, y0 + panel_h],
                            radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        d.text((x0 + 30, y0 + 20), title, fill=MAROON, font=font("sans_bold", 32))
        d.text((x0 + 30, y0 + 60), sub, fill=MUTED, font=font("mono", 26))

        # mini axes
        ax_y = y0 + panel_h - 60
        ax_x = x0 + panel_w // 2  # vertical axis at center
        d.line([(x0 + 60, ax_y), (x0 + panel_w - 30, ax_y)], fill=MUTED, width=2)
        d.line([(ax_x, y0 + 110), (ax_x, ax_y + 20)], fill=MUTED, width=2)

        if kind == "corner":
            # y = |x| — two diagonal lines meeting at origin
            x_left_end = x0 + 80
            y_left_end = ax_y - (ax_x - x_left_end)
            d.line([(x_left_end, y_left_end), (ax_x, ax_y)], fill=deck.accent, width=5)
            x_right_end = x0 + panel_w - 50
            y_right_end = ax_y - (x_right_end - ax_x)
            # clip so it doesn't blow past panel
            if y_right_end < y0 + 110:
                y_right_end = y0 + 110
            d.line([(ax_x, ax_y), (x_right_end, y_right_end)], fill=deck.accent, width=5)
            # red dot at the corner
            d.ellipse([ax_x - 9, ax_y - 9, ax_x + 9, ax_y + 9],
                      fill=RED, outline=RED)

        elif kind == "cusp":
            # y = x^(2/3) — symmetric, comes in steep on both sides to (0,0)
            for k in range(1, 100):
                xc_left = ax_x - 4 * k
                xc_right = ax_x + 4 * k
                if xc_left < x0 + 60 or xc_right > x0 + panel_w - 30:
                    break
                # y = (4k/scale)^(2/3) scaled
                yval = int(((4 * k) ** (2 / 3)) * 12)
                ypos = ax_y - yval
                if ypos < y0 + 110:
                    ypos = y0 + 110
                d.ellipse([xc_left - 2, ypos - 2, xc_left + 2, ypos + 2], fill=deck.accent)
                d.ellipse([xc_right - 2, ypos - 2, xc_right + 2, ypos + 2], fill=deck.accent)
            d.ellipse([ax_x - 9, ax_y - 9, ax_x + 9, ax_y + 9],
                      fill=RED, outline=RED)

        elif kind == "vtan":
            # y = x^(1/3) — passes through origin with vertical tangent
            for k in range(1, 100):
                xc_right = ax_x + 4 * k
                xc_left = ax_x - 4 * k
                if xc_right > x0 + panel_w - 30 or xc_left < x0 + 60:
                    break
                yval = int(((4 * k) ** (1 / 3)) * 26)
                yp_up = ax_y - yval
                yp_dn = ax_y + yval
                if yp_up < y0 + 110:
                    yp_up = y0 + 110
                if yp_dn > ax_y + (panel_h - (ax_y - y0)) - 20:
                    continue
                d.ellipse([xc_right - 2, yp_up - 2, xc_right + 2, yp_up + 2], fill=deck.accent)
                d.ellipse([xc_left - 2, yp_dn - 2, xc_left + 2, yp_dn + 2], fill=deck.accent)
            d.ellipse([ax_x - 9, ax_y - 9, ax_x + 9, ax_y + 9],
                      fill=RED, outline=RED)
            # mark tangent direction with a vertical accent line near origin
            d.line([(ax_x, ax_y - 70), (ax_x, ax_y + 50)], fill=RED, width=2)

        else:  # disc — jump discontinuity
            # left segment + open dot, right segment + closed dot
            d.line([(x0 + 60, ax_y - 50), (ax_x - 4, ax_y - 50)],
                   fill=deck.accent, width=5)
            d.ellipse([ax_x - 12, ax_y - 58, ax_x + 4, ax_y - 42],
                      outline=deck.accent, width=4, fill=deck.card_bg)
            d.line([(ax_x + 4, ax_y - 130), (x0 + panel_w - 50, ax_y - 130)],
                   fill=deck.accent, width=5)
            d.ellipse([ax_x - 4, ax_y - 138, ax_x + 12, ax_y - 122],
                      fill=deck.accent)
            d.text((ax_x - 30, ax_y - 9), "•", fill=RED, font=font("sans_bold", 60))


deck.custom("08_diff_implies_cont", diff_implies_cont)


# ─── 09 — power rule ─────────────────────────────────────────────────────
deck.equation(
    "09_power_rule", "Power Rule  ·  d/dx[x^n] = n · x^(n−1)",
    [
        ("d/dx[x⁵]      =  5x⁴",         INK,    "exponent down, drop by 1"),
        ("d/dx[x^(1/2)]  =  (1/2)x^(−1/2)", MUTED, "works for any real n"),
        ("d/dx[1/x]     =  −1/x²",       MAROON, "rewrite as x⁻¹ first"),
        ("d/dx[c] = 0    ·    d/dx[c·f] = c · f'", INK, "constant + constant-multiple"),
    ],
)


# ─── 10 — sum rule + derivative table (custom 2-column) ──────────────────
def sum_and_table(img, d):
    d.text((110, 80), "Sum rule  +  the must-memorize table.",
           fill=MAROON, font=font("serif_bold", 60))

    # LEFT — sum/difference rule
    d.rounded_rectangle([110, 240, 880, 820], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((140, 270), "Sum / difference rule", fill=MAROON, font=font("serif_bold", 40))
    d.text((140, 360), "(f ± g)'  =  f'  ±  g'", fill=INK, font=font("mono", 56))
    d.text((140, 470), "Derivatives distribute over", fill=MUTED, font=font("sans", 30))
    d.text((140, 510), "addition and subtraction.", fill=MUTED, font=font("sans", 30))
    d.text((140, 600), "Example:", fill=MAROON, font=font("sans_bold", 34))
    d.text((140, 660), "(x³ + sin x)'", fill=INK, font=font("mono", 42))
    d.text((140, 720), "= 3x² + cos x", fill=MAROON, font=font("mono", 42))

    # RIGHT — derivative table
    d.rounded_rectangle([940, 240, W - 110, 820], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((970, 270), "Memorize cold", fill=MAROON, font=font("serif_bold", 40))
    rows = [
        ("d/dx[sin x]  =   cos x",      INK),
        ("d/dx[cos x]  =  −sin x",      MAROON),
        ("d/dx[eˣ]     =   eˣ",          INK),
        ("d/dx[ln x]   =   1/x",        INK),
    ]
    y = 360
    for txt, color in rows:
        d.text((970, y), txt, fill=color, font=font("mono", 38))
        y += 80
    d.text((970, 740), "Star the negative on cosine.", fill=deck.accent, font=font("sans_bold", 30))
    d.text((970, 780), "ln x  defined for  x > 0.", fill=MUTED, font=font("sans", 26))

    # Bottom strip
    d.rounded_rectangle([110, 850, W - 110, 960], radius=20, fill=deck.accent_light)
    centered(d, "Most common AP slip: forgetting the minus sign on  d/dx[cos x].",
             font("sans_bold", 32), 880, MAROON_DARK)


deck.custom("10_sum_and_table", sum_and_table)


# ─── 11 — product rule ───────────────────────────────────────────────────
deck.equation(
    "11_product_rule", "Product Rule  ·  (f·g)' = f'·g + f·g'",
    [
        ("f = x²,        f' = 2x",                 MUTED,  "differentiate each piece"),
        ("g = sin x,     g' = cos x",              MUTED,  None),
        ("(x² · sin x)' = 2x · sin x + x² · cos x", MAROON, "both terms — not just f'·g'"),
    ],
)


# ─── 12 — pause-and-try ──────────────────────────────────────────────────
deck.pause(
    "12_pause1", "PAUSE  &  TRY",
    "Find  d/dx[ x · cos x ]  using the product rule:",
    "x · cos x",
    hint="Set up your f, g, f', g'.  Pause. Solve. Press play when ready.",
)

# ─── 13 — pause silence (duplicate of 12) ────────────────────────────────
deck.duplicate("12_pause1", "13_pause1_silence")


# ─── 14 — quotient rule ──────────────────────────────────────────────────
deck.equation(
    "14_quotient_rule", "Quotient Rule  ·  (f/g)' = (f'·g − f·g') / g²",
    [
        ("d/dx[ sin x / x ]",                       INK,    "f = sin x, g = x"),
        ("=  (cos x · x  −  sin x · 1) / x²",       MUTED,  "f'·g  −  f·g'"),
        ("=  (x cos x  −  sin x) / x²",             MAROON, "d-high · low  −  high · d-low,  over low²"),
    ],
)


# ─── 15 — compare (quotient-rule sign trap) ──────────────────────────────
deck.compare(
    "15_compare",
    "Common trap — quotient rule order.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "(f/g)'  =  (f · g'  −  f' · g) / g²",
            "Numerator terms swapped.",
            "Sign of the answer flips.",
            "AP loses you a point.",
        ],
        "footnote": "If you write  f · g'  first, you flipped it.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "(f/g)'  =  (f' · g  −  f · g') / g²",
            "f' (derivative of TOP) first.",
            "Then  minus  f · g'.",
            "All over the bottom squared.",
        ],
        "footnote": "'d-high times low  minus  high times d-low,  over low².'",
    },
)


# ─── 16 — other trig derivatives ─────────────────────────────────────────
deck.equation(
    "16_other_trig", "The other four trig derivatives.",
    [
        ("d/dx[tan x]   =    sec² x",              INK,    None),
        ("d/dx[cot x]   =  − csc² x",              MAROON, "cot — minus"),
        ("d/dx[sec x]   =    sec x · tan x",       INK,    None),
        ("d/dx[csc x]   =  − csc x · cot x",       MAROON, "csc — minus"),
    ],
)


# ─── 17 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "17_recap", "Recap.",
    [
        "Derivative  =  limit of the difference quotient.",
        "Two forms: h-form and point-form — use whichever's easier.",
        "Tangent line at a:  y = f(a) + f'(a)·(x − a).",
        "Differentiable ⇒ continuous (one way).  Four failure modes.",
        "Toolkit: power, sum, product, quotient.  Memorize trig / exp / log.",
    ],
)


# ─── 18 — path ───────────────────────────────────────────────────────────
deck.path(
    "18_path",
    items=[
        ("✓",  "Watch this lesson",          "(done!)"),
        ("1.", "OpenStax Calculus Vol 1",    "Read chapters 3.1 – 3.6"),
        ("2.", "Khan Academy practice",      "AP Calc AB · Derivatives 1 unit"),
        ("3.", "Assignment in dashboard",    "20 mixed product / quotient problems"),
        ("4.", "Advisor check-in",           "Book if differentiability rules feel fuzzy"),
    ],
    next_text="Next up:  Module 3 — Composite, Implicit & Inverse Functions (chain rule).",
)


print("AP Calc AB Module 2 slides built.")

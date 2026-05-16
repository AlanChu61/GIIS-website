"""AP Calculus AB · Module 7 — Riemann Sums and the Fundamental Theorem of Calculus.

Built on slide_kit (math theme = gold + cream).
Custom slides:
- 02_hook                   : velocity-vs-time curve with shaded area = distance
- 05_riemann_sums           : 2x2 mini-grid showing L, R, M, T rectangles under a curve
- 07_definite_integral      : Σ collapsing into ∫ — sum-to-integral transition diagram
- 13_ftc_part1              : FTC Part 1 statement with accumulation-function visual + chain-rule extension
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
deck = Deck(course="AP Calculus AB", module_num=7,
            output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 7 — Riemann Sums and the Fundamental Theorem of Calculus",
    "~9 minutes  ·  Unit 6a  ·  CHA 6.1 · LIM 6.2-6.3 · FUN 6.4-6.7",
)


# ─── 02 — hook (custom: velocity-time curve with shaded distance area) ───
def hook(img, d):
    d.text((110, 80), "Area under the rate  =  total amount.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168),
           "Velocity vs time.  The shaded area is the distance traveled.",
           fill=MUTED, font=font("sans", 34))

    # Graph area
    gx0, gy0 = 200, 260
    gw, gh = 1520, 580
    ax_y = gy0 + gh - 60
    ax_x = gx0 + 40

    # axes
    d.line([(ax_x, gy0 + 40), (ax_x, ax_y)], fill=INK, width=3)
    d.line([(ax_x, ax_y), (gx0 + gw - 30, ax_y)], fill=INK, width=3)

    # axis labels
    d.text((gx0 + gw - 80, ax_y + 12), "t  (sec)", fill=INK, font=font("serif_ital", 30))
    d.text((ax_x - 60, gy0 + 5), "v(t)  (m/s)", fill=INK, font=font("serif_ital", 30))

    # velocity curve: v(t) = 8 + 3t - 0.4 t^2 on t ∈ [0, 7] — rising then leveling
    # Scale: t in [0, 7] across gw - 80;  v in [0, 18] across gh - 80
    t_lo, t_hi = 0.0, 7.0
    v_lo, v_hi = 0.0, 18.0
    plot_w = gw - 100
    plot_h = gh - 100
    sx = plot_w / (t_hi - t_lo)
    sy = plot_h / (v_hi - v_lo)

    def to_px(t, v):
        return (ax_x + (t - t_lo) * sx, ax_y - (v - v_lo) * sy)

    def vfn(t):
        return 8 + 3 * t - 0.4 * t * t

    # x-axis ticks
    for tv in range(0, 8):
        px, _ = to_px(tv, 0)
        d.line([(px, ax_y - 6), (px, ax_y + 6)], fill=INK, width=2)
        lbl = str(tv)
        tw = d.textlength(lbl, font=font("sans", 22))
        d.text((px - tw / 2, ax_y + 12), lbl, fill=INK, font=font("sans", 22))
    # y-axis ticks
    for yv in [5, 10, 15]:
        _, py = to_px(0, yv)
        d.line([(ax_x - 6, py), (ax_x + 6, py)], fill=INK, width=2)
        d.text((ax_x - 50, py - 14), str(yv), fill=INK, font=font("sans", 22))

    # shaded area under curve from t = 0.5 to t = 5.5
    t_a, t_b = 0.5, 5.5
    poly_pts = []
    poly_pts.append(to_px(t_a, 0))
    t = t_a
    while t <= t_b:
        poly_pts.append(to_px(t, vfn(t)))
        t += 0.05
    poly_pts.append(to_px(t_b, vfn(t_b)))
    poly_pts.append(to_px(t_b, 0))
    d.polygon(poly_pts, fill=deck.accent_light)

    # curve
    curve_pts = []
    t = t_lo
    while t <= t_hi:
        curve_pts.append(to_px(t, vfn(t)))
        t += 0.04
    for a_pt, b_pt in zip(curve_pts[:-1], curve_pts[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=6)

    # bound markers (vertical dashed-ish lines)
    pa = to_px(t_a, vfn(t_a))
    pb = to_px(t_b, vfn(t_b))
    pa_base = to_px(t_a, 0)
    pb_base = to_px(t_b, 0)
    d.line([pa_base, pa], fill=MAROON_DARK, width=3)
    d.line([pb_base, pb], fill=MAROON_DARK, width=3)
    # bound labels
    d.text((pa_base[0] - 14, ax_y + 36), "a", fill=MAROON_DARK, font=font("serif_bold_ital" if False else "serif_ital", 30))
    d.text((pb_base[0] - 14, ax_y + 36), "b", fill=MAROON_DARK, font=font("serif_ital", 30))

    # "DISTANCE" label centered in the shaded region
    mid_t = (t_a + t_b) / 2
    mid_px, mid_py_curve = to_px(mid_t, vfn(mid_t) / 2)
    d.text((mid_px - 95, mid_py_curve - 20), "DISTANCE",
           fill=MAROON_DARK, font=font("serif_bold", 44))
    d.text((mid_px - 130, mid_py_curve + 30),
           "= area under v(t)",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # integral expression label, top-right of graph
    d.text((gx0 + gw - 420, gy0 + 60),
           "∫  v(t) dt  =  distance",
           fill=MAROON, font=font("mono", 38))
    d.text((gx0 + gw - 410, gy0 + 110),
           "from  a  to  b",
           fill=MUTED, font=font("sans", 26))

    # closing strip
    d.rounded_rectangle([110, 880, W - 110, 1000], radius=20,
                        fill=deck.accent_light)
    centered(d, "Integration is accumulation.",
             font("serif_bold", 38), 895, MAROON_DARK)
    centered(d, "Rate × time.  Today we make it precise.",
             font("sans_bold", 32), 945, MAROON_DARK)


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Riemann sums — chop the area into rectangles.",
        "Take the limit — the sum becomes the definite integral.",
        "Fundamental Theorem of Calculus — both parts. The bridge.",
    ],
    footnote="Unit 6 is the highest-weighted unit on the AP exam.  It earns its weight today.",
)


# ─── 04 — accumulation idea (definition card) ────────────────────────────
deck.definition(
    "04_accumulation_idea", "Integration  =  accumulation.",
    "rate  ×  time  =  total amount",
    "If  f(t)  is a rate, then  ∫ f(t) dt  from  a  to  b  is the total accumulated change.",
)


# ─── 05 — Riemann sums (custom: 2x2 grid L / R / M / T) ──────────────────
def riemann_sums(img, d):
    d.text((110, 70), "Four ways to approximate the area.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 148),
           "Slice  [a, b]  into  n  sub-intervals.   Width  Δx = (b − a) / n.",
           fill=MUTED, font=font("sans", 32))

    # 2x2 grid
    panel_w = 800
    panel_h = 360
    gap_x = 40
    gap_y = 30
    top_y = 230

    panels = [
        ("LEFT  endpoints",     "L",  130, top_y),
        ("RIGHT  endpoints",    "R",  130 + panel_w + gap_x, top_y),
        ("MIDPOINT",            "M",  130, top_y + panel_h + gap_y),
        ("TRAPEZOIDAL",         "T",  130 + panel_w + gap_x, top_y + panel_h + gap_y),
    ]

    # underlying curve: y = -0.5(x-3)^2 + 8 on x in [0, 6] — a parabola peak around x=3
    def f(x):
        return -0.5 * (x - 3) ** 2 + 8

    for title, kind, x0, y0 in panels:
        # card background
        d.rounded_rectangle([x0, y0, x0 + panel_w, y0 + panel_h],
                            radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        d.text((x0 + 30, y0 + 18), title, fill=MAROON, font=font("serif_bold", 36))

        # mini axes inside the panel
        plot_x0 = x0 + 60
        plot_y0 = y0 + 80
        plot_w = panel_w - 100
        plot_h = panel_h - 130
        ax_y = plot_y0 + plot_h
        d.line([(plot_x0, ax_y), (plot_x0 + plot_w, ax_y)], fill=INK, width=2)
        d.line([(plot_x0, plot_y0), (plot_x0, ax_y)], fill=INK, width=2)

        x_lo, x_hi = 0, 6
        y_lo, y_hi = 0, 9
        sx = plot_w / (x_hi - x_lo)
        sy = plot_h / (y_hi - y_lo)

        def to_px(xv, yv):
            return (plot_x0 + (xv - x_lo) * sx, ax_y - (yv - y_lo) * sy)

        # rectangles — n = 6 subintervals
        n = 6
        dx = (x_hi - x_lo) / n
        for i in range(n):
            xi = x_lo + i * dx
            xj = xi + dx
            if kind == "L":
                h_val = f(xi)
                p1 = to_px(xi, 0)
                p2 = to_px(xj, h_val)
                d.rectangle([p1[0], p2[1], p2[0], p1[1]],
                            fill=deck.accent_light, outline=MAROON_DARK, width=2)
            elif kind == "R":
                h_val = f(xj)
                p1 = to_px(xi, 0)
                p2 = to_px(xj, h_val)
                d.rectangle([p1[0], p2[1], p2[0], p1[1]],
                            fill=deck.accent_light, outline=MAROON_DARK, width=2)
            elif kind == "M":
                xm = (xi + xj) / 2
                h_val = f(xm)
                p1 = to_px(xi, 0)
                p2 = to_px(xj, h_val)
                d.rectangle([p1[0], p2[1], p2[0], p1[1]],
                            fill=deck.accent_light, outline=MAROON_DARK, width=2)
            else:  # T — trapezoid
                hL = f(xi)
                hR = f(xj)
                pL_top = to_px(xi, hL)
                pR_top = to_px(xj, hR)
                pL_bot = to_px(xi, 0)
                pR_bot = to_px(xj, 0)
                d.polygon([pL_bot, pL_top, pR_top, pR_bot],
                          fill=deck.accent_light, outline=MAROON_DARK)

        # the curve f(x) overlaid on top
        pts = []
        xv = x_lo
        while xv <= x_hi:
            pts.append(to_px(xv, f(xv)))
            xv += 0.04
        for a_pt, b_pt in zip(pts[:-1], pts[1:]):
            d.line([a_pt, b_pt], fill=MAROON, width=4)


deck.custom("05_riemann_sums", riemann_sums)


# ─── 06 — Riemann concavity / monotonicity compare ───────────────────────
deck.compare(
    "06_riemann_concavity",
    "Monotonicity decides L vs R.",
    left={
        "label": "f INCREASING",
        "color": MAROON,
        "lines": [
            "Left sum:   UNDER-estimates.",
            "Right sum:  OVER-estimates.",
            "(Curve rises faster than rectangles.)",
            "Midpoint usually wins.",
        ],
        "footnote": "Increasing → L low, R high.  Sketch one rectangle and you'll see it.",
    },
    right={
        "label": "f DECREASING",
        "color": MAROON_DARK,
        "lines": [
            "Left sum:   OVER-estimates.",
            "Right sum:  UNDER-estimates.",
            "(Sign of monotonicity flips it.)",
            "Midpoint still tends to win.",
        ],
        "footnote": "Decreasing → L high, R low.  The mirror image.",
    },
)


# ─── 07 — sum to integral (custom) ───────────────────────────────────────
def sum_to_integral(img, d):
    d.text((110, 80), "Take the limit — the sum becomes the integral.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 158),
           "As  n → ∞,  Δx → 0,  the rectangles fit the curve perfectly.",
           fill=MUTED, font=font("sans", 32))

    # LEFT — the sum
    d.rounded_rectangle([110, 260, 880, 760], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((140, 290), "finite Riemann sum",
           fill=MAROON, font=font("serif_bold", 38))
    # the big Σ formula
    centered_x_l = (110 + 880) // 2
    d.text((centered_x_l - 230, 400), "n",
           fill=INK, font=font("mono", 32))
    d.text((centered_x_l - 250, 440), "Σ",
           fill=MAROON, font=font("mono", 110))
    d.text((centered_x_l - 250, 580), "i = 1",
           fill=INK, font=font("mono", 32))
    d.text((centered_x_l - 130, 460), "f(xᵢ*) · Δx",
           fill=INK, font=font("mono", 56))

    d.text((140, 670), "xᵢ* = any sample point",
           fill=MUTED, font=font("sans", 26))
    d.text((140, 705), "(left, right, midpoint — all converge)",
           fill=MUTED, font=font("sans", 26))

    # ARROW between cards
    arrow_y = 510
    d.line([(900, arrow_y), (1010, arrow_y)], fill=MAROON_DARK, width=8)
    d.polygon([(1010, arrow_y - 18), (1010, arrow_y + 18), (1040, arrow_y)],
              fill=MAROON_DARK)
    d.text((905, arrow_y - 70), "n → ∞", fill=MAROON, font=font("mono", 36))
    d.text((905, arrow_y + 30), "Δx → 0", fill=MAROON, font=font("mono", 36))

    # RIGHT — the integral
    d.rounded_rectangle([1050, 260, W - 110, 760], radius=24,
                        outline=MAROON, width=5, fill=deck.accent_light)
    d.text((1080, 290), "definite integral",
           fill=MAROON_DARK, font=font("serif_bold", 38))

    # Big ∫ expression centered
    centered_x_r = (1050 + W - 110) // 2
    d.text((centered_x_r - 60, 360), "b",
           fill=MAROON_DARK, font=font("serif_ital", 34))
    d.text((centered_x_r - 200, 410), "∫",
           fill=MAROON_DARK, font=font("mono", 140))
    d.text((centered_x_r - 60, 590), "a",
           fill=MAROON_DARK, font=font("serif_ital", 34))
    d.text((centered_x_r - 30, 470), "f(x) dx",
           fill=MAROON_DARK, font=font("mono", 56))

    d.text((1080, 670), "lower bound  a,  upper bound  b",
           fill=MAROON_DARK, font=font("sans", 26))
    d.text((1080, 705), "integrand  f(x),  differential  dx",
           fill=MAROON_DARK, font=font("sans", 26))

    # Footer banner
    d.rounded_rectangle([110, 800, W - 110, 950], radius=20,
                        outline=MAROON, width=3, fill=deck.bg)
    centered(d, "Σ  becomes  ∫.    Δx  becomes  dx.    Definition of the definite integral.",
             font("sans_bold", 36), 830, MAROON_DARK)
    centered(d, "Sample point doesn't matter — all four schemes converge to the same number.",
             font("sans", 30), 890, MUTED)


deck.custom("07_definite_integral", sum_to_integral)


# ─── 08 — integral is a NUMBER ───────────────────────────────────────────
deck.definition(
    "08_integral_is_number",
    "The definite integral is a NUMBER.",
    "∫ from a to b  of  f(x) dx   =   one  number.",
    "No  x  in the answer.  If you see  x,  you forgot to evaluate.  (Indefinite integrals — different — coming in Module 8.)",
)


# ─── 09 — five properties ────────────────────────────────────────────────
deck.equation(
    "09_properties",
    "Five properties of the definite integral.",
    [
        ("∫ₐᵃ f(x) dx  =  0",                              INK,    "1. same point to itself — no area"),
        ("∫ᵦᵃ f(x) dx  =  − ∫ₐᵇ f(x) dx",                   MAROON, "2. swapping the bounds flips the sign  ← AP trap"),
        ("∫ₐᶜ f  =  ∫ₐᵇ f  +  ∫ᵦᶜ f",                       INK,    "3. additivity — split at any interior point"),
        ("∫ₐᵇ k · f(x) dx  =  k · ∫ₐᵇ f(x) dx",             INK,    "4. constants pull out"),
        ("∫ₐᵇ (f + g) dx  =  ∫ₐᵇ f  +  ∫ₐᵇ g",              INK,    "5. integral of a sum  =  sum of integrals"),
    ],
)


# ─── 10 — FTC Part 2 ─────────────────────────────────────────────────────
deck.equation(
    "10_ftc_part2",
    "FTC Part 2  ·  the evaluation theorem.",
    [
        ("∫ₐᵇ f(x) dx  =  F(b)  −  F(a)",          INK,    "where  F'(x) = f(x)  — F is any antiderivative of f"),
        ("∫₁³ 2x dx  =  x²  |₁³",                  MUTED,  "antiderivative of  2x  is  x²"),
        ("           =  (3)²  −  (1)²",            MUTED,  "plug in upper, plug in lower"),
        ("           =  9  −  1  =  8",            MAROON, "the integral is the number  8"),
    ],
)


# ─── 11 — pause-and-try ──────────────────────────────────────────────────
deck.pause(
    "11_pause1", "PAUSE  &  TRY",
    "Evaluate using FTC Part 2:",
    "∫₀² (3x² + 1) dx",
    hint="Antiderivative.  Plug in 2.  Plug in 0.  Subtract.  Press play when ready.",
)

# ─── 12 — pause silence (duplicate of 11) ────────────────────────────────
deck.duplicate("11_pause1", "12_pause1_silence")


# ─── 13 — FTC Part 1 (custom) ────────────────────────────────────────────
def ftc_part1(img, d):
    d.text((110, 70), "FTC Part 1  ·  the accumulation theorem.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 148),
           "Differentiation and integration undo each other.",
           fill=MUTED, font=font("sans", 32))

    # MAIN statement card — split into two halves left/right inside the card
    d.rounded_rectangle([110, 220, W - 110, 470], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    # LEFT half — definition
    d.text((150, 250), "Define an accumulation function:",
           fill=MAROON, font=font("serif_bold", 32))
    d.text((180, 320), "F(x)  =  ∫ₐˣ  f(t) dt",
           fill=INK, font=font("mono", 58))
    # Divider
    d.line([(W // 2, 250), (W // 2, 440)], fill=MUTED, width=2)
    # RIGHT half — conclusion
    d.text((W // 2 + 40, 250), "Then differentiate it:",
           fill=MAROON, font=font("serif_bold", 32))
    d.text((W // 2 + 80, 320), "F'(x)  =  f(x)",
           fill=MAROON_DARK, font=font("mono", 64))

    # ── Chain-rule extension card ──
    d.rounded_rectangle([110, 510, 940, 800], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    d.text((140, 530), "Chain-rule extension",
           fill=MAROON_DARK, font=font("serif_bold", 38))
    d.text((140, 600), "d/dx  ∫ₐ^{g(x)}  f(t) dt",
           fill=MAROON_DARK, font=font("mono", 38))
    d.text((140, 670), "    =  f( g(x) )  ·  g'(x)",
           fill=MAROON_DARK, font=font("mono", 38))
    d.text((140, 740), "Plug the upper bound into  f,  then multiply by  g'.",
           fill=MAROON_DARK, font=font("sans", 28))

    # ── Warning card ──
    d.rounded_rectangle([980, 510, W - 110, 800], radius=20,
                        outline=RED, width=4, fill=deck.card_bg)
    d.text((1010, 530), "Two warnings",
           fill=RED, font=font("serif_bold", 38))
    d.text((1010, 600), "•  t  is a DUMMY variable",
           fill=INK, font=font("sans_bold", 30))
    d.text((1010, 645), "    — does not appear in F'(x).",
           fill=MUTED, font=font("sans", 28))
    d.text((1010, 700), "•  The answer is  f  evaluated at",
           fill=INK, font=font("sans_bold", 30))
    d.text((1010, 745), "    the upper bound,  not  f(t).",
           fill=MUTED, font=font("sans", 28))

    # Footer
    d.text((110, 870), "Integration and differentiation are inverse operations.  That's the whole theorem.",
           fill=deck.accent, font=font("sans_bold", 32))


deck.custom("13_ftc_part1", ftc_part1)


# ─── 14 — FTC Part 1 wrong-vs-right compare ──────────────────────────────
deck.compare(
    "14_compare",
    "Most-misstated theorem on the AP exam.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "d/dx ∫ₐˣ f(t) dt  =  f(t)",
            "d/dx ∫ₐˣ f(t) dt  =  F(x)",
            "d/dx ∫ₐˣ f(t) dt  =  0",
            "Three classic mis-statements.",
        ],
        "footnote": "t is a dummy.  F is not the answer.  Zero is wrong.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "d/dx ∫ₐˣ f(t) dt  =  f(x)",
            "Upper-bound variable goes IN.",
            "Dummy t  gets eaten by  d/dx.",
            "f evaluated at the upper bound.",
        ],
        "footnote": "If the upper bound is  g(x),  multiply by  g'(x).",
    },
)


# ─── 15 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "15_recap", "Recap.",
    [
        "Integration  =  accumulation  =  signed area under a rate.",
        "Riemann sums  (L / R / M / T)  approximate;  limit gives the integral.",
        "The definite integral is a NUMBER.  No  x  in the answer.",
        "Five properties — including bound-swap sign flip.",
        "FTC Part 1:  d/dx ∫ₐˣ f(t) dt  =  f(x).",
        "FTC Part 2:  ∫ₐᵇ f(x) dx  =  F(b) − F(a).",
    ],
    assignment=[
        "15 mixed Riemann + FTC problems in your dashboard.",
        "5 numeric Riemann estimates  +  10 FTC evaluations.",
    ],
)


# ─── 16 — path ───────────────────────────────────────────────────────────
deck.path(
    "16_path",
    items=[
        ("✓",  "Watch this lesson",            "(done!)"),
        ("1.", "OpenStax Calculus Vol 1",      "Read sections 5.1 – 5.4"),
        ("2.", "Khan Academy practice",        "AP Calc AB · Unit 6 part 1 — Riemann sums + FTC"),
        ("3.", "Assignment in dashboard",      "15 mixed Riemann / FTC problems"),
        ("4.", "Advisor check-in",             "Book if FTC Part 1 dummy-variable still feels odd"),
    ],
    next_text="Next up:  Module 8 — Antiderivatives & Substitution.  How to actually FIND antiderivatives.",
)


print("AP Calc AB Module 7 slides built.")

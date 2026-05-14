"""AP Calculus AB · Module 6 — Graph Sketching, Optimization & Implicit Behavior.

Built on slide_kit (math theme = gold + cream).
Custom slides:
- 02_hook                        : soup-can diagram + objective (least aluminum) callout
- 04_reading_derivative_graphs   : side-by-side f' graph vs derived f sketch with sign labels
- 05_second_derivative_meaning   : concave-up smile vs concave-down frown panels + inflection
- 06_sketch_f_from_fprime        : f' graph (piecewise linear, zeros at -1 and 3) + sign chart
                                    + derived sketch of f below — labelled "this is f', NOT f"
- 08_optimization_example_rectangle : parabola y = 4 - x^2 + inscribed rectangle + A(x)
                                    + candidates table (A(0)=0, A(2)=0, A(sqrt(4/3)) ≈ 6.16)
- 13_implicit_example_circle     : circle x^2 + y^2 = 25 with H/V tangent markers
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
deck = Deck(course="AP Calculus AB", module_num=6,
            output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 6 — Graph Sketching, Optimization & Implicit Behavior",
    "~10 minutes  ·  Unit 5(b) · FUN 5.8 – 5.12",
)


# ─── 02 — hook (custom: soup-can optimization framing) ───────────────────
def hook(img, d):
    d.text((110, 80), "Design the soup can.",
           fill=MAROON, font=font("serif_bold", 80))
    d.text((110, 178),
           "Holds exactly 350 mL. Uses the least aluminum.  What r and h?",
           fill=MUTED, font=font("sans", 36))

    # LEFT — soup can illustration
    cx = 480
    top_y = 320
    bot_y = 820
    rx = 170
    ry = 50  # ellipse "thickness" for top/bottom
    # body
    d.rectangle([cx - rx, top_y, cx + rx, bot_y], fill=deck.card_bg,
                outline=MAROON, width=5)
    # bottom ellipse (visible as the curved bottom)
    d.ellipse([cx - rx, bot_y - ry, cx + rx, bot_y + ry],
              fill=deck.card_bg, outline=MAROON, width=5)
    # top ellipse (lid)
    d.ellipse([cx - rx, top_y - ry, cx + rx, top_y + ry],
              fill=deck.accent_light, outline=MAROON, width=5)
    # label band
    d.rectangle([cx - rx + 10, top_y + 180, cx + rx - 10, top_y + 320],
                fill=MAROON, outline=MAROON_DARK, width=3)
    centered_x = cx
    d.text((cx - 80, top_y + 200), "SOUP",
           fill=deck.bg, font=font("serif_bold", 56))
    d.text((cx - 90, top_y + 270), "350 mL",
           fill=deck.accent_light, font=font("sans_bold", 36))

    # radius arrow (top)
    d.line([(cx, top_y), (cx + rx, top_y)], fill=MAROON_DARK, width=3)
    d.polygon([(cx + rx, top_y), (cx + rx - 14, top_y - 8),
               (cx + rx - 14, top_y + 8)], fill=MAROON_DARK)
    d.text((cx + 50, top_y - 50), "r = ?",
           fill=MAROON_DARK, font=font("serif_bold", 38))

    # height arrow (right side)
    arr_x = cx + rx + 60
    d.line([(arr_x, top_y), (arr_x, bot_y)], fill=MAROON_DARK, width=3)
    d.polygon([(arr_x, top_y), (arr_x - 8, top_y + 14),
               (arr_x + 8, top_y + 14)], fill=MAROON_DARK)
    d.polygon([(arr_x, bot_y), (arr_x - 8, bot_y - 14),
               (arr_x + 8, bot_y - 14)], fill=MAROON_DARK)
    d.text((arr_x + 18, (top_y + bot_y) // 2 - 24), "h = ?",
           fill=MAROON_DARK, font=font("serif_bold", 38))

    # RIGHT — objective + constraint cards
    card_x = 900
    card_w = W - 110 - card_x
    # Objective card
    d.rounded_rectangle([card_x, 310, card_x + card_w, 510], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, 330), "Objective — minimize",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((card_x + 30, 400), "A  =  2πr²  +  2πrh",
           fill=INK, font=font("mono", 50))
    d.text((card_x + 30, 460), "(surface area of aluminum)",
           fill=MUTED, font=font("sans", 28))

    # Constraint card
    d.rounded_rectangle([card_x, 540, card_x + card_w, 740], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, 560), "Constraint — fixed volume",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((card_x + 30, 630), "πr²h  =  350",
           fill=INK, font=font("mono", 50))
    d.text((card_x + 30, 690), "(volume of the cylinder)",
           fill=MUTED, font=font("sans", 28))

    # Closing strip
    d.rounded_rectangle([110, 870, W - 110, 1000], radius=20,
                        fill=deck.accent_light)
    centered(d, "One right answer.  Calculus pins it down.",
             font("sans_bold", 38), 900, MAROON_DARK)


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Read f, f', and f'' fluently — sketch one from the other.",
        "The 5-step optimization method, with feasibility check.",
        "Implicit differentiation — curves that aren't functions of x.",
    ],
    footnote="Module 5 gave you the tests.  Module 6 makes them earn their keep.",
)


# ─── 04 — reading derivative graphs (custom: signs of f' → behavior of f) ─
def reading_derivative_graphs(img, d):
    d.text((110, 80), "Sign of  f'  controls behavior of  f.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 158),
           "Read the sign — read the motion.",
           fill=MUTED, font=font("sans", 34))

    # Three big rule cards
    card_y = 240
    card_h = 180
    card_w = 540
    gap = 30
    cards = [
        ("f' > 0", "f is increasing", deck.accent),
        ("f' < 0", "f is decreasing", MAROON),
        ("f' = 0", "critical point", MAROON_DARK),
    ]
    for i, (top, bot, col) in enumerate(cards):
        x0 = 110 + i * (card_w + gap)
        d.rounded_rectangle([x0, card_y, x0 + card_w, card_y + card_h],
                            radius=20, outline=col, width=5, fill=deck.card_bg)
        d.text((x0 + 30, card_y + 25), top, fill=col, font=font("mono", 60))
        d.text((x0 + 30, card_y + 110), bot, fill=INK, font=font("sans_bold", 36))

    # Sign-change panel
    panel_y = 480
    panel_h = 380
    d.rounded_rectangle([110, panel_y, W - 110, panel_y + panel_h],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((150, panel_y + 25), "Sign change at a critical point  =  relative extremum.",
           fill=MAROON, font=font("serif_bold", 40))

    # Two mini sign charts
    # LEFT — f' goes + to - (relative MAX)
    sx0 = 200
    sy = panel_y + 180
    d.line([(sx0, sy), (sx0 + 600, sy)], fill=INK, width=3)
    d.ellipse([sx0 + 290, sy - 10, sx0 + 310, sy + 10], fill=MAROON_DARK)
    d.text((sx0 + 100, sy - 70), "f'  +", fill=deck.accent, font=font("mono", 50))
    d.text((sx0 + 440, sy - 70), "f'  −", fill=MAROON, font=font("mono", 50))
    d.text((sx0 + 270, sy + 20), "c", fill=INK, font=font("serif_ital", 38))
    d.text((sx0 + 130, sy + 90), "f  has a relative MAX at  c",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # RIGHT — f' goes - to + (relative MIN)
    sx0 = 1010
    d.line([(sx0, sy), (sx0 + 600, sy)], fill=INK, width=3)
    d.ellipse([sx0 + 290, sy - 10, sx0 + 310, sy + 10], fill=MAROON_DARK)
    d.text((sx0 + 100, sy - 70), "f'  −", fill=MAROON, font=font("mono", 50))
    d.text((sx0 + 440, sy - 70), "f'  +", fill=deck.accent, font=font("mono", 50))
    d.text((sx0 + 270, sy + 20), "c", fill=INK, font=font("serif_ital", 38))
    d.text((sx0 + 130, sy + 90), "f  has a relative MIN at  c",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # Bottom note
    d.text((110, 910), "No sign change at  c  →  not an extremum.  Just a flat spot.",
           fill=deck.accent, font=font("sans_bold", 32))


deck.custom("04_reading_derivative_graphs", reading_derivative_graphs)


# ─── 05 — second derivative meaning (custom: concavity panels) ───────────
def second_derivative(img, d):
    d.text((110, 80), "Sign of  f''  controls concavity.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 158), "Smile or frown.  Holding water or spilling.",
           fill=MUTED, font=font("sans", 34))

    # Two large panels
    panel_w = 820
    panel_h = 540
    panel_y = 240
    panels = [
        (110, "f''  >  0", "concave UP  (smile)", "holds water", deck.accent, True),
        (980, "f''  <  0", "concave DOWN  (frown)", "spills water", MAROON, False),
    ]
    for x0, eq, sub, water, col, smile in panels:
        d.rounded_rectangle([x0, panel_y, x0 + panel_w, panel_y + panel_h],
                            radius=24, outline=col, width=5, fill=deck.card_bg)
        d.text((x0 + 40, panel_y + 25), eq, fill=col, font=font("mono", 60))
        d.text((x0 + 40, panel_y + 110), sub, fill=INK, font=font("sans_bold", 38))

        # Draw a small parabola — smile or frown
        cx = x0 + panel_w // 2
        cy = panel_y + 360
        scale_y = 1 if smile else -1
        pts = []
        for k in range(-160, 161, 4):
            yv = (k * k) / 80
            pts.append((cx + k, cy - yv * scale_y))
        for a_pt, b_pt in zip(pts[:-1], pts[1:]):
            d.line([a_pt, b_pt], fill=col, width=6)

        d.text((x0 + 40, panel_y + 470), water, fill=MUTED,
               font=font("sans", 30))

    # Inflection note
    d.rounded_rectangle([110, 830, W - 110, 980], radius=20,
                        fill=deck.accent_light)
    centered(d, "Where  f''  changes sign  →  point of inflection.",
             font("sans_bold", 38), 855, MAROON_DARK)
    centered(d, "The concavity flips. The curve switches from cup-up to cup-down or vice versa.",
             font("sans", 30), 915, MAROON_DARK)


deck.custom("05_second_derivative_meaning", second_derivative)


# ─── 06 — sketch f from f' (custom: warning + f' graph + f sketch) ───────
def sketch_f_from_fprime(img, d):
    # Big warning banner
    d.rectangle([0, 80, W, 200], fill=RED)
    centered(d, "This is the graph of  f'(x),  NOT  f(x).",
             font("serif_bold", 60), 105, deck.bg)

    d.text((110, 220), "Read f' as a slope-meter for f. Don't trace it as if it's f.",
           fill=MAROON_DARK, font=font("sans", 30))

    # LEFT — f'(x) piecewise-linear graph (zeros at -1 and 3)
    gx0, gy0 = 140, 290
    gw, gh = 800, 360
    # axes
    ax_y = gy0 + gh // 2
    d.line([(gx0, ax_y), (gx0 + gw, ax_y)], fill=INK, width=3)
    d.line([(gx0 + gw // 2, gy0), (gx0 + gw // 2, gy0 + gh)],
           fill=INK, width=3)
    d.text((gx0 + gw - 30, ax_y + 10), "x", fill=INK, font=font("serif_ital", 28))
    d.text((gx0 + gw // 2 + 10, gy0 - 30), "f'(x)",
           fill=INK, font=font("serif_ital", 30))

    # x-axis tick labels: -3, -1, 0, 1, 3, 5
    unit = gw // 8  # 8 units wide → -4 to +4
    origin = gx0 + gw // 2
    for xv in [-3, -1, 0, 1, 3, 5]:
        tx = origin + xv * unit
        d.line([(tx, ax_y - 6), (tx, ax_y + 6)], fill=INK, width=2)
        lbl = str(xv)
        tw = d.textlength(lbl, font=font("sans", 22))
        d.text((tx - tw / 2, ax_y + 12), lbl, fill=INK, font=font("sans", 22))

    # Piecewise-linear f' with zeros at x = -1 and x = 3:
    # Use f'(x) shape: V-shape down before -1, peak around x=1, back down to 0 at x=3
    # Concrete points (x in graph coords):
    # (-3, -2) → (-1, 0) → (1, 2) → (3, 0) → (5, -2)
    fprime_pts_data = [(-3, -2), (-1, 0), (1, 2), (3, 0), (5, -2)]
    yscale = (gh // 2 - 20) // 3  # so y = ±3 fits inside
    fp_pts = []
    for xv, yv in fprime_pts_data:
        px = origin + xv * unit
        py = ax_y - yv * yscale
        fp_pts.append((px, py))
    for a_pt, b_pt in zip(fp_pts[:-1], fp_pts[1:]):
        d.line([a_pt, b_pt], fill=deck.accent, width=6)
    # zero markers (filled dots on the x-axis where f' = 0)
    for xv, yv in fprime_pts_data:
        if yv == 0:
            px = origin + xv * unit
            d.ellipse([px - 8, ax_y - 8, px + 8, ax_y + 8], fill=MAROON_DARK)
            d.text((px - 10, ax_y - 40), f"x={xv}",
                   fill=MAROON_DARK, font=font("sans_bold", 22))

    d.text((gx0 + 250, gy0 - 25), "graph of  f'(x)",
           fill=MAROON, font=font("serif_bold", 32))

    # Sign chart for f' beneath the graph
    sc_y = gy0 + gh + 50
    d.line([(gx0 + 40, sc_y), (gx0 + gw - 40, sc_y)], fill=INK, width=3)
    # ticks at -1 and 3
    m1_x = origin + (-1) * unit
    p3_x = origin + 3 * unit
    for tx, lbl in [(m1_x, "−1"), (p3_x, "3")]:
        d.line([(tx, sc_y - 8), (tx, sc_y + 8)], fill=INK, width=2)
        d.text((tx - 14, sc_y + 14), lbl, fill=INK, font=font("sans_bold", 24))
    # signs in each region
    d.text((gx0 + 80, sc_y - 50), "f'  −", fill=MAROON, font=font("mono", 36))
    d.text(((m1_x + p3_x) // 2 - 50, sc_y - 50), "f'  +",
           fill=deck.accent, font=font("mono", 36))
    d.text((p3_x + 80, sc_y - 50), "f'  −", fill=MAROON, font=font("mono", 36))

    # RIGHT — derived sketch of f
    fx0, fy0 = 1020, 290
    fw, fh = 800, 540
    fax_y = fy0 + fh // 2 + 40
    d.line([(fx0, fax_y), (fx0 + fw, fax_y)], fill=INK, width=3)
    f_origin = fx0 + fw // 2
    d.line([(f_origin, fy0), (f_origin, fy0 + fh)], fill=INK, width=3)
    d.text((fx0 + fw - 30, fax_y + 10), "x", fill=INK, font=font("serif_ital", 28))
    d.text((f_origin + 10, fy0 - 30), "f(x)",
           fill=INK, font=font("serif_ital", 30))

    # tick labels for f-graph
    funit = fw // 8
    for xv in [-3, -1, 0, 1, 3, 5]:
        tx = f_origin + xv * funit
        d.line([(tx, fax_y - 6), (tx, fax_y + 6)], fill=INK, width=2)
        lbl = str(xv)
        tw = d.textlength(lbl, font=font("sans", 22))
        d.text((tx - tw / 2, fax_y + 12), lbl, fill=INK, font=font("sans", 22))

    # Sketch f: decreasing → max at -1 → decreasing... wait.
    # f' negative on (-inf, -1) → f decreasing
    # f' positive on (-1, 3)    → f increasing
    # f' negative on (3, inf)   → f decreasing
    # So: f decreases, hits MIN at x=-1, increases to MAX at x=3, decreases.
    # NOTE: a sign change + to - = max; - to + = min.
    # f' goes -, then +, then -. So at -1: - to + = MIN.  At 3: + to - = MAX.
    # Let me re-check: yes — at x = -1, f' changes from negative to positive → f has a relative MIN.
    # At x = 3, f' changes from positive to negative → f has a relative MAX.
    # Build a smooth-ish curve: parabola-stitching using control values
    # x: -3, -1, 1, 3, 5  → relative heights for f:  high, LOW (min), middle, HIGH (max), low
    f_heights = {-3: 2.0, -1: -2.0, 1: 0.5, 3: 2.5, 5: -1.5}
    yscale_f = 50

    # sample x from -3.5 to 5.5 using piecewise-quadratic through the keypoints
    def f_val(x):
        # piecewise linear interpolation between keypoints for clarity
        keys = sorted(f_heights.keys())
        for i in range(len(keys) - 1):
            x0k, x1k = keys[i], keys[i + 1]
            if x0k <= x <= x1k:
                # smooth interpolation (cosine ease)
                t = (x - x0k) / (x1k - x0k)
                t_smooth = (1 - math.cos(t * math.pi)) / 2
                return f_heights[x0k] + (f_heights[x1k] - f_heights[x0k]) * t_smooth
        if x < keys[0]:
            return f_heights[keys[0]]
        return f_heights[keys[-1]]

    pts_f = []
    x = -3.5
    while x <= 5.5:
        px = f_origin + x * funit
        py = fax_y - f_val(x) * yscale_f
        if fy0 < py < fy0 + fh:
            pts_f.append((px, py))
        x += 0.05
    for a_pt, b_pt in zip(pts_f[:-1], pts_f[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)

    # mark MIN at x=-1 and MAX at x=3 on f
    min_x = f_origin + (-1) * funit
    min_y = fax_y - f_val(-1) * yscale_f
    max_x = f_origin + 3 * funit
    max_y = fax_y - f_val(3) * yscale_f
    d.ellipse([min_x - 9, min_y - 9, min_x + 9, min_y + 9], fill=MAROON_DARK)
    d.text((min_x - 60, min_y + 18), "MIN",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    d.ellipse([max_x - 9, max_y - 9, max_x + 9, max_y + 9], fill=MAROON_DARK)
    d.text((max_x - 30, max_y - 50), "MAX",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    d.text((fx0 + 230, fy0 - 25), "derived sketch of  f(x)",
           fill=MAROON, font=font("serif_bold", 32))


deck.custom("06_sketch_f_from_fprime", sketch_f_from_fprime)


# ─── 07 — optimization 5-step method (overview) ──────────────────────────
deck.overview(
    "07_optimization_5step_method", "Optimization — five steps.",
    [
        "Read the problem.  Draw the picture.",
        "Identify the objective function and the constraint.",
        "Reduce to one variable  +  feasibility check (domain).",
        "Differentiate.  Find critical points.",
        "Verify max vs. min  (2nd-deriv test  or  candidates test).",
    ],
    footnote="Skip step 5 and you lose points on the AP free response.",
)


# ─── 08 — optimization example: rectangle under parabola (custom) ────────
def opt_rectangle(img, d):
    d.text((110, 70), "Inscribed rectangle under  y = 4 − x².",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 148),
           "Feasibility:  x ∈ [0, 2].   Maximize  A(x) = 2x · (4 − x²).",
           fill=MUTED, font=font("sans", 32))

    # LEFT — graph
    gx0, gy0 = 130, 220
    gw, gh = 760, 560
    ax_y = gy0 + gh - 80
    origin_x = gx0 + gw // 2

    # axes
    d.line([(gx0, ax_y), (gx0 + gw, ax_y)], fill=INK, width=3)
    d.line([(origin_x, gy0 + 10), (origin_x, ax_y + 30)], fill=INK, width=3)
    d.text((gx0 + gw - 30, ax_y + 12), "x", fill=INK, font=font("serif_ital", 28))
    d.text((origin_x + 10, gy0), "y", fill=INK, font=font("serif_ital", 28))

    # scaling: x range -2.5 to 2.5  → gw; y range 0 to 5 → ax_y - gy0 - 20
    x_min, x_max = -2.5, 2.5
    y_min, y_max = -1.0, 5.0
    sx = gw / (x_max - x_min)
    sy = (ax_y - gy0 - 30) / (y_max - y_min)

    def to_px(xv, yv):
        return (gx0 + (xv - x_min) * sx, ax_y - (yv - 0) * sy)

    # x-axis tick labels
    for xv in [-2, -1, 0, 1, 2]:
        px, _ = to_px(xv, 0)
        d.line([(px, ax_y - 6), (px, ax_y + 6)], fill=INK, width=2)
        lbl = str(xv)
        tw = d.textlength(lbl, font=font("sans", 22))
        d.text((px - tw / 2, ax_y + 12), lbl, fill=INK, font=font("sans", 22))
    # y-axis ticks
    for yv in [1, 2, 3, 4]:
        _, py = to_px(0, yv)
        d.line([(origin_x - 6, py), (origin_x + 6, py)], fill=INK, width=2)
        d.text((origin_x - 35, py - 14), str(yv), fill=INK, font=font("sans", 22))

    # Parabola y = 4 - x^2 (only y >= 0 region shown)
    parab_pts = []
    xv = -2.2
    while xv <= 2.2:
        yv = 4 - xv * xv
        if yv >= -0.2:
            parab_pts.append(to_px(xv, yv))
        xv += 0.04
    for a_pt, b_pt in zip(parab_pts[:-1], parab_pts[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)

    # Inscribed rectangle at x = sqrt(4/3) ≈ 1.155
    x_star = math.sqrt(4 / 3)
    y_star = 4 - x_star * x_star  # = 4 - 4/3 = 8/3 ≈ 2.667
    p1 = to_px(-x_star, 0)
    p2 = to_px(x_star, 0)
    p3 = to_px(x_star, y_star)
    p4 = to_px(-x_star, y_star)
    # filled translucent-ish rectangle (use accent_light)
    d.polygon([p1, p2, p3, p4], fill=deck.accent_light, outline=MAROON_DARK)
    # outline
    d.line([p1, p2], fill=MAROON_DARK, width=4)
    d.line([p2, p3], fill=MAROON_DARK, width=4)
    d.line([p3, p4], fill=MAROON_DARK, width=4)
    d.line([p4, p1], fill=MAROON_DARK, width=4)

    # mark corner (x, 4-x²)
    d.ellipse([p3[0] - 8, p3[1] - 8, p3[0] + 8, p3[1] + 8], fill=MAROON_DARK)
    d.text((p3[0] + 12, p3[1] - 35), "(x, 4 − x²)",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # base width label
    d.text(((p1[0] + p2[0]) / 2 - 30, p1[1] + 16), "base = 2x",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # RIGHT — candidates table
    tx0 = 970
    d.rounded_rectangle([tx0, 220, W - 110, 530], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((tx0 + 30, 240), "Candidates test on  [0, 2]",
           fill=MAROON, font=font("serif_bold", 38))

    # table
    rows = [
        ("x = 0",            "A(0) = 0",                   MUTED),
        ("x = 2  (endpoint)", "A(2) = 0",                   MUTED),
        ("x = √(4/3) ≈ 1.155", "A(x*) ≈ 6.16  ← MAX",       MAROON),
    ]
    y = 320
    for lhs, rhs, col in rows:
        d.text((tx0 + 40, y), lhs, fill=INK, font=font("mono", 28))
        d.text((tx0 + 40, y + 38), rhs, fill=col, font=font("mono", 32))
        y += 90

    # Objective + derivative card
    d.rounded_rectangle([tx0, 560, W - 110, 870], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((tx0 + 30, 580), "A(x)  =  2x · (4 − x²)",
           fill=INK, font=font("mono", 36))
    d.text((tx0 + 30, 640), "      =  8x  −  2x³",
           fill=INK, font=font("mono", 36))
    d.text((tx0 + 30, 710), "A'(x) =  8  −  6x²",
           fill=INK, font=font("mono", 36))
    d.text((tx0 + 30, 770), "0 = 8 − 6x²  →  x² = 4/3",
           fill=MUTED, font=font("mono", 32))
    d.text((tx0 + 30, 815), "x  =  √(4/3)  ≈ 1.155",
           fill=MAROON, font=font("mono", 36))

    # Bottom note
    d.text((110, 900), "Interior critical point wins.  Endpoints both give zero area.",
           fill=deck.accent, font=font("sans_bold", 30))


deck.custom("08_optimization_example_rectangle", opt_rectangle)


# ─── 09 — verify max vs min ──────────────────────────────────────────────
deck.definition(
    "09_verify_max_vs_min",
    "Verify — never skip this.",
    "Endpoints  +  every interior critical point  →  compare.",
    "Largest value = absolute max.  Smallest = absolute min.  "
    "Or use the 2nd-derivative test on each interior CP.",
)


# ─── 10 — pause-and-try ──────────────────────────────────────────────────
deck.pause(
    "10_pause1", "PAUSE  &  TRY",
    "A rectangle has perimeter 40.  Find the dimensions that maximize area:",
    "P = 40",
    hint="Set up your constraint, reduce to one variable, then optimize.  "
         "Pause.  Solve.  Press play when ready.",
)

# ─── 10_pause1_silence — duplicate of 10_pause1 (P4) ─────────────────────
deck.duplicate("10_pause1", "10_pause1_silence")


# ─── 11 — pause solution ─────────────────────────────────────────────────
deck.equation(
    "11_pause1_solution",
    "Solution — perimeter 40, maximize area.",
    [
        ("2L + 2W = 40   →   W = 20 − L",        MUTED,  "constraint to one variable"),
        ("A(L)  =  L · (20 − L)  =  20L − L²",   INK,    "objective in L only"),
        ("A'(L) =  20  −  2L  =  0",             INK,    "critical point"),
        ("L = 10,  W = 10",                      MAROON, "10 × 10 square — symmetric optimum"),
    ],
)


# ─── 12 — implicit relations (definition) ────────────────────────────────
def implicit_intro(img, d):
    d.text((110, 80), "When  y  is not a function of  x.",
           fill=MAROON, font=font("serif_bold", 60))

    # Card 1 — the problem
    d.rounded_rectangle([110, 250, W - 110, 470], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    centered(d, "x²  +  y²  =  25", font("mono", 80), 280, INK)
    centered(d, "For most  x,  there are TWO  y  values.  Fails the vertical line test.",
             font("sans", 32), 400, MUTED)

    # Card 2 — implicit diff
    d.rounded_rectangle([110, 510, W - 110, 800], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    d.text((150, 530), "Implicit differentiation",
           fill=MAROON_DARK, font=font("serif_bold", 40))
    centered(d, "1.  Treat  y  as a function of  x.",
             font("sans_bold", 34), 600, MAROON_DARK)
    centered(d, "2.  Differentiate both sides  →  chain rule on  y.",
             font("sans_bold", 34), 660, MAROON_DARK)
    centered(d, "3.  Solve for  dy/dx.   (Answer involves both  x  and  y.)",
             font("sans_bold", 34), 720, MAROON_DARK)

    d.text((110, 850), "Why we care:  horizontal tangents  ↔  dy/dx = 0.   Vertical tangents  ↔  dy/dx undefined.",
           fill=deck.accent, font=font("sans_bold", 30))


deck.custom("12_implicit_relations", implicit_intro)


# ─── 13 — implicit example: circle (custom) ──────────────────────────────
def implicit_circle(img, d):
    d.text((110, 70), "Circle  x² + y² = 25  →  dy/dx = −x/y.",
           fill=MAROON, font=font("serif_bold", 54))

    # LEFT — work
    d.rounded_rectangle([110, 220, 870, 880], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((140, 240), "Differentiate both sides:",
           fill=MAROON, font=font("serif_bold", 34))
    d.text((140, 310), "2x  +  2y · dy/dx  =  0",
           fill=INK, font=font("mono", 42))
    d.text((140, 400), "Solve:",
           fill=MAROON, font=font("serif_bold", 34))
    d.text((140, 470), "dy/dx  =  −x / y",
           fill=MAROON, font=font("mono", 50))

    d.text((140, 580), "Horizontal tangent:  dy/dx = 0",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((140, 625), "→  x = 0  →  (0, 5)  and  (0, −5)",
           fill=INK, font=font("mono", 32))

    d.text((140, 720), "Vertical tangent:  dy/dx  undefined",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((140, 765), "→  y = 0  →  (5, 0)  and  (−5, 0)",
           fill=INK, font=font("mono", 32))

    # RIGHT — circle diagram
    cx = 1340
    cy = 540
    r = 280
    # axes
    d.line([(cx - r - 80, cy), (cx + r + 80, cy)], fill=INK, width=3)
    d.line([(cx, cy - r - 80), (cx, cy + r + 80)], fill=INK, width=3)
    d.text((cx + r + 90, cy + 10), "x", fill=INK, font=font("serif_ital", 28))
    d.text((cx + 12, cy - r - 105), "y", fill=INK, font=font("serif_ital", 28))

    # circle
    d.ellipse([cx - r, cy - r, cx + r, cy + r],
              outline=MAROON, width=6)

    # H/V tangent markers — short tangent line segments at each cardinal point
    tan_len = 110
    # top (0, 5) — horizontal tangent
    d.line([(cx - tan_len, cy - r), (cx + tan_len, cy - r)],
           fill=deck.accent, width=5)
    d.ellipse([cx - 8, cy - r - 8, cx + 8, cy - r + 8], fill=MAROON_DARK)
    d.text((cx + 16, cy - r - 38), "(0, 5)",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    # bottom (0, -5)
    d.line([(cx - tan_len, cy + r), (cx + tan_len, cy + r)],
           fill=deck.accent, width=5)
    d.ellipse([cx - 8, cy + r - 8, cx + 8, cy + r + 8], fill=MAROON_DARK)
    d.text((cx + 16, cy + r + 20), "(0, −5)",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    # right (5, 0) — vertical tangent
    d.line([(cx + r, cy - tan_len), (cx + r, cy + tan_len)],
           fill=deck.accent, width=5)
    d.ellipse([cx + r - 8, cy - 8, cx + r + 8, cy + 8], fill=MAROON_DARK)
    d.text((cx + r + 14, cy + 14), "(5, 0)",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    # left (-5, 0)
    d.line([(cx - r, cy - tan_len), (cx - r, cy + tan_len)],
           fill=deck.accent, width=5)
    d.ellipse([cx - r - 8, cy - 8, cx - r + 8, cy + 8], fill=MAROON_DARK)
    d.text((cx - r - 110, cy + 14), "(−5, 0)",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # H / V labels
    d.text((cx - 130, cy - r + 14), "horizontal",
           fill=deck.accent, font=font("sans_bold", 24))
    d.text((cx + r - 90, cy + 130), "vertical",
           fill=deck.accent, font=font("sans_bold", 24))


deck.custom("13_implicit_example_circle", implicit_circle)


# ─── 14 — AP trap compare ────────────────────────────────────────────────
deck.compare(
    "14_ap_trap_compare",
    "Common AP trap — stopping at the critical point.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "Found  x = √(4/3).",
            "Plugged in.  Reported the answer.",
            "Never asked: is it max or min?",
            "AP loses you the verify point.",
        ],
        "footnote": "Right number, wrong logic — partial credit only.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "Found  x = √(4/3).",
            "Ran the candidates test on  [0, 2].",
            "A(0)=0, A(2)=0, A(x*) ≈ 6.16.",
            "Concluded:  interior CP is the MAX.",
        ],
        "footnote": "Verify on every free-response.  Every single time.",
    },
)


# ─── 15 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "15_recap", "Recap.",
    [
        "Sign of  f'  →  monotonicity  (increasing / decreasing).",
        "Sign of  f''  →  concavity  (up = smile, down = frown).",
        "Sketch  f  from  f'  using sign changes  →  extrema.",
        "Optimize with the 5-step method  +  feasibility check.",
        "Always verify max vs. min  (candidates test or 2nd-deriv).",
        "Implicit differentiation handles non-function curves.",
    ],
)


# ─── 16 — path ───────────────────────────────────────────────────────────
deck.path(
    "16_path",
    items=[
        ("✓",  "Watch this lesson",            "(done!)"),
        ("1.", "OpenStax Calculus Vol 1",      "Read sections 4.7 – 4.8"),
        ("2.", "Khan Academy practice",        "AP Calc AB · Unit 5 Part 2 — Optimization & analyzing f'"),
        ("3.", "Assignment in dashboard",      "GIIS Optimization Set — 5 applied + 2 implicit"),
        ("4.", "Advisor check-in",             "15-min walkthrough of one optimization FRQ"),
    ],
    next_text="Next up:  Module 7 — Riemann Sums and the Fundamental Theorem of Calculus.",
)


print("AP Calc AB Module 6 slides built.")

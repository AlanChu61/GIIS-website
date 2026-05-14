"""AP Calculus AB · Module 4 — Contextual Applications of Differentiation.

Built on slide_kit (math theme = gold + cream).
Custom slides:
- 02_hook                  : ladder sliding down a wall, with 1 ft/s arrow
- 04_units_of_derivative   : units table (f, x, f') with examples
- 05_motion_pva            : s(t) → v(t) = s'(t) → a(t) = v''(t) chain
- 07_applied_rates         : three mini-panels (water tank, population, marginal cost)
- 08_related_rates_intro   : 4-step numbered method box
- 09_related_rates_ladder  : ladder triangle + worked dy/dt
- 11_pause1_solution       : worked solution for balloon problem
- 12_linearization         : sqrt(x) curve + tangent line at x=4
- 13_lhopital_rule         : main rule + two refinement callouts
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
deck = Deck(course="AP Calculus AB", module_num=4, output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 4 — Contextual Applications of Differentiation",
    "~9 minutes  ·  Motion, related rates, linearization, L'Hospital",
)


# ─── 02 — hook (custom: ladder sliding down a wall) ──────────────────────
def hook(img, d):
    d.text((110, 80), "A ladder slides down a wall.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "The bottom moves at 1 ft/s. How fast does the top fall?",
           fill=MUTED, font=font("sans", 34))

    # Ground line + wall line (right triangle scene)
    # Wall on the left, ground at bottom. Ladder is the hypotenuse.
    ground_y = 880
    wall_x   = 380
    # Wall (vertical) and ground (horizontal)
    d.line([(wall_x, 320), (wall_x, ground_y)], fill=INK, width=6)
    d.line([(wall_x, ground_y), (W - 200, ground_y)], fill=INK, width=6)
    # Brick-ish hatching on the wall
    for k in range(8):
        y = 340 + k * 70
        d.line([(wall_x - 22, y), (wall_x, y)], fill=MUTED, width=2)
    # Ground hatching
    for k in range(14):
        x = wall_x + 30 + k * 70
        if x > W - 220:
            break
        d.line([(x, ground_y + 4), (x - 22, ground_y + 30)], fill=MUTED, width=2)

    # Ladder: from top-of-wall point (x=wall_x, y_top) to base (x_base, ground_y)
    y_top  = 400         # ladder top contact on the wall
    x_base = 1180        # ladder base on the ground
    # Two stiles
    d.line([(wall_x, y_top), (x_base, ground_y)], fill=deck.accent, width=12)
    d.line([(wall_x + 18, y_top - 14), (x_base + 18, ground_y - 14)],
           fill=deck.accent_light, width=8)
    # Rungs (perpendicular-ish, evenly spaced along the ladder)
    rungs = 8
    for k in range(1, rungs):
        t = k / rungs
        rx = wall_x + (x_base - wall_x) * t
        ry = y_top + (ground_y - y_top) * t
        # rung offset perpendicular to ladder direction
        dxL = (x_base - wall_x)
        dyL = (ground_y - y_top)
        length = math.hypot(dxL, dyL)
        nx = -dyL / length * 16
        ny =  dxL / length * 16
        d.line([(rx - nx, ry - ny), (rx + nx, ry + ny)],
               fill=MAROON_DARK, width=4)

    # Labels: x (along ground), y (along wall), 10 ft (ladder)
    # y label (wall height from ground to ladder top)
    d.text((wall_x - 70, (y_top + ground_y) // 2 - 20),
           "y", fill=MAROON, font=font("serif_bold", 60))
    # x label (ground from wall to base)
    d.text(((wall_x + x_base) // 2 - 14, ground_y + 36),
           "x", fill=MAROON, font=font("serif_bold", 60))
    # ladder length label, near middle of ladder, offset above
    mid_x = (wall_x + x_base) // 2
    mid_y = (y_top + ground_y) // 2
    d.text((mid_x + 30, mid_y - 90),
           "10 ft", fill=MAROON_DARK, font=font("sans_bold", 38))

    # Arrow at base showing 1 ft/s outward (to the right)
    arrow_y = ground_y + 90
    ax0 = x_base - 60
    ax1 = x_base + 140
    d.line([(ax0, arrow_y), (ax1, arrow_y)], fill=RED, width=6)
    # Arrowhead
    d.polygon([(ax1, arrow_y), (ax1 - 22, arrow_y - 14),
               (ax1 - 22, arrow_y + 14)], fill=RED)
    d.text((ax0 - 10, arrow_y + 18),
           "dx/dt = 1 ft/s", fill=RED, font=font("mono", 34))

    # Downward arrow at top of ladder showing top sliding down
    tax = wall_x - 70
    d.line([(tax, y_top - 60), (tax, y_top + 80)], fill=RED, width=6)
    d.polygon([(tax, y_top + 80), (tax - 14, y_top + 58),
               (tax + 14, y_top + 58)], fill=RED)
    d.text((tax - 110, y_top - 110),
           "dy/dt = ?", fill=RED, font=font("mono", 32))

    # Caption strip at bottom
    d.rounded_rectangle([110, 940, W - 110, 1040], radius=20, fill=deck.accent_light)
    centered(d, "As the ladder flattens, the top speeds up.  The derivative tells us exactly how fast.",
             font("sans_bold", 30), 968, MAROON_DARK)


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "The derivative as a real-world rate — with units.",
        "Related rates — when two quantities change together in time.",
        "Linearization for approximation  +  L'Hospital's Rule for limits.",
    ],
    footnote="Every applied-derivative problem on the AP exam reduces to one of these three moves.",
)


# ─── 04 — units of derivative (custom: table) ────────────────────────────
def units_table(img, d):
    d.text((110, 80), "Units of a derivative  =  units of f  ÷  units of x.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 160), "Always write the units. They tell you what the answer means.",
           fill=MUTED, font=font("sans", 32))

    # Table: 4 columns × 4 rows
    cols = ["Quantity  f", "Input  x", "Derivative  f'", "Units"]
    rows = [
        ("position  s(t)  [m]",   "time  t  [s]",         "velocity  s'(t)",   "m / s"),
        ("cost  C(x)  [$]",       "items  x",              "marginal cost  C'(x)", "$ / item"),
        ("distance  D(t)  [mi]",  "time  t  [hr]",        "speed  D'(t)",       "mi / hr  (mph)"),
        ("volume  V(t)  [L]",     "time  t  [min]",       "flow rate  V'(t)",   "L / min"),
    ]
    # Geometry
    table_x = 110
    table_y = 240
    table_w = W - 220
    col_widths = [int(table_w * 0.30), int(table_w * 0.22),
                  int(table_w * 0.27), 0]
    col_widths[3] = table_w - sum(col_widths[:3])
    row_h = 100

    # Header row
    cx = table_x
    for i, h in enumerate(cols):
        d.rectangle([cx, table_y, cx + col_widths[i], table_y + row_h],
                    fill=MAROON, outline=MAROON)
        tw = d.textlength(h, font=font("sans_bold", 30))
        d.text((cx + (col_widths[i] - tw) / 2, table_y + 32),
               h, fill=deck.bg, font=font("sans_bold", 30))
        cx += col_widths[i]

    # Body rows
    for r_idx, row in enumerate(rows):
        cx = table_x
        y0 = table_y + (r_idx + 1) * row_h
        bg = deck.card_bg if r_idx % 2 == 0 else deck.bg
        for i, cell in enumerate(row):
            d.rectangle([cx, y0, cx + col_widths[i], y0 + row_h],
                        fill=bg, outline=MAROON, width=2)
            text_color = MAROON if i == 3 else INK
            f_cell = font("mono", 26) if i == 3 else font("sans", 26)
            tw = d.textlength(cell, font=f_cell)
            d.text((cx + (col_widths[i] - tw) / 2, y0 + 35),
                   cell, fill=text_color, font=f_cell)
            cx += col_widths[i]

    # Footer callout
    d.rounded_rectangle([110, 800, W - 110, 960], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    centered(d, "Forgetting units is the #1 way to lose easy AP points.",
             font("sans_bold", 36), 825, MAROON_DARK)
    centered(d, "If C(x) is in dollars and x is widgets, then  C'(x)  is in  dollars per widget.",
             font("sans", 32), 880, MAROON_DARK)


deck.custom("04_units_of_derivative", units_table)


# ─── 05 — motion p-v-a (custom: derivative chain) ────────────────────────
def motion_pva(img, d):
    d.text((110, 80), "Motion — the position–velocity–acceleration chain.",
           fill=MAROON, font=font("serif_bold", 56))

    # Three stacked cards: s(t), v(t), a(t) with arrows between
    card_w = W - 220
    card_x = 110
    cards = [
        ("Position",     "s(t)",                    "where the object is",     INK),
        ("Velocity",     "v(t)  =  s'(t)",          "rate of change of position",  MAROON),
        ("Acceleration", "a(t)  =  v'(t)  =  s''(t)", "rate of change of velocity",  MAROON_DARK),
    ]
    card_h = 150
    gap = 30
    top = 220
    for i, (lbl, eqn, sub, color) in enumerate(cards):
        y0 = top + i * (card_h + gap)
        d.rounded_rectangle([card_x, y0, card_x + card_w, y0 + card_h],
                            radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        d.text((card_x + 40, y0 + 25), lbl, fill=MAROON,
               font=font("serif_bold", 36))
        d.text((card_x + 40, y0 + 80), sub, fill=MUTED,
               font=font("sans", 26))
        # Equation, right-aligned in card
        eqn_font = font("mono", 50)
        ew = d.textlength(eqn, font=eqn_font)
        d.text((card_x + card_w - ew - 60, y0 + 50),
               eqn, fill=color, font=eqn_font)
        # Down arrow between cards (except after last)
        if i < len(cards) - 1:
            ax = card_x + 80
            ay0 = y0 + card_h
            ay1 = ay0 + gap
            d.line([(ax, ay0), (ax, ay1)], fill=deck.accent, width=6)
            d.polygon([(ax, ay1), (ax - 12, ay1 - 14),
                       (ax + 12, ay1 - 14)], fill=deck.accent)
            d.text((ax + 24, ay0 + 2), "d/dt",
                   fill=deck.accent, font=font("mono", 24))

    # Bottom rule strip — speed sign rule
    d.rounded_rectangle([110, 780, W - 110, 960], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    centered(d, "Speed  =  |v(t)|",
             font("mono", 44), 800, MAROON_DARK)
    centered(d, "Speed is INCREASING when  v  and  a  have the SAME sign  (v · a > 0).",
             font("sans_bold", 30), 870, MAROON_DARK)
    centered(d, "Opposite signs → slowing down.",
             font("sans", 28), 915, MAROON_DARK)


deck.custom("05_motion_pva", motion_pva)


# ─── 06 — motion example (equation) ──────────────────────────────────────
deck.equation(
    "06_motion_example", "Example — particle motion at  t = 4.",
    [
        ("s(t) = t³ − 6t² + 9t",            INK,    "position"),
        ("v(t) = 3t² − 12t + 9  =  3(t−1)(t−3)", MUTED, "differentiate once"),
        ("a(t) = 6t − 12",                  MUTED,  "differentiate twice"),
        ("v(4) = +9   ·   a(4) = +12",     MAROON, "same sign  →  speeding up"),
    ],
)


# ─── 07 — applied rates (custom: 3 mini-panels) ──────────────────────────
def applied_rates(img, d):
    d.text((110, 80), "Same math, different units.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Every applied derivative is a ratio — output per input.",
           fill=MUTED, font=font("sans", 32))

    # Three side-by-side panels
    panel_w = 540
    panel_h = 520
    gap = 30
    total_w = panel_w * 3 + gap * 2
    start_x = (W - total_w) // 2
    top_y = 280

    panels = [
        ("Water flowing into a tank",
         "dV/dt",
         "liters / min",
         "tank"),
        ("Population growth",
         "dP/dt",
         "people / year",
         "population"),
        ("Marginal cost",
         "dC/dx",
         "dollars / item",
         "cost"),
    ]

    for i, (title, expr, units, kind) in enumerate(panels):
        x0 = start_x + i * (panel_w + gap)
        d.rounded_rectangle([x0, top_y, x0 + panel_w, top_y + panel_h],
                            radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        # Title
        d.text((x0 + 30, top_y + 30), title,
               fill=MAROON, font=font("serif_bold", 32))

        # Icon area (middle)
        icon_cx = x0 + panel_w // 2
        icon_cy = top_y + 230
        if kind == "tank":
            # Rectangle with water filled to ~60%
            tw, th = 220, 200
            tx0 = icon_cx - tw // 2
            ty0 = icon_cy - th // 2
            d.rectangle([tx0, ty0, tx0 + tw, ty0 + th],
                        outline=INK, width=5)
            # water fill
            fill_h = int(th * 0.55)
            d.rectangle([tx0 + 4, ty0 + th - fill_h, tx0 + tw - 4, ty0 + th - 4],
                        fill=deck.accent_light)
            # faucet/drip arrow above
            d.line([(icon_cx, ty0 - 60), (icon_cx, ty0 - 8)],
                   fill=deck.accent, width=6)
            d.polygon([(icon_cx, ty0 - 8), (icon_cx - 10, ty0 - 22),
                       (icon_cx + 10, ty0 - 22)], fill=deck.accent)
        elif kind == "population":
            # Three little person stick figures
            for k, dx_off in enumerate([-70, 0, 70]):
                px = icon_cx + dx_off
                py = icon_cy
                # head
                d.ellipse([px - 16, py - 70, px + 16, py - 38],
                          outline=MAROON, width=5, fill=deck.card_bg)
                # body
                d.line([(px, py - 38), (px, py + 30)], fill=MAROON, width=5)
                # arms
                d.line([(px - 28, py - 10), (px + 28, py - 10)],
                       fill=MAROON, width=5)
                # legs
                d.line([(px, py + 30), (px - 20, py + 70)], fill=MAROON, width=5)
                d.line([(px, py + 30), (px + 20, py + 70)], fill=MAROON, width=5)
            # up-arrow
            d.line([(icon_cx + 120, icon_cy + 40), (icon_cx + 120, icon_cy - 60)],
                   fill=deck.accent, width=6)
            d.polygon([(icon_cx + 120, icon_cy - 60),
                       (icon_cx + 108, icon_cy - 42),
                       (icon_cx + 132, icon_cy - 42)], fill=deck.accent)
        else:  # cost — dollar sign + bar chart
            for k, h in enumerate([60, 90, 130, 160]):
                bx = icon_cx - 130 + k * 60
                by = icon_cy + 70
                d.rectangle([bx, by - h, bx + 44, by], fill=deck.accent,
                            outline=MAROON, width=3)
            d.text((icon_cx - 30, icon_cy - 130), "$",
                   fill=MAROON, font=font("serif_bold", 80))

        # Expression
        d.text((x0 + 30, top_y + panel_h - 130), expr,
               fill=INK, font=font("mono", 44))
        # Units strip
        d.rounded_rectangle([x0 + 30, top_y + panel_h - 70,
                             x0 + panel_w - 30, top_y + panel_h - 25],
                            radius=12, fill=deck.accent_light)
        centered_units_x = x0 + panel_w // 2
        uw = d.textlength(units, font=font("sans_bold", 26))
        d.text((centered_units_x - uw / 2, top_y + panel_h - 62),
               units, fill=MAROON_DARK, font=font("sans_bold", 26))

    # Bottom footer
    d.rounded_rectangle([110, 840, W - 110, 960], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    centered(d, "The math is identical.  Only the units change.",
             font("sans_bold", 36), 875, MAROON_DARK)


deck.custom("07_applied_rates", applied_rates)


# ─── 08 — related rates intro (custom: 4-step method) ────────────────────
def related_rates_intro(img, d):
    d.text((110, 80), "Related rates — the 4-step method.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Two quantities changing in time, linked by one equation.",
           fill=MUTED, font=font("sans", 32))

    steps = [
        ("1", "Draw and label",
         "Sketch the scene. Put names on every length, angle, volume."),
        ("2", "Name variables as functions of  t",
         "Anything that's changing gets  (t).  Constants stay constants."),
        ("3", "Write one equation relating them",
         "Geometry, Pythagoras, volume, area — whatever ties the variables together."),
        ("4", "Differentiate w.r.t.  t,  THEN substitute",
         "Plugging in numbers BEFORE differentiating is the #1 mistake on this topic."),
    ]
    y0 = 250
    for i, (num, head, sub) in enumerate(steps):
        sy = y0 + i * 150
        # Number circle
        cx = 180
        cy = sy + 50
        d.ellipse([cx - 50, cy - 50, cx + 50, cy + 50],
                  outline=MAROON, width=5, fill=deck.accent)
        nw = d.textlength(num, font=font("serif_bold", 56))
        d.text((cx - nw / 2, cy - 38), num, fill=MAROON_DARK,
               font=font("serif_bold", 56))
        # Headline
        d.text((280, sy + 8), head, fill=INK, font=font("serif_bold", 40))
        d.text((280, sy + 70), sub, fill=MUTED, font=font("sans", 28))

    # Bottom emphasis strip
    d.rounded_rectangle([110, 900, W - 110, 1010], radius=20,
                        outline=RED, width=4, fill=deck.accent_light)
    centered(d, "Differentiate FIRST.  Substitute LAST.",
             font("sans_bold", 38), 928, MAROON_DARK)


deck.custom("08_related_rates_intro", related_rates_intro)


# ─── 09 — related rates ladder (custom: triangle + worked) ───────────────
def ladder_worked(img, d):
    d.text((110, 70), "Related rates — the ladder, worked.",
           fill=MAROON, font=font("serif_bold", 56))

    # LEFT half: triangle diagram
    # Right triangle with legs y (vertical) and x (horizontal)
    # Place wall at left, ground at bottom
    base_y = 760
    wall_x = 230
    # Scale so x=8, y=6 (3-4-5-ish flipped). Use ~75 px per unit.
    scale = 75
    x_units = 8
    y_units = 6
    x_base_px = wall_x + x_units * scale
    y_top_px  = base_y - y_units * scale

    # Wall (vertical leg) — y
    d.line([(wall_x, y_top_px), (wall_x, base_y)], fill=INK, width=6)
    # Ground (horizontal leg) — x
    d.line([(wall_x, base_y), (x_base_px, base_y)], fill=INK, width=6)
    # Hypotenuse — ladder (10)
    d.line([(wall_x, y_top_px), (x_base_px, base_y)], fill=deck.accent, width=10)
    # Right angle square
    sq = 22
    d.rectangle([wall_x, base_y - sq, wall_x + sq, base_y], outline=INK, width=3)

    # Labels: x along ground, y along wall, 10 on ladder
    d.text(((wall_x + x_base_px) // 2 - 20, base_y + 18),
           "x = 8", fill=MAROON, font=font("serif_bold", 38))
    d.text((wall_x - 110, (y_top_px + base_y) // 2 - 18),
           "y = 6", fill=MAROON, font=font("serif_bold", 38))
    mid_x = (wall_x + x_base_px) // 2
    mid_y = (y_top_px + base_y) // 2
    d.text((mid_x + 30, mid_y - 70),
           "10", fill=MAROON_DARK, font=font("sans_bold", 38))
    # small dx/dt arrow at base
    ar_y = base_y + 80
    d.line([(x_base_px - 50, ar_y), (x_base_px + 60, ar_y)],
           fill=RED, width=5)
    d.polygon([(x_base_px + 60, ar_y), (x_base_px + 42, ar_y - 10),
               (x_base_px + 42, ar_y + 10)], fill=RED)
    d.text((x_base_px - 110, ar_y + 16),
           "dx/dt = 1", fill=RED, font=font("mono", 26))

    # RIGHT half: worked steps card
    card_x = 1000
    card_y = 200
    card_w = W - 110 - card_x
    card_h = 720
    d.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, card_y + 25), "Solve.",
           fill=MAROON, font=font("serif_bold", 44))

    lines = [
        ("x² + y² = 100",                   INK,        "Pythagoras"),
        ("2x · dx/dt + 2y · dy/dt = 0",     MUTED,      "d/dt both sides"),
        ("dy/dt = − (x / y) · dx/dt",       INK,        "solve for dy/dt"),
        ("dy/dt = − (8 / 6) · 1",           MUTED,      "plug in  x=8, y=6"),
        ("dy/dt = − 4/3  ft/s",             MAROON,     "≈  − 1.33 ft/s"),
    ]
    ly = card_y + 110
    for txt, color, note in lines:
        d.text((card_x + 30, ly), txt, fill=color, font=font("mono", 34))
        if note:
            d.text((card_x + 30, ly + 50), note,
                   fill=deck.accent, font=font("sans_bold", 22))
        ly += 110

    # Footer band
    d.rounded_rectangle([110, 970, W - 110, 1050], radius=16,
                        fill=deck.accent_light)
    centered(d, "Negative sign  →  the top is falling.  And it's falling FASTER than the base slides.",
             font("sans_bold", 28), 990, MAROON_DARK)


deck.custom("09_related_rates_ladder", ladder_worked)


# ─── 10 — pause + silence duplicate ──────────────────────────────────────
deck.pause(
    "10_pause1", "PAUSE  &  TRY",
    "A balloon's radius grows at  dr/dt = 2 cm/s.  Find  dV/dt  when  r = 5 cm:",
    "V = (4/3)π r³",
    hint="Differentiate V with respect to t.  Pause. Solve. Press play when ready.",
)

deck.duplicate("10_pause1", "10_pause1_silence")


# ─── 11 — pause1 solution (worked) ───────────────────────────────────────
deck.equation(
    "11_pause1_solution", "Solution — balloon problem.",
    [
        ("V  =  (4/3)π r³",                         INK,    "given formula"),
        ("dV/dt  =  4π r² · dr/dt",                 MUTED,  "chain rule on r(t)"),
        ("dV/dt  =  4π (5)² (2)",                   MUTED,  "substitute  r=5,  dr/dt=2"),
        ("dV/dt  =  200π  cm³/s",                   MAROON, "≈  628.3 cm³ / s"),
    ],
)


# ─── 12 — linearization (custom: curve + tangent) ────────────────────────
def linearization(img, d):
    d.text((110, 70), "Linearization — local tangent-line approximation.",
           fill=MAROON, font=font("serif_bold", 50))
    d.text((110, 145), "Near a point, a smooth curve looks like its tangent line.",
           fill=MUTED, font=font("sans", 30))

    # LEFT card: formula + when-to-use
    card_x = 110
    card_y = 230
    card_w = 820
    card_h = 740
    d.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, card_y + 25), "The formula",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((card_x + 30, card_y + 95),
           "L(x) = f(a) + f'(a)(x − a)",
           fill=INK, font=font("mono", 36))

    d.text((card_x + 30, card_y + 200), "When do you use it?",
           fill=MAROON, font=font("serif_bold", 32))
    note_lines = [
        "When you need to approximate  f(b),",
        "and  b  is close to some  a  where",
        "both  f(a)  and  f'(a)  are easy to",
        "compute exactly.",
    ]
    for k, line in enumerate(note_lines):
        d.text((card_x + 30, card_y + 270 + k * 44), line,
               fill=INK, font=font("sans", 30))

    # Worked example block
    d.rounded_rectangle([card_x + 30, card_y + 480,
                         card_x + card_w - 30, card_y + 710],
                        radius=14, fill=deck.accent_light)
    d.text((card_x + 50, card_y + 495), "Estimate  √4.1",
           fill=MAROON_DARK, font=font("serif_bold", 32))
    ex_lines = [
        "Anchor  a = 4   (we know  √4 = 2).",
        "f'(x) = 1 / (2√x)   →   f'(4) = 1/4.",
        "L(4.1) = 2 + (1/4)(0.1) = 2.025.",
        "True value:  2.0248...    Stunningly close.",
    ]
    for k, line in enumerate(ex_lines):
        d.text((card_x + 50, card_y + 540 + k * 40), line,
               fill=INK, font=font("mono", 24))

    # RIGHT: the curve y = sqrt(x) with tangent line at x=4
    gx0 = 1000
    gy0 = 280
    gw  = 800
    gh  = 620
    # Axes
    d.line([(gx0, gy0 + gh), (gx0 + gw, gy0 + gh)], fill=INK, width=3)
    d.line([(gx0, gy0), (gx0, gy0 + gh)], fill=INK, width=3)
    d.text((gx0 + gw - 30, gy0 + gh + 10), "x",
           fill=INK, font=font("serif_ital", 32))
    d.text((gx0 - 40, gy0 - 10), "y",
           fill=INK, font=font("serif_ital", 32))

    # Pixel scale: x in [0, 9], y in [0, 3.5]
    x_max = 9.0
    y_max = 3.5
    sx = gw / x_max
    sy = gh / y_max

    def pt(xv, yv):
        return (gx0 + xv * sx, gy0 + gh - yv * sy)

    # y = sqrt(x) curve
    prev = None
    xv = 0.0
    while xv <= x_max:
        yv = math.sqrt(xv)
        p = pt(xv, yv)
        if prev is not None:
            d.line([prev, p], fill=MAROON, width=5)
        prev = p
        xv += 0.05

    # Tangent line at a=4: y = 2 + (1/4)(x - 4)
    def tang(xv):
        return 2 + 0.25 * (xv - 4)
    # Draw across a window
    t_x0 = 1.5
    t_x1 = 7.5
    d.line([pt(t_x0, tang(t_x0)), pt(t_x1, tang(t_x1))],
           fill=MAROON_DARK, width=4)

    # Anchor point at (4, 2)
    apt = pt(4, 2)
    d.ellipse([apt[0] - 10, apt[1] - 10, apt[0] + 10, apt[1] + 10],
              fill=MAROON_DARK)
    d.text((apt[0] + 14, apt[1] - 10), "(4, 2)",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # Approximation point at x=4.1
    bpt = pt(4.1, tang(4.1))
    d.ellipse([bpt[0] - 8, bpt[1] - 8, bpt[0] + 8, bpt[1] + 8],
              outline=deck.accent, width=4, fill=deck.bg)
    d.text((bpt[0] + 14, bpt[1] - 30),
           "L(4.1) = 2.025", fill=deck.accent,
           font=font("sans_bold", 24))

    # Curve label
    d.text((gx0 + 360, gy0 + 60), "y = √x",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((gx0 + 360, gy0 + 120), "tangent at a = 4",
           fill=MAROON_DARK, font=font("sans", 26))

    # x-axis ticks for 0..9
    for tick in range(int(x_max) + 1):
        tp = pt(tick, 0)
        d.line([(tp[0], tp[1]), (tp[0], tp[1] + 8)], fill=INK, width=2)
        d.text((tp[0] - 6, tp[1] + 12), str(tick),
               fill=MUTED, font=font("sans", 22))


deck.custom("12_linearization", linearization)


# ─── 13 — L'Hospital's Rule (custom: main rule + refinements) ────────────
def lhopital(img, d):
    d.text((110, 70), "L'Hospital's Rule.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "Rescues limits that look like  0/0  or  ∞/∞.",
           fill=MUTED, font=font("sans", 32))

    # Main rule banner
    d.rounded_rectangle([110, 230, W - 110, 380], radius=20,
                        outline=MAROON, width=5, fill=deck.accent_light)
    centered(d, "If  lim  f(x)/g(x)  is  0/0  or  ∞/∞,  then",
             font("sans_bold", 32), 252, MAROON_DARK)
    centered(d, "lim  f(x) / g(x)   =   lim  f'(x) / g'(x).",
             font("mono", 44), 305, MAROON_DARK)

    # Two refinement callout boxes side by side
    box_w = (W - 220 - 30) // 2
    box_h = 520
    box_y = 420

    # LEFT — must rearrange first
    lx = 110
    d.rounded_rectangle([lx, box_y, lx + box_w, box_y + box_h],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((lx + 30, box_y + 25),
           "Rearrange other forms FIRST",
           fill=MAROON, font=font("serif_bold", 30))
    d.text((lx + 30, box_y + 90),
           "0·∞,  ∞−∞,  0⁰,  1^∞,  ∞⁰",
           fill=INK, font=font("mono", 30))
    d.text((lx + 30, box_y + 140),
           "are indeterminate, but L'Hospital",
           fill=MUTED, font=font("sans", 26))
    d.text((lx + 30, box_y + 175),
           "doesn't apply until you rewrite",
           fill=MUTED, font=font("sans", 26))
    d.text((lx + 30, box_y + 210),
           "them as  0/0  or  ∞/∞.",
           fill=MUTED, font=font("sans", 26))
    # Example
    d.text((lx + 30, box_y + 280), "Example.",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((lx + 30, box_y + 325),
           "lim  x · ln x   (x → 0⁺)",
           fill=INK, font=font("mono", 26))
    d.text((lx + 30, box_y + 365),
           "is  0 · ∞.  Rewrite as",
           fill=MUTED, font=font("sans", 26))
    d.text((lx + 30, box_y + 400),
           "ln x  /  (1/x)   →   ∞/∞.",
           fill=INK, font=font("mono", 28))
    d.text((lx + 30, box_y + 445),
           "Now L'Hospital applies.",
           fill=deck.accent, font=font("sans_bold", 26))

    # RIGHT — apply repeatedly
    rx = 110 + box_w + 30
    d.rounded_rectangle([rx, box_y, rx + box_w, box_y + box_h],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((rx + 30, box_y + 25),
           "Apply REPEATEDLY if still 0/0",
           fill=MAROON, font=font("serif_bold", 30))
    d.text((rx + 30, box_y + 90),
           "lim  (1 − cos x) / x²",
           fill=INK, font=font("mono", 30))
    d.text((rx + 30, box_y + 145),
           "is  0/0.  Differentiate top & bottom:",
           fill=MUTED, font=font("sans", 24))
    d.text((rx + 30, box_y + 200),
           "→   sin x / (2x)",
           fill=INK, font=font("mono", 30))
    d.text((rx + 30, box_y + 250),
           "still  0/0.  Apply again:",
           fill=MUTED, font=font("sans", 24))
    d.text((rx + 30, box_y + 300),
           "→   cos x / 2",
           fill=INK, font=font("mono", 30))
    d.text((rx + 30, box_y + 360),
           "Evaluate:  cos 0 / 2  =  1/2.",
           fill=MAROON, font=font("mono", 28))
    d.text((rx + 30, box_y + 440),
           "Two applications. Both legal.",
           fill=deck.accent, font=font("sans_bold", 26))


deck.custom("13_lhopital_rule", lhopital)


# ─── 14 — L'Hospital trap (compare) ──────────────────────────────────────
deck.compare(
    "14_lhopital_trap",
    "L'Hospital trap — check the form FIRST.",
    left={
        "label": "✓ LEGAL",
        "color": MAROON,
        "lines": [
            "lim x→0   sin x / x",
            "Check form:  sin 0 / 0  =  0/0.",
            "Indeterminate — rule applies.",
            "→  lim  cos x / 1  =  1.",
        ],
        "footnote": "0/0 confirmed → differentiate top & bottom.",
    },
    right={
        "label": "✗ ILLEGAL",
        "color": RED,
        "lines": [
            "lim x→0   cos x / 1",
            "Check form:  cos 0 / 1  =  1/1.",
            "NOT indeterminate.  Just plug in.",
            "Applying L'Hospital here is wrong.",
        ],
        "footnote": "Even if you accidentally get the right answer, you lose the point.",
    },
)


# ─── 15 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "15_recap", "Recap.",
    [
        "Units of  f'(x)  =  units of  f  /  units of  x.  Always write them.",
        "Motion chain:  s → v = s' → a = v''.  Speed grows when  v·a > 0.",
        "Related rates:  differentiate w.r.t.  t  FIRST, substitute LAST.",
        "Linearization:  L(x) = f(a) + f'(a)(x − a).  Tangent-line approximation.",
        "L'Hospital:  only for  0/0  or  ∞/∞.  Check the form first.",
    ],
    assignment=[
        "GIIS Module 4 problem set — 8 free-response style problems.",
        "Due Friday.  Submit through the Learn Portal.",
    ],
)


# ─── 16 — path ───────────────────────────────────────────────────────────
deck.path(
    "16_path",
    items=[
        ("✓",  "Watch this lesson",              "(done!)"),
        ("1.", "OpenStax Calculus Vol 1",        "Read chapters 4.1 – 4.7"),
        ("2.", "Khan Academy practice",          "AP Calc AB · Unit 4 — Contextual Applications"),
        ("3.", "Assignment in dashboard",        "Module 4 problem set  ·  8 problems"),
        ("4.", "Advisor check-in",               "Book if related rates still feel fuzzy"),
    ],
    next_text="Next up:  Module 5 — Mean Value Theorem, Extreme Value Theorem, and the derivative tests.",
)


print("AP Calc AB Module 4 slides built.")

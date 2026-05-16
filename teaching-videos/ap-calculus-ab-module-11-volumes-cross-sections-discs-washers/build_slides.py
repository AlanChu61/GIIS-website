"""AP Calculus AB · Module 11 — Volumes: Cross-Sections, Discs, and Washers.

Built on slide_kit (math theme = gold + cream).
Custom slides:
- 02_hook            : a "loaf of bread" sliced into cross-sections, showing
                       V = sum of slice areas * thickness
- 07_disc_setup      : region under y = sqrt(x) on [0, 4] revolved around the
                       x-axis, with one representative disc drawn through the
                       solid; labels R(x) = sqrt(x), thickness dx
- 13_axis_choice     : side-by-side decision diagram: horizontal axis -> dx,
                       vertical axis -> dy, with the slice direction drawn in
                       each case
"""
import sys
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H, wrap,
    INK, MAROON, MAROON_DARK, MUTED, RED, CREAM, PARCHMENT, GRID,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Calculus AB", module_num=11,
            output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 11 — Volumes: Cross-Sections, Discs & Washers",
    "~10 minutes  ·  Unit 8(b) · CHA 8.7 – 8.12",
)


# ─── 02 — hook (custom: loaf-of-bread sliced into cross-sections) ────────
def hook_loaf(img, d):
    d.text((110, 70), "Volume  =  stack of cross-sections.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158),
           "Slice a loaf.  Each slice has area A(x).  Stack them with thickness dx.",
           fill=MUTED, font=font("sans", 34))

    # Draw a "loaf" as a series of stacked slices going off to the right
    # (slight perspective). Each slice is a rectangle with rounded top.
    base_y = 720           # bottom of loaf
    top_y = 360            # top of crust
    loaf_left = 240
    n_slices = 18
    slice_w = 56           # visible thickness of each slice
    skew = 6               # x-shift per slice for parallel projection feel
    loaf_h = base_y - top_y

    # Each slice: front rectangle slightly taller in the middle of the loaf
    # to evoke a loaf shape, slimmer toward the ends.
    for i in range(n_slices):
        # height envelope: low at ends, tall in the middle
        u = i / (n_slices - 1)
        env = 0.55 + 0.45 * math.sin(math.pi * u)  # 0.55 .. 1.0 .. 0.55
        h_i = int(loaf_h * env)
        x0 = loaf_left + i * slice_w + i * 2
        y0 = base_y - h_i
        x1 = x0 + slice_w
        y1 = base_y
        # slice "face" (rounded top corners)
        d.rounded_rectangle([x0, y0, x1, y1], radius=14,
                            fill=deck.accent_light, outline=MAROON_DARK, width=3)
        # subtle inner shading line
        d.line([(x0 + 6, y0 + 18), (x1 - 6, y0 + 18)],
               fill=deck.accent, width=2)

    # Bracket showing thickness dx on one slice
    bracket_i = 6
    bx0 = loaf_left + bracket_i * slice_w + bracket_i * 2
    bx1 = bx0 + slice_w
    by = base_y + 30
    d.line([(bx0, by), (bx1, by)], fill=MAROON, width=4)
    d.line([(bx0, by - 10), (bx0, by + 10)], fill=MAROON, width=4)
    d.line([(bx1, by - 10), (bx1, by + 10)], fill=MAROON, width=4)
    d.text(((bx0 + bx1) // 2 - 24, by + 18), "dx",
           fill=MAROON, font=font("serif_bold", 36))

    # Arrow + label "A(x) = area of this slice" pointing into the loaf
    arrow_target_x = loaf_left + (n_slices // 2) * (slice_w + 2) + slice_w // 2
    arrow_target_y = top_y + 30
    arrow_x0 = arrow_target_x + 200
    arrow_y0 = arrow_target_y - 60
    d.line([(arrow_x0, arrow_y0), (arrow_target_x + 10, arrow_target_y + 5)],
           fill=MAROON_DARK, width=4)
    d.polygon([(arrow_target_x + 10, arrow_target_y + 5),
               (arrow_target_x + 30, arrow_target_y - 6),
               (arrow_target_x + 28, arrow_target_y + 18)],
              fill=MAROON_DARK)
    d.text((arrow_x0 - 60, arrow_y0 - 40), "A(x)  =  area of one slice",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    # Bottom formula card
    card_y = 830
    card_h = 170
    d.rounded_rectangle([110, card_y, W - 110, card_y + card_h],
                        radius=22, outline=MAROON, width=5, fill=deck.card_bg)
    centered(d, "V  =  ∫ₐᵇ  A(x)  dx",
             font("mono", 80), card_y + 30, MAROON)
    centered(d, "Discs and washers are just the case where A(x) is a circle.",
             font("sans_bold", 28), card_y + 125, MUTED)


deck.custom("02_hook", hook_loaf)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Solids with KNOWN cross-sections (squares, semicircles, triangles).",
        "DISC method — region touches the axis  →  each slice is a circle.",
        "WASHER method — region does NOT touch the axis  →  each slice has a hole.",
    ],
    footnote="Every volumes FRQ asks one of these three.  The setup point is everything.",
)


# ─── 04 — cross-sections setup (definition) ──────────────────────────────
deck.definition(
    "04_cross_sections_setup",
    "Solids with known cross-sections.",
    "V  =  ∫ₐᵇ  A(x)  dx",
    "Side length s  comes from the base region (usually top − bottom).  "
    "Plug s into the area formula for the shape.  Then integrate.",
)


# ─── 05 — cross-sections, squares (equation) ─────────────────────────────
deck.equation(
    "05_cross_sections_squares",
    "SQUARE cross-sections.   Base:  y = √x  and x-axis  on  [0, 4].",
    [
        ("s(x)  =  √x   (top − bottom)",          MUTED,  "side length from the base"),
        ("A(x)  =  s²   =   x",                    INK,    "square ⇒ area = s²"),
        ("V  =  ∫₀⁴  x  dx   =   [ x²/2 ]₀⁴",      INK,    "integrate the area function"),
        ("    =   16/2   =   8",                   MAROON, "volume = 8 cubic units"),
    ],
)


# ─── 06 — three shape formulas (equation as cheat-sheet) ─────────────────
deck.equation(
    "06_cross_sections_other_shapes",
    "Three shape formulas you MUST memorize.",
    [
        ("SQUARE                A  =  s²",                          INK,    None),
        ("EQUILATERAL TRIANGLE  A  =  (√3 / 4) · s²",               INK,    None),
        ("SEMICIRCLE (s = diam) A  =  (π / 8) · s²",                INK,    "radius = s/2, half of π r²"),
        ("",                                                         INK,    None),
        ("Trap: s is the DIAMETER of the semicircle — NOT the radius.", MAROON, "AP exam loves this slip"),
    ],
)


# ─── 07 — disc setup (custom: revolution diagram) ────────────────────────
def disc_setup(img, d):
    d.text((110, 70), "Disc method — every slice is a circle.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158),
           "Region under  y = √x  on  [0, 4]  revolved around the x-axis.",
           fill=MUTED, font=font("sans", 34))

    # Axes: x runs across the slide, y up. Place axis low (the axis of revolution)
    ax_y = 720
    ax_x0 = 200
    ax_x1 = 1400
    d.line([(ax_x0, ax_y), (ax_x1, ax_y)], fill=INK, width=3)
    d.polygon([(ax_x1, ax_y), (ax_x1 - 18, ax_y - 10),
               (ax_x1 - 18, ax_y + 10)], fill=INK)
    d.text((ax_x1 + 12, ax_y - 16), "x", fill=INK, font=font("serif_ital", 30))

    # Plot region: x from 0 to 4 (scale 230 px / unit -> width 920 px), y from 0 to 2 (scale 200 px / unit)
    x_min, x_max = 0, 4
    y_min, y_max = 0, 2
    sx = 230
    sy = 200
    origin_x = ax_x0 + 60

    def to_px(xv, yv):
        return (origin_x + xv * sx, ax_y - yv * sy)

    # x ticks 1..4
    for xv in [1, 2, 3, 4]:
        px, _ = to_px(xv, 0)
        d.line([(px, ax_y - 6), (px, ax_y + 6)], fill=INK, width=2)
        d.text((px - 8, ax_y + 12), str(xv), fill=INK, font=font("sans", 22))

    # Draw the SOLID OF REVOLUTION as a horn: a series of nested ellipses
    # (foreshortened discs) along the x-axis, each with horizontal radius small
    # and vertical radius equal to f(x) = sqrt(x).
    # We fill them as the "side" of the horn (top half above axis, bottom half below).
    # Use accent_light as the body color, MAROON for the outline.
    n = 80
    for i in range(n):
        xv = x_max * (i / (n - 1))
        r_y = math.sqrt(xv) * sy
        cx, cy = to_px(xv, 0)
        r_x = 18  # ellipse horizontal radius (depth illusion)
        # Filled ellipse (disc rim)
        if i % 2 == 0:
            d.ellipse([cx - r_x, cy - r_y, cx + r_x, cy + r_y],
                      fill=deck.accent_light)

    # Top outline: y = sqrt(x) on [0, 4]
    pts_top = []
    pts_bot = []
    xv = 0
    while xv <= x_max + 0.001:
        px, py = to_px(xv, math.sqrt(xv))
        pts_top.append((px, py))
        px2, py2 = to_px(xv, -math.sqrt(xv))
        pts_bot.append((px2, py2))
        xv += 0.04
    for a_pt, b_pt in zip(pts_top[:-1], pts_top[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)
    for a_pt, b_pt in zip(pts_bot[:-1], pts_bot[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)

    # End disc at x = 4 (full ellipse, slightly darker outline)
    end_x, _ = to_px(4, 0)
    r_end = math.sqrt(4) * sy
    d.ellipse([end_x - 22, ax_y - r_end, end_x + 22, ax_y + r_end],
              outline=MAROON_DARK, width=5)

    # Highlight one representative disc at x = 2.25 (vertical) — show as a vertical line
    # with arrow, labelled R(x) = sqrt(x).
    rep_x = 2.25
    rep_px, _ = to_px(rep_x, 0)
    rep_r_y = math.sqrt(rep_x) * sy
    # Draw the representative disc as a thicker, darker-edged ellipse
    d.ellipse([rep_px - 20, ax_y - rep_r_y, rep_px + 20, ax_y + rep_r_y],
              outline=MAROON_DARK, width=4)
    # Radius line from axis to top of curve at rep_x
    d.line([(rep_px, ax_y), (rep_px, ax_y - rep_r_y)],
           fill=MAROON_DARK, width=4)
    # Label "R(x) = √x"
    d.text((rep_px + 30, ax_y - rep_r_y // 2 - 18),
           "R(x) = √x", fill=MAROON_DARK, font=font("serif_bold", 30))

    # Bracket "thickness dx" along the axis at the rep disc
    d.line([(rep_px - 25, ax_y + rep_r_y + 22),
            (rep_px + 25, ax_y + rep_r_y + 22)], fill=MAROON, width=3)
    d.line([(rep_px - 25, ax_y + rep_r_y + 12),
            (rep_px - 25, ax_y + rep_r_y + 32)], fill=MAROON, width=3)
    d.line([(rep_px + 25, ax_y + rep_r_y + 12),
            (rep_px + 25, ax_y + rep_r_y + 32)], fill=MAROON, width=3)
    d.text((rep_px - 14, ax_y + rep_r_y + 40), "dx",
           fill=MAROON, font=font("serif_bold", 28))

    # Right-side formula card
    card_x = 1480
    d.rounded_rectangle([card_x, 260, W - 100, 760], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 25, 280), "Disc formula.",
           fill=MAROON, font=font("serif_bold", 42))
    d.text((card_x + 25, 360), "Area of disc:",
           fill=INK, font=font("sans_bold", 28))
    d.text((card_x + 25, 405), "  π · R(x)²",
           fill=INK, font=font("mono", 38))
    d.text((card_x + 25, 490), "Stack along axis:",
           fill=INK, font=font("sans_bold", 28))
    d.text((card_x + 25, 540), "         ⌠ b",
           fill=INK, font=font("mono", 32))
    d.text((card_x + 25, 580), "V = π · │  R(x)² dx",
           fill=MAROON, font=font("mono", 32))
    d.text((card_x + 25, 620), "         ⌡ a",
           fill=INK, font=font("mono", 32))
    d.text((card_x + 25, 700), "(region must TOUCH axis)",
           fill=MUTED, font=font("sans", 24))


deck.custom("07_disc_setup", disc_setup)


# ─── 08 — disc example, x-axis (equation) ────────────────────────────────
deck.equation(
    "08_disc_example_x_axis",
    "DISC.   y = √x  on  [0, 4]  revolved around the x-axis.",
    [
        ("R(x)  =  √x",                            MUTED,  "function value = radius"),
        ("V  =  π · ∫₀⁴  (√x)²  dx",                INK,    "stack the disc areas"),
        ("    =  π · ∫₀⁴  x  dx",                   INK,    "(√x)² = x"),
        ("    =  π · [ x²/2 ]₀⁴   =   8π",          MAROON, "volume = 8π"),
    ],
)


# ─── 09 — disc around other axis (equation) ──────────────────────────────
deck.equation(
    "09_disc_around_other_axis",
    "DISC around  y = −1.   Same region.   Shift the radius.",
    [
        ("axis:  y = −1   (below the region)",      MUTED,  "axis of revolution"),
        ("R(x)  =  √x − (−1)  =  √x + 1",           INK,    "DISTANCE from curve to axis"),
        ("V  =  π · ∫₀⁴  (√x + 1)²  dx",            MAROON, "setup — NOT the same as 8π"),
        ("",                                         INK,    None),
        ("Rule:  revolve around  y = k  →  shift every radius by k.", MAROON, "memorize this"),
    ],
)


# ─── 10 — washer setup (definition) ──────────────────────────────────────
deck.definition(
    "10_washer_setup",
    "Washer method — region does NOT touch the axis.",
    "V  =  π · ∫ₐᵇ  ( R² − r² )  dx",
    "Outer radius R, inner radius r.  Square first, THEN subtract.  "
    "Writing (R − r)² is the #1 wrong-setup error on Section II.",
)


# ─── 11 — washer example (equation) ──────────────────────────────────────
deck.equation(
    "11_washer_example",
    "WASHER.   y = x  and  y = x²  on  [0, 1]  around the x-axis.",
    [
        ("Line is on TOP of parabola on (0, 1).",   MUTED,  "identify outer / inner"),
        ("Outer R = x        Inner r = x²",          INK,    "farther from axis = outer"),
        ("V = π · ∫₀¹ ( x² − x⁴ ) dx",               INK,    "square FIRST, then subtract"),
        ("  = π · [ x³/3 − x⁵/5 ]₀¹",                INK,    "antiderivative"),
        ("  = π · (1/3 − 1/5)  =  2π / 15",          MAROON, "volume = 2π/15"),
    ],
)


# ─── 12 — washer around other axis (equation) ────────────────────────────
deck.equation(
    "12_washer_around_other_axis",
    "WASHER around  y = 2.   Same region.   Radii FLIP.",
    [
        ("axis:  y = 2   (above both curves)",      MUTED,  "axis is on the OTHER side"),
        ("Parabola sits LOWER  →  farther from y=2", MUTED,  "outer = farthest from axis"),
        ("Outer R = 2 − x²      Inner r = 2 − x",    INK,    "distances to y = 2"),
        ("V = π · ∫₀¹ ((2 − x²)² − (2 − x)²) dx",    MAROON, "setup — radii swapped"),
    ],
)


# ─── 13 — axis choice (custom: dx vs dy decision diagram) ────────────────
def axis_choice(img, d):
    d.text((110, 70), "Slice PERPENDICULAR to the axis of revolution.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 148),
           "Horizontal axis  →  vertical slices  →  dx.   "
           "Vertical axis  →  horizontal slices  →  dy.",
           fill=MUTED, font=font("sans", 30))

    # Two side-by-side panels
    panel_top = 230
    panel_bot = 900
    panel_h = panel_bot - panel_top
    gap = 60
    pw = (W - 220 - gap) // 2
    left_x = 110
    right_x = left_x + pw + gap

    for panel_x, label, sub, axis_dir in [
        (left_x, "Axis is HORIZONTAL",
         "y = k   or   x-axis", "h"),
        (right_x, "Axis is VERTICAL",
         "x = k   or   y-axis", "v"),
    ]:
        d.rounded_rectangle([panel_x, panel_top, panel_x + pw, panel_bot],
                            radius=22, outline=MAROON, width=5, fill=deck.card_bg)
        d.text((panel_x + 30, panel_top + 20), label,
               fill=MAROON, font=font("serif_bold", 42))
        d.text((panel_x + 30, panel_top + 80), sub,
               fill=MUTED, font=font("sans", 30))

        # Mini graph inside each panel
        g_x0 = panel_x + 60
        g_y0 = panel_top + 160
        g_x1 = panel_x + pw - 60
        g_y1 = panel_bot - 220
        g_w = g_x1 - g_x0
        g_h = g_y1 - g_y0

        # Background grid
        for gx in range(g_x0, g_x1, 50):
            d.line([(gx, g_y0), (gx, g_y1)], fill=GRID, width=1)
        for gy in range(g_y0, g_y1, 50):
            d.line([(g_x0, gy), (g_x1, gy)], fill=GRID, width=1)

        # Axes (origin at lower-left of mini graph)
        d.line([(g_x0, g_y1), (g_x1, g_y1)], fill=INK, width=3)
        d.line([(g_x0, g_y1), (g_x0, g_y0)], fill=INK, width=3)

        # A simple curve: y = sqrt(x) ish, scaled
        pts = []
        steps = 40
        for i in range(steps + 1):
            t = i / steps  # 0..1
            xv = t * g_w
            yv = math.sqrt(t) * g_h * 0.9
            pts.append((g_x0 + xv, g_y1 - yv))
        for a_pt, b_pt in zip(pts[:-1], pts[1:]):
            d.line([a_pt, b_pt], fill=MAROON, width=5)

        if axis_dir == "h":
            # Axis of revolution = the horizontal bottom line (x-axis itself).
            # Make it bold and red-ish.
            d.line([(g_x0, g_y1), (g_x1, g_y1)], fill=RED, width=6)
            d.text((g_x1 - 130, g_y1 + 12), "axis: y = k",
                   fill=RED, font=font("sans_bold", 24))
            # Slices: vertical strips (dx)
            for sx_pos in range(g_x0 + 40, g_x1 - 20, 60):
                t = (sx_pos - g_x0) / g_w
                yv = math.sqrt(t) * g_h * 0.9
                d.line([(sx_pos, g_y1), (sx_pos, g_y1 - yv)],
                       fill=deck.accent, width=4)
            # Big "dx" callout
            d.text((panel_x + 30, panel_bot - 180),
                   "→  slice VERTICALLY",
                   fill=MAROON_DARK, font=font("sans_bold", 30))
            d.text((panel_x + 30, panel_bot - 130),
                   "→  integrate  dx",
                   fill=MAROON, font=font("serif_bold", 44))
            d.text((panel_x + 30, panel_bot - 70),
                   "curves as functions of x",
                   fill=MUTED, font=font("sans", 26))
        else:
            # Axis of revolution = the vertical left line (y-axis itself).
            d.line([(g_x0, g_y0), (g_x0, g_y1)], fill=RED, width=6)
            d.text((g_x0 - 10, g_y0 - 32), "axis: x = k",
                   fill=RED, font=font("sans_bold", 24))
            # Slices: horizontal strips (dy)
            for sy_pos in range(g_y0 + 30, g_y1 - 10, 50):
                # Find x where curve is at this height
                # yv = sqrt(t) * g_h * 0.9  → t = (yv / (0.9 g_h))**2
                yv = g_y1 - sy_pos
                t = (yv / (0.9 * g_h)) ** 2
                if t > 1:
                    t = 1
                end_x = g_x0 + t * g_w
                d.line([(g_x0, sy_pos), (end_x, sy_pos)],
                       fill=deck.accent, width=4)
            # Big "dy" callout
            d.text((panel_x + 30, panel_bot - 180),
                   "→  slice HORIZONTALLY",
                   fill=MAROON_DARK, font=font("sans_bold", 30))
            d.text((panel_x + 30, panel_bot - 130),
                   "→  integrate  dy",
                   fill=MAROON, font=font("serif_bold", 44))
            d.text((panel_x + 30, panel_bot - 70),
                   "curves as functions of y",
                   fill=MUTED, font=font("sans", 26))

    # Bottom mnemonic strip
    d.rounded_rectangle([110, 920, W - 110, 1000], radius=18,
                        fill=deck.accent_light)
    centered(d, "Slice ⊥ axis of revolution.  Same disc / washer formulas — just swap dx ↔ dy.",
             font("sans_bold", 32), 940, MAROON_DARK)


deck.custom("13_axis_choice", axis_choice)


# ─── 14 — pause ─────────────────────────────────────────────────────────
deck.pause(
    "14_pause1", "PAUSE  &  TRY",
    "Region between  y = x²  and  y = 4,  revolved around the x-axis.",
    "Disc or washer ?   Find  V.",
    hint="Identify outer / inner radii  →  find the bounds  →  π ∫ (R² − r²) dx.  "
         "Pause.  Solve.  Press play when ready.",
)
deck.duplicate("14_pause1", "15_pause1_silence")


# ─── 16 — compare: shift trap (compare) ─────────────────────────────────
deck.compare(
    "16_compare_shift",
    "AP trap — revolution around  y = k  ≠ 0.  Forgetting the shift.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "Asked to revolve around y = −1.",
            "Used  R = √x  (just the function).",
            "V = π ∫₀⁴ (√x)² dx  =  8π.",
            "",
            "That's the volume around the",
            "x-AXIS — not around y = −1.",
        ],
        "footnote": "Same setup as the x-axis case.  Shift was dropped.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "Axis y = −1 is BELOW the region.",
            "R  =  DISTANCE from curve to axis",
            "R  =  √x − (−1)  =  √x + 1.",
            "",
            "V = π ∫₀⁴ (√x + 1)² dx.",
            "Different number.",
        ],
        "footnote": "Revolve around y = k  →  shift every radius by k.",
    },
)


# ─── 17 — traps summary (definition with checklist feel) ─────────────────
def traps_summary(img, d):
    d.text((110, 80), "Five checks before you write the final volume answer.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 168),
           "Most FRQ points lost on this topic come from these five things.",
           fill=MUTED, font=font("sans", 32))

    checks = [
        ("1.", "Did I include  π  ?",
         "Disc and washer integrals always carry a π."),
        ("2.", "Did I square FIRST, then subtract?",
         "Washer:  (R² − r²).   Never  (R − r)²."),
        ("3.", "Did I shift the radii by  k  ?",
         "Revolving around y = k means R = (curve − k)."),
        ("4.", "Is  dx / dy  perpendicular to the axis of revolution?",
         "Horizontal axis ⇒ dx.   Vertical axis ⇒ dy."),
        ("5.", "Cross-sections:  side length s in the right area formula?",
         "Square: s².  Equilateral △: (√3/4)s².  Semicircle (s=diam): (π/8)s²."),
    ]
    y = 260
    for num, head, sub in checks:
        d.text((140, y), num, fill=deck.accent, font=font("serif_bold", 50))
        d.text((230, y), head, fill=INK, font=font("serif_bold", 34))
        d.text((230, y + 46), sub, fill=MUTED, font=font("sans", 26))
        y += 130


deck.custom("17_traps_summary", traps_summary)


# ─── 18 — recap ─────────────────────────────────────────────────────────
deck.recap(
    "18_recap", "Recap.",
    [
        "Cross-sections:  V = ∫ₐᵇ A(x) dx.   Plug s into the shape formula.",
        "Disc:  V = π ∫ R(x)² dx   (region TOUCHES the axis).",
        "Washer:  V = π ∫ (R² − r²) dx   (region does NOT touch the axis).",
        "Square first, THEN subtract.   Never (R − r)².",
        "Around y = k:  shift every radius by k.",
        "Slice perpendicular to the axis of revolution.   dx vs. dy.",
    ],
    assignment=[
        "GIIS Unit 8b Set  —  4 volume problems  +  1 with a shifted axis.",
        "Submit through the dashboard.  Advisor reviews within 48 hours.",
    ],
)


# ─── 19 — path ──────────────────────────────────────────────────────────
deck.path(
    "19_path",
    items=[
        ("✓",  "Watch this lesson",         "(done!)"),
        ("1.", "OpenStax Calculus Vol 2",   "Chapter 6 — volumes by slicing (cross-sections, disc, washer)"),
        ("2.", "Khan Academy practice",     "AP Calculus AB · Unit 8 — Volumes lessons"),
        ("3.", "Assignment in dashboard",   "GIIS Unit 8b Set — 4 volume problems incl. 1 with a shifted axis"),
        ("4.", "Advisor check-in",          "Book 15 min if shifted-axis radii still feel fuzzy"),
    ],
    next_text="Next up:  Module 12 — Differential Equations and Slope Fields.",
)


print("AP Calculus AB Module 11 slides built.")

"""Algebra I — Module 8: Graphing Linear Equations.

Mix of slide_kit deck calls + custom slides for the graphs / Cartesian plane.
"""
import sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from PIL import Image, ImageDraw
from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, CREAM, GRID,
)

deck = Deck(course="Algebra I", module_num=8,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

ACCENT = deck.accent          # gold for math
ACCENT_LIGHT = deck.accent_light
CARD = deck.card_bg

# ─── helpers for custom graph slides ──────────────────────────────────

def draw_axes(d, cx, cy, span=300, step=50, x_range=None, y_range=None, label=True):
    """Cartesian grid centered at (cx, cy)."""
    for i in range(-span, span + 1, step):
        d.line([(cx - span, cy + i), (cx + span, cy + i)], fill=GRID, width=1)
        d.line([(cx + i, cy - span), (cx + i, cy + span)], fill=GRID, width=1)
    d.line([(cx - span, cy), (cx + span, cy)], fill=INK, width=3)
    d.line([(cx, cy - span), (cx, cy + span)], fill=INK, width=3)
    fnt = font("sans", 22)
    # tick labels at every step in unit terms
    units_x = x_range if x_range else range(-(span // step), span // step + 1)
    for u in units_x:
        if u == 0:
            continue
        px = cx + u * step
        if abs(px - cx) > span:
            continue
        d.text((px - 8, cy + 8), str(u), fill=MUTED, font=fnt)
    units_y = y_range if y_range else range(-(span // step), span // step + 1)
    for u in units_y:
        if u == 0:
            continue
        py = cy - u * step
        if abs(py - cy) > span:
            continue
        d.text((cx + 8, py - 12), str(u), fill=MUTED, font=fnt)
    if label:
        d.text((cx + span + 20, cy - 14), "x", fill=INK, font=font("sans_bold", 32))
        d.text((cx - 14, cy - span - 44), "y", fill=INK, font=font("sans_bold", 32))


def to_px(cx, cy, x, y, step=50):
    return cx + x * step, cy - y * step


def plot_line(d, cx, cy, p1, p2, step=50, color=MAROON, span=300,
              label_points=True, point_color=None):
    x1, y1 = p1
    x2, y2 = p2
    px1, py1 = to_px(cx, cy, x1, y1, step)
    px2, py2 = to_px(cx, cy, x2, y2, step)
    dx, dy = px2 - px1, py2 - py1
    mag = max(1, math.hypot(dx, dy))
    ux, uy = dx / mag, dy / mag
    extend = span
    d.line([(px1 - ux * extend, py1 - uy * extend),
            (px2 + ux * extend, py2 + uy * extend)],
           fill=color, width=5)
    pc = point_color or MAROON_DARK
    for px, py in [(px1, py1), (px2, py2)]:
        d.ellipse([px - 12, py - 12, px + 12, py + 12], fill=pc,
                  outline=CREAM, width=3)
    if label_points:
        d.text((px1 + 16, py1 - 42), f"({x1}, {y1})", fill=INK,
               font=font("sans_bold", 26))
        d.text((px2 + 16, py2 - 42), f"({x2}, {y2})", fill=INK,
               font=font("sans_bold", 26))


# ═════════════════════════════════════════════════════════════════════
# 01 — title
deck.title("01_title", "Algebra I",
           "Module 8 — Graphing Linear Equations",
           "Sample lesson  ·  ~6 minutes")

# ═════════════════════════════════════════════════════════════════════
# 02 — hook: Uber pricing — show equation + tiny plotted line
def hook_render(img, d):
    d.text((110, 90), "Uber: $2.50 base  +  $1.50 / mile.",
           fill=MAROON, font=font("serif_bold", 64))
    # The equation, centered
    centered(d, "y  =  1.5 x  +  2.5", font("mono", 110), 230, MAROON_DARK)
    # Mini axes & line on right
    cx, cy = 1300, 660
    draw_axes(d, cx, cy, span=250, step=50, label=True)
    # plot y = 1.5x + 2.5 from x=0 to x=4 (origin shifted: only first quadrant relevant)
    p1 = (0, 2.5)
    p2 = (4, 8.5)
    px1, py1 = to_px(cx, cy, *p1)
    px2, py2 = to_px(cx, cy, *p2)
    # only need to clip into visible area
    d.line([(px1, py1), (px2, py2)], fill=MAROON, width=6)
    d.ellipse([px1 - 10, py1 - 10, px1 + 10, py1 + 10], fill=ACCENT,
              outline=MAROON, width=3)
    d.text((px1 + 18, py1 - 8), "(0, 2.5)", fill=INK, font=font("sans_bold", 24))
    # Left side message
    d.text((110, 480), "An equation is just a line", fill=INK,
           font=font("sans", 44))
    d.text((110, 540), "you haven't drawn yet.", fill=INK,
           font=font("sans", 44))
    d.text((110, 660), "Seeing it is faster than", fill=ACCENT,
           font=font("sans_bold", 38))
    d.text((110, 710), "reading the numbers.", fill=ACCENT,
           font=font("sans_bold", 38))

deck.custom("02_hook", hook_render)

# ═════════════════════════════════════════════════════════════════════
# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Decode the slope-intercept form  y = m x + b.",
    "Plot any line straight from its equation.",
    "Read a graph backwards into an equation.",
], footnote="Equations and graphs are two views of the same thing.")

# ═════════════════════════════════════════════════════════════════════
# 04 — Cartesian recap
def cartesian_render(img, d):
    d.text((110, 90), "The Cartesian plane.", fill=MAROON,
           font=font("serif_bold", 76))
    cx, cy = W // 2, 580
    draw_axes(d, cx, cy, span=320, step=60, label=True)
    # Origin point
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=MAROON_DARK)
    d.text((cx + 18, cy + 10), "origin (0, 0)", fill=MUTED,
           font=font("sans_bold", 26))
    # Quadrant labels — Roman numerals
    quads = [("I",  cx + 200, cy - 200),
             ("II", cx - 220, cy - 200),
             ("III", cx - 220, cy + 170),
             ("IV", cx + 200, cy + 170)]
    for q, qx, qy in quads:
        d.text((qx, qy), q, fill=ACCENT, font=font("serif_bold", 56))
    # caption
    centered(d, "Two axes.  Four quadrants.  Every point gets (x, y).",
             font("sans", 38), 920, MUTED)

deck.custom("04_cartesian_recap", cartesian_render)

# ═════════════════════════════════════════════════════════════════════
# 05 — slope-intercept form
deck.equation("05_slope_intercept", "Slope-intercept form.", [
    ("y  =  m x  +  b",     MAROON,      "m = slope,  b = y-intercept"),
    ("y  =  2 x  +  3",     INK,         "slope 2,  y-intercept 3"),
    ("rise/run = 2,  cross y at 3", MUTED,  "two numbers → one line"),
])

# ═════════════════════════════════════════════════════════════════════
# 06 — plot from equation: y = 2x + 3
def plot_eq_render(img, d):
    d.text((110, 90), "Plot  y = 2x + 3.", fill=MAROON,
           font=font("serif_bold", 76))
    cx, cy = 700, 600
    draw_axes(d, cx, cy, span=320, step=50, label=True)
    # y-intercept (0, 3)
    p1 = (0, 3)
    p2 = (1, 5)
    px1, py1 = to_px(cx, cy, *p1)
    px2, py2 = to_px(cx, cy, *p2)
    # Draw a long line
    dx, dy = px2 - px1, py2 - py1
    mag = max(1, math.hypot(dx, dy))
    ux, uy = dx / mag, dy / mag
    d.line([(px1 - ux * 350, py1 - uy * 350),
            (px2 + ux * 350, py2 + uy * 350)],
           fill=MAROON, width=5)
    # rise (vertical) + run (horizontal) construction marks
    d.line([(px1, py1), (px1 + 50, py1)], fill=ACCENT, width=4)
    d.line([(px1 + 50, py1), (px1 + 50, py1 - 100)], fill=ACCENT, width=4)
    d.text((px1 + 10, py1 + 8), "run 1", fill=ACCENT,
           font=font("sans_bold", 24))
    d.text((px1 + 58, py1 - 60), "rise 2", fill=ACCENT,
           font=font("sans_bold", 24))
    # Points
    for px, py in [(px1, py1), (px2, py2)]:
        d.ellipse([px - 12, py - 12, px + 12, py + 12], fill=MAROON_DARK,
                  outline=CREAM, width=3)
    d.text((px1 - 140, py1 - 12), "(0, 3)", fill=INK,
           font=font("sans_bold", 26))
    d.text((px2 + 22, py2 - 16), "(1, 5)", fill=INK,
           font=font("sans_bold", 26))
    # Steps panel right
    rx = 1280
    d.text((rx, 220), "1.  y-intercept  →  (0, 3)", fill=INK,
           font=font("sans", 34))
    d.text((rx, 290), "2.  slope 2  →  up 2,  right 1", fill=INK,
           font=font("sans", 34))
    d.text((rx, 360), "3.  Mark (1, 5)", fill=INK,
           font=font("sans", 34))
    d.text((rx, 430), "4.  Connect.  Extend.", fill=INK,
           font=font("sans", 34))
    d.text((rx, 540), "Done.", fill=MAROON,
           font=font("serif_bold", 56))

deck.custom("06_plot_from_eq", plot_eq_render)

# ═════════════════════════════════════════════════════════════════════
# 07 — table method for y = -x + 4
deck.equation("07_table_method", "Table method:  y = −x + 4", [
    ("x = 0   →   y = 4",  INK,    None),
    ("x = 1   →   y = 3",  INK,    None),
    ("x = 2   →   y = 2",  INK,    None),
    ("plot, connect, extend", MAROON, "three points line up — that's the line"),
])

# ═════════════════════════════════════════════════════════════════════
# 08 — intercepts of 2x + 3y = 12
deck.equation("08_intercepts", "Intercepts:  2x + 3y = 12", [
    ("y = 0  →  2x = 12  →  x = 6",   INK,    "x-intercept  (6, 0)"),
    ("x = 0  →  3y = 12  →  y = 4",   INK,    "y-intercept  (0, 4)"),
    ("plot (6, 0) and (0, 4) — connect",   MAROON, "two points, one line"),
])

# ═════════════════════════════════════════════════════════════════════
# 09 — pause 1
deck.pause("09_pause1", "PAUSE  &  TRY", "Plot the line:",
           "y  =  −x  +  4",
           hint="Y-intercept = 4.   Slope = −1  (down 1, right 1).")

# 10 — pause 1 silence (duplicate)
deck.duplicate("09_pause1", "10_pause1_silence")

# ═════════════════════════════════════════════════════════════════════
# 11 — parallel & perpendicular
def parallel_perp_render(img, d):
    d.text((110, 90), "Parallel  vs  perpendicular.", fill=MAROON,
           font=font("serif_bold", 70))

    # Left panel — parallel
    d.rounded_rectangle([110, 230, 920, 880], radius=24, outline=MAROON,
                        width=4, fill=CARD)
    d.text((150, 260), "Parallel", fill=MAROON, font=font("serif_bold", 56))
    d.text((150, 330), "same slope", fill=ACCENT,
           font=font("sans_bold", 36))
    cx, cy = 515, 600
    # mini axes
    span = 180
    for i in range(-span, span + 1, 40):
        d.line([(cx - span, cy + i), (cx + span, cy + i)], fill=GRID, width=1)
        d.line([(cx + i, cy - span), (cx + i, cy + span)], fill=GRID, width=1)
    d.line([(cx - span, cy), (cx + span, cy)], fill=INK, width=2)
    d.line([(cx, cy - span), (cx, cy + span)], fill=INK, width=2)
    # two parallel lines slope 1
    d.line([(cx - span, cy + span - 40), (cx + span, cy - span - 40)],
           fill=MAROON, width=5)
    d.line([(cx - span, cy + span + 40), (cx + span, cy - span + 40)],
           fill=MAROON_DARK, width=5)
    d.text((150, 830), "y = x + 2     y = x − 2", fill=INK,
           font=font("mono", 32))

    # Right panel — perpendicular
    d.rounded_rectangle([1000, 230, 1810, 880], radius=24, outline=MAROON,
                        width=4, fill=CARD)
    d.text((1040, 260), "Perpendicular", fill=MAROON,
           font=font("serif_bold", 56))
    d.text((1040, 330), "negative reciprocals", fill=ACCENT,
           font=font("sans_bold", 36))
    cx2, cy2 = 1405, 600
    for i in range(-span, span + 1, 40):
        d.line([(cx2 - span, cy2 + i), (cx2 + span, cy2 + i)], fill=GRID, width=1)
        d.line([(cx2 + i, cy2 - span), (cx2 + i, cy2 + span)], fill=GRID, width=1)
    d.line([(cx2 - span, cy2), (cx2 + span, cy2)], fill=INK, width=2)
    d.line([(cx2, cy2 - span), (cx2, cy2 + span)], fill=INK, width=2)
    # slope 2 line + slope -1/2 line through origin
    # slope 2: from (-90, +180) to (90, -180)
    d.line([(cx2 - 90, cy2 + 180), (cx2 + 90, cy2 - 180)],
           fill=MAROON, width=5)
    # slope -1/2: from (-180, +90) to (180, -90)... that's negative reciprocal of 2
    d.line([(cx2 - 180, cy2 - 90), (cx2 + 180, cy2 + 90)],
           fill=MAROON_DARK, width=5)
    d.text((1040, 830), "y = 2x       y = −½ x", fill=INK,
           font=font("mono", 32))

    centered(d, "Multiply the slopes — perpendicular gives you −1.",
             font("sans_bold", 32), 940, ACCENT)

deck.custom("11_parallel_perp", parallel_perp_render)

# ═════════════════════════════════════════════════════════════════════
# 12 — real world Uber
def uber_render(img, d):
    d.text((110, 90), "Uber pricing as a line.", fill=MAROON,
           font=font("serif_bold", 72))
    centered(d, "y  =  1.5 x  +  2.5", font("mono", 80), 200, MAROON_DARK)

    # Graph on left
    cx, cy = 600, 700
    # axes — only show first quadrant style
    span_x_units = 8
    span_y_units = 14
    step = 35
    # grid + axis
    for i in range(0, span_x_units + 1):
        x = cx + i * step
        d.line([(x, cy), (x, cy - span_y_units * step)], fill=GRID, width=1)
    for j in range(0, span_y_units + 1):
        y = cy - j * step
        d.line([(cx, y), (cx + span_x_units * step, y)], fill=GRID, width=1)
    d.line([(cx, cy), (cx + span_x_units * step, cy)], fill=INK, width=3)  # x
    d.line([(cx, cy), (cx, cy - span_y_units * step)], fill=INK, width=3)  # y
    # ticks
    fnt = font("sans", 22)
    for i in range(0, span_x_units + 1, 2):
        d.text((cx + i * step - 6, cy + 6), str(i), fill=MUTED, font=fnt)
    for j in range(0, span_y_units + 1, 2):
        d.text((cx - 30, cy - j * step - 10), str(j), fill=MUTED, font=fnt)
    d.text((cx + span_x_units * step + 12, cy - 10), "miles",
           fill=INK, font=font("sans_bold", 26))
    d.text((cx - 8, cy - span_y_units * step - 36), "$",
           fill=INK, font=font("sans_bold", 30))

    # line: y = 1.5x + 2.5 from x=0 (y=2.5) to x=8 (y=14.5 → clipped to 14)
    p1 = (cx + 0 * step, cy - 2.5 * step)
    p2 = (cx + 8 * step, cy - 14.5 * step)
    d.line([p1, p2], fill=MAROON, width=6)
    # y-intercept dot
    d.ellipse([p1[0] - 11, p1[1] - 11, p1[0] + 11, p1[1] + 11],
              fill=ACCENT, outline=MAROON, width=3)
    # 10-mile point — out of frame, so mark at 8 miles → y = 14.5
    d.ellipse([p2[0] - 11, p2[1] - 11, p2[0] + 11, p2[1] + 11],
              fill=MAROON_DARK, outline=CREAM, width=3)

    # arrow + callouts
    d.text((p1[0] + 18, p1[1] - 6), "base fee $2.50", fill=ACCENT,
           font=font("sans_bold", 26))
    d.text((p2[0] - 220, p2[1] - 36), "$1.50 per mile", fill=ACCENT,
           font=font("sans_bold", 26))

    # Right column — readable insights
    rx = 1180
    d.text((rx, 340), "·  y-intercept  =  $2.50", fill=INK,
           font=font("sans", 38))
    d.text((rx + 50, 388), "base fee, before moving", fill=MUTED,
           font=font("sans", 28))
    d.text((rx, 460), "·  slope  =  $1.50", fill=INK,
           font=font("sans", 38))
    d.text((rx + 50, 508), "cost per mile", fill=MUTED,
           font=font("sans", 28))
    d.text((rx, 600), "·  10 mi  →  ≈ $17.50", fill=MAROON,
           font=font("serif_bold", 40))
    d.text((rx + 50, 660), "read it off the line", fill=ACCENT,
           font=font("sans_bold", 28))

deck.custom("12_real_world", uber_render)

# ═════════════════════════════════════════════════════════════════════
# 13 — compare: x,y order
deck.compare("13_compare", "Common trap:  (x, y) order.",
    left={
        "label": "✗  WRONG",
        "color": RED,
        "lines": [
            "Reading (3, 2) as:",
            "   up 3, then right 2.",
            "",
            "You end up at the wrong",
            "spot — every single time.",
        ],
        "footnote": "Flipping x and y is the #1 plotting error.",
    },
    right={
        "label": "✓  RIGHT",
        "color": MAROON,
        "lines": [
            "Reading (3, 2) as:",
            "   right 3, then up 2.",
            "",
            "x first  (horizontal),",
            "then y  (vertical).",
        ],
        "footnote": "Say it out loud the first 10 times.  It sticks.",
    })

# ═════════════════════════════════════════════════════════════════════
# 14 — recap
deck.recap("14_recap", "Recap.", [
    "Slope-intercept form:  y = m x + b.   m = slope,  b = y-intercept.",
    "Three ways to plot:  slope-intercept, intercepts, or a table of points.",
    "Same slope  →  parallel.   Negative-reciprocal slopes  →  perpendicular.",
    "Always plot (x, y) — horizontal first, then vertical.",
], assignment=[
    "Graph 4 lines from their equations.",
    "Then  write equations from 2 graphs.",
    "Submit through your Learn Portal dashboard.",
])

# ═════════════════════════════════════════════════════════════════════
# 15 — path
deck.path("15_path",
    items=[
        ("✓",  "Watch this lesson",            "(done!)"),
        ("1.", "Read OpenStax Ch 3.2",         "Graph Linear Equations in Two Variables"),
        ("2.", "Khan Academy practice",        "20 problems · Graphing slope-intercept form"),
        ("3.", "Assignment in dashboard",      "4 lines to plot  +  2 graphs to decode"),
        ("4.", "Advisor check-in",             "Book a session if anything still feels foggy"),
    ],
    next_text="Next up:  Module 9 — Slope and Rate of Change.")

print("Slides built.")

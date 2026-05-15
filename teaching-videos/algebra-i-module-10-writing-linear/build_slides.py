"""Module 10 — Writing Linear Equations.

Built end-to-end on slide_kit.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="Algebra I", module_num=10,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "Algebra I",
           "Module 10 — Writing Linear Equations",
           "Sample lesson  ·  ~7 minutes")

# 02 — hook  (custom: gym example with two facts → infinite predictions)
def hook(img, d):
    d.text((110, 90), "Two facts.  Infinite predictions.",
           fill=MAROON, font=font("serif_bold", 64))
    # Two-fact card
    d.rounded_rectangle([110, 230, W-110, 460], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((150, 260), "The gym:", fill=MUTED, font=font("sans_bold", 36))
    centered(d, "$30 join fee   +   $15 / month",
             font("serif_bold", 72), 330, INK)
    # Question line below the card
    d.text((110, 490), "...what will you have paid at month 6?  Month 12?  Month 30?",
           fill=deck.accent, font=font("sans_bold", 32))
    # Three prediction badges
    preds = [("Month 6", "$120"), ("Month 12", "$210"), ("Month 30", "$480")]
    box_w, gap = 480, 60
    total_w = 3*box_w + 2*gap
    start_x = (W - total_w) // 2
    for i, (label, value) in enumerate(preds):
        x0 = start_x + i*(box_w + gap)
        d.rounded_rectangle([x0, 560, x0 + box_w, 800], radius=20,
                            outline=MAROON, width=4, fill=deck.card_bg)
        d.text((x0 + 40, 590), label, fill=MUTED, font=font("sans_bold", 36))
        centered_x = x0 + box_w/2 - d.textlength(value, font=font("mono", 96))/2
        d.text((centered_x, 660), value, fill=MAROON, font=font("mono", 96))
    d.text((110, 880),
           "One equation handles every month.  That's what we're writing today.",
           fill=deck.accent, font=font("sans_bold", 32))
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Write from slope + y-intercept.",
    "Write from a point + slope (point-slope form).",
    "Write from two points.",
    "Bonus: parallel and perpendicular lines.",
], footnote="Any facts about a line → its equation.  Every time.")

# 04 — slope-intercept recap
deck.definition("04_slope_intercept_recap",
                "Slope-intercept form.",
                "y = m x + b",
                sub="m = slope    ·    b = y-intercept")

# 05 — from slope + y-intercept
deck.equation("05_from_slope_yint",
              "Slope = 4,   y-intercept = −1",
              [
                  ("m = 4,   b = −1", MUTED, "drop them into  y = mx + b"),
                  ("y = 4x + (−1)",   INK,   None),
                  ("y = 4x − 1",      MAROON, "done — straight plug-in"),
              ])

# 06 — point-slope form definition
deck.definition("06_point_slope_form",
                "Point-slope form.",
                "y − y₁ = m (x − x₁)",
                sub="Use this when you have a slope + ANY point on the line.")

# 07 — from point + slope
deck.equation("07_from_point_slope",
              "Slope = 3,   point (2, 7)",
              [
                  ("y − 7 = 3 (x − 2)", INK,   "plug in m, x₁, y₁"),
                  ("y − 7 = 3x − 6",    MUTED, "distribute the 3"),
                  ("y = 3x + 1",        MAROON, "add 7 to both sides"),
              ])

# 08 — from two points
deck.equation("08_from_two_points",
              "Points (1, 2) and (3, 8)",
              [
                  ("m = (8 − 2) / (3 − 1) = 3", MUTED, "step 1 — find the slope"),
                  ("y − 2 = 3 (x − 1)",         INK,   "step 2 — use point-slope"),
                  ("y = 3x − 1",                MAROON, "simplify"),
              ])

# 09 / 10 — pause-and-try
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Write the equation of the line through:",
           "(2, 5)   and   (4, 11)",
           hint="Find slope first, then use point-slope.")
deck.duplicate("09_pause1", "10_pause1_silence")

# 11 — parallel
deck.equation("11_parallel_lines",
              "Parallel to  y = 2x + 5,  through (3, 1)",
              [
                  ("parallel ⟹ same slope:   m = 2", MUTED, None),
                  ("y − 1 = 2 (x − 3)",              INK,   "point-slope"),
                  ("y = 2x − 5",                     MAROON, "same slope, new y-intercept"),
              ])

# 12 — perpendicular
deck.equation("12_perpendicular_lines",
              "Perpendicular to  y = 2x + 5,  through (3, 1)",
              [
                  ("perp ⟹ slope is  −1/2", MUTED, "flip and change sign"),
                  ("y − 1 = −½ (x − 3)",     INK,   "point-slope"),
                  ("y = −½ x + 5/2",         MAROON, "now it crosses at 90°"),
              ])

# 13 — real world (custom: gym equation + predictions table)
def real_world(img, d):
    d.text((110, 90), "Back to the gym.",
           fill=MAROON, font=font("serif_bold", 72))
    # Big equation
    centered(d, "y = 15 x  +  30",
             font("mono", 130), 220, MAROON)
    d.text((110, 400), "$15/month is the slope  ·  $30 join fee is the y-intercept",
           fill=deck.accent, font=font("sans_bold", 32))
    # Predictions table
    d.rounded_rectangle([110, 500, W-110, 880], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((150, 530), "Predictions",
           fill=MAROON, font=font("serif_bold", 44))
    rows = [
        ("Month  6:", "15 × 6  + 30",  "= $120"),
        ("Month 12:", "15 × 12 + 30",  "= $210"),
        ("Month 30:", "15 × 30 + 30",  "= $480"),
    ]
    y = 620
    for label, calc, ans in rows:
        d.text((180, y), label, fill=INK,    font=font("mono", 44))
        d.text((480, y), calc,  fill=MUTED,  font=font("mono", 44))
        d.text((1100, y), ans,  fill=MAROON, font=font("mono", 44))
        y += 70
deck.custom("13_real_world", real_world)

# 14 — horizontal & vertical (custom: two mini-cards side by side)
def horiz_vert(img, d):
    d.text((110, 90), "Two special cases.",
           fill=MAROON, font=font("serif_bold", 80))
    # Horizontal card
    d.rounded_rectangle([110, 260, 920, 820], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((150, 300), "Horizontal", fill=MAROON, font=font("serif_bold", 52))
    d.text((150, 370), "slope = 0", fill=MUTED, font=font("sans", 36))
    centered_x = 110 + (920-110)/2 - d.textlength("y = 4", font=font("mono", 130))/2
    d.text((centered_x, 460), "y = 4", fill=INK, font=font("mono", 130))
    # mini horizontal line
    d.line([(200, 650), (830, 650)], fill=MAROON, width=8)
    d.text((150, 760), "flat line at height 4",
           fill=deck.accent, font=font("sans_bold", 30))
    # Vertical card
    d.rounded_rectangle([1000, 260, 1810, 820], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((1040, 300), "Vertical", fill=MAROON, font=font("serif_bold", 52))
    d.text((1040, 370), "slope is undefined", fill=MUTED, font=font("sans", 36))
    centered_x2 = 1000 + (1810-1000)/2 - d.textlength("x = −2", font=font("mono", 130))/2
    d.text((centered_x2, 460), "x = −2", fill=INK, font=font("mono", 130))
    # mini vertical line
    d.line([(1755, 600), (1755, 740)], fill=MAROON, width=8)
    d.text((1040, 760), "straight up-down at x = −2",
           fill=deck.accent, font=font("sans_bold", 30))
deck.custom("14_horizontal_vertical", horiz_vert)

# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Slope-intercept form (y = mx + b) when you have slope + y-intercept.",
    "Point-slope form (y − y₁ = m(x − x₁)) when you have slope + any point.",
    "Two points?  Find slope first, then plug into point-slope.",
    "Parallel = same slope.   Perpendicular = negative reciprocal.",
], assignment=[
    "Write 5 equations from different inputs:",
    "slope + y-int  ·  slope + point  ·  two points  ·  parallel  ·  perpendicular.",
])

# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Ch 3.4",    "Find the Equation of a Line"),
    ("2.", "Khan Academy practice",   "Writing linear equations · 15 problems"),
    ("3.", "Assignment in dashboard", "5 equations from various inputs · show work"),
    ("4.", "Advisor check-in",        "Book 15 min if point-slope still feels awkward"),
], next_text="Next up:  Module 11 — Systems of Equations.")

print("Module 10 (Writing Linear Equations) slides built via slide_kit.")

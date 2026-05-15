"""Module 11 — Systems of Linear Equations.

Built end-to-end on slide_kit. Mix of definitions, equations, and custom
slides for the graphing method, classification cases, word problem setup,
and method-picker.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, GRID,
)

deck = Deck(course="Algebra I", module_num=11,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")


# 01 — title
deck.title("01_title", "Algebra I",
           "Module 11 — Systems of Linear Equations",
           "Sample lesson  ·  ~9 minutes")


# 02 — hook  (custom: movie theater problem)
def hook(img, d):
    d.text((110, 90), "Two unknowns. One system.", fill=MAROON,
           font=font("serif_bold", 64))
    # Scenario card
    d.rounded_rectangle([110, 220, W - 110, 560], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((160, 260), "Movie theater problem.", fill=MAROON,
           font=font("serif_bold", 48))
    lines = [
        "14 tickets sold for $128 total.",
        "Adult ticket  =  $12.",
        "Child ticket  =  $7.",
        "How many adults?  How many children?",
    ]
    y = 340
    for line in lines:
        d.text((160, y), line, fill=INK, font=font("sans", 38))
        y += 55
    # Two pill boxes: unknown 1 and unknown 2
    pill_w, pill_h, gap = 600, 130, 80
    left_x = (W - 2 * pill_w - gap) // 2
    right_x = left_x + pill_w + gap
    d.rounded_rectangle([left_x, 640, left_x + pill_w, 640 + pill_h],
                        radius=20, fill=MAROON)
    centered_a = left_x + pill_w / 2 - d.textlength("a  =  adults",
                                                    font=font("mono", 56)) / 2
    d.text((centered_a, 665), "a  =  adults", fill=deck.accent,
           font=font("mono", 56))
    d.rounded_rectangle([right_x, 640, right_x + pill_w, 640 + pill_h],
                        radius=20, fill=MAROON)
    centered_c = right_x + pill_w / 2 - d.textlength("c  =  children",
                                                     font=font("mono", 56)) / 2
    d.text((centered_c, 665), "c  =  children", fill=deck.accent,
           font=font("mono", 56))
    # Caption
    d.text((110, 850), "One equation can't pin down two unknowns.   "
                       "You need a SYSTEM.",
           fill=deck.accent, font=font("sans_bold", 36))
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "What a system of equations is.",
    "Method 1 — graphing.",
    "Method 2 — substitution.",
    "Method 3 — elimination  (plus: which to pick when).",
], footnote="By the end, word problems with two unknowns will be routine.")


# 04 — what is a system
deck.definition("04_what_is", "What is a system?",
                "Two or more equations sharing the same variables.",
                "Solution = the (x, y) pair that makes ALL equations true at once.")


# 05 — graphing method  (custom: cartesian plane with two intersecting lines)
def graphing_method(img, d):
    d.text((110, 90), "Method 1  ·  Graphing.", fill=MAROON,
           font=font("serif_bold", 64))
    # Plane setup
    cx, cy = W // 2, 560
    unit = 55          # pixels per unit
    x_range = 7        # -7 ... 7
    y_range = 5        # -2 ... 7  (asymmetric below)

    plane_left   = cx - x_range * unit
    plane_right  = cx + x_range * unit
    plane_top    = cy - (y_range + 2) * unit       # top extends a bit for y up to 7
    plane_bottom = cy + 2 * unit                    # bottom for y down to -2

    # Grid
    for i in range(-x_range, x_range + 1):
        x = cx + i * unit
        d.line([(x, plane_top), (x, plane_bottom)], fill=GRID, width=1)
    for j in range(-2, y_range + 3):
        y = cy - j * unit
        d.line([(plane_left, y), (plane_right, y)], fill=GRID, width=1)
    # Axes
    d.line([(plane_left, cy), (plane_right, cy)], fill=INK, width=3)   # x-axis
    d.line([(cx, plane_top), (cx, plane_bottom)], fill=INK, width=3)    # y-axis
    # Axis labels
    d.text((plane_right + 10, cy - 18), "x", fill=INK,
           font=font("serif_bold", 32))
    d.text((cx + 10, plane_top - 4), "y", fill=INK,
           font=font("serif_bold", 32))

    # Line 1:  y = x + 1   from x=-3 to x=6
    def to_px(xu, yu):
        return (cx + xu * unit, cy - yu * unit)
    p1a = to_px(-3, -2)
    p1b = to_px(6, 7)
    d.line([p1a, p1b], fill=MAROON, width=5)

    # Line 2:  y = -x + 5   from x=-2 to x=6
    p2a = to_px(-2, 7)
    p2b = to_px(6, -1)
    d.line([p2a, p2b], fill=deck.accent, width=5)

    # Intersection point (2, 3)
    ix, iy = to_px(2, 3)
    d.ellipse([ix - 12, iy - 12, ix + 12, iy + 12],
              fill=MAROON_DARK, outline=INK, width=2)
    # Intersection label
    d.text((ix + 20, iy - 50), "(2, 3)", fill=MAROON_DARK,
           font=font("serif_bold", 36))

    # Legend on the left
    d.text((110, 220), "y = x + 1", fill=MAROON,
           font=font("mono", 44))
    d.text((110, 280), "y = −x + 5", fill=deck.accent,
           font=font("mono", 44))
    d.text((110, 360), "→  cross at  (2, 3)", fill=INK,
           font=font("sans_bold", 32))

    # Caption
    d.text((110, 920),
           "Plot both lines.  Where they cross IS the solution.   "
           "Slow — and only exact when the intersection lands on grid.",
           fill=deck.accent, font=font("sans_bold", 28))
deck.custom("05_graphing_method", graphing_method)


# 06 — substitution intro
deck.definition("06_substitution_intro", "Method 2  ·  Substitution.",
                "Solve one equation for one variable, plug it into the other.",
                "Best when one variable is already isolated  (e.g. y = …).")


# 07 — substitution example
deck.equation("07_substitution_example",
              "Example  ·  y = 2x + 1   and   x + y = 10", [
    ("x + (2x + 1) = 10", MUTED,  "substitute y into the second equation"),
    ("3x + 1 = 10",       MUTED,  "combine like terms"),
    ("x = 3",             MUTED,  "solve for x"),
    ("y = 2(3) + 1 = 7",  MUTED,  "plug x back in"),
    ("(3, 7)",            MAROON, "solution"),
])


# 08 — elimination intro
deck.definition("08_elimination_intro", "Method 3  ·  Elimination.",
                "Add or subtract the equations to cancel a variable.",
                "Multiply an equation first if coefficients don't match.")


# 09 — elimination example
deck.equation("09_elimination_example",
              "Example  ·  2x + 3y = 12   and   4x − 3y = 6", [
    ("2x + 3y = 12",        INK,    ""),
    ("4x − 3y =  6",        INK,    "y coefficients already cancel"),
    ("6x = 18    →   x = 3", MUTED, "add the two equations"),
    ("2(3) + 3y = 12  →  y = 2", MUTED, "plug back into the first"),
    ("(3, 2)",              MAROON, "solution"),
])


# 10 — pause and try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Solve this system:",
           "x + y = 10    and    2x − y = 2",
           hint="Try elimination — add the equations to eliminate y.")
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — classification  (custom: three side-by-side outcomes)
def classification(img, d):
    d.text((110, 90), "Three possible outcomes.", fill=MAROON,
           font=font("serif_bold", 64))

    # Three columns
    col_w = 540
    gap = 50
    total = 3 * col_w + 2 * gap
    start = (W - total) // 2
    plane_h = 360
    plane_top = 280
    plane_bottom = plane_top + plane_h
    unit_small = 26
    titles = ["ONE solution", "NO solutions", "INFINITE solutions"]
    captions = [
        "Lines cross at one point.",
        "Parallel — same slope,\ndifferent intercept.",
        "Same line — every point\nis a solution.",
    ]

    for i in range(3):
        col_x = start + i * (col_w + gap)
        # Frame
        d.rounded_rectangle([col_x, 230, col_x + col_w, 870],
                            radius=20, outline=MAROON, width=4,
                            fill=deck.card_bg)
        # Title
        d.text((col_x + 30, 260), titles[i], fill=MAROON,
               font=font("serif_bold", 36))

        # Plane center for this column
        cx_p = col_x + col_w // 2
        cy_p = plane_top + plane_h // 2 + 30
        # Axes
        d.line([(col_x + 40, cy_p), (col_x + col_w - 40, cy_p)],
               fill=INK, width=2)
        d.line([(cx_p, plane_top + 30), (cx_p, plane_bottom + 30)],
               fill=INK, width=2)

        if i == 0:
            # Two crossing lines
            d.line([(col_x + 60, cy_p + 110),
                    (col_x + col_w - 60, cy_p - 110)],
                   fill=MAROON, width=5)
            d.line([(col_x + 60, cy_p - 110),
                    (col_x + col_w - 60, cy_p + 110)],
                   fill=deck.accent, width=5)
            # Intersection dot
            d.ellipse([cx_p - 10, cy_p - 10, cx_p + 10, cy_p + 10],
                      fill=MAROON_DARK)
        elif i == 1:
            # Two parallel lines
            d.line([(col_x + 60, cy_p + 50),
                    (col_x + col_w - 60, cy_p - 130)],
                   fill=MAROON, width=5)
            d.line([(col_x + 60, cy_p + 150),
                    (col_x + col_w - 60, cy_p - 30)],
                   fill=deck.accent, width=5)
        else:
            # Same line (drawn slightly offset for visibility)
            d.line([(col_x + 60, cy_p + 110),
                    (col_x + col_w - 60, cy_p - 110)],
                   fill=MAROON, width=7)
            d.line([(col_x + 62, cy_p + 108),
                    (col_x + col_w - 58, cy_p - 112)],
                   fill=deck.accent, width=3)

        # Caption
        cap_y = 720
        for line in captions[i].split("\n"):
            d.text((col_x + 30, cap_y), line, fill=MUTED,
                   font=font("sans", 26))
            cap_y += 36

    d.text((110, 920),
           "Parallel = same slope, different intercept  →  no solution.   "
           "Same line  →  infinite.",
           fill=deck.accent, font=font("sans_bold", 30))
deck.custom("12_classification", classification)


# 13 — word problem setup  (custom: movie theater becomes a system)
def word_setup(img, d):
    d.text((110, 90), "Set up the movie theater problem.",
           fill=MAROON, font=font("serif_bold", 60))

    # Step 1: define variables
    d.text((110, 220), "Step 1  ·  Assign variables.",
           fill=MAROON, font=font("serif_bold", 40))
    d.text((140, 285), "a  =  number of adult tickets",
           fill=INK, font=font("mono", 36))
    d.text((140, 335), "c  =  number of child tickets",
           fill=INK, font=font("mono", 36))

    # Step 2: write the two equations
    d.text((110, 430), "Step 2  ·  Two equations from two facts.",
           fill=MAROON, font=font("serif_bold", 40))

    # Equation 1 box
    d.rounded_rectangle([140, 510, W - 140, 620], radius=18,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((175, 535), "Total tickets:", fill=MUTED,
           font=font("sans_bold", 28))
    centered(d, "a + c = 14", font("mono", 56), 545, INK)

    # Equation 2 box
    d.rounded_rectangle([140, 660, W - 140, 770], radius=18,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((175, 685), "Total dollars:", fill=MUTED,
           font=font("sans_bold", 28))
    centered(d, "12a + 7c = 128", font("mono", 56), 695, INK)

    # Caption
    d.text((110, 820),
           "Two unknowns.  Two equations.   That's a system  —  ready to solve.",
           fill=deck.accent, font=font("sans_bold", 32))
deck.custom("13_word_problem_setup", word_setup)


# 14 — word problem solve
deck.equation("14_word_problem_solve",
              "Solve by substitution  ·  a + c = 14,  12a + 7c = 128", [
    ("a = 14 − c",                MUTED,  "solve eq. 1 for a"),
    ("12(14 − c) + 7c = 128",     MUTED,  "substitute into eq. 2"),
    ("168 − 5c = 128",            MUTED,  "distribute and combine"),
    ("c = 8",                     MUTED,  "solve for c"),
    ("a = 14 − 8 = 6",            MUTED,  "plug back in"),
    ("6 adults,  8 children",     MAROON, "answer"),
])


# 15 — when to use which method  (custom)
def when_each(img, d):
    d.text((110, 90), "Which method should you pick?",
           fill=MAROON, font=font("serif_bold", 64))
    rows = [
        ("Substitution",
         "When one variable is already isolated  (y = … or x = …)."),
        ("Elimination",
         "When coefficients line up — or are easy to match by multiplying."),
        ("Graphing",
         "Mostly for visual intuition.  Slow and imprecise for ugly numbers."),
    ]
    y = 260
    for name, when in rows:
        d.rounded_rectangle([110, y, W - 110, y + 160], radius=18,
                            outline=MAROON, width=4, fill=deck.card_bg)
        d.text((150, y + 30), name, fill=MAROON,
               font=font("serif_bold", 48))
        d.text((150, y + 95), when, fill=INK, font=font("sans", 32))
        y += 200
    d.text((110, 900),
           "Substitution and elimination are your everyday tools.",
           fill=deck.accent, font=font("sans_bold", 32))
deck.custom("15_when_each", when_each)


# 16 — recap
deck.recap("16_recap", "Recap.", [
    "System = 2+ equations with the same variables.",
    "Three methods:  graphing, substitution, elimination.",
    "Three outcomes:  one solution, none (parallel), infinite (same line).",
    "Word problems  →  assign variables  →  two equations  →  solve.",
], assignment=[
    "Solve 4 systems by the method of your choice.",
    "Plus 1 word problem  —  show the variable assignment and both equations.",
])


# 17 — path
deck.path("17_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax  Ch 4",     "Systems of Linear Equations"),
    ("2.", "Khan Academy practice",   "Systems of equations — full set"),
    ("3.", "Assignment in dashboard", "4 systems + 1 word problem"),
    ("4.", "Advisor check-in",        "Book a session if word problems still trip you up"),
], next_text="Next up:  Module 12 — Exponents & Polynomials.")


print("Module 11 (Systems of Linear Equations) slides built via slide_kit.")

"""Module 6 — Linear Inequalities.

Pure-math module built on slide_kit. Highlights the FLIP-when-dividing-by-negative
rule with an accent-colored line on slide 07, plus a custom number-line graphing
slide and a wrong-vs-right comparison.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="Algebra I", module_num=6,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# ── 01 — title ──
deck.title("01_title", "Algebra I",
           "Module 6 — Linear Inequalities",
           "Sample lesson  ·  ~6 minutes")

# ── 02 — hook (custom: cookie shop scenario → set up 3x + 5 ≤ 20) ──
def hook(img, d):
    d.text((110, 90), "Cookies, brownies, and twenty bucks.",
           fill=MAROON, font=font("serif_bold", 60))
    # Scenario lines
    f_body = font("sans", 36)
    d.text((110, 220), "You walk into a cookie shop with  $20.", fill=INK, font=f_body)
    d.text((110, 280), "Cookies cost  $3  each.   One brownie costs  $5.", fill=INK, font=f_body)
    d.text((110, 340), "How many cookies can you buy?", fill=INK, font=font("sans_bold", 38))

    # Equation vs inequality card
    d.rounded_rectangle([110, 440, W - 110, 800], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    # Inequality
    centered(d, "3x + 5  ≤  20", font("mono", 110), 480, MAROON)
    d.text((150, 640), "Equation  →  ONE answer.", fill=MUTED, font=font("sans", 34))
    d.text((150, 700), "Inequality  →  a RANGE of answers.",
           fill=deck.accent, font=font("sans_bold", 36))

    # Bottom caption
    d.text((110, 900), "x  is the number of cookies you CAN buy — many values work.",
           fill=MUTED, font=font("sans", 28))
deck.custom("02_hook", hook)

# ── 03 — overview ──
deck.overview("03_overview", "Game plan.", [
    "The four inequality symbols and what they mean.",
    "Solving like an equation — with ONE twist.",
    "Graphing on a number line + real word problems.",
], footnote="The twist is the rule everyone forgets. Don't be everyone.")

# ── 04 — symbols (custom: 4 rows, symbol + meaning + endpoint included? ──
def symbols(img, d):
    d.text((110, 90), "The four inequality symbols.",
           fill=MAROON, font=font("serif_bold", 60))
    rows = [
        ("<",  "less than",                 "endpoint NOT included"),
        ("≤",  "less than or equal to",     "endpoint IS included"),
        (">",  "greater than",              "endpoint NOT included"),
        ("≥",  "greater than or equal to",  "endpoint IS included"),
    ]
    y = 230
    for sym, name, note in rows:
        d.rounded_rectangle([110, y, W - 110, y + 140], radius=18,
                            outline=MAROON, width=4, fill=deck.card_bg)
        # Symbol badge
        d.rounded_rectangle([130, y + 20, 280, y + 120], radius=12, fill=MAROON)
        sym_w = d.textlength(sym, font=font("mono", 80))
        d.text((130 + 75 - sym_w / 2, y + 20), sym,
               fill=deck.accent, font=font("mono", 80))
        # Name
        d.text((320, y + 30), name, fill=INK, font=font("serif_bold", 40))
        # Note
        note_color = deck.accent if "IS included" in note else MUTED
        d.text((320, y + 90), note, fill=note_color, font=font("sans", 30))
        y += 160
    d.text((110, 920), "The line under the symbol means \"or equal to\" — boundary counts.",
           fill=MUTED, font=font("sans", 28))
deck.custom("04_symbols", symbols)

# ── 05 — one-step ──
deck.equation("05_one_step", "Example 1   ·   Solve  x + 5 < 12", [
    ("x + 5 < 12",          INK,    None),
    ("x + 5 − 5 < 12 − 5",  MUTED,  "subtract 5 from both sides"),
    ("x < 7",               MAROON, "solution — any number less than 7"),
])

# ── 06 — two-step ──
deck.equation("06_two_step", "Example 2   ·   Solve  3x + 2 ≥ 14", [
    ("3x + 2 ≥ 14",  INK,    None),
    ("3x ≥ 12",      MUTED,  "subtract 2 from both sides"),
    ("x ≥ 4",        MAROON, "divide both sides by 3"),
])

# ── 07 — flip rule (THE key rule, use accent for flipped line) ──
deck.equation("07_flip_rule", "THE rule   ·   Solve  −2x > 6", [
    ("−2x > 6",   INK,         "divide both sides by −2 …"),
    ("x < −3",    deck.accent, "FLIPPED — we divided by a negative"),
    ("check:  −2(−10) = 20  >  6   ✓",  MAROON, "negative numbers work — confirms it"),
])

# ── 08 — pause and try ──
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Solve this inequality:",  "−3x + 5 ≤ 17",
           hint="Hint:  subtract 5 first,  then divide by −3  and  FLIP.")
# ── 09 — duplicate of 08 for the answer-reveal narration ──
deck.duplicate("08_pause1", "09_pause1_silence")

# ── 10 — graphing on a number line (custom) ──
def graphing(img, d):
    d.text((110, 90), "Graph it on a number line.",
           fill=MAROON, font=font("serif_bold", 60))

    # Helper: draw a number line at vertical y_axis with tick marks from x0..x9 (0..9 indices)
    def draw_line(y_axis: int, label_eq: str, boundary_idx: int,
                  filled: bool, direction: str):
        # geometry: number line spans x=200..1720 with 11 ticks (indices 0..10)
        x_start, x_end = 200, 1720
        n = 10
        step = (x_end - x_start) / n

        # Equation label above
        d.text((110, y_axis - 110), label_eq,
               fill=INK, font=font("mono", 56))

        # Main axis
        d.line([(x_start, y_axis), (x_end, y_axis)], fill=INK, width=4)
        # Ticks + numbers (we label −5..+5 so index i corresponds to value i−5)
        f_num = font("sans", 26)
        for i in range(n + 1):
            tx = int(x_start + i * step)
            d.line([(tx, y_axis - 12), (tx, y_axis + 12)], fill=INK, width=3)
            val = str(i - 5)
            tw = d.textlength(val, font=f_num)
            d.text((tx - tw / 2, y_axis + 22), val, fill=MUTED, font=f_num)

        # Boundary dot
        bx = int(x_start + boundary_idx * step)
        r = 22
        if filled:
            d.ellipse([bx - r, y_axis - r, bx + r, y_axis + r], fill=deck.accent,
                      outline=MAROON, width=4)
        else:
            d.ellipse([bx - r, y_axis - r, bx + r, y_axis + r],
                      fill=deck.bg, outline=MAROON, width=5)

        # Arrow
        arrow_len = 280
        if direction == "left":
            ax_start, ax_end = bx - 30, bx - arrow_len
        else:
            ax_start, ax_end = bx + 30, bx + arrow_len
        d.line([(ax_start, y_axis), (ax_end, y_axis)], fill=MAROON, width=8)
        # Arrowhead
        head = 22
        if direction == "left":
            d.polygon([(ax_end, y_axis),
                       (ax_end + head, y_axis - head),
                       (ax_end + head, y_axis + head)], fill=MAROON)
        else:
            d.polygon([(ax_end, y_axis),
                       (ax_end - head, y_axis - head),
                       (ax_end - head, y_axis + head)], fill=MAROON)

    # First number line:  x < 7  →  open circle at "7" (we re-label tick at idx 9 as 7 for clarity)
    # Simpler approach: relabel so −5..+5 becomes 0..10. We want 7 to be in range, so use 0..10.
    # Re-draw to use 0..10 labelling on top line and lower line independently.

    def draw_line_labeled(y_axis: int, label_eq: str,
                          left_val: int, right_val: int,
                          boundary_val: int, filled: bool, direction: str):
        x_start, x_end = 220, 1700
        n = right_val - left_val
        step = (x_end - x_start) / n
        d.text((110, y_axis - 110), label_eq,
               fill=INK, font=font("mono", 56))
        d.line([(x_start, y_axis), (x_end, y_axis)], fill=INK, width=4)
        f_num = font("sans", 26)
        for i in range(n + 1):
            tx = int(x_start + i * step)
            d.line([(tx, y_axis - 12), (tx, y_axis + 12)], fill=INK, width=3)
            val = str(left_val + i)
            tw = d.textlength(val, font=f_num)
            d.text((tx - tw / 2, y_axis + 22), val, fill=MUTED, font=f_num)
        bx = int(x_start + (boundary_val - left_val) * step)
        r = 22
        if filled:
            d.ellipse([bx - r, y_axis - r, bx + r, y_axis + r], fill=deck.accent,
                      outline=MAROON, width=4)
        else:
            d.ellipse([bx - r, y_axis - r, bx + r, y_axis + r],
                      fill=deck.bg, outline=MAROON, width=5)
        arrow_len = 300
        if direction == "left":
            ax_start, ax_end = bx - 30, bx - arrow_len
        else:
            ax_start, ax_end = bx + 30, bx + arrow_len
        d.line([(ax_start, y_axis), (ax_end, y_axis)], fill=MAROON, width=8)
        head = 22
        if direction == "left":
            d.polygon([(ax_end, y_axis),
                       (ax_end + head, y_axis - head),
                       (ax_end + head, y_axis + head)], fill=MAROON)
        else:
            d.polygon([(ax_end, y_axis),
                       (ax_end - head, y_axis - head),
                       (ax_end - head, y_axis + head)], fill=MAROON)

    # Line 1:  x < 7   (open circle at 7, arrow left), labels 0..10
    draw_line_labeled(y_axis=410,
                      label_eq="x < 7   (strict)",
                      left_val=0, right_val=10,
                      boundary_val=7, filled=False, direction="left")

    # Line 2:  x ≥ 4   (filled circle at 4, arrow right), labels 0..10
    draw_line_labeled(y_axis=730,
                      label_eq="x ≥ 4   (inclusive)",
                      left_val=0, right_val=10,
                      boundary_val=4, filled=True, direction="right")

    # Caption
    d.text((110, 930),
           "Strict  ( < , > )  =  open circle.    Inclusive  ( ≤ , ≥ )  =  filled circle.",
           fill=deck.accent, font=font("sans_bold", 32))
deck.custom("10_graphing", graphing)

# ── 11 — real-world cookie shop solved ──
deck.equation("11_real_world", "Cookie shop   ·   3x + 5 ≤ 20", [
    ("3x + 5 ≤ 20",  INK,    "x  =  number of cookies"),
    ("3x ≤ 15",      MUTED,  "subtract 5 from both sides"),
    ("x ≤ 5",        MAROON, "you can buy AT MOST 5 cookies"),
])

# ── 12 — wrong-vs-right compare (the FLIP trap) ──
deck.compare("12_compare", "The #1 mistake on this module.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "−2x  >  6",
            "divide both sides by −2",
            "x  >  −3        ← forgot to flip",
        ],
        "footnote": "Test:  −2(0) = 0,  not  > 6.   0  is NOT a solution.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "−2x  >  6",
            "divide both sides by −2,  FLIP",
            "x  <  −3        ← flipped correctly",
        ],
        "footnote": "Test:  −2(−10) = 20,  and  20 > 6.   ✓",
    })

# ── 13 — recap ──
deck.recap("13_recap", "Recap.", [
    "Inequality symbols describe a RANGE, not a single answer.",
    "Solve inequalities the same way you solve equations.",
    "FLIP the sign when you multiply or divide by a NEGATIVE.",
    "Graph:  open circle for strict, filled for inclusive, + arrow.",
],
assignment=[
    "Solve 5 linear inequalities — at least ONE must have a",
    "negative coefficient (to practice the flip rule).",
    "Graph each solution on a number line.",
])

# ── 14 — path ──
deck.path("14_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read OpenStax Ch 2.6",     "Solve Linear Inequalities"),
    ("2.", "Khan Academy practice",    "15 problems · linear inequalities (incl. negative coefficients)"),
    ("3.", "Assignment in dashboard",  "5 inequalities · one with a negative coefficient"),
    ("4.", "Advisor check-in",         "Book a session if the flip rule still feels fuzzy"),
], next_text="Next up:  Module 7 — Introduction to Functions.")

print("Module 6 (Linear Inequalities) slides built via slide_kit.")

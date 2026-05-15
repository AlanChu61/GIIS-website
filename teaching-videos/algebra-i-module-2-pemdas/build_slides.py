"""Module 2 — Order of Operations (PEMDAS).

A pure-math module written end-to-end on slide_kit.  No bespoke PIL code.
This is what most future Algebra modules should look like.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

deck = Deck(course="Algebra I", module_num=2,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "Algebra I",
           "Module 2 — Order of Operations",
           "Sample lesson  ·  ~5 minutes")

# 02 — hook  (custom: viral 8 ÷ 2(2+2) showdown)
def hook(img, d):
    d.text((110, 90), "Why the internet fights about math.", fill=MAROON, font=font("serif_bold", 64))
    # Big controversial expression
    f_eq = font("mono", 200)
    eq = "8 ÷ 2(2 + 2)"
    centered(d, eq, f_eq, 250, INK)
    # Two answer columns
    box_w, box_h, gap = 700, 280, 100
    left_x = (W - 2*box_w - gap) // 2
    right_x = left_x + box_w + gap
    # Left: answer 1
    d.rounded_rectangle([left_x, 580, left_x+box_w, 580+box_h], radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((left_x+40, 610), "Camp 1 says:", fill=MUTED, font=font("sans_bold", 32))
    centered_in_box = (left_x + box_w/2 - d.textlength("1", font=font("mono", 140))/2)
    d.text((centered_in_box, 680), "1", fill=MAROON, font=font("mono", 140))
    # Right: answer 2
    d.rounded_rectangle([right_x, 580, right_x+box_w, 580+box_h], radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((right_x+40, 610), "Camp 2 says:", fill=MUTED, font=font("sans_bold", 32))
    centered_r = (right_x + box_w/2 - d.textlength("16", font=font("mono", 140))/2)
    d.text((centered_r, 680), "16", fill=MAROON, font=font("mono", 140))
    # Caption below
    d.text((110, 920), "Both groups know arithmetic.  They're missing  ORDER OF OPERATIONS.",
           fill=deck.accent, font=font("sans_bold", 32))
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "PEMDAS — what each letter means.",
    "Why we even need the rule.",
    "Four worked examples + a pause-and-try.",
], footnote="By the end, viral math problems will be obvious to you.")

# 04 — PEMDAS card  (custom: 4 stacked priority levels)
def pemdas(img, d):
    d.text((110, 90), "PEMDAS — four priority levels.", fill=MAROON, font=font("serif_bold", 60))
    levels = [
        ("P",   "Parentheses",                   "do these first"),
        ("E",   "Exponents",                     "do next"),
        ("M D", "Multiplication & Division",     "left to right"),
        ("A S", "Addition & Subtraction",        "left to right"),
    ]
    y = 250
    for letter, name, sub in levels:
        d.rounded_rectangle([110, y, W-110, y+140], radius=18, outline=MAROON, width=4, fill=deck.card_bg)
        # Letter badge on left
        d.rounded_rectangle([130, y+20, 280, y+120], radius=12, fill=MAROON)
        centered_letter_x = 130 + 75 - d.textlength(letter, font=font("mono", 60))/2
        d.text((centered_letter_x, y+35), letter, fill=deck.accent, font=font("mono", 60))
        # Name
        d.text((310, y+30), name, fill=INK, font=font("serif_bold", 44))
        d.text((310, y+88), sub, fill=MUTED, font=font("sans", 30))
        y += 160
deck.custom("04_pemdas", pemdas)

# 05 — why we need it
deck.equation("05_why", "Why we need the rule.", [
    ("6 + 4 × 3", INK, "this expression — what's the answer?"),
    ("(6 + 4) × 3 = 30", MUTED, "if you go left to right…"),
    ("6 + (4 × 3) = 18", MAROON, "if you follow PEMDAS"),
])

# 06-09 — four worked examples
deck.equation("06_example1", "Example 1   ·   6 + 4 × 3", [
    ("4 × 3 = 12", MUTED,  "multiplication first"),
    ("6 + 12 = 18", MAROON, "then addition"),
])
deck.equation("07_example2", "Example 2   ·   12 ÷ 2 + 4", [
    ("12 ÷ 2 = 6", MUTED,  "division first"),
    ("6 + 4 = 10", MAROON, "then addition"),
])
deck.equation("08_example3", "Example 3   ·   2² + 5", [
    ("2² = 4", MUTED,  "exponent first"),
    ("4 + 5 = 9", MAROON, "then addition"),
])
deck.equation("09_example4", "Example 4   ·   5(3 + 2) − 4", [
    ("3 + 2 = 5", MUTED,  "parentheses first"),
    ("5 × 5 = 25", MUTED, "then multiplication"),
    ("25 − 4 = 21", MAROON, "finally subtraction"),
])

# 10-11 — pause and try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Solve using PEMDAS:", "8 + 3 × 2²",
           hint="Order:  exponents  →  multiplication  →  addition.")
deck.duplicate("10_pause1", "11_pause1_silence")

# 12 — warning  (custom: two-column same-priority left-to-right)
def warning(img, d):
    d.text((110, 90), "Two traps to avoid.", fill=MAROON, font=font("serif_bold", 76))
    # Trap 1: M and D same priority
    d.rounded_rectangle([110, 240, W-110, 530], radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((150, 270), "Trap 1 — M and D share priority.",
           fill=MAROON, font=font("serif_bold", 40))
    centered(d, "8 ÷ 4 × 2", font("mono", 64), 350, INK)
    centered(d, "= 2 × 2  =  4", font("mono", 56), 430, deck.accent)
    d.text((150, 490), "(left to right — NOT 8÷8)",
           fill=MUTED, font=font("sans", 28))
    # Trap 2: A and S same priority
    d.rounded_rectangle([110, 580, W-110, 870], radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((150, 610), "Trap 2 — A and S share priority.",
           fill=MAROON, font=font("serif_bold", 40))
    centered(d, "10 − 3 + 2", font("mono", 64), 690, INK)
    centered(d, "= 7 + 2  =  9", font("mono", 56), 770, deck.accent)
    d.text((150, 830), "(left to right — NOT 10−5)",
           fill=MUTED, font=font("sans", 28))
deck.custom("12_warning", warning)

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "PEMDAS = Parentheses · Exponents · MD · AS.",
    "Four priority levels (NOT six — MD share, AS share).",
    "Top-down between levels.  Left-to-right inside a level.",
    "The rule never breaks.  No exceptions in this course.",
])

# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Ch 1.1",    "Order of Operations section"),
    ("2.", "Khan Academy practice",   "Order of Operations Practice"),
    ("3.", "Assignment in dashboard", "Write 5 multi-step expressions yourself · solve step by step"),
    ("4.", "Advisor check-in",        "Optional — mostly straightforward, but ask if M/D ordering trips you up"),
], next_text="Next up:  Module 3 — Properties of Real Numbers.")

print("Module 2 (PEMDAS) slides built via slide_kit.")

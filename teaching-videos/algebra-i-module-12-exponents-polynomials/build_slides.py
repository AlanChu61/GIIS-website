"""Module 12 — Exponents and Polynomials."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="Algebra I", module_num=12,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "Algebra I",
           "Module 12 — Exponents and Polynomials",
           "Sample lesson  ·  ~7 minutes")

# 02 — hook  (custom: paper-fold shock)
def hook(img, d):
    d.text((110, 90), "Fold a paper in half 50 times.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 175), "How thick is the stack?", fill=MUTED, font=font("sans", 36))
    # Big shock equation
    f_eq = font("mono", 180)
    centered(d, "2⁵⁰", f_eq, 270, INK)
    # Three answer rows showing escalation
    rows = [
        ("after 10 folds",   "≈ 1,000 sheets",        "(about an inch)"),
        ("after 30 folds",   "≈ 1 billion sheets",    "(higher than Everest)"),
        ("after 50 folds",   "> 1 quadrillion sheets","(thicker than Earth → Sun)"),
    ]
    y = 600
    for label, count, note in rows:
        d.rounded_rectangle([110, y, W-110, y+90], radius=14, outline=MAROON, width=3, fill=deck.card_bg)
        d.text((140, y+24), label, fill=MUTED, font=font("sans_bold", 30))
        d.text((620, y+22), count, fill=INK, font=font("serif_bold", 38))
        d.text((1260, y+28), note, fill=deck.accent, font=font("sans", 28))
        y += 110
    d.text((110, 940), "Exponents don't grow.  They EXPLODE.",
           fill=deck.accent, font=font("sans_bold", 36))
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Five exponent rules — product, quotient, power, zero, negative.",
    "Polynomial vocabulary — degree, terms, names.",
    "Polynomial operations — add, subtract, multiply.",
], footnote="By the end, you'll simplify any expression in this family.")

# 04 — exponent basics
deck.definition("04_exp_basics", "Exponent basics.",
                "xⁿ  =  multiply x by itself n times",
                sub="x³ = x · x · x       base = x       exponent = 3")

# 05 — product rule
deck.equation("05_product_rule", "Rule 1 — Product rule (same base, multiply)", [
    ("x² · x³  =  x · x · x · x · x  =  x⁵", INK, "write it out — five x's"),
    ("xᵃ · xᵇ  =  xᵃ⁺ᵇ", MAROON, "rule: ADD the exponents"),
    ("2³ · 2⁴  =  2⁷", MUTED, "example"),
])

# 06 — quotient rule
deck.equation("06_quotient_rule", "Rule 2 — Quotient rule (same base, divide)", [
    ("x⁵ / x²  =  x³", INK, "5 on top, 2 on bottom, 3 left over"),
    ("xᵃ / xᵇ  =  xᵃ⁻ᵇ", MAROON, "rule: SUBTRACT (top − bottom)"),
    ("7⁸ / 7²  =  7⁶", MUTED, "example"),
])

# 07 — power of a power
deck.equation("07_power_of_power", "Rule 3 — Power of a power", [
    ("(x²)³  =  x² · x² · x²  =  x⁶", INK, "three copies, each contributes 2"),
    ("(xᵃ)ᵇ  =  xᵃᵇ", MAROON, "rule: MULTIPLY the exponents"),
    ("(5³)²  =  5⁶", MUTED, "example"),
])

# 08 — zero and negative exponents
deck.equation("08_zero_negative", "Rules 4 & 5 — Zero and negative exponents", [
    ("x⁰  =  1", INK, "any nonzero base to the 0 = 1"),
    ("x⁻ⁿ  =  1 / xⁿ", MAROON, "negative exponent flips to denominator"),
    ("5⁰ = 1     2⁻³ = 1/8", MUTED, "examples"),
])

# 09 — pause and try
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Simplify using the exponent rules:",
           "x⁵ · x⁻² / x³",
           hint="Apply product rule on top first, then quotient rule.")
deck.duplicate("09_pause1", "10_pause1_silence")

# 11 — polynomial vocabulary (custom: 4 vocab cards)
def poly_vocab(img, d):
    d.text((110, 90), "Polynomial vocabulary.", fill=MAROON, font=font("serif_bold", 70))
    # Example polynomial at top
    f_eq = font("mono", 76)
    centered(d, "4x³ + 2x² − 7x + 5", f_eq, 220, INK)
    # Four small labeled cards
    items = [
        ("Polynomial",  "Sum of terms (coef × variable^whole-exponent)."),
        ("Degree",      "Highest exponent in the expression.  Above: 3."),
        ("Leading coef","Number in front of the highest-degree term.  Above: 4."),
        ("Names",       "1 term = monomial   ·   2 = binomial   ·   3 = trinomial"),
    ]
    y = 380
    for label, body in items:
        d.rounded_rectangle([110, y, W-110, y+120], radius=16, outline=MAROON, width=4, fill=deck.card_bg)
        d.text((140, y+22), label, fill=MAROON, font=font("serif_bold", 38))
        d.text((140, y+72), body, fill=INK, font=font("sans", 30))
        y += 140
deck.custom("11_polynomial_vocab", poly_vocab)

# 12 — adding and subtracting polynomials
deck.equation("12_add_sub_poly", "Add / subtract — combine like terms.", [
    ("(3x² + 2x − 1) + (x² − 4x + 5)", INK, "group by exponent"),
    ("(3x² + x²) + (2x − 4x) + (−1 + 5)", MUTED, "like terms together"),
    ("4x² − 2x + 4", MAROON, "answer  ·  for −, distribute the minus first"),
])

# 13 — multiplying mono × polynomial
deck.equation("13_mult_mono_poly", "Multiply  monomial × polynomial  (distribute).", [
    ("3x · (2x² + 5x − 4)", INK, "hit every term inside with 3x"),
    ("6x³ + 15x² − 12x", MAROON, "answer"),
])

# 14 — compare (wrong vs right)
deck.compare("14_compare", "The biggest trap.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "x² + x³  =  x⁵",
            "",
            "Adding the exponents",
            "when the terms are",
            "ADDED, not multiplied.",
        ],
        "footnote": "Only add exponents when MULTIPLYING same-base terms.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "x² + x³  stays as",
            "x² + x³",
            "",
            "Different exponents",
            "→ NOT like terms.",
        ],
        "footnote": "Like terms need identical variable AND identical exponent.",
    })

# 15 — recap
deck.recap("15_recap", "Recap.", [
    "5 exponent rules:  product +,  quotient −,  power ×,  zero = 1,  negative flips.",
    "Polynomial vocab:  degree, leading coefficient, monomial / binomial / trinomial.",
    "Add & subtract  →  combine like terms (same variable AND same exponent).",
    "Multiply mono × poly  →  distribute across every term.",
],
assignment=[
    "10 problems mixing all 5 exponent rules.",
    "4 polynomial operations — add, subtract, multiply.",
    "Show every step.  No shortcuts — show the work.",
])

# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read OpenStax Ch 6.2 & 6.3", "Use Properties of Exponents  +  Multiply Polynomials"),
    ("2.", "Khan Academy practice",    "Exponent properties  +  Polynomial operations"),
    ("3.", "Assignment in dashboard",  "10 exponent + 4 polynomial problems"),
    ("4.", "Advisor check-in",         "Book a session if negative exponents still feel weird"),
], next_text="Next up:  Module 13 — Factoring Polynomials.")

print("Module 12 (Exponents and Polynomials) slides built via slide_kit.")

"""Module 3 — Properties of Real Numbers.  Pure slide_kit (no custom helpers needed)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))
from slide_kit import Deck, INK, MAROON, MUTED

deck = Deck(course="Algebra I", module_num=3,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

deck.title("01_title", "Algebra I", "Module 3 — Properties of Real Numbers",
           "Sample lesson  ·  ~5 minutes")

# 02 — hook (commutative example you've used your whole life)
deck.equation("02_hook", "Order doesn't matter (for adding).", [
    ("8 + 5  =  13", INK,    None),
    ("5 + 8  =  13", MAROON, "same answer — you knew that"),
])

deck.overview("03_overview", "Five named properties.", [
    "Commutative — order doesn't matter.",
    "Associative — grouping doesn't matter.",
    "Distributive — multiplication spreads.",
    "Identity — 0 for +, 1 for ×.",
    "Inverse — every number has an undoer.",
], footnote="You've used all five since elementary school.  Today we name them.")

# 04-08 — five properties as equation slides
deck.equation("04_commutative", "Commutative.   Order doesn't matter.", [
    ("a + b  =  b + a", INK,    "for addition"),
    ("a × b  =  b × a", INK,    "for multiplication"),
    ("(NOT for − or ÷)", MUTED, "5 − 3  ≠  3 − 5"),
])

deck.equation("05_associative", "Associative.   Grouping doesn't matter.", [
    ("(a + b) + c  =  a + (b + c)", INK,    "for addition"),
    ("(a × b) × c  =  a × (b × c)", INK,    "for multiplication"),
    ("Same answer — just different parens.", MUTED, None),
])

deck.equation("06_distributive", "Distributive.   The mighty one.", [
    ("a (b + c)  =  ab + ac", INK,    "multiplication spreads across +"),
    ("3 (x + 4)  =  3x + 12", MAROON, "concrete example"),
    ("This rule starts every simplification.", MUTED, None),
])

deck.equation("07_identity", "Identity.   Doing nothing.", [
    ("a + 0  =  a", INK,    "additive identity is 0"),
    ("a × 1  =  a", INK,    "multiplicative identity is 1"),
    ("Used to insert/remove without changing value.", MUTED, None),
])

deck.equation("08_inverse", "Inverse.   The undo-er.", [
    ("a + (−a)  =  0",    INK,    "additive inverse"),
    ("a × (1/a)  =  1",   INK,    "multiplicative inverse  (a ≠ 0)"),
    ("This is WHY 'subtract from both sides' works.", MAROON, None),
])

# 09-10 — pause and try
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Which property?",
           "2 + (x + 5)  =  (2 + x) + 5",
           hint="Order stayed the same.  Only the parentheses moved.")
deck.duplicate("09_pause1", "10_pause1_silence")

# 11 — why this matters in actual algebra
deck.equation("11_why_matters", "Why this matters.", [
    ("3x + 2 + 5x − 7", INK,    "raw expression"),
    ("(3x + 5x) + (2 − 7)", MUTED, "commute + associate"),
    ("8x − 5", MAROON, "simplified — three properties used"),
])

deck.recap("12_recap", "Recap.", [
    "Commutative — order swaps. Plus and times only.",
    "Associative — groups shift. Plus and times only.",
    "Distributive — multiplication spreads across addition.",
    "Identity — 0 for +, 1 for × (do nothing).",
    "Inverse — every number has an undoer.",
])

deck.path("13_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Ch 1.3–1.5", "Real Number Properties"),
    ("2.", "Khan Academy practice",    "Properties of Numbers"),
    ("3.", "Assignment in dashboard",  "Identify the property in 10 algebraic steps · simplify 5 expressions"),
    ("4.", "Advisor check-in",         "Optional — these properties feel obvious until they don't"),
], next_text="Next up:  Module 4 — Solving One-Step and Two-Step Equations.")

print("Module 3 slides built.")

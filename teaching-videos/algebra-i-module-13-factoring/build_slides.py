"""Module 13 — Factoring Polynomials.

Four techniques: GCF, trinomials, difference of squares, grouping.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="Algebra I", module_num=13,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# ── 01 title ──────────────────────────────────────────────────────────
deck.title("01_title", "Algebra I",
           "Module 13 — Factoring Polynomials",
           "Sample lesson  ·  ~10 minutes")

# ── 02 hook — number factoring → polynomial factoring ─────────────────
def hook(img, d):
    d.text((110, 90), "Factoring isn't new.", fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 200), "You already did it with numbers.",
           fill=MUTED, font=font("sans", 38))

    # Two side-by-side cards: numbers vs polynomials
    box_w = 800
    box_h = 380
    gap = 60
    left_x  = (W - 2 * box_w - gap) // 2
    right_x = left_x + box_w + gap
    top_y = 340

    # Left: numbers
    d.rounded_rectangle([left_x, top_y, left_x + box_w, top_y + box_h],
                         radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((left_x + 40, top_y + 30), "Numbers", fill=MAROON,
           font=font("serif_bold", 44))
    centered_x = left_x + box_w // 2
    f_eq = font("mono", 64)
    eq1 = "12  =  2² × 3"
    eq1_w = d.textlength(eq1, font=f_eq)
    d.text((centered_x - eq1_w / 2, top_y + 140), eq1, fill=INK, font=f_eq)
    d.text((left_x + 40, top_y + 260), "Prime factorization —",
           fill=MUTED, font=font("sans", 30))
    d.text((left_x + 40, top_y + 300), "broken into multiplied pieces.",
           fill=MUTED, font=font("sans", 30))

    # Right: polynomials
    d.rounded_rectangle([right_x, top_y, right_x + box_w, top_y + box_h],
                         radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((right_x + 40, top_y + 30), "Polynomials", fill=MAROON,
           font=font("serif_bold", 44))
    centered_xr = right_x + box_w // 2
    eq2 = "x² + 5x + 6"
    eq2_w = d.textlength(eq2, font=f_eq)
    d.text((centered_xr - eq2_w / 2, top_y + 130), eq2, fill=INK, font=f_eq)
    eq3 = "=  (x + 2)(x + 3)"
    eq3_w = d.textlength(eq3, font=f_eq)
    d.text((centered_xr - eq3_w / 2, top_y + 200), eq3, fill=MAROON, font=f_eq)
    d.text((right_x + 40, top_y + 300), "Same idea — multiplied pieces.",
           fill=MUTED, font=font("sans", 30))

    d.text((110, 850), "Factored form REVEALS solutions and structure.",
           fill=deck.accent, font=font("sans_bold", 36))
deck.custom("02_hook", hook)

# ── 03 overview ───────────────────────────────────────────────────────
deck.overview("03_overview", "Four techniques today.", [
    "GCF — always check for it first.",
    "Trinomials  x² + bx + c.",
    "Difference of squares  a² − b².",
    "Grouping — for four-term polynomials.",
], footnote="Then a strategy slide to pick the right tool every time.")

# ── 04 what is factoring ──────────────────────────────────────────────
deck.definition("04_what_is_factor", "What is factoring?",
                "Writing a polynomial as a product of simpler polynomials.",
                sub="It's the reverse of distributing.")

# ── 05 GCF1 ──────────────────────────────────────────────────────────
deck.equation("05_GCF1", "GCF  ·  Factor   3x² + 6x", [
    ("3x² + 6x", INK, "every term has  3x  in common"),
    ("3x(x + 2)", MAROON, "pull the GCF out front"),
    ("check:  3x·x = 3x² ,  3x·2 = 6x  ✓", MUTED, "distribute back to verify"),
])

# ── 06 GCF2 ──────────────────────────────────────────────────────────
deck.equation("06_GCF2", "GCF  ·  Factor   12x³ − 18x²", [
    ("12x³ − 18x²", INK, "GCF of 12 and 18 is 6 ;  both have at least x²"),
    ("GCF = 6x²", MUTED, "pull out the most you can"),
    ("6x²(2x − 3)", MAROON, "factored form"),
])

# ── 07 trinomials1 ───────────────────────────────────────────────────
deck.equation("07_trinomials1", "Trinomial  ·  Factor   x² + 5x + 6", [
    ("x² + 5x + 6", INK, "need two numbers:  multiply to 6,  add to 5"),
    ("2  and  3", MUTED, "2 · 3 = 6 ,  2 + 3 = 5  ✓"),
    ("(x + 2)(x + 3)", MAROON, "verify by FOIL"),
])

# ── 08 trinomials2 (with negatives) ──────────────────────────────────
deck.equation("08_trinomials2", "Trinomial  ·  Factor   x² + 2x − 8", [
    ("x² + 2x − 8", INK, "multiply to −8,  add to +2"),
    ("4  and  −2", MUTED, "4 · (−2) = −8 ,  4 + (−2) = 2  ✓"),
    ("(x + 4)(x − 2)", MAROON, "watch the signs"),
])

# ── 09 pause + 10 silence duplicate ──────────────────────────────────
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Factor:", "x² + 7x + 12",
           hint="Find the pair that multiplies to 12 and adds to 7.")
deck.duplicate("09_pause1", "10_pause1_silence")

# ── 11 difference of squares ─────────────────────────────────────────
def diff_sq(img, d):
    d.text((110, 90), "Difference of squares — a pattern.",
           fill=MAROON, font=font("serif_bold", 60))
    # Banner pattern
    f_eq = font("mono", 100)
    pat = "a² − b²  =  (a − b)(a + b)"
    pw = d.textlength(pat, font=f_eq)
    d.text(((W - pw) / 2, 250), pat, fill=MAROON, font=f_eq)
    d.text((110, 410), "Spot it instantly.  Then apply.", fill=MUTED,
           font=font("sans", 32))

    # Two example cards
    box_w = 800
    gap = 80
    left_x = (W - 2 * box_w - gap) // 2
    right_x = left_x + box_w + gap
    top_y = 500
    f_ex = font("mono", 60)

    d.rounded_rectangle([left_x, top_y, left_x + box_w, top_y + 280],
                         radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    eq_a = "x² − 9"
    eq_aw = d.textlength(eq_a, font=f_ex)
    d.text((left_x + (box_w - eq_aw) / 2, top_y + 50), eq_a, fill=INK, font=f_ex)
    eq_a2 = "(x − 3)(x + 3)"
    eq_a2w = d.textlength(eq_a2, font=f_ex)
    d.text((left_x + (box_w - eq_a2w) / 2, top_y + 160), eq_a2,
           fill=MAROON, font=f_ex)

    d.rounded_rectangle([right_x, top_y, right_x + box_w, top_y + 280],
                         radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    eq_b = "4x² − 25"
    eq_bw = d.textlength(eq_b, font=f_ex)
    d.text((right_x + (box_w - eq_bw) / 2, top_y + 50), eq_b, fill=INK, font=f_ex)
    eq_b2 = "(2x − 5)(2x + 5)"
    eq_b2w = d.textlength(eq_b2, font=f_ex)
    d.text((right_x + (box_w - eq_b2w) / 2, top_y + 160), eq_b2,
           fill=MAROON, font=f_ex)
deck.custom("11_diff_squares", diff_sq)

# ── 12 grouping ──────────────────────────────────────────────────────
deck.equation("12_grouping", "Grouping  ·  Factor   x³ + 2x² + 3x + 6", [
    ("x³ + 2x² + 3x + 6", INK, "four terms  →  try grouping"),
    ("(x³ + 2x²) + (3x + 6)", MUTED, "group first two , last two"),
    ("x²(x + 2) + 3(x + 2)", MUTED, "pull GCF from each group"),
    ("(x + 2)(x² + 3)", MAROON, "common factor (x + 2) out front"),
])

# ── 13 strategy flowchart ────────────────────────────────────────────
def strategy(img, d):
    d.text((110, 90), "Which technique?  Use this order.",
           fill=MAROON, font=font("serif_bold", 60))

    # Step 1 — always GCF first
    d.rounded_rectangle([110, 220, W - 110, 340], radius=20,
                         outline=MAROON, width=5, fill=deck.card_bg)
    d.text((150, 240), "Step 1.", fill=deck.accent, font=font("serif_bold", 40))
    d.text((310, 245), "ALWAYS check for a GCF first.", fill=INK,
           font=font("serif_bold", 38))
    d.text((310, 295), "Pull out the most you can before anything else.",
           fill=MUTED, font=font("sans", 28))

    # Step 2 — count terms
    d.rounded_rectangle([110, 370, W - 110, 720], radius=20,
                         outline=MAROON, width=5, fill=deck.card_bg)
    d.text((150, 390), "Step 2.", fill=deck.accent, font=font("serif_bold", 40))
    d.text((310, 395), "Count the terms.", fill=INK, font=font("serif_bold", 38))

    rows = [
        ("2 terms",  "→",  "Look for difference of squares."),
        ("3 terms",  "→",  "Trinomial — find pair (mult to c, add to b)."),
        ("4 terms",  "→",  "Try grouping."),
    ]
    yr = 470
    f_mono = font("mono", 36)
    f_sans = font("sans", 32)
    for tc, arr, what in rows:
        d.text((200, yr), tc, fill=MAROON, font=f_mono)
        d.text((430, yr), arr, fill=deck.accent, font=f_mono)
        d.text((520, yr + 2), what, fill=INK, font=f_sans)
        yr += 65

    # Step 3 — verify
    d.rounded_rectangle([110, 750, W - 110, 870], radius=20,
                         outline=MAROON, width=5, fill=deck.card_bg)
    d.text((150, 770), "Step 3.", fill=deck.accent, font=font("serif_bold", 40))
    d.text((310, 775), "Verify by distributing back.", fill=INK,
           font=font("serif_bold", 38))
    d.text((310, 825), "Matches original?  Done.", fill=MUTED,
           font=font("sans", 28))
deck.custom("13_strategy", strategy)

# ── 14 real-world rectangle area ─────────────────────────────────────
def real_world(img, d):
    d.text((110, 90), "Real-world:  rectangle area.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 180), "Area  =  x² + 5x + 6.   What are the dimensions?",
           fill=INK, font=font("sans", 36))

    # Rectangle on left
    rx, ry, rw, rh = 200, 340, 600, 420
    d.rectangle([rx, ry, rx + rw, ry + rh], outline=MAROON, width=6,
                 fill=deck.card_bg)
    centered_x = rx + rw // 2
    centered_y = ry + rh // 2
    f_area = font("mono", 60)
    a_txt = "x² + 5x + 6"
    a_w = d.textlength(a_txt, font=f_area)
    d.text((centered_x - a_w / 2, centered_y - 30), a_txt,
           fill=MAROON, font=f_area)
    # Dimension labels
    d.text((rx + rw // 2 - 80, ry - 70), "x + 3", fill=INK,
           font=font("mono", 50))
    d.text((rx - 180, ry + rh // 2 - 30), "x + 2", fill=INK,
           font=font("mono", 50))

    # Factoring shown on right
    f_step = font("mono", 50)
    d.text((950, 360), "Factor the area:", fill=MUTED, font=font("sans", 34))
    d.text((950, 430), "x² + 5x + 6", fill=INK, font=f_step)
    d.text((950, 510), "=  (x + 2)(x + 3)", fill=MAROON, font=f_step)
    d.text((950, 620), "Dimensions:", fill=MUTED, font=font("sans", 34))
    d.text((950, 680), "(x + 2)  by  (x + 3)", fill=MAROON,
           font=font("mono", 48))

    d.text((110, 860), "Factoring turned area into physical dimensions.",
           fill=deck.accent, font=font("sans_bold", 32))
deck.custom("14_real_world", real_world)

# ── 15 compare — sum of squares trap ─────────────────────────────────
deck.compare("15_compare", "Sum of squares  ≠  difference of squares.",
    left={
        "label": "✗  WRONG",
        "color": RED,
        "lines": [
            "x² + 9  =  (x + 3)(x + 3)",
            "",
            "FOIL gives  x² + 6x + 9",
            "—  not  x² + 9.",
            "Doesn't match.  Wrong.",
        ],
        "footnote": "Sum of squares does NOT factor over the reals.",
    },
    right={
        "label": "✓  RIGHT",
        "color": MAROON,
        "lines": [
            "x² + 9   stays unfactored",
            "(over the real numbers)",
            "",
            "x² − 9  =  (x − 3)(x + 3)",
            "Different sign  →  different rule.",
        ],
        "footnote": "Pattern matters.  Difference ≠ Sum.",
    },
)

# ── 16 recap ─────────────────────────────────────────────────────────
deck.recap("16_recap", "Recap.", [
    "Factoring is multiplication reversed.",
    "GCF first.  Always.",
    "Trinomial:  find pair (multiply to c , add to b).",
    "Difference of squares pattern:  a² − b² = (a − b)(a + b).",
    "Four terms  →  try grouping.",
    "Verify by distributing back.",
], assignment=[
    "12 factoring problems mixing all 4 methods",
    "(GCF · trinomials · difference of squares · grouping)",
])

# ── 17 path ──────────────────────────────────────────────────────────
deck.path("17_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax  Ch 7",     "Factoring"),
    ("2.", "Khan Academy practice",   "Factoring polynomials — full set"),
    ("3.", "Assignment in dashboard", "12 problems · all 4 methods"),
    ("4.", "Advisor check-in",        "Especially if trinomial sign-tracking trips you up"),
], next_text="Next up:  Module 14 — Quadratic Equations  (where factoring becomes a SOLVING tool!)")

print("Module 13 (Factoring) slides built via slide_kit.")

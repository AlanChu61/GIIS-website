"""AP Calculus AB · Module 8 — Antiderivatives and Integration by Substitution.

Built on slide_kit (math theme = gold + cream).

Custom slides:
- 02_hook            : d/dx[sin(x²)] → ∫2x·cos(x²)dx mirror diagram (chain rule played backward)
- 09_usub_motivation : chain-rule footprint diagram showing inside + leftover derivative
- 18_selecting       : FUN 6.14 decision flow + form→tool reference card
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H, wrap,
    INK, MAROON, MAROON_DARK, MUTED, RED, GRID,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Calculus AB", module_num=8, output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 8 — Antiderivatives & Integration by Substitution",
    "~9 minutes  ·  Unit 6b  ·  FUN 6.8 – 6.14",
)


# ─── 02 — hook (custom: chain-rule mirror diagram) ───────────────────────
def hook(img, d):
    d.text((110, 80), "Every integral today",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "is chain rule played backward.",
           fill=MAROON, font=font("serif_bold", 70))

    # LEFT card — derivative direction
    lx0, ly0 = 110, 300
    lw, lh = 800, 480
    d.rounded_rectangle([lx0, ly0, lx0 + lw, ly0 + lh],
                        radius=22, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((lx0 + 30, ly0 + 20), "Differentiate  →",
           fill=MAROON, font=font("sans_bold", 36))
    d.text((lx0 + 30, ly0 + 110), "F(x)  =  sin(x²)",
           fill=INK, font=font("mono", 50))
    d.text((lx0 + 30, ly0 + 220), "d/dx[F(x)]",
           fill=MUTED, font=font("mono", 42))
    d.text((lx0 + 30, ly0 + 300), "=  2x · cos(x²)",
           fill=MAROON, font=font("mono", 50))
    d.text((lx0 + 30, ly0 + 410), "the 2x is the chain-rule tail.",
           fill=deck.accent, font=font("sans_bold", 28))

    # Center arrows showing mirror direction
    arrow_x = lx0 + lw + 30
    arrow_w = 100
    # right arrow on top
    d.line([(arrow_x, ly0 + 100), (arrow_x + arrow_w, ly0 + 100)],
           fill=MAROON, width=6)
    d.polygon([(arrow_x + arrow_w, ly0 + 88),
               (arrow_x + arrow_w + 22, ly0 + 100),
               (arrow_x + arrow_w, ly0 + 112)], fill=MAROON)
    d.text((arrow_x + 6, ly0 + 60), "d/dx",
           fill=MAROON, font=font("sans_bold", 28))
    # left arrow on bottom
    d.line([(arrow_x, ly0 + 380), (arrow_x + arrow_w, ly0 + 380)],
           fill=MAROON_DARK, width=6)
    d.polygon([(arrow_x, ly0 + 368),
               (arrow_x - 22, ly0 + 380),
               (arrow_x, ly0 + 392)], fill=MAROON_DARK)
    d.text((arrow_x + 4, ly0 + 400), "∫ dx",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    # RIGHT card — antiderivative direction
    rx0 = arrow_x + arrow_w + 30
    rw = W - rx0 - 110
    d.rounded_rectangle([rx0, ly0, rx0 + rw, ly0 + lh],
                        radius=22, outline=MAROON_DARK, width=5,
                        fill=deck.accent_light)
    d.text((rx0 + 30, ly0 + 20), "←  Antidifferentiate",
           fill=MAROON_DARK, font=font("sans_bold", 36))
    d.text((rx0 + 30, ly0 + 110), "∫ 2x · cos(x²) dx",
           fill=INK, font=font("mono", 44))
    d.text((rx0 + 30, ly0 + 220), "spot the inside  &  its derivative",
           fill=MAROON_DARK, font=font("sans", 28))
    d.text((rx0 + 30, ly0 + 300), "=  sin(x²) + C",
           fill=MAROON, font=font("mono", 50))
    d.text((rx0 + 30, ly0 + 410), "u-sub is the inverse of chain rule.",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    # Bottom strip — caption
    d.rounded_rectangle([110, 830, W - 110, 985], radius=20, fill=deck.accent_light)
    centered(d, "Look for the chain-rule footprint:  an inside function  AND  its derivative nearby.",
             font("sans_bold", 32), 848, MAROON_DARK)
    centered(d, "Integration is detective work.",
             font("serif_bold", 38), 905, MAROON_DARK)


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Antiderivatives — basic rules and the  +C  habit.",
        "U-substitution — chain rule, played backward.",
        "Long division  &  completing the square — two algebra rescues.",
    ],
    footnote="FUN 6.14 — knowing WHICH tool to pick is half the battle.",
)


# ─── 04 — antiderivative definition ──────────────────────────────────────
deck.definition(
    "04_antiderivative_def", "Antiderivative.",
    "If  F'(x) = f(x)   then   ∫ f(x) dx  =  F(x) + C",
    "The +C captures the constant that vanished when we differentiated.",
)


# ─── 05 — basic rules (reverse power) ────────────────────────────────────
deck.equation(
    "05_basic_rules", "Reverse Power Rule  ·  FUN 6.8",
    [
        ("∫ xⁿ dx  =  xⁿ⁺¹ / (n+1)  +  C", MAROON, "for any real n ≠ −1"),
        ("∫ (1/x) dx  =  ln|x|  +  C",     INK,    "the n = −1 exception"),
        ("∫ k · f(x) dx  =  k · ∫ f(x) dx", MUTED,  "constants pull out"),
        ("∫ [f ± g] dx  =  ∫ f dx  ±  ∫ g dx", MUTED, "sums distribute"),
    ],
)


# ─── 06 — basic antiderivative table ─────────────────────────────────────
deck.equation(
    "06_basic_table", "Memorize cold.",
    [
        ("∫ sin x dx  =  − cos x + C",                 MAROON, "sine ↔ cosine flip"),
        ("∫ cos x dx  =    sin x + C",                 INK,    "no minus this direction"),
        ("∫ sec² x dx =    tan x + C    ∫ eˣ dx = eˣ + C", INK, None),
        ("∫ 1/(1+x²) dx  =  arctan x + C",             MAROON, "the arctan pattern"),
        ("∫ 1/√(1−x²) dx  =  arcsin x + C",            MAROON, "the arcsin pattern"),
    ],
)


# ─── 07 — compare: +C trap ───────────────────────────────────────────────
deck.compare(
    "07_plus_C_trap",
    "AP trap #1 — forgetting  +C.",
    left={
        "label": "✗ INCOMPLETE",
        "color": RED,
        "lines": [
            "∫ (3x² + 4x − 1) dx",
            "    =  x³ + 2x² − x",
            "Arithmetic is right.",
            "Answer is incomplete — one  C  short.",
        ],
        "footnote": "The integral asks for ALL antiderivatives, not one.",
    },
    right={
        "label": "✓ COMPLETE",
        "color": MAROON,
        "lines": [
            "∫ (3x² + 4x − 1) dx",
            "    =  x³ + 2x² − x  +  C",
            "Same arithmetic.",
            "Plus the family of constants.",
        ],
        "footnote": "Every indefinite integral ends with  +C.  No exceptions.",
    },
)


# ─── 08 — definite integrals: +C cancels ─────────────────────────────────
deck.equation(
    "08_definite_no_C", "Definite integrals — drop the +C.",
    [
        ("∫ from a to b  f(x) dx  =  F(b) − F(a)", MAROON, "the +C would cancel in subtraction"),
        ("∫₀¹ x² dx  =  [x³/3]₀¹",                 INK,    "evaluate at upper, subtract lower"),
        ("       =  1/3  −  0  =  1/3",            MAROON, "no +C needed"),
        ("Indefinite  →  +C.    Definite  →  no +C.", MUTED, "the one rule to remember"),
    ],
)


# ─── 09 — u-sub motivation (custom: chain-rule footprint diagram) ────────
def usub_motivation(img, d):
    d.text((110, 80), "Why u-substitution exists.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 160), "Spot the chain-rule footprint — and walk it backward.",
           fill=MUTED, font=font("sans", 34))

    # TOP card — derivative example showing chain rule
    tx0, ty0 = 110, 240
    tw, th = W - 220, 220
    d.rounded_rectangle([tx0, ty0, tx0 + tw, ty0 + th],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((tx0 + 30, ty0 + 20), "Forward (chain rule):",
           fill=MAROON, font=font("sans_bold", 32))
    d.text((tx0 + 30, ty0 + 80), "d/dx[ (x²+1)⁴ ]  =  4(x²+1)³ · 2x",
           fill=INK, font=font("mono", 46))
    d.text((tx0 + 30, ty0 + 150), "inside = x²+1            inside' = 2x",
           fill=deck.accent, font=font("sans_bold", 28))

    # BOTTOM card — backward direction
    bx0 = 110
    by0 = ty0 + th + 30
    bh = 240
    d.rounded_rectangle([bx0, by0, bx0 + tw, by0 + bh],
                        radius=20, outline=MAROON_DARK, width=5,
                        fill=deck.accent_light)
    d.text((bx0 + 30, by0 + 20), "Backward (u-sub):",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((bx0 + 30, by0 + 80), "∫ 8x(x²+1)³ dx",
           fill=INK, font=font("mono", 46))
    d.text((bx0 + 30, by0 + 145), "See:  inside (x²+1)  AND  derivative-of-inside (2x).",
           fill=MAROON_DARK, font=font("sans", 30))
    d.text((bx0 + 30, by0 + 190), "→ chain rule was here. Unwind it.",
           fill=MAROON, font=font("sans_bold", 28))

    # Bottom rule strip
    d.rounded_rectangle([110, 880, W - 110, 990], radius=20, fill=deck.accent_light)
    centered(d, "Whenever an inside function AND its derivative both show up — reach for u-sub.",
             font("sans_bold", 34), 905, MAROON_DARK)


deck.custom("09_usub_motivation", usub_motivation)


# ─── 10 — u-sub 5-step recipe ────────────────────────────────────────────
deck.equation(
    "10_usub_recipe", "U-Substitution Recipe  ·  FUN 6.9",
    [
        ("1.  Pick  u  =  inside function",          INK,    "the composite's inside"),
        ("2.  Compute  du  =  u'(x) · dx",           INK,    "differentiate, attach dx"),
        ("3.  Substitute every x-piece, dx included", INK,   "the integrand must end up in u only"),
        ("4.  Antidifferentiate the cleaner u-form",  INK,    None),
        ("5.  Substitute  x  back in",               MAROON, "(indefinite only — see slide 15)"),
    ],
)


# ─── 11 — u-sub worked: ∫ 2x·cos(x²) dx ──────────────────────────────────
deck.equation(
    "11_usub_worked", "Worked  ·  ∫ 2x · cos(x²) dx",
    [
        ("u  =  x²        du  =  2x dx",        MUTED,  "the 2x dx in the integrand IS du"),
        ("∫ 2x · cos(x²) dx   =   ∫ cos(u) du", INK,    "substitute"),
        ("=  sin(u) + C",                       INK,    "basic rule"),
        ("=  sin(x²) + C",                      MAROON, "substitute x back"),
    ],
)


# ─── 12 — u-sub fix-the-constant: ∫ x(x²+1)³ dx ──────────────────────────
deck.equation(
    "12_usub_fix_constant", "When  du  is off by a constant.",
    [
        ("∫ x · (x² + 1)³ dx",                   INK,    "u = x²+1  →  du = 2x dx"),
        ("x dx  =  (1/2) du",                    MUTED,  "we only have half a du"),
        ("=  (1/2) · ∫ u³ du   =   (1/2) · u⁴/4 + C", INK, "pull the 1/2 out front"),
        ("=  (x² + 1)⁴ / 8  +  C",               MAROON, "substitute back, simplify"),
    ],
)


# ─── 13 — pause & try ────────────────────────────────────────────────────
deck.pause(
    "13_pause1", "PAUSE  &  TRY",
    "Use u-substitution to find:",
    "∫ x² · √(x³ + 5) dx",
    hint="Pick  u  as the inside of the square root.  Pause. Solve. Press play when ready.",
)

# ─── 14 — pause silence (duplicate of 13) ────────────────────────────────
deck.duplicate("13_pause1", "14_pause1_silence")


# ─── 15 — definite-integral substitution (change the bounds) ─────────────
deck.equation(
    "15_definite_bounds", "Definite u-sub — change the bounds too.",
    [
        ("∫₀¹  2x · (x² + 1)³ dx",            INK,    "u = x²+1,  du = 2x dx"),
        ("x = 0  →  u = 1       x = 1  →  u = 2", MAROON, "translate the bounds"),
        ("=  ∫₁²  u³ du   =   [u⁴/4]₁²",      INK,    "no need to substitute x back"),
        ("=  16/4  −  1/4   =   15/4",        MAROON, "answer"),
    ],
)


# ─── 16 — long division (FUN 6.10) ───────────────────────────────────────
deck.equation(
    "16_long_division", "Long division  ·  FUN 6.10",
    [
        ("∫  (x² + 1) / (x − 1)  dx",                MUTED,  "top degree ≥ bottom degree"),
        ("x² + 1  =  (x − 1)(x + 1)  +  2",          INK,    "polynomial long division"),
        ("=  ∫ [ (x + 1)  +  2/(x − 1) ] dx",        INK,    "split into clean pieces"),
        ("=  x²/2  +  x  +  2 · ln|x − 1|  +  C",    MAROON, "integrate term by term"),
    ],
)


# ─── 17 — completing the square (FUN 6.10) ───────────────────────────────
deck.equation(
    "17_complete_square", "Completing the square  ·  FUN 6.10",
    [
        ("∫  1 / (x² + 2x + 5)  dx",                 MUTED,  "quadratic with no real roots"),
        ("x² + 2x + 5  =  (x + 1)²  +  4",           INK,    "complete the square"),
        ("u = (x+1)/2     dx = 2 du                ", MUTED,  "scale to match arctan form"),
        ("=  (1/2)  ·  ∫  1/(u² + 1)  du",           INK,    "the arctan pattern"),
        ("=  (1/2) · arctan( (x+1)/2 )  +  C",       MAROON, "answer"),
    ],
)


# ─── 18 — selecting techniques  ·  FUN 6.14 (custom decision flow) ───────
def selecting(img, d):
    d.text((110, 80), "Selecting techniques  ·  FUN 6.14",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160), "Look at the integrand.  Ask these four questions  IN ORDER:",
           fill=MUTED, font=font("sans", 32))

    # LEFT card — decision flow (numbered)
    lx0, ly0 = 110, 230
    lw, lh = 1090, 600
    d.rounded_rectangle([lx0, ly0, lx0 + lw, ly0 + lh],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    steps = [
        ("1.", "Match a basic rule?",
               "(power, trig, eˣ, ln, arctan, arcsin)  →  use the table"),
        ("2.", "Inside function with its derivative nearby?",
               "→  u-substitution"),
        ("3.", "Rational, top degree  ≥  bottom degree?",
               "→  long division first,  then integrate"),
        ("4.", "Quadratic denominator with no real roots?",
               "→  complete the square  →  usually arctan"),
    ]
    step_y = ly0 + 50
    for n, q, ans in steps:
        d.text((lx0 + 40, step_y), n, fill=MAROON, font=font("serif_bold", 56))
        d.text((lx0 + 120, step_y + 4), q, fill=INK, font=font("sans_bold", 32))
        d.text((lx0 + 120, step_y + 56), ans, fill=deck.accent, font=font("sans", 28))
        step_y += 135

    # RIGHT card — form → tool reference table
    rx0 = lx0 + lw + 30
    rw = W - rx0 - 110
    d.rounded_rectangle([rx0, ly0, rx0 + rw, ly0 + lh],
                        radius=20, outline=MAROON_DARK, width=5,
                        fill=deck.accent_light)
    d.text((rx0 + 25, ly0 + 20), "FORM  →  TOOL",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.line([(rx0 + 20, ly0 + 70), (rx0 + rw - 20, ly0 + 70)],
           fill=MAROON_DARK, width=2)
    pairs = [
        ("xⁿ, sin, eˣ, ln,", "basic"),
        ("arctan, arcsin",   "table"),
        ("f(g(x))·g'(x)",    "u-sub"),
        ("P(x) / Q(x),",     "long"),
        ("deg P ≥ deg Q",    "div."),
        ("1 / (quadratic)",  "complete"),
        ("no real roots",    "the sq."),
    ]
    py = ly0 + 90
    for form, tool in pairs:
        d.text((rx0 + 25, py), form, fill=INK, font=font("mono", 26))
        d.text((rx0 + rw - 25 - d.textlength(tool, font=font("sans_bold", 28)), py),
               tool, fill=MAROON, font=font("sans_bold", 28))
        py += 60

    # Bottom strip — meta-rule
    d.rounded_rectangle([110, 860, W - 110, 980], radius=20, fill=deck.accent_light)
    centered(d, "Try the questions IN ORDER. First match wins.",
             font("sans_bold", 32), 880, MAROON_DARK)
    centered(d, "Picking the right tool is half the AP score.",
             font("serif_bold", 36), 928, MAROON_DARK)


deck.custom("18_selecting", selecting)


# ─── 19 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "19_recap", "Recap.",
    [
        "Antiderivative:  F'(x) = f(x).   Indefinite gets  +C,  definite does NOT.",
        "Reverse power rule  +  basic table (sin, cos, eˣ, 1/x → ln|x|, arctan, arcsin).",
        "U-sub  =  chain rule backward.  Pick inside, compute du, substitute dx too.",
        "Definite u-sub:  change the bounds.  No need to substitute x back.",
        "Long division  for top-heavy rational.   Complete the square  for arctan.",
        "FUN 6.14:  basic rule  →  u-sub  →  long-div  →  complete-the-square.",
    ],
    assignment=[
        "GIIS Assignment M8 — 15 mixed problems:",
        "5 basic rules · 5 indefinite u-sub · 3 definite u-sub · 2 long-div / complete-sq.",
        "Due before Module 9.  Submit in the Learn Portal.",
    ],
)


# ─── 20 — path ───────────────────────────────────────────────────────────
deck.path(
    "20_path",
    items=[
        ("✓",  "Watch this lesson",         "(done!)"),
        ("1.", "OpenStax Calculus Vol 1",    "Read sections 5.5 – 5.7 (substitution + integration)"),
        ("2.", "Khan Academy practice",      "AP Calc AB · Unit 6 — antiderivatives & substitution"),
        ("3.", "Assignment in dashboard",    "GIIS Assignment M8 — 15 mixed problems"),
        ("4.", "Advisor check-in",           "Book if bound-changing on definite u-sub feels fuzzy"),
    ],
    next_text="Next up:  Module 9 — Differential Equations  (where antiderivatives earn their keep).",
)


print("AP Calc AB Module 8 slides built.")

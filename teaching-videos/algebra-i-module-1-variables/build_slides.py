"""Module 1 — Variables & Algebraic Expressions.  Built on slide_kit.

This file used to be ~250 lines of repeated PIL boilerplate. Now it's the
data + 4 small custom drawings, because slide_kit handles the 80% case
(title, overview, definition, equation, pause, recap, path) consistently.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="Algebra I", module_num=1, output_dir="slides", logo_path=LOGO)

# 01 — title  (theme: math → gold accent)
deck.title("01_title", "Algebra I",
           "Module 1 — Variables & Algebraic Expressions",
           "Sample lesson  ·  ~5 minutes")

# 02 — hook  (custom: phone passcode mockup)
def hook(img, d):
    d.text((110, 90), "Pull out your phone.", fill=MAROON, font=font("serif_bold", 80))
    # Phone mockup
    px, py = 380, 240
    d.rounded_rectangle([px, py, px+520, py+540], radius=40, outline=MAROON, width=8)
    d.rounded_rectangle([px+30, py+30, px+490, py+510], radius=20, fill=deck.card_bg)
    d.text((px+90, py+80), "Enter passcode", fill=MUTED, font=font("sans", 32))
    fx = font("mono", 88)
    for i in range(6):
        x = px + 60 + i*65
        d.rounded_rectangle([x, py+200, x+50, py+280], radius=6, outline=MAROON, width=3)
        d.text((x+12, py+205), "x", fill=MAROON, font=fx)
    d.text((px+60, py+340), "Six unknowns.", fill=INK, font=font("sans_bold", 36))
    d.text((px+60, py+390), "Only YOU know what they are.", fill=MUTED, font=font("sans", 28))
    # Right column
    d.text((1080, 280), "x = a variable", fill=MAROON, font=font("serif_bold", 64))
    d.text((1080, 380), "= a placeholder for", fill=INK, font=font("sans", 36))
    d.text((1080, 430), "  a number we don't", fill=INK, font=font("sans", 36))
    d.text((1080, 480), "  know yet.", fill=INK, font=font("sans", 36))
    d.text((1080, 600), "Algebra is the language", fill=deck.accent, font=font("sans_bold", 36))
    d.text((1080, 650), "we use to talk about",   fill=deck.accent, font=font("sans_bold", 36))
    d.text((1080, 700), "those unknowns.",        fill=deck.accent, font=font("sans_bold", 36))
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "What a variable is.",
    "What an algebraic expression is — and the vocab.",
    "How to evaluate when you DO know the value.",
], footnote="Don't sleep on this — every other module assumes you nailed it.")

# 04 — definition card
deck.definition("04_variable", "What's a variable?",
                "A letter that stands in for a number.",
                "Either an unknown — or one that can change.")

# 05 — expression  (custom: 3 example boxes + signoff strip)
def expression(img, d):
    d.text((110, 90), "Algebraic expression.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 210), "Variables + numbers + operations.  No equals sign.",
           fill=MUTED, font=font("sans", 36))
    for i, e in enumerate(["3x + 5", "x² − 7", "4y / 3"]):
        x = 200 + i*540
        d.rounded_rectangle([x, 350, x+440, 530], radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        f_eq = font("mono", 96); cen_w = d.textlength(e, font=f_eq)
        d.text((x + (440-cen_w)/2, 390), e, fill=INK, font=f_eq)
    d.text((110, 650), "Each one describes a quantity —", fill=INK, font=font("sans", 38))
    d.text((110, 700), "but doesn't say what that quantity equals.", fill=INK, font=font("sans", 38))
    d.rounded_rectangle([110, 780, W-110, 880], radius=20, fill=deck.accent)
    centered(d, "expression  ≠  equation   (no equals sign yet)",
             font("sans_bold", 40), 808, MAROON_DARK)
deck.custom("05_expression", expression)

# 06 — vocab annotation  (custom: arrows from 3x+5 to labels)
def vocab(img, d):
    d.text((110, 90), "Three words to know.", fill=MAROON, font=font("serif_bold", 76))
    eq = "3x + 5"
    f_eq = font("mono", 200); eq_w = d.textlength(eq, font=f_eq); eq_x = (W - eq_w) / 2
    d.text((eq_x, 280), eq, fill=INK, font=f_eq)
    f_lab = font("sans_bold", 32); f_def = font("sans", 28)
    # coefficient (the 3)
    d.line([(eq_x+50, 480), (eq_x-50, 580)], fill=deck.accent, width=4)
    d.text((eq_x-380, 560), "coefficient", fill=deck.accent, font=f_lab)
    d.text((eq_x-380, 600), "the number multiplying x", fill=MUTED, font=f_def)
    # term (3x)
    d.line([(eq_x+90, 540), (eq_x-30, 720)], fill=MAROON, width=4)
    d.text((eq_x-200, 720), "term", fill=MAROON, font=f_lab)
    d.text((eq_x-200, 760), "(also: 5 is a term)", fill=MUTED, font=f_def)
    # constant (the 5)
    d.line([(eq_x+eq_w-90, 480), (eq_x+eq_w+50, 580)], fill=deck.accent, width=4)
    d.text((eq_x+eq_w+50, 560), "constant", fill=deck.accent, font=f_lab)
    d.text((eq_x+eq_w+50, 600), "fixed number, no variable", fill=MUTED, font=f_def)
deck.custom("06_vocab", vocab)

# 07-08 — equation walkthroughs
deck.equation("07_evaluate1", "Evaluate  3x + 5  when  x = 2", [
    ("3(2) + 5", INK,    "substitute x with 2"),
    ("6 + 5",    MUTED,  "multiply first"),
    ("11",       MAROON, "answer"),
])
deck.equation("08_evaluate2", "Evaluate  4(y − 3)  when  y = 7", [
    ("4(7 − 3)", INK,    "substitute y with 7"),
    ("4(4)",     MUTED,  "parentheses first (PEMDAS)"),
    ("16",       MAROON, "answer"),
])

# 09 — pause-and-try (10 reuses the same image)
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Evaluate this when  a = 5:", "2a + 6",
           hint="Pause. Solve. Press play when you've got it.")
deck.duplicate("09_pause1", "10_pause1_silence")

# 11 — real-world  (custom: ticket-receipt visual)
def real_world(img, d):
    d.text((110, 90), "Where you'll see this.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 220), "Movie tickets cost $12 each.  Buy n tickets:",
           fill=INK, font=font("sans", 38))
    centered(d, "Total cost  =  12n", font("mono", 100), 340, MAROON)
    d.rounded_rectangle([110, 540, W-110, 740], radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((150, 580), "Buy 3 tickets?", fill=MAROON, font=font("sans_bold", 40))
    centered(d, "12 (3)  =  $36", font("mono", 80), 640, INK)
    d.text((110, 800), "The expression let us write the rule once — for any number of tickets.",
           fill=deck.accent, font=font("sans_bold", 36))
deck.custom("11_real_world", real_world)

# 12 — recap
deck.recap("12_recap", "Recap.", [
    "Variable — a letter standing for an unknown or changing number.",
    "Expression — variables + numbers + operations.  No equals sign.",
    "Coefficient (multiplies the variable), term, constant (no variable).",
    "Evaluate — plug in for the variable, then simplify.",
])

# 13 — path  ("how to actually master")
deck.path("13_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax  Ch 1.1",   "Use the Language of Algebra"),
    ("2.", "Khan Academy practice",   "20 problems · Writing Algebraic Expressions"),
    ("3.", "Assignment in dashboard", "10 real-life situations as expressions; evaluate each"),
    ("4.", "Advisor check-in",        "Book a session if anything feels fuzzy"),
], next_text="Next up:  Module 2 — Order of Operations (PEMDAS).")

print("Module 1 slides built (via slide_kit).")

"""Module 3 — Boolean Expressions and if Statements (AP Computer Science A).

CS theme = steel-blue accent (auto-resolved from course name).
Java code rendered via deck.equation() — mono font. Lines kept short
to fit at 80pt mono. Single .compare() slide for the == vs .equals trap.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="AP Computer Science A", module_num=3,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 3 — Boolean Expressions & if",
           "Sample lesson  ·  ~7 minutes")

# 02 — hook: subway turnstile analogy (custom)
def hook_render(img, d):
    d.text((110, 90), "Every decision in code.", fill=MAROON,
           font=font("serif_bold", 76))
    d.text((110, 200),
           "A subway turnstile, in one sentence:",
           fill=MUTED, font=font("sans", 36))

    # Card with the IF / ELSE structure
    d.rounded_rectangle([110, 290, W - 110, 720], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)

    f_kw   = font("serif_bold", 60)
    f_code = font("mono", 56)

    # IF line
    d.text((180, 340), "IF", fill=deck.accent, font=f_kw)
    d.text((360, 348), "balance  ≥  price", fill=INK, font=f_code)
    d.text((360, 425), "→  gate opens", fill=MAROON, font=font("sans", 38))

    # ELSE line
    d.text((180, 530), "ELSE", fill=deck.accent, font=f_kw)
    d.text((360, 538), "block the rider", fill=INK, font=f_code)
    d.text((360, 615), "→  no entry", fill=MAROON, font=font("sans", 38))

    d.text((110, 770),
           "That's the entire structure of computer decision-making.",
           fill=deck.accent, font=font("sans_bold", 36))

deck.custom("02_hook", hook_render)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Boolean expressions:  ==,  &&,  ||  (return true / false).",
    "Branching:  if  /  else  /  else-if.",
    "The  ==  vs  .equals()  trap for Strings.",
], footnote="By the end your code stops running in a straight line — it branches.")

# 04 — relational operators
deck.equation("04_relational", "Relational operators (return a boolean).", [
    ("a > b     a < b",         MAROON, "greater / less than"),
    ("a >= b    a <= b",        MAROON, "or-equal-to versions"),
    ("a == b    a != b",        MAROON, "equality  ·  not-equal"),
    ("age >= 18  → false",      MUTED,  "int age = 17;  boolean canVote = age >= 18;"),
])

# 05 — equality on Strings (preview the trap)
deck.equation("05_equality_strings", "Heads-up:  Strings are different.", [
    ('"hi" == "hi"',             MAROON, "may LOOK true..."),
    ('new String("hi") == "hi"', MAROON, "...but breaks here."),
    ("Use  .equals()  for Strings.", MUTED, "we'll see this again on the compare slide"),
])

# 06 — logical operators
deck.equation("06_logical_and_or", "Logical operators:  &&  ||  !", [
    ("a && b",       MAROON, "AND — both must be true"),
    ("a || b",       MAROON, "OR  — at least one true"),
    ("!a",           MAROON, "NOT — flips the boolean"),
    ("age>=13 && age<=19", MUTED, "true if the person is a teenager"),
])

# 07 — short-circuit (definition)
deck.definition("07_short_circuit",
                "Java short-circuits.",
                "if (b != 0  &&  a/b > 1)",
                sub="If the left of && is FALSE, the right is NEVER evaluated.  Reverse the order and you'd divide by zero.")

# 08 — De Morgan's laws
deck.equation("08_demorgan", "De Morgan's laws — logic gold.", [
    ("!(a && b)  ≡  !a || !b", MAROON, "flip an AND into ORs"),
    ("!(a || b)  ≡  !a && !b", MAROON, "flip an OR  into ANDs"),
    ("Negate compounds cleanly.", MUTED, "shows up every year on the exam"),
])

# 09 — pause1
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Write a boolean expression that's true",
           "when  age  is  13–19  inclusive.",
           hint="Both bounds must hold — that's an AND.")
deck.duplicate("09_pause1", "10_pause1_silence")

# 11 — if / else
deck.equation("11_if_else", "Basic if  /  else.", [
    ("if (cond) { ... }",        MAROON, "runs when cond is true"),
    ("else      { ... }",        MAROON, "runs otherwise"),
    ('if (score>=60) "Pass"',    MUTED,  'else "Fail"  —  two-way branch'),
])

# 12 — if / else-if ladder
deck.equation("12_if_else_if", "Else-if ladder  (checked top-down).", [
    ("if (s >= 90)  g = 'A';",      MAROON, None),
    ("else if (s >= 80)  g = 'B';", MAROON, None),
    ("else if (s >= 70)  g = 'C';", MAROON, None),
    ("else  g = 'F';",              MAROON, "strictest condition first"),
])

# 13 — nested if
deck.equation("13_nested_if", "Nested  if  (use sparingly).", [
    ("if (loggedIn) {",       MAROON, None),
    ("  if (isAdmin) { ... }", MAROON, "inner check"),
    ("  else        { ... }", MAROON, None),
    ("}",                      MAROON, "prefer  &&  when you can"),
])

# 14 — compare: == vs .equals for Strings
deck.compare("14_compare", "Strings:  ==  vs  .equals()",
    left={
        "label": "✗  WRONG",
        "color": RED,
        "lines": [
            'if (name == "Alex") {',
            '    ...',
            '}',
            "",
            "May return FALSE even when",
            "name LOOKS equal to \"Alex\".",
        ],
        "footnote": "==  compares REFERENCES, not contents.",
    },
    right={
        "label": "✓  RIGHT",
        "color": MAROON,
        "lines": [
            'if (name.equals("Alex")) {',
            '    ...',
            '}',
            "",
            "Compares the actual characters.",
            "Always use .equals() for Strings.",
        ],
        "footnote": "Same rule for any object — use .equals(), not ==.",
    })

# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Six relational operators  (>  <  >=  <=  ==  !=)  →  boolean.",
    "Compounds:  &&  (AND),  ||  (OR),  !  (NOT).",
    "Short-circuit:  the right side may never run.",
    "De Morgan flips compounds:  !(a && b) ≡ !a || !b.",
    "Branch with  if  /  else if  /  else.",
    "Strings use  .equals()  —  not  ==.",
], assignment=[
    "Write a Java program that reads a numeric score and prints the letter",
    "grade  (A  ≥ 90,  B  ≥ 80,  C  ≥ 70,  D  ≥ 60,  else F).",
])

# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",         "(done!)"),
    ("1.", "Runestone chapter",         "Boolean Expressions and if Statements"),
    ("2.", "Codingbat Logic-1",         "10 problems · build boolean intuition"),
    ("3.", "Assignment in dashboard",   "score  →  letter grade with if / else-if"),
    ("4.", "Advisor check-in",          "Book a session if  ==  vs  .equals  still feels fuzzy"),
], next_text="Next up:  Module 4 — Iteration.")

print("Module 3 (Boolean Expressions and if Statements) slides built via slide_kit.")

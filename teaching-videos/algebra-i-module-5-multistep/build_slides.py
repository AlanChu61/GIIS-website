"""Module 5 — Multi-Step and Literal Equations.  Pure slide_kit."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))
from slide_kit import Deck, INK, MAROON, MUTED

deck = Deck(course="Algebra I", module_num=5,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

deck.title("01_title", "Algebra I",
           "Module 5 — Multi-Step & Literal Equations",
           "Sample lesson  ·  ~7 minutes")

# 02 — hook: today's progression compared to Module 4
deck.equation("02_hook", "Module 4 → Module 5.   Same rules, more moves.", [
    ("x + 5 = 12",                 MUTED, "Module 4"),
    ("3x + 7 = 2x + 12",            INK,    "variables on both sides"),
    ("5(x − 2) = 15",               INK,    "parentheses to distribute"),
    ("x/4 + x/6 = 5",               INK,    "fractions to clear"),
    ("A = lw   →   solve for w",    MAROON, "rearrange a formula"),
])

deck.overview("03_overview", "Four new moves + one new idea.", [
    "Distribute parentheses first.",
    "Combine like terms.",
    "Get the variable on one side only.",
    "Clear fractions by multiplying by the LCD.",
    "Literal equations — rearrange formulas for a chosen variable.",
])

deck.equation("04_distribute", "Move 1.   Distribute first.", [
    ("5(x − 2) = 15",      INK,    None),
    ("5x − 10 = 15",        MUTED,  "distribute the 5"),
    ("5x = 25",             MUTED,  "add 10 to both sides"),
    ("x = 5",               MAROON, "divide by 5"),
])

deck.equation("05_combine", "Move 2.   Combine like terms.", [
    ("2x + 7 + 3x − 4 = 15", INK,    None),
    ("5x + 3 = 15",          MUTED,  "combine 2x + 3x  and  7 − 4"),
    ("5x = 12",              MUTED,  "subtract 3"),
    ("x = 2.4",              MAROON, "divide by 5"),
])

deck.equation("06_both_sides", "Move 3.   Variables on both sides.", [
    ("3x + 7 = 2x + 12",     INK,    "pick a side, move the other variable"),
    ("x + 7 = 12",            MUTED,  "subtract 2x from both sides"),
    ("x = 5",                 MAROON, "subtract 7"),
])

deck.pause("07_pause1", "PAUSE  &  TRY",
           "Solve:", "4x − 6 = 2x + 8",
           hint="Move the smaller coefficient.  Avoids negatives.")
deck.duplicate("07_pause1", "08_pause1_silence")

deck.equation("09_fractions", "Move 4.   Clear fractions first.", [
    ("Find the LCD of all denominators.", INK, None),
    ("Multiply EVERY term by the LCD.",   INK, None),
    ("Fractions vanish.  Solve as usual.", MAROON, None),
])

deck.equation("10_fractions_example", "Example.   x/2 + x/3 = 5", [
    ("LCD = 6", MUTED, "denominators are 2 and 3"),
    ("3x + 2x = 30", MUTED, "multiply every term by 6"),
    ("5x = 30", MUTED, "combine"),
    ("x = 6", MAROON, "divide by 5"),
])

deck.definition("11_literal_intro", "Literal equations.",
                "The answer isn't a number — it's a rearranged formula.",
                "Same rules.  Symbols all the way down.")

deck.equation("12_literal_example1", "Solve  A = lw  for  w.", [
    ("A = l w",      INK,    "treat A and l as numbers"),
    ("A / l = w",     MUTED,  "divide both sides by l"),
    ("w = A / l",     MAROON, "rearranged for w"),
])

deck.equation("13_literal_example2", "Solve  PV = nRT  for  T.", [
    ("P V = n R T",          INK,    "the ideal gas law"),
    ("PV / (nR) = T",         MUTED,  "divide both sides by nR"),
    ("T = PV / (nR)",         MAROON, "physics formulas are just literal equations"),
])

deck.pause("14_pause2", "PAUSE  &  TRY  #2",
           "Solve  d = rt  for  r:", "d = r × t",
           hint="Treat d and t as numbers.  You want r alone.")
deck.duplicate("14_pause2", "15_pause2_silence")

deck.recap("16_recap", "Recap.", [
    "Distribute parentheses first.",
    "Combine like terms before solving.",
    "Variables on both sides — move the smaller coefficient.",
    "Fractions — multiply by the LCD to clear them.",
    "Literal equations are just letter-rearranging with the same rules.",
])

deck.path("17_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Ch 2.4–2.5", "Multi-step + literal equations"),
    ("2.", "Khan Academy practice",    "Variables on Both Sides"),
    ("3.", "Assignment in dashboard",  "10 multi-step equations  +  5 literal equations to rearrange"),
    ("4.", "Advisor check-in",         "Literal equations feel weird at first — book a session if they don't click"),
], next_text="Next up:  Module 6 — Inequalities & Interval Notation.  One detail breaks everything.")

print("Module 5 slides built.")

"""Module 1 — Primitive Types (AP Computer Science A).

CS theme = steel-blue accent (auto-resolved from course name).
Code rendered via deck.equation() — mono font, MAROON on focus lines,
MUTED on inline comments. Lines stay <= 32 chars wide at 80pt mono.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="AP Computer Science A", module_num=1,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 1 — Primitive Types",
           "Sample lesson  ·  ~7 minutes")

# 02 — hook: hello-world Java
deck.equation("02_hook", "Your first Java program.", [
    ('System.out.println(', INK, None),
    ('  "Hello, GIIS!"',    MAROON, "the message"),
    (");",                  INK, "semicolon ends the statement"),
])

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "What makes Java tick — compile, bytecode, JVM.",
    "Primitives: int, double, boolean, char.",
    "Variables, casting, and println.",
], footnote="By the end you'll be reading and writing Java statements.")

# 04 — what is Java (definition)
deck.definition("04_what_is_java",
                "Java is a compiled language.",
                ".java  →  .class  →  JVM",
                sub="Source code compiles to bytecode. The JVM runs the bytecode.  Write once, run anywhere.")

# 05 — primitives intro (definition)
deck.definition("05_primitives_intro",
                "Primitives store SIMPLE values.",
                "int  ·  double  ·  boolean  ·  char",
                sub="Whole numbers · decimals · true/false · a single character.")

# 06 — int + double
deck.equation("06_int_double", "Whole numbers and decimals.", [
    ("int age = 17;",     MAROON, "whole numbers"),
    ("double pi = 3.14;", MAROON, "decimals"),
    ("int max ≈ 2 billion", MUTED, "for bigger whole numbers, use long"),
])

# 07 — boolean + char
deck.equation("07_boolean_char", "True/false and single characters.", [
    ("boolean isOpen = true;", MAROON, "true or false — nothing else"),
    ("char grade = 'A';",      MAROON, "SINGLE quotes for char"),
    ('String name = "Alan";',  MUTED,  "double quotes = String (not primitive)"),
])

# 08 — declaration pattern
deck.equation("08_declaration", "Pattern:  type  name  =  value;", [
    ("int score = 95;",       MAROON, "type · name · value · ;"),
    ("double rate = 0.075;",  MAROON, "every statement ends with ;"),
])

# 09 — pause1
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Declare three variables:",
           "pi (3.14)  ·  isOpen (true)  ·  count (5)",
           hint="Pick the right primitive type for each.")
deck.duplicate("09_pause1", "10_pause1_silence")

# 11 — casting
deck.equation("11_casting", "Casting — explicit vs. widening.", [
    ("int x = (int) 3.9;", MAROON, "x = 3   (TRUNCATES — does not round!)"),
    ("double y = 5;",      MAROON, "auto-widens to 5.0   (no cast needed)"),
    ("(int) cuts off",     MUTED,  "the most common gotcha in CS A"),
])

# 12 — println
deck.equation("12_println", "println — compute vs. print text.", [
    ("println(2 + 3);",   MAROON, "prints  5   (Java computes)"),
    ('println("2 + 3");', MAROON, 'prints  2 + 3   (quotes = String)'),
    ("Quotes = text.",    MUTED,  "without quotes, Java computes"),
])

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Java is compiled  →  .class bytecode  →  JVM.",
    "Four primitives:  int · double · boolean · char.",
    "Declare with:  type  name = value;",
    "(int) TRUNCATES — it does not round.",
    "println prints.  Quotes turn anything into a String.",
], assignment=[
    "Write a Java program that declares your  age,  GPA,  and  isHonorRoll,",
    "then prints all three with System.out.println.",
])

# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read CodeHS / Runestone",  "Primitive Types chapter — interactive code blocks"),
    ("2.", "Practice on Codingbat",    "10 small programs · one per new idea today"),
    ("3.", "Assignment in dashboard",  "age + GPA + isHonorRoll · printed with println"),
    ("4.", "Advisor check-in",         "Book a session if casting or println feels fuzzy"),
], next_text="Next up:  Module 2 — Using Objects.")

print("Module 1 (Primitive Types) slides built via slide_kit.")

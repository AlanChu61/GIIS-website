"""Module 7 — ArrayList (AP Computer Science A).

CS theme = steel-blue accent (auto-resolved from course name).
Java code rendered via deck.equation() — mono font, MAROON on focus lines,
MUTED on inline comments. Lines stay <= 32 chars wide at 80pt mono.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="AP Computer Science A", module_num=7,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 7 — ArrayList",
           "Sample lesson  ·  ~8 minutes")

# 02 — hook: arrays are fixed; ArrayList grows
def _hook(img, d):
    d.text((110, 90), "Arrays are FIXED forever.",
           fill=MAROON, font=font("serif_bold", 70))
    # Show fixed array problem
    d.rounded_rectangle([110, 240, W - 110, 470], radius=20,
                        outline=RED, width=5, fill=deck.card_bg)
    d.text((150, 270), "Fixed-size array", fill=RED, font=font("serif_bold", 44))
    centered(d, "int[] students = new int[10];", font("mono", 56), 350, INK)
    centered(d, "Need an 11th student?  Can't.", font("sans", 36), 420, MUTED)
    # Show ArrayList solution
    d.rounded_rectangle([110, 520, W - 110, 760], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((150, 550), "ArrayList — grows and shrinks", fill=deck.accent,
           font=font("serif_bold", 44))
    centered(d, "list.add(student);", font("mono", 56), 630, INK)
    centered(d, "As many as you want.  On demand.", font("sans", 36), 700, MUTED)
    centered(d, "Same indexing.  None of the pain.",
             font("sans_bold", 38), 810, MAROON)

deck.custom("02_hook", _hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "ArrayList vs. plain array — what's different.",
    "Six core methods: add, get, set, remove, size.",
    "Iteration + the autoboxing pitfall.",
], footnote="The most-used container in the Java standard library.")

# 04 — import
deck.equation("04_import", "ArrayList lives in  java.util.", [
    ("import java.util.ArrayList;", MAROON, "name the class directly"),
    ("import java.util.*;",         MAROON, "or the whole package"),
])

# 05 — declaration
deck.equation("05_declaration", "Declaring with generics.", [
    ("ArrayList<String> names =",  MAROON, "type goes in angle brackets"),
    ("    new ArrayList<>();",     MAROON, "the <> diamond infers the type"),
])

# 06 — generics (definition)
deck.definition("06_generic",
                "GENERICS  =  type-safe collections.",
                "ArrayList<String>  only accepts  String.",
                sub="Primitives (int, double) need wrappers (Integer, Double).")

# 07 — the six methods
deck.equation("07_methods", "The 6 methods you use 99% of the time.", [
    ("list.add(x);",     MAROON, "append to the end"),
    ("list.add(i, x);",  MAROON, "insert at index i"),
    ("list.get(i);",     MAROON, "element at index i"),
    ("list.set(i, x);",  MAROON, "replace at index i"),
    ("list.remove(i);",  MAROON, "remove at index i"),
    ("list.size();",     MAROON, "count — note the ()"),
])

# 08 — pause1
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Create ArrayList<String>, add A,B,C,",
           'remove(1) — print what remains.',
           hint="remove(1) removes B.  Result is [A, C].")
deck.duplicate("08_pause1", "09_pause1_silence")

# 10 — indexed for loop
deck.equation("10_iterate_for", "Iterate — indexed for loop.", [
    ("for (int i=0;",          MAROON, None),
    ("     i<list.size();",    MAROON, ".size()  is a METHOD — needs ()"),
    ("     i++) {",            MAROON, None),
    ("  println(list.get(i));", INK,    "vs. array.length (field, no ())"),
    ("}",                       MAROON, None),
])

# 11 — enhanced for loop
deck.equation("11_iterate_foreach", "Iterate — enhanced for loop.", [
    ("for (String s : list) {", MAROON, "cleaner when you just READ"),
    ("  println(s);",           INK,    None),
    ("}",                       MAROON, None),
    ("Don't add/remove here!",  MUTED,  "→ ConcurrentModificationException"),
])

# 12 — array vs ArrayList comparison
deck.compare("12_array_vs_list", "Array  vs.  ArrayList.",
    left={
        "label": "ARRAY",
        "color": MAROON,
        "lines": [
            "·  Fixed size — set once.",
            "·  Uses  .length  (field).",
            "·  Slightly faster.",
            "·  Holds primitives directly.",
            "·  int[]  double[]  char[]",
        ],
        "footnote": "Best when size is known and won't change.",
    },
    right={
        "label": "ArrayList",
        "color": deck.accent,
        "lines": [
            "·  Grows and shrinks freely.",
            "·  Uses  .size()  (method).",
            "·  Small overhead.",
            "·  Holds OBJECTS only.",
            "·  Primitives → wrappers.",
        ],
        "footnote": "Best when size changes as the program runs.",
    },
)

# 13 — autoboxing
deck.equation("13_autoboxing", "Autoboxing — primitive ↔ wrapper.", [
    ("ArrayList<Integer> nums",  MAROON, "wrapper class — not int!"),
    ("    = new ArrayList<>();", MAROON, None),
    ("nums.add(5);",             MAROON, "5 auto-BOXED into Integer"),
    ("int x = nums.get(0);",     MAROON, "auto-UNBOXED back to int"),
    ("null → NullPointer!",      MUTED,  "unboxing a null Integer crashes"),
])

# 14 — recap
deck.recap("14_recap", "Recap.", [
    "ArrayList grows and shrinks  —  arrays are fixed.",
    "Import  java.util.ArrayList;   declare with  <Type>.",
    "6 methods:  add · add(i,x) · get · set · remove · size.",
    "Use  .size()  (method) — NOT  .length  (field).",
    "Holds objects only  →  primitives are autoboxed to wrappers.",
], assignment=[
    "Read 5 strings from input into an ArrayList,",
    "then print them in REVERSE order.",
])

# 15 — path
deck.path("15_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read Runestone — ArrayList", "Interactive code blocks · try every example"),
    ("2.", "Codingbat AP-1 ArrayList",   "Work the full practice set"),
    ("3.", "Assignment in dashboard",    "Reverse-print 5 strings from input"),
    ("4.", "Advisor check-in",           "Book a session if iteration feels fuzzy"),
], next_text="Next up:  Module 8 — 2D Array.")

print("Module 7 (ArrayList) slides built via slide_kit.")

"""AP CS A Module 2 — Using Objects."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="AP Computer Science A", module_num=2,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 2 — Using Objects",
           "Sample lesson  ·  ~7 minutes")


# 02 — hook  (custom: phone-as-object analogy)
def hook(img, d):
    d.text((110, 90), "Your phone is an object.",
           fill=MAROON, font=font("serif_bold", 70))
    # Two columns: HAS  vs  DOES
    box_w, box_h, gap = 760, 480, 80
    left_x = (W - 2 * box_w - gap) // 2
    right_x = left_x + box_w + gap
    # Left: HAS (data)
    d.rounded_rectangle([left_x, 260, left_x + box_w, 260 + box_h],
                        radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((left_x + 40, 290), "HAS  (data)", fill=deck.accent,
           font=font("serif_bold", 48))
    for i, item in enumerate(["·  battery %",
                              "·  contact list",
                              "·  photos",
                              "·  current location"]):
        d.text((left_x + 60, 380 + i * 70), item, fill=INK, font=font("sans", 36))
    # Right: DOES (methods)
    d.rounded_rectangle([right_x, 260, right_x + box_w, 260 + box_h],
                        radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((right_x + 40, 290), "DOES  (methods)", fill=deck.accent,
           font=font("serif_bold", 48))
    for i, item in enumerate(["·  ring()",
                              "·  text(msg)",
                              "·  takePhoto()",
                              "·  navigate(to)"]):
        d.text((right_x + 60, 380 + i * 70), item,
               fill=INK, font=font("mono", 34))
    # Punchline
    d.text((110, 820), "Java objects work the same way:  data  +  behavior  bundled.",
           fill=deck.accent, font=font("sans_bold", 34))
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Primitive types vs. reference types.",
    "The String class + the Math class.",
    "Creating objects with  new  + the  ==  vs  .equals()  trap.",
], footnote="By the end, you'll know why  s1 == s2  is almost always a bug.")


# 04 — primitive vs reference
deck.definition("04_primitive_vs_ref",
                "Primitive vs. reference.",
                "Primitive holds the VALUE.  Reference holds an ADDRESS.",
                sub="int, double, boolean store the value directly. "
                    "String, Random, Scanner store a pointer to an object.")


# 05 — String methods  (Java code via equation/mono)
deck.equation("05_string_methods",
              "Four String methods you'll use forever.", [
    ("s.length()",            INK,         "number of chars"),
    ("s.substring(0, 3)",     INK,         "first 3 chars"),
    ("s.indexOf(\"a\")",      INK,         "position of 'a' (or -1)"),
    ("s.toUpperCase()",       MAROON,      "new uppercase String"),
])


# 06 — String immutability
deck.definition("06_string_immut",
                "Strings are immutable.",
                "You can never change a String — only replace it.",
                sub="s = s + \"!\"  creates a NEW String. "
                    "The original is unchanged.")


# 07 — Math class
deck.equation("07_math_class",
              "The Math class — utility methods, no  new  needed.", [
    ("Math.abs(-7)",     INK,    "→  7"),
    ("Math.pow(2, 8)",   INK,    "→  256.0"),
    ("Math.sqrt(25)",    INK,    "→  5.0"),
    ("Math.random()",    MAROON, "→  random double in [0, 1)"),
])


# 08 — pause and try
def pause1(img, d):
    d.rectangle([0, 80, W, 220], fill=deck.accent)
    centered(d, "PAUSE  &  TRY", font("serif_bold", 96), 100, MAROON_DARK)
    d.text((110, 290), "Compute these two:", fill=INK, font=font("sans", 46))
    # Question 1
    centered(d, "Math.pow(2, 8)", font("mono", 90), 400, MAROON)
    # Question 2
    centered(d, '"Genesis".substring(0, 3)', font("mono", 80), 560, MAROON)
    d.text((110, 760),
           "Hint:  pow() returns double.  substring is (inclusive, exclusive).",
           fill=MUTED, font=font("sans", 36))
deck.custom("08_pause1", pause1)
deck.duplicate("08_pause1", "09_pause1_silence")


# 10 — wrapper classes
deck.definition("10_wrapper",
                "Wrapper classes.",
                "Integer wraps int.  Double wraps double.",
                sub="Needed when collections (like ArrayList) "
                    "only accept objects, not primitives. Java auto-boxes.")


# 11 — new keyword
deck.equation("11_new_keyword",
              "Creating objects:  Type var = new Type(args);", [
    ("Random r = new Random();", INK,    "now r is a Random object"),
    ("String s = new String(\"hi\");", MUTED, "rare — usually just \"hi\""),
    ("Scanner in = new Scanner(...)", MAROON, "same pattern, every time"),
])


# 12 — == vs .equals() comparison
deck.compare("12_compare_equals",
             "The big trap — comparing Strings.",
             left={
                 "label": "✗  WRONG",
                 "color": RED,
                 "lines": [
                     "if (s1 == s2) { ... }",
                     "",
                     "==  compares REFERENCES",
                     "(memory addresses).",
                     "",
                     "Breaks the moment one",
                     "String is created with new.",
                 ],
                 "footnote": "Almost never what you want."
             },
             right={
                 "label": "✓  RIGHT",
                 "color": MAROON,
                 "lines": [
                     "if (s1.equals(s2)) { ... }",
                     "",
                     ".equals()  compares the",
                     "actual contents of the",
                     "Strings, character by",
                     "character.",
                 ],
                 "footnote": "Use this for ALL String comparison."
             })


# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Primitive holds a value · reference holds an address.",
    "String:  length, substring, indexOf, toUpperCase.",
    "Math:  random, abs, pow, sqrt  (no  new  needed).",
    "Create objects with  new ClassName(args).",
    "Compare Strings with  .equals()  — NEVER with  ==.",
], assignment=[
    "Write a Java program that:",
    "1.  reads a name from the user,",
    "2.  prints its length,",
    "3.  prints the uppercase version,",
    "4.  prints the first 3 letters.",
])


# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Runestone — Using Objects chapter", "Read + do the in-line exercises"),
    ("2.", "Codingbat — String-1",    "10 short problems · cements the methods"),
    ("3.", "Assignment in dashboard", "Name-processor program (see recap)"),
    ("4.", "Advisor check-in",        "Especially if  ==  vs  .equals()  is still fuzzy"),
], next_text="Next up:  Module 3 — Boolean Expressions and if Statements.")

print("AP CS A Module 2 (Using Objects) slides built via slide_kit.")

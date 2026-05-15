"""Module 6 — Arrays (AP Computer Science A).

CS theme = steel-blue accent (auto-resolved from course name).
Java code via deck.equation() — mono font, lines kept <= 32 chars at 80pt.
Two custom slides: 02_hook (scale problem visual) and 12_common_algos
(three side-by-side templates).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, CREAM, PARCHMENT,
)

deck = Deck(course="AP Computer Science A", module_num=6,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 6 — Arrays",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook (custom): the scale problem — 30 variables vs. 1 array
def hook(img, d):
    d.text((110, 90), "The scale problem.", fill=MAROON,
           font=font("serif_bold", 76))
    d.text((110, 200),
           "Tracking 30 students' grades.  What do you do?",
           fill=INK, font=font("sans", 38))

    # Left card: the bad way — 30 variables
    d.rounded_rectangle([110, 290, 900, 820], radius=20,
                        outline=RED, width=5, fill=deck.card_bg)
    d.text((140, 310), "✗  THIRTY  VARIABLES?", fill=RED,
           font=font("serif_bold", 40))
    d.text((140, 380), "int g1 = 88;",  fill=INK, font=font("mono", 36))
    d.text((140, 430), "int g2 = 91;",  fill=INK, font=font("mono", 36))
    d.text((140, 480), "int g3 = 76;",  fill=INK, font=font("mono", 36))
    d.text((140, 530), "int g4 = ...;", fill=INK, font=font("mono", 36))
    d.text((140, 600), "...", fill=MUTED, font=font("mono", 48))
    d.text((140, 670), "int g30 = 95;", fill=INK, font=font("mono", 36))
    d.text((140, 750), "(unmaintainable)", fill=MUTED,
           font=font("sans", 28))

    # Right card: the good way — ONE array
    d.rounded_rectangle([1020, 290, 1810, 820], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((1050, 310), "✓  ONE  ARRAY", fill=deck.accent,
           font=font("serif_bold", 40))
    d.text((1050, 410), "int[] grades", fill=INK, font=font("mono", 40))
    d.text((1050, 470), "    = new int[30];", fill=INK,
           font=font("mono", 40))
    d.text((1050, 600), "30 slots.", fill=MAROON,
           font=font("serif_bold", 44))
    d.text((1050, 670), "One name.", fill=MAROON,
           font=font("serif_bold", 44))
    d.text((1050, 750), "That container is an ARRAY.", fill=MUTED,
           font=font("sans", 28))

    d.text((110, 870),
           "Same type.  Fixed size.  Indexed in order.",
           fill=deck.accent, font=font("sans_bold", 34))

deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Declaration & initialization.",
    "Indexing + .length.",
    "Traversal + common algorithms.",
], footnote="Master arrays  →  half of CS A is muscle memory.")


# 04 — declaration: two ways
deck.equation("04_declaration", "Two ways to declare an array.", [
    ("int[] grades = new int[30];", MAROON,
     "size 30 · all slots initialized to 0"),
    ("int[] xs = {5, 10, 15};", MAROON,
     "literal form · Java sizes it for you"),
    ("type[] name = ...", MUTED,
     "the bracket pair makes it an array type"),
])


# 05 — initialize with literals
deck.equation("05_init_literal", "Initialize with literal values.", [
    ('String[] names =', INK, None),
    ('  {"Anya","Bo","Cami"};', MAROON,
     "three Strings · array of size 3"),
    ('double[] rates =', INK, None),
    ('  {0.05, 0.075};', MAROON,
     "two doubles · array of size 2"),
])


# 06 — indexing (zero-indexed)
deck.equation("06_indexing", "Zero-indexed.  0 to length − 1.", [
    ("int[] xs = {10, 20, 30};", MAROON, "size 3"),
    ("xs[0]   →   10", MAROON, "first element is index 0"),
    ("xs[2]   →   30", MAROON, "last element is index 2  (size − 1)"),
    ("xs[3]   →   ✗", RED,
     "ArrayIndexOutOfBoundsException"),
])


# 07 — .length is a field
deck.equation("07_length", ".length  is a FIELD  (no parens).", [
    ("int[] xs = {10, 20, 30};", MAROON, None),
    ("xs.length    →   3", MAROON, "no parentheses · it's a field"),
    ("xs.length-1  →   2", MAROON, "the last valid index"),
    ('"hi".length()', MUTED,
     "Strings use length() · arrays use .length"),
])


# 08 — standard for loop traversal
deck.equation("08_traverse_for", "Traversal — standard for loop.", [
    ("for (int i = 0;", MAROON, None),
    ("     i < arr.length;", MAROON, "stop BEFORE length"),
    ("     i++) {", MAROON, None),
    ("  System.out.println(", INK, None),
    ("    arr[i] );", INK, "read or write at index i"),
    ("}", INK, None),
])


# 09 — pause1: sum the elements
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Sum every element of  int[] grades.",
           "int sum = ?  ·  loop  ·  add",
           hint="Start sum = 0.  Loop with i = 0 to length − 1.  Add each grades[i].")
deck.duplicate("09_pause1", "10_pause1_silence")


# 11 — for-each (enhanced for)
deck.equation("11_traverse_foreach", "For-each — cleaner for read-only.", [
    ("int sum = 0;", INK, None),
    ("for (int g : grades) {", MAROON,
     "g = each element in turn"),
    ("  sum += g;", MAROON, None),
    ("}", MAROON, None),
    ("// can't write to grades via g", MUTED,
     "use indexed for-loop when you need to modify"),
])


# 12 — common algorithms (custom): MAX · COUNT · FIND, three side-by-side
def common_algos(img, d):
    d.text((110, 90), "Three patterns you'll write all year.",
           fill=MAROON, font=font("serif_bold", 56))

    cards = [
        ("MAX",
         "Track largest.",
         [
             "int max = arr[0];",
             "for (int x : arr)",
             "  if (x > max)",
             "    max = x;",
         ]),
        ("COUNT",
         "Count matches.",
         [
             "int count = 0;",
             "for (int x : arr)",
             "  if (x == target)",
             "    count++;",
         ]),
        ("FIND",
         "Linear search.",
         [
             "int idx = -1;",
             "for (int i = 0;",
             "  i < arr.length; i++)",
             "  if (arr[i]==v)",
             "    idx = i;",
         ]),
    ]

    col_w = 580
    gap = 30
    total = col_w * 3 + gap * 2
    start_x = (W - total) // 2
    f_lab = font("serif_bold", 44)
    f_idea = font("sans", 28)
    f_code = font("mono", 28)

    for i, (label, idea, code_lines) in enumerate(cards):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, 220, x + col_w, 880], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 250), label, fill=MAROON, font=f_lab)
        d.text((x + 30, 320), idea, fill=MUTED, font=f_idea)
        y = 410
        for line in code_lines:
            d.text((x + 30, y), line, fill=INK, font=f_code)
            y += 60

    d.text((110, 920),
           "Same skeleton:  initialize  ·  loop  ·  check  ·  update.",
           fill=deck.accent, font=font("sans_bold", 30))

deck.custom("12_common_algos", common_algos)


# 13 — common bug: off-by-one with .length
deck.compare("13_oobe", "The #1 array bug.",
    left={
        "label": "✗  WRONG",
        "color": RED,
        "lines": [
            "arr[arr.length]",
            "",
            "Index .length is",
            "OUT of bounds.",
            "",
            "Throws Array-",
            "IndexOutOfBounds-",
            "Exception.",
        ],
        "footnote": "Valid indices stop at length − 1.",
    },
    right={
        "label": "✓  RIGHT",
        "color": deck.accent,
        "lines": [
            "arr[arr.length - 1]",
            "",
            "This is the LAST",
            "element.",
            "",
            "Indices run from",
            "0  to  length − 1.",
        ],
        "footnote": "Burn this pattern into your fingers.",
    })


# 14 — recap
deck.recap("14_recap", "Recap.", [
    "Declare:  new int[size]  or  {literal}.",
    "Zero-indexed.  Valid:  0  to  length − 1.",
    ".length  is a FIELD  —  no parentheses.",
    "Indexed for-loop  =  read OR write.",
    "For-each loop  =  read-only, cleaner.",
    "Last index  =  arr.length − 1.",
], assignment=[
    "Write three programs:",
    "(1) array average     (2) count evens     (3) find max",
])


# 15 — path
deck.path("15_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Runestone — Array chapter",
            "Interactive code blocks — best way to make it stick"),
    ("2.", "Codingbat — Array-1 + Array-2",
            "15 problems · do them all · don't peek at the answers"),
    ("3.", "Assignment in dashboard",
            "average · count evens · find max"),
    ("4.", "Advisor check-in",
            "Book a session if traversal feels fuzzy"),
], next_text="Next up:  Module 7 — ArrayList.")

print("Module 6 (Arrays) slides built via slide_kit.")

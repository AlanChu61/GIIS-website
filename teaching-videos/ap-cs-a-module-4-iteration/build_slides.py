"""Module 4 — Iteration (AP Computer Science A).

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

deck = Deck(course="AP Computer Science A", module_num=4,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 4 — Iteration",
           "Sample lesson  ·  ~8 minutes")

# 02 — hook (custom): billions per second, loops hand them the scale
def hook(img, d):
    d.text((110, 90), "Loops scale your code.", fill=MAROON, font=font("serif_bold", 72))
    # Big number
    centered(d, "1,000,000,000+", font("mono", 170), 230, INK)
    d.text((W/2 - 280, 410), "operations per second", fill=MUTED, font=font("sans", 38))
    # Subtitle/arrow
    centered(d, "Loops hand the computer that scale.",
             font("serif_bold", 48), 540, MAROON)
    # Two camp boxes — without loops vs with loops
    box_w, box_h, gap = 760, 280, 80
    left_x = (W - 2*box_w - gap) // 2
    right_x = left_x + box_w + gap
    d.rounded_rectangle([left_x, 650, left_x+box_w, 650+box_h],
                         radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((left_x+40, 680), "Without loops:", fill=MUTED, font=font("sans_bold", 32))
    d.text((left_x+40, 740), "calculator math.", fill=INK, font=font("serif_bold", 50))
    d.text((left_x+40, 820), "one line  →  one answer", fill=MUTED, font=font("sans", 28))
    d.rounded_rectangle([right_x, 650, right_x+box_w, 650+box_h],
                         radius=24, outline=MAROON, width=5, fill=deck.card_bg)
    d.text((right_x+40, 680), "With loops:", fill=MUTED, font=font("sans_bold", 32))
    d.text((right_x+40, 740), "real programs.", fill=INK, font=font("serif_bold", 50))
    d.text((right_x+40, 820), "3 lines  →  1M records", fill=deck.accent, font=font("sans_bold", 28))
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "while loops — for unknown counts.",
    "for and enhanced-for — for known counts.",
    "Loop patterns + common pitfalls.",
], footnote="By the end you'll spot every loop bug in a code sample.")

# 04 — while loop syntax
deck.equation("04_while", "while loop — the simplest loop.", [
    ("while (cond) {",   MAROON, "as long as cond is true…"),
    ("  // do stuff",    MUTED,  "…run the body"),
    ("}",                MAROON, "check happens BEFORE each iter"),
])

# 05 — while example: count down from 10
deck.equation("05_while_example", "Count down from 10.", [
    ("int n = 10;",                 MAROON, "start at 10"),
    ("while (n > 0) {",             MAROON, "loop while n is positive"),
    ("  System.out.println(n);",    INK,    "print current n"),
    ("  n--;",                      MUTED,  "DECREMENT — moves toward exit"),
    ("}",                           MAROON, None),
])

# 06 — for loop syntax
deck.equation("06_for_loop", "for loop — three parts.", [
    ("for (init; cond; step) {",  MAROON, "init once · cond before · step after"),
    ("  // body",                 MUTED,  None),
    ("}",                         MAROON, None),
    ("for (int i=0; i<5; i++)",   INK,    "loops exactly 5 times"),
])

# 07 — for example: sum 1 to 100 (Gauss)
deck.equation("07_for_example", "Sum 1 to 100  (Gauss).", [
    ("int sum = 0;",                MAROON, "running total starts at 0"),
    ("for (int i=1; i<=100; i++) {", MAROON, "i from 1 to 100 INCLUSIVE"),
    ("  sum += i;",                 INK,    "add i to sum"),
    ("}",                           MAROON, None),
    ("// sum == 5050",              MUTED,  "Gauss did this in his head"),
])

# 08 — enhanced for / for-each
deck.equation("08_enhanced_for", "Enhanced for (for-each, Java 5+).", [
    ("for (int x : arr) {",         MAROON, "read: 'for each x in arr'"),
    ("  System.out.println(x);",    INK,    "visit every element"),
    ("}",                           MAROON, None),
    ("// READ-ONLY",                MUTED,  "assigning to x does NOT mutate arr"),
])

# 09 — pause1
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Write a loop that sums the squares of 1 through 10.",
           "1²  +  2²  +  …  +  10²",
           hint="For i from 1 to 10, add i*i to a running total.")
deck.duplicate("09_pause1", "10_pause1_silence")

# 11 — nested loops: multiplication table
deck.equation("11_nested_loops", "Nested loops — a 3x3 table.", [
    ("for (int r=1; r<=3; r++) {",  MAROON, "outer loop — rows"),
    ("  for (int c=1; c<=3; c++) {", MAROON, "inner loop — columns"),
    ("    print(r * c);",           INK,    "do work with r and c"),
    ("  }",                         MUTED,  None),
    ("}",                           MAROON, None),
])

# 12 — patterns (custom): four classic loop patterns
def patterns(img, d):
    d.text((110, 90), "Four loop patterns — memorize these.",
           fill=MAROON, font=font("serif_bold", 56))
    # 2x2 grid of cards
    card_w, card_h = 830, 290
    gap_x, gap_y = 60, 40
    grid_left = (W - 2*card_w - gap_x) // 2
    grid_top = 230
    cards = [
        ("SUM",   "running total",     [
            "int sum = 0;",
            "for (... ) sum += x;",
        ]),
        ("COUNT", "counter for matches", [
            "int count = 0;",
            "for (... )",
            "  if (cond) count++;",
        ]),
        ("MAX",   "track largest seen", [
            "int max = arr[0];",
            "for (... )",
            "  if (x > max) max = x;",
        ]),
        ("MIN",   "track smallest seen", [
            "int min = arr[0];",
            "for (... )",
            "  if (x < min) min = x;",
        ]),
    ]
    for i, (name, sub, lines) in enumerate(cards):
        col, row = i % 2, i // 2
        x = grid_left + col*(card_w + gap_x)
        y = grid_top + row*(card_h + gap_y)
        d.rounded_rectangle([x, y, x+card_w, y+card_h], radius=20,
                             outline=MAROON, width=4, fill=deck.card_bg)
        # Header badge
        d.rounded_rectangle([x+24, y+24, x+220, y+90], radius=12, fill=MAROON)
        bw = d.textlength(name, font=font("serif_bold", 40))
        d.text((x+24 + (196 - bw)/2, y+30), name, fill=deck.accent, font=font("serif_bold", 40))
        d.text((x+240, y+38), sub, fill=MUTED, font=font("sans", 28))
        # Code lines
        ly = y + 115
        for ln in lines:
            d.text((x+30, ly), ln, fill=INK, font=font("mono", 30))
            ly += 50
deck.custom("12_patterns", patterns)

# 13 — off-by-one (compare): wrong vs right
deck.compare("13_off_by_one",
    "Off-by-one — the classic trap.",
    {
        "label":   "✗ WRONG",
        "color":   RED,
        "lines": [
            "for (int i = 0;",
            "     i <= arr.length;",
            "     i++) {",
            "  use(arr[i]);",
            "}",
        ],
        "footnote": "arr[arr.length] doesn't exist → crash.",
    },
    {
        "label":   "✓ RIGHT",
        "color":   MAROON,
        "lines": [
            "for (int i = 0;",
            "     i < arr.length;",
            "     i++) {",
            "  use(arr[i]);",
            "}",
        ],
        "footnote": "Indices go from 0 to length − 1.",
    })

# 14 — infinite loop
deck.equation("14_infinite", "Infinite loop — forgot the step.", [
    ("int n = 10;",              MAROON, None),
    ("while (n > 0) {",          MAROON, None),
    ("  System.out.println(n);", INK,    None),
    ("  // forgot n--;",         RED,    "← counter never changes"),
    ("}",                        MAROON, "INFINITE LOOP  →  Ctrl-C to kill"),
])

# 15 — recap
deck.recap("15_recap", "Recap.", [
    "while  for unknown-count loops.",
    "for  for known-count loops.",
    "enhanced-for  for read-only traversal.",
    "Nested loops for grids and matrices.",
    "4 patterns:  sum · count · max · min.",
    "Off-by-one:  i < length, NOT i <= length.",
], assignment=[
    "Write 4 small programs:  factorial,  FizzBuzz,",
    "find max in an array,  count vowels in a String.",
])

# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read Runestone Iteration", "Interactive chapter on while / for / for-each"),
    ("2.", "Codingbat Logic-2 + Loops", "12 problems — lock in the four patterns"),
    ("3.", "Assignment in dashboard",  "factorial · FizzBuzz · max · count vowels"),
    ("4.", "Advisor check-in",         "Book a session if any pattern feels fuzzy"),
], next_text="Next up:  Module 5 — Writing Classes.")

print("Module 4 (Iteration) slides built via slide_kit.")

"""Module 10 — Recursion (AP Computer Science A).

Hardest unit in the course. Uses slide_kit primitives + a few custom slides
for the stack-trace and binary-search visuals.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

deck = Deck(course="AP Computer Science A", module_num=10,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# ─── 01 — title ───
deck.title("01_title", "AP Computer Science A",
           "Module 10 — Recursion",
           "Final unit  ·  ~9 minutes")

# ─── 02 — hook: matryoshka dolls ───
def hook(img, d):
    d.text((110, 90), "A function that calls itself.",
           fill=MAROON, font=font("serif_bold", 64))
    # Five nested boxes shrinking right — matryoshka stack
    box_x, box_y = 200, 250
    sizes = [(700, 600), (560, 480), (430, 370), (310, 270), (200, 170)]
    colors = [deck.accent, deck.accent_light, MAROON, MAROON_DARK, deck.accent]
    cx, cy = 960, 560
    for i, (bw, bh) in enumerate(sizes):
        x0 = cx - bw // 2
        y0 = cy - bh // 2
        d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh],
                            radius=24, outline=colors[i], width=6,
                            fill=deck.card_bg if i % 2 == 0 else deck.bg)
    d.text((cx - 30, cy - 30), "1", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 920),
           "Each call is a smaller version of the same problem  ·  until it's tiny.",
           fill=deck.accent, font=font("sans_bold", 32))
deck.custom("02_hook", hook)

# ─── 03 — overview ───
deck.overview("03_overview", "Game plan.", [
    "Recursion in one sentence.",
    "The two parts every recursive method needs.",
    "Classics: factorial, Fibonacci, sum-of-digits, reverse, binary search.",
    "When to use it  ·  when iteration is cleaner.",
], footnote="Recursion is the hardest unit. Slow down. Trace by hand.")

# ─── 04 — what is recursion ───
deck.definition("04_what_is", "What is recursion?",
                "A method that calls itself on a smaller input.",
                "Each call solves a smaller piece — until the smallest case is obvious.")

# ─── 05 — two parts ───
deck.definition("05_two_parts", "Every recursive method needs:",
                "BASE CASE  +  RECURSIVE CASE",
                "Miss either, and you get StackOverflowError.")

# ─── 06 — factorial code ───
deck.equation("06_factorial", "Example  ·  factorial.   n! = n × (n−1)!", [
    ("public int fact(int n) {",       INK,    None),
    ("  if (n == 0) return 1;",        MAROON, "base case"),
    ("  return n * fact(n - 1);",      MAROON, "recursive case"),
    ("}",                              INK,    None),
])

# ─── 07 — factorial trace (custom: call stack going down then back up) ───
def trace(img, d):
    d.text((110, 80), "Trace  ·  fact(4)  on the call stack.",
           fill=MAROON, font=font("serif_bold", 56))
    # Down arrow (calls deepen)
    f_eq = font("mono", 44)
    lines_down = [
        ("fact(4) = 4 * fact(3)", INK),
        ("fact(3) = 3 * fact(2)", INK),
        ("fact(2) = 2 * fact(1)", INK),
        ("fact(1) = 1 * fact(0)", INK),
        ("fact(0) = 1   ← BASE",  MAROON),
    ]
    y = 200
    for text, color in lines_down:
        centered(d, text, f_eq, y, color)
        y += 70
    # Unwind arrow
    d.text((110, y + 20), "↑ unwinds back up:",
           fill=deck.accent, font=font("sans_bold", 32))
    lines_up = ["1", "1 × 1 = 1", "2 × 1 = 2", "3 × 2 = 6", "4 × 6 = 24"]
    y += 80
    f_up = font("mono", 36)
    centered(d, "  →  ".join(lines_up), f_up, y, deck.accent)
deck.custom("07_factorial_trace", trace)

# ─── 08 — fibonacci ───
deck.equation("08_fibonacci", "Example  ·  Fibonacci.   fib(n) = fib(n-1) + fib(n-2)", [
    ("public int fib(int n) {",          INK,    None),
    ("  if (n <= 1) return n;",          MAROON, "two base cases"),
    ("  return fib(n-1) + fib(n-2);",    MAROON, "two recursive calls"),
    ("}",                                INK,    None),
])

# ─── 09 — pause and try ───
deck.pause("09_pause1", "PAUSE  &  TRY",
           "Write sumOfDigits(int n) recursively.",
           "sumOfDigits(123) → 6",
           hint="Base: n < 10. Recursive: (n % 10) + sumOfDigits(n / 10).")

# ─── 10 — pause silence: walked-through answer ───
deck.equation("10_pause1_silence", "Answer  ·  sumOfDigits", [
    ("public int sumOfDigits(int n) {",  INK,    None),
    ("  if (n < 10) return n;",          MAROON, "base case"),
    ("  return (n % 10) +",              MAROON, "last digit"),
    ("    sumOfDigits(n / 10);",         MAROON, "drop the last digit"),
    ("}",                                INK,    None),
])

# ─── 11 — string recursion (reverse) ───
deck.equation("11_string_recursion", "String recursion  ·  reverse(s)", [
    ("public String rev(String s) {",      INK,    None),
    ("  if (s.length() <= 1)",             MAROON, "base case"),
    ("    return s;",                      MAROON, None),
    ("  return rev(s.substring(1))",       MAROON, "rest, reversed"),
    ("    + s.charAt(0);",                 MAROON, "+ first char at end"),
    ("}",                                  INK,    None),
])

# ─── 12 — binary search (custom: sorted array + halving search) ───
def bsearch(img, d):
    d.text((110, 80), "Binary search  ·  divide and conquer.",
           fill=MAROON, font=font("serif_bold", 56))
    # Array of 9 values, looking for 17
    values = [3, 5, 8, 11, 14, 17, 21, 27, 33]
    n = len(values)
    box = 140
    total_w = box * n
    start_x = (W - total_w) // 2
    y = 280
    for i, v in enumerate(values):
        x = start_x + i * box
        # Step 1: full range  (gray boxes)
        outline = INK
        fill = deck.card_bg
        if v == 17:
            outline = MAROON; fill = deck.accent_light
        d.rounded_rectangle([x, y, x + box - 10, y + box - 10],
                            radius=12, outline=outline, width=4, fill=fill)
        centered_v = x + (box - 10) // 2 - d.textlength(str(v), font=font("mono", 56)) // 2
        d.text((centered_v, y + 35), str(v),
               fill=MAROON_DARK if v == 17 else INK, font=font("mono", 56))
        # Index label
        d.text((x + 50, y + box + 5), f"[{i}]", fill=MUTED, font=font("sans", 22))
    # Steps
    f_step = font("sans", 32)
    d.text((110, 620), "Looking for 17 in a sorted array.",
           fill=INK, font=font("sans_bold", 36))
    d.text((110, 690), "1.  Check middle (14). 17 > 14 → search right half.",
           fill=INK, font=f_step)
    d.text((110, 740), "2.  Middle of [17, 21, 27, 33] is 21. 17 < 21 → search left.",
           fill=INK, font=f_step)
    d.text((110, 790), "3.  Found 17 at index 5.  Three comparisons, not nine.",
           fill=deck.accent, font=font("sans_bold", 36))
    d.text((110, 880), "Each call halves the search space  →  O(log n).",
           fill=MAROON, font=font("serif_bold", 36))
deck.custom("12_binary_search", bsearch)

# ─── 13 — stack overflow trap ───
deck.compare("13_stack_overflow",
             "The trap  ·  no base case.",
             left={
                 "label": "✗ INFINITE",
                 "color": RED,
                 "lines": [
                     "int loop(int n) {",
                     "  return loop(n - 1);",
                     "}",
                     "",
                     "Never reaches a stop.",
                     "→ StackOverflowError.",
                 ],
                 "footnote": "No base case = crash.",
             },
             right={
                 "label": "✓ SAFE",
                 "color": MAROON,
                 "lines": [
                     "int loop(int n) {",
                     "  if (n == 0) return 0;",
                     "  return loop(n - 1);",
                     "}",
                     "",
                     "Base case first.",
                 ],
                 "footnote": "Always check base FIRST.",
             })

# ─── 14 — when to use recursion ───
deck.definition("14_when_recursion", "When recursion shines.",
                "Tree / graph traversal  ·  divide-and-conquer  ·  naturally recursive data.",
                "For simple counted loops, iteration is usually clearer and faster.")

# ─── 15 — recursion vs iteration ───
deck.compare("15_rec_vs_iter",
             "Recursion vs. iteration.",
             left={
                 "label": "RECURSION",
                 "color": deck.accent,
                 "lines": [
                     "Cleaner for tree-like",
                     "problems.",
                     "",
                     "Each call uses stack",
                     "memory.",
                     "",
                     "Naive recursion can",
                     "be slow (e.g. fib).",
                 ],
                 "footnote": "Pick when structure is recursive.",
             },
             right={
                 "label": "ITERATION",
                 "color": MAROON,
                 "lines": [
                     "Cleaner for simple",
                     "counted loops.",
                     "",
                     "Constant memory",
                     "(no stack growth).",
                     "",
                     "Usually faster in",
                     "practice.",
                 ],
                 "footnote": "Pick when a loop will do.",
             })

# ─── 16 — common mistakes ───
deck.compare("16_compare",
             "Common mistakes.",
             left={
                 "label": "✗ WRONG",
                 "color": RED,
                 "lines": [
                     "No base case.",
                     "",
                     "Base case never",
                     "triggers.",
                     "",
                     "Recursive call uses",
                     "the SAME input  →",
                     "no progress.",
                 ],
                 "footnote": "All three crash the program.",
             },
             right={
                 "label": "✓ RIGHT",
                 "color": MAROON,
                 "lines": [
                     "Base case FIRST.",
                     "",
                     "Base case reachable",
                     "from every input.",
                     "",
                     "Recursive call uses",
                     "a SMALLER input  →",
                     "progress toward base.",
                 ],
                 "footnote": "Three checks before you ship.",
             })

# ─── 17 — recap ───
deck.recap("17_recap", "Recap.", [
    "Recursion = method calls itself on a smaller input.",
    "Every recursive method needs a base case + a recursive case.",
    "Classics: factorial, Fibonacci, sumOfDigits, reverse, binary search.",
    "Trace by drawing the call stack — down, then back up.",
    "Pick recursion for trees / divide-and-conquer.  Pick iteration for simple loops.",
    "Common bug:  missing base case  →  StackOverflowError.",
], assignment=[
    "Write three recursive methods:",
    "  · power(base, exp)",
    "  · gcd(a, b)            (Euclidean)",
    "  · isPalindrome(String)",
])

# ─── 18 — path ───
deck.path("18_path", items=[
    ("✓",  "Watch this lesson",       "(done — final unit!)"),
    ("1.", "Runestone  ·  Recursion", "Read + run the in-browser examples"),
    ("2.", "Codingbat",                "Recursion-1 + Recursion-2  ·  15 problems"),
    ("3.", "Assignment in dashboard",  "power · gcd · isPalindrome"),
    ("4.", "Advisor check-in",         "Plan your AP exam practice tests"),
], next_text="You've finished AP Computer Science A.  Next stop:  the AP exam.")

print("Module 10 (Recursion) slides built via slide_kit.")

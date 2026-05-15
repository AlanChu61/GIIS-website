"""Module 9 — Inheritance (AP Computer Science A).

CS theme = steel-blue accent. Java code lives in deck.equation() blocks
(mono font). Each code line stays <= 32 chars at 80pt mono.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, CREAM, PARCHMENT,
)
from PIL import ImageDraw

deck = Deck(course="AP Computer Science A", module_num=9,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

ACCENT = deck.accent
ACCENT_LIGHT = deck.accent_light

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 9 — Inheritance",
           "Sample lesson  ·  ~10 minutes")

# 02 — hook: IS-A relationship diagram (custom)
def hook(img, d):
    d.text((110, 90), "IS-A.  The reuse idea.",
           fill=MAROON, font=font("serif_bold", 72))

    # Top: Animal box
    box_w, box_h = 420, 170
    cx = W // 2
    ax, ay = cx - box_w // 2, 240
    d.rounded_rectangle([ax, ay, ax + box_w, ay + box_h], radius=18,
                        outline=MAROON, width=5, fill=PARCHMENT)
    centered(d, "Animal", font("serif_bold", 56), ay + 18, MAROON)
    centered(d, "name · age · eat()", font("mono", 30), ay + 100, INK)

    # Two arrows down to Cat and Dog
    # Cat box (left)
    cx_left = 460
    cy = 600
    d.rounded_rectangle([cx_left, cy, cx_left + box_w, cy + box_h], radius=18,
                        outline=ACCENT, width=5, fill=PARCHMENT)
    centered_x_l = cx_left + box_w // 2
    d.text((centered_x_l - d.textlength("Cat", font=font("serif_bold", 56)) / 2, cy + 18),
           "Cat", fill=MAROON, font=font("serif_bold", 56))
    note_l = "+ purr()"
    d.text((centered_x_l - d.textlength(note_l, font=font("mono", 30)) / 2, cy + 100),
           note_l, fill=INK, font=font("mono", 30))

    # Dog box (right)
    cx_right = W - 460 - box_w
    d.rounded_rectangle([cx_right, cy, cx_right + box_w, cy + box_h], radius=18,
                        outline=ACCENT, width=5, fill=PARCHMENT)
    centered_x_r = cx_right + box_w // 2
    d.text((centered_x_r - d.textlength("Dog", font=font("serif_bold", 56)) / 2, cy + 18),
           "Dog", fill=MAROON, font=font("serif_bold", 56))
    note_r = "+ fetch()"
    d.text((centered_x_r - d.textlength(note_r, font=font("mono", 30)) / 2, cy + 100),
           note_r, fill=INK, font=font("mono", 30))

    # Arrows from Animal down to Cat / Dog
    parent_bottom_x = cx
    parent_bottom_y = ay + box_h
    # Left arrow
    left_top = (parent_bottom_x, parent_bottom_y)
    left_end = (cx_left + box_w // 2, cy)
    d.line([left_top, (left_top[0], (parent_bottom_y + cy) // 2),
            (left_end[0], (parent_bottom_y + cy) // 2), left_end],
           fill=MAROON, width=4)
    # Right arrow
    right_end = (cx_right + box_w // 2, cy)
    d.line([left_top, (left_top[0], (parent_bottom_y + cy) // 2),
            (right_end[0], (parent_bottom_y + cy) // 2), right_end],
           fill=MAROON, width=4)
    # Arrowheads (simple triangles)
    for ex, ey in [left_end, right_end]:
        d.polygon([(ex - 10, ey - 14), (ex + 10, ey - 14), (ex, ey)],
                  fill=MAROON)

    # "IS-A" labels on the arrows
    d.text((cx_left + box_w + 10, 540), "IS-A", fill=ACCENT,
           font=font("sans_bold", 32))
    d.text((cx_right - 100, 540), "IS-A", fill=ACCENT,
           font=font("sans_bold", 32))

    d.text((110, 870),
           "Write Animal ONCE — every subclass reuses it.",
           fill=ACCENT, font=font("sans_bold", 36))

deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "extends + super  (how a class inherits)",
    "Overriding methods  (child does it differently)",
    "Polymorphism  (the big idea)",
    "Abstract classes · Object · instanceof",
], footnote="Dense material. We go slow. Pause whenever you need.")

# 04 — extends
deck.equation("04_extends", "Subclass inherits from superclass.", [
    ("public class Animal {",        MAROON, None),
    ("  private String name;",        INK,    None),
    ("}",                             MAROON, None),
    ("public class Cat extends Animal {", MAROON, None),
    ("  // gets name automatically",  MUTED,  "extends = IS-A"),
    ("}",                             MAROON, None),
])

# 05 — super constructor
deck.equation("05_super_constructor",
              "Subclass constructor calls super FIRST.", [
    ("public Cat(String n) {", MAROON, None),
    ("  super(n);",            MAROON, "calls Animal(n)"),
    ("}",                      MAROON, "super must be line 1"),
])

# 06 — inherited members (definition)
deck.definition("06_inherited_members",
                "Subclass inherits ALL non-private members.",
                "private  =  not directly accessible",
                sub="Use protected fields or accessor methods.  Public methods work as if defined in the subclass.")

# 07 — overriding
deck.equation("07_overriding", "Override — same name, same signature.", [
    ("// in Animal:",     MUTED,  None),
    ("public void sound() {", MAROON, None),
    ('  print("generic");',   INK,    None),
    ("}",                     MAROON, None),
    ("// in Cat:",        MUTED,  None),
    ("@Override",         ACCENT, "tells compiler: I'm replacing parent's"),
    ("public void sound() {", MAROON, None),
    ('  print("meow");',  INK,    None),
    ("}",                 MAROON, None),
])

# 08 — pause1
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Write Cat extends Animal,",
           "override sound() → \"meow\"",
           hint="Use @Override.  Same method signature as parent.")
deck.duplicate("08_pause1", "09_pause1_silence")

# Build a separate answer-key style equation as the "silence" answer reveal.
# (We re-save 09_pause1_silence as a full code walkthrough so the reveal
# shows the worked solution. The 08_pause1 question slide is kept as-is.)
deck.equation("09_pause1_silence",
              "Answer  ·  Cat extends Animal", [
    ("public class Cat extends Animal {", MAROON, None),
    ("  public Cat(String n) {",          MAROON, None),
    ("    super(n);",                     INK,    "first line"),
    ("  }",                               MAROON, None),
    ("  @Override",                       ACCENT, None),
    ("  public void sound() {",           MAROON, None),
    ('    print("meow");',                INK,    None),
    ("  }",                               MAROON, None),
    ("}",                                 MAROON, None),
])

# 10 — polymorphism (the BIG idea)
deck.equation("10_polymorphism", "Polymorphism — the BIG idea.", [
    ('Animal a = new Cat("M");',  MAROON, "declared Animal, actually Cat"),
    ("a.sound();",                MAROON, 'prints  "meow"'),
    ("// Cat's sound() runs.",    MUTED,  "object type wins, not variable type"),
])

# 11 — late binding (definition)
deck.definition("11_late_binding",
                "Late binding  =  decided at RUNTIME.",
                "Java picks the method based on the OBJECT, not the variable.",
                sub="Also called dynamic dispatch.  It's the engine behind polymorphism.")

# 12 — Object class (definition)
deck.definition("12_object_class",
                "Every class extends Object.",
                "toString()  ·  equals(Object o)  ·  hashCode()",
                sub="You get these free.  Override toString to make println pretty.")

# 13 — abstract classes
deck.equation("13_abstract_classes",
              "Abstract class — can't instantiate.", [
    ("public abstract class Shape {", MAROON, None),
    ("  public abstract", MAROON, None),
    ("  double area();",  INK,    "no body — subclasses MUST implement"),
    ("}",                 MAROON, None),
    ("new Shape();  // ERROR",      RED,    "Circle, Rectangle extend Shape"),
])

# 14 — instanceof
deck.equation("14_instanceof", "instanceof — runtime type check.", [
    ("if (a instanceof Cat) {",  MAROON, "is the object really a Cat?"),
    ("  Cat c = (Cat) a;",       MAROON, "safe to cast now"),
    ("  c.purr();",              INK,    "Cat-only method"),
    ("}",                        MAROON, None),
])

# 15 — compare (overriding vs overloading)
deck.compare("15_compare",
             "Overriding  vs.  Overloading.",
             left={
                 "label": "OVERRIDING",
                 "color": MAROON,
                 "lines": [
                     "Same name.",
                     "SAME parameters.",
                     "Across parent and child.",
                     "Decided at RUNTIME.",
                     "Use @Override.",
                 ],
                 "footnote": "Inheritance feature.  Child replaces parent.",
             },
             right={
                 "label": "OVERLOADING",
                 "color": ACCENT,
                 "lines": [
                     "Same name.",
                     "DIFFERENT parameters.",
                     "Inside ONE class.",
                     "Decided at COMPILE time.",
                     "No annotation needed.",
                 ],
                 "footnote": "Multiple versions for different inputs.",
             })

# 16 — recap
deck.recap("16_recap", "Recap.", [
    "extends  →  IS-A relationship.",
    "super  calls the parent's constructor or method.",
    "@Override redefines a parent method with same signature.",
    "Polymorphism  →  variable general, object specific.",
    "Late binding picks the method at RUNTIME.",
    "Every class extends Object.  Abstract classes can't be new'd.",
    "instanceof tests the real type.",
], assignment=[
    "Build a Shape hierarchy:  abstract Shape, then Circle and Rectangle.",
    "Each subclass implements  area().  Print each shape's area.",
])

# 17 — path
deck.path("17_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read Runestone — Inheritance", "Chapter on extends, super, polymorphism"),
    ("2.", "Codingbat AP-1 inheritance", "Practice set — write 10 small subclasses"),
    ("3.", "Assignment in dashboard",  "Shape hierarchy · Circle + Rectangle · area()"),
    ("4.", "Advisor check-in",         "Book a session if polymorphism feels fuzzy"),
], next_text="Next up:  Module 10 — Recursion.")

print("Module 9 (Inheritance) slides built via slide_kit.")

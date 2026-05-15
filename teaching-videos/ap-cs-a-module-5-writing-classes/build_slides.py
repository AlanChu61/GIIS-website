"""Module 5 — Writing Classes (AP Computer Science A).

CS theme = steel-blue accent (auto-resolved from course name).
The hardest module of the first half — 18 sections covering class blueprint,
instance variables, constructors, methods, accessors/mutators, this, toString,
and static. Java code rendered via deck.equation() — mono font. Lines stay
<= 32 chars wide at 80pt mono.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, CREAM,
)

deck = Deck(course="AP Computer Science A", module_num=5,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

# 01 — title
deck.title("01_title", "AP Computer Science A",
           "Module 5 — Writing Classes",
           "Sample lesson  ·  ~10 minutes")

# 02 — hook (custom: USED → WRITE upgrade)
def hook_render(img, d):
    d.text((110, 90), "From USING classes  →  WRITING them.",
           fill=MAROON, font=font("serif_bold", 64))
    # Two-column "before / after"
    d.rounded_rectangle([110, 240, 920, 720], radius=24,
                        outline=MUTED, width=4, fill=deck.card_bg)
    d.text((150, 280), "Before",  fill=MUTED, font=font("serif_bold", 44))
    d.text((150, 360), "You USED Java's classes:",
           fill=INK, font=font("sans", 32))
    f_m = font("mono", 44)
    d.text((150, 430), "String", fill=deck.accent, font=f_m)
    d.text((150, 500), "Math",   fill=deck.accent, font=f_m)
    d.text((150, 570), "Random", fill=deck.accent, font=f_m)
    d.text((150, 660), "Someone else built them.",
           fill=MUTED, font=font("sans", 28))

    d.rounded_rectangle([1000, 240, W - 110, 720], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((1040, 280), "Now", fill=MAROON, font=font("serif_bold", 44))
    d.text((1040, 360), "You'll WRITE your own:",
           fill=INK, font=font("sans", 32))
    d.text((1040, 430), "Student",     fill=MAROON, font=f_m)
    d.text((1040, 500), "BankAccount", fill=MAROON, font=f_m)
    d.text((1040, 570), "Dog",         fill=MAROON, font=f_m)
    d.text((1040, 660), "Model anything you can imagine.",
           fill=MUTED, font=font("sans", 28))

    d.text((110, 800),
           "Class = blueprint.    Object = one instance built from it.",
           fill=deck.accent, font=font("sans_bold", 38))

deck.custom("02_hook", hook_render)

# 03 — overview
deck.overview("03_overview", "Four areas.", [
    "Class vs. object — blueprint vs. instance.",
    "Instance variables + constructors — state & build.",
    "Methods — accessors, mutators, toString.",
    "The  this  keyword  +  static  vs. instance.",
], footnote="The deepest module of the first half — slow down here.")

# 04 — class blueprint (definition)
deck.definition("04_class_blueprint",
                "Class = blueprint.   Object = instance.",
                "One cutter.   Infinite cookies.",
                sub="The class defines the shape.  Each object is one specific thing built from it.")

# 05 — instance variables (Java code)
deck.equation("05_instance_vars", "Instance variables hold state.", [
    ("public class Dog {",     INK,    "the blueprint"),
    ("  private String name;", MAROON, "field — outside code can't touch"),
    ("  private int age;",     MAROON, "private = encapsulation"),
    ("}",                      INK,    None),
])

# 06 — constructor
deck.equation("06_constructor", "Constructor builds an object.", [
    ("public Dog(String n,",   MAROON, "same name as class"),
    ("           int a) {",    MAROON, "no return type — not even void"),
    ("  name = n;",            INK,    None),
    ("  age = a;",             INK,    "assigns parameters to fields"),
    ("}",                      INK,    'call:  new Dog("Rex", 3);'),
])

# 07 — methods
deck.equation("07_methods", "Methods = what a class can DO.", [
    ("public void bark() {",            MAROON, "void = no return value"),
    ('  System.out.println("Woof");',   INK,    None),
    ("}",                                INK,    None),
    ("// or return int, String, etc.",  MUTED,  "put return type before name"),
])

# 08 — accessor (getter)
deck.equation("08_accessor", "Accessor (getter) — READ a field.", [
    ("public String getName() {", MAROON, "return type matches field"),
    ("  return name;",            INK,    None),
    ("}",                          INK,    None),
    ("String n = d.getName();",   MUTED,  "read-only access"),
])

# 09 — mutator (setter)
deck.equation("09_mutator", "Mutator (setter) — CHANGE a field.", [
    ("public void setAge(int a) {", MAROON, "void — no return"),
    ("  age = a;",                  INK,    None),
    ("}",                            INK,    None),
    ("d.setAge(4);",                MUTED,  "controlled write access"),
])

# 10 — this keyword
deck.equation("10_this_keyword", "this.field  resolves shadowing.", [
    ("public Dog(String name) {", MAROON, "parameter shadows the field!"),
    ("  this.name = name;",       INK,    "this.name = field"),
    ("}",                          INK,    "(right side) name = parameter"),
])

# 11 — pause1
deck.pause("11_pause1", "PAUSE  &  TRY",
           "Write a Student class:",
           "name (String)  ·  gpa (double)  ·  getName()",
           hint="Private fields  +  public constructor  +  public accessor.")
deck.duplicate("11_pause1", "12_pause1_silence")

# 13 — toString
deck.equation("13_toString", "Override toString for printing.", [
    ("public String toString() {",      MAROON, "Java calls this in println"),
    ('  return name + " (" + age + ")";', INK,  "concatenate with +"),
    ("}",                                INK,    None),
    ("println(d)  →  Rex (3)",          MUTED,  "called automatically"),
])

# 14 — static (definition)
deck.definition("14_static",
                "static = class-level, not instance-level.",
                "Math.random()  ·  no object needed.",
                sub="Use static for utility methods and counters shared across all instances.")

# 15 — static vs instance
deck.equation("15_static_vs_instance", "Instance vs. static — who do you call?", [
    ("d.bark();",        MAROON, "INSTANCE — need an object"),
    ("Math.random();",   MAROON, "STATIC — call on the CLASS"),
    ("add  static  →  class-level", MUTED, "one keyword changes everything"),
])

# 16 — compare wrong vs right
deck.compare("16_compare", "Common traps.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "public getName() {",
            "  return name;",
            "}",
            "",
            "d.getName    // no parens!",
        ],
        "footnote": "Missing return type → won't compile.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "public String getName() {",
            "  return name;",
            "}",
            "",
            "d.getName()  // call it!",
        ],
        "footnote": "Return type + parens on the call site.",
    })

# 17 — recap
deck.recap("17_recap", "Recap.", [
    "Class = blueprint.  Object = instance.",
    "private fields + public methods  =  encapsulation.",
    "Constructor builds.  Methods do.",
    "this.field  resolves parameter/field shadowing.",
    "toString  controls how the object prints.",
    "static = class-level.   instance = object-level.",
], assignment=[
    "Write a BankAccount class:  balance field,  deposit + withdraw,",
    "getBalance accessor,  and a toString.  Submit in your dashboard.",
])

# 18 — path
deck.path("18_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Runestone — Writing Classes", "Interactive code blocks · trace every example"),
    ("2.", "Codingbat practice",      "AP-1 set  +  Class-design problems"),
    ("3.", "Assignment in dashboard", "BankAccount class · full skeleton + toString"),
    ("4.", "Advisor check-in",        "20 minutes here unblocks the rest of the year"),
], next_text="Next up:  Module 6 — Array.")

print("Module 5 (Writing Classes) slides built via slide_kit.")

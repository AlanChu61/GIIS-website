"""AP Psychology · Module 7 — Memory.

Lavender theme (psychology). Heavy on slide_kit primitives plus a few
custom slides for diagrams that earn their keep:
  - 04 multi-store model as a horizontal flow
  - 06 levels-of-processing depth diagram
  - 07 LTM types tree
  - 09 pause-answer (proactive vs retroactive direction reveal)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=7, output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 7 — Memory",
           "~7 minutes  ·  How memory works, why it fails, how to study smart")

# 02 — hook (the levels-of-processing trap)
def hook(img, d):
    d.text((110, 80), "The studying trap.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 168), "Why re-reading the textbook fails the test.",
           fill=MAROON_DARK, font=font("serif", 44))

    # Two contrasting cards
    cards = [
        (110,  "WHAT YOU DO",
               ["Open the textbook.",
                "Read the chapter twice.",
                "Highlight a bunch of stuff.",
                "Spotify on. Feel productive."],
               MUTED),
        (1000, "WHAT YOUR BRAIN DOES",
               ["Eyes scan the shapes of words.",
                "No meaning attached.",
                "Nothing connects to memory.",
                "You blank on the test."],
               deck.accent),
    ]
    for x, title, lines, color in cards:
        d.rounded_rectangle([x, 290, x + 810, 720], radius=22,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((x + 36, 320), title, fill=color, font=font("sans_bold", 40))
        for i, ln in enumerate(lines):
            d.text((x + 36, 410 + i * 64), ln, fill=INK, font=font("sans", 32))

    d.rounded_rectangle([110, 770, W - 110, 920], radius=22, fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Shallow processing in.  No memory out.",
             font("serif_bold", 46), 800, MAROON_DARK)
    centered(d, "Today: how memory ACTUALLY works — and how to study smart.",
             font("sans", 32), 870, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Multi-store model: sensory  ->  short-term  ->  long-term.",
    "Why you forget — including the AP trap (proactive vs retroactive).",
    "Studying strategies that actually work.",
], footnote="By end: you'll never re-read a textbook the same way again.")

# 04 — Atkinson-Shiffrin multi-store model (horizontal flow)
def multistore(img, d):
    d.text((110, 80), "Atkinson & Shiffrin  ·  1968.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Memory has three stages, like a factory line.",
           fill=MUTED, font=font("sans", 34))

    boxes = [
        ("SENSORY",     "All sights & sounds",  "Iconic: <1 sec",  "Echoic: ~3 sec"),
        ("SHORT-TERM",  "Mental scratchpad",    "~7 ± 2 items",    "~30 sec"),
        ("LONG-TERM",   "The vault",            "Effectively",     "unlimited"),
    ]
    box_w, box_h = 500, 360
    spacing = 80
    total = 3 * box_w + 2 * spacing
    start_x = (W - total) // 2
    y = 320

    for i, (name, sub, line1, line2) in enumerate(boxes):
        x = start_x + i * (box_w + spacing)
        d.rounded_rectangle([x, y, x + box_w, y + box_h], radius=24,
                            outline=deck.accent, width=6, fill=deck.card_bg)
        d.text((x + 30, y + 30), name, fill=deck.accent, font=font("sans_bold", 44))
        d.text((x + 30, y + 100), sub, fill=MUTED, font=font("sans", 30))
        d.text((x + 30, y + 200), line1, fill=INK, font=font("sans_bold", 36))
        d.text((x + 30, y + 250), line2, fill=INK, font=font("sans_bold", 36))

        # Arrow to next box
        if i < 2:
            ax = x + box_w
            ay = y + box_h // 2
            d.line([ax + 10, ay, ax + spacing - 10, ay], fill=MAROON, width=8)
            # arrowhead
            d.polygon([
                (ax + spacing - 10, ay - 18),
                (ax + spacing - 10, ay + 18),
                (ax + spacing + 10, ay),
            ], fill=MAROON)

    # Attention/rehearsal labels under arrows
    d.text((start_x + box_w - 10, y + box_h + 30), "attention", fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((start_x + 2*box_w + spacing - 30, y + box_h + 30), "rehearsal", fill=MAROON_DARK, font=font("sans_bold", 26))

    # Bottom takeaway
    d.rounded_rectangle([110, 800, W - 110, 920], radius=22, fill=MAROON)
    centered(d, "Only what you ATTEND to moves on.  Only what you REHEARSE sticks.",
             font("sans_bold", 36), 835, deck.accent_light)
deck.custom("04_multistore", multistore)

# 05 — working memory (Baddeley)
def working_memory(img, d):
    d.text((110, 80), "Working memory  ·  Baddeley.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Short-term memory isn't just storage — it's the workspace where thinking happens.",
           fill=MUTED, font=font("sans", 28))

    # Central executive at top, two slaves below, episodic buffer to the side
    # Central executive
    d.rounded_rectangle([560, 240, 1360, 380], radius=20,
                        outline=MAROON, width=5, fill=deck.accent_light)
    centered(d, "CENTRAL EXECUTIVE", font("sans_bold", 42), 270, MAROON)
    centered(d, "the boss — directs attention, switches tasks", font("sans", 28), 330, MAROON_DARK)

    # Lines down to the three subsystems
    for x in [400, 960, 1520]:
        d.line([960, 380, x, 480], fill=deck.accent, width=4)

    subsystems = [
        (110,  470, "PHONOLOGICAL LOOP",
         "verbal & auditory",
         "the voice in your head"),
        (670,  470, "VISUOSPATIAL SKETCHPAD",
         "visual & spatial",
         "picture your bedroom layout"),
        (1230, 470, "EPISODIC BUFFER",
         "ties it all together",
         "links to long-term memory"),
    ]
    for x, y, title, sub1, sub2 in subsystems:
        d.rounded_rectangle([x, y, x + 580, y + 280], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        # Title may wrap
        title_lines = wrap(d, title, font("sans_bold", 32), 540)
        ty = y + 30
        for tl in title_lines:
            d.text((x + 30, ty), tl, fill=deck.accent, font=font("sans_bold", 32))
            ty += 40
        d.text((x + 30, y + 130), sub1, fill=INK, font=font("sans_bold", 30))
        d.text((x + 30, y + 180), sub2, fill=MUTED, font=font("sans", 28))

    d.rounded_rectangle([110, 820, W - 110, 940], radius=22, fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Working memory = where mental math, sentence-following, problem-solving live.",
             font("sans_bold", 32), 855, MAROON_DARK)
deck.custom("05_working_memory", working_memory)

# 06 — levels of processing (depth diagram)
def levels(img, d):
    d.text((110, 80), "Levels of processing.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 170), "Craik & Lockhart, 1972.  How DEEP you process = how WELL you remember.",
           fill=MUTED, font=font("sans", 30))

    # Three horizontal layers, increasing in depth (color intensity)
    layers = [
        ("SHALLOW · structural",  "What does the word LOOK like?  CAPS or lowercase?",
         "Forgotten in seconds.",                            deck.accent_light, INK),
        ("MEDIUM · phonemic",     "What does the word SOUND like?  Does it rhyme?",
         "Slightly better. Still weak.",                      deck.accent,       (255,255,255)),
        ("DEEP · semantic",       "What does the word MEAN?  How does it connect?",
         "Durable memory.  ✓",                                MAROON,            (255,255,255)),
    ]
    y = 270
    for label, prompt, result, fill_color, txt_color in layers:
        d.rounded_rectangle([110, y, W - 110, y + 180], radius=20, fill=fill_color)
        d.text((140, y + 22), label, fill=txt_color, font=font("sans_bold", 36))
        d.text((140, y + 78), prompt, fill=txt_color, font=font("sans", 32))
        d.text((140, y + 130), result, fill=txt_color, font=font("sans_bold", 30))
        y += 210

    # Self-reference effect callout
    d.rounded_rectangle([110, 900, W - 110, 990], radius=18, fill=MAROON_DARK)
    centered(d, "DEEPEST of all = self-reference.  Tie it to YOUR life.  You'll remember.",
             font("sans_bold", 34), 925, deck.accent_light)
deck.custom("06_levels", levels)

# 07 — LTM types tree (explicit/implicit branching)
def ltm_types(img, d):
    d.text((110, 80), "Types of long-term memory.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Long-term memory isn't one bucket — it splits.",
           fill=MUTED, font=font("sans", 32))

    # Root node
    root_x, root_y = 960, 240
    d.rounded_rectangle([root_x - 220, root_y, root_x + 220, root_y + 100], radius=18,
                        outline=MAROON, width=5, fill=deck.accent_light)
    centered_text = "LONG-TERM MEMORY"
    tw = d.textlength(centered_text, font=font("sans_bold", 36))
    d.text((root_x - tw/2, root_y + 30), centered_text, fill=MAROON, font=font("sans_bold", 36))

    # Two branches: explicit (left) and implicit (right)
    branches = [
        (450,  400, "EXPLICIT (declarative)",  "conscious recall · put into words", deck.accent),
        (1470, 400, "IMPLICIT (non-declarative)", "can't easily verbalize",         deck.accent),
    ]
    for bx, by, name, sub, color in branches:
        # connecting line from root
        d.line([root_x, root_y + 100, bx, by], fill=MAROON, width=4)
        d.rounded_rectangle([bx - 280, by, bx + 280, by + 130], radius=18,
                            outline=color, width=5, fill=deck.card_bg)
        title_lines = wrap(d, name, font("sans_bold", 30), 540)
        ty = by + 16
        for tl in title_lines:
            tw2 = d.textlength(tl, font=font("sans_bold", 30))
            d.text((bx - tw2/2, ty), tl, fill=color, font=font("sans_bold", 30))
            ty += 38
        sub_w = d.textlength(sub, font=font("sans", 26))
        d.text((bx - sub_w/2, by + 90), sub, fill=MUTED, font=font("sans", 26))

    # Sub-branches: 4 leaves
    leaves = [
        (200,  640, "EPISODIC",
         "your personal experiences",
         "10th birthday, first day of school"),
        (700,  640, "SEMANTIC",
         "general facts & knowledge",
         "capital of France · photosynthesis"),
        (1220, 640, "PROCEDURAL",
         "skills you can DO",
         "ride a bike · tie shoes"),
        (1720 - 240, 640, "CONDITIONED",
         "classical responses",
         "flinch at loud noise"),
    ]

    # Map first 2 to explicit (450,400 area), last 2 to implicit (1470, 400)
    parent_x = [450, 450, 1470, 1470]
    for i, (x, y, name, sub1, sub2) in enumerate(leaves):
        # connecting line from parent branch
        d.line([parent_x[i], 530, x + 200, y], fill=deck.accent, width=3)
        d.rounded_rectangle([x, y, x + 400, y + 230], radius=16,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 20, y + 18), name, fill=deck.accent, font=font("sans_bold", 32))
        # wrap sub1
        for j, ln in enumerate(wrap(d, sub1, font("sans", 26), 360)[:2]):
            d.text((x + 20, y + 80 + j * 36), ln, fill=INK, font=font("sans", 26))
        for j, ln in enumerate(wrap(d, sub2, font("sans_ital" if False else "sans", 24), 360)[:2]):
            d.text((x + 20, y + 160 + j * 32), ln, fill=MUTED, font=font("sans", 24))

    # Brain regions footnote
    d.rounded_rectangle([110, 920, W - 110, 1010], radius=18, fill=MAROON)
    centered(d, "Hippocampus = explicit.   Cerebellum & basal ganglia = procedural.",
             font("sans_bold", 32), 945, deck.accent_light)
deck.custom("07_ltm_types", ltm_types)

# 08 — pause + try (proactive vs retroactive)
deck.pause("08_pause1", "PAUSE  &  TRY",
           "You keep typing your OLD phone passcode by accident, even though you set a new one. The old one keeps blocking the new one.",
           "Proactive or retroactive interference?",
           hint="Pause. Decide. Press play.")

# 09 — pause answer (custom — proactive vs retroactive direction)
def pause_answer(img, d):
    d.text((110, 80), "PROACTIVE interference.",
           fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 180), "Old memory blocking new memory.",
           fill=MAROON_DARK, font=font("serif", 42))

    # Two side-by-side direction diagrams
    sides = [
        (110,  "PROACTIVE",
         "OLD  ─►  blocks NEW",
         "PRO = forward",
         "old code stops you typing the new code",
         deck.accent),
        (1000, "RETROACTIVE",
         "NEW  ─►  overwrites OLD",
         "RETRO = backward",
         "new French replaces your old Spanish",
         MUTED),
    ]
    for x, name, line1, line2, ex, color in sides:
        d.rounded_rectangle([x, 280, x + 810, 720], radius=22,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((x + 36, 310), name, fill=color, font=font("sans_bold", 50))
        d.text((x + 36, 400), line1, fill=INK, font=font("sans_bold", 44))
        d.text((x + 36, 480), line2, fill=color, font=font("sans_bold", 36))
        # example, wrapped
        for j, ln in enumerate(wrap(d, ex, font("sans", 30), 740)):
            d.text((x + 36, 560 + j * 42), ln, fill=MUTED, font=font("sans", 30))

    d.rounded_rectangle([110, 770, W - 110, 920], radius=22, fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Direction matters.  PRO = forward in time.  RETRO = backward.",
             font("serif_bold", 38), 800, MAROON_DARK)
    centered(d, "AP exam loves this question.  Get the direction right and you'll never miss it.",
             font("sans_bold", 30), 860, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# 10 — five reasons we forget
deck.recap("10_forgetting", "Why we forget.  Five reasons.", [
    "ENCODING FAILURE — the info never made it in.  Most everyday forgetting is this.",
    "DECAY — memory fades over time without use.  Mostly sensory & short-term.",
    "INTERFERENCE — proactive (old blocks new) or retroactive (new blocks old).",
    "RETRIEVAL FAILURE — it's there, but you can't grab it.  Tip-of-the-tongue.",
    "MOTIVATED FORGETTING — Freud: pushing painful memories away.  Less supported today.",
])

# 11 — memory errors (Loftus + reconstruction)
def memory_errors(img, d):
    d.text((110, 80), "Memory is reconstruction — not recording.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 168), "Every recall rebuilds the memory.  Every rebuild can be wrong.",
           fill=MUTED, font=font("sans", 30))

    # Loftus headline card
    d.rounded_rectangle([110, 250, W - 110, 480], radius=22,
                        outline=MAROON, width=5, fill=deck.accent_light)
    d.text((140, 280), "LOFTUS · 1974  ·  Misinformation effect",
           fill=MAROON, font=font("sans_bold", 38))
    d.text((140, 350), "\"How fast were the cars going when they SMASHED?\"  ->  higher speed estimates",
           fill=INK, font=font("sans", 30))
    d.text((140, 400), "Same video.  Different verb.  Different memory.  Even false 'broken glass'.",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # Three quick-cards
    items = [
        ("SOURCE AMNESIA",  "Remember the fact, forget where you heard it."),
        ("FALSE MEMORIES",  "Fabricated events that feel completely real."),
        ("SCHEMAS",         "Mental templates fill in gaps — with what 'should' be there."),
    ]
    for i, (name, body) in enumerate(items):
        x = 110 + i * 605
        d.rounded_rectangle([x, 530, x + 580, 760], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 560), name, fill=deck.accent, font=font("sans_bold", 32))
        for j, ln in enumerate(wrap(d, body, font("sans", 28), 530)):
            d.text((x + 24, 630 + j * 40), ln, fill=INK, font=font("sans", 28))

    d.rounded_rectangle([110, 800, W - 110, 950], radius=22, fill=MAROON)
    centered(d, "Eyewitness testimony is way less reliable than juries believe.",
             font("sans_bold", 36), 835, deck.accent_light)
    centered(d, "Don't trust your memory just because it feels vivid.",
             font("sans", 30), 890, deck.accent_light)
deck.custom("11_memory_errors", memory_errors)

# 12 — improvement strategies (the studying playbook)
def improvement(img, d):
    d.text((110, 80), "The studying playbook.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 170), "Five strategies backed by research.  Re-reading isn't on the list.",
           fill=MUTED, font=font("sans", 30))

    strategies = [
        ("CHUNKING",        "Group items into meaningful units.  Phone numbers exist for this reason."),
        ("MNEMONICS",       "ROY G BIV.  Method of loci.  Force deep, memorable processing."),
        ("SPACING EFFECT",  "Spread study across days.  Beats cramming every single time."),
        ("TESTING EFFECT",  "Quiz yourself.  Pulling info OUT > putting it back IN.  Flashcards win."),
        ("SLEEP",           "Consolidation happens overnight.  All-nighters are biochemically dumb."),
    ]
    for i, (name, body) in enumerate(strategies):
        y = 260 + i * 130
        d.rounded_rectangle([110, y, W - 110, y + 110], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        # number circle
        d.ellipse([140, y + 25, 220, y + 105], fill=deck.accent)
        num = str(i + 1)
        nw = d.textlength(num, font=font("serif_bold", 50))
        d.text((180 - nw/2, y + 35), num, fill=(255, 255, 255), font=font("serif_bold", 50))
        # title + body
        d.text((260, y + 22), name, fill=MAROON, font=font("sans_bold", 36))
        d.text((260, y + 68), body, fill=INK, font=font("sans", 28))
deck.custom("12_improvement", improvement)

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "3 stages: sensory (<1s)  ->  STM (~7±2 items, ~30s)  ->  LTM (unlimited).",
    "Working memory: phonological loop, visuospatial sketchpad, central executive, episodic buffer.",
    "Deep semantic processing > shallow visual.  Self-reference is the deepest.",
    "LTM splits: explicit (episodic + semantic)  ·  implicit (procedural + conditioned).",
    "PROACTIVE = old blocks new.  RETROACTIVE = new blocks old.  Lock the direction.",
    "Study smart: chunk, mnemonic, space, test, sleep.  Re-reading is the trap.",
])

# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",          "(done!)"),
    ("1.", "Read Myers Module 7",        "Memory — encoding · storage · retrieval + Loftus studies"),
    ("2.", "AP Classroom · 15 MCQ",      "Identifying types of memory and types of forgetting"),
    ("3.", "Assignment in dashboard",    "Test 3 vocab words with retrieval+spacing vs 3 with re-reading"),
    ("4.", "Advisor check-in",           "If proactive vs retroactive still feels fuzzy"),
], next_text="Next up:  Module 8 — Cognition & Language. How the brain solves problems, and why autocorrect is a psych experiment.")

print("AP Psych Module 7 slides built.")

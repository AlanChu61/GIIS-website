"""AP Psychology · Module 1 — History & Approaches.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Heavy on slide_kit primitives: text-driven content, no equations to render.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=1, output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 1 — History & Approaches",
           "~6 minutes  ·  Where psychology came from + the 6 lenses")

# 02 — hook (six approaches looking at one teenager)
def hook(img, d):
    d.text((110, 80), "Six psychologists.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 168), "One miserable teenager. Six explanations.",
           fill=MAROON_DARK, font=font("serif", 48))

    # Center figure (stylized phone-staring icon)
    cx, cy = 960, 560
    d.rounded_rectangle([cx-80, cy-160, cx+80, cy+120], radius=20, outline=MAROON, width=6, fill=deck.card_bg)  # phone
    d.ellipse([cx-50, cy-130, cx+50, cy-30], fill=MAROON_DARK)  # head
    d.text((cx-30, cy+30), "😞", font=font("sans", 80), fill=INK)

    # Six labels around the figure
    labels = [
        (cx - 700, cy - 200, "BIOLOGICAL",      "→ brain chemistry"),
        (cx + 220, cy - 200, "COGNITIVE",       "→ how she interprets it"),
        (cx - 700, cy - 60,  "BEHAVIORAL",      "→ learned cue + response"),
        (cx + 220, cy - 60,  "PSYCHODYNAMIC",   "→ unconscious conflict"),
        (cx - 700, cy + 80,  "HUMANISTIC",      "→ blocked from her ideals"),
        (cx + 220, cy + 80,  "SOCIOCULTURAL",   "→ shaped by her culture"),
    ]
    for lx, ly, name, sub in labels:
        d.rounded_rectangle([lx, ly, lx + 460, ly + 100], radius=14,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((lx + 20, ly + 14), name, fill=deck.accent, font=font("sans_bold", 30))
        d.text((lx + 20, ly + 56), sub, fill=INK, font=font("sans", 28))

    centered(d, "Same person.   Six lenses.   None of them wrong.",
             font("serif_bold", 38), 870, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Where psychology came from — the short version.",
    "The six modern approaches and what each one cares about.",
    "Why no single approach owns the truth.",
], footnote="By end: read a study description, name the approach.")

# 04 — origins (definition card with date highlight)
def origins(img, d):
    d.text((110, 80), "Where psychology started.", fill=MAROON, font=font("serif_bold", 70))

    # Big date callout
    d.rounded_rectangle([110, 240, W-110, 480], radius=24, fill=deck.accent_light, outline=MAROON, width=6)
    centered(d, "1879", font("serif_bold", 200), 250, MAROON)
    centered(d, "Wilhelm Wundt opens the first psychology lab", font("sans_bold", 38), 460, MAROON_DARK)

    d.text((110, 540), "Before 1879:  psychology was philosophy.",
           fill=INK, font=font("sans", 38))
    d.text((110, 600), "After 1879:  measured, timed, recorded — like a science.",
           fill=INK, font=font("sans", 38))

    d.rounded_rectangle([110, 700, W-110, 820], radius=20, fill=MAROON)
    centered(d, "1879  ·  Leipzig, Germany  ·  AP loves this date.",
             font("sans_bold", 42), 730, deck.accent_light)
deck.custom("04_origins", origins)

# 05 — early schools (compare two)
deck.compare("05_early_schools", "Two early schools.",
    {"label": "STRUCTURALISM · Titchener",
     "color": MAROON,
     "lines": [
         "What ARE the parts of",
         "consciousness?",
         "Method: introspection.",
         "",
         "Died out. Hard to verify.",
     ],
     "footnote": "Wundt's direct heir, but a dead end."},
    {"label": "FUNCTIONALISM · James",
     "color": deck.accent,
     "lines": [
         "What is the mind FOR?",
         "Why did it evolve?",
         "",
         "Lives on as modern",
         "cognitive science.",
     ],
     "footnote": "Pragmatic. Big in American psychology."})

# 06 — six approaches (one card per approach in a 3x2 grid)
def six_approaches(img, d):
    d.text((110, 70), "The six modern approaches.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "All six show up on the AP exam. Memorize.",
           fill=MUTED, font=font("sans", 32))

    approaches = [
        ("BIOLOGICAL",     "the mind is the brain — neurons, hormones, genes"),
        ("COGNITIVE",      "information processing — encode · store · retrieve"),
        ("BEHAVIORAL",     "skip the inside — watch behavior — stimulus & response"),
        ("PSYCHODYNAMIC",  "Freud's descendants — unconscious motives, childhood"),
        ("HUMANISTIC",     "people want to grow — Maslow, Rogers, self-actualization"),
        ("SOCIOCULTURAL",  "culture and context — same person, different rooms"),
    ]
    cw, ch = 580, 220
    for i, (name, desc) in enumerate(approaches):
        col = i % 3
        row = i // 3
        x = 110 + col * (cw + 20)
        y = 240 + row * (ch + 20)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, y + 22), name, fill=deck.accent, font=font("sans_bold", 36))
        # word-wrap the description
        from slide_kit import wrap as wrap_text
        lines = wrap_text(d, desc, font("sans", 28), cw - 48)
        for j, ln in enumerate(lines[:5]):
            d.text((x + 24, y + 80 + j * 38), ln, fill=INK, font=font("sans", 28))
deck.custom("06_six_approaches", six_approaches)

# 07 — same fear, six explanations (compare-style detail)
def compare1(img, d):
    d.text((110, 80), "Same fear.  Six explanations.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 170), "Someone is afraid of dogs. What would each approach say?",
           fill=MUTED, font=font("sans", 32))

    items = [
        ("Biological",      "overactive amygdala  ·  anxious genetics"),
        ("Cognitive",       "she's catastrophizing — expecting an attack"),
        ("Behavioral",      "she was bitten — classical conditioning did the rest"),
        ("Psychodynamic",   "the dog represents an unconscious childhood threat"),
        ("Humanistic",      "fear is blocking her from being her full self"),
        ("Sociocultural",   "her culture treats dogs as unclean"),
    ]
    for i, (name, expl) in enumerate(items):
        y = 270 + i * 100
        d.rounded_rectangle([110, y, W-110, y + 80], radius=14,
                            outline=deck.accent, width=2, fill=deck.card_bg)
        d.text((140, y + 20), name, fill=deck.accent, font=font("sans_bold", 36))
        d.text((480, y + 20), expl, fill=INK, font=font("sans", 32))

    d.rounded_rectangle([110, 880, W-110, 970], radius=18, fill=deck.accent_light)
    centered(d, "Six explanations. None complete on its own.",
             font("serif_bold", 38), 905, MAROON_DARK)
deck.custom("07_compare1", compare1)

# 08 — pause + try
deck.pause("08_pause1", "PAUSE  &  TRY",
           "A researcher puts students in a lavender room or a sterile white room, then measures stress with a saliva (cortisol) test.",
           "Which approach is this?",
           hint="Pause. Decide. Press play.")

# 09 — pause answer (custom — show two answers, both right)
def pause_answer(img, d):
    d.text((110, 80), "The answer:  it's actually both.",
           fill=MAROON, font=font("serif_bold", 70))

    # Two columns
    for i, (title, body) in enumerate([
        ("BIOLOGICAL",  "The cortisol test — measuring hormone — is biological."),
        ("SOCIOCULTURAL", "The room (lavender vs. sterile) — environment shaping behavior — is sociocultural."),
    ]):
        x = 110 + i * 870
        d.rounded_rectangle([x, 250, x + 760, 540], radius=24, outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 280), title, fill=deck.accent, font=font("sans_bold", 44))
        from slide_kit import wrap as wrap_text
        lines = wrap_text(d, body, font("sans", 32), 700)
        for j, ln in enumerate(lines):
            d.text((x + 30, 360 + j * 46), ln, fill=INK, font=font("sans", 32))

    d.rounded_rectangle([110, 620, W-110, 880], radius=24, fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "BIOPSYCHOSOCIAL  =  combine all three lenses.",
             font("serif_bold", 56), 660, MAROON_DARK)
    centered(d, "Most modern researchers don't pick one approach.",
             font("sans", 36), 750, MAROON_DARK)
    centered(d, "They use whichever lens answers the question.",
             font("sans_bold", 36), 800, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# 10 — modern shifts
deck.recap("10_modern", "Two waves that shaped modern psych.", [
    "1950s — Cognitive revolution. The 'inside of the mind' came back after decades of strict behaviorism.",
    "Late 1990s — Positive psychology (Seligman). Don't just study disorders — study what makes people flourish.",
    "Both still shaping research today.",
])

# 11 — real world
def real_world(img, d):
    d.text((110, 80), "Where you've already seen this.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 180), "Two headlines you'll see this week:", fill=MUTED, font=font("sans", 36))

    # Two newspaper-style cards
    for i, (title, sub) in enumerate([
        ("'Depression is genetic.'", "biological approach"),
        ("'Depression is caused by social media.'", "sociocultural approach"),
    ]):
        y = 280 + i * 200
        d.rounded_rectangle([110, y, W-110, y + 160], radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        d.text((140, y + 25), title, fill=INK, font=font("serif_bold", 44))
        d.text((140, y + 95), sub, fill=deck.accent, font=font("sans", 32))

    d.rounded_rectangle([110, 740, W-110, 920], radius=20, fill=deck.accent_light)
    centered(d, "These aren't contradictions.", font("serif_bold", 44), 770, MAROON_DARK)
    centered(d, "They're two approaches answering different questions.",
             font("sans_bold", 36), 830, MAROON_DARK)
    centered(d, "The honest answer is usually:  both.",
             font("sans_bold", 36), 880, MAROON_DARK)
deck.custom("11_real_world", real_world)

# 12 — recap
deck.recap("12_recap", "Recap.", [
    "Pre-1879 = philosophy. 1879 = Wundt's lab = science.",
    "Early schools: Structuralism (Titchener), Functionalism (James).",
    "Six modern approaches: biological, cognitive, behavioral, psychodynamic, humanistic, sociocultural.",
    "Biopsychosocial = combine them. AP loves this term.",
    "Modern shifts: cognitive revolution (1950s), positive psychology (late 1990s).",
])

# 13 — path
deck.path("13_path", [
    ("✓",  "Watch this lesson",         "(done!)"),
    ("1.", "Read Myers Module 1",       "History and approaches"),
    ("2.", "AP Classroom · 10 MCQ",     "Identify the approach from a study description"),
    ("3.", "Assignment in dashboard",    "Label 3 study descriptions with the matching approach"),
    ("4.", "One-page approaches chart",  "Make it. Tape it where you'll see it."),
], next_text="Next up:  Module 2 — Research Methods. We get strict about what counts as evidence.")

print("AP Psych Module 1 slides built.")

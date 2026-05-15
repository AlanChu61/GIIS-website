"""AP Psychology · Module 8 — Cognition & Language.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Heavy on slide_kit primitives, with custom slides for:
  - heuristics card-row (algorithm vs heuristic)
  - biases gallery (availability vs representativeness vs confirmation, etc.)
  - language development timeline (4mo -> 6mo -> 12mo -> 24mo -> 4yr)
  - pause-answer (availability vs representativeness, side-by-side)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=8, output_dir="slides", logo_path=LOGO)


# ── 01 — title ────────────────────────────────────────────────────────
deck.title("01_title", "AP Psychology",
           "Module 8 — Cognition & Language",
           "~9 minutes  ·  How thinking works, where it breaks, how language gets built")


# ── 02 — hook (plane crash / availability) ────────────────────────────
def hook(img, d):
    d.text((110, 80), "You saw a plane crash on the news.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Now flying feels scary.  Driving feels safe.",
           fill=MAROON_DARK, font=font("serif", 44))

    # Two side-by-side stat cards
    cards = [
        (110, "FLYING", "1 in ~11 million", "fatal-crash odds per flight", deck.accent),
        (985, "DRIVING", "1 in ~5,000", "fatal-crash odds per year of driving", MAROON),
    ]
    for x, label, big, sub, col in cards:
        d.rounded_rectangle([x, 320, x + 825, 640], radius=24,
                            outline=col, width=6, fill=deck.card_bg)
        d.text((x + 36, 350), label, fill=col, font=font("sans_bold", 44))
        centered_x = x + 825 // 2
        bw = d.textlength(big, font=font("serif_bold", 88))
        d.text((centered_x - bw / 2, 420), big, fill=INK, font=font("serif_bold", 88))
        sw = d.textlength(sub, font=font("sans", 30))
        d.text((centered_x - sw / 2, 560), sub, fill=MUTED, font=font("sans", 30))

    # Verdict bar
    d.rounded_rectangle([110, 700, W - 110, 800], radius=20, fill=MAROON)
    centered(d, "Driving is ~100× more dangerous.  Why doesn't it feel that way?",
             font("serif_bold", 38), 728, deck.accent_light)

    centered(d, "Because your brain runs a shortcut, not the math.",
             font("sans_bold", 40), 850, MAROON_DARK)
    centered(d, "It's called the AVAILABILITY HEURISTIC.  Today we open the box.",
             font("sans", 34), 910, INK)
deck.custom("02_hook", hook)


# ── 03 — overview ─────────────────────────────────────────────────────
deck.overview("03_overview", "Game plan.", [
    "How your brain stores categories (prototypes & exemplars).",
    "How you solve problems — the shortcuts and the biases.",
    "Language: the stack, how kids learn it, and does it shape thought?",
], footnote="By end: spot a heuristic in the wild and name it.")


# ── 04 — concepts (prototypes vs exemplars) ───────────────────────────
def concepts(img, d):
    d.text((110, 80), "Concepts compress experience.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 170), "We don't store every dog we've met. We compress two ways:",
           fill=MUTED, font=font("sans", 32))

    # Two columns
    for i, (label, body) in enumerate([
        ("PROTOTYPE",
         "The most TYPICAL example of a category.\n\n"
         "Say 'bird' → you think robin or sparrow,\nnot penguin.\n\n"
         "Fast: does this match my mental average?"),
        ("EXEMPLAR",
         "Specific past examples you've actually met.\n\n"
         "Your friend's beagle is an exemplar of 'dog.'\n\n"
         "Richer: does this remind me of any\nspecific dog I've seen?"),
    ]):
        x = 110 + i * 870
        d.rounded_rectangle([x, 270, x + 760, 760], radius=24,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 300), label, fill=deck.accent, font=font("sans_bold", 44))
        # word-wrap each paragraph block
        y = 380
        for para in body.split("\n"):
            if not para.strip():
                y += 20
                continue
            for ln in wrap(d, para, font("sans", 30), 700):
                d.text((x + 30, y), ln, fill=INK, font=font("sans", 30))
                y += 42

    d.rounded_rectangle([110, 800, W - 110, 920], radius=20, fill=deck.accent_light)
    centered(d, "Both run at the same time.  Categories let you act in real time.",
             font("serif_bold", 38), 833, MAROON_DARK)
deck.custom("04_concepts", concepts)


# ── 05 — problem solving (algorithm vs heuristic) ─────────────────────
deck.compare("05_problem_solving", "Two ways to solve a problem.",
    {"label": "ALGORITHM",
     "color": MAROON,
     "lines": [
         "Step-by-step rule.",
         "Guaranteed to find the answer.",
         "Slow.  Expensive.",
         "",
         "Long division.",
         "Trying every password 0000–9999.",
     ],
     "footnote": "Always works.  Almost never used in daily life."},
    {"label": "HEURISTIC",
     "color": deck.accent,
     "lines": [
         "Mental shortcut.",
         "Fast — often right, sometimes wrong.",
         "Cheap.  Default mode.",
         "",
         "Lost your keys?  Check the 3",
         "places you usually leave them.",
     ],
     "footnote": "Trade accuracy for speed.  This is where biases live."})


# ── 06 — heuristics card-row (availability vs representativeness) ─────
def heuristics(img, d):
    d.text((110, 80), "The two heuristics AP loves.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "They look identical until you look closely. This is the trap.",
           fill=MUTED, font=font("sans", 32))

    items = [
        ("AVAILABILITY",
         "Judge likelihood by how EASILY\nexamples come to mind.",
         "Plane crash on the news →\nflying feels dangerous.\n\nShark attack headline →\nyou avoid the ocean.",
         "Trigger word:  vivid · recent · easy to recall"),
        ("REPRESENTATIVENESS",
         "Judge by how well something\nMATCHES your mental prototype.",
         "Quiet guy reading a book →\n'librarian,' not 'farmer.'\n\n(There are way more farmers\nthan librarians.)",
         "Trigger word:  matches a stereotype / prototype"),
    ]
    for i, (label, defn, ex, trigger) in enumerate(items):
        x = 110 + i * 870
        d.rounded_rectangle([x, 240, x + 760, 880], radius=24,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 270), label, fill=deck.accent, font=font("sans_bold", 42))

        # definition
        y = 350
        for ln in defn.split("\n"):
            d.text((x + 30, y), ln, fill=INK, font=font("sans_bold", 30))
            y += 42

        # example block
        d.rounded_rectangle([x + 30, 470, x + 730, 720], radius=14,
                            fill=deck.accent_light)
        y = 490
        for ln in ex.split("\n"):
            if not ln.strip():
                y += 16
                continue
            d.text((x + 50, y), ln, fill=INK, font=font("sans", 26))
            y += 36

        # trigger pill
        d.rounded_rectangle([x + 30, 760, x + 730, 840], radius=14,
                            fill=MAROON)
        for ln in wrap(d, trigger, font("sans_bold", 24), 660):
            d.text((x + 50, 780), ln, fill=deck.accent_light,
                   font=font("sans_bold", 24))
            break  # one line is enough for these
deck.custom("06_heuristics", heuristics)


# ── 07 — biases gallery ───────────────────────────────────────────────
def biases(img, d):
    d.text((110, 80), "Bias gallery.",
           fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 178), "Systematic ways thinking goes wrong (plus one way it goes right).",
           fill=MUTED, font=font("sans", 30))

    biases_list = [
        ("CONFIRMATION BIAS",
         "Seek evidence that confirms what you already believe; ignore what doesn't."),
        ("BELIEF PERSEVERANCE",
         "Cling to a belief even after the original evidence has been debunked."),
        ("FRAMING EFFECT",
         "Wording changes your decision.  '90% fat-free' beats '10% fat.'"),
        ("FUNCTIONAL FIXEDNESS",
         "Only see an object's normal use.  Can't see the wrench as a hammer."),
        ("MENTAL SET",
         "Stuck on a strategy that worked before, even when a new one would work better."),
        ("INSIGHT  (the good one)",
         "The 'aha' moment.  Not trial-and-error — the answer just clicks all at once."),
    ]

    cw, ch = 880, 200
    for i, (name, desc) in enumerate(biases_list):
        col = i % 2
        row = i // 2
        x = 110 + col * (cw + 20)
        y = 250 + row * (ch + 20)
        # last one (insight) — paint with accent fill so it stands out as positive
        is_insight = name.startswith("INSIGHT")
        outline = deck.accent if is_insight else MAROON
        fill = deck.accent_light if is_insight else deck.card_bg
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=18,
                            outline=outline, width=4, fill=fill)
        d.text((x + 24, y + 22), name,
               fill=outline, font=font("sans_bold", 32))
        for j, ln in enumerate(wrap(d, desc, font("sans", 28), cw - 48)):
            d.text((x + 24, y + 80 + j * 38), ln, fill=INK, font=font("sans", 28))
deck.custom("07_biases", biases)


# ── 08 — pause + try ──────────────────────────────────────────────────
def pause1(img, d):
    d.rectangle([0, 80, W, 220], fill=deck.accent)
    centered(d, "PAUSE  &  TRY", font("serif_bold", 96), 100, MAROON_DARK)

    d.text((110, 270), "Two scenarios.  Which is which?",
           fill=INK, font=font("sans_bold", 42))

    # Scenario A
    d.rounded_rectangle([110, 360, W - 110, 540], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((140, 380), "A.", fill=deck.accent, font=font("serif_bold", 44))
    body_a = ("You read 3 news articles about lottery winners.  Suddenly buying a "
              "ticket feels like a real shot.")
    for j, ln in enumerate(wrap(d, body_a, font("sans", 32), W - 360)):
        d.text((220, 380 + j * 44), ln, fill=INK, font=font("sans", 32))

    # Scenario B
    d.rounded_rectangle([110, 580, W - 110, 760], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((140, 600), "B.", fill=deck.accent, font=font("serif_bold", 44))
    body_b = ("Person on the train: glasses, thick book.  You assume 'professor' "
              "even though they could just as easily be an electrician on lunch.")
    for j, ln in enumerate(wrap(d, body_b, font("sans", 32), W - 360)):
        d.text((220, 600 + j * 44), ln, fill=INK, font=font("sans", 32))

    d.text((110, 820), "Availability heuristic or representativeness heuristic?",
           fill=MAROON_DARK, font=font("sans_bold", 38))
    d.text((110, 900), "Pause. Decide. Press play.",
           fill=MUTED, font=font("sans", 36))
deck.custom("08_pause1", pause1)


# ── 09 — pause answer (custom — both heuristics, side-by-side) ────────
def pause_answer(img, d):
    d.text((110, 70), "The answer.",
           fill=MAROON, font=font("serif_bold", 70))

    panels = [
        ("A → AVAILABILITY",
         "The vivid recent articles\nmade winning feel common.",
         "Brain checked: how easily can\nI recall examples?  Easy.",
         "Actual odds: ~1 in 300,000,000."),
        ("B → REPRESENTATIVENESS",
         "Glasses + book matched your\nprototype of 'professor.'",
         "Brain checked: does this\nmatch the stereotype?  Yes.",
         "Ignored the base rate (way\nmore electricians)."),
    ]
    for i, (label, l1, l2, l3) in enumerate(panels):
        x = 110 + i * 870
        d.rounded_rectangle([x, 200, x + 760, 720], radius=24,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 230), label, fill=deck.accent, font=font("sans_bold", 38))

        y = 320
        for block in (l1, l2, l3):
            for ln in block.split("\n"):
                d.text((x + 30, y), ln, fill=INK, font=font("sans", 28))
                y += 38
            y += 14

    # Shortcut box at the bottom
    d.rounded_rectangle([110, 760, W - 110, 950], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Tell them apart:",
             font("serif_bold", 40), 780, MAROON_DARK)
    centered(d, "Availability  =  ease of recall  (vivid · recent)",
             font("sans_bold", 36), 840, MAROON_DARK)
    centered(d, "Representativeness  =  match to a prototype  (stereotype)",
             font("sans_bold", 36), 890, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)


# ── 10 — language structure (phonemes → morphemes → grammar) ──────────
def language_structure(img, d):
    d.text((110, 80), "Language has a stack.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 178), "Smallest pieces at the bottom.  Meaning emerges as you go up.",
           fill=MUTED, font=font("sans", 32))

    # Three layers, stacked top-down
    layers = [
        ("GRAMMAR",
         "Syntax (word order)  +  Semantics (meaning)",
         "'The dog bit the man.'  ≠  'The man bit the dog.'"),
        ("MORPHEMES",
         "Smallest units of MEANING",
         "cats = cat + s   ·   unhappiness = un + happy + ness"),
        ("PHONEMES",
         "Smallest units of SOUND  (~44 in English)",
         "the 'b' in 'bat' is one phoneme"),
    ]
    for i, (label, defn, ex) in enumerate(layers):
        y = 280 + i * 200
        d.rounded_rectangle([110, y, W - 110, y + 170], radius=20,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((150, y + 18), label, fill=deck.accent, font=font("sans_bold", 40))
        d.text((150, y + 70), defn, fill=INK, font=font("sans_bold", 30))
        d.text((150, y + 115), ex, fill=MUTED, font=font("sans", 28))

    # Footnote
    d.rounded_rectangle([110, 900, W - 110, 990], radius=18, fill=deck.accent_light)
    centered(d, "Phonemes → morphemes → grammar.  Memorize the stack.",
             font("serif_bold", 36), 925, MAROON_DARK)
deck.custom("10_language_structure", language_structure)


# ── 11 — language development timeline (4mo → 4yr) ────────────────────
def language_development(img, d):
    d.text((110, 80), "How kids actually learn language.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 168), "Predictable stages — set your watch by them.",
           fill=MUTED, font=font("sans", 32))

    # Horizontal timeline
    track_y = 460
    track_x0, track_x1 = 180, W - 180
    d.line([(track_x0, track_y), (track_x1, track_y)], fill=deck.accent, width=8)

    stages = [
        (0.00, "4–6 mo",  "BABBLING",         "Every sound on Earth.\n'ba-ba,' 'ga-ga,' clicks."),
        (0.25, "12 mo",   "ONE-WORD",         "'Mama.' 'Dog.' 'No.'\nOne word = whole sentence."),
        (0.55, "24 mo",   "TELEGRAPHIC",      "Two-word combos.\n'Want cookie.' 'Daddy go.'"),
        (0.85, "3–4 yr",  "GRAMMATICAL",      "Full sentences.\nSyntax, plurals, past tense."),
        (1.00, "5+ yr",   "FLUENT",           "The whole machine\nis online."),
    ]
    for frac, age, label, body in stages:
        x = int(track_x0 + frac * (track_x1 - track_x0))
        # node
        d.ellipse([x - 22, track_y - 22, x + 22, track_y + 22],
                  fill=MAROON, outline=deck.accent_light, width=4)

        # age label above
        aw = d.textlength(age, font=font("sans_bold", 32))
        d.text((x - aw / 2, track_y - 90), age, fill=MAROON_DARK,
               font=font("sans_bold", 32))

        # stage label below
        lw = d.textlength(label, font=font("sans_bold", 30))
        d.text((x - lw / 2, track_y + 50), label, fill=deck.accent,
               font=font("sans_bold", 30))

        # body lines under
        for j, ln in enumerate(body.split("\n")):
            ln_w = d.textlength(ln, font=font("sans", 22))
            d.text((x - ln_w / 2, track_y + 100 + j * 32),
                   ln, fill=INK, font=font("sans", 22))

    # Big debate bar at the bottom
    d.rounded_rectangle([110, 740, W - 110, 990], radius=20,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((140, 758), "But how do they pull it off?",
           fill=MAROON, font=font("serif_bold", 32))
    d.text((140, 818), "SKINNER:  reinforcement — praise & correct, child shapes speech.",
           fill=INK, font=font("sans", 24))
    d.text((140, 864), "CHOMSKY:  innate Language Acquisition Device (LAD) wired for grammar.",
           fill=INK, font=font("sans", 24))
    d.text((140, 930), "Modern view:  nature + nurture — built-in readiness PLUS exposure.",
           fill=deck.accent, font=font("sans_bold", 24))
deck.custom("11_language_development", language_development)


# ── 12 — Whorf (linguistic relativity) ────────────────────────────────
def whorf(img, d):
    d.text((110, 80), "Does language SHAPE thought?",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 178), "Whorf's linguistic relativity hypothesis (1940s).",
           fill=MUTED, font=font("sans", 32))

    # Strong vs modern view
    panels = [
        ("STRONG VERSION  ✗",
         MAROON,
         "Language DETERMINES thought.\n\n"
         "If your language has no word\nfor it, you can't think it.\n\n"
         "Mostly debunked by modern\nresearch."),
        ("MODERN VIEW  ✓",
         deck.accent,
         "Language INFLUENCES thought.\n\n"
         "Grammatical gender shifts how\nspeakers describe objects.\n\n"
         "Bilinguals feel different in\ndifferent languages."),
    ]
    for i, (label, col, body) in enumerate(panels):
        x = 110 + i * 870
        d.rounded_rectangle([x, 280, x + 760, 760], radius=24,
                            outline=col, width=5, fill=deck.card_bg)
        d.text((x + 30, 310), label, fill=col, font=font("sans_bold", 42))
        y = 400
        for ln in body.split("\n"):
            if not ln.strip():
                y += 18
                continue
            d.text((x + 30, y), ln, fill=INK, font=font("sans", 30))
            y += 42

    d.rounded_rectangle([110, 800, W - 110, 950], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "AP nuance:  language is an INFLUENCE, not a cage.",
             font("serif_bold", 42), 840, MAROON_DARK)
    centered(d, "It shapes thought — it doesn't lock you in.",
             font("sans_bold", 32), 900, MAROON_DARK)
deck.custom("12_whorf", whorf)


# ── 13 — recap ────────────────────────────────────────────────────────
deck.recap("13_recap", "Recap.", [
    "Concepts compress experience: prototypes (typical) + exemplars (specific).",
    "Algorithms guarantee but slow.  Heuristics are fast shortcuts.",
    "Availability = ease of recall.  Representativeness = match to a prototype.",
    "Biases: confirmation, belief perseverance, framing, functional fixedness, mental set.",
    "Language stack: phonemes → morphemes → grammar (syntax + semantics).",
    "Stages: babbling (4–6mo) → one-word (12mo) → telegraphic (24mo) → grammatical (4yr).",
    "Chomsky's LAD vs. Skinner's reinforcement.  Whorf: language influences thought.",
])


# ── 14 — path ─────────────────────────────────────────────────────────
deck.path("14_path", [
    ("✓",  "Watch this lesson",          "(done!)"),
    ("1.", "Read Myers Module 8",         "Cognition & language — focus on availability vs. representativeness"),
    ("2.", "AP Classroom · 15 MCQ",       "Identify heuristics & biases from real-life scenarios"),
    ("3.", "Assignment in dashboard",     "Label 10 scenarios: availability, representativeness, confirmation, framing, functional fixedness"),
    ("4.", "Advisor check-in",            "Book a session if availability vs. representativeness still feels fuzzy"),
], next_text="Next up:  Module 9 — Motivation & Emotion. Why you'll all-nighter a video game but not a 5-page paper.")

print("AP Psych Module 8 slides built.")

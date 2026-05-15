"""AP Psychology · Module 5 — States of Consciousness.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Sleep stages, dreams, hypnosis, psychoactive drugs.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)
from slide_kit import wrap as wrap_text

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=5, output_dir="slides", logo_path=LOGO)


# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 5 — States of Consciousness",
           "~7 minutes  ·  Sleep, dreams, hypnosis & drugs")


# 02 — hook (the all-nighter)
def hook(img, d):
    d.text((110, 80), "You pulled an all-nighter.", fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 168), "Why does the next morning feel broken?",
           fill=MAROON_DARK, font=font("serif", 44))

    # Three "next-morning" symptom cards
    symptoms = [
        ("Can't focus.",          "→ memory not consolidated"),
        ("Jokes don't land.",     "→ mood regulation off"),
        ("Re-read same paragraph.", "→ working memory dragging"),
        ("Crying over a sandwich.", "→ amygdala unfiltered"),
    ]
    cw, ch = 820, 130
    for i, (sym, why) in enumerate(symptoms):
        col = i % 2
        row = i // 2
        x = 110 + col * (cw + 60)
        y = 290 + row * (ch + 30)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 28, y + 18), sym, fill=INK, font=font("serif_bold", 42))
        d.text((x + 28, y + 76), why, fill=deck.accent, font=font("sans", 30))

    d.rounded_rectangle([110, 620, W - 110, 880], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "You skipped the brain's nightly maintenance cycle.",
             font("serif_bold", 46), 660, MAROON_DARK)
    centered(d, "Memory consolidation. Mood regulation. Cellular cleanup.",
             font("sans", 36), 740, MAROON_DARK)
    centered(d, "Once you know the stages, the fog makes sense.",
             font("sans_bold", 36), 800, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Levels of awareness — conscious, preconscious, unconscious.",
    "Sleep stages — NREM 1·2·3 → REM, and the 90-minute cycle.",
    "Dreams & hypnosis — competing theories AP loves to compare.",
    "Psychoactive drugs — agonist vs. antagonist + three categories.",
], footnote="By end: name the stage, the theory, the drug type.")


# 04 — awareness levels (definition + layered card)
def awareness(img, d):
    d.text((110, 80), "Levels of awareness.", fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 170), "From spotlight on  →  spotlight off.",
           fill=MUTED, font=font("sans", 34))

    # Stacked layers — top is most aware, bottom is least
    layers = [
        ("CONSCIOUS",      "What you're aware of right now — these words, this room.",         deck.accent),
        ("PRECONSCIOUS",   "Not active, but easy to pull up. (What did you eat yesterday?)",   deck.accent),
        ("UNCONSCIOUS",    "Freud — hidden drives & repressed memories shaping behavior.",     MAROON),
        ("NONCONSCIOUS",   "Background processes — heart rate, breathing, balance.",           MAROON),
        ("AUTOMATIC",      "Used-to-be-conscious actions now on autopilot — driving home.",    MAROON_DARK),
    ]
    for i, (name, desc, color) in enumerate(layers):
        y = 250 + i * 130
        d.rounded_rectangle([110, y, W - 110, y + 110], radius=16,
                            outline=color, width=4, fill=deck.card_bg)
        d.text((140, y + 18), name, fill=color, font=font("sans_bold", 38))
        d.text((140, y + 64), desc, fill=INK, font=font("sans", 30))
deck.custom("04_awareness_levels", awareness)


# 05 — sleep cycle hypnogram (custom — descending NREM stages then REM emerging)
def sleep_cycle(img, d):
    d.text((110, 70), "The 90-minute sleep cycle.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "NREM goes deep early; REM lengthens toward morning.",
           fill=MUTED, font=font("sans", 30))

    # Hypnogram axes
    chart_x0, chart_y0 = 180, 280
    chart_x1, chart_y1 = W - 110, 760
    # Y rows for stages (top = awake, bottom = NREM3)
    rows = [
        ("Awake",   chart_y0 + 0),
        ("REM",     chart_y0 + 80),
        ("NREM 1",  chart_y0 + 160),
        ("NREM 2",  chart_y0 + 240),
        ("NREM 3",  chart_y0 + 360),
    ]
    # Draw row labels and gridlines
    f_lab = font("sans_bold", 26)
    for label, y in rows:
        d.text((40, y - 14), label, fill=MAROON_DARK, font=f_lab)
        d.line([(chart_x0, y), (chart_x1, y)], fill=(220, 210, 230), width=2)
    # X axis labels (4 cycles)
    f_x = font("sans", 24)
    cycle_w = (chart_x1 - chart_x0) // 4
    for i in range(5):
        x = chart_x0 + i * cycle_w
        d.line([(x, chart_y0), (x, chart_y1 - 40)], fill=(220, 210, 230), width=2)
        if i < 4:
            d.text((x + cycle_w // 2 - 40, chart_y1 - 20),
                   f"Cycle {i+1}", fill=MUTED, font=f_x)

    # Hypnogram trace — descend through NREM 1→2→3, climb back, REM
    # Each cycle: down to deep, REM gets longer each cycle.
    trace = []
    awake_y, rem_y, n1_y, n2_y, n3_y = (rows[0][1], rows[1][1], rows[2][1], rows[3][1], rows[4][1])
    # Cycle pattern (relative x within cycle, y)
    # cycle 1: deep N3, short REM. cycle 4: barely N2, long REM.
    cycle_specs = [
        # (n1_w, n2_w, n3_w, climb_w, rem_w) — proportional widths summing to ~cycle_w
        (0.10, 0.18, 0.35, 0.27, 0.10),
        (0.10, 0.20, 0.25, 0.25, 0.20),
        (0.10, 0.30, 0.10, 0.20, 0.30),
        (0.10, 0.30, 0.05, 0.15, 0.40),
    ]
    cur_x = chart_x0
    trace.append((cur_x, awake_y))
    for spec in cycle_specs:
        n1_w, n2_w, n3_w, climb_w, rem_w = [w * cycle_w for w in spec]
        # descend N1
        cur_x += n1_w; trace.append((cur_x, n1_y))
        # N2
        cur_x += n2_w; trace.append((cur_x, n2_y))
        # N3 (deep) — only if non-zero
        if n3_w > 5:
            cur_x += n3_w; trace.append((cur_x, n3_y))
        # climb back up
        cur_x += climb_w; trace.append((cur_x, n2_y))
        # REM segment
        cur_x += rem_w; trace.append((cur_x, rem_y))
    # End — brief rise toward awake
    trace.append((chart_x1, awake_y))
    # Draw the trace
    for i in range(len(trace) - 1):
        d.line([trace[i], trace[i + 1]], fill=MAROON, width=5)

    # Highlight REM segments with accent stripe at top (rem_y row)
    # Re-walk to mark REM segments
    cur_x2 = chart_x0
    cur_x2 += 0  # start
    seg_x = chart_x0
    for spec in cycle_specs:
        n1_w, n2_w, n3_w, climb_w, rem_w = [w * cycle_w for w in spec]
        seg_x += n1_w + n2_w + (n3_w if n3_w > 5 else 0) + climb_w
        # REM band
        d.rectangle([seg_x, rem_y - 10, seg_x + rem_w, rem_y + 10],
                    fill=deck.accent_light)
        seg_x += rem_w

    # Caption box
    d.rounded_rectangle([110, 820, W - 110, 970], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    centered(d, "Deep NREM dominates early.   REM dominates later.",
             font("serif_bold", 38), 845, MAROON_DARK)
    centered(d, "That's why your wildest dreams come right before you wake.",
             font("sans", 32), 905, INK)
deck.custom("05_sleep_cycle", sleep_cycle)


# 06 — three sleep theories (recap-style list)
deck.recap("06_sleep_theories", "Why do we sleep?  Three theories.", [
    "Restorative — sleep repairs the body and brain.  Fits deep NREM.",
    "Consolidation (memory) — sleep moves info to long-term storage.  Fits REM.",
    "Evolutionary — being still + quiet at night kept us safe from predators.",
    "Reality:  it's all three at once.  AP wants you to name all three.",
])


# 07 — sleep disorders (compare NREM vs REM disorders cleanly)
deck.compare("07_sleep_disorders", "Sleep disorders — five to know.",
    {"label": "NREM-side disorders",
     "color": MAROON,
     "lines": [
         "Insomnia — chronic trouble",
         "falling or staying asleep.",
         "",
         "Sleep apnea — breathing",
         "stops; never reaches deep sleep.",
         "",
         "Somnambulism — sleepwalking,",
         "happens in NREM 3.",
     ],
     "footnote": "Sleepwalkers aren't acting out dreams."},
    {"label": "REM-side disorders",
     "color": deck.accent,
     "lines": [
         "Narcolepsy — sudden sleep",
         "attacks, often straight into REM.",
         "",
         "REM sleep behavior disorder —",
         "paralysis fails, person acts",
         "out vivid dreams.",
         "",
         "Often dangerous to bed partners.",
     ],
     "footnote": "AP trap: somnambulism = NREM, dream-acting = REM."})


# 08 — pause + try
deck.pause("08_pause1", "PAUSE  &  TRY",
           "(1) During which stage does the brain look most awake on EEG, and why is the body paralyzed?",
           "(2) Sleepwalking happens in which stage?",
           hint="Pause. Decide. Press play.")


# 09 — pause answer (custom — two-column reveal)
def pause_answer(img, d):
    d.text((110, 70), "The answers.", fill=MAROON, font=font("serif_bold", 72))

    # Q1
    d.rounded_rectangle([110, 200, W - 110, 530], radius=24,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((140, 220), "Q1 — REM (paradoxical sleep).", fill=deck.accent,
           font=font("sans_bold", 42))
    lines1 = [
        "EEG looks awake — that's the paradox.",
        "Brainstem locks voluntary muscles so you don't",
        "kick, swing, or run during a vivid dream.",
    ]
    for i, ln in enumerate(lines1):
        d.text((140, 290 + i * 56), ln, fill=INK, font=font("sans", 32))

    # Q2
    d.rounded_rectangle([110, 560, W - 110, 870], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((140, 580), "Q2 — NREM 3 (deep slow-wave sleep).", fill=MAROON,
           font=font("sans_bold", 42))
    lines2 = [
        "Surprises people — dreams happen in REM,",
        "but in REM the body is paralyzed.",
        "Sleepwalkers are partially awake during deep,",
        "non-dream sleep. Different stage, different mechanism.",
    ]
    for i, ln in enumerate(lines2):
        d.text((140, 650 + i * 50), ln, fill=INK, font=font("sans", 30))
deck.custom("09_pause1_answer", pause_answer)


# 10 — dreams (three-theory compare done as custom 3-col)
def dreams(img, d):
    d.text((110, 70), "Dreams — three theories.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "AP loves a side-by-side compare. Here you go.",
           fill=MUTED, font=font("sans", 30))

    cards = [
        ("FREUD",
         "Psychoanalytic",
         ["Manifest content =",
          "what literally happened.",
          "",
          "Latent content =",
          "hidden symbolic meaning.",
          "",
          "Largely abandoned in",
          "research; still cultural."],
         MAROON),
        ("HOBSON",
         "Activation-Synthesis",
         ["Brainstem fires random",
          "neural signals during REM.",
          "",
          "Cortex weaves a story.",
          "",
          "The story isn't meaningful —",
          "the brain just hates",
          "randomness."],
         deck.accent),
        ("INFO-PROCESSING",
         "Memory consolidation",
         ["Dreams = brain sorting",
          "the day's memories.",
          "",
          "Big test tomorrow?",
          "Probably going to dream",
          "about it.",
          "",
          "Modern + research-backed."],
         MAROON_DARK),
    ]
    cw = 580
    for i, (name, sub, lines, color) in enumerate(cards):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 230, x + cw, 920], radius=20,
                            outline=color, width=4, fill=deck.card_bg)
        d.text((x + 24, 250), name, fill=color, font=font("sans_bold", 38))
        d.text((x + 24, 300), sub, fill=MUTED, font=font("sans", 28))
        for j, ln in enumerate(lines):
            d.text((x + 24, 360 + j * 50), ln, fill=INK, font=font("sans", 28))
deck.custom("10_dreams", dreams)


# 11 — hypnosis (compare two theories)
deck.compare("11_hypnosis", "Hypnosis — two competing theories.",
    {"label": "DIVIDED CONSCIOUSNESS",
     "color": deck.accent,
     "lines": [
         "Hilgard.",
         "",
         "Hypnosis splits awareness.",
         "A 'hidden observer' is",
         "aware of pain or events",
         "even when conscious self",
         "isn't.",
     ],
     "footnote": "Strong evidence in pain studies."},
    {"label": "SOCIAL INFLUENCE",
     "color": MAROON,
     "lines": [
         "Spanos & others.",
         "",
         "Not a special state.",
         "People play a deeply",
         "suggested role —",
         "an immersive expectation,",
         "not altered consciousness.",
     ],
     "footnote": "Hypnosis can't make you act against core values."})


# 12 — drug categories (custom 3-column table)
def drug_categories(img, d):
    d.text((110, 70), "Psychoactive drugs.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "Mechanism words first, then the three big categories.",
           fill=MUTED, font=font("sans", 30))

    # Mechanism row
    d.rounded_rectangle([110, 220, (W // 2) - 20, 350], radius=18,
                        outline=deck.accent, width=4, fill=deck.card_bg)
    d.text((140, 240), "AGONIST", fill=deck.accent, font=font("sans_bold", 38))
    d.text((140, 290), "mimics or boosts a neurotransmitter.",
           fill=INK, font=font("sans", 28))
    d.text((140, 320), "(heroin → endorphin receptors)",
           fill=MUTED, font=font("sans", 24))

    d.rounded_rectangle([(W // 2) + 20, 220, W - 110, 350], radius=18,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text(((W // 2) + 50, 240), "ANTAGONIST", fill=MAROON, font=font("sans_bold", 38))
    d.text(((W // 2) + 50, 290), "blocks a neurotransmitter.",
           fill=INK, font=font("sans", 28))
    d.text(((W // 2) + 50, 320), "(naloxone → reverses opioid overdose)",
           fill=MUTED, font=font("sans", 24))

    # Three category cards
    cats = [
        ("STIMULANTS",
         "speed up the CNS",
         ["caffeine",
          "nicotine",
          "cocaine",
          "methamphetamine"],
         "↑ heart rate · ↑ alertness · ↑ dopamine",
         deck.accent),
        ("DEPRESSANTS",
         "slow down the CNS",
         ["alcohol",
          "opioids (heroin, oxy)",
          "benzodiazepines (Xanax)",
          ""],
         "calm anxiety · slow breathing · risky at high dose",
         MAROON),
        ("HALLUCINOGENS",
         "distort perception",
         ["LSD",
          "psilocybin",
          "MDMA",
          "marijuana*"],
         "*marijuana technically its own category",
         MAROON_DARK),
    ]
    cw = 580
    for i, (name, sub, items, foot, color) in enumerate(cats):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 400, x + cw, 950], radius=20,
                            outline=color, width=4, fill=deck.card_bg)
        d.text((x + 24, 420), name, fill=color, font=font("sans_bold", 38))
        d.text((x + 24, 470), sub, fill=MUTED, font=font("sans", 28))
        for j, item in enumerate(items):
            if item:
                d.text((x + 24, 540 + j * 60), f"·  {item}",
                       fill=INK, font=font("sans", 32))
        # footer line, wrapped
        foot_lines = wrap_text(d, foot, font("sans", 24), cw - 48)
        for k, fl in enumerate(foot_lines):
            d.text((x + 24, 850 + k * 32), fl, fill=color, font=font("sans", 24))
deck.custom("12_drug_categories", drug_categories)


# 13 — tolerance / dependence / withdrawal (definition trio)
def tolerance(img, d):
    d.text((110, 80), "Tolerance · Dependence · Withdrawal.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 170), "Three different ideas. One underlying theme — the brain finding a new normal.",
           fill=MUTED, font=font("sans", 30))

    items = [
        ("TOLERANCE",
         "Body adapts; you need more for the same effect.",
         "First sip of coffee in 7th grade hit hard. Now 3 cups barely register.",
         deck.accent),
        ("DEPENDENCE",
         "Body needs the drug to feel normal.",
         "Two flavors — physical (rewired body) and psychological (cravings, habit).",
         MAROON),
        ("WITHDRAWAL",
         "Unpleasant symptoms when the drug is removed.",
         "Coffee headaches.  Alcohol tremors & seizures.  Severity = how much the brain adapted.",
         MAROON_DARK),
    ]
    for i, (name, defn, ex, color) in enumerate(items):
        y = 270 + i * 220
        d.rounded_rectangle([110, y, W - 110, y + 200], radius=20,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((140, y + 20), name, fill=color, font=font("sans_bold", 44))
        d.text((140, y + 80), defn, fill=INK, font=font("sans_bold", 34))
        # wrap example
        ex_lines = wrap_text(d, ex, font("sans", 28), W - 320)
        for j, ln in enumerate(ex_lines):
            d.text((140, y + 130 + j * 36), ln, fill=MUTED, font=font("sans", 28))
deck.custom("13_tolerance", tolerance)


# 14 — recap
deck.recap("14_recap", "Recap.", [
    "Awareness:  conscious · preconscious · unconscious · automatic.",
    "Sleep cycles ~90 min through NREM 1·2·3 → REM.  REM = paradoxical, lengthens toward morning.",
    "Sleep theories:  restorative · consolidation · evolutionary.",
    "Disorders:  insomnia · apnea · somnambulism (NREM) · narcolepsy · REM behavior disorder.",
    "Dreams:  Freud (manifest/latent) · Hobson (activation-synthesis) · info-processing.",
    "Drugs:  agonist mimics · antagonist blocks.  Stimulants · Depressants · Hallucinogens.  Tolerance · Dependence · Withdrawal.",
])


# 15 — path
deck.path("15_path", [
    ("✓",  "Watch this lesson",          "(done!)"),
    ("1.", "Read Myers Module 5",        "Sleep stages + drug table especially"),
    ("2.", "AP Classroom · 15 MCQ",      "Sleep stages, dream theories, drug categories"),
    ("3.", "Assignment in dashboard",     "Label 5 scenarios — stage / theory / drug type"),
    ("4.", "Advisor check-in",           "If agonist vs antagonist, NREM vs REM still fuzzy"),
], next_text="Next up:  Module 6 — Learning & Conditioning. Pavlov, Skinner, and your study habits.")


print("AP Psych Module 5 slides built.")

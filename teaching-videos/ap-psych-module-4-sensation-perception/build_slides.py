"""AP Psychology · Module 4 — Sensation & Perception.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
14 slides. Heavy on slide_kit primitives; 4 customs:
  - 02_hook              : the gorilla / inattentional blindness opener
  - 05_thresholds        : Weber's Law graph (constant ratio, not constant amount)
  - 06_signal_detection  : 2x2 hit / miss / false alarm / correct rejection matrix
  - 09_pause1_answer     : sensory adaptation explanation
  - 10_attention_gestalt : 6-cell Gestalt principles grid (mini illustrations)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=4, output_dir="slides", logo_path=LOGO)


# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 4 — Sensation & Perception",
           "~7 minutes  ·  Why your brain shows you a different world than your eyes do")


# 02 — hook (the famous gorilla / inattentional-blindness experiment)
def hook(img, d):
    d.text((110, 80), "The invisible gorilla.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 168), "Simons & Chabris (1999) — Harvard's most famous attention experiment.",
           fill=MAROON_DARK, font=font("serif_ital", 36))

    # Left card — the "task" the participants thought they were doing
    px, py, pw, ph = 110, 250, 800, 540
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=24,
                        outline=deck.accent, width=6, fill=deck.card_bg)
    d.text((px + 30, py + 30), "YOUR JOB:", fill=deck.accent, font=font("sans_bold", 38))
    d.text((px + 30, py + 100), "Watch a short video.",
           fill=INK, font=font("sans", 36))
    d.text((px + 30, py + 160), "Count how many times the",
           fill=INK, font=font("sans", 36))
    d.text((px + 30, py + 210), "white-shirt team passes the ball.",
           fill=INK, font=font("sans", 36))

    # Two stick-figure teams
    # White team
    for i, x in enumerate([px + 60, px + 160, px + 260]):
        d.ellipse([x, py + 320, x + 50, py + 370], outline=INK, width=4, fill=deck.card_bg)
        d.rectangle([x + 5, py + 370, x + 45, py + 440], outline=INK, width=4, fill=deck.card_bg)
    # Black team
    for i, x in enumerate([px + 460, px + 560, px + 660]):
        d.ellipse([x, py + 320, x + 50, py + 370], outline=INK, width=4, fill=INK)
        d.rectangle([x + 5, py + 370, x + 45, py + 440], outline=INK, width=4, fill=INK)
    # Ball
    d.ellipse([px + 360, py + 360, px + 410, py + 410], fill=deck.accent, outline=MAROON, width=3)

    # Right card — the twist
    cx, cy = 980, 250
    d.rounded_rectangle([cx, cy, cx + 830, cy + 540], radius=24,
                        outline=MAROON, width=6, fill=deck.accent_light)
    d.text((cx + 30, cy + 30), "THE TWIST:", fill=MAROON_DARK, font=font("sans_bold", 38))
    # The gorilla
    gx, gy = cx + 380, cy + 200
    d.ellipse([gx - 60, gy - 110, gx + 60, gy + 10], fill=MAROON_DARK)  # head
    d.rounded_rectangle([gx - 90, gy + 10, gx + 90, gy + 170], radius=20, fill=MAROON_DARK)  # body
    d.ellipse([gx - 25, gy - 80, gx - 5, gy - 60], fill=deck.accent_light)  # eye
    d.ellipse([gx + 5, gy - 80, gx + 25, gy - 60], fill=deck.accent_light)  # eye
    d.line([gx - 95, gy + 80, gx - 130, gy + 130], fill=MAROON_DARK, width=12)  # arm
    d.line([gx + 95, gy + 80, gx + 130, gy + 130], fill=MAROON_DARK, width=12)  # arm

    d.text((cx + 30, cy + 410), "A person in a gorilla suit",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((cx + 30, cy + 450), "walks straight through the game.",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((cx + 30, cy + 495), "Half the students never see it.",
           fill=RED, font=font("sans_bold", 32))

    centered(d, "Your eyes saw it. Your brain threw it out. That gap = today's whole module.",
             font("serif_bold", 32), 880, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Sensation vs. perception. Bottom-up vs. top-down.",
    "Thresholds — absolute, JND, and Weber's Law.",
    "Signal detection + sensory adaptation.",
    "Gestalt principles + selective attention.",
    "Depth, constancy, and perceptual set.",
], footnote="By end: read a scenario, name the concept.")


# 04 — sensation vs perception (compare)
deck.compare("04_sense_vs_perceive", "Sensation  vs.  Perception.",
    {"label": "SENSATION  ·  bottom-up",
     "color": MAROON,
     "lines": [
         "Raw data hitting your",
         "sense organs.",
         "",
         "Eyes catch light.",
         "Ears catch vibration.",
         "Skin catches pressure.",
     ],
     "footnote": "World → senses → brain. The signal coming in."},
    {"label": "PERCEPTION  ·  top-down",
     "color": deck.accent,
     "lines": [
         "What your brain DOES",
         "with that raw data.",
         "",
         "Sort, label, fill in gaps,",
         "decide what matters —",
         "shaped by expectations.",
     ],
     "footnote": "Same dress, two colors. That's the gap."})


# 05 — Weber's Law graph (constant RATIO, not constant amount)
def thresholds(img, d):
    d.text((110, 70), "Weber's Law — constant RATIO, not constant amount.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 158), "The just-noticeable-difference (JND) scales with the original stimulus.",
           fill=MUTED, font=font("sans", 30))

    # Three weight comparisons stacked
    # For each: a "starting weight" bar + a "JND" sliver, with the percentage shown
    examples = [
        # (label, base_text, jnd_text, ratio_pct, base_width)
        ("pencil",   "100 g",    "+ 2 g",    "2%",   170),
        ("book",     "1,000 g",  "+ 20 g",   "2%",   480),
        ("dumbbell", "50 lb",    "+ 1 lb",   "2%",   820),
    ]
    bar_x = 320
    bar_h = 90
    label_x = W - 380

    for i, (label, base_t, jnd_t, ratio, base_w) in enumerate(examples):
        y = 270 + i * 160
        # Label on the far left
        d.text((110, y + 25), label, fill=MAROON_DARK, font=font("sans_bold", 32))

        # Base bar
        d.rectangle([bar_x, y, bar_x + base_w, y + bar_h],
                    fill=deck.accent_light, outline=MAROON, width=4)
        d.text((bar_x + 12, y + 26), base_t, fill=MAROON_DARK, font=font("sans_bold", 32))

        # JND sliver — proportional (~2% wide) but shown wider so it's visible
        jnd_w = max(int(base_w * 0.04), 24)  # exaggerated for legibility
        d.rectangle([bar_x + base_w, y, bar_x + base_w + jnd_w, y + bar_h],
                    fill=deck.accent, outline=MAROON_DARK, width=4)
        d.text((bar_x + base_w + jnd_w + 14, y + 26),
               jnd_t, fill=deck.accent, font=font("sans_bold", 30))

        # Ratio chip on the right
        d.rounded_rectangle([label_x, y + 12, label_x + 200, y + bar_h - 12],
                            radius=14, fill=MAROON, outline=MAROON_DARK, width=3)
        ratio_text = f"JND ≈ {ratio}"
        tw = d.textlength(ratio_text, font=font("sans_bold", 28))
        d.text((label_x + (200 - tw) / 2, y + 24), ratio_text,
               fill=deck.accent_light, font=font("sans_bold", 28))

    # Bottom box — the rule
    d.rounded_rectangle([110, 800, W - 110, 950], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Same 2 grams: noticed on a pencil. Invisible on a dumbbell.",
             font("serif_bold", 36), 825, MAROON_DARK)
    centered(d, "Weber:  weight ≈ 2%   ·   sound ≈ 5%   ·   constant percentage, not constant amount.",
             font("sans_bold", 32), 885, MAROON_DARK)
deck.custom("05_thresholds", thresholds)


# 06 — signal detection 2x2 matrix
def signal_detection(img, d):
    d.text((110, 70), "Signal detection theory  —  the radiologist's 2×2.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 158), "Same X-ray. Four possible outcomes. Detection isn't just about the signal.",
           fill=MUTED, font=font("sans", 30))

    # 2x2 matrix layout
    # Columns:    SIGNAL PRESENT (tumor)  |  SIGNAL ABSENT (no tumor)
    # Rows:       SAID YES                |  SAID NO
    cell_w = 700
    cell_h = 230
    grid_x = 360
    grid_y = 320

    # Column headers
    d.text((grid_x + 60, grid_y - 80), "TUMOR PRESENT",
           fill=MAROON, font=font("sans_bold", 36))
    d.text((grid_x + cell_w + 80, grid_y - 80), "TUMOR ABSENT",
           fill=MAROON, font=font("sans_bold", 36))

    # Row labels
    d.text((90, grid_y + 80), "SAID",
           fill=MAROON, font=font("sans_bold", 36))
    d.text((90, grid_y + 130), "\"YES\"",
           fill=MAROON, font=font("sans_bold", 36))
    d.text((90, grid_y + cell_h + 80), "SAID",
           fill=MAROON, font=font("sans_bold", 36))
    d.text((90, grid_y + cell_h + 130), "\"NO\"",
           fill=MAROON, font=font("sans_bold", 36))

    # Four cells — (label, sub, color, fill)
    cells = [
        # row 0 (said yes)
        ("HIT",              "correctly spotted",        deck.accent,    deck.accent_light),
        ("FALSE ALARM",      "saw a tumor that wasn't",  RED,            deck.card_bg),
        # row 1 (said no)
        ("MISS",             "missed a real tumor",      RED,            deck.card_bg),
        ("CORRECT REJECTION","correctly cleared",        deck.accent,    deck.accent_light),
    ]
    for i, (label, sub, color, fill) in enumerate(cells):
        col = i % 2
        row = i // 2
        x0 = grid_x + col * cell_w
        y0 = grid_y + row * cell_h
        d.rounded_rectangle([x0, y0, x0 + cell_w - 30, y0 + cell_h - 30],
                            radius=18, outline=color, width=5, fill=fill)
        d.text((x0 + 30, y0 + 30), label, fill=color, font=font("sans_bold", 38))
        d.text((x0 + 30, y0 + 110), sub, fill=INK, font=font("sans", 30))

    # Bottom takeaway
    d.rounded_rectangle([110, 850, W - 110, 970], radius=20,
                        fill=MAROON, outline=MAROON_DARK, width=4)
    centered(d, "Expectations · motivation · fatigue all shift the line. The detector matters as much as the signal.",
             font("sans_bold", 28), 895, deck.accent_light)
deck.custom("06_signal_detection", signal_detection)


# 07 — sensory adaptation (definition card)
deck.definition("07_adaptation",
                "Sensory adaptation.",
                "A constant, unchanging stimulus fades from awareness.",
                sub="The smell of your own room. The clock ticking. The seat under you right now.")


# 08 — pause + try (perfume saleswoman)
deck.pause("08_pause1", "PAUSE  &  TRY",
           "A perfume saleswoman sprays a sample on her wrist. Two hours in, a customer says \"wow, your perfume is strong.\" She barely smells it anymore.",
           "What concept?  Why the gap?",
           hint="Pause. Decide. Press play.")


# 09 — pause answer
def pause_answer(img, d):
    d.text((110, 80), "Answer.",
           fill=MAROON, font=font("serif_bold", 80))

    chips = [
        ("CONCEPT",      "SENSORY ADAPTATION  —  constant stimulus fades from awareness."),
        ("HER",          "Olfactory neurons still firing. Brain stopped reporting it up."),
        ("THE CUSTOMER", "Brand-new stimulus to them. Their system hasn't adapted yet."),
    ]
    for i, (label, body) in enumerate(chips):
        y = 240 + i * 150
        d.rounded_rectangle([110, y, W - 110, y + 120], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((150, y + 30), label, fill=deck.accent,
               font=font("sans_bold", 38))
        # word-wrap the body so it doesn't overflow
        body_lines = wrap(d, body, font("sans", 32), W - 660)
        for j, ln in enumerate(body_lines[:2]):
            d.text((480, y + 24 + j * 44), ln, fill=INK, font=font("sans", 32))

    # Bottom banner
    d.rounded_rectangle([110, 760, W - 110, 920], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Same molecules in the air. Two completely different perceptions.",
             font("serif_bold", 40), 790, MAROON_DARK)
    centered(d, "Why you can't trust your own nose to tell you you've put on too much cologne.",
             font("sans", 32), 855, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)


# 10 — Gestalt principles grid (3x2 mini-illustrations)
def gestalt_grid(img, d):
    d.text((110, 70), "Gestalt principles + attention.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "The brain's rules for turning a mess of pixels into a meaningful whole.",
           fill=MUTED, font=font("sans", 30))

    # 3x2 grid of principle cards
    cw, ch = 580, 300
    start_x = 110
    start_y = 230
    gap = 20

    principles = [
        "PROXIMITY", "SIMILARITY", "CLOSURE",
        "CONTINUITY", "FIGURE / GROUND", "COMMON FATE",
    ]
    blurbs = [
        "things close together = grouped",
        "things alike = grouped",
        "brain fills missing gaps",
        "we see smooth lines, not breaks",
        "object pops out from background",
        "things moving together = grouped",
    ]

    for i, (name, sub) in enumerate(zip(principles, blurbs)):
        col = i % 3
        row = i // 3
        x = start_x + col * (cw + gap)
        y = start_y + row * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, y + 20), name, fill=deck.accent, font=font("sans_bold", 30))

        # Mini-illustration in the lower portion of each card
        ix0 = x + 24
        iy0 = y + 80
        ix1 = x + cw - 24
        iy1 = y + ch - 70

        if name == "PROXIMITY":
            # 6 dots: 3 close, gap, 3 close → reads as 2 groups
            cx_ = (ix0 + ix1) / 2
            cy_ = (iy0 + iy1) / 2
            for j, dx in enumerate([-180, -150, -120, 60, 90, 120]):
                d.ellipse([cx_ + dx - 16, cy_ - 16, cx_ + dx + 16, cy_ + 16],
                          fill=MAROON)
        elif name == "SIMILARITY":
            # rows alternating filled circles vs filled squares → reads as rows by SHAPE
            cx_ = (ix0 + ix1) / 2
            cy_ = (iy0 + iy1) / 2
            for ry, kind in enumerate(["circle", "square", "circle"]):
                for cxoff in [-160, -100, -40, 20, 80, 140]:
                    px = cx_ + cxoff
                    py = cy_ - 60 + ry * 60
                    if kind == "circle":
                        d.ellipse([px - 16, py - 16, px + 16, py + 16], fill=MAROON)
                    else:
                        d.rectangle([px - 16, py - 16, px + 16, py + 16], fill=deck.accent)
        elif name == "CLOSURE":
            # broken circle — 4 arcs with gaps
            cx_ = (ix0 + ix1) / 2
            cy_ = (iy0 + iy1) / 2
            r = 80
            for start, end in [(20, 70), (110, 160), (200, 250), (290, 340)]:
                d.arc([cx_ - r, cy_ - r, cx_ + r, cy_ + r],
                      start=start, end=end, fill=MAROON, width=8)
        elif name == "CONTINUITY":
            # Two crossing curves — eye reads them as continuous, not 4 separate
            cx_ = (ix0 + ix1) / 2
            cy_ = (iy0 + iy1) / 2
            # smooth curve 1 (sine-ish) drawn as line segments
            pts1 = [(cx_ - 200 + i * 20, cy_ + int(40 * (i - 10) / 10) * (-1 if i > 10 else 1))
                    for i in range(0, 21)]
            for j in range(len(pts1) - 1):
                d.line([pts1[j], pts1[j + 1]], fill=MAROON, width=6)
            # smooth crossing diagonal
            d.line([(cx_ - 200, cy_ - 60), (cx_ + 200, cy_ + 60)],
                   fill=deck.accent, width=6)
        elif name == "FIGURE / GROUND":
            # Big rounded box (background) with a contrasting circle on top (figure)
            d.rectangle([ix0 + 40, iy0 + 10, ix1 - 40, iy1 - 10],
                        fill=deck.accent_light, outline=MAROON, width=3)
            cx_ = (ix0 + ix1) / 2
            cy_ = (iy0 + iy1) / 2
            d.ellipse([cx_ - 70, cy_ - 70, cx_ + 70, cy_ + 70],
                      fill=MAROON, outline=MAROON_DARK, width=3)
        elif name == "COMMON FATE":
            # 4 arrows all pointing the same direction → grouped
            cx_ = (ix0 + ix1) / 2
            cy_ = (iy0 + iy1) / 2
            for ry in range(4):
                ay = cy_ - 60 + ry * 40
                d.line([(cx_ - 120, ay), (cx_ + 80, ay)], fill=MAROON, width=6)
                # arrowhead
                d.polygon([(cx_ + 80, ay - 12), (cx_ + 110, ay), (cx_ + 80, ay + 12)],
                          fill=MAROON)

        # Sub-caption at the bottom of the card
        d.text((x + 24, y + ch - 50), sub, fill=MUTED, font=font("sans", 24))

    # No room for a footer banner with this 3x2 grid; rely on the title.
deck.custom("10_attention_gestalt", gestalt_grid)


# 11 — depth + constancy (compare monocular vs binocular)
deck.compare("11_depth_constancy", "Depth cues  ·  monocular  vs.  binocular.",
    {"label": "MONOCULAR  ·  one eye",
     "color": MAROON,
     "lines": [
         "Interposition — closer",
         "blocks farther.",
         "Linear perspective — lines",
         "converge into the distance.",
         "Relative size & texture",
         "gradient.",
     ],
     "footnote": "Why depth still works in a flat photograph."},
    {"label": "BINOCULAR  ·  both eyes",
     "color": deck.accent,
     "lines": [
         "Retinal disparity — each",
         "eye gets a different image.",
         "Convergence — eyes turn",
         "inward as objects get closer.",
         "",
         "+ Constancy keeps it stable.",
     ],
     "footnote": "Plus: size · shape · color constancy hold the world steady."})


# 12 — real world: perceptual set + culture
def real_world(img, d):
    d.text((110, 80), "Perceptual set  =  what you expect to see shapes what you see.",
           fill=MAROON, font=font("serif_bold", 46))

    # Two cards side by side — same blurry photo, two different labels
    for i, (label, sub, color) in enumerate([
        ("Told it's a CAT.", "they describe whiskers, slit pupils", deck.accent),
        ("Told it's a DOG.", "they describe a snout, floppy ears", MAROON),
    ]):
        x = 110 + i * 870
        d.rounded_rectangle([x, 220, x + 810, 580], radius=24,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((x + 30, 250), label, fill=color, font=font("sans_bold", 46))
        # Stylized blurry oval "photo"
        d.ellipse([x + 200, 360, x + 610, 510],
                  fill=deck.accent_light, outline=MUTED, width=3)
        d.text((x + 30, 540), sub, fill=INK, font=font("serif_ital", 30))

    # Big takeaway banner
    d.rounded_rectangle([110, 620, W - 110, 800], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Same photo. Different prior knowledge. Different perception.",
             font("serif_bold", 40), 650, MAROON_DARK)
    centered(d, "Culture also shapes it — kids who never grew up around right-angled buildings",
             font("sans", 30), 715, MAROON_DARK)
    centered(d, "are less fooled by certain optical illusions that depend on those angles.",
             font("sans", 30), 755, MAROON_DARK)

    # Bottom: eyewitness consequence
    d.rounded_rectangle([110, 830, W - 110, 950], radius=20,
                        fill=MAROON, outline=MAROON_DARK, width=4)
    centered(d, "Why eyewitness testimony is way less reliable than people think.",
             font("sans_bold", 34), 870, deck.accent_light)
deck.custom("12_real_world", real_world)


# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Sensation = bottom-up raw input. Perception = top-down interpretation.",
    "Absolute threshold = min you can detect. JND = min change. Weber = constant %.",
    "Signal detection: hits, misses, false alarms, correct rejections — expectations matter.",
    "Sensory adaptation: constant stimulus fades. The smell of your own room.",
    "Gestalt: figure-ground, proximity, similarity, closure, continuity, common fate.",
    "Depth = monocular + binocular cues. Constancy holds the world steady. Perceptual set shapes what you see.",
])


# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read Myers Module 4",      "Sensation & Perception — focus on Weber's Law and Gestalt"),
    ("2.", "AP Classroom · 15 MCQ",    "Especially: identify the Gestalt principle in example images"),
    ("3.", "Assignment in dashboard",  "Label thresholds, attention, and Gestalt across 5 scenarios"),
    ("4.", "Advisor check-in",         "Book one if signal detection or Weber still feel fuzzy"),
], next_text="Next up:  Module 5 — States of Consciousness. Sleep, dreams, and what your brain does when you're not driving.")


print("AP Psych Module 4 slides built.")

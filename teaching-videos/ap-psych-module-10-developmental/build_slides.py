"""AP Psychology · Module 10 — Developmental Psychology.

Lavender theme (auto-resolved from "AP Psychology" prefix).
Custom slides:
  - Piaget's 4 stages as a horizontal age timeline
  - Erikson's 8 stages as a vertical lifespan ladder ("you are here" on stage 5)
  - Attachment 4-quadrant
  - Pause-answer custom
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=10, output_dir="slides", logo_path=LOGO)

# ── 01 — title ─────────────────────────────────────────────────────────
deck.title("01_title", "AP Psychology",
           "Module 10 — Developmental Psychology",
           "~9 minutes  ·  How a cell becomes a person — across a whole lifespan")

# ── 02 — hook (Erikson identity vs role confusion: YOU ARE HERE) ───────
def hook(img, d):
    d.text((110, 80), "You are here.", fill=MAROON, font=font("serif_bold", 96))
    d.text((110, 200), "Erikson Stage 5  ·  Identity vs. Role Confusion",
           fill=MAROON_DARK, font=font("serif", 52))

    # Big "YOU" arrow card
    d.rounded_rectangle([110, 320, W - 110, 540], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=6)
    centered(d, "Adolescence  ·  ages 12–18",
             font("sans_bold", 42), 350, MAROON_DARK)
    centered(d, "\"Who am I, separate from my parents and friends?\"",
             font("serif_ital", 48), 420, INK)
    centered(d, "Your single biggest psychological task — right now.",
             font("sans", 36), 490, MAROON_DARK)

    # Three side facts
    facts = [
        ("BABIES",  "trust the world?"),
        ("YOU",     "who am I?"),
        ("ELDERS",  "did my life mean something?"),
    ]
    cw = 540
    for i, (name, q) in enumerate(facts):
        x = 110 + i * (cw + 30)
        d.rounded_rectangle([x, 620, x + cw, 800], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 640), name, fill=deck.accent, font=font("sans_bold", 40))
        d.text((x + 24, 710), q, fill=INK, font=font("serif_ital", 36))

    centered(d, "This module isn't just about babies and old people.   The middle is partly about you.",
             font("serif_bold", 36), 870, MAROON_DARK)
deck.custom("02_hook", hook)

# ── 03 — overview ──────────────────────────────────────────────────────
deck.overview("03_overview", "Game plan.", [
    "Three domains  +  prenatal  +  infancy  (how a human gets built).",
    "Piaget's 4 stages  +  Vygotsky's ZPD  (cognitive development).",
    "Erikson, Kohlberg, attachment, aging  (the rest of the lifespan).",
], footnote="By end: separate Piaget's 4 stages from Erikson's 8 stages without flinching.")

# ── 04 — three domains + prenatal + teratogens ────────────────────────
def domains(img, d):
    d.text((110, 70), "Three domains. One prenatal road.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Development happens in three streams at once.",
           fill=MUTED, font=font("sans", 32))

    # Three domain cards
    cw = 580
    domain_data = [
        ("PHYSICAL",         "body  ·  brain  ·  motor skills"),
        ("COGNITIVE",        "thinking  ·  language  ·  memory"),
        ("SOCIAL-EMOTIONAL", "relationships  ·  identity  ·  feelings"),
    ]
    for i, (name, desc) in enumerate(domain_data):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 220, x + cw, 380], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 244), name, fill=deck.accent, font=font("sans_bold", 36))
        d.text((x + 24, 308), desc, fill=INK, font=font("sans", 28))

    # Prenatal stage strip
    d.text((110, 430), "Prenatal — three stages.",
           fill=MAROON, font=font("serif_bold", 48))
    stages = [
        ("ZYGOTE",  "weeks 0–2",   "single cell → implants"),
        ("EMBRYO",  "weeks 2–8",   "organs forming"),
        ("FETUS",   "week 9 → birth", "growth + brain wiring"),
    ]
    for i, (label, age, note) in enumerate(stages):
        x = 110 + i * (cw + 20)
        y = 510
        d.rounded_rectangle([x, y, x + cw, y + 160], radius=18,
                            outline=MAROON, width=4, fill=deck.card_bg)
        d.text((x + 24, y + 14), label, fill=MAROON, font=font("serif_bold", 40))
        d.text((x + 24, y + 70), age, fill=deck.accent, font=font("sans_bold", 30))
        d.text((x + 24, y + 112), note, fill=INK, font=font("sans", 28))

    # Teratogen warning bar
    d.rounded_rectangle([110, 720, W - 110, 920], radius=22,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "TERATOGEN  =  agent that crosses placenta + damages development",
             font("sans_bold", 40), 745, MAROON_DARK)
    centered(d, "Textbook example:  ALCOHOL  →  Fetal Alcohol Syndrome (FAS)",
             font("serif_bold", 48), 815, MAROON)
    centered(d, "AP-favorite link.  Memorize:  alcohol  =  FAS.",
             font("sans", 32), 880, MAROON_DARK)
deck.custom("04_domains", domains)

# ── 05 — attachment 4-quadrant (Harlow + Ainsworth) ───────────────────
def attachment(img, d):
    d.text((110, 70), "Attachment — Ainsworth's four styles.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150), "Harlow first:  cloth mother > wire mother.   Contact comfort beats food.",
           fill=MUTED, font=font("sans", 30))

    # 2x2 grid
    qx, qy = 110, 230
    qw, qh = 850, 320
    gap = 30

    quadrants = [
        ("SECURE",                   "upset when mom leaves,",
         "calmed when she returns",  "healthiest — most kids",  deck.accent),
        ("INSECURE-AVOIDANT",        "ignores mom either way",
         "appears indifferent",      "the 'I don't care' style", MAROON),
        ("INSECURE-ANXIOUS",         "upset when mom leaves",
         "stays upset, even pushes her away on return",
         "also called 'resistant'",  MAROON_DARK),
        ("DISORGANIZED",             "no clear strategy",
         "freezes, contradicts itself",
         "often linked to abuse / trauma", RED),
    ]
    for i, (name, l1, l2, foot, color) in enumerate(quadrants):
        col = i % 2
        row = i // 2
        x = qx + col * (qw + gap)
        y = qy + row * (qh + gap)
        d.rounded_rectangle([x, y, x + qw, y + qh], radius=22,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((x + 30, y + 24), name, fill=color, font=font("sans_bold", 42))
        d.text((x + 30, y + 100), l1, fill=INK, font=font("sans", 32))
        d.text((x + 30, y + 150), l2, fill=INK, font=font("sans", 32))
        d.text((x + 30, y + 240), foot, fill=MUTED, font=font("serif_ital", 30))

    centered(d, "Strange Situation experiment  ·  Mary Ainsworth",
             font("sans_bold", 32), 920, MAROON_DARK)
deck.custom("05_attachment", attachment)

# ── 06 — Piaget's 4 stages as horizontal age timeline ─────────────────
def piaget(img, d):
    d.text((110, 70), "Piaget — 4 stages of cognitive development.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 150), "Mnemonic:  Some  Pretty  Cool  Frogs.",
           fill=deck.accent, font=font("sans_bold", 36))

    # Horizontal timeline
    line_y = 320
    box_w, box_h = 380, 380
    line_x0 = 110 + box_w // 2          # leftmost marker centered above leftmost card
    line_x1 = W - 110 - box_w // 2      # rightmost marker centered above rightmost card
    d.rectangle([line_x0, line_y - 4, line_x1, line_y + 4], fill=MAROON)

    # 4 evenly-spaced stage markers
    span = (line_x1 - line_x0) / 3   # 4 markers, 3 gaps
    stages = [
        ("SENSORIMOTOR",    "0 – 2",   "Object permanence"),
        ("PREOPERATIONAL",  "2 – 7",   "Symbolic thought\nEgocentrism\nNo conservation"),
        ("CONCRETE OPER.",  "7 – 11",  "Conservation\nReversibility\nLogic on real things"),
        ("FORMAL OPER.",    "11 +",    "Abstract reasoning\nHypothetical thinking"),
    ]
    for i, (name, age, milestone) in enumerate(stages):
        cx = int(line_x0 + i * span)
        # Circle + age label on the line
        d.ellipse([cx - 28, line_y - 28, cx + 28, line_y + 28],
                  fill=deck.accent, outline=MAROON, width=4)
        d.text((cx - 60, line_y + 50), age,
               fill=MAROON, font=font("sans_bold", 38))

        # Stage card below
        bx = cx - box_w // 2
        by = line_y + 130
        d.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        # Title (wrap if needed)
        f_t = font("sans_bold", 30)
        title_lines = wrap(d, name, f_t, box_w - 30)
        for j, tl in enumerate(title_lines):
            d.text((bx + 18, by + 18 + j * 36), tl,
                   fill=deck.accent, font=f_t)
        # Milestone (multi-line)
        f_m = font("sans", 26)
        ms_y = by + 18 + len(title_lines) * 36 + 24
        for line in milestone.split("\n"):
            d.text((bx + 18, ms_y), line, fill=INK, font=f_m)
            ms_y += 38

    # Bottom note
    d.rounded_rectangle([110, 880, W - 110, 970], radius=18, fill=deck.accent_light)
    centered(d, "Conservation task  =  the single most-tested experiment in this unit.",
             font("serif_bold", 36), 905, MAROON_DARK)
deck.custom("06_piaget", piaget)

# ── 07 — Vygotsky ZPD ─────────────────────────────────────────────────
def vygotsky(img, d):
    d.text((110, 70), "Vygotsky — Zone of Proximal Development.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 150), "Cognitive development is social.   Culture + tools + a more-skilled helper.",
           fill=MUTED, font=font("sans", 32))

    # Three concentric rings (left side)
    cx, cy = 580, 600
    rings = [
        (350, deck.card_bg, MUTED,            "TOO HARD  ·  even with help"),
        (240, deck.accent_light, deck.accent, "ZPD  ·  with help"),
        (130, MAROON,            MAROON_DARK, "alone"),
    ]
    for r, fill_color, outline_color, _ in rings:
        d.ellipse([cx - r, cy - r, cx + r, cy + r],
                  fill=fill_color, outline=outline_color, width=5)
    centered_x_text = lambda txt, fnt, y, color: d.text(
        (cx - d.textlength(txt, font=fnt) / 2, y), txt, fill=color, font=fnt
    )
    centered_x_text("CAN DO", font("sans_bold", 30), cy - 70, deck.accent_light)
    centered_x_text("ALONE",  font("sans_bold", 30), cy - 30, deck.accent_light)
    centered_x_text("ZPD",    font("sans_bold", 38), cy + 90, MAROON)
    centered_x_text("(with help)", font("sans", 26), cy + 140, MAROON_DARK)
    d.text((cx - 350, cy + 290), "TOO HARD — even with help",
           fill=MUTED, font=font("sans", 28))

    # Right column: scaffolding + Piaget vs Vygotsky
    rx = 1080
    d.rounded_rectangle([rx, 250, W - 110, 460], radius=22,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((rx + 30, 270), "SCAFFOLDING", fill=deck.accent, font=font("sans_bold", 44))
    d.text((rx + 30, 340), "Give just enough support,",
           fill=INK, font=font("sans", 32))
    d.text((rx + 30, 380), "then pull it back as they get",
           fill=INK, font=font("sans", 32))
    d.text((rx + 30, 420), "stronger.   (Like training wheels.)",
           fill=INK, font=font("sans", 32))

    d.rounded_rectangle([rx, 500, W - 110, 800], radius=22,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((rx + 30, 520), "PIAGET  vs.  VYGOTSKY",
           fill=MAROON, font=font("serif_bold", 40))
    d.text((rx + 30, 600), "Piaget:  development drives learning.",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, 650), "Vygotsky:  learning — social,",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, 690), "cultural — drives development.",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, 750), "AP loves this contrast.",
           fill=deck.accent, font=font("sans_bold", 28))
deck.custom("07_vygotsky", vygotsky)

# ── 08 — pause + try (conservation task) ───────────────────────────────
deck.pause("08_pause1", "PAUSE  &  TRY",
           "A 6-year-old watches you pour juice from a wide short cup into a tall narrow cup. None added, none removed. They say the tall cup has MORE.",
           "Which limit + which Piaget stage?",
           hint="Pause. Decide. Press play.")

# ── 09 — pause answer ──────────────────────────────────────────────────
def pause_answer(img, d):
    d.text((110, 80), "The answer.",
           fill=MAROON, font=font("serif_bold", 80))

    # Two answer cards
    answers = [
        ("LIMIT",  "lack of  CONSERVATION",
         "Quantity stays the same when shape changes — the child can't see that yet."),
        ("STAGE",  "PREOPERATIONAL  (ages 2–7)",
         "A 6-year-old fits.   By Concrete Operational (7+), they would conserve."),
    ]
    for i, (label, head, body) in enumerate(answers):
        x = 110 + i * 870
        d.rounded_rectangle([x, 240, x + 760, 580], radius=24,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 264), label, fill=deck.accent, font=font("sans_bold", 36))
        d.text((x + 30, 320), head, fill=MAROON, font=font("serif_bold", 42))
        # Wrap body
        f_b = font("sans", 30)
        for j, ln in enumerate(wrap(d, body, f_b, 700)):
            d.text((x + 30, 410 + j * 44), ln, fill=INK, font=f_b)

    # Footer
    d.rounded_rectangle([110, 640, W - 110, 920], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Egocentrism  +  lack of conservation  =  PREOPERATIONAL limits.",
             font("serif_bold", 44), 670, MAROON_DARK)
    centered(d, "The conservation task is the single most-tested",
             font("sans_bold", 36), 760, MAROON_DARK)
    centered(d, "experiment in this whole unit.",
             font("sans_bold", 36), 810, MAROON_DARK)
    centered(d, "Lock it in.",
             font("serif_bold", 38), 870, MAROON)
deck.custom("09_pause1_answer", pause_answer)

# ── 10 — Erikson's 8 stages as vertical lifespan ladder ───────────────
def erikson(img, d):
    d.text((110, 60), "Erikson — 8 psychosocial stages.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 130), "One identity crisis per life chapter.   Stage 5 is on every AP exam.",
           fill=MUTED, font=font("sans", 28))

    stages = [
        ("1", "Infancy",          "Trust  vs.  Mistrust",                False),
        ("2", "Toddler",          "Autonomy  vs.  Shame & Doubt",        False),
        ("3", "Preschool",        "Initiative  vs.  Guilt",              False),
        ("4", "Elementary",       "Industry  vs.  Inferiority",          False),
        ("5", "Adolescence",      "IDENTITY  vs.  ROLE CONFUSION",       True),
        ("6", "Young adulthood",  "Intimacy  vs.  Isolation",            False),
        ("7", "Middle adulthood", "Generativity  vs.  Stagnation",       False),
        ("8", "Late adulthood",   "Integrity  vs.  Despair",             False),
    ]

    # Vertical ladder
    row_h = 90
    y0 = 200
    for i, (num, age, crisis, highlight) in enumerate(stages):
        y = y0 + i * row_h
        if highlight:
            fill_color = deck.accent_light
            outline = MAROON
            width_b = 6
        else:
            fill_color = deck.card_bg
            outline = deck.accent
            width_b = 3
        d.rounded_rectangle([110, y, W - 110, y + row_h - 12], radius=14,
                            outline=outline, width=width_b, fill=fill_color)
        # Stage number circle
        d.ellipse([140, y + 12, 200, y + 72],
                  fill=MAROON if highlight else deck.accent,
                  outline=MAROON_DARK, width=3)
        nfnt = font("sans_bold", 36)
        nw = d.textlength(num, font=nfnt)
        d.text((170 - nw / 2, y + 18), num, fill=deck.bg, font=nfnt)
        # Age band
        d.text((230, y + 22), age, fill=MUTED, font=font("sans", 30))
        # Crisis
        d.text((620, y + 22), crisis,
               fill=MAROON if highlight else INK,
               font=font("serif_bold" if highlight else "serif", 36))
        # "YOU ARE HERE" arrow
        if highlight:
            d.text((W - 360, y + 22), "← YOU ARE HERE",
                   fill=MAROON, font=font("sans_bold", 32))
deck.custom("10_erikson", erikson)

# ── 11 — Kohlberg + Gilligan ──────────────────────────────────────────
def kohlberg(img, d):
    d.text((110, 70), "Kohlberg — 3 levels of moral reasoning.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 150), "Heinz dilemma:  steal a drug to save your dying wife?   Reasoning > answer.",
           fill=MUTED, font=font("sans", 30))

    levels = [
        ("PRECONVENTIONAL",   "young children",
         "\"Don't steal — you'll get caught.\"",
         "Avoid punishment.   Get rewards."),
        ("CONVENTIONAL",      "most teens & adults",
         "\"Don't steal — it's against the law.\"",
         "Social rules.   What others think."),
        ("POSTCONVENTIONAL",  "some adults",
         "\"Steal it — life > property.\"",
         "Abstract principles, even vs. law."),
    ]
    cw = 580
    for i, (name, who, quote, what) in enumerate(levels):
        x = 110 + i * (cw + 20)
        y = 230
        d.rounded_rectangle([x, y, x + cw, y + 460], radius=20,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, y + 22), name, fill=deck.accent, font=font("sans_bold", 32))
        d.text((x + 24, y + 80), who, fill=MUTED, font=font("serif_ital", 28))
        d.rounded_rectangle([x + 24, y + 140, x + cw - 24, y + 280], radius=14,
                            fill=deck.accent_light)
        f_q = font("serif_ital", 28)
        for j, ln in enumerate(wrap(d, quote, f_q, cw - 80)):
            d.text((x + 40, y + 160 + j * 38), ln, fill=MAROON_DARK, font=f_q)
        f_w = font("sans", 26)
        for j, ln in enumerate(wrap(d, what, f_w, cw - 48)):
            d.text((x + 24, y + 320 + j * 36), ln, fill=INK, font=f_w)

    # Gilligan critique band
    d.rounded_rectangle([110, 740, W - 110, 920], radius=22,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "CAROL GILLIGAN  —  the AP-favorite critique.",
             font("serif_bold", 42), 770, MAROON)
    centered(d, "Kohlberg's research = male-biased.   Women often reason through CARE + RELATIONSHIPS,",
             font("sans", 30), 830, MAROON_DARK)
    centered(d, "not abstract justice — and his scoring penalized that.",
             font("sans", 30), 870, MAROON_DARK)
deck.custom("11_kohlberg", kohlberg)

# ── 12 — Aging: crystallized vs fluid (compare) ───────────────────────
deck.compare("12_aging", "Aging the mind — two intelligences.",
    {"label": "CRYSTALLIZED  ↑",
     "color": deck.accent,
     "lines": [
         "Knowledge, vocabulary,",
         "expertise.",
         "",
         "Stable — or grows — with age.",
     ],
     "footnote": "Why grandparents crush trivia night."},
    {"label": "FLUID  ↓",
     "color": MAROON,
     "lines": [
         "Raw processing speed,",
         "working memory, problem-solving.",
         "",
         "Peaks in 20s.  Declines after.",
     ],
     "footnote": "Memorize the pair.   AP loves it."})

# ── 13 — recap ─────────────────────────────────────────────────────────
deck.recap("13_recap", "Recap.", [
    "3 domains: physical, cognitive, social-emotional. Teratogens → alcohol = FAS.",
    "Attachment: Harlow's contact comfort. Ainsworth's 4 — secure, avoidant, anxious, disorganized.",
    "Piaget's 4 stages: sensorimotor (object permanence) → preop (egocentrism, no conservation) → concrete (conservation) → formal (abstract).",
    "Vygotsky: ZPD + scaffolding. Learning is social and cultural.",
    "Erikson's 8 stages — AP-favorite is Stage 5: identity vs. role confusion.",
    "Kohlberg: pre / conventional / post. Gilligan: it's male-biased. Aging: crystallized stays, fluid declines.",
])

# ── 14 — path ──────────────────────────────────────────────────────────
deck.path("14_path", [
    ("✓",  "Watch this lesson",          "(done!)"),
    ("1.", "Read Myers Module 10",       "Developmental psychology — focus on Piaget + Erikson"),
    ("2.", "AP Classroom · 15 MCQ",      "Match scenarios to a Piaget stage OR an Erikson stage"),
    ("3.", "Assignment in dashboard",    "10 scenarios — tag each with the correct theorist + stage"),
    ("4.", "Advisor check-in",           "Book one if Piaget vs. Erikson still feels fuzzy. Most-confused pair in AP Psych."),
], next_text="Next up:  Module 11 — Personality.   Why you and your sibling, raised in the same house, came out wildly different humans.")

print("AP Psych Module 10 slides built.")

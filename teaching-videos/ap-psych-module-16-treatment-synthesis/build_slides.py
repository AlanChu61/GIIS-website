"""AP Psychology · Module 16 — Treatment: Synthesis & Review (AP exam prep).

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
This is the FINAL module of the course. Tone: supportive, exam-strategy-focused.
Custom slides: M13→M14→M15 synthesis flow · biopsychosocial Venn ·
exam structure pie · MCQ pattern decoder · pause-answer · trap comparison.
"""
import sys
import math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=16,
            output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 16 — Treatment: Synthesis & Review",
           "~9 minutes  ·  AP exam prep  ·  Patterns, strategy, FRQ tactics")

# 02 — hook (the exam-prep reframe)
def hook(img, d):
    d.text((110, 80), "16 modules later.",
           fill=MUTED, font=font("serif", 50))
    d.text((110, 160), "Today is the cash-it-in module.",
           fill=MAROON, font=font("serif_bold", 60))

    # Big banner
    d.rounded_rectangle([110, 290, W-110, 540], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "The AP exam tests in patterns.",
             font("serif_bold", 56), 320, MAROON_DARK)
    centered(d, "You don't need to know every detail.",
             font("sans", 38), 410, INK)
    centered(d, "You need to know which patterns the test repeats.",
             font("sans_bold", 38), 460, MAROON_DARK)

    # Three "today is about" cards
    items = [
        ("SYNTHESIS",  "M13 + M14 + M15 → one mental model"),
        ("STRATEGY",   "MCQ patterns + FRQ rules"),
        ("CONFIDENCE", "the test is studyable. content is finite."),
    ]
    cw = 580
    for i, (name, sub) in enumerate(items):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 600, x + cw, 800], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 622), name, fill=deck.accent, font=font("sans_bold", 38))
        lines = wrap(d, sub, font("sans", 28), cw - 48)
        for j, ln in enumerate(lines[:3]):
            d.text((x + 24, 690 + j * 38), ln, fill=INK, font=font("sans", 28))

    centered(d, "Today, the patterns.   Today, the strategy.   Today, we get you ready.",
             font("serif_bold", 36), 870, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Synthesis map — how M13, M14, M15 connect.",
    "Biopsychosocial — the unifying lens.",
    "AP exam structure — sections, timing, scoring.",
    "MCQ patterns + FRQ strategy + common traps.",
], footnote="By end: less studying psychology, more studying the test.")

# 04 — synthesis map (M13 → M14 → M15)
def synthesis_map(img, d):
    d.text((110, 70), "Three modules.  One flow.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "If a vignette appears, this is the path you walk.",
           fill=MUTED, font=font("sans", 32))

    # Three big boxes connected by arrows
    box_w = 500
    box_h = 380
    y0 = 280
    gap = 70
    total = box_w * 3 + gap * 2
    x_start = (W - total) // 2

    boxes = [
        {
            "tag":   "MODULE 13",
            "title": "ABNORMAL",
            "verb":  "Identify the disorder.",
            "lines": [
                "The four D's:",
                "deviance · distress ·",
                "dysfunction · danger.",
                "",
                "DSM-5 categories:",
                "anxiety · OCD · mood ·",
                "psychotic · personality.",
            ],
        },
        {
            "tag":   "MODULE 14",
            "title": "TREATMENT",
            "verb":  "Choose from the toolbox.",
            "lines": [
                "5 psychological:",
                "psychodynamic · behavioral ·",
                "cognitive · CBT · humanistic.",
                "",
                "Biomedical:",
                "SSRIs · antipsychotics ·",
                "lithium · ECT.",
            ],
        },
        {
            "tag":   "MODULE 15",
            "title": "APPLICATIONS",
            "verb":  "Match to the person.",
            "lines": [
                "Anxiety → exposure.",
                "Depression → CBT (+SSRI).",
                "OCD → ERP.",
                "PTSD → TF-CBT / EMDR.",
                "Schizophrenia → meds primary.",
                "BPD → DBT.",
            ],
        },
    ]

    for i, box in enumerate(boxes):
        x = x_start + i * (box_w + gap)
        # Card
        d.rounded_rectangle([x, y0, x + box_w, y0 + box_h], radius=22,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        # Header band
        d.rounded_rectangle([x, y0, x + box_w, y0 + 80], radius=22, fill=deck.accent)
        d.text((x + 22, y0 + 18), box["tag"], fill=deck.card_bg,
               font=font("sans_bold", 28))
        d.text((x + 22, y0 + 48), box["title"], fill=deck.card_bg,
               font=font("serif_bold", 26))
        # Verb headline
        d.text((x + 22, y0 + 100), box["verb"], fill=MAROON_DARK,
               font=font("sans_bold", 28))
        # Body
        f_b = font("sans", 24)
        for j, ln in enumerate(box["lines"]):
            d.text((x + 22, y0 + 150 + j * 30), ln, fill=INK, font=f_b)

        # Arrow to next box
        if i < 2:
            ax = x + box_w + 5
            ay = y0 + box_h // 2
            d.polygon([(ax, ay - 18), (ax + gap - 10, ay), (ax, ay + 18)],
                      fill=MAROON)

    # Bottom takeaway
    d.rounded_rectangle([110, 720, W-110, 870], radius=22,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Identify  →  Choose  →  Match.",
             font("serif_bold", 56), 745, MAROON_DARK)
    centered(d, "That's the entire treatment cluster on the AP exam.",
             font("sans_bold", 32), 820, MAROON_DARK)
deck.custom("04_synthesis_map", synthesis_map)

# 05 — biopsychosocial Venn diagram
def biopsychosocial(img, d):
    d.text((110, 70), "Biopsychosocial.",
           fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 168), "The lens that ties the whole course together.",
           fill=MUTED, font=font("sans", 32))

    # Three overlapping circles (Venn-style) — moved left, made smaller
    cx, cy = 700, 560
    r = 200
    # top, bottom-left, bottom-right
    centers = [
        (cx,            cy - 110),  # BIO (top)
        (cx - 170,      cy + 130),  # PSYCH (bottom-left)
        (cx + 170,      cy + 130),  # SOCIAL (bottom-right)
    ]
    colors_outline = [MAROON, deck.accent, MAROON_DARK]

    # Draw filled circles
    for (ccx, ccy), col in zip(centers, colors_outline):
        d.ellipse([ccx - r, ccy - r, ccx + r, ccy + r],
                  outline=col, width=8, fill=deck.accent_light)
    # Re-draw outlines on top
    for (ccx, ccy), col in zip(centers, colors_outline):
        d.ellipse([ccx - r, ccy - r, ccx + r, ccy + r],
                  outline=col, width=8)

    # In-circle labels — short, centered ON each circle (not outside)
    incircle = [
        ("BIO",     centers[0][0],     centers[0][1] - 130),
        ("PSYCH",   centers[1][0],     centers[1][1] + 90),
        ("SOCIAL",  centers[2][0],     centers[2][1] + 90),
    ]
    for name, lx, ly in incircle:
        f = font("sans_bold", 32)
        tw = d.textlength(name, font=f)
        d.text((lx - tw / 2, ly), name, fill=MAROON_DARK, font=f)

    # Center overlap label
    f_c = font("sans_bold", 22)
    line1 = "where most"
    line2 = "disorders live"
    line3 = "& treatment works"
    for j, ln in enumerate([line1, line2, line3]):
        tw = d.textlength(ln, font=f_c)
        d.text((cx - tw / 2, cy + 10 + j * 28), ln,
               fill=MAROON_DARK, font=f_c)

    # Right-side legend (outside the Venn)
    legend_x = 1230
    legend_y = 280
    d.rounded_rectangle([legend_x, legend_y, W - 110, 870], radius=22,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((legend_x + 30, legend_y + 24), "THREE LENSES",
           fill=MAROON, font=font("serif_bold", 40))

    legend = [
        ("BIOLOGY",     "genes · brain ·",
                        "neurotransmitters ·",
                        "hormones"),
        ("PSYCHOLOGY",  "thoughts · learning ·",
                        "emotion · memory ·",
                        "personality"),
        ("SOCIAL",      "culture · family ·",
                        "community · stressors ·",
                        "trauma"),
    ]
    ly = legend_y + 110
    for name, l1, l2, l3 in legend:
        d.text((legend_x + 30, ly), name, fill=deck.accent,
               font=font("sans_bold", 30))
        d.text((legend_x + 30, ly + 42), l1, fill=INK, font=font("sans", 24))
        d.text((legend_x + 30, ly + 72), l2, fill=INK, font=font("sans", 24))
        d.text((legend_x + 30, ly + 102), l3, fill=INK, font=font("sans", 24))
        ly += 170

    # Bottom takeaway
    d.rounded_rectangle([110, 920, W-110, 1010], radius=18,
                        fill=MAROON, outline=deck.accent, width=4)
    centered(d, "AP loves biopsychosocial.   Frame any FRQ this way → almost always earns points.",
             font("sans_bold", 28), 950, deck.accent_light)
deck.custom("05_biopsychosocial", biopsychosocial)

# 06 — AP exam structure (split bar + key facts)
def exam_structure(img, d):
    d.text((110, 70), "The AP exam — know this cold.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Two sections.  120 minutes total.",
           fill=MUTED, font=font("sans", 32))

    # Big horizontal split bar — 66.7% MCQ, 33.3% FRQ
    bar_x0, bar_x1 = 110, W - 110
    bar_y0, bar_y1 = 240, 360
    bar_w = bar_x1 - bar_x0
    mcq_w = int(bar_w * 0.667)
    # MCQ block
    d.rectangle([bar_x0, bar_y0, bar_x0 + mcq_w, bar_y1], fill=deck.accent)
    # FRQ block
    d.rectangle([bar_x0 + mcq_w, bar_y0, bar_x1, bar_y1], fill=MAROON)
    # Outline
    d.rectangle([bar_x0, bar_y0, bar_x1, bar_y1], outline=INK, width=3)
    # Labels in bar
    centered_x_mcq = bar_x0 + mcq_w // 2
    d.text((centered_x_mcq - 100, bar_y0 + 20), "66.7%",
           fill=deck.card_bg, font=font("serif_bold", 56))
    d.text((centered_x_mcq - 60, bar_y0 + 80), "MCQ",
           fill=deck.card_bg, font=font("sans_bold", 28))
    centered_x_frq = bar_x0 + mcq_w + (bar_w - mcq_w) // 2
    d.text((centered_x_frq - 90, bar_y0 + 20), "33.3%",
           fill=deck.accent_light, font=font("serif_bold", 56))
    d.text((centered_x_frq - 50, bar_y0 + 80), "FRQ",
           fill=deck.accent_light, font=font("sans_bold", 28))

    # Two info cards
    cards = [
        {
            "title": "SECTION 1 — MCQ",
            "lines": [
                "100 questions  ·  70 minutes",
                "~42 seconds per question",
                "Don't park.  Flag and move.",
                "Always come back.",
            ],
        },
        {
            "title": "SECTION 2 — FRQ",
            "lines": [
                "2 questions  ·  50 minutes",
                "FRQ #1 — concept application",
                "FRQ #2 — research design",
                "Write in sentences. Don't list.",
            ],
        },
    ]
    cw = 870
    for i, card in enumerate(cards):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 420, x + cw, 720], radius=20,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 30, 444), card["title"], fill=MAROON,
               font=font("serif_bold", 40))
        f_b = font("sans", 30)
        for j, ln in enumerate(card["lines"]):
            d.text((x + 30, 520 + j * 46), ln, fill=INK, font=f_b)

    # Scoring strip
    d.rounded_rectangle([110, 760, W-110, 940], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=5)
    d.text((150, 785), "SCORING — 1 to 5.   5 = highest.",
           fill=MAROON_DARK, font=font("sans_bold", 36))
    d.text((150, 845), "Most top US universities grant credit for a 4 or a 5.",
           fill=INK, font=font("sans", 30))
    d.text((150, 890), "Some accept a 3.   Aim high — the strategies work.",
           fill=MAROON_DARK, font=font("sans_bold", 30))
deck.custom("06_exam_structure", exam_structure)

# 07 — MCQ pattern decoder table
def mcq_patterns(img, d):
    d.text((110, 70), "The 5 MCQ patterns — memorize these.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 156), "Treatment-cluster vignettes repeat. Trigger phrase → answer.",
           fill=MUTED, font=font("sans", 30))

    rows = [
        ("“lie on a couch and free associate”",     "PSYCHODYNAMIC",            "(Freud)"),
        ("“graded exposure to a feared object”",    "SYSTEMATIC DESENS.",       "(behavioral)"),
        ("“challenges automatic neg. thoughts”",     "COGNITIVE / CBT",          "(Beck · Ellis)"),
        ("“unconditional positive regard”",         "HUMANISTIC",               "(Rogers)"),
        ("“treatment-resistant depression”",         "ECT",                      "(electroconvulsive)"),
    ]
    # Header row
    y0 = 220
    d.rounded_rectangle([110, y0, W-110, y0 + 60], radius=10, fill=MAROON)
    d.text((140, y0 + 12), "TRIGGER PHRASE IN VIGNETTE",
           fill=deck.accent_light, font=font("sans_bold", 28))
    d.text((1020, y0 + 12), "ANSWER",
           fill=deck.accent_light, font=font("sans_bold", 28))
    d.text((1500, y0 + 12), "ASSOCIATED NAME",
           fill=deck.accent_light, font=font("sans_bold", 28))

    y = y0 + 60
    row_h = 92
    f_phrase = font("serif_ital", 28)
    f_ans = font("sans_bold", 28)
    f_name = font("sans", 24)
    for i, (phrase, answer, name) in enumerate(rows):
        bg = deck.card_bg if i % 2 == 0 else deck.bg
        d.rectangle([110, y, W-110, y + row_h], fill=bg)
        # Wrap phrase to fit column width ~880
        plines = wrap(d, phrase, f_phrase, 880)
        for j, ln in enumerate(plines[:2]):
            d.text((140, y + 18 + j * 36), ln, fill=INK, font=f_phrase)
        d.text((1020, y + 30), answer, fill=deck.accent, font=f_ans)
        d.text((1500, y + 34), name, fill=MUTED, font=f_name)
        y += row_h
    # Border
    d.rectangle([110, y0, W-110, y], outline=deck.accent, width=3)

    # Bottom note
    d.rounded_rectangle([110, y + 30, W-110, y + 150], radius=18,
                        fill=deck.accent_light, outline=MAROON, width=4)
    centered(d, "5 patterns.  5 answer keys.  Worth several MCQ points on test day.",
             font("sans_bold", 32), y + 70, MAROON_DARK)
deck.custom("07_mcq_patterns", mcq_patterns)

# 08 — pause & try (CBT thought record vignette)
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Therapist asks the client to log upsetting situations + automatic thoughts + balanced alternatives, then test the new thought in real life this week.",
           "Approach?   Specific tool?",
           hint="Pause. Decide. Press play.")

# 09 — pause answer (and CBT vs cognitive trap)
def pause_answer(img, d):
    d.text((110, 70), "The answer.",
           fill=MAROON, font=font("serif_bold", 76))

    # Top answer card
    d.rounded_rectangle([110, 200, W-110, 380], radius=22,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((140, 230), "APPROACH:", fill=deck.accent, font=font("sans_bold", 32))
    d.text((400, 224), "Cognitive-Behavioral Therapy  (CBT)",
           fill=INK, font=font("serif_bold", 44))
    d.text((140, 310), "TOOL:", fill=deck.accent, font=font("sans_bold", 32))
    d.text((280, 304), "Thought record  +  behavioral homework",
           fill=INK, font=font("serif_bold", 40))

    # Trap explanation — two-column comparison
    d.text((110, 420), "The trap — CBT vs. pure cognitive:",
           fill=MAROON, font=font("serif_bold", 40))

    cols = [
        {
            "label": "PURE COGNITIVE",
            "color": MUTED,
            "lines": [
                "Stops at challenging",
                "the thought.",
                "",
                "All the work happens",
                "in the therapist's office.",
            ],
        },
        {
            "label": "CBT",
            "color": MAROON,
            "lines": [
                "Challenges the thought —",
                "AND tests it in real life.",
                "",
                "Behavioral homework /",
                "behavioral experiment.",
            ],
        },
    ]
    cw = 870
    for i, col in enumerate(cols):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 510, x + cw, 820], radius=20,
                            outline=col["color"], width=5, fill=deck.card_bg)
        d.text((x + 30, 538), col["label"], fill=col["color"],
               font=font("sans_bold", 42))
        f_b = font("sans", 32)
        for j, ln in enumerate(col["lines"]):
            d.text((x + 30, 620 + j * 40), ln, fill=INK, font=f_b)

    # Tell line
    d.rounded_rectangle([110, 860, W-110, 970], radius=18,
                        fill=deck.accent_light, outline=MAROON, width=4)
    centered(d, "Tell on the AP exam:  homework or behavioral test  =  CBT.",
             font("sans_bold", 34), 895, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# 10 — FRQ strategy (3 rules + 1 bonus)
def frq_strategy(img, d):
    d.text((110, 70), "FRQ strategy — where most points are lost.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 158), "33.3% of the exam.  Learnable.  Teachable.  Practiceable.",
           fill=MUTED, font=font("sans", 30))

    rules = [
        {
            "num": "1.",
            "head": "DEFINE every term.",
            "ex": "Don't say “CBT.”  Say “cognitive-behavioral therapy refers to a structured approach combining cognitive restructuring with behavioral techniques.”",
        },
        {
            "num": "2.",
            "head": "APPLY explicitly.",
            "ex": "Don't say “This is CBT.”  Say “In Maria's case, the therapist would help her identify the automatic thought 'I always fail,' challenge it with evidence, and assign behavioral activation.”",
        },
        {
            "num": "3.",
            "head": "NAME the psychologist.",
            "ex": "Pavlov · Skinner · Beck · Ellis · Rogers · Maslow · Freud.  Cite the actual person — almost always earns the point.",
        },
        {
            "num": "+",
            "head": "DON'T list.  EXPLAIN.",
            "ex": "A bullet list of terms gets fewer points than two sentences that actually use them. Write in sentences. Apply, don't catalog.",
        },
    ]

    y = 230
    for r in rules:
        d.rounded_rectangle([110, y, W-110, y + 170], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((140, y + 22), r["num"], fill=MAROON,
               font=font("serif_bold", 56))
        d.text((230, y + 30), r["head"], fill=MAROON,
               font=font("serif_bold", 40))
        f_b = font("sans", 26)
        lines = wrap(d, r["ex"], f_b, W - 410)
        for j, ln in enumerate(lines[:3]):
            d.text((230, y + 90 + j * 32), ln, fill=INK, font=f_b)
        y += 185
deck.custom("10_frq_strategy", frq_strategy)

# 11 — common traps (3 traps as cards)
def common_traps(img, d):
    d.text((110, 70), "3 traps the AP exam loves.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Treatment cluster — these come up almost every year.",
           fill=MUTED, font=font("sans", 32))

    traps = [
        {
            "tag":   "TRAP 1",
            "title": "CBT  vs.  pure cognitive  vs.  pure behavioral",
            "tell":  "Tell:  homework / experiment present?  →  CBT.   Thoughts only?  →  cognitive.   Action only?  →  behavioral.",
        },
        {
            "tag":   "TRAP 2",
            "title": "Negative reinforcement  ≠  punishment",
            "tell":  "Neg. reinforcement REMOVES unpleasant → INCREASES behavior. Punishment → DECREASES behavior. (Carries over from M6.)",
        },
        {
            "tag":   "TRAP 3",
            "title": "ECT is NOT outdated.",
            "tell":  "Modern ECT — anesthesia, controlled, safe.   For severe treatment-resistant depression (3+ failed meds), often the most effective option. Pop-culture image is 50 yrs out of date.",
        },
    ]

    y = 240
    for t in traps:
        d.rounded_rectangle([110, y, W-110, y + 200], radius=20,
                            outline=MAROON, width=5, fill=deck.card_bg)
        # Tag pill
        d.rounded_rectangle([130, y + 20, 280, y + 70], radius=10,
                            fill=MAROON)
        centered_x = 130 + (280 - 130) // 2
        tag_w = d.textlength(t["tag"], font=font("sans_bold", 26))
        d.text((centered_x - tag_w / 2, y + 30), t["tag"],
               fill=deck.accent_light, font=font("sans_bold", 26))
        # Title
        d.text((310, y + 26), t["title"], fill=MAROON_DARK,
               font=font("serif_bold", 36))
        # Tell line
        f_b = font("sans", 26)
        lines = wrap(d, t["tell"], f_b, W - 360)
        for j, ln in enumerate(lines[:3]):
            d.text((310, y + 90 + j * 34), ln, fill=INK, font=f_b)
        y += 220
deck.custom("11_common_traps", common_traps)

# 12 — real world / why synthesis matters beyond the test
def real_world(img, d):
    d.text((110, 80), "Beyond the test.",
           fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 180), "Every clinician thinks the way you're learning to think.",
           fill=MUTED, font=font("sans", 36))

    d.rounded_rectangle([110, 290, W-110, 540], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "They don't ask  “is this biology or psychology.”",
             font("sans", 38), 320, INK)
    centered(d, "They ask  “how much of each — and which lever moves first.”",
             font("serif_bold", 40), 380, MAROON_DARK)
    centered(d, "That's the move. That's the whole game.",
             font("sans_bold", 36), 460, MAROON_DARK)

    # Three "use it for life" cards
    items = [
        ("A friend struggles.",   "you'll have a framework."),
        ("A news article.",        "you'll spot the lens."),
        ("A character in a film.", "you'll see what's going on."),
    ]
    cw = 580
    for i, (line1, line2) in enumerate(items):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 600, x + cw, 800], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 632), line1, fill=MAROON,
               font=font("serif_bold", 36))
        d.text((x + 24, 700), line2, fill=INK, font=font("sans", 30))

    centered(d, "Not just a test skill.   A life skill.",
             font("serif_bold", 44), 870, MAROON_DARK)
deck.custom("12_real_world", real_world)

# 13 — recap (exam strategy edition)
deck.recap("13_recap", "Recap — exam strategy edition.", [
    "5 MCQ patterns:  couch · graded exposure · challenge thoughts · unconditional regard · treatment-resistant.",
    "CBT = cognitive + behavioral. The behavioral homework is the tell.",
    "FRQ rules: define every term, apply by name, cite the psychologist, write in sentences.",
    "Biopsychosocial framing on FRQs almost always earns points.",
    "100 MCQ in 70 min  +  2 FRQs in 50 min.   Score 4 or 5 → most US colleges grant credit.",
    "The test is studyable.  The content is finite.  The strategies work.",
])

# 14 — path (DIFFERENT — final-module exam-readiness path; CUSTOM so we can
# render the celebratory closing across multiple lines)
def final_path(img, d):
    d.text((110, 80), "How to actually master this module.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 170), "The course is over.  Here's your runway to the exam:",
           fill=MUTED, font=font("sans", 34))

    items = [
        ("✓",  "Watch this lesson",              "(done!)"),
        ("1.", "Schedule a full practice exam",  "Sit 2 hours. Time yourself. Score it honestly."),
        ("2.", "Review your weakest module",     "Practice scores tell you where to go back."),
        ("3.", "AP Classroom · past FRQs",       "Write 3+ FRQs by hand. Score against the rubric."),
        ("4.", "Advisor readiness check-in",     "Talk through weakest area. Make a 2-week plan."),
    ]
    y = 270
    for n, head, sub in items:
        done = n.strip() == "✓"
        n_color = deck.accent if done else MAROON
        head_color = deck.accent if done else INK
        d.text((140, y), n, fill=n_color, font=font("serif_bold", 44))
        d.text((230, y), head, fill=head_color, font=font("serif_bold", 38))
        if sub:
            d.text((230, y + 50), sub, fill=MUTED, font=font("sans", 28))
        y += 100

    # Celebratory closing card
    d.rounded_rectangle([110, 820, W-110, 1010], radius=22,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "This is the FINAL module.   You finished AP Psychology.",
             font("serif_bold", 36), 845, MAROON_DARK)
    centered(d, "You've earned a seat at the AP exam table.",
             font("sans_bold", 32), 905, MAROON_DARK)
    centered(d, "Now go take it.   Good luck.",
             font("serif_bold", 36), 955, MAROON)
deck.custom("14_path", final_path)

print("AP Psych Module 16 slides built.")

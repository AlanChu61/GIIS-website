"""AP Calculus AB · Module 12 — AP Exam Synthesis and Free-Response Strategy.

Capstone / synthesis module. No new calculus. Covers exam structure, the
six recurring FRQ patterns, and the rubric conventions (units, BECAUSE,
setup integral, calculator hygiene, time budgeting).

Custom slides:
- 02_hook              : the "right math, wrong rubric" story — student
                         loses 3 points to missing units / missing BECAUSE
                         / missing setup integral
- 04_exam_structure    : two-section AP exam layout card — Section I (MC,
                         105 min, 50%) and Section II (FRQ, 90 min, 50%),
                         with Part A / Part B calc-vs-no-calc breakdowns
- 12_calculator_hygiene: three-rule card (STORE intermediate values, 3+
                         decimals, SETUP integral before pressing button)
- 14_time_budget       : 90 / 6 = 15 min per FRQ, with the "easy parts of
                         every problem first" tactical guidance
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H, wrap,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Calculus AB", module_num=12,
            output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 12 — AP Exam Synthesis & Free-Response Strategy",
    "~10 minutes  ·  Capstone / Synthesis  ·  Exam-day playbook",
)


# ─── 02 — hook (custom: right math, wrong rubric) ───────────────────────
def hook(img, d):
    d.text((110, 80), "Right math.  Wrong rubric.",
           fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 178),
           "A true story from the AP Reading — three perfect answers, zero points.",
           fill=MUTED, font=font("sans", 34))

    # Three "zero-point" cards stacked
    card_y0 = 280
    card_h  = 200
    gap     = 30

    rows = [
        ("Part A", "Got the number right.",          "✗  Missing UNITS.",                     "−1 point"),
        ("Part B", "Got the number right.",          "✗  No 'BECAUSE' on the justification.", "−1 point"),
        ("Part C", "Got the calculator answer.",     "✗  No SETUP integral written.",         "−1 point"),
    ]

    for i, (lbl, did, missed, loss) in enumerate(rows):
        y = card_y0 + i * (card_h + gap)
        d.rounded_rectangle([110, y, W - 110, y + card_h], radius=20,
                            outline=MAROON, width=4, fill=deck.card_bg)
        # Left tag — "Part A / B / C"
        d.rounded_rectangle([130, y + 20, 290, y + card_h - 20], radius=14,
                            fill=MAROON)
        centered_tag_x = 210
        tag_text = lbl
        tw = d.textlength(tag_text, font=font("serif_bold", 44))
        d.text((centered_tag_x - tw / 2, y + 78), tag_text,
               fill=deck.accent_light, font=font("serif_bold", 44))
        # Middle — what student did
        d.text((330, y + 35), did, fill=INK, font=font("sans", 36))
        # Right — what they missed (in red)
        d.text((330, y + 100), missed, fill=RED, font=font("sans_bold", 38))
        # Loss tag on the far right
        loss_w = d.textlength(loss, font=font("serif_bold", 42))
        d.text((W - 130 - loss_w, y + 78), loss,
               fill=MAROON_DARK, font=font("serif_bold", 42))


deck.custom("02_hook", hook)


# ─── 03 — overview ──────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "How the exam is actually built — two sections, 50/50, calc vs. no-calc.",
        "The six FRQ patterns that show up every year.",
        "The rubric:  units, BECAUSE, setup integral, calculator hygiene, time.",
    ],
    footnote="No new calculus today.  Everything you already know — organized for the exam.",
)


# ─── 04 — exam structure (custom: two-section card) ─────────────────────
def exam_structure(img, d):
    d.text((110, 70), "The AP Calculus AB exam.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158),
           "Two sections.  3 hours 15 minutes total.  Each section = 50% of your score.",
           fill=MUTED, font=font("sans", 32))

    # LEFT card — Section I
    lx0, ly0 = 110, 240
    lx1, ly1 = 940, 940
    d.rounded_rectangle([lx0, ly0, lx1, ly1], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    # Title bar
    d.rounded_rectangle([lx0, ly0, lx1, ly0 + 90], radius=24, fill=MAROON)
    d.rectangle([lx0, ly0 + 60, lx1, ly0 + 90], fill=MAROON)
    centered_x = (lx0 + lx1) // 2
    s1_title = "SECTION I  —  Multiple Choice"
    tw = d.textlength(s1_title, font=font("serif_bold", 38))
    d.text((centered_x - tw / 2, ly0 + 22), s1_title,
           fill=deck.accent_light, font=font("serif_bold", 38))
    # Top-level stats
    d.text((lx0 + 40, ly0 + 130),
           "45 questions  ·  105 min  ·  50%",
           fill=MAROON_DARK, font=font("serif_bold", 42))

    # Part A box
    pa_y = ly0 + 230
    d.rounded_rectangle([lx0 + 30, pa_y, lx1 - 30, pa_y + 200], radius=16,
                        outline=MAROON_DARK, width=3, fill=deck.bg)
    d.text((lx0 + 50, pa_y + 20), "Part A",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((lx0 + 50, pa_y + 80), "30 questions  ·  60 min",
           fill=INK, font=font("sans", 32))
    d.text((lx0 + 50, pa_y + 130), "NO calculator",
           fill=RED, font=font("sans_bold", 34))

    # Part B box
    pb_y = pa_y + 230
    d.rounded_rectangle([lx0 + 30, pb_y, lx1 - 30, pb_y + 200], radius=16,
                        outline=MAROON_DARK, width=3, fill=deck.bg)
    d.text((lx0 + 50, pb_y + 20), "Part B",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((lx0 + 50, pb_y + 80), "15 questions  ·  45 min",
           fill=INK, font=font("sans", 32))
    d.text((lx0 + 50, pb_y + 130), "Calculator required",
           fill=MAROON_DARK, font=font("sans_bold", 34))

    # RIGHT card — Section II
    rx0, ry0 = 980, 240
    rx1, ry1 = W - 110, 940
    d.rounded_rectangle([rx0, ry0, rx1, ry1], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.rounded_rectangle([rx0, ry0, rx1, ry0 + 90], radius=24, fill=MAROON)
    d.rectangle([rx0, ry0 + 60, rx1, ry0 + 90], fill=MAROON)
    centered_rx = (rx0 + rx1) // 2
    s2_title = "SECTION II  —  Free Response"
    tw2 = d.textlength(s2_title, font=font("serif_bold", 38))
    d.text((centered_rx - tw2 / 2, ry0 + 22), s2_title,
           fill=deck.accent_light, font=font("serif_bold", 38))
    d.text((rx0 + 40, ry0 + 130),
           "6 questions  ·  90 min  ·  50%",
           fill=MAROON_DARK, font=font("serif_bold", 42))

    # Part A — FRQ
    pa2_y = ry0 + 230
    d.rounded_rectangle([rx0 + 30, pa2_y, rx1 - 30, pa2_y + 200], radius=16,
                        outline=MAROON_DARK, width=3, fill=deck.bg)
    d.text((rx0 + 50, pa2_y + 20), "Part A",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((rx0 + 50, pa2_y + 80), "2 questions  ·  30 min",
           fill=INK, font=font("sans", 32))
    d.text((rx0 + 50, pa2_y + 130), "Calculator required",
           fill=MAROON_DARK, font=font("sans_bold", 34))

    # Part B — FRQ
    pb2_y = pa2_y + 230
    d.rounded_rectangle([rx0 + 30, pb2_y, rx1 - 30, pb2_y + 200], radius=16,
                        outline=MAROON_DARK, width=3, fill=deck.bg)
    d.text((rx0 + 50, pb2_y + 20), "Part B",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((rx0 + 50, pb2_y + 80), "4 questions  ·  60 min",
           fill=INK, font=font("sans", 32))
    d.text((rx0 + 50, pb2_y + 130), "NO calculator",
           fill=RED, font=font("sans_bold", 34))


deck.custom("04_exam_structure", exam_structure)


# ─── 05 — the six FRQ patterns (overview) ───────────────────────────────
deck.overview(
    "05_frq_patterns", "The six FRQ patterns.",
    [
        "Rate in / rate out  (tank accumulation).",
        "Particle motion  (net displacement vs. total distance).",
        "Area & volume  (Modules 10 and 11).",
        "Table-based  (trapezoidal sum, MVT, IVT).",
        "Differential equation  (separable + slope field).",
        "Function defined by an integral  (g(x) = ∫ₐˣ f(t) dt).",
    ],
    footnote="First move on any FRQ:  name the pattern.",
)


# ─── 06 — rate in / rate out (equation) ─────────────────────────────────
deck.equation(
    "06_rate_in_out_example",
    "Pattern 1 — Rate in / rate out.",
    [
        ("R(t)  in,    S(t)  out,    V₀  initial.",      INK,    "set up the language first"),
        ("",                                              INK,    None),
        ("V(T)  =  V₀  +  ∫₀ᵀ ( R(t) − S(t) ) dt",       MAROON, "write the SETUP — even if calc does it"),
        ("",                                              INK,    None),
        ("Units:  gallons.    Always.",                   MAROON_DARK, "rate · time = amount"),
    ],
)


# ─── 07 — particle motion recall (equation) ─────────────────────────────
deck.equation(
    "07_particle_motion_recall",
    "Pattern 2 — Particle motion  (recall  v = t² − 4  on [0, 3]).",
    [
        ("Net displacement  =  ∫₀³ v(t) dt  =  −3",         INK,    "signed integral — can be negative"),
        ("Total distance    =  ∫₀³ |v(t)| dt  =  23/3",     MAROON, "always non-negative"),
        ("",                                                 INK,    None),
        ("Same trip.  Different question.",                  MAROON_DARK, "AP exam asks for BOTH in one problem"),
    ],
)


# ─── 08 — function defined by integral (definition) ─────────────────────
deck.definition(
    "08_function_defined_by_integral",
    "Pattern 6 — Function defined by an integral.",
    "g(x) = ∫ₐˣ f(t) dt   →   g'(x) = f(x)   (FTC Part 1)",
    "g has a maximum where f changes from +  to  − ,  "
    "BECAUSE  g' = f  and the sign change is from positive to negative.",
)


# ─── 09 — pause ─────────────────────────────────────────────────────────
deck.pause(
    "09_pause1", "PAUSE  &  TRY",
    "g(x) = ∫₀ˣ f(t) dt.   f > 0 on (0, 3),   f < 0 on (3, 5).",
    "Where is g's max on [0, 5] — and JUSTIFY.",
    hint="Use the word BECAUSE.  Cite the Fundamental Theorem.  "
         "Pause.  Write the sentence.  Press play when ready.",
)
deck.duplicate("09_pause1", "10_pause1_silence")


# ─── 11 — BECAUSE compare (wrong vs right justification) ────────────────
deck.compare(
    "11_because_compare",
    "The BECAUSE rule  —  same answer, only one earns the point.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "g has a max at x = 3.",
            "",
            "(true conclusion)",
            "(no reason given)",
            "(no theorem cited)",
        ],
        "footnote": "Zero points.  A claim is not a justification.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "g has a max at x = 3",
            "BECAUSE  g'(x) = f(x)  by FTC,",
            "and f changes from +",
            "to − at x = 3.",
            "",
        ],
        "footnote": "Full point.  Where + BECAUSE + theorem.",
    },
)


# ─── 12 — calculator hygiene (custom: 3-rule card) ──────────────────────
def calculator_hygiene(img, d):
    d.text((110, 70), "Calculator hygiene  —  three rules.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158),
           "On Section I Part B and Section II Part A only.  No-calc sections — these don't apply.",
           fill=MUTED, font=font("sans", 30))

    # Three big rule cards
    rules = [
        ("1.", "STORE  intermediate values.",
               "Press the  STO→  arrow.  Re-typing  0.732  loses digits  →  final answer is off."),
        ("2.", "Answers to ≥ 3 decimals.",
               "Two decimals = rounded.  AP grader marks it wrong.  Round only at the very end."),
        ("3.", "Always write the SETUP first.",
               "The integral, equation, or expression — before you press the button.  "
               "Calculator answer alone earns ZERO."),
    ]

    card_y0 = 250
    card_h  = 200
    gap     = 30

    for i, (n, head, sub) in enumerate(rules):
        y = card_y0 + i * (card_h + gap)
        d.rounded_rectangle([110, y, W - 110, y + card_h], radius=20,
                            outline=MAROON, width=4, fill=deck.card_bg)
        # Big numeral
        d.rounded_rectangle([130, y + 20, 250, y + card_h - 20], radius=14,
                            fill=MAROON)
        n_w = d.textlength(n, font=font("serif_bold", 80))
        d.text((190 - n_w / 2, y + 40), n,
               fill=deck.accent_light, font=font("serif_bold", 80))
        # Headline + subtext
        d.text((290, y + 30), head, fill=MAROON_DARK,
               font=font("serif_bold", 44))
        # Wrap the subtext
        sub_lines = wrap(d, sub, font("sans", 28), W - 110 - 290 - 40)
        sy = y + 100
        for line in sub_lines:
            d.text((290, sy), line, fill=INK, font=font("sans", 28))
            sy += 38


deck.custom("12_calculator_hygiene", calculator_hygiene)


# ─── 13 — units rule (definition) ───────────────────────────────────────
deck.definition(
    "13_units_rule",
    "Units.   Every applied FRQ answer.   Every time.",
    "gallons   ·   meters/sec   ·   dollars/day   ·   people",
    "Integral of a rate over time  =  ( units of f ) × ( units of t ).  "
    "One missing unit  =  one missing point.",
)


# ─── 14 — time budget (custom) ──────────────────────────────────────────
def time_budget(img, d):
    d.text((110, 70), "Time budget  —  Section II.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168),
           "90 minutes  ·  6 free response  ·  15 min per problem.",
           fill=MUTED, font=font("sans", 34))

    # Big arithmetic on the left
    eq_y = 290
    d.text((140, eq_y), "90 min", fill=MAROON_DARK,
           font=font("serif_bold", 96))
    d.text((140, eq_y + 130), "─────────  =  15 min / FRQ",
           fill=INK, font=font("mono", 60))
    d.text((140, eq_y + 260), "6 FRQs", fill=MAROON_DARK,
           font=font("serif_bold", 96))

    # Tactic card on the right
    tx0 = 1020
    d.rounded_rectangle([tx0, 270, W - 110, 880], radius=22,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((tx0 + 30, 290), "But — the real tactic:",
           fill=MAROON, font=font("serif_bold", 42))

    tactics = [
        ("✓", "Parts (a) and (b) of EVERY problem first.",
               "They're usually the easy entry points."),
        ("✓", "Then loop back for (c) and (d).",
               "The justification-heavy ones."),
        ("✓", "Circle every final answer.",
               "So the grader doesn't miss it."),
        ("✓", "2 min left?  Write a SETUP integral.",
               "Partial credit is real.  Setup alone often = 1 of 2 points."),
    ]
    ty = 380
    for chk, head, sub in tactics:
        d.text((tx0 + 30, ty), chk,
               fill=deck.accent, font=font("serif_bold", 40))
        d.text((tx0 + 80, ty), head, fill=MAROON_DARK,
               font=font("sans_bold", 28))
        d.text((tx0 + 80, ty + 42), sub, fill=MUTED,
               font=font("sans", 24))
        ty += 120


deck.custom("14_time_budget", time_budget)


# ─── 15 — recap ─────────────────────────────────────────────────────────
deck.recap(
    "15_recap", "Recap.",
    [
        "2 sections, 50/50.  FRQ:  Part A (2 q, calc, 30 min),  Part B (4 q, no-calc, 60 min).",
        "Six FRQ patterns — name the pattern first on any new problem.",
        "Always write the SETUP integral.",
        "Always include UNITS.",
        "Always use the word BECAUSE on justifications.",
        "Store intermediate values.  Final answer to ≥ 3 decimals.",
    ],
    assignment=[
        "This week:  one full released AP Calc AB FRQ set, timed (90 min).",
        "Submit through the GIIS dashboard.  Advisor scores against the official rubric.",
    ],
)


# ─── 16 — path (no next module — this IS the last) ─────────────────────
deck.path(
    "16_path",
    items=[
        ("✓",  "Watched this lesson",          "(done!)"),
        ("1.", "Download a released FRQ set",  "Recent AP Calculus AB — from The College Board's website"),
        ("2.", "Khan Academy practice course", "AP Calc AB — timed full multiple-choice sections"),
        ("3.", "GIIS advisor — mock exam",     "Book a full timed mock, scored against the official rubric"),
        ("4.", "Target your 3 weakest patterns","From the mock score sheet — final week of study"),
    ],
    next_text="Next up:  a real FRQ.  Real timer.  Real conditions.  Go earn the 5.",
)


print("AP Calc AB Module 12 slides built.")

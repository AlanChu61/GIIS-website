"""AP Psychology · Module 14 — Treatment of Psychological Disorders.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Direct sequel to Module 13 (Abnormal Psychology). Tone: hopeful, respectful.
Five major psychological approaches + biomedical treatments + effectiveness.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=14, output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 14 — Treatment of Psychological Disorders",
           "~7 minutes  ·  The 5 therapies + biomedical + does it work?")

# 02 — hook (hopeful pivot from Module 13)
def hook(img, d):
    d.text((110, 80), "Module 13:  what can go wrong.",
           fill=MUTED, font=font("serif", 52))
    d.text((110, 160), "Module 14:  100 years of figuring out what helps.",
           fill=MAROON, font=font("serif_bold", 56))

    # Big banner
    d.rounded_rectangle([110, 290, W-110, 540], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Therapy isn't soft pseudoscience anymore.",
             font("serif_bold", 56), 320, MAROON_DARK)
    centered(d, "CBT for depression has more empirical support",
             font("sans", 40), 410, INK)
    centered(d, "than most prescription drugs.",
             font("sans_bold", 42), 460, MAROON_DARK)

    # Three short cards
    items = [
        ("SSRIs",       "help millions every day"),
        ("Modern ECT",  "safe, controlled, often most effective for severe cases"),
        ("CBT",         "front-line for depression, anxiety, OCD, PTSD"),
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

    centered(d, "None of it is magic.   All of it is evidence.",
             font("serif_bold", 40), 870, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "The 5 major psychological therapies.",
    "Biomedical treatments — drugs, ECT, brief brain stimulation.",
    "Does any of this actually work? (Spoiler: yes.)",
], footnote="By end: read a session description, name the approach.")

# 04 — psychodynamic
def psychodynamic(img, d):
    d.text((110, 80), "1. Psychoanalytic / Psychodynamic.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 170), "Freud's heritage.  Make the unconscious conscious.",
           fill=MUTED, font=font("sans", 36))

    # Three technique cards stacked
    techs = [
        ("FREE ASSOCIATION",  "Person says whatever comes to mind, no filter.",
         "Therapist listens for patterns."),
        ("DREAM ANALYSIS",    "Dreams treated as a window into hidden conflicts.",
         "Symbols, recurring themes."),
        ("TRANSFERENCE",      "Person unconsciously treats therapist like an",
         "important figure from the past — that's the material."),
    ]
    for i, (name, l1, l2) in enumerate(techs):
        y = 270 + i * 200
        d.rounded_rectangle([110, y, W-110, y + 170], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((140, y + 20), name, fill=deck.accent, font=font("sans_bold", 40))
        d.text((140, y + 80), l1, fill=INK, font=font("sans", 32))
        d.text((140, y + 124), l2, fill=INK, font=font("sans", 32))

    d.text((110, 900), "Modern version:  shorter, more focused. Same core move.",
           fill=MAROON_DARK, font=font("sans_bold", 30))
deck.custom("04_psychodynamic", psychodynamic)

# 05 — behavioral
def behavioral(img, d):
    d.text((110, 80), "2. Behavioral therapy.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 170), "Forget the unconscious.  Behavior was learned — it can be unlearned.",
           fill=MUTED, font=font("sans", 32))

    # Two columns: classical / operant
    col_w = 870
    x_left = 110
    x_right = 110 + col_w + 50

    # Left column — Classical conditioning
    d.rounded_rectangle([x_left, 270, x_left + col_w, 880], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((x_left + 30, 290), "CLASSICAL-based", fill=deck.accent,
           font=font("sans_bold", 40))
    d.text((x_left + 30, 350), "(reflex / fear pairing)",
           fill=MUTED, font=font("sans", 28))
    bullets_left = [
        "• Systematic desensitization",
        "    pair feared thing with relaxation,",
        "    climb a fear hierarchy.",
        "",
        "• Exposure therapy",
        "    confront the feared situation,",
        "    no escape, brain learns it's safe.",
        "",
        "• Aversive conditioning",
        "    pair unwanted behavior",
        "    with something unpleasant.",
    ]
    for j, line in enumerate(bullets_left):
        d.text((x_left + 30, 420 + j * 40), line, fill=INK, font=font("sans", 28))

    # Right column — Operant conditioning
    d.rounded_rectangle([x_right, 270, x_right + col_w, 880], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((x_right + 30, 290), "OPERANT-based", fill=deck.accent,
           font=font("sans_bold", 40))
    d.text((x_right + 30, 350), "(consequences shape behavior)",
           fill=MUTED, font=font("sans", 28))
    bullets_right = [
        "• Token economies",
        "    earn tokens for desired behavior,",
        "    exchange for privileges.",
        "    (classrooms · inpatient units)",
        "",
        "• Behavior modification",
        "    reinforce target behavior,",
        "    extinguish problem behavior.",
        "",
        "Best for:  anxiety, phobias, OCD —",
        "fastest & most reliable.",
    ]
    for j, line in enumerate(bullets_right):
        d.text((x_right + 30, 420 + j * 40), line, fill=INK, font=font("sans", 28))
deck.custom("05_behavioral", behavioral)

# 06 — cognitive (with cognitive triad triangle)
def cognitive(img, d):
    d.text((110, 80), "3. Cognitive therapy.   Beck & Ellis.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 170), "It's not the event — it's how you interpret the event.",
           fill=MUTED, font=font("sans", 36))

    # Left side — example
    d.rounded_rectangle([110, 260, 880, 600], radius=18,
                        outline=deck.accent, width=4, fill=deck.card_bg)
    d.text((140, 285), "Friend doesn't text back.",
           fill=INK, font=font("serif_bold", 38))
    d.text((140, 365), "Person A:", fill=deck.accent, font=font("sans_bold", 32))
    d.text((140, 410), "  'They're busy.'", fill=INK, font=font("sans", 30))
    d.text((140, 480), "Person B:", fill=deck.accent, font=font("sans_bold", 32))
    d.text((140, 525), "  'They hate me. No one likes me.", fill=INK, font=font("sans", 30))
    d.text((140, 560), "   I'm worthless.'", fill=INK, font=font("sans", 30))

    # Right side — Beck's cognitive triad as triangle
    cx, cy = 1380, 480
    R = 230
    # Triangle vertices
    import math
    pts = []
    for k in range(3):
        ang = math.radians(-90 + k * 120)
        pts.append((cx + R * math.cos(ang), cy + R * math.sin(ang)))
    # Draw triangle outline
    d.line([pts[0], pts[1]], fill=MAROON, width=6)
    d.line([pts[1], pts[2]], fill=MAROON, width=6)
    d.line([pts[2], pts[0]], fill=MAROON, width=6)

    centered(d, "BECK'S COGNITIVE TRIAD",
             font("sans_bold", 36), 270, MAROON_DARK)
    centered(d, "(of depression)",
             font("sans", 28), 320, MUTED)

    # Vertex labels
    labels = [
        (pts[0][0], pts[0][1] - 90, "SELF",   "'I'm worthless.'"),
        (pts[1][0] + 30, pts[1][1] - 30, "WORLD",  "'Everything is unfair.'"),
        (pts[2][0] - 290, pts[2][1] - 30, "FUTURE", "'It'll never get better.'"),
    ]
    for lx, ly, name, quote in labels:
        d.rounded_rectangle([lx - 10, ly, lx + 270, ly + 90], radius=12,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((lx, ly + 6), name, fill=deck.accent, font=font("sans_bold", 30))
        d.text((lx, ly + 50), quote, fill=INK, font=font("sans", 24))

    # Vertex dots
    for px, py in pts:
        d.ellipse([px - 12, py - 12, px + 12, py + 12], fill=MAROON)

    # Bottom takeaway
    d.rounded_rectangle([110, 800, W-110, 920], radius=18, fill=deck.accent_light)
    centered(d, "Therapy work:  identify automatic thoughts → examine evidence → replace.",
             font("sans_bold", 32), 840, MAROON_DARK)
deck.custom("06_cognitive", cognitive)

# 07 — CBT
def cbt(img, d):
    d.text((110, 80), "4. Cognitive-Behavioral Therapy.   CBT.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 170), "The integration:  change thinking AND behavior, at once.",
           fill=MUTED, font=font("sans", 34))

    # Strongest evidence callout
    d.rounded_rectangle([110, 240, W-110, 360], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Most empirically-supported psychotherapy we have.",
             font("serif_bold", 40), 260, MAROON_DARK)
    centered(d, "Front-line for depression · anxiety · OCD · PTSD",
             font("sans_bold", 32), 320, MAROON_DARK)

    # Three tools
    tools = [
        ("THOUGHT RECORDS",
         "Log:  situation → automatic thought →",
         "emotion → balanced alternative."),
        ("BEHAVIORAL EXPERIMENTS",
         "Don't argue about whether the feared",
         "thing happens — go test it."),
        ("BEHAVIORAL ACTIVATION",
         "When depressed, person stops doing things.",
         "Re-schedule meaningful activities back in."),
    ]
    cw = 580
    for i, (name, l1, l2) in enumerate(tools):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 410, x + cw, 720], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 432), name, fill=deck.accent, font=font("sans_bold", 32))
        d.text((x + 24, 510), l1, fill=INK, font=font("sans", 26))
        d.text((x + 24, 550), l2, fill=INK, font=font("sans", 26))

    d.text((110, 770), "Structured.  Short — typically 12-20 sessions.  Homework-heavy.",
           fill=INK, font=font("sans", 32))
    d.text((110, 820), "If you remember one therapy from this module — remember CBT.",
           fill=MAROON, font=font("serif_bold", 38))
deck.custom("07_cbt", cbt)

# 08 — pause
deck.pause("08_pause1", "PAUSE  &  TRY",
           "A person seeking depression treatment keeps a daily log of: situation, automatic thought, emotion, balanced alternative.",
           "Which approach?  What's the tool?",
           hint="Pause. Decide. Press play.")

# 09 — pause answer
def pause_answer(img, d):
    d.text((110, 80), "The answer.",
           fill=MAROON, font=font("serif_bold", 76))

    # Two answer cards
    d.rounded_rectangle([110, 230, W-110, 410], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((140, 260), "APPROACH:", fill=deck.accent, font=font("sans_bold", 36))
    d.text((420, 256), "Cognitive-Behavioral Therapy  (CBT)",
           fill=INK, font=font("serif_bold", 44))
    d.text((140, 340), "TOOL:", fill=deck.accent, font=font("sans_bold", 36))
    d.text((420, 336), "Thought record",
           fill=INK, font=font("serif_bold", 44))

    # Why both
    d.rounded_rectangle([110, 460, W-110, 880], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Notice how it does BOTH jobs at once.",
             font("serif_bold", 48), 490, MAROON_DARK)

    d.rounded_rectangle([180, 580, 940, 820], radius=18,
                        fill=deck.card_bg, outline=deck.accent, width=4)
    d.text((210, 600), "COGNITIVE", fill=deck.accent, font=font("sans_bold", 36))
    d.text((210, 670), "Identify the automatic thought.",
           fill=INK, font=font("sans", 30))
    d.text((210, 720), "Challenge it with evidence.",
           fill=INK, font=font("sans", 30))
    d.text((210, 770), "Find a more balanced view.",
           fill=INK, font=font("sans", 30))

    d.rounded_rectangle([980, 580, 1740, 820], radius=18,
                        fill=deck.card_bg, outline=deck.accent, width=4)
    d.text((1010, 600), "BEHAVIORAL", fill=deck.accent, font=font("sans_bold", 36))
    d.text((1010, 670), "Build the active habit",
           fill=INK, font=font("sans", 30))
    d.text((1010, 720), "of doing it on paper,",
           fill=INK, font=font("sans", 30))
    d.text((1010, 770), "every single day.",
           fill=INK, font=font("sans", 30))
deck.custom("09_pause1_answer", pause_answer)

# 10 — humanistic
def humanistic(img, d):
    d.text((110, 80), "5. Humanistic therapy.   Rogers (& Maslow).",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 170), "People have an innate drive to grow.  Create the conditions.",
           fill=MUTED, font=font("sans", 32))

    # Three Rogerian conditions
    conds = [
        ("UNCONDITIONAL", "POSITIVE REGARD",
         "Person is accepted as they are.",
         "Not graded. Not judged."),
        ("GENUINENESS",   "(congruence)",
         "Therapist is real with the person.",
         "Not playing a role."),
        ("EMPATHY",       "(active listening)",
         "Trying to feel what",
         "the person is feeling."),
    ]
    cw = 580
    for i, (name1, name2, l1, l2) in enumerate(conds):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 270, x + cw, 600], radius=20,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 295), name1, fill=deck.accent, font=font("sans_bold", 36))
        d.text((x + 24, 345), name2, fill=deck.accent, font=font("sans_bold", 36))
        d.text((x + 24, 430), l1, fill=INK, font=font("sans", 30))
        d.text((x + 24, 475), l2, fill=INK, font=font("sans", 30))

    # Reflective listening callout
    d.rounded_rectangle([110, 660, W-110, 870], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Active technique:  REFLECTIVE LISTENING.",
             font("serif_bold", 44), 690, MAROON_DARK)
    centered(d, "Therapist mirrors back what the person said.",
             font("sans", 34), 760, INK)
    centered(d, "Sounds simple.  Powerful — person hears their own words.",
             font("sans_bold", 32), 810, MAROON_DARK)
deck.custom("10_humanistic", humanistic)

# 11 — biomedical (drug categories table + ECT/TMS panels)
def biomedical(img, d):
    d.text((110, 70), "6. Biomedical treatments.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 158), "When the brain is the problem, you change the brain.",
           fill=MUTED, font=font("sans", 30))

    # Drug categories table
    d.text((110, 220), "DRUG CATEGORIES", fill=deck.accent, font=font("sans_bold", 36))
    rows = [
        ("Antidepressants",   "SSRIs (e.g. fluoxetine)",  "raise serotonin → depression, anxiety, OCD"),
        ("Antipsychotics",    "block dopamine receptors", "schizophrenia (positive symptoms)"),
        ("Anxiolytics",       "benzodiazepines",          "short-term anxiety relief"),
        ("Mood stabilizers",  "lithium",                  "bipolar — smooths highs & lows"),
    ]
    # Header row
    y = 280
    d.rounded_rectangle([110, y, W-110, y + 60], radius=10, fill=MAROON)
    d.text((130, y + 12), "CATEGORY",     fill=deck.accent_light, font=font("sans_bold", 28))
    d.text((600, y + 12), "MAIN EXAMPLE", fill=deck.accent_light, font=font("sans_bold", 28))
    d.text((1100, y + 12), "USED FOR",    fill=deck.accent_light, font=font("sans_bold", 28))
    y += 60
    for i, (cat, ex, use) in enumerate(rows):
        bg = deck.card_bg if i % 2 == 0 else deck.bg
        d.rectangle([110, y, W-110, y + 70], fill=bg)
        d.text((130, y + 18), cat, fill=INK, font=font("sans_bold", 30))
        d.text((600, y + 18), ex,  fill=INK, font=font("sans", 28))
        d.text((1100, y + 18), use, fill=INK, font=font("sans", 28))
        y += 70
    # Border around the whole table
    d.rectangle([110, 280, W-110, y], outline=deck.accent, width=3)

    # Below — ECT and TMS callouts
    panel_y = 700
    # ECT
    d.rounded_rectangle([110, panel_y, 940, panel_y + 200], radius=18,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((140, panel_y + 18), "ECT — Electroconvulsive Therapy",
           fill=MAROON, font=font("sans_bold", 32))
    d.text((140, panel_y + 75), "Severe, treatment-resistant depression.",
           fill=INK, font=font("sans", 26))
    d.text((140, panel_y + 115), "Done under anesthesia + muscle relaxants.",
           fill=INK, font=font("sans", 26))
    d.text((140, panel_y + 155), "Modern version is safe & effective.",
           fill=deck.accent, font=font("sans_bold", 26))
    # TMS / psychosurgery
    d.rounded_rectangle([980, panel_y, W-110, panel_y + 200], radius=18,
                        outline=deck.accent, width=4, fill=deck.card_bg)
    d.text((1010, panel_y + 18), "TMS  &  psychosurgery",
           fill=deck.accent, font=font("sans_bold", 32))
    d.text((1010, panel_y + 75), "TMS — magnetic pulses stimulate brain regions.",
           fill=INK, font=font("sans", 26))
    d.text((1010, panel_y + 115), "No anesthesia needed.",
           fill=INK, font=font("sans", 26))
    d.text((1010, panel_y + 155), "Lobotomies = essentially never done today.",
           fill=MUTED, font=font("sans", 26))
deck.custom("11_biomedical", biomedical)

# 12 — effectiveness (compare therapy vs no-treatment + common factors)
deck.compare("12_effectiveness", "Does any of this actually work?  Yes.",
    {"label": "WITH therapy",
     "color": deck.accent,
     "lines": [
         "~75% show meaningful",
         "improvement.",
         "",
         "CBT has strongest evidence",
         "for depression & anxiety.",
         "",
         "Therapy + meds usually beats",
         "either alone (moderate-severe).",
     ],
     "footnote": "Meta-analyses across hundreds of studies."},
    {"label": "WITHOUT treatment",
     "color": MUTED,
     "lines": [
         "~35% improve on their own",
         "(spontaneous remission).",
         "",
         "Many stay stuck — or get worse.",
         "",
         "Common factors across",
         "approaches:  alliance · hope ·",
         "working through · learned-",
         "helplessness reversal.",
     ],
     "footnote": "Therapeutic alliance predicts outcome more than technique."})

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Psychodynamic — unconscious work · free association · dreams · transference.",
    "Behavioral — relearn responses · desensitization · exposure · token economies.",
    "Cognitive — Beck's triad · self / world / future · restructure thoughts.",
    "CBT — front-line for depression, anxiety, OCD, PTSD. Thought records · experiments.",
    "Humanistic (Rogers) — unconditional positive regard · genuineness · empathy.",
    "Biomedical — SSRIs · antipsychotics · anxiolytics · lithium · modern ECT.",
])

# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",                "(done!)"),
    ("1.", "Read Myers Module 14",             "Therapy + biomedical treatment"),
    ("2.", "AP Classroom · 15 MCQ",            "Identify approach from a session description"),
    ("3.", "Assignment in dashboard",          "Label 6 therapy vignettes with the matching approach"),
    ("4.", "Advisor check-in",                 "If techniques blur — they blur for everyone first time"),
], next_text="Next up:  Module 15 — Treatment, Advanced Applications. Specific cases, group & family therapy, matching the treatment to the person.")

print("AP Psych Module 14 slides built.")

"""AP Psychology · Module 15 — Treatment, Advanced Applications.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Sequel to Module 14. Tone: HS teacher with personality — respectful on cases.
Disorder→treatment matrix · 3 case-study cards · group / family / individual
comparison · pause-and-try.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=15,
            output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 15 — Treatment: Advanced Applications",
           "~8 minutes  ·  Matching the right treatment to the right person")

# 02 — hook (toolbox → choosing the right tool)
def hook(img, d):
    d.text((110, 80), "Last module:  the toolbox.",
           fill=MUTED, font=font("serif", 50))
    d.text((110, 158), "Today:  choose the right tool for the right problem.",
           fill=MAROON, font=font("serif_bold", 54))

    # Big banner
    d.rounded_rectangle([110, 290, W-110, 540], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Treatment isn't one-size-fits-all.",
             font("serif_bold", 56), 320, MAROON_DARK)
    centered(d, "It's a match. Match the disorder. Match the person.",
             font("sans", 38), 410, INK)
    centered(d, "Match the culture, the age, the family.",
             font("sans_bold", 38), 460, MAROON_DARK)

    # Three "doesn't work" cards
    items = [
        ("PTSD",      "→ Freudian couch + 50-year-old theory?", "doesn't work."),
        ("Schizophrenia", "→ thought records alone?",            "doesn't work."),
        ("Phobia",     "→ years of dream analysis?",             "doesn't work."),
    ]
    cw = 580
    for i, (cat, line1, line2) in enumerate(items):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 600, x + cw, 800], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 622), cat, fill=deck.accent, font=font("sans_bold", 38))
        d.text((x + 24, 690), line1, fill=INK, font=font("sans", 26))
        d.text((x + 24, 740), line2, fill=MAROON, font=font("sans_bold", 30))

    centered(d, "Match the treatment to the person.   That's the whole game.",
             font("serif_bold", 38), 870, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Disorder → first-line treatment matrix (what the evidence says).",
    "Three case studies — read the presentation, pick the treatment.",
    "Group, family, cultural fit, and special notes for kids & teens.",
], footnote="By end: read a vignette, explain why one treatment fits better than another.")

# 04 — match disorder (matrix table)
def match_disorder(img, d):
    d.text((110, 70), "Disorder  →  first-line treatment.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 156), "What the evidence base actually says.",
           fill=MUTED, font=font("sans", 30))

    rows = [
        ("Anxiety / Phobias",          "Behavioral — exposure, systematic desensitization"),
        ("Depression",                 "CBT (mild-mod)  ·  CBT + SSRI (mod-severe)"),
        ("OCD",                        "CBT with ERP (exposure + response prevention)  ·  SSRI"),
        ("PTSD",                       "Trauma-focused CBT  ·  EMDR  ·  prolonged exposure"),
        ("Schizophrenia",              "Antipsychotic medication PRIMARY  ·  family education"),
        ("Bipolar disorder",           "Mood stabilizer (lithium)  ·  therapy for psychosocial support"),
        ("Borderline personality",     "DBT — dialectical behavior therapy"),
    ]
    # Header row
    y0 = 220
    d.rounded_rectangle([110, y0, W-110, y0 + 60], radius=10, fill=MAROON)
    d.text((140, y0 + 12), "DISORDER",
           fill=deck.accent_light, font=font("sans_bold", 30))
    d.text((780, y0 + 12), "FRONT-LINE TREATMENT",
           fill=deck.accent_light, font=font("sans_bold", 30))
    y = y0 + 60
    row_h = 78
    for i, (disorder, treatment) in enumerate(rows):
        bg = deck.card_bg if i % 2 == 0 else deck.bg
        d.rectangle([110, y, W-110, y + row_h], fill=bg)
        d.text((140, y + 22), disorder, fill=INK, font=font("sans_bold", 30))
        d.text((780, y + 22), treatment, fill=INK, font=font("sans", 28))
        y += row_h
    # Border around the whole table
    d.rectangle([110, y0, W-110, y], outline=deck.accent, width=3)

    # Pattern callout at the bottom
    d.rounded_rectangle([110, y + 30, W-110, y + 180], radius=18,
                        fill=deck.accent_light, outline=MAROON, width=4)
    centered(d, "Pattern:  anxiety-spectrum  →  behavioral / cognitive lead.",
             font("sans_bold", 32), y + 60, MAROON_DARK)
    centered(d, "Psychotic & severe mood  →  medication leads, therapy supports.",
             font("sans_bold", 32), y + 110, MAROON_DARK)
deck.custom("04_match_disorder", match_disorder)

# ── helper for case study cards ──────────────────────────────────────
def _case_card(d, title, age_label, presentation, recommendation, why):
    """Three-section case card: presentation → recommendation → why."""
    # Header band
    d.rounded_rectangle([110, 80, W-110, 200], radius=18, fill=MAROON)
    d.text((140, 105), title, fill=deck.accent_light, font=font("serif_bold", 56))
    d.text((W - 110 - 380, 130), age_label, fill=deck.accent_light,
           font=font("sans", 32))

    # Section 1 — Presentation
    y = 240
    d.rounded_rectangle([110, y, W-110, y + 240], radius=18,
                        outline=deck.accent, width=4, fill=deck.card_bg)
    d.text((140, y + 16), "PRESENTATION",
           fill=deck.accent, font=font("sans_bold", 32))
    f_b = font("sans", 30)
    plines = wrap(d, presentation, f_b, W - 320)
    for i, ln in enumerate(plines[:5]):
        d.text((140, y + 70 + i * 38), ln, fill=INK, font=f_b)

    # Section 2 — Recommendation
    y = 500
    d.rounded_rectangle([110, y, W-110, y + 220], radius=18,
                        outline=MAROON, width=5, fill=deck.accent_light)
    d.text((140, y + 16), "RECOMMENDED TREATMENT",
           fill=MAROON, font=font("sans_bold", 32))
    rlines = wrap(d, recommendation, f_b, W - 320)
    for i, ln in enumerate(rlines[:4]):
        d.text((140, y + 70 + i * 38), ln, fill=MAROON_DARK,
               font=font("sans_bold", 30))

    # Section 3 — Why this works
    y = 740
    d.rounded_rectangle([110, y, W-110, y + 200], radius=18,
                        outline=deck.accent, width=3, fill=deck.card_bg)
    d.text((140, y + 16), "WHY IT WORKS",
           fill=deck.accent, font=font("sans_bold", 32))
    wlines = wrap(d, why, f_b, W - 320)
    for i, ln in enumerate(wlines[:3]):
        d.text((140, y + 70 + i * 38), ln, fill=INK, font=f_b)

# 05 — case anxiety
def case_anxiety(img, d):
    _case_card(d,
        "Case 1 — Maya",
        "hypothetical, age 17",
        "Escalating fear of dogs since a bite at age 9. School & friends fine. Now refuses routes where dogs may be off-leash. Recent panic episode.",
        "Systematic desensitization / graduated exposure. Build a fear hierarchy. Pair each step with relaxation. ~8-12 sessions. No medication usually needed.",
        "Original fear was learned via classical conditioning. Treatment uses the same learning system to teach a new association: dog = safe.")
deck.custom("05_case_anxiety", case_anxiety)

# 06 — case depression
def case_depression(img, d):
    _case_card(d,
        "Case 2 — Jordan",
        "hypothetical, age 16",
        "Won't get out of bed. Lost interest in soccer. Sleeping 12 hr/day. 6 weeks of low mood, low energy, feeling worthless. Grades slipping.",
        "CBT or interpersonal therapy first. Heavy on behavioral activation + thought records. SSRI (fluoxetine) added if therapy alone insufficient or symptoms severe.",
        "CBT + behavioral activation has the strongest adolescent evidence. Family involved. Most adolescents with depression recover fully when treated. Path back exists.")
deck.custom("06_case_depression", case_depression)

# 07 — case ocd
def case_ocd(img, d):
    _case_card(d,
        "Case 3 — Alex",
        "hypothetical, age 18",
        "College freshman. Intrusive thoughts of contamination. Washes hands 40+ times a day; hands cracked. 2 hours nightly cleaning the room before sleep.",
        "Exposure & Response Prevention (ERP). Gradually expose to triggers; prevent the compulsion. SSRI as adjunct, often higher dose than for depression.",
        "ERP teaches the brain that the feared catastrophe doesn't happen. Hard work, counterintuitive at first — but quality of life can change in months.")
deck.custom("07_case_ocd", case_ocd)

# 08 — pause + try (PTSD vignette)
deck.pause("08_pause1", "PAUSE  &  TRY",
           "College sophomore — flashbacks, nightmares, severe distress at fireworks since a violent incident last summer. Avoids the area. Hypervigilant, irritable.",
           "Disorder?   Front-line treatment?",
           hint="Pause. Decide. Press play.")

# 09 — pause answer
def pause_answer(img, d):
    d.text((110, 80), "The answer.",
           fill=MAROON, font=font("serif_bold", 76))

    # Diagnosis card
    d.rounded_rectangle([110, 220, W-110, 380], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((140, 250), "DISORDER:", fill=deck.accent, font=font("sans_bold", 36))
    d.text((420, 246), "Post-Traumatic Stress Disorder  (PTSD)",
           fill=INK, font=font("serif_bold", 44))
    d.text((140, 320), "Tip:", fill=MUTED, font=font("sans_bold", 28))
    d.text((230, 318), "flashbacks · avoidance · hyperarousal AFTER trauma.",
           fill=INK, font=font("sans", 30))

    # Three treatment options
    d.rounded_rectangle([110, 420, W-110, 470], radius=10, fill=MAROON)
    centered(d, "FRONT-LINE TREATMENTS",
             font("sans_bold", 32), 428, deck.accent_light)
    treatments = [
        ("Trauma-focused CBT",
         "Reprocess the memory in a safe, structured frame."),
        ("EMDR",
         "Eye-movement desensitization & reprocessing."),
        ("Prolonged exposure",
         "Repeatedly approach the memory until it loses charge."),
    ]
    cw = 580
    for i, (name, sub) in enumerate(treatments):
        x = 110 + i * (cw + 20)
        d.rounded_rectangle([x, 500, x + cw, 760], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, 524), name, fill=deck.accent,
               font=font("sans_bold", 34))
        lines = wrap(d, sub, font("sans", 28), cw - 48)
        for j, ln in enumerate(lines[:5]):
            d.text((x + 24, 600 + j * 40), ln, fill=INK, font=font("sans", 28))

    # Closing pattern note
    d.rounded_rectangle([110, 800, W-110, 920], radius=18,
                        fill=deck.accent_light, outline=MAROON, width=4)
    centered(d, "Pattern:  identify disorder  →  match evidence-based treatment  →  adjust for person.",
             font("sans_bold", 30), 845, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# 10 — group / family / individual comparison (3-column)
def group_family_individual(img, d):
    d.text((110, 70), "Group  ·  family  ·  individual.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Different formats solve different problems.",
           fill=MUTED, font=font("sans", 32))

    columns = [
        {
            "name": "INDIVIDUAL",
            "sub":  "(one-on-one)",
            "lines": [
                "Deep, private work.",
                "Focused on one person's",
                "history & goals.",
                "",
                "Best for:  most disorders",
                "as the foundation.",
                "Higher cost / hour.",
            ],
            "footnote": "The default mode.",
        },
        {
            "name": "GROUP",
            "sub":  "(several with shared issue)",
            "lines": [
                "Shared experience.",
                "Normalization — you're",
                "not the only one.",
                "Peer feedback. Lower cost.",
                "",
                "Best for:  substance abuse,",
                "social anxiety, grief.",
            ],
            "footnote": "Complement, not always a substitute.",
        },
        {
            "name": "FAMILY  /  COUPLES",
            "sub":  "(systemic)",
            "lines": [
                "Treats the system,",
                "not just the person.",
                "Boundaries · hierarchy ·",
                "communication patterns.",
                "",
                "Best for:  teen behavior issues,",
                "marital conflict, family stress.",
            ],
            "footnote": "Symptom may express system tension.",
        },
    ]

    cw = 580
    for i, col in enumerate(columns):
        x = 110 + i * (cw + 20)
        # Card
        d.rounded_rectangle([x, 240, x + cw, 870], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        # Header band
        d.rounded_rectangle([x, 240, x + cw, 340], radius=20, fill=deck.accent)
        d.text((x + 24, 258), col["name"], fill=deck.card_bg,
               font=font("sans_bold", 36))
        d.text((x + 24, 305), col["sub"], fill=deck.accent_light,
               font=font("sans", 26))
        # Body lines
        f_b = font("sans", 28)
        for j, ln in enumerate(col["lines"]):
            d.text((x + 24, 370 + j * 42), ln, fill=INK, font=f_b)
        # Footnote
        d.text((x + 24, 820), col["footnote"], fill=MUTED, font=font("sans", 24))
deck.custom("10_group", group_family_individual)

# 11 — family / couples — systemic spotlight
def family_systemic(img, d):
    d.text((110, 80), "When the family IS the case.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 170), "Systemic insight — symptom may be the visible part of system tension.",
           fill=MUTED, font=font("sans", 30))

    # Big visual: "patient" central, with arrows to family roles
    d.rounded_rectangle([110, 260, W-110, 600], radius=24,
                        outline=deck.accent, width=4, fill=deck.card_bg)

    # Center node — "the kid showing the symptom"
    cx, cy = 960, 430
    d.ellipse([cx-110, cy-110, cx+110, cy+110], outline=MAROON, width=6,
              fill=deck.accent_light)
    centered_block_x = cx - 60
    d.text((centered_block_x - 25, cy - 30), "TEEN", fill=MAROON_DARK,
           font=font("sans_bold", 36))
    d.text((centered_block_x - 30, cy + 20), "(symptom)", fill=MAROON_DARK,
           font=font("sans", 22))

    # Surrounding family role nodes
    nodes = [
        (cx - 600, cy,       "PARENT A",    "withdrawn"),
        (cx + 600, cy,       "PARENT B",    "over-involved"),
        (cx - 350, cy - 130, "SIBLING",     "high achiever"),
        (cx + 350, cy + 130, "GRANDPARENT", "boundary-blurring"),
    ]
    for nx, ny, label, sub in nodes:
        d.rounded_rectangle([nx-130, ny-50, nx+130, ny+50], radius=16,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((nx-115, ny-30), label, fill=deck.accent,
               font=font("sans_bold", 26))
        d.text((nx-115, ny+5), sub, fill=INK, font=font("sans", 22))
        # Arrow line toward the center
        d.line([(nx, ny), (cx, cy)], fill=MUTED, width=3)

    # Bottom takeaways
    d.rounded_rectangle([110, 660, W-110, 940], radius=22,
                        fill=deck.accent_light, outline=MAROON, width=5)
    d.text((150, 690), "STRUCTURAL FAMILY THERAPY",
           fill=MAROON_DARK, font=font("sans_bold", 38))
    d.text((150, 760), "→ examines boundaries · hierarchy · roles · who's enmeshed",
           fill=INK, font=font("sans", 30))
    d.text((150, 810), "→ couples therapy similarly:  the relationship is the patient",
           fill=INK, font=font("sans", 30))
    d.text((150, 870), "Treating only the individual when the system is the cause →",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((150, 905), "bailing out a boat without fixing the leak.",
           fill=MAROON_DARK, font=font("sans_bold", 28))
deck.custom("11_family", family_systemic)

# 12 — cultural + youth
def cultural_youth(img, d):
    d.text((110, 70), "Culture  ·  children & adolescents.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 156), "One-size-fits-all therapy is bad therapy.",
           fill=MUTED, font=font("sans", 32))

    # Two big columns
    # ── Cultural considerations ──
    d.rounded_rectangle([110, 230, 935, 880], radius=22,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.rounded_rectangle([110, 230, 935, 320], radius=22, fill=deck.accent)
    d.text((140, 252), "CULTURAL FIT", fill=deck.card_bg,
           font=font("sans_bold", 42))
    bullets_l = [
        "Therapist needs cultural",
        "competence — not optional.",
        "",
        "Trust gaps are real.  Some",
        "communities have very good",
        "historical reasons to be wary.",
        "",
        "Language access matters.",
        "Stigma varies by culture.",
        "",
        "Skilled therapist adapts:",
        "pace · style · framing ·",
        "family involvement.",
    ]
    f_b = font("sans", 28)
    for i, ln in enumerate(bullets_l):
        d.text((140, 350 + i * 38), ln, fill=INK, font=f_b)

    # ── Children & adolescents ──
    d.rounded_rectangle([985, 230, W-110, 880], radius=22,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.rounded_rectangle([985, 230, W-110, 320], radius=22, fill=deck.accent)
    d.text((1015, 252), "CHILDREN & TEENS", fill=deck.card_bg,
           font=font("sans_bold", 42))
    bullets_r = [
        "Younger kids → play therapy,",
        "art therapy.  Non-verbal way",
        "to express what words can't.",
        "",
        "Family involvement is essential —",
        "kids don't exist in isolation.",
        "",
        "SSRIs in teens →  FDA black-box",
        "warning re: early-treatment",
        "suicidality risk.  Still used —",
        "but with very close monitoring",
        "in the first weeks.",
        "",
        "Therapy first.  Med carefully second.",
    ]
    for i, ln in enumerate(bullets_r):
        d.text((1015, 350 + i * 38), ln, fill=INK, font=f_b)
deck.custom("12_cultural_youth", cultural_youth)

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Anxiety / phobias → behavioral (exposure, systematic desensitization).",
    "Depression → CBT;  add SSRI for moderate-severe.   OCD → ERP + SSRI.   PTSD → TF-CBT, EMDR, prolonged exposure.",
    "Schizophrenia → antipsychotics PRIMARY.   Bipolar → mood stabilizer.   Borderline → DBT.",
    "Group therapy normalizes & lowers cost.   Family / couples therapy treats the system.",
    "Cultural competence is required.   Kids → play therapy, family involvement, careful SSRI monitoring.",
    "Whole game:  match treatment to disorder, to person, to context.",
])

# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",                "(done!)"),
    ("1.", "Read Myers Module 15",             "Treatment matching · group · family · cultural · youth"),
    ("2.", "AP Classroom · 15 MCQ",            "Read a case → pick the best treatment"),
    ("3.", "Assignment in dashboard",          "6 vignettes — match treatment + 1-sentence rationale"),
    ("4.", "Advisor check-in",                 "If disorder-treatment pairings blur, book a session"),
], next_text="Next up:  Module 16 — Synthesis & AP exam strategy. Tying it all together + crushing the FRQs.")

print("AP Psych Module 15 slides built.")

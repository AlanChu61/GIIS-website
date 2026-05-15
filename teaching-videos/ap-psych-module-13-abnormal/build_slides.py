"""AP Psychology · Module 13 — Abnormal Psychology.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Sensitive topic — keep tone respectful, normalize seeking help, no sensationalism.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=13, output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 13 — Abnormal Psychology",
           "~8 minutes  ·  How psychologists define disorder + the major categories")

# 02 — hook (1-in-5 stat, normalize)
def hook(img, d):
    d.text((110, 80), "Look around your classroom.", fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 172), "Roughly 1 in 5 adults meet criteria for a disorder this year.",
           fill=MAROON_DARK, font=font("serif", 40))

    # Big visual: 5 person icons, 1 highlighted
    icon_y = 360
    spacing = 280
    start_x = (W - (5 * spacing - 80)) // 2
    for i in range(5):
        cx = start_x + i * spacing + 100
        is_one = (i == 2)  # middle person highlighted
        body_color = deck.accent if is_one else deck.card_bg
        body_outline = deck.accent if is_one else MUTED
        # head
        d.ellipse([cx - 50, icon_y, cx + 50, icon_y + 100],
                  fill=body_color, outline=body_outline, width=4)
        # shoulders/torso
        d.rounded_rectangle([cx - 80, icon_y + 110, cx + 80, icon_y + 240],
                            radius=24, fill=body_color, outline=body_outline, width=4)
        # caption under
        cap = "1 in 5" if is_one else ""
        if cap:
            tw = d.textlength(cap, font=font("sans_bold", 32))
            d.text((cx - tw / 2, icon_y + 260), cap, fill=deck.accent,
                   font=font("sans_bold", 32))

    # Bottom callout — normalize
    d.rounded_rectangle([110, 720, W - 110, 920], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Common.   Treatable.   Not shameful.",
             font("serif_bold", 56), 760, MAROON_DARK)
    centered(d, "Today: how psychologists draw the line — and what they look for.",
             font("sans", 36), 850, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "How we define abnormal — the 4 D's.",
    "DSM-5 framework + the major categories of disorders.",
    "Diathesis-stress: why same risk, different outcomes.",
], footnote="By end: read symptoms, place them in the right category.")

# 04 — the 4 D's as 4 cards
def four_ds(img, d):
    d.text((110, 80), "What makes a behavior \"abnormal\"?", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 172), "Psychologists ask 4 questions. None alone is enough.",
           fill=MUTED, font=font("sans", 34))

    cards = [
        ("DEVIANCE",   "Statistically rare or violates social norms.",
                       "Unusual is not always disorder."),
        ("DISTRESS",   "The person feels significant emotional pain.",
                       "Sadness alone is not disorder."),
        ("DYSFUNCTION","Interferes with daily life — work, school, relationships.",
                       "Can't function = closer to disorder."),
        ("DANGER",     "Risk of harm to self or others.",
                       "Most disorders involve no danger."),
    ]
    cw, ch = 870, 320
    for i, (name, defn, sub) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = 110 + col * (cw + 20)
        y = 280 + row * (ch + 20)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, y + 24), name, fill=deck.accent, font=font("sans_bold", 48))
        # def line, wrapped
        f_def = font("sans", 30)
        lines = wrap(d, defn, f_def, cw - 60)
        for j, ln in enumerate(lines[:3]):
            d.text((x + 30, y + 110 + j * 42), ln, fill=INK, font=f_def)
        d.text((x + 30, y + ch - 70), sub, fill=MUTED, font=font("serif_ital", 28))

    centered(d, "Multiple D's together = clinicians may diagnose.",
             font("serif_bold", 36), 945, MAROON_DARK)
deck.custom("04_four_ds", four_ds)

# 05 — DSM
def dsm(img, d):
    d.text((110, 80), "The diagnostic playbook.", fill=MAROON, font=font("serif_bold", 70))

    # Main DSM-5 callout
    d.rounded_rectangle([110, 220, W - 110, 470], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=6)
    centered(d, "DSM-5", font("serif_bold", 160), 230, MAROON)
    centered(d, "Diagnostic and Statistical Manual of Mental Disorders, 5th ed.",
             font("sans_bold", 34), 410, MAROON_DARK)

    d.text((110, 510), "U.S. standard.   Internationally:  ICD-11  (broadly similar).",
           fill=INK, font=font("sans", 36))

    # Key AP point
    d.rounded_rectangle([110, 600, W - 110, 870], radius=24, fill=deck.card_bg,
                        outline=deck.accent, width=5)
    d.text((150, 630), "Critical AP point:", fill=deck.accent, font=font("sans_bold", 38))
    d.text((150, 700), "DSM is DESCRIPTIVE.", fill=INK, font=font("serif_bold", 44))
    d.text((150, 760), "It tells you what a disorder looks like —", fill=INK, font=font("sans", 32))
    d.text((150, 805), "but NOT what causes it, and NOT how to treat it.", fill=INK, font=font("sans", 32))
deck.custom("05_dsm", dsm)

# 06 — anxiety, OCD, trauma
def anxiety_ocd(img, d):
    d.text((110, 70), "Anxiety  ·  OCD  ·  Trauma.", fill=MAROON, font=font("serif_bold", 62))
    d.text((110, 158), "Excess fear, intrusive thoughts, and post-trauma response.",
           fill=MUTED, font=font("sans", 32))

    sections = [
        ("ANXIETY", [
            "GAD — chronic worry",
            "Panic disorder — sudden attacks",
            "Phobias — specific  ·  social",
        ]),
        ("OCD  (own DSM-5 category)", [
            "Obsessions — intrusive thoughts",
            "Compulsions — repeat to relieve",
            "Washing · checking · counting",
        ]),
        ("TRAUMA", [
            "PTSD — re-experiencing event",
            "Flashbacks  ·  nightmares",
            "Hyperarousal",
        ]),
    ]
    cw = 580
    for i, (name, lines) in enumerate(sections):
        x = 110 + i * (cw + 20)
        y = 250
        d.rounded_rectangle([x, y, x + cw, y + 600], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 24, y + 24), name, fill=deck.accent, font=font("sans_bold", 30))
        for j, ln in enumerate(lines):
            # Use smaller font and wrap if needed
            f_ln = font("sans", 26)
            wrapped = wrap(d, "·  " + ln, f_ln, cw - 60)
            for k, wl in enumerate(wrapped[:2]):
                d.text((x + 24, y + 130 + j * 90 + k * 32), wl, fill=INK, font=f_ln)
deck.custom("06_anxiety_ocd", anxiety_ocd)

# 07 — mood disorders
def mood(img, d):
    d.text((110, 80), "Mood disorders.", fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 172), "Persistent disruptions of emotional state. Treatable.",
           fill=MUTED, font=font("sans", 34))

    rows = [
        ("Major Depressive Disorder",
         "≥2 weeks of persistent sadness, loss of interest, low energy, sleep & appetite changes."),
        ("Persistent Depressive Disorder",
         "Milder but longer — ≥2 years of low mood."),
        ("Bipolar I",
         "Full manic episodes (racing thoughts, no sleep, risky behavior) + depression."),
        ("Bipolar II",
         "Hypomania (milder elevation) + depressive episodes."),
    ]
    for i, (name, body) in enumerate(rows):
        y = 280 + i * 150
        d.rounded_rectangle([110, y, W - 110, y + 130], radius=18,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((140, y + 18), name, fill=deck.accent, font=font("sans_bold", 36))
        # body wrap
        f_b = font("sans", 30)
        lines = wrap(d, body, f_b, W - 320)
        for j, ln in enumerate(lines[:2]):
            d.text((140, y + 65 + j * 36), ln, fill=INK, font=f_b)

    d.rounded_rectangle([110, 920, W - 110, 1000], radius=16, fill=deck.accent_light)
    centered(d, "Therapy + medication change lives.  Recovery is the expected outcome.",
             font("sans_bold", 32), 942, MAROON_DARK)
deck.custom("07_mood", mood)

# 08 — pause (custom — long case prompt needs wrapping)
def pause1(img, d):
    # banner
    d.rectangle([0, 80, W, 220], fill=deck.accent)
    centered(d, "PAUSE  &  TRY", font("serif_bold", 96), 100, MAROON_DARK)

    # case description, wrapped
    f_p = font("sans", 38)
    case = ("A college student has felt deeply sad for 3 weeks. She has stopped going to "
            "class, can't get out of bed, and has lost interest in things she loved. "
            "She is not in danger of harming herself.")
    lines = wrap(d, case, f_p, W - 220)
    y = 280
    for ln in lines:
        d.text((110, y), ln, fill=INK, font=f_p)
        y += 52

    # questions, centered, big but fits
    f_q = font("sans_bold", 56)
    q_y = y + 60
    centered(d, "Which D's are present?", f_q, q_y, MAROON)
    centered(d, "Which DSM category?",     f_q, q_y + 80, MAROON)

    # hint
    d.text((110, 940), "Pause. Decide. Press play.", fill=MUTED, font=font("sans", 36))
deck.custom("08_pause1", pause1)

# 09 — pause answer (custom)
def pause_answer(img, d):
    d.text((110, 70), "The answer.", fill=MAROON, font=font("serif_bold", 70))

    # Three D's present
    d.text((110, 180), "Three D's are clearly present:",
           fill=MUTED, font=font("sans", 34))
    items = [
        ("DISTRESS",    "she feels deep sadness."),
        ("DYSFUNCTION", "can't attend class, can't function day-to-day."),
        ("DEVIANCE",    "significant departure from her usual baseline."),
    ]
    for i, (name, body) in enumerate(items):
        y = 250 + i * 90
        d.rounded_rectangle([110, y, W - 110, y + 70], radius=14,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((140, y + 16), name, fill=deck.accent, font=font("sans_bold", 36))
        d.text((460, y + 18), body, fill=INK, font=font("sans", 32))

    # Danger note
    d.text((110, 540), "Danger is NOT present  —  and that's fine. You don't need all 4.",
           fill=MUTED, font=font("serif_ital", 30))

    # Category
    d.rounded_rectangle([110, 610, W - 110, 880], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "DSM category:  Mood disorders.",
             font("serif_bold", 50), 640, MAROON_DARK)
    centered(d, "Specifically — Major Depressive Disorder.",
             font("sans_bold", 38), 720, MAROON_DARK)
    centered(d, "Treatable. Therapy + medication have strong evidence.",
             font("sans", 34), 790, MAROON_DARK)
    centered(d, "Recovery is the expected outcome.",
             font("sans_bold", 34), 835, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# 10 — schizophrenia (positive vs negative 2-column)
def schizophrenia(img, d):
    d.text((110, 70), "Schizophrenia.", fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 162), "Disrupted thinking, perception, and emotion. Two symptom clusters.",
           fill=MUTED, font=font("sans", 32))

    # Two columns
    cols = [
        ("POSITIVE  (added)", [
            "Hallucinations",
            "  — usually auditory voices",
            "Delusions",
            "  — fixed false beliefs",
            "Disorganized speech",
        ], "Things present that shouldn't be."),
        ("NEGATIVE  (missing)", [
            "Flat affect",
            "  — reduced emotional expression",
            "Avolition",
            "  — lack of motivation",
            "Social withdrawal",
        ], "Things absent that should be."),
    ]
    for i, (label, lines, sub) in enumerate(cols):
        x = 110 + i * 870
        d.rounded_rectangle([x, 250, x + 810, 770], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 270), label, fill=deck.accent, font=font("sans_bold", 42))
        for j, ln in enumerate(lines):
            f = font("sans_bold", 34) if not ln.strip().startswith("—") and not ln.strip().startswith("  —") else font("sans", 30)
            color = INK if not ln.strip().startswith("—") and not ln.strip().startswith("  —") else MUTED
            d.text((x + 30, 360 + j * 60), ln, fill=color, font=f)
        d.text((x + 30, 700), sub, fill=MUTED, font=font("serif_ital", 28))

    # Bottom: dopamine hypothesis + language
    d.rounded_rectangle([110, 800, W - 110, 985], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Dopamine hypothesis:  overactive dopamine pathways → positive symptoms.",
             font("sans_bold", 32), 820, MAROON_DARK)
    centered(d, "Most antipsychotics block dopamine receptors.",
             font("sans", 30), 870, MAROON_DARK)
    centered(d, "Language:  \"a person with schizophrenia\"  —  not  \"a schizophrenic.\"",
             font("serif_bold", 32), 925, MAROON)
deck.custom("10_schizophrenia", schizophrenia)

# 11 — personality disorders 3-cluster diagram
def personality(img, d):
    d.text((110, 70), "Personality disorders — 3 clusters.", fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Enduring, inflexible patterns causing distress or dysfunction.",
           fill=MUTED, font=font("sans", 30))

    clusters = [
        ("CLUSTER  A", "ODD / ECCENTRIC", [
            "Paranoid",
            "Schizoid",
            "Schizotypal",
        ]),
        ("CLUSTER  B", "DRAMATIC / ERRATIC", [
            "Borderline",
            "Narcissistic",
            "Antisocial",
            "Histrionic",
        ]),
        ("CLUSTER  C", "ANXIOUS / FEARFUL", [
            "Avoidant",
            "Dependent",
            "OCPD",
        ]),
    ]
    cw = 580
    for i, (label, sub, items) in enumerate(clusters):
        x = 110 + i * (cw + 20)
        y = 240
        d.rounded_rectangle([x, y, x + cw, y + 600], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        # cluster header band
        d.rounded_rectangle([x, y, x + cw, y + 100], radius=20,
                            fill=deck.accent_light, outline=deck.accent, width=5)
        centered_in_box_x = x + cw // 2
        tw = d.textlength(label, font=font("sans_bold", 42))
        d.text((centered_in_box_x - tw / 2, y + 22), label,
               fill=MAROON, font=font("sans_bold", 42))
        tw2 = d.textlength(sub, font=font("sans", 26))
        d.text((centered_in_box_x - tw2 / 2, y + 70), sub,
               fill=MAROON_DARK, font=font("sans", 26))
        # items
        for j, item in enumerate(items):
            d.text((x + 40, y + 150 + j * 70), "·  " + item,
                   fill=INK, font=font("sans_bold", 36))

    # Footer note
    d.rounded_rectangle([110, 880, W - 110, 985], radius=18, fill=deck.accent_light)
    centered(d, "OCPD  ≠  OCD.  OCPD = rigid personality.  OCD = intrusive thoughts + compulsions.",
             font("sans_bold", 30), 905, MAROON_DARK)
    centered(d, "Also: dissociative disorders (dissociative amnesia, DID).",
             font("sans", 28), 945, MAROON_DARK)
deck.custom("11_personality", personality)

# 12 — diathesis-stress model
def diathesis(img, d):
    d.text((110, 80), "Diathesis-stress model.", fill=MAROON, font=font("serif_bold", 68))
    d.text((110, 172), "Why same risk, different outcomes.",
           fill=MUTED, font=font("sans", 36))

    # Equation-style
    f_eq = font("sans_bold", 64)
    eq_y = 290
    parts = [
        ("DIATHESIS",  deck.accent),
        ("  +  ",      MUTED),
        ("STRESS",     deck.accent),
        ("  =  ",      MUTED),
        ("ONSET",      MAROON),
    ]
    # measure total
    total = sum(d.textlength(t, font=f_eq) for t, _ in parts)
    cur_x = (W - total) // 2
    for t, c in parts:
        d.text((cur_x, eq_y), t, fill=c, font=f_eq)
        cur_x += d.textlength(t, font=f_eq)

    # caption
    centered(d, "predisposition  (genes / biology)   +   triggering life event",
             font("sans", 32), eq_y + 100, MUTED)

    # 3-row table of combinations
    rows = [
        ("HIGH vulnerability",   "+",  "HIGH stress",   "→",  "ONSET",       MAROON),
        ("HIGH vulnerability",   "+",  "LOW stress",    "→",  "no onset",    MUTED),
        ("LOW vulnerability",    "+",  "HIGH stress",   "→",  "no onset",    MUTED),
    ]
    table_y = 530
    for i, (a, plus, b, arrow, result, color) in enumerate(rows):
        y = table_y + i * 95
        d.rounded_rectangle([180, y, W - 180, y + 80], radius=14,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((220, y + 22), a, fill=INK, font=font("sans_bold", 32))
        d.text((680, y + 22), plus, fill=MUTED, font=font("sans_bold", 32))
        d.text((760, y + 22), b, fill=INK, font=font("sans_bold", 32))
        d.text((1180, y + 22), arrow, fill=MUTED, font=font("sans_bold", 32))
        d.text((1280, y + 22), result, fill=color, font=font("sans_bold", 32))

    d.rounded_rectangle([110, 870, W - 110, 985], radius=18, fill=deck.accent_light)
    centered(d, "Biology sets the stage.   Environment writes the script.",
             font("serif_bold", 38), 905, MAROON_DARK)
deck.custom("12_diathesis_stress", diathesis)

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "4 D's: deviance, distress, dysfunction, danger. None alone is enough.",
    "DSM-5 = U.S. standard.  Descriptive, not explanatory.",
    "Categories: anxiety, OCD, trauma, mood, schizophrenia, personality, dissociative.",
    "Schizophrenia: positive vs negative symptoms · dopamine hypothesis.",
    "Personality clusters: A odd · B dramatic · C anxious.  Diathesis-stress: predisposition + stress = onset.",
    "~1 in 5 adults this year. Common, treatable. The disorder is never the person.",
])

# 14 — path (custom — gives us room for the personal-resonance footer)
def path_slide(img, d):
    d.text((110, 70), "How to actually master this module.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 152), "This video is ~10% of the work.  Here's the rest:",
           fill=MUTED, font=font("sans", 32))

    items = [
        ("✓",  "Watch this lesson",             "(done!)",                                         True),
        ("1.", "Read Myers · disorders modules", "Focus on the DSM categories and the 4 D's",       False),
        ("2.", "AP Classroom · 15 MCQ",          "Identify the disorder from short case descriptions", False),
        ("3.", "Assignment in dashboard",         "Label 8 case vignettes with the right DSM category", False),
        ("4.", "Advisor check-in",                "If categories blur together — that's normal",        False),
    ]
    y = 240
    for n, head, sub, done in items:
        n_color = deck.accent if done else MAROON
        head_color = deck.accent if done else INK
        d.text((140, y), n, fill=n_color, font=font("serif_bold", 40))
        d.text((230, y), head, fill=head_color, font=font("serif_bold", 36))
        d.text((230, y + 48), sub, fill=MUTED, font=font("sans", 26))
        y += 100

    # Personal resonance card — emphasized
    d.rounded_rectangle([110, 760, W - 110, 900], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "If anything in this lesson resonated personally —",
             font("serif_bold", 36), 780, MAROON_DARK)
    centered(d, "talk to a trusted adult or counselor.   Asking for help is strength.",
             font("sans_bold", 30), 835, MAROON_DARK)

    # Next up
    d.text((110, 940), "Next up:  Module 14 — Treatment of Psychological Disorders.  What actually helps.",
           fill=deck.accent, font=font("sans_bold", 30))
deck.custom("14_path", path_slide)

print("AP Psych Module 13 slides built.")

"""AP Psychology · Module 2 — Research Methods.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
14 slides. Heavy on slide_kit primitives; 3 customs:
  - 04_methods_ladder  : the case-study → experiment ladder
  - 10_correlation     : the −1 ↔ +1 correlation-coefficient ruler
  - 11_real_world      : ice cream vs. drowning spurious-correlation cartoon
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=2, output_dir="slides", logo_path=LOGO)


# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 2 — Research Methods",
           "~6 minutes  ·  How psychology actually proves things")


# 02 — hook (TikTok coffee-longevity claim)
def hook(img, d):
    d.text((110, 80), "TikTok said:", fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 168), "\"People who drink coffee live longer.\"",
           fill=MAROON_DARK, font=font("serif_ital", 52))

    # Phone-style card showing the post
    px, py, pw, ph = 200, 280, 760, 520
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=44,
                        outline=MAROON, width=8, fill=deck.card_bg)
    # Header strip
    d.rounded_rectangle([px + 24, py + 24, px + pw - 24, py + 100], radius=18,
                        fill=deck.accent_light)
    d.text((px + 50, py + 44), "@health_hacks_daily", fill=MAROON_DARK,
           font=font("sans_bold", 30))
    d.text((px + 50, py + 150), "\"People who drink",
           fill=INK, font=font("serif_bold", 42))
    d.text((px + 50, py + 200), " coffee live longer.\"",
           fill=INK, font=font("serif_bold", 42))
    d.text((px + 50, py + 280), "Drink up.  ☕☕☕",
           fill=MAROON, font=font("sans_bold", 38))
    d.text((px + 50, py + 360), "(cites a real study)",
           fill=MUTED, font=font("sans", 28))
    d.text((px + 50, py + 420), "❤  142k    💬  3.2k",
           fill=MUTED, font=font("sans", 28))

    # Right-side commentary
    cx, cy = 1080, 320
    d.text((cx, cy), "Honestly?", fill=MAROON, font=font("serif_bold", 64))
    d.text((cx, cy + 90), "No.", fill=RED, font=font("serif_bold", 90))
    d.text((cx, cy + 220), "That's a CORRELATION.",
           fill=MAROON_DARK, font=font("sans_bold", 40))
    d.text((cx, cy + 280), "It does NOT prove",
           fill=INK, font=font("sans", 36))
    d.text((cx, cy + 326), "coffee made them",
           fill=INK, font=font("sans", 36))
    d.text((cx, cy + 372), "live longer.",
           fill=INK, font=font("sans", 36))

    centered(d, "Today: how to tell \"goes together\" from \"caused.\"",
             font("serif_bold", 38), 880, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "The methods ladder — case study → experiment.",
    "IV, DV, confounds. The vocab AP grades you on.",
    "Correlation vs. causation. The number r.",
], footnote="By end: read a study description, name the method.")


# 04 — methods ladder (custom — the 5-rung ladder)
def methods_ladder(img, d):
    d.text((110, 70), "The methods ladder.", fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 156), "Higher rung = more control = stronger claims.",
           fill=MUTED, font=font("sans", 32))

    rungs = [
        ("EXPERIMENT",            "manipulate IV, randomize, measure DV",
         "ONLY way to prove CAUSE", deck.accent),
        ("CORRELATIONAL",         "measure two variables, see if they move together",
         "shows relationship, not cause", MAROON),
        ("SURVEY",                "ask a lot of people questions",
         "cheap and fast — but people lie", MAROON),
        ("NATURALISTIC OBSERVATION","watch behavior in the wild — don't interfere",
         "honest data, but no control", MAROON),
        ("CASE STUDY",            "one person (or one group) — deep dive",
         "great for rare cases, can't generalize", MAROON),
    ]
    box_h = 130
    top_y = 240
    gap = 16
    for i, (name, what, claim, color) in enumerate(rungs):
        y = top_y + i * (box_h + gap)
        # Indent the bottom rungs a bit so it reads like a ladder
        indent = (4 - i) * 28
        x0 = 110 + indent
        x1 = W - 110 - indent
        d.rounded_rectangle([x0, y, x1, y + box_h], radius=16,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((x0 + 28, y + 18), name, fill=color, font=font("sans_bold", 36))
        d.text((x0 + 28, y + 70), what, fill=INK, font=font("sans", 28))
        # Right-side claim
        claim_w = d.textlength(claim, font=font("sans_bold", 26))
        d.text((x1 - claim_w - 28, y + 78), claim, fill=color,
               font=font("sans_bold", 26))
deck.custom("04_methods_ladder", methods_ladder)


# 05 — IV / DV definition
def iv_dv(img, d):
    d.text((110, 80), "Independent vs. dependent variable.",
           fill=MAROON, font=font("serif_bold", 60))

    # Two cards side by side
    boxes = [
        (110, "INDEPENDENT  (IV)", "What the experimenter CHANGES on purpose.",
         "the cause we're testing", "ex: caffeine vs. placebo"),
        (1000, "DEPENDENT  (DV)", "What the experimenter MEASURES to see if it changed.",
         "the effect we're looking for", "ex: reaction time on a video game"),
    ]
    for x, title, body, sub, ex in boxes:
        d.rounded_rectangle([x, 220, x + 810, 700], radius=24,
                            outline=deck.accent, width=6, fill=deck.card_bg)
        d.text((x + 30, 250), title, fill=deck.accent, font=font("sans_bold", 44))
        ls = wrap(d, body, font("sans", 32), 750)
        for j, ln in enumerate(ls):
            d.text((x + 30, 340 + j * 44), ln, fill=INK, font=font("sans", 32))
        d.text((x + 30, 510), sub, fill=MAROON_DARK,
               font=font("sans_bold", 30))
        d.text((x + 30, 590), ex, fill=MUTED, font=font("serif_ital", 30))

    # Mnemonic banner
    d.rounded_rectangle([110, 760, W - 110, 880], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=4)
    centered(d, "DV  depends  on  IV.    Tattoo it on your brain.",
             font("serif_bold", 44), 800, MAROON_DARK)
deck.custom("05_iv_dv", iv_dv)


# 06 — confounds (definition + example)
deck.definition("06_confounds",
                "Confound  =  the variable that ruins your study.",
                "A third variable, not your IV, that also affects the DV.",
                sub="Random assignment is how we spread confounds evenly so they cancel out.")


# 07 — random sampling vs random assignment (compare)
deck.compare("07_random", "Random sampling  ≠  random assignment.",
    {"label": "RANDOM SAMPLING",
     "color": MAROON,
     "lines": [
         "How you PICK who's",
         "in your study.",
         "",
         "Goal: a sample that",
         "represents the whole",
         "population.",
     ],
     "footnote": "Lets you generalize results to the world."},
    {"label": "RANDOM ASSIGNMENT",
     "color": deck.accent,
     "lines": [
         "How you SPLIT them",
         "into groups.",
         "",
         "Goal: groups that",
         "are equivalent so",
         "confounds cancel.",
     ],
     "footnote": "Lets you trust cause-and-effect inside the study."})


# 08 — pause + try
deck.pause("08_pause1", "PAUSE  &  TRY",
           "100 students. Half randomly assigned to study with music, half in silence. Same quiz.",
           "IV?   DV?   Experiment or correlation?",
           hint="Pause. Decide. Press play.")


# 09 — pause answer (custom)
def pause_answer(img, d):
    d.text((110, 80), "Answer.",
           fill=MAROON, font=font("serif_bold", 80))

    # Three answer chips stacked
    chips = [
        ("IV",  "music  vs.  silence  (what she controlled)"),
        ("DV",  "quiz score  (what she measured)"),
        ("METHOD", "EXPERIMENT  —  she randomly assigned + manipulated one variable"),
    ]
    for i, (label, body) in enumerate(chips):
        y = 240 + i * 150
        d.rounded_rectangle([110, y, W - 110, y + 120], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((150, y + 30), label, fill=deck.accent,
               font=font("sans_bold", 44))
        d.text((430, y + 36), body, fill=INK, font=font("sans", 36))

    # Footer
    d.rounded_rectangle([110, 760, W - 110, 920], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Random assignment is what unlocks the word \"caused.\"",
             font("serif_bold", 42), 790, MAROON_DARK)
    centered(d, "Without it, you can only say \"linked\" or \"associated.\"",
             font("sans", 36), 855, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)


# 10 — correlation coefficient ruler (custom)
def correlation_ruler(img, d):
    d.text((110, 70), "The correlation coefficient  r.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "One number that summarizes how two variables move together.",
           fill=MUTED, font=font("sans", 32))

    # The ruler — horizontal bar from -1 to +1
    bar_y = 380
    bar_left = 200
    bar_right = W - 200
    bar_h = 70
    # Background ruler
    d.rectangle([bar_left, bar_y, bar_right, bar_y + bar_h],
                fill=deck.accent_light, outline=MAROON, width=4)

    # Tick marks at -1, -0.5, 0, +0.5, +1
    ticks = [(-1.0, "−1"), (-0.5, "−0.5"), (0.0, "0"), (0.5, "+0.5"), (1.0, "+1")]
    for val, label in ticks:
        x = bar_left + int((val + 1) / 2 * (bar_right - bar_left))
        d.line([x, bar_y - 20, x, bar_y + bar_h + 20], fill=MAROON, width=4)
        tw = d.textlength(label, font=font("sans_bold", 36))
        d.text((x - tw / 2, bar_y + bar_h + 30),
               label, fill=MAROON_DARK, font=font("sans_bold", 36))

    # Zone labels (above ruler)
    d.text((bar_left + 40, bar_y - 90), "STRONG NEGATIVE",
           fill=deck.accent, font=font("sans_bold", 28))
    d.text((bar_left + 40, bar_y - 56),
           "as one ↑, the other ↓", fill=INK, font=font("sans", 26))

    centered_x = (bar_left + bar_right) / 2
    txt = "NO RELATIONSHIP"
    tw = d.textlength(txt, font=font("sans_bold", 28))
    d.text((centered_x - tw / 2, bar_y - 90), txt,
           fill=deck.accent, font=font("sans_bold", 28))

    txt2 = "STRONG POSITIVE"
    tw2 = d.textlength(txt2, font=font("sans_bold", 28))
    d.text((bar_right - tw2 - 40, bar_y - 90), txt2,
           fill=deck.accent, font=font("sans_bold", 28))
    d.text((bar_right - 290, bar_y - 56),
           "as one ↑, the other ↑", fill=INK, font=font("sans", 26))

    # Bottom: sign vs strength box
    d.rounded_rectangle([110, 600, W - 110, 920], radius=20,
                        fill=deck.card_bg, outline=deck.accent, width=4)
    d.text((150, 620), "Two things to read off  r:",
           fill=MAROON, font=font("serif_bold", 44))
    d.text((150, 700), "SIGN  →  direction.",
           fill=deck.accent, font=font("sans_bold", 38))
    d.text((720, 700), "+ = move together.   − = move opposite.",
           fill=INK, font=font("sans", 34))
    d.text((150, 770), "SIZE  →  strength.",
           fill=deck.accent, font=font("sans_bold", 38))
    d.text((720, 770), "0.9 is strong.   0.1 is basically nothing.",
           fill=INK, font=font("sans", 34))
    d.text((150, 850), "Examples:  hours studied & test score = +0.6.   TikTok hours & test score ≈ −0.4.",
           fill=MUTED, font=font("serif_ital", 30))
deck.custom("10_correlation", correlation_ruler)


# 11 — real world: ice cream vs drowning spurious correlation (custom)
def ice_cream(img, d):
    d.text((110, 70), "Correlation  ≠  causation.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "The famous one AP loves:",
           fill=MUTED, font=font("sans", 32))

    # Three nodes: ice cream, drowning, sun (the real cause)
    # Top: ice cream and drowning sitting side by side
    # Connect them with a "?" arrow that's wrong
    # Below: sun pointing up to BOTH

    # Ice cream node
    d.rounded_rectangle([200, 260, 760, 440], radius=24,
                        outline=deck.accent, width=6, fill=deck.card_bg)
    centered_x_left = 480
    txt = "🍦  ICE CREAM SALES"
    tw = d.textlength(txt, font=font("sans_bold", 38))
    d.text((centered_x_left - tw / 2, 290), txt, fill=MAROON_DARK,
           font=font("sans_bold", 38))
    d.text((centered_x_left - 150, 360), "go up in summer",
           fill=INK, font=font("sans", 32))

    # Drowning node
    d.rounded_rectangle([1160, 260, 1720, 440], radius=24,
                        outline=deck.accent, width=6, fill=deck.card_bg)
    centered_x_right = 1440
    txt2 = "🏊  DROWNINGS"
    tw2 = d.textlength(txt2, font=font("sans_bold", 38))
    d.text((centered_x_right - tw2 / 2, 290), txt2, fill=MAROON_DARK,
           font=font("sans_bold", 38))
    d.text((centered_x_right - 165, 360), "go up in summer",
           fill=INK, font=font("sans", 32))

    # Wrong arrow (red, struck through)
    d.line([760, 350, 1160, 350], fill=RED, width=8)
    # Big X over the wrong arrow
    d.line([920, 310, 1000, 390], fill=RED, width=10)
    d.line([1000, 310, 920, 390], fill=RED, width=10)
    d.text((815, 220), "Did ice cream cause drowning?",
           fill=RED, font=font("sans_bold", 30))

    # The actual cause — third variable below, pointing up to both
    d.rounded_rectangle([700, 600, 1220, 760], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=6)
    centered(d, "☀  HOT WEATHER", font("serif_bold", 50), 620, MAROON_DARK)
    centered(d, "the actual third variable", font("sans", 30), 700, MAROON_DARK)

    # Arrows from sun box up to each node
    d.line([800, 600, 480, 440], fill=MAROON, width=6)
    d.line([1120, 600, 1440, 440], fill=MAROON, width=6)
    # Arrowheads
    d.polygon([(480, 440), (500, 460), (460, 460)], fill=MAROON)
    d.polygon([(1440, 440), (1420, 460), (1460, 460)], fill=MAROON)

    # Bottom warning
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=deck.card_bg, outline=deck.accent, width=4)
    centered(d, "\"linked to\" / \"associated with\" = correlation words. They cannot prove cause.",
             font("sans_bold", 32), 870, MAROON_DARK)
deck.custom("11_real_world", ice_cream)


# 12 — experiment design: experimental vs control + double-blind + p < .05
def experiment_design(img, d):
    d.text((110, 80), "Inside a real experiment.",
           fill=MAROON, font=font("serif_bold", 64))

    # Top row: experimental vs control
    for i, (label, body, color) in enumerate([
        ("EXPERIMENTAL GROUP", "gets the actual treatment\n(real caffeine, real drug)", deck.accent),
        ("CONTROL GROUP",      "gets nothing — or a PLACEBO\n(fake pill that looks identical)", MAROON),
    ]):
        x = 110 + i * 870
        d.rounded_rectangle([x, 200, x + 810, 460], radius=20,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((x + 30, 220), label, fill=color, font=font("sans_bold", 38))
        for j, ln in enumerate(body.split("\n")):
            d.text((x + 30, 300 + j * 50), ln, fill=INK, font=font("sans", 32))

    # Middle: double-blind banner
    d.rounded_rectangle([110, 500, W - 110, 660], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "DOUBLE-BLIND", font("serif_bold", 50), 520, MAROON_DARK)
    centered(d, "Neither participants nor researchers know who got the real treatment",
             font("sans", 32), 590, MAROON_DARK)
    centered(d, "until the data is in.  Stops bias on both sides.",
             font("sans", 32), 625, MAROON_DARK)

    # Bottom: p < .05
    d.rounded_rectangle([110, 700, W - 110, 920], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((150, 720), "Statistical significance:", fill=MAROON,
           font=font("serif_bold", 40))
    centered(d, "p  <  .05", font("mono", 92), 770, deck.accent)
    centered(d, "= the result is unlikely to be random chance. Probably a real effect.",
             font("sans", 30), 870, MUTED)
deck.custom("12_experiment_design", experiment_design)


# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Methods ladder: case study · observation · survey · correlation · EXPERIMENT.",
    "Only experiments prove CAUSE.  Everything else shows relationships.",
    "IV = what you change. DV = what you measure. Confound = the sneaky third variable.",
    "Random sampling = who's in the study.  Random assignment = how they're split.",
    "r runs from −1 to +1.  Sign = direction, size = strength.  Ice cream ↛ drowning.",
    "Real experiment = experimental + control group, double-blind, p < .05.",
])


# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read Myers Module 2",      "Research methods — focus on the experiments section"),
    ("2.", "AP Classroom · 15 MCQ",    "Identify IV, DV, and method type from study descriptions"),
    ("3.", "Assignment in dashboard",  "Label IV / DV / method on 4 study descriptions"),
    ("4.", "Advisor check-in",         "If confounds & random assignment still feel fuzzy"),
], next_text="Next up:  Module 3 — Biological Bases of Behavior. We crack open the brain itself.")


print("AP Psych Module 2 slides built.")

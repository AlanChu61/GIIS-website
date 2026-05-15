"""AP Psychology · Module 9 — Motivation & Emotion.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Custom slides earn their keep:
  - 05 Maslow's pyramid (5 levels drawn with PIL)
  - 04 Yerkes-Dodson inverted-U graph (simple vs. hard task curves)
  - 07 Side-by-side of the 4 emotion theories
  - 09 Pause-answer custom
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, GRID,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=9, output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 9 — Motivation & Emotion",
           "~8 minutes  ·  Why we do things + how feelings actually work")

# 02 — hook (textbook vs. Spotify playlist; intrinsic vs. extrinsic)
def hook(img, d):
    d.text((110, 80), "Same brain. Different effort.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "Textbook: 11 minutes.   Playlist: 4 hours.   Why?",
           fill=MAROON_DARK, font=font("serif", 44))

    # Two cards side-by-side
    cards = [
        (110,  "TEXTBOOK",
         ["Assigned by someone else.",
          "Reward is a future grade.",
          "= EXTRINSIC motivation."],
         "Quits after 11 minutes."),
        (1000, "SPOTIFY PLAYLIST",
         ["You picked the project.",
          "The doing IS the reward.",
          "= INTRINSIC motivation."],
         "4 hours, no problem."),
    ]
    for x, title, lines, footer in cards:
        d.rounded_rectangle([x, 290, x + 810, 800], radius=22,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 40, 320), title, fill=deck.accent, font=font("sans_bold", 44))
        for i, ln in enumerate(lines):
            d.text((x + 40, 410 + i * 70), ln, fill=INK, font=font("sans", 34))
        d.text((x + 40, 720), footer, fill=MAROON_DARK, font=font("serif_bold", 34))

    d.rounded_rectangle([110, 850, W - 110, 950], radius=18, fill=deck.accent_light)
    centered(d, "Intrinsic vs. extrinsic motivation — most-studied gap in psychology.",
             font("serif_bold", 36), 880, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Theories of motivation — instinct, drives, arousal, Maslow, self-determination.",
    "Four theories of emotion — the AP exam's favorite trap.",
    "Universal emotions across cultures + why polygraphs don't detect lies.",
], footnote="By end: read a scenario, name the motivation OR emotion theory.")

# 04 — Yerkes-Dodson + drive-reduction (custom: inverted-U graph)
def drive_arousal(img, d):
    d.text((110, 80), "Drive-reduction  +  arousal theory.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160), "Sometimes we want to REDUCE arousal. Sometimes we want to INCREASE it.",
           fill=MUTED, font=font("sans", 30))

    # Left: drive-reduction summary card
    d.rounded_rectangle([110, 230, 760, 660], radius=18,
                        outline=deck.accent, width=4, fill=deck.card_bg)
    d.text((140, 250), "DRIVE-REDUCTION", fill=deck.accent, font=font("sans_bold", 38))
    body = [
        "Body wants homeostasis.",
        "Hunger pushes you to eat.",
        "Thirst pushes you to drink.",
        "Behavior reduces the drive.",
        "",
        "Great for hunger / thirst.",
        "Useless for skydiving.",
    ]
    for i, ln in enumerate(body):
        d.text((140, 320 + i * 46), ln, fill=INK, font=font("sans", 30))

    # Right: Yerkes-Dodson inverted-U graph
    gx0, gy0 = 850, 250          # graph origin (top-left of plot box)
    gw, gh = 970, 540
    px0, py0 = gx0 + 90, gy0 + 60         # plot area top-left
    pw, ph = gw - 130, gh - 130           # plot dimensions
    px1, py1 = px0 + pw, py0 + ph         # plot bottom-right

    # plot frame
    d.rounded_rectangle([gx0, gy0, gx0 + gw, gy0 + gh], radius=18,
                        outline=deck.accent, width=4, fill=deck.card_bg)
    # axes
    d.line([(px0, py0), (px0, py1)], fill=INK, width=4)        # y-axis
    d.line([(px0, py1), (px1, py1)], fill=INK, width=4)        # x-axis
    # grid
    for k in range(1, 5):
        d.line([(px0 + k * pw // 5, py0), (px0 + k * pw // 5, py1)],
               fill=GRID, width=1)
        d.line([(px0, py1 - k * ph // 5), (px1, py1 - k * ph // 5)],
               fill=GRID, width=1)

    # Build inverted-U curves: y = a - b*(x - c)^2
    # Hard task: peaks LEFT (lower optimal arousal). Easy task: peaks RIGHT.
    import math
    def curve(peak_frac, points=80):
        """Return list of (x, y) pixel coords for an inverted U whose peak is at peak_frac of x-axis."""
        pts = []
        for i in range(points + 1):
            t = i / points  # 0..1 across arousal axis
            # parabola peaking at peak_frac with max value 0.92
            val = 0.92 - 4.2 * (t - peak_frac) ** 2
            val = max(val, 0.05)
            x = px0 + int(t * pw)
            y = py1 - int(val * ph)
            pts.append((x, y))
        return pts

    hard_pts = curve(peak_frac=0.32)   # hard task — optimal arousal LOW
    easy_pts = curve(peak_frac=0.70)   # easy task — optimal arousal HIGH

    # draw curves
    for pts, color, w in [(hard_pts, MAROON, 6), (easy_pts, deck.accent, 6)]:
        for i in range(len(pts) - 1):
            d.line([pts[i], pts[i + 1]], fill=color, width=w)

    # axis labels
    d.text((px0 - 60, py0 - 40), "Performance",
           fill=INK, font=font("sans_bold", 26))
    # x-axis label centered under axis
    arousal_lbl = "Arousal →"
    alw = d.textlength(arousal_lbl, font=font("sans_bold", 26))
    d.text((px0 + (pw - alw) / 2, py1 + 46), arousal_lbl,
           fill=INK, font=font("sans_bold", 26))
    d.text((px0 - 8, py1 + 18), "low", fill=MUTED, font=font("sans", 22))
    high_w = d.textlength("high", font=font("sans", 22))
    d.text((px1 - high_w, py1 + 18), "high", fill=MUTED, font=font("sans", 22))

    # peak markers
    for pts, color, label in [(hard_pts, MAROON, "HARD task → low arousal"),
                              (easy_pts, deck.accent, "EASY task → high arousal")]:
        peak = min(pts, key=lambda p: p[1])
        d.ellipse([peak[0] - 8, peak[1] - 8, peak[0] + 8, peak[1] + 8], fill=color)

    # legend
    lx, ly = px0 + 12, py0 + 12
    d.rectangle([lx, ly, lx + 40, ly + 8], fill=MAROON)
    d.text((lx + 52, ly - 10), "Hard task", fill=INK, font=font("sans_bold", 24))
    d.rectangle([lx, ly + 40, lx + 40, ly + 48], fill=deck.accent)
    d.text((lx + 52, ly + 30), "Easy task", fill=INK, font=font("sans_bold", 24))

    # caption under graph
    centered(d, "Yerkes-Dodson Law  ·  optimal arousal depends on task difficulty",
             font("sans_bold", 28), gy0 + gh + 18, MAROON_DARK)

    # bottom strip
    d.rounded_rectangle([110, 870, W - 110, 960], radius=18, fill=deck.accent_light)
    centered(d, "Too little arousal = sleepy.   Too much = panicking.   Sweet spot in the middle.",
             font("sans_bold", 30), 895, MAROON_DARK)
deck.custom("04_drive_arousal", drive_arousal)

# 05 — Maslow's pyramid (custom: 5-level pyramid)
def maslow(img, d):
    d.text((110, 80), "Maslow's hierarchy of needs.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Five levels. Lower needs first — mostly.",
           fill=MUTED, font=font("sans", 32))

    # Pyramid geometry — apex at top, base wide.
    apex_x = W // 2
    apex_y = 250
    base_y = 880
    half_base = 520     # half-width of base
    levels = 5
    pyr_h = base_y - apex_y

    # Level data, from TOP (apex) to BOTTOM (base)
    # Each: (label, example, fill_color)
    LAV = deck.accent
    LAV_LT = deck.accent_light
    # Generate 5 shades from accent (top, darkest) → accent_light (bottom, lightest)
    def lerp(a, b, t):
        return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
    shades = [lerp(LAV, LAV_LT, i / (levels - 1)) for i in range(levels)]

    rows = [
        ("SELF-ACTUALIZATION", "becoming your fullest self"),
        ("ESTEEM",             "competence · respect · achievement"),
        ("BELONGING & LOVE",   "friends · family · connection"),
        ("SAFETY",             "shelter · security · predictability"),
        ("PHYSIOLOGICAL",      "food · water · sleep · oxygen"),
    ]

    for i, (label, example) in enumerate(rows):
        # row i goes from y_top to y_bot
        y_top = apex_y + int(pyr_h * i / levels)
        y_bot = apex_y + int(pyr_h * (i + 1) / levels)
        # widths at top/bottom of this row (linear interp)
        top_half = int(half_base * i / levels)
        bot_half = int(half_base * (i + 1) / levels)
        # trapezoid polygon (or triangle for top row)
        if i == 0:
            poly = [(apex_x, y_top),
                    (apex_x - bot_half, y_bot),
                    (apex_x + bot_half, y_bot)]
        else:
            poly = [(apex_x - top_half, y_top),
                    (apex_x + top_half, y_top),
                    (apex_x + bot_half, y_bot),
                    (apex_x - bot_half, y_bot)]
        d.polygon(poly, fill=shades[i], outline=MAROON_DARK)

        # label inside the band
        y_mid = (y_top + y_bot) // 2
        # Top row is small — only fits the label
        if i == 0:
            f_lbl = font("sans_bold", 28)
            tw = d.textlength(label, font=f_lbl)
            d.text((apex_x - tw / 2, y_mid - 16), label, fill=MAROON_DARK, font=f_lbl)
        else:
            f_lbl = font("sans_bold", 36)
            f_ex = font("sans", 26)
            tw = d.textlength(label, font=f_lbl)
            d.text((apex_x - tw / 2, y_mid - 32), label, fill=MAROON_DARK, font=f_lbl)
            ew = d.textlength(example, font=f_ex)
            d.text((apex_x - ew / 2, y_mid + 14), example, fill=INK, font=f_ex)

    # Side arrow on the LEFT
    d.line([(apex_x - half_base - 70, base_y),
            (apex_x - half_base - 70, apex_y)],
           fill=MAROON, width=5)
    d.polygon([(apex_x - half_base - 85, apex_y + 18),
               (apex_x - half_base - 55, apex_y + 18),
               (apex_x - half_base - 70, apex_y - 10)], fill=MAROON)
    d.text((apex_x - half_base - 200, (apex_y + base_y) // 2 - 30),
           "higher", fill=MAROON, font=font("sans_bold", 28))
    d.text((apex_x - half_base - 200, (apex_y + base_y) // 2 + 6),
           "needs", fill=MAROON, font=font("sans_bold", 28))

    # bottom note
    d.text((110, 920), "Caveat: real life isn't this neat — hungry people still need love.",
           fill=MUTED, font=font("sans", 26))
deck.custom("05_maslow", maslow)

# 06 — self-determination theory (3-need card grid + overjustification box)
def self_determination(img, d):
    d.text((110, 80), "Self-Determination Theory  ·  Deci & Ryan, 1980s",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 158), "Three core psychological needs. Meet all three → intrinsic motivation.",
           fill=MUTED, font=font("sans", 30))

    needs = [
        ("AUTONOMY",    "I chose this.\nNobody is forcing me."),
        ("COMPETENCE",  "I'm good at it.\nOr I'm getting better."),
        ("RELATEDNESS", "I'm connected\nto other people."),
    ]
    cw = 560
    gap = 30
    total_w = 3 * cw + 2 * gap
    x0 = (W - total_w) // 2
    for i, (n, body) in enumerate(needs):
        x = x0 + i * (cw + gap)
        y = 250
        d.rounded_rectangle([x, y, x + cw, y + 320], radius=22,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, y + 30), n, fill=deck.accent, font=font("sans_bold", 44))
        for j, ln in enumerate(body.split("\n")):
            d.text((x + 30, y + 130 + j * 50), ln, fill=INK, font=font("sans", 34))

    # Overjustification effect call-out
    d.rounded_rectangle([110, 640, W - 110, 950], radius=22,
                        outline=MAROON, width=5, fill=deck.accent_light)
    d.text((150, 670), "Overjustification effect",
           fill=MAROON, font=font("serif_bold", 48))
    body_lines = [
        "Pay a kid to read books they already loved → they often stop reading when the money stops.",
        "Brain says: 'Oh, I guess I was only doing this for the money.'",
        "Extrinsic rewards can KILL intrinsic motivation. Build for autonomy + competence + relatedness instead.",
    ]
    for i, ln in enumerate(body_lines):
        lines = wrap(d, ln, font("sans", 30), W - 320)
        for j, sub in enumerate(lines):
            d.text((150, 740 + i * 70 + j * 38), sub, fill=INK, font=font("sans", 30))
deck.custom("06_self_determination", self_determination)

# 07 — Four emotion theories side-by-side (custom)
def emotion_theories(img, d):
    d.text((110, 70), "The four theories of emotion.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 150), "Same question, different orderings. AP's favorite trap.",
           fill=MUTED, font=font("sans", 30))

    theories = [
        ("JAMES-LANGE",
         "Body FIRST.\nFeeling follows.",
         ["see snake", "heart races", "→ FEAR"],
         "'I run, therefore I'm afraid.'"),
        ("CANNON-BARD",
         "Body and feeling\nat the SAME time.",
         ["see snake", "heart races + FEAR (parallel)", "thalamus splits"],
         "Simultaneous via thalamus."),
        ("SCHACHTER-SINGER",
         "Arousal + label\n= emotion.",
         ["see snake", "heart races", "label → FEAR"],
         "Two factors required."),
        ("LAZARUS",
         "Cognitive appraisal\nFIRST.",
         ["see snake", "appraise: threat!", "→ FEAR + body"],
         "Thought before feeling."),
    ]

    cw = 430
    gap = 14
    total_w = 4 * cw + 3 * gap
    x0 = (W - total_w) // 2
    y0 = 220

    for i, (name, blurb, sequence, footnote) in enumerate(theories):
        x = x0 + i * (cw + gap)
        # outer card
        d.rounded_rectangle([x, y0, x + cw, y0 + 720], radius=20,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        # name banner
        d.rectangle([x, y0, x + cw, y0 + 90], fill=deck.accent)
        nw = d.textlength(name, font=font("sans_bold", 30))
        d.text((x + (cw - nw) / 2, y0 + 28), name, fill=MAROON_DARK,
               font=font("sans_bold", 30))

        # short blurb
        for j, ln in enumerate(blurb.split("\n")):
            lw = d.textlength(ln, font=font("serif_bold", 28))
            d.text((x + (cw - lw) / 2, y0 + 110 + j * 40),
                   ln, fill=MAROON, font=font("serif_bold", 28))

        # sequence pills (vertical)
        py = y0 + 240
        for k, step in enumerate(sequence):
            lines = wrap(d, step, font("sans_bold", 24), cw - 40)
            box_h = 30 + len(lines) * 36
            d.rounded_rectangle([x + 20, py, x + cw - 20, py + box_h],
                                radius=12, outline=MAROON, width=2,
                                fill=deck.accent_light)
            for li, ln in enumerate(lines):
                lw = d.textlength(ln, font=font("sans_bold", 24))
                d.text((x + (cw - lw) / 2, py + 12 + li * 32),
                       ln, fill=MAROON_DARK, font=font("sans_bold", 24))
            py += box_h + 12
            # arrow down
            if k < len(sequence) - 1:
                ax = x + cw // 2
                d.line([(ax, py - 8), (ax, py + 8)], fill=MAROON, width=3)
                d.polygon([(ax - 8, py + 6), (ax + 8, py + 6),
                           (ax, py + 16)], fill=MAROON)
                py += 18

        # footnote at bottom
        fn_lines = wrap(d, footnote, font("sans", 22), cw - 40)
        for j, ln in enumerate(fn_lines):
            d.text((x + 20, y0 + 660 + j * 28), ln,
                   fill=MUTED, font=font("sans", 22))
deck.custom("07_emotion_theories", emotion_theories)

# 08 — pause + try (dark room scenario)
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Dark room. Heart pounds. You SEE a figure, label it as fear. Roommate flips on the light — it's a coat rack. Fear melts.",
           "Which emotion theory fits?",
           hint="Pause. Decide. Press play.")

# 09 — pause answer (custom)
def pause_answer(img, d):
    d.text((110, 70), "Answer:  Schachter-Singer.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "Two factors — physical arousal + cognitive label = emotion.",
           fill=MUTED, font=font("sans", 32))

    # The sequence row
    seq = [
        ("1", "Heart pounds", "(arousal)"),
        ("2", "Look around", "(scan for label)"),
        ("3", "See figure",  "label it: FEAR"),
        ("4", "Light flips", "relabel: just a coat rack"),
        ("5", "Fear melts",  "label changed → emotion changed"),
    ]
    sw = 340
    gap = 14
    total = 5 * sw + 4 * gap
    x0 = (W - total) // 2
    y0 = 250
    for i, (num, head, sub) in enumerate(seq):
        x = x0 + i * (sw + gap)
        d.rounded_rectangle([x, y0, x + sw, y0 + 200], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((x + 24, y0 + 16), num, fill=deck.accent, font=font("serif_bold", 40))
        d.text((x + 24, y0 + 80), head, fill=INK, font=font("sans_bold", 30))
        # wrap subtext
        for j, ln in enumerate(wrap(d, sub, font("sans", 24), sw - 48)):
            d.text((x + 24, y0 + 130 + j * 32), ln, fill=MUTED,
                   font=font("sans", 24))
        # arrow between
        if i < len(seq) - 1:
            ax = x + sw + 2
            ay = y0 + 100
            d.line([(ax, ay), (ax + gap - 4, ay)], fill=MAROON, width=4)
            d.polygon([(ax + gap - 4, ay - 8),
                       (ax + gap - 4, ay + 8),
                       (ax + gap + 4, ay)], fill=MAROON)

    # Quick contrast strip
    d.rounded_rectangle([110, 530, W - 110, 850], radius=22,
                        outline=MAROON, width=5, fill=deck.accent_light)
    d.text((150, 560), "Why not the others?",
           fill=MAROON, font=font("serif_bold", 42))
    contrasts = [
        ("James-Lange:",       "the pounding heart IS the fear — no labeling needed."),
        ("Cannon-Bard:",       "pounding heart and feeling of fear hit at the SAME instant."),
        ("Lazarus:",           "you appraised 'threat' BEFORE the heart pounded."),
        ("Schachter-Singer:",  "arousal + a label, IN THAT ORDER. ← matches the story."),
    ]
    for i, (k, v) in enumerate(contrasts):
        d.text((150, 640 + i * 50), k, fill=MAROON, font=font("sans_bold", 28))
        d.text((520, 640 + i * 50), v, fill=INK, font=font("sans", 28))

    centered(d, "Two factors  ·  arousal + cognitive label  ·  = emotion.",
             font("serif_bold", 36), 880, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# 10 — universal emotions (Ekman's six)
def universal(img, d):
    d.text((110, 80), "Universal emotions  ·  Ekman, 1960s–70s",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 168), "Six facial expressions recognized in every culture studied.",
           fill=MUTED, font=font("sans", 32))

    emotions = [
        ("HAPPY",    ":)"),
        ("SAD",      ":("),
        ("FEAR",     ":O"),
        ("ANGER",    ">:("),
        ("DISGUST",  ":P"),
        ("SURPRISE", ":!"),
    ]
    cw, ch = 540, 220
    gap = 20
    rows = 2
    cols = 3
    total_w = cols * cw + (cols - 1) * gap
    x0 = (W - total_w) // 2
    y0 = 270

    for i, (name, glyph) in enumerate(emotions):
        col = i % cols
        row = i // cols
        x = x0 + col * (cw + gap)
        y = y0 + row * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=20,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        # left: glyph as a "face" in a circle
        cx, cy = x + 100, y + ch // 2
        d.ellipse([cx - 65, cy - 65, cx + 65, cy + 65],
                  outline=MAROON, width=4, fill=deck.accent_light)
        gw = d.textlength(glyph, font=font("serif_bold", 56))
        d.text((cx - gw / 2, cy - 36), glyph, fill=MAROON_DARK,
               font=font("serif_bold", 56))
        # right: name
        d.text((x + 200, y + 80), name, fill=INK, font=font("sans_bold", 44))

    d.rounded_rectangle([110, 760, W - 110, 950], radius=20, fill=deck.accent_light)
    d.text((150, 780),
           "Even isolated tribes recognize these. Babies show them. Blind kids smile.",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((150, 830),
           "BUT — display rules differ by culture.",
           fill=MAROON, font=font("serif_bold", 36))
    d.text((150, 890),
           "WHEN it's appropriate to show emotion (and how big) varies. Performance ≠ feeling.",
           fill=INK, font=font("sans", 28))
deck.custom("10_universal", universal)

# 11 — polygraph limitations
def polygraph(img, d):
    d.text((110, 80), "Polygraphs measure arousal — not lying.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 170), "Famous on TV. Mostly inadmissible in U.S. courts. Here's why.",
           fill=MUTED, font=font("sans", 30))

    # What it measures
    d.rounded_rectangle([110, 250, W - 110, 390], radius=20,
                        outline=deck.accent, width=4, fill=deck.card_bg)
    d.text((140, 270), "What it measures:",
           fill=deck.accent, font=font("sans_bold", 36))
    d.text((140, 320), "heart rate  ·  breathing  ·  skin conductance  ·  blood pressure",
           fill=INK, font=font("sans", 32))

    # Three problems
    problems = [
        ("Problem 1",
         "Calm liars pass.  Guilty + low-arousal = polygraph says 'truth.'"),
        ("Problem 2",
         "Nervous innocents fail.  Anxious about the test = polygraph says 'lie.'"),
        ("Problem 3",
         "Many emotions look the same.  Fear, guilt, anger, embarrassment, even excitement — all light up the polygraph."),
    ]
    y = 430
    for label, body in problems:
        d.rounded_rectangle([110, y, W - 110, y + 130], radius=16,
                            outline=MAROON, width=3, fill=deck.card_bg)
        d.text((140, y + 18), label, fill=MAROON, font=font("sans_bold", 32))
        for j, ln in enumerate(wrap(d, body, font("sans", 28), W - 320)):
            d.text((140, y + 64 + j * 36), ln, fill=INK, font=font("sans", 28))
        y += 150

    # AP takeaway
    d.rounded_rectangle([110, 890, W - 110, 980], radius=18, fill=deck.accent_light)
    centered(d, "AP answer: polygraphs measure AROUSAL, not lying.  Validity is low.",
             font("sans_bold", 32), 915, MAROON_DARK)
deck.custom("11_polygraph", polygraph)

# 12 — real world examples
def real_world(img, d):
    d.text((110, 80), "Where you've already seen this.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 168), "Once you know this unit, you can't un-see it.",
           fill=MUTED, font=font("sans", 30))

    items = [
        ("Daily-reward streaks in games",
         "variable-ratio reinforcement + a hit of autonomy & competence"),
        ("Diets that fail after the cash bonus ends",
         "overjustification effect — extrinsic reward killed the habit"),
        ("Coach saying 'relax' before a free throw",
         "Yerkes-Dodson — dialing arousal DOWN for a precise task"),
        ("Laughing only AFTER you realize you're safe",
         "Lazarus — appraisal flips, emotion flips with it"),
        ("'Why don't I just open the textbook?'",
         "low autonomy + low competence = no intrinsic motivation"),
    ]
    y = 260
    for head, sub in items:
        d.rounded_rectangle([110, y, W - 110, y + 110], radius=16,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((140, y + 14), head, fill=INK, font=font("serif_bold", 36))
        d.text((140, y + 64), sub, fill=deck.accent, font=font("sans", 28))
        y += 130
deck.custom("12_real_world", real_world)

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Drive-reduction = homeostasis (hunger, thirst). Yerkes-Dodson = optimal arousal depends on task.",
    "Maslow's hierarchy: physiological → safety → belonging → esteem → self-actualization.",
    "Self-determination = autonomy + competence + relatedness. Overjustification kills intrinsic.",
    "James-Lange (body first) · Cannon-Bard (parallel) · Schachter-Singer (arousal + label) · Lazarus (appraisal first).",
    "Ekman: 6 universal emotions. Display rules differ by culture.",
    "Polygraph measures arousal, not lying. Low validity.",
])

# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",         "(done!)"),
    ("1.", "Read Myers Module 9",       "Motivation & emotion — focus on the 4 emotion theories"),
    ("2.", "AP Classroom · 12 MCQ",     "Identify the emotion theory from the scenario"),
    ("3.", "Assignment in dashboard",    "Label 8 scenarios as James-Lange / Cannon-Bard / Schachter-Singer / Lazarus"),
    ("4.", "Advisor check-in",           "Book a session if Maslow vs. self-determination feels fuzzy"),
], next_text="Next up:  Module 10 — Developmental Psychology. From a clump of cells to old age.")

print("AP Psych Module 9 slides built.")

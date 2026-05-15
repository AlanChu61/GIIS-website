"""AP Psychology · Module 12 — Testing & Intelligence.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Custom diagrams: reliability-vs-validity dartboard 2x2, IQ bell curve with
±15 SD bands, three theories of intelligence side-by-side cards, plus the
standard kit primitives.
"""
import sys
import math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, CREAM, RED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=12, output_dir="slides", logo_path=LOGO)

# ── 01 — title ───────────────────────────────────────────────────────
deck.title("01_title", "AP Psychology",
           "Module 12 — Testing & Intelligence",
           "~8 minutes  ·  Can one number measure smart?")

# ── 02 — hook (broken scale + broken thermometer) ────────────────────
def hook(img, d):
    d.text((110, 80), "Reliability  ≠  Validity.",
           fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 168), "A broken scale and a broken thermometer.",
           fill=MAROON_DARK, font=font("serif_ital", 44))

    # Two big cards side-by-side
    cards = [
        (110, 280,
         "BATHROOM SCALE",
         "Weighs you 4 times.",
         "150 · 168 · 142 · 155.",
         "Inconsistent  →  unreliable.",
         deck.accent),
        (1000, 280,
         "BROKEN THERMOMETER",
         "Always reads 72°F.",
         "Even inside a freezer.",
         "Reliable  →  but invalid.",
         MAROON),
    ]
    for x, y, label, line1, line2, verdict, color in cards:
        d.rounded_rectangle([x, y, x + 810, y + 380], radius=24,
                            outline=color, width=6, fill=deck.card_bg)
        d.text((x + 30, y + 26), label, fill=color, font=font("sans_bold", 40))
        d.text((x + 30, y + 100), line1, fill=INK, font=font("sans", 34))
        d.text((x + 30, y + 152), line2, fill=INK, font=font("sans", 34))
        d.text((x + 30, y + 280), verdict, fill=MAROON_DARK,
               font=font("serif_bold", 36))

    d.rounded_rectangle([110, 720, W-110, 900], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Consistent  ≠  Correct.",
             font("serif_bold", 56), 750, MAROON_DARK)
    centered(d, "AP loves this trap. Don't fall for it.",
             font("sans_bold", 34), 830, MAROON_DARK)
deck.custom("02_hook", hook)

# ── 03 — overview ────────────────────────────────────────────────────
deck.overview("03_overview", "Game plan.", [
    "Three test-quality criteria — reliability, validity, standardization.",
    "Three theories of intelligence — Spearman, Gardner, Sternberg.",
    "IQ tests, the bell curve, the Flynn effect, and bias.",
], footnote="By end: read a test description, name reliable vs. valid vs. both vs. neither.")

# ── 04 — three criteria ──────────────────────────────────────────────
def three_criteria(img, d):
    d.text((110, 70), "What makes a test actually good.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Three bars to clear. Skip one — it isn't really a test.",
           fill=MUTED, font=font("sans", 30))

    items = [
        ("RELIABILITY",      "consistent results",
         "same person, same conditions  →  similar score"),
        ("VALIDITY",         "measures what it claims",
         "an IQ test should measure thinking — not reading speed"),
        ("STANDARDIZATION",  "uniform procedure + comparison group",
         "same instructions for everyone  ·  scored vs. a normed sample"),
    ]
    cw = W - 220
    for i, (name, defn, ex) in enumerate(items):
        y = 250 + i * 200
        d.rounded_rectangle([110, y, 110 + cw, y + 170], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((140, y + 22), name, fill=deck.accent, font=font("sans_bold", 42))
        d.text((140, y + 80), defn, fill=INK, font=font("serif_bold", 36))
        d.text((140, y + 126), ex, fill=MUTED, font=font("sans", 28))

    d.rounded_rectangle([110, 870, W-110, 970], radius=20, fill=deck.accent_light)
    centered(d, "All three.  Or it's not a test  —  it's an opinion.",
             font("serif_bold", 38), 895, MAROON_DARK)
deck.custom("04_three_criteria", three_criteria)

# ── 05 — reliability vs validity 2x2 with dartboard images ──────────
def reliability_validity(img, d):
    d.text((110, 60), "Reliability vs. Validity  ·  the dartboard test.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 138), "Reliability = darts cluster.   Validity = darts hit the bullseye.",
           fill=MUTED, font=font("sans", 28))

    # 2x2 grid of dartboards
    cell_w, cell_h = 700, 320
    gap = 30
    grid_x = (W - 2 * cell_w - gap) // 2
    grid_y = 200

    # Cells: (col, row, label, sub, dart_pattern)
    # dart_pattern = "tight_center" | "tight_off" | "spread_center" | "spread_off"
    cells = [
        (0, 0, "HIGH RELIABILITY  ·  LOW VALIDITY",
         "consistent  ·  but wrong target",
         "tight_off"),
        (1, 0, "HIGH RELIABILITY  ·  HIGH VALIDITY",
         "consistent  ·  hits the bullseye",
         "tight_center"),
        (0, 1, "LOW RELIABILITY  ·  LOW VALIDITY",
         "scattered  ·  not on target",
         "spread_off"),
        (1, 1, "LOW RELIABILITY  ·  HIGH VALIDITY",
         "scattered  ·  but average is on target",
         "spread_center"),
    ]

    def draw_dartboard(cx, cy, r, pattern):
        # Concentric circles
        rings = [(r, CREAM, MAROON_DARK),
                 (int(r * 0.78), deck.accent_light, MAROON_DARK),
                 (int(r * 0.55), CREAM, MAROON_DARK),
                 (int(r * 0.32), deck.accent, MAROON_DARK),
                 (int(r * 0.14), MAROON, MAROON_DARK)]
        for radius, fill, outline in rings:
            d.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                      fill=fill, outline=outline, width=3)

        # Decide dart positions
        import random
        rng = random.Random(hash(pattern) & 0xFFFFFFFF)
        if pattern == "tight_center":
            center = (cx, cy)
            spread = 10
        elif pattern == "tight_off":
            center = (cx + 55, cy - 50)
            spread = 10
        elif pattern == "spread_center":
            center = (cx, cy)
            spread = 60
        else:  # spread_off
            center = (cx + 45, cy - 40)
            spread = 60

        darts = []
        for _ in range(5):
            dx = rng.gauss(0, spread)
            dy = rng.gauss(0, spread)
            darts.append((center[0] + dx, center[1] + dy))
        # Draw darts as small filled red circles with a darker outline
        for px, py in darts:
            d.ellipse([px - 9, py - 9, px + 9, py + 9],
                      fill=RED, outline=MAROON_DARK, width=2)

    for col, row, label, sub, pattern in cells:
        x = grid_x + col * (cell_w + gap)
        y = grid_y + row * (cell_h + gap)
        d.rounded_rectangle([x, y, x + cell_w, y + cell_h], radius=18,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        # Label at top
        d.text((x + 24, y + 16), label, fill=MAROON, font=font("sans_bold", 24))
        d.text((x + 24, y + 50), sub, fill=MUTED, font=font("sans", 22))
        # Dartboard centered in lower portion
        cx = x + cell_w // 2
        cy = y + 195
        draw_dartboard(cx, cy, 110, pattern)

    d.text((110, 945), "Top-right is the goal.  The thermometer-stuck-at-72 lives in the top-LEFT.",
           fill=MAROON_DARK, font=font("serif_bold", 26))
deck.custom("05_reliability_validity", reliability_validity)

# ── 06 — Spearman's g ────────────────────────────────────────────────
def g_factor(img, d):
    d.text((110, 70), "Spearman's  g.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "Score well on one mental test  →  tend to score well on others.",
           fill=MUTED, font=font("sans", 30))

    # Center: a big g circle with arrows fanning out to skills
    cx, cy = 540, 600
    rg = 160
    d.ellipse([cx - rg, cy - rg, cx + rg, cy + rg],
              fill=MAROON, outline=MAROON_DARK, width=6)
    centered_letter = "g"
    lw = d.textlength(centered_letter, font=font("serif_bold", 200))
    d.text((cx - lw / 2, cy - 130), centered_letter,
           fill=CREAM, font=font("serif_bold", 200))

    # Skills around g — radiating arrows
    skills = [
        ("vocabulary",       cx + 480, cy - 240),
        ("math reasoning",   cx + 480, cy - 100),
        ("spatial puzzles",  cx + 480, cy + 40),
        ("reading speed",    cx + 480, cy + 180),
    ]
    for name, sx, sy in skills:
        # arrow line from edge of g circle to skill card
        # angle from center to skill
        ang = math.atan2(sy + 30 - cy, sx - cx)
        ex_ = cx + math.cos(ang) * (rg + 4)
        ey_ = cy + math.sin(ang) * (rg + 4)
        d.line([(ex_, ey_), (sx - 10, sy + 30)], fill=MAROON, width=5)
        # skill card
        d.rounded_rectangle([sx, sy, sx + 460, sy + 70], radius=14,
                            outline=deck.accent, width=4, fill=deck.card_bg)
        d.text((sx + 20, sy + 20), name, fill=INK, font=font("sans_bold", 32))

    # Right side — the takeaway
    d.rounded_rectangle([110, 880, W-110, 990], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=4)
    centered(d, "g  =  the all-purpose mental horsepower.",
             font("serif_bold", 38), 905, MAROON_DARK)
    centered(d, "Charles Spearman, 1904.  Hard to argue with statistically.",
             font("sans", 28), 952, MAROON_DARK)

    # Date label up top right
    d.rounded_rectangle([cx + 480, cy - 380, cx + 940, cy - 280], radius=18,
                        outline=MAROON, width=4, fill=CREAM)
    d.text((cx + 500, cy - 365), "1904  ·  Charles Spearman",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((cx + 500, cy - 325), "noticed scores correlated",
           fill=INK, font=font("sans", 24))
deck.custom("06_g_factor", g_factor)

# ── 07 — three theories of intelligence (side-by-side cards) ─────────
def theories(img, d):
    d.text((110, 60), "Three answers to:  what counts as smart?",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 138), "Spearman, Gardner, Sternberg  ·  one, eight, three.",
           fill=MUTED, font=font("sans", 30))

    col_w = 560
    col_gap = 30
    total = col_w * 3 + col_gap * 2
    start_x = (W - total) // 2

    # ── Spearman card ──
    sx = start_x
    sy = 200
    d.rounded_rectangle([sx, sy, sx + col_w, sy + 700], radius=22,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((sx + 24, sy + 24), "SPEARMAN", fill=MAROON, font=font("sans_bold", 38))
    d.text((sx + 24, sy + 76), "ONE general factor",
           fill=INK, font=font("serif_bold", 28))
    # Big "1"
    d.rounded_rectangle([sx + 24, sy + 130, sx + col_w - 24, sy + 290], radius=16,
                        fill=deck.accent_light, outline=MAROON, width=3)
    big = "1"
    bw = d.textlength(big, font=font("serif_bold", 140))
    d.text((sx + col_w / 2 - bw / 2, sy + 140), big,
           fill=MAROON, font=font("serif_bold", 140))
    # Description
    d.text((sx + 24, sy + 320), "g  =  general intelligence.",
           fill=INK, font=font("sans_bold", 28))
    desc = "Performance on one mental test predicts performance on others. One underlying ability."
    for j, ln in enumerate(wrap(d, desc, font("sans", 26), col_w - 48)):
        d.text((sx + 24, sy + 370 + j * 36), ln, fill=INK, font=font("sans", 26))
    # Verdict
    d.rounded_rectangle([sx + 24, sy + 570, sx + col_w - 24, sy + 680], radius=14,
                        outline=deck.accent, width=3)
    d.text((sx + 40, sy + 586), "Verdict.", fill=deck.accent, font=font("sans_bold", 28))
    d.text((sx + 40, sy + 628), "Statistically robust.",
           fill=INK, font=font("sans", 26))

    # ── Gardner card ──
    gx = start_x + col_w + col_gap
    gy = 200
    d.rounded_rectangle([gx, gy, gx + col_w, gy + 700], radius=22,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((gx + 24, gy + 24), "GARDNER", fill=MAROON, font=font("sans_bold", 38))
    d.text((gx + 24, gy + 76), "EIGHT intelligences",
           fill=INK, font=font("serif_bold", 28))
    # 8 small chips in a 2x4 grid
    eight = ["linguistic", "logical-math", "spatial", "musical",
             "bodily-kines.", "interpersonal", "intrapersonal", "naturalist"]
    chip_w = (col_w - 60) // 2
    chip_h = 50
    chip_gap_y = 8
    chip_y0 = gy + 130
    for i, name in enumerate(eight):
        col = i % 2
        row = i // 2
        cx_ = gx + 24 + col * (chip_w + 12)
        cy_ = chip_y0 + row * (chip_h + chip_gap_y)
        d.rounded_rectangle([cx_, cy_, cx_ + chip_w, cy_ + chip_h], radius=10,
                            fill=deck.accent_light, outline=deck.accent, width=2)
        # center text inside chip
        tw = d.textlength(name, font=font("sans_bold", 22))
        d.text((cx_ + chip_w / 2 - tw / 2, cy_ + 12), name,
               fill=MAROON_DARK, font=font("sans_bold", 22))
    # Description
    desc_g = "Eight separate kinds of smart, not one. Hugely popular in schools."
    for j, ln in enumerate(wrap(d, desc_g, font("sans", 26), col_w - 48)):
        d.text((gx + 24, gy + 410 + j * 36), ln, fill=INK, font=font("sans", 26))
    # Verdict
    d.rounded_rectangle([gx + 24, gy + 570, gx + col_w - 24, gy + 680], radius=14,
                        outline=RED, width=3)
    d.text((gx + 40, gy + 586), "AP catch.", fill=RED, font=font("sans_bold", 28))
    d.text((gx + 40, gy + 628), "Weak empirical support.",
           fill=INK, font=font("sans", 26))

    # ── Sternberg card ──
    tx = start_x + 2 * (col_w + col_gap)
    ty = 200
    d.rounded_rectangle([tx, ty, tx + col_w, ty + 700], radius=22,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((tx + 24, ty + 24), "STERNBERG", fill=MAROON, font=font("sans_bold", 38))
    d.text((tx + 24, ty + 76), "THREE intelligences  ·  triarchic",
           fill=INK, font=font("serif_bold", 28))
    triplet = [
        ("ANALYTICAL", "book smart  ·  what schools test"),
        ("CREATIVE",   "generating new ideas"),
        ("PRACTICAL",  "street smart  ·  real-world"),
    ]
    for i, (name, sub) in enumerate(triplet):
        y_ = ty + 130 + i * 130
        d.rounded_rectangle([tx + 24, y_, tx + col_w - 24, y_ + 110], radius=14,
                            outline=deck.accent, width=3, fill=deck.accent_light)
        d.text((tx + 44, y_ + 14), name, fill=MAROON, font=font("sans_bold", 30))
        d.text((tx + 44, y_ + 60), sub, fill=INK, font=font("sans", 26))
    # Verdict
    d.rounded_rectangle([tx + 24, ty + 570, tx + col_w - 24, ty + 680], radius=14,
                        outline=deck.accent, width=3)
    d.text((tx + 40, ty + 586), "Verdict.", fill=deck.accent, font=font("sans_bold", 28))
    d.text((tx + 40, ty + 628), "Defensible. Hard to Scantron.",
           fill=INK, font=font("sans", 26))

    d.text((110, 945), "AP will ask you to attach a name to a number  ·  one, eight, or three.",
           fill=MAROON_DARK, font=font("serif_bold", 26))
deck.custom("07_theories", theories)

# ── 08 — pause + try ─────────────────────────────────────────────────
deck.pause("08_pause1", "PAUSE  &  TRY",
           "SAT in October. Same students retake in March. Scores are nearly identical.",
           "reliable or valid?",
           hint="Q2: does this prove the SAT predicts college GPA?  ·  Pause. Decide. Press play.")

# ── 09 — pause answer ────────────────────────────────────────────────
def pause_answer(img, d):
    d.text((110, 60), "Reliable  ≠  Valid.  Don't conflate.",
           fill=MAROON, font=font("serif_bold", 60))

    # Two columns
    cols = [
        ("RELIABLE  ·  YES",
         "Same test, same students, two times, similar scores. That's TEST-RETEST reliability. The test is consistent.",
         deck.accent),
        ("PREDICTIVE VALIDITY  ·  NOT YET",
         "To prove the SAT predicts GPA, follow the same students into college. Compare their freshman GPA to their SAT prediction. Different study, different question.",
         MAROON),
    ]
    for i, (title, body, color) in enumerate(cols):
        x = 110 + i * 870
        d.rounded_rectangle([x, 200, x + 760, 640], radius=24,
                            outline=color, width=5, fill=deck.card_bg)
        d.text((x + 30, 230), title, fill=color, font=font("sans_bold", 38))
        lines = wrap(d, body, font("sans", 30), 700)
        for j, ln in enumerate(lines):
            d.text((x + 30, 320 + j * 44), ln, fill=INK, font=font("sans", 30))

    d.rounded_rectangle([110, 700, W-110, 920], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "A broken thermometer that always says 72°F is perfectly reliable.",
             font("serif_bold", 36), 730, MAROON_DARK)
    centered(d, "And tells you nothing about the actual temperature.",
             font("sans_bold", 32), 790, MAROON_DARK)
    centered(d, "Reliability is necessary  —  but not sufficient.",
             font("serif_bold", 38), 850, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# ── 10 — IQ normal distribution bell curve ───────────────────────────
def iq_bell(img, d):
    d.text((110, 60), "IQ  ·  the normal distribution.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 138), "Mean = 100.  SD = 15.  Bell curve.  68 / 95 / 99.",
           fill=MUTED, font=font("sans", 30))

    # Bell curve area
    chart_x0 = 200
    chart_x1 = W - 200
    chart_y0 = 240
    chart_y1 = 760
    # baseline
    base_y = chart_y1
    # x-axis line
    d.line([(chart_x0, base_y), (chart_x1, base_y)], fill=MAROON_DARK, width=4)

    # Compute points for the bell curve. 7 SDs from mean (55..145 covers ±3 SD)
    # Map IQ range 40..160 to the chart x range.
    iq_min = 40
    iq_max = 160
    def iq_to_x(iq):
        return chart_x0 + (iq - iq_min) / (iq_max - iq_min) * (chart_x1 - chart_x0)

    # Gaussian peak height (in pixels above base)
    peak_h = 460
    sd = 15
    mean = 100
    def iq_to_y(iq):
        z = (iq - mean) / sd
        h = peak_h * math.exp(-0.5 * z * z)
        return base_y - h

    # Build polygon for shaded curve
    points = []
    for iq_step in range(iq_min, iq_max + 1):
        points.append((iq_to_x(iq_step), iq_to_y(iq_step)))

    # Fill shaded regions: ±3SD lightest, ±2SD medium, ±1SD darkest
    def fill_band(lo, hi, color):
        poly = [(iq_to_x(lo), base_y)]
        for iq_step in range(lo, hi + 1):
            poly.append((iq_to_x(iq_step), iq_to_y(iq_step)))
        poly.append((iq_to_x(hi), base_y))
        d.polygon(poly, fill=color)

    # Darken bands toward center
    fill_band(iq_min, iq_max, deck.card_bg)        # background body
    fill_band(70, 130, deck.accent_light)          # ±2 SD
    fill_band(85, 115, deck.accent)                # ±1 SD

    # Curve outline
    d.line(points, fill=MAROON, width=5)

    # Vertical SD lines
    sd_lines = [(70, "70"), (85, "85"), (100, "100"), (115, "115"), (130, "130")]
    for iq_v, label in sd_lines:
        x = iq_to_x(iq_v)
        d.line([(x, base_y), (x, iq_to_y(iq_v))], fill=MAROON_DARK, width=2)
        # x-axis tick label
        lw = d.textlength(label, font=font("sans_bold", 28))
        d.text((x - lw / 2, base_y + 14), label,
               fill=MAROON_DARK, font=font("sans_bold", 28))

    # Mean label at peak
    peak_x = iq_to_x(100)
    peak_y = iq_to_y(100)
    d.text((peak_x - 60, peak_y - 60), "MEAN = 100",
           fill=MAROON, font=font("sans_bold", 30))

    # Band percentages above the bands
    band_label_y = base_y + 70
    # ±1 SD = 68%
    cx_1 = (iq_to_x(85) + iq_to_x(115)) / 2
    label_1 = "68%  within ±1 SD  (85–115)"
    lw = d.textlength(label_1, font=font("sans_bold", 28))
    d.text((cx_1 - lw / 2, band_label_y), label_1,
           fill=MAROON_DARK, font=font("sans_bold", 28))
    # ±2 SD = 95%
    cx_2 = (iq_to_x(70) + iq_to_x(130)) / 2
    label_2 = "95%  within ±2 SD  (70–130)"
    lw = d.textlength(label_2, font=font("sans_bold", 26))
    d.text((cx_2 - lw / 2, band_label_y + 50), label_2,
           fill=MUTED, font=font("sans", 26))

    # Tests note at top-right
    d.rounded_rectangle([W - 480, 200, W - 110, 380], radius=18,
                        outline=MAROON, width=4, fill=CREAM)
    d.text((W - 460, 220), "THE TESTS", fill=MAROON, font=font("sans_bold", 28))
    d.text((W - 460, 264), "·  Stanford-Binet  ·  1916", fill=INK, font=font("sans", 24))
    d.text((W - 460, 298), "·  WAIS  ·  adults", fill=INK, font=font("sans", 24))
    d.text((W - 460, 332), "·  WISC  ·  children", fill=INK, font=font("sans", 24))

    d.text((110, 945),
           "Score 130 → top 2.5%.   Score 70 → bottom 2.5%.   Memorize 68 / 95 / 99.",
           fill=MAROON_DARK, font=font("serif_bold", 28))
deck.custom("10_iq_distribution", iq_bell)

# ── 11 — Flynn effect (rising IQ over decades) ───────────────────────
def flynn(img, d):
    d.text((110, 60), "The Flynn effect.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 158), "Average IQ has been rising  ·  ~3 points per decade.",
           fill=MUTED, font=font("sans", 30))

    # Simple line chart: x = decade (1940..2020), y = IQ
    chart_x0 = 200
    chart_x1 = 1100
    chart_y0 = 280
    chart_y1 = 760

    # Frame
    d.line([(chart_x0, chart_y1), (chart_x1, chart_y1)], fill=MAROON_DARK, width=4)
    d.line([(chart_x0, chart_y0), (chart_x0, chart_y1)], fill=MAROON_DARK, width=4)

    # Decades
    decades = [1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
    iq_min = 95
    iq_max = 130
    def yx(decade, iq):
        x = chart_x0 + (decade - 1940) / (2020 - 1940) * (chart_x1 - chart_x0)
        y = chart_y1 - (iq - iq_min) / (iq_max - iq_min) * (chart_y1 - chart_y0)
        return x, y

    # Y axis labels
    for iq_v in [100, 110, 120, 130]:
        _, y = yx(1940, iq_v)
        d.line([(chart_x0 - 8, y), (chart_x0, y)], fill=MAROON_DARK, width=2)
        d.text((chart_x0 - 70, y - 14), str(iq_v),
               fill=MAROON_DARK, font=font("sans_bold", 24))

    # X axis labels
    for dec in decades:
        x, _ = yx(dec, iq_min)
        d.line([(x, chart_y1), (x, chart_y1 + 8)], fill=MAROON_DARK, width=2)
        lw = d.textlength(str(dec), font=font("sans", 22))
        d.text((x - lw / 2, chart_y1 + 14), str(dec),
               fill=MAROON_DARK, font=font("sans", 22))

    # Plot line — IQ at 1940 baseline = 100, +3 per decade re-normed
    # Since real-world tests are re-normed, we plot the un-renormed equivalent.
    pts = []
    for dec in decades:
        iq_v = 100 + (dec - 1940) / 10 * 3
        pts.append(yx(dec, iq_v))

    # Shade under curve
    poly = [pts[0]] + pts + [(pts[-1][0], chart_y1), (pts[0][0], chart_y1)]
    d.polygon(poly, fill=deck.accent_light)
    # Line
    d.line(pts, fill=MAROON, width=6)
    # Dots
    for x, y in pts:
        d.ellipse([x - 8, y - 8, x + 8, y + 8],
                  fill=MAROON, outline=MAROON_DARK, width=2)

    # Labels for endpoints
    x0, y0 = pts[0]
    d.text((x0 + 14, y0 - 10), "100", fill=MAROON, font=font("sans_bold", 26))
    x_e, y_e = pts[-1]
    d.text((x_e - 80, y_e - 40), "~124", fill=MAROON, font=font("sans_bold", 26))

    # Right-side panel — why
    rx = 1180
    ry = 280
    d.rounded_rectangle([rx, ry, rx + 630, ry + 480], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((rx + 24, ry + 20), "WHY IT'S RISING", fill=MAROON, font=font("sans_bold", 32))
    items = [
        "·  better nutrition",
        "·  more years of schooling",
        "·  smaller families  →  more attention",
        "·  more abstract thinking in daily life",
    ]
    for j, t in enumerate(items):
        d.text((rx + 24, ry + 90 + j * 50), t, fill=INK, font=font("sans", 28))

    # Bottom bar
    d.rounded_rectangle([rx + 14, ry + 320, rx + 616, ry + 460], radius=16,
                        fill=deck.accent_light)
    d.text((rx + 30, ry + 340), "Tests get re-normed every generation",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    d.text((rx + 30, ry + 380), "to keep the mean at 100.",
           fill=INK, font=font("sans", 24))
    d.text((rx + 30, ry + 420), "Not biologically smarter  —  better at THESE skills.",
           fill=INK, font=font("serif_ital", 22))

    d.text((110, 945), "James Flynn  ·  named after him  ·  one of the most replicated findings in psychology.",
           fill=MAROON_DARK, font=font("serif_bold", 28))
deck.custom("11_flynn", flynn)

# ── 12 — stereotype threat (Steele & Aronson) ────────────────────────
def stereotype_threat(img, d):
    d.text((110, 60), "Stereotype threat.  Steele & Aronson, 1995.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 138), "Same test. Different framing. Different score.",
           fill=MUTED, font=font("sans", 30))

    # Two condition cards
    conditions = [
        (110, 220,
         "GROUP A",
         "told it measured",
         "VERBAL ABILITY",
         "↓  scored significantly lower",
         RED),
        (1000, 220,
         "GROUP B",
         "told it was a",
         "PROBLEM-SOLVING EXERCISE",
         "↑  scored at expected level",
         deck.accent),
    ]
    for x, y, label, line1, line2, verdict, color in conditions:
        d.rounded_rectangle([x, y, x + 810, y + 460], radius=24,
                            outline=color, width=6, fill=deck.card_bg)
        d.text((x + 30, y + 24), label, fill=color, font=font("sans_bold", 40))
        d.text((x + 30, y + 100), line1, fill=INK, font=font("sans", 32))
        # Highlight box
        d.rounded_rectangle([x + 30, y + 160, x + 780, y + 260], radius=14,
                            fill=deck.accent_light, outline=color, width=3)
        # center inside highlight
        f_h = font("sans_bold", 36)
        tw = d.textlength(line2, font=f_h)
        d.text((x + 30 + (750 - tw) / 2, y + 195), line2, fill=MAROON_DARK, font=f_h)
        d.text((x + 30, y + 320), verdict, fill=color,
               font=font("serif_bold", 36))

    # Mechanism explainer at bottom
    d.rounded_rectangle([110, 720, W-110, 970], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Why?  Fear of confirming a stereotype  →  cognitive load  →  performance drops.",
             font("serif_bold", 36), 750, MAROON_DARK)
    centered(d, "Replicated with women on math tests.   Same effect.",
             font("sans_bold", 32), 820, MAROON_DARK)
    centered(d, "The test wasn't the problem.  The framing was.",
             font("serif_bold", 38), 880, MAROON_DARK)
deck.custom("12_stereotype_threat", stereotype_threat)

# ── 13 — recap ───────────────────────────────────────────────────────
deck.recap("13_recap", "Recap.", [
    "Three test-quality criteria — reliability, validity, standardization.",
    "Reliability = test-retest, split-half, inter-rater.  Validity = content, construct, criterion.",
    "Spearman 1 (g)  ·  Gardner 8 (weak support)  ·  Sternberg 3 (analytical, creative, practical).",
    "IQ tests: Stanford-Binet, WAIS, WISC.  Mean 100, SD 15, 68 / 95 / 99.",
    "Flynn effect — IQ rising ~3 points per decade.  Tests get re-normed.",
    "Bias matters — cultural bias in content, stereotype threat in framing (Steele & Aronson).",
])

# ── 14 — path ────────────────────────────────────────────────────────
deck.path("14_path", [
    ("✓",  "Watch this lesson",            "(done!)"),
    ("1.", "Read Myers Module 12",         "Testing & intelligence — esp. reliability vs. validity"),
    ("2.", "AP Classroom · 15 MCQ",        "Identify reliability vs. validity from short test descriptions"),
    ("3.", "Assignment in dashboard",       "10 test scenarios · label reliable, valid, both, or neither"),
    ("4.", "Advisor check-in",              "Book one if Gardner vs. Sternberg or R vs. V is still fuzzy"),
], next_text="Next up:  Module 13 — Abnormal Psychology.  Where does 'normal' end and 'disorder' begin?")

print("AP Psych Module 12 slides built.")

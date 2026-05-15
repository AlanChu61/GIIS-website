"""AP Psychology · Module 11 — Personality.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Custom diagrams: Freud's iceberg, OCEAN spectrum, defense mechanism gallery,
projective vs self-report compare, plus the standard kit primitives.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, CREAM,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=11, output_dir="slides", logo_path=LOGO)

# ── 01 — title ───────────────────────────────────────────────────────
deck.title("01_title", "AP Psychology",
           "Module 11 — Personality",
           "~8 minutes  ·  Why are you, you?")

# ── 02 — hook (shy at school vs loud at home) ────────────────────────
def hook(img, d):
    d.text((110, 80), "Same friend. Two rooms.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 168), "Which one is the real her?",
           fill=MAROON_DARK, font=font("serif_ital", 48))

    # Two contrasting cards — school vs home
    cards = [
        (110,  280, "AT SCHOOL",  "Quiet.  One friend.  Eyes on the floor.",  MAROON),
        (1000, 280, "AT HOME",    "Loud. Hilarious. Completely different.",   deck.accent),
    ]
    for x, y, label, desc, color in cards:
        d.rounded_rectangle([x, y, x + 810, y + 320], radius=24,
                            outline=color, width=6, fill=deck.card_bg)
        d.text((x + 30, y + 30), label, fill=color, font=font("sans_bold", 44))
        lines = wrap(d, desc, font("sans", 36), 750)
        for i, ln in enumerate(lines):
            d.text((x + 30, y + 130 + i * 50), ln, fill=INK, font=font("sans", 36))

    d.rounded_rectangle([110, 660, W-110, 880], radius=24, fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "Two personalities?  Or one personality + two contexts?",
             font("serif_bold", 44), 700, MAROON_DARK)
    centered(d, "Different theories give different answers. Today: which is which.",
             font("sans", 32), 780, MAROON_DARK)
    centered(d, "(And those online quizzes? Watered-down trait theory.)",
             font("serif_ital", 30), 830, MAROON_DARK)
deck.custom("02_hook", hook)

# ── 03 — overview ────────────────────────────────────────────────────
deck.overview("03_overview", "Game plan.", [
    "Four theories: psychoanalytic, humanistic, trait, social-cognitive.",
    "The Big Five (OCEAN) — the framework AP tests the most.",
    "How psychologists actually measure personality — and the AP trap.",
], footnote="By end: read a scenario, name the theory, name the assessment.")

# ── 04 — psychoanalytic (Freud's iceberg + id/ego/superego) ──────────
def psychoanalytic(img, d):
    d.text((110, 70), "Freud's iceberg.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "Most of who you are is hidden — even from you.",
           fill=MUTED, font=font("sans", 32))

    # Iceberg lives in the CENTER region only — left and right panels stay clear
    ice_left, ice_right = 500, W - 500
    waterline_y = 400
    ice_bottom = 880
    # Sky region — light tint above (purple sky)
    d.rectangle([ice_left, 230, ice_right, waterline_y], fill=deck.accent_light)
    # Water region — deep tint below
    d.rectangle([ice_left, waterline_y, ice_right, ice_bottom + 30], fill=MAROON_DARK)

    # The iceberg — a triangle/polygon centered in the middle region
    cx = (ice_left + ice_right) // 2
    iceberg = [
        (cx - 80,  260),       # top point
        (cx + 80,  260),
        (cx + 260, waterline_y),
        (cx + 360, ice_bottom),   # bottom right
        (cx - 360, ice_bottom),   # bottom left
        (cx - 260, waterline_y),
    ]
    d.polygon(iceberg, fill=CREAM, outline=MAROON)

    # Waterline (only across the iceberg region, not the side panels)
    d.line([(ice_left, waterline_y), (ice_right, waterline_y)], fill=MAROON, width=4)
    # Waterline label sits in the small open-water gap on the LEFT,
    # between the iceberg's left edge at the waterline (cx-260) and ice_left.
    # Available space ≈ (cx-260) - ice_left = (960-260) - 500 = 200px wide.
    waterline_label = "waterline"
    d.text((ice_left + 14, waterline_y + 8), waterline_label,
           fill=CREAM, font=font("sans_bold", 22))
    d.text((ice_left + 14, waterline_y + 38), "= awareness",
           fill=CREAM, font=font("sans_bold", 22))

    # Conscious — at the iceberg tip, centered on cx
    label = "CONSCIOUS"
    lw = d.textlength(label, font=font("sans_bold", 26))
    d.text((cx - lw / 2, 268), label, fill=MAROON, font=font("sans_bold", 26))
    sub = "(tip — what you notice now)"
    sw = d.textlength(sub, font=font("sans", 18))
    d.text((cx - sw / 2, 302), sub, fill=INK, font=font("sans", 18))

    # Preconscious — just under waterline, centered on cx
    label = "PRECONSCIOUS"
    lw = d.textlength(label, font=font("sans_bold", 30))
    d.text((cx - lw / 2, waterline_y + 30), label, fill=MAROON, font=font("sans_bold", 30))
    sub = "stuff you can pull up if you try"
    sw = d.textlength(sub, font=font("sans", 22))
    d.text((cx - sw / 2, waterline_y + 75), sub, fill=INK, font=font("sans", 22))

    # Unconscious — deep, centered on cx
    label = "UNCONSCIOUS"
    lw = d.textlength(label, font=font("sans_bold", 36))
    d.text((cx - lw / 2, 720), label, fill=MAROON, font=font("sans_bold", 36))
    sub = "buried memories  ·  urges  ·  conflicts"
    sw = d.textlength(sub, font=font("sans", 22))
    d.text((cx - sw / 2, 770), sub, fill=INK, font=font("sans", 22))

    # Side panel — id/ego/superego layers (LEFT — fully outside iceberg region)
    panel_x = 110
    panel_y = 260
    d.rounded_rectangle([panel_x, panel_y, panel_x + 360, panel_y + 540], radius=18,
                        outline=MAROON, width=4, fill=CREAM)
    d.text((panel_x + 20, panel_y + 16), "PERSONALITY", fill=MAROON, font=font("sans_bold", 26))
    d.text((panel_x + 20, panel_y + 46), "= 3 parts",          fill=MUTED, font=font("sans", 22))

    parts = [
        ("SUPEREGO", "moral conscience", "\"don't you dare\""),
        ("EGO",      "realistic referee", "balances id & superego"),
        ("ID",       "pleasure-seeking", "\"I want it now\""),
    ]
    for i, (name, role, ex) in enumerate(parts):
        py = panel_y + 100 + i * 145
        d.rounded_rectangle([panel_x + 16, py, panel_x + 344, py + 130], radius=12,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((panel_x + 28, py + 12), name, fill=deck.accent, font=font("sans_bold", 30))
        d.text((panel_x + 28, py + 54), role, fill=INK,         font=font("sans", 24))
        d.text((panel_x + 28, py + 88), ex,   fill=MUTED,       font=font("serif_ital", 22))

    # Right panel — psychosexual stages (brief mention)
    rp_x = W - 470
    rp_y = 260
    d.rounded_rectangle([rp_x, rp_y, rp_x + 360, rp_y + 240], radius=18,
                        outline=MAROON, width=4, fill=CREAM)
    d.text((rp_x + 20, rp_y + 16), "PSYCHOSEXUAL", fill=MAROON, font=font("sans_bold", 26))
    d.text((rp_x + 20, rp_y + 46), "STAGES (brief)",  fill=MUTED, font=font("sans", 22))
    stages = ["oral", "anal", "phallic", "latency", "genital"]
    for i, s in enumerate(stages):
        d.text((rp_x + 28, rp_y + 90 + i * 28), f"·  {s}", fill=INK, font=font("sans", 24))
deck.custom("04_psychoanalytic", psychoanalytic)

# ── 05 — defense mechanisms gallery (3x2 grid of 6 cards) ────────────
def defenses(img, d):
    d.text((110, 70), "Defense mechanisms.", fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "Unconscious tricks the ego uses to keep you functioning.",
           fill=MUTED, font=font("sans", 32))

    items = [
        ("REPRESSION",      "pushing a painful memory out of awareness"),
        ("DENIAL",          "refusing to accept that it happened"),
        ("PROJECTION",      "\"I'm not jealous — YOU'RE jealous.\""),
        ("DISPLACEMENT",    "yelled at by boss → snap at the dog"),
        ("RATIONALIZATION", "\"I didn't really want that job anyway.\""),
        ("SUBLIMATION",     "channel rage into the gym  ·  the only healthy one"),
    ]
    cw, ch = 580, 220
    for i, (name, ex) in enumerate(items):
        col = i % 3
        row = i // 3
        x = 110 + col * (cw + 20)
        y = 240 + row * (ch + 20)
        is_sub = (name == "SUBLIMATION")
        outline = MAROON if is_sub else deck.accent
        fill_bg = deck.accent_light if is_sub else deck.card_bg
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=18,
                            outline=outline, width=5 if is_sub else 4, fill=fill_bg)
        d.text((x + 24, y + 22), name, fill=outline, font=font("sans_bold", 32))
        lines = wrap(d, ex, font("sans", 28), cw - 48)
        for j, ln in enumerate(lines[:4]):
            d.text((x + 24, y + 80 + j * 38), ln, fill=INK, font=font("sans", 28))

    # Footer cue: sublimation is the healthy one
    d.text((110, 945), "Five distort reality.   Sublimation REDIRECTS it — that's why it's the healthy one.",
           fill=MAROON_DARK, font=font("serif_bold", 30))
deck.custom("05_defenses", defenses)

# ── 06 — humanistic (Rogers + Maslow) ────────────────────────────────
deck.compare("06_humanistic", "Humanistic theory.",
    {"label": "ROGERS",
     "color": deck.accent,
     "lines": [
         "Unconditional positive regard.",
         "Self-concept.",
         "Real self vs. ideal self.",
         "Congruence = the two match.",
     ],
     "footnote": "Healthy personality grows in acceptance."},
    {"label": "MASLOW",
     "color": MAROON,
     "lines": [
         "Hierarchy of needs:",
         "physiological → safety →",
         "love → esteem →",
         "self-actualization (top).",
     ],
     "footnote": "Reach the top = the most you you can be."})

# ── 07 — Big Five OCEAN spectrum (5 horizontal bars) ─────────────────
def big_five(img, d):
    d.text((110, 60), "The Big Five  ·  OCEAN.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 144), "AP's most-tested personality framework.",
           fill=MUTED, font=font("sans", 30))

    traits = [
        ("O", "OPENNESS",          "cautious  ·  conventional",   "curious  ·  creative"),
        ("C", "CONSCIENTIOUSNESS", "spontaneous  ·  careless",    "organized  ·  disciplined"),
        ("E", "EXTRAVERSION",      "reserved  ·  energized alone", "outgoing  ·  energized by people"),
        ("A", "AGREEABLENESS",     "competitive  ·  skeptical",   "kind  ·  cooperative"),
        ("N", "NEUROTICISM",       "calm  ·  emotionally steady", "anxious  ·  emotionally reactive"),
    ]
    bar_x0 = 280
    bar_x1 = W - 110
    row_h  = 130
    bar_h  = 70
    y0 = 220
    for i, (letter, name, low, high) in enumerate(traits):
        y = y0 + i * row_h
        # Big letter on the left — square card
        d.rounded_rectangle([110, y + 12, 240, y + 12 + 100], radius=14,
                            outline=MAROON, width=4, fill=MAROON)
        centered_letter_x = 110 + (240 - 110) // 2
        lw = d.textlength(letter, font=font("serif_bold", 80))
        d.text((centered_letter_x - lw / 2, y + 14), letter,
               fill=CREAM, font=font("serif_bold", 80))

        # Trait name ABOVE the bar
        d.text((bar_x0, y + 8), name, fill=MAROON, font=font("sans_bold", 28))

        # Spectrum bar
        bar_top = y + 50
        d.rounded_rectangle([bar_x0, bar_top, bar_x1, bar_top + bar_h], radius=18,
                            outline=deck.accent, width=3, fill=deck.accent_light)
        # Low end (left)
        low_text = "low: " + low
        d.text((bar_x0 + 18, bar_top + 18), low_text, fill=INK, font=font("sans", 26))
        # High end (right)
        high_text = "high: " + high
        hw = d.textlength(high_text, font=font("sans", 26))
        d.text((bar_x1 - hw - 18, bar_top + 18), high_text, fill=INK, font=font("sans", 26))

    d.text((110, 945), "Cross-culture, cross-decade, millions of people  ·  these five hold up.",
           fill=MAROON_DARK, font=font("serif_bold", 28))
deck.custom("07_traits_big5", big_five)

# ── 08 — pause + try (extraversion / social-cognitive) ───────────────
# Pause helper centers the "equation" at 130pt, so it must be SHORT.
# Any longer prompt goes into hint at smaller size to avoid overflow.
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Roommate: 'You're such an introvert.'",
           "name the trait.",
           hint="Then: would a social-cognitive theorist agree?  ·  Pause. Decide. Press play.")

# ── 09 — pause answer (custom — trait answer + social-cognitive pushback) ─
def pause_answer(img, d):
    d.text((110, 80), "Trait says one thing. Social-cognitive pushes back.",
           fill=MAROON, font=font("serif_bold", 56))

    # Two columns
    cols = [
        ("TRAIT THEORIST",
         "Low extraversion  =  introversion. The E in OCEAN. A stable trait that travels with her room to room.",
         deck.accent),
        ("SOCIAL-COGNITIVE THEORIST",
         "Maybe she's not introverted as a trait. New cafeteria, new strangers, new behavior. Put her in her dorm with her best friend — different person.",
         MAROON),
    ]
    for i, (title, body, color) in enumerate(cols):
        x = 110 + i * 870
        d.rounded_rectangle([x, 240, x + 760, 660], radius=24, outline=color, width=5, fill=deck.card_bg)
        d.text((x + 30, 270), title, fill=color, font=font("sans_bold", 38))
        lines = wrap(d, body, font("sans", 32), 700)
        for j, ln in enumerate(lines):
            d.text((x + 30, 360 + j * 46), ln, fill=INK, font=font("sans", 32))

    d.rounded_rectangle([110, 720, W-110, 920], radius=24, fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "AP will ask which theory the QUESTION is testing.",
             font("serif_bold", 44), 750, MAROON_DARK)
    centered(d, "Trait = \"she IS\" introverted.   Social-cognitive = \"she ACTED\" introverted in this situation.",
             font("sans", 32), 830, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)

# ── 10 — social-cognitive (reciprocal determinism + self-efficacy) ───
def social_cognitive(img, d):
    d.text((110, 70), "Social-cognitive theory  ·  Bandura.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 158), "Personality lives in a triangle. Three forces. All push each other.",
           fill=MUTED, font=font("sans", 30))

    # Reciprocal determinism triangle
    cx, cy = 720, 600
    r = 220
    # Three corner positions for the triangle
    top    = (cx,         cy - r)
    bot_l  = (cx - 220,   cy + 180)
    bot_r  = (cx + 220,   cy + 180)

    # Draw arrows between the three nodes (double-headed — they all influence each other)
    nodes = [top, bot_l, bot_r]
    for i in range(3):
        a = nodes[i]
        b = nodes[(i + 1) % 3]
        d.line([a, b], fill=MAROON, width=6)
        # Arrowheads — small triangles at each end
        # forward arrow at b
        # midpoint for visual balance — keep it simple, just thick line with text labels

    # Node circles
    nodes_data = [
        (top,    "BEHAVIOR",   "what you do"),
        (bot_l,  "COGNITION",  "what you think"),
        (bot_r,  "ENVIRONMENT","what surrounds you"),
    ]
    for (px, py), label, sub in nodes_data:
        d.ellipse([px - 150, py - 110, px + 150, py + 110], outline=MAROON,
                  width=6, fill=deck.accent_light)
        # Center text inside circle
        lw = d.textlength(label, font=font("sans_bold", 32))
        d.text((px - lw / 2, py - 36), label, fill=MAROON, font=font("sans_bold", 32))
        sw = d.textlength(sub, font=font("sans", 22))
        d.text((px - sw / 2, py + 8), sub, fill=INK, font=font("sans", 22))

    # Right side — self-efficacy callout
    rp_x = 1240
    rp_y = 280
    d.rounded_rectangle([rp_x, rp_y, rp_x + 590, rp_y + 480], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((rp_x + 24, rp_y + 24), "SELF-EFFICACY", fill=MAROON, font=font("sans_bold", 40))
    d.text((rp_x + 24, rp_y + 80), "your belief in your ability",
           fill=INK, font=font("sans", 28))
    d.text((rp_x + 24, rp_y + 116), "to do a SPECIFIC thing.",
           fill=INK, font=font("sans", 28))

    d.text((rp_x + 24, rp_y + 190), "·  high in math → try harder problems",
           fill=INK, font=font("sans", 26))
    d.text((rp_x + 24, rp_y + 230), "·  low in dating → give up sooner",
           fill=INK, font=font("sans", 26))

    d.rounded_rectangle([rp_x + 14, rp_y + 320, rp_x + 576, rp_y + 460], radius=18,
                        fill=deck.accent_light)
    d.text((rp_x + 28, rp_y + 340), "Domain-specific.", fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((rp_x + 28, rp_y + 386), "High in coding,",  fill=INK, font=font("sans", 26))
    d.text((rp_x + 28, rp_y + 420), "low in dating — same brain.",
           fill=INK, font=font("sans", 26))

    # Footer line
    d.text((110, 945),
           "Reciprocal determinism  =  no single force is the boss.",
           fill=MAROON_DARK, font=font("serif_bold", 30))
deck.custom("10_social_cognitive", social_cognitive)

# ── 11 — assessment: projective vs self-report ───────────────────────
deck.compare("11_assessment", "How do you measure personality?",
    {"label": "PROJECTIVE TESTS",
     "color": MAROON,
     "lines": [
         "Show ambiguous image.",
         "Person 'projects' onto it.",
         "·  Rorschach inkblot",
         "·  TAT (Thematic Appercep.)",
     ],
     "footnote": "Low reliability + validity. Rare in modern research."},
    {"label": "SELF-REPORT",
     "color": deck.accent,
     "lines": [
         "Long questionnaires.",
         "·  MMPI — clinical disorders",
         "·  Big Five Inventory — traits",
         "MMPI = decades of validation.",
     ],
     "footnote": "TRAP: Big Five ≠ MMPI. Traits vs. clinical inventory."})

# ── 12 — real world ──────────────────────────────────────────────────
def real_world(img, d):
    d.text((110, 80), "You've already met all of this.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 168), "Personality theory is the operating system underneath everyday life.",
           fill=MUTED, font=font("sans", 30))

    items = [
        ("Job application personality quiz",      "Big Five inventory in disguise"),
        ("Dating app match score",                 "Big Five again, often"),
        ("Therapist asks about your childhood",   "psychoanalytic tradition"),
        ("Coach: 'BELIEVE you can take that shot'","Bandura's self-efficacy"),
        ("Friend: 'I'm just being myself'",        "Rogers' self-concept"),
    ]
    for i, (left, right) in enumerate(items):
        y = 270 + i * 110
        d.rounded_rectangle([110, y, W-110, y + 90], radius=14,
                            outline=deck.accent, width=3, fill=deck.card_bg)
        d.text((140, y + 24), left, fill=INK, font=font("sans_bold", 32))
        rt = "→  " + right
        rw = d.textlength(rt, font=font("sans", 30))
        d.text((W - 140 - rw, y + 28), rt, fill=deck.accent, font=font("sans", 30))

    d.text((110, 945), "Not museum stuff. The OS underneath every interview, app, advice column.",
           fill=MAROON_DARK, font=font("serif_bold", 28))
deck.custom("12_real_world", real_world)

# ── 13 — recap ───────────────────────────────────────────────────────
deck.recap("13_recap", "Recap.", [
    "Psychoanalytic — Freud — id, ego, superego — most of you is hidden.",
    "Defenses — repression, denial, projection, displacement, rationalization, sublimation.",
    "Humanistic — Rogers + Maslow — congruence + self-actualization.",
    "Trait — Big Five OCEAN — most-tested AP framework.",
    "Social-cognitive — Bandura — reciprocal determinism + self-efficacy.",
    "Assessment — projective (low reliability) vs. self-report; Big Five ≠ MMPI.",
])

# ── 14 — path ────────────────────────────────────────────────────────
deck.path("14_path", [
    ("✓",  "Watch this lesson",            "(done!)"),
    ("1.", "Read Myers Module 11",         "Personality — focus Big Five & defense mechanisms"),
    ("2.", "AP Classroom · 15 MCQ",        "Especially: name the defense mechanism + Big Five vs. MMPI"),
    ("3.", "Assignment in dashboard",       "10 scenarios · label the matching theory + concept"),
    ("4.", "Advisor check-in",              "Book one if the four theories are still blurring together"),
], next_text="Next up:  Module 12 — Testing & Intelligence.  Can one number measure smart?")

print("AP Psych Module 11 slides built.")

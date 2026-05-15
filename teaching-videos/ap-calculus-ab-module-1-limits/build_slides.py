"""AP Calculus AB · Module 1 — Limits & Continuity.

Built on slide_kit (math theme = gold + cream).
Limits are a visual idea, so several slides are custom drawings:
- the 'walking toward the wall' hook
- left/right one-sided number line
- 3 ways a limit can fail
- 3 flavors of discontinuity (mini-graphs)
- speedometer for the real-world tie-in
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Calculus AB", module_num=1, output_dir="slides", logo_path=LOGO)

# 01 — title
deck.title("01_title", "AP Calculus AB",
           "Module 1 — Limits & Continuity",
           "~6 minutes  ·  Where calculus actually starts")

# 02 — hook  (custom: walking-toward-the-wall, halfway each step)
def hook(img, d):
    d.text((110, 80), "Walk toward the wall —", fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 168), "but only halfway, each step.", fill=MAROON, font=font("serif_bold", 72))

    # The wall (right side)
    wall_x = 1500
    d.rectangle([wall_x, 320, wall_x + 60, 740], fill=MAROON)
    d.text((wall_x - 10, 770), "WALL", fill=MAROON, font=font("sans_bold", 40))

    # Person start (left)
    start_x = 220
    foot_y = 600
    # Tick marks at each halfway point
    positions = [start_x]
    cur = start_x
    for _ in range(7):
        cur = cur + (wall_x - cur) // 2
        positions.append(cur)

    # Ground line
    d.line([(140, foot_y), (wall_x, foot_y)], fill=MUTED, width=4)

    # Steps (arrows + dots) — getting smaller and smaller
    for i, (a, b) in enumerate(zip(positions[:-1], positions[1:])):
        # Dot at start of step
        d.ellipse([a-10, foot_y-10, a+10, foot_y+10], fill=deck.accent)
        # Arrow to next step
        d.line([(a+15, foot_y - 30), (b - 15, foot_y - 30)], fill=MAROON, width=4)
        # Tiny arrowhead
        d.polygon([(b-15, foot_y-30), (b-25, foot_y-38), (b-25, foot_y-22)], fill=MAROON)
    # Final dot (closest to wall — never touches)
    d.ellipse([positions[-1]-10, foot_y-10, positions[-1]+10, foot_y+10], fill=deck.accent)

    # Caption strip
    d.rounded_rectangle([110, 820, W-110, 940], radius=20, fill=deck.accent_light)
    centered(d, "You'll get arbitrarily close — but you'll never touch it.",
             font("sans_bold", 38), 838, MAROON_DARK)
    centered(d, "That gap shrinking toward zero  =  a limit.",
             font("serif_bold", 38), 888, MAROON_DARK)
deck.custom("02_hook", hook)

# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "What a limit is — and the notation.",
    "One-sided limits — and when a limit doesn't exist.",
    "Continuity — the three-condition test.",
], footnote="By the end: read a graph, name the limit and whether f is continuous.")

# 04 — what is a limit (definition card)
deck.definition("04_what_is_limit", "What's a limit?",
                "The value f(x) approaches as x sneaks up on a.",
                "Not f(a). The value you're heading toward — even if you never land on it.")

# 05 — notation (equation walkthrough)
deck.equation("05_notation", "Limit notation.", [
    ("lim  f(x)  =  L", INK,    "as x approaches a, f(x) approaches L"),
    ("x→a", MUTED,  "the arrow does the work — x gets close to a, never has to BE a"),
    ("'limit, as x approaches a, of f of x, equals L'", MAROON, "read it out loud once"),
])

# 06 — one-sided  (custom: number line with arrows from L and R)
def one_sided(img, d):
    d.text((110, 90), "Approaching from two sides.", fill=MAROON, font=font("serif_bold", 70))

    # Number line
    nl_y = 460
    d.line([(140, nl_y), (W-140, nl_y)], fill=INK, width=4)
    # Tick at 'a'
    a_x = 960
    d.line([(a_x, nl_y - 20), (a_x, nl_y + 20)], fill=MAROON, width=6)
    d.text((a_x - 14, nl_y + 38), "a", fill=MAROON, font=font("serif_bold", 60))

    # Arrows from left and right
    # left arrow
    for i in range(5):
        x_start = a_x - 350 + i * 50
        x_end = x_start + 40
        d.line([(x_start, nl_y - 80), (x_end, nl_y - 80)], fill=deck.accent, width=4)
        d.polygon([(x_end, nl_y-80), (x_end-10, nl_y-86), (x_end-10, nl_y-74)], fill=deck.accent)
    d.text((a_x - 380, nl_y - 150), "x → a⁻", fill=deck.accent, font=font("mono", 56))
    d.text((a_x - 380, nl_y - 95), "(left side)", fill=MUTED, font=font("sans", 28))

    # right arrow (pointing left, toward a from the right)
    for i in range(5):
        x_start = a_x + 350 - i * 50
        x_end = x_start - 40
        d.line([(x_end, nl_y - 80), (x_start, nl_y - 80)], fill=deck.accent, width=4)
        d.polygon([(x_end, nl_y-80), (x_end+10, nl_y-86), (x_end+10, nl_y-74)], fill=deck.accent)
    d.text((a_x + 130, nl_y - 150), "x → a⁺", fill=deck.accent, font=font("mono", 56))
    d.text((a_x + 130, nl_y - 95), "(right side)", fill=MUTED, font=font("sans", 28))

    # Bottom rule
    d.rounded_rectangle([110, 720, W-110, 940], radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    centered(d, "If left = right  →  the two-sided limit exists.",
             font("sans_bold", 40), 750, INK)
    centered(d, "If left ≠ right  →  the limit  D N E.",
             font("sans_bold", 40), 810, MAROON_DARK)
    centered(d, "(Does Not Exist — that's a valid AP answer.)",
             font("sans", 32), 870, MUTED)
deck.custom("06_one_sided", one_sided)

# 07 — DNE (3 ways limits fail) — small mini-graphs side by side
def dne(img, d):
    d.text((110, 80), "Three ways a limit can fail.", fill=MAROON, font=font("serif_bold", 64))

    # Three panels
    panel_w, panel_h = 480, 380
    panel_y = 220
    titles = ["JUMP", "INFINITY", "OSCILLATION"]
    for i, title in enumerate(titles):
        x0 = 100 + i * (panel_w + 30)
        d.rounded_rectangle([x0, panel_y, x0 + panel_w, panel_y + panel_h],
                            radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        d.text((x0 + 30, panel_y + 20), title, fill=MAROON, font=font("sans_bold", 36))

        # mini axes
        ax_y = panel_y + 230
        d.line([(x0 + 50, panel_y + 80), (x0 + 50, panel_y + panel_h - 30)], fill=MUTED, width=2)
        d.line([(x0 + 50, ax_y), (x0 + panel_w - 30, ax_y)], fill=MUTED, width=2)

        if title == "JUMP":
            # Two horizontal segments at different heights, with open/closed dots
            d.line([(x0 + 60, ax_y - 80), (x0 + 220, ax_y - 80)], fill=deck.accent, width=5)
            d.ellipse([x0+213, ax_y-87, x0+227, ax_y-73], outline=deck.accent, width=4, fill=deck.card_bg)  # open
            d.line([(x0 + 220, ax_y - 30), (x0 + 380, ax_y - 30)], fill=deck.accent, width=5)
            d.ellipse([x0+213, ax_y-37, x0+227, ax_y-23], fill=deck.accent)  # closed
            d.text((x0 + 100, panel_y + panel_h - 60), "left ≠ right", fill=INK, font=font("sans", 26))
        elif title == "INFINITY":
            # Asymptote — curve shooting up near x=a
            for k in range(40):
                xc = x0 + 60 + k * 4
                yc = ax_y - 30 - int(8000 / (220 - k * 4 + 1))
                if yc > panel_y + 80:
                    d.line([(xc, ax_y - 30), (xc, yc)], fill=deck.accent, width=2)
            d.line([(x0 + 220, panel_y + 70), (x0 + 220, ax_y + 30)], fill=MAROON, width=2)
            d.text((x0 + 100, panel_y + panel_h - 60), "→ ±∞", fill=INK, font=font("sans", 26))
        else:  # OSCILLATION
            # Squiggle that gets denser
            import math
            prev = None
            for k in range(80):
                xc = x0 + 60 + k * 4
                t = (80 - k) * 0.3
                yc = ax_y - 30 - int(40 * math.sin(t))
                if prev:
                    d.line([prev, (xc, yc)], fill=deck.accent, width=3)
                prev = (xc, yc)
            d.text((x0 + 80, panel_y + panel_h - 60), "never settles", fill=INK, font=font("sans", 26))

    # Caption strip
    d.rounded_rectangle([110, 660, W-110, 940], radius=20, fill=deck.accent_light)
    centered(d, "All three:  the limit  D N E.",
             font("serif_bold", 50), 700, MAROON_DARK)
    centered(d, "On the AP exam — DNE is a real, correct answer.",
             font("sans", 36), 770, MAROON_DARK)
    centered(d, "If you see a jump, an asymptote, or an oscillation: write DNE.",
             font("sans", 36), 820, MAROON_DARK)
deck.custom("07_dne", dne)

# 08 — pause + try
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Left side approaches 3.   Right side approaches 5.   What's the two-sided limit at  x = 2?",
           "lim  f(x)  =  ?",
           hint="Pause the video. Decide. Press play when you have an answer.")

# 09 — pause answer  (we re-render so the answer is on the slide, not just narrated)
def pause_answer(img, d):
    d.text((110, 80), "The answer.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 220), "Left-hand limit:", fill=INK, font=font("sans", 44))
    d.text((600, 220), "3", fill=deck.accent, font=font("mono", 60))
    d.text((110, 320), "Right-hand limit:", fill=INK, font=font("sans", 44))
    d.text((600, 320), "5", fill=deck.accent, font=font("mono", 60))

    d.rounded_rectangle([110, 460, W-110, 600], radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    centered(d, "3  ≠  5    →    two-sided limit  D N E",
             font("mono", 60), 500, MAROON_DARK)

    d.text((110, 700), "The one-sided limits each exist.", fill=INK, font=font("sans", 36))
    d.text((110, 750), "But the two-sided limit needs them to agree.", fill=INK, font=font("sans", 36))
    d.text((110, 800), "They don't — so DNE is the right answer.", fill=deck.accent, font=font("sans_bold", 36))
deck.custom("09_pause1_answer", pause_answer)

# 10 — continuity (definition with 3 conditions)
def continuity(img, d):
    d.text((110, 80), "Continuity at  x = a.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 200), "Draw through the point without lifting your pencil.",
           fill=MUTED, font=font("sans", 38))

    # 3 conditions in numbered cards
    conds = [
        ("1.", "f(a)  exists.",                  "The function has a value at a."),
        ("2.", "lim f(x)  exists  (x → a).",     "Both one-sided limits agree."),
        ("3.", "lim f(x)  =  f(a).",             "The limit equals the actual value."),
    ]
    for i, (num, headline, sub) in enumerate(conds):
        y = 320 + i * 170
        d.rounded_rectangle([110, y, W-110, y + 150], radius=20, outline=MAROON, width=3, fill=deck.card_bg)
        d.text((140, y + 30), num, fill=deck.accent, font=font("serif_bold", 56))
        d.text((230, y + 30), headline, fill=INK, font=font("mono", 52))
        d.text((230, y + 95), sub, fill=MUTED, font=font("sans", 30))

    d.text((110, 880), "All three. If even one fails — discontinuous at a.",
           fill=MAROON_DARK, font=font("sans_bold", 36))
deck.custom("10_continuity", continuity)

# 11 — 3 flavors of discontinuity (mini graphs again)
def three_kinds(img, d):
    d.text((110, 80), "Three flavors of discontinuity.", fill=MAROON, font=font("serif_bold", 64))

    panel_w, panel_h = 480, 380
    panel_y = 220
    kinds = [
        ("REMOVABLE",  "(a hole)"),
        ("JUMP",       "(steps)"),
        ("INFINITE",   "(asymptote)"),
    ]
    for i, (title, sub) in enumerate(kinds):
        x0 = 100 + i * (panel_w + 30)
        d.rounded_rectangle([x0, panel_y, x0 + panel_w, panel_y + panel_h],
                            radius=20, outline=MAROON, width=4, fill=deck.card_bg)
        d.text((x0 + 30, panel_y + 20), title, fill=MAROON, font=font("sans_bold", 36))
        d.text((x0 + 30, panel_y + 65), sub, fill=MUTED, font=font("sans", 26))

        ax_y = panel_y + 250
        d.line([(x0 + 50, panel_y + 110), (x0 + 50, panel_y + panel_h - 30)], fill=MUTED, width=2)
        d.line([(x0 + 50, ax_y), (x0 + panel_w - 30, ax_y)], fill=MUTED, width=2)

        if title == "REMOVABLE":
            # Diagonal line with one open circle in the middle
            d.line([(x0 + 60, ax_y + 40), (x0 + 420, ax_y - 100)], fill=deck.accent, width=5)
            mid_x, mid_y = x0 + 240, ax_y - 30
            d.ellipse([mid_x-9, mid_y-9, mid_x+9, mid_y+9], outline=deck.accent, width=4, fill=deck.card_bg)
        elif title == "JUMP":
            d.line([(x0 + 60, ax_y - 30), (x0 + 220, ax_y - 30)], fill=deck.accent, width=5)
            d.ellipse([x0+213, ax_y-37, x0+227, ax_y-23], outline=deck.accent, width=4, fill=deck.card_bg)
            d.line([(x0 + 220, ax_y - 100), (x0 + 420, ax_y - 100)], fill=deck.accent, width=5)
            d.ellipse([x0+213, ax_y-107, x0+227, ax_y-93], fill=deck.accent)
        else:  # INFINITE
            # vertical asymptote at panel center, curve approaches it
            for k in range(40):
                xc = x0 + 60 + k * 4
                yc = ax_y - 30 - int(7000 / (220 - k * 4 + 5))
                if yc > panel_y + 100:
                    d.line([(xc, ax_y - 30), (xc, yc)], fill=deck.accent, width=2)
            d.line([(x0 + 220, panel_y + 100), (x0 + 220, ax_y + 30)], fill=MAROON, width=2)

    d.rounded_rectangle([110, 660, W-110, 940], radius=20, fill=deck.accent_light)
    centered(d, "AP loves to ask — classify the discontinuity.",
             font("serif_bold", 44), 690, MAROON_DARK)
    centered(d, "Removable.   Jump.   Infinite.   Memorize the names.",
             font("sans_bold", 38), 770, MAROON_DARK)
    centered(d, "Hole?  Removable.   Step?  Jump.   Asymptote?  Infinite.",
             font("sans", 32), 830, MAROON_DARK)
deck.custom("11_three_kinds", three_kinds)

# 12 — real world (speedometer + instantaneous velocity)
def real_world(img, d):
    d.text((110, 80), "Where you've already used a limit.", fill=MAROON, font=font("serif_bold", 64))

    # Speedometer (circle, gauge needle)
    cx, cy, r = 480, 540, 220
    d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=MAROON, width=8, fill=deck.card_bg)
    d.ellipse([cx-r+30, cy-r+30, cx+r-30, cy+r-30], outline=MUTED, width=3)
    # tick marks
    import math
    for i in range(11):
        ang = math.radians(180 + i * 18)
        x1 = cx + (r-15) * math.cos(ang)
        y1 = cy + (r-15) * math.sin(ang)
        x2 = cx + (r-40) * math.cos(ang)
        y2 = cy + (r-40) * math.sin(ang)
        d.line([(x1, y1), (x2, y2)], fill=INK, width=4)
    # needle
    needle_ang = math.radians(180 + 5 * 18)
    nx = cx + (r-60) * math.cos(needle_ang)
    ny = cy + (r-60) * math.sin(needle_ang)
    d.line([(cx, cy), (nx, ny)], fill=deck.accent, width=10)
    d.ellipse([cx-12, cy-12, cx+12, cy+12], fill=MAROON)
    d.text((cx-50, cy+30), "55 mph", fill=MAROON_DARK, font=font("sans_bold", 38))

    # Right column explanation
    d.text((860, 280), "Instantaneous speed", fill=MAROON, font=font("serif_bold", 56))
    d.text((860, 360), "= average speed", fill=INK, font=font("sans", 40))
    d.text((860, 410), "  over a tiny interval", fill=INK, font=font("sans", 40))
    d.text((860, 460), "  ...as that interval", fill=INK, font=font("sans", 40))
    d.text((860, 510), "  shrinks toward zero.", fill=INK, font=font("sans", 40))

    d.rounded_rectangle([860, 600, W-100, 720], radius=20, fill=deck.accent)
    centered_x_left = 880
    d.text((centered_x_left, 625), "That limit  =  the derivative.", fill=MAROON_DARK, font=font("sans_bold", 36))
    d.text((centered_x_left, 670), "We define it formally in Module 3.", fill=MAROON_DARK, font=font("sans", 30))

    d.text((110, 870), "Your speedometer is doing calculus.  Right now.",
           fill=deck.accent, font=font("serif_bold", 40))
deck.custom("12_real_world", real_world)

# 13 — recap
deck.recap("13_recap", "Recap.", [
    "A limit is the value f(x) approaches — not f(a) itself.",
    "Notation:  lim (x → a) f(x) = L.   Read the arrow carefully.",
    "Two-sided limit needs left and right to agree.  Otherwise: DNE.",
    "Three ways to fail:  jump  ·  infinity  ·  oscillation.",
    "Continuity = three conditions:  f(a) exists, limit exists, they're equal.",
    "Three flavors of discontinuity:  removable  ·  jump  ·  infinite.",
])

# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",              "(done!)"),
    ("1.", "Read OpenStax Calc Vol 1, Ch 2", "Limits — graphical examples are gold"),
    ("2.", "Khan Academy AP Calc — Unit 1",  "20 problems · estimating limits from graphs/tables"),
    ("3.", "Assignment in dashboard",        "One function — limit estimated 3 ways (graph, table, substitution)"),
    ("4.", "AP Classroom · Unit 1 PPC",      "Personal Progress Check (FRQ + MCQ) when ready"),
], next_text="Next up:  Module 2 — Limit Laws and the Squeeze Theorem.")

print("AP Calc AB Module 1 slides built.")

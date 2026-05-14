"""AP Calculus AB · Module 3 — Composite, Implicit & Inverse Derivatives.

Built on slide_kit (math theme = gold + cream).

Custom slides:
- 02_hook              : balloon V(r(t)) and dV/dt = dV/dr · dr/dt
- 08_implicit_motivation : unit-circle graph x² + y² = 25 with tangent at (3,4)
- 17_selecting         : "which rule when?" decision table + nested example
"""
import sys
import math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H, wrap,
    INK, MAROON, MAROON_DARK, MUTED, RED, GRID,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Calculus AB", module_num=3, output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 3 — Composite, Implicit & Inverse Derivatives",
    "~9 minutes  ·  Unit 3  ·  FUN 3.1 – 3.6",
)


# ─── 02 — hook (custom: balloon + chained rates) ─────────────────────────
def hook(img, d):
    d.text((110, 80), "When one rate hides", fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 168), "inside another rate.", fill=MAROON, font=font("serif_bold", 70))

    # LEFT: Balloon
    bx, by, br = 480, 540, 180
    # subtle shadow + balloon body
    d.ellipse([bx - br, by - br, bx + br, by + br],
              outline=MAROON, width=8, fill=deck.accent_light)
    # highlight gleam
    d.ellipse([bx - br + 40, by - br + 40, bx - br + 110, by - br + 110],
              fill=deck.bg)
    # knot
    d.polygon([(bx - 18, by + br - 4), (bx + 18, by + br - 4),
               (bx + 8, by + br + 28), (bx - 8, by + br + 28)],
              fill=MAROON_DARK)
    # tie string
    d.line([(bx, by + br + 28), (bx, by + br + 100)], fill=MAROON_DARK, width=4)

    # arrows showing inflation (radius growing)
    for ang_deg in (210, 240, 300, 330):
        ang = math.radians(ang_deg)
        x1 = bx + (br - 30) * math.cos(ang)
        y1 = by + (br - 30) * math.sin(ang)
        x2 = bx + (br + 50) * math.cos(ang)
        y2 = by + (br + 50) * math.sin(ang)
        d.line([(x1, y1), (x2, y2)], fill=MAROON_DARK, width=5)
        # arrowhead
        d.ellipse([x2 - 7, y2 - 7, x2 + 7, y2 + 7], fill=MAROON_DARK)

    # labels — V, r, t
    d.text((bx - 22, by - 30), "V", fill=MAROON_DARK, font=font("serif_bold", 72))
    d.text((bx - 30 + br, by - 110), "r", fill=MAROON_DARK, font=font("serif_ital", 46))
    d.text((bx - 80, by + br + 110), "inflating over time  t",
           fill=MUTED, font=font("sans", 28))

    # RIGHT: V → r → t cascade + chain rule
    gx0 = 950
    # cascade boxes
    box_w, box_h = 280, 110
    gap_y = 50
    # box 1
    d.rounded_rectangle([gx0, 280, gx0 + box_w, 280 + box_h], radius=18,
                        outline=MAROON, width=4, fill=deck.card_bg)
    centered_x = gx0 + box_w // 2
    tw = d.textlength("V depends on r", font=font("sans_bold", 32))
    d.text((centered_x - tw / 2, 310), "V depends on r", fill=INK, font=font("sans_bold", 32))
    # arrow
    d.line([(centered_x, 280 + box_h), (centered_x, 280 + box_h + gap_y)],
           fill=MAROON, width=4)
    d.polygon([(centered_x - 10, 280 + box_h + gap_y - 12),
               (centered_x + 10, 280 + box_h + gap_y - 12),
               (centered_x, 280 + box_h + gap_y + 4)],
              fill=MAROON)
    # box 2
    y2 = 280 + box_h + gap_y + 10
    d.rounded_rectangle([gx0, y2, gx0 + box_w, y2 + box_h], radius=18,
                        outline=MAROON, width=4, fill=deck.card_bg)
    tw = d.textlength("r depends on t", font=font("sans_bold", 32))
    d.text((centered_x - tw / 2, y2 + 30), "r depends on t", fill=INK, font=font("sans_bold", 32))
    # arrow
    d.line([(centered_x, y2 + box_h), (centered_x, y2 + box_h + gap_y)],
           fill=MAROON, width=4)
    d.polygon([(centered_x - 10, y2 + box_h + gap_y - 12),
               (centered_x + 10, y2 + box_h + gap_y - 12),
               (centered_x, y2 + box_h + gap_y + 4)],
              fill=MAROON)
    # box 3 — nested V(r(t))
    y3 = y2 + box_h + gap_y + 10
    d.rounded_rectangle([gx0, y3, gx0 + box_w, y3 + box_h], radius=18,
                        outline=MAROON_DARK, width=5, fill=deck.accent_light)
    tw = d.textlength("V( r( t ) )", font=font("mono", 44))
    d.text((centered_x - tw / 2, y3 + 28), "V( r( t ) )", fill=MAROON_DARK,
           font=font("mono", 44))

    # Big chain-rule equation strip to the right of cascade
    eq_x = gx0 + box_w + 60
    # vertical separator
    d.line([(eq_x - 30, 280), (eq_x - 30, y3 + box_h)], fill=MUTED, width=2)
    d.text((eq_x, 320), "Multiply", fill=MAROON, font=font("sans_bold", 36))
    d.text((eq_x, 370), "the rates:", fill=MAROON, font=font("sans_bold", 36))
    d.text((eq_x, 470), "dV", fill=INK, font=font("mono", 56))
    d.line([(eq_x, 540), (eq_x + 80, 540)], fill=INK, width=3)
    d.text((eq_x + 8, 548), "dt", fill=INK, font=font("mono", 50))
    d.text((eq_x + 110, 500), "=", fill=INK, font=font("mono", 56))
    d.text((eq_x + 180, 470), "dV", fill=MAROON, font=font("mono", 56))
    d.line([(eq_x + 180, 540), (eq_x + 260, 540)], fill=MAROON, width=3)
    d.text((eq_x + 188, 548), "dr", fill=MAROON, font=font("mono", 50))
    d.text((eq_x + 290, 500), "·", fill=INK, font=font("mono", 56))
    d.text((eq_x + 340, 470), "dr", fill=MAROON, font=font("mono", 56))
    d.line([(eq_x + 340, 540), (eq_x + 420, 540)], fill=MAROON, width=3)
    d.text((eq_x + 348, 548), "dt", fill=MAROON, font=font("mono", 50))

    # Caption strip
    d.rounded_rectangle([110, 880, W - 110, 1000], radius=20, fill=deck.accent_light)
    centered(d, "When one rate is nested inside another — multiply them.",
             font("sans_bold", 34), 895, MAROON_DARK)
    centered(d, "That's the chain rule. The single most useful tool in calculus.",
             font("serif_bold", 36), 942, MAROON_DARK)


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Chain rule — for any composite  f(g(x)).",
        "Implicit differentiation — when y is tangled with x.",
        "Inverse-function & inverse-trig derivatives.",
    ],
    footnote="By the end, you can differentiate almost anything the AP exam throws at you.",
)


# ─── 04 — chain intuition (definition) ───────────────────────────────────
deck.definition(
    "04_chain_intuition", "Composite function.",
    "(f ∘ g)(x)  =  f( g(x) )",
    "Peel the onion from the outside in:  inner first, outer last.",
)


# ─── 05 — chain rule (equation, two forms) ───────────────────────────────
deck.equation(
    "05_chain_rule", "Chain Rule  ·  FUN 3.1",
    [
        ("d/dx [ f(g(x)) ]  =  f'(g(x)) · g'(x)", MAROON, "prime form"),
        ("dy/dx  =  (dy/du) · (du/dx)",           INK,    "Leibniz form,  u = g(x)"),
        ("OUTSIDE derivative at the inside  ×  INSIDE derivative",
         MUTED, "you'll use this dozens of times per AP exam"),
    ],
)


# ─── 06 — three worked chain-rule examples ───────────────────────────────
deck.equation(
    "06_chain_examples", "Chain Rule — three examples.",
    [
        ("d/dx [ sin(3x²) ]    =  cos(3x²) · 6x",        MAROON, "outside: cos · inside: 6x"),
        ("d/dx [ (2x+1)⁵ ]     =  5(2x+1)⁴ · 2",         INK,    "= 10(2x+1)⁴"),
        ("d/dx [ e^(x²) ]      =  e^(x²) · 2x",          MAROON, "outside · inside"),
    ],
)


# ─── 07 — chain-rule trap (compare) ──────────────────────────────────────
deck.compare(
    "07_chain_trap",
    "AP trap #1 — forgetting the inside derivative.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "d/dx [ sin(x²) ]",
            "      =  cos(x²)",
            "Stopped at the outside.",
            "Inside derivative dropped.",
        ],
        "footnote": "Most common chain-rule slip on the AP exam.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "d/dx [ sin(x²) ]",
            "      =  cos(x²) · 2x",
            "Outside  ·  inside.",
            "Always ask:  what's nested?",
        ],
        "footnote": "Outside-prime AT the inside, TIMES inside-prime.",
    },
)


# ─── 08 — implicit motivation (custom: unit-circle with tangent) ─────────
def implicit_motivation(img, d):
    d.text((110, 80), "A circle isn't a function of x —", fill=MAROON,
           font=font("serif_bold", 56))
    d.text((110, 152), "but every point on it has a slope.", fill=MAROON,
           font=font("serif_bold", 56))

    # Coordinate axes for the circle (radius 5)
    cx, cy = 720, 620
    scale = 60  # 1 unit = 60 px
    # axes
    d.line([(cx - 360, cy), (cx + 360, cy)], fill=INK, width=3)
    d.line([(cx, cy - 360), (cx, cy + 360)], fill=INK, width=3)
    # axis labels
    d.text((cx + 350, cy + 10), "x", fill=INK, font=font("serif_ital", 32))
    d.text((cx + 10, cy - 360), "y", fill=INK, font=font("serif_ital", 32))
    # tick marks
    for k in range(-5, 6):
        if k == 0: continue
        # x-axis ticks
        d.line([(cx + k * scale, cy - 6), (cx + k * scale, cy + 6)], fill=INK, width=2)
        # y-axis ticks
        d.line([(cx - 6, cy - k * scale), (cx + 6, cy - k * scale)], fill=INK, width=2)
    # gridlines (light)
    for k in range(-5, 6):
        if k == 0: continue
        d.line([(cx + k * scale, cy - 5 * scale), (cx + k * scale, cy + 5 * scale)],
               fill=GRID, width=1)
        d.line([(cx - 5 * scale, cy - k * scale), (cx + 5 * scale, cy - k * scale)],
               fill=GRID, width=1)
    # re-draw main axes on top of grid
    d.line([(cx - 5 * scale - 30, cy), (cx + 5 * scale + 30, cy)], fill=INK, width=3)
    d.line([(cx, cy - 5 * scale - 30), (cx, cy + 5 * scale + 30)], fill=INK, width=3)

    # The circle  x² + y² = 25  (radius 5 units)
    d.ellipse([cx - 5 * scale, cy - 5 * scale, cx + 5 * scale, cy + 5 * scale],
              outline=MAROON, width=6)

    # Point (3, 4) and tangent line
    px, py = cx + 3 * scale, cy - 4 * scale
    # tangent slope at (3, 4) on circle: -3/4
    slope = -3 / 4
    tlen = 200
    tx1, ty1 = px - tlen, py - tlen * slope * (-1)  # screen y inverted
    tx2, ty2 = px + tlen, py + tlen * slope * (-1)
    # actually screen y is inverted so a slope of -3/4 (math) means dy negative when dx positive,
    # which on screen means dy_screen = -(-3/4 * dx) = +3/4 * dx for positive dx
    # Let me redo this:
    # math slope -3/4: dy_math = -3/4 dx
    # screen y points down, so dy_screen = -dy_math = +3/4 dx
    # so on screen the tangent line goes up-right? No: dy_screen positive = moving DOWN on screen
    # so as dx increases, line goes DOWN by (3/4)dx on screen.
    # Recompute clean:
    dx = 200
    dy_screen = -slope * dx  # = +0.75*dx (line goes down on screen as x increases)
    # Wait: slope = -3/4 means dy_math/dx = -3/4. On screen, screen_y = -math_y.
    # So d(screen_y)/dx = -(-3/4) = 3/4. Positive screen_y is downward.
    # So as x increases by 200, screen_y increases by 150 (moves down).
    tx1, ty1 = px - dx, py - dy_screen
    tx2, ty2 = px + dx, py + dy_screen
    d.line([(tx1, ty1), (tx2, ty2)], fill=MAROON_DARK, width=5)

    # mark the point
    d.ellipse([px - 10, py - 10, px + 10, py + 10], fill=MAROON_DARK)
    d.text((px + 18, py - 38), "(3, 4)", fill=MAROON_DARK,
           font=font("serif_bold", 32))

    # Equation label
    d.rounded_rectangle([60, 320, 380, 460], radius=18,
                        outline=MAROON, width=4, fill=deck.card_bg)
    centered_eq_x = 220
    d.text((85, 340), "the curve:", fill=MAROON, font=font("sans_bold", 28))
    tw = d.textlength("x² + y² = 25", font=font("mono", 50))
    d.text((centered_eq_x - tw / 2, 390), "x² + y² = 25", fill=INK, font=font("mono", 50))

    # Question card
    d.rounded_rectangle([60, 500, 380, 730], radius=18,
                        outline=MAROON, width=4, fill=deck.accent_light)
    d.text((85, 520), "Question:", fill=MAROON_DARK,
           font=font("sans_bold", 28))
    d.text((85, 575), "How do we find", fill=MAROON_DARK,
           font=font("sans", 30))
    d.text((85, 620), "dy/dx without", fill=MAROON_DARK,
           font=font("sans", 30))
    d.text((85, 665), "isolating y?", fill=MAROON_DARK,
           font=font("sans_bold", 32))

    # Bottom strip
    d.rounded_rectangle([110, 880, W - 110, 990], radius=20, fill=deck.accent_light)
    centered(d, "Fails the vertical-line test — yet every point still has a tangent slope.",
             font("sans_bold", 32), 900, MAROON_DARK)
    centered(d, "We need a new trick:  IMPLICIT differentiation.",
             font("serif_bold", 36), 945, MAROON_DARK)


deck.custom("08_implicit_motivation", implicit_motivation)


# ─── 09 — implicit method (equation, 3-step + worked example) ────────────
deck.equation(
    "09_implicit_method", "Implicit differentiation  ·  FUN 3.2",
    [
        ("1.  d/dx both sides — every y picks up dy/dx", INK,    "treat y as a function of x"),
        ("2.  Collect all dy/dx terms on one side",       INK,    None),
        ("3.  Solve algebraically for dy/dx",             INK,    None),
        ("x² + y² = 25  →  2x + 2y·(dy/dx) = 0",          MUTED,  "step 1 applied"),
        ("dy/dx = − x / y     at (3, 4):  − 3/4",         MAROON, "the tangent slope"),
    ],
)


# ─── 10 — implicit trap (compare) ────────────────────────────────────────
deck.compare(
    "10_implicit_trap",
    "Implicit trap — every y has a chain-rule tail.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "d/dx [ y² ]  =  2y",
            "Treated y like a constant.",
            "Chain rule was skipped.",
            "Everything downstream is off.",
        ],
        "footnote": "Sign errors when isolating dy/dx also sink the problem.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "d/dx [ y² ]  =  2y · dy/dx",
            "y is a function of x.",
            "So chain-rule it.",
            "Every y term gets a dy/dx.",
        ],
        "footnote": "Give every y its dy/dx tail.  Then collect and solve.",
    },
)


# ─── 11 — pause-and-try ──────────────────────────────────────────────────
deck.pause(
    "11_pause1", "PAUSE  &  TRY",
    "Find  dy/dx  for the curve below — use implicit differentiation:",
    "x² + xy + y² = 7",
    hint="Product rule on the  x·y  term.  Pause. Solve. Press play when ready.",
)

# ─── 12 — pause silence (duplicate of 11) ────────────────────────────────
deck.duplicate("11_pause1", "12_pause1_silence")


# ─── 13 — inverse-function derivative (equation) ─────────────────────────
deck.equation(
    "13_inverse_fn", "Inverse-function derivative  ·  FUN 3.3",
    [
        ("(f⁻¹)'(b)  =  1 / f'( f⁻¹(b) )",            MAROON, "reciprocal at the matching point"),
        ("Need:  f is one-to-one  AND  f'(f⁻¹(b)) ≠ 0", MUTED,  "otherwise the inverse has a vertical tangent"),
        ("f(x) = x³ + x + 1    f(0) = 1  ⇒  f⁻¹(1) = 0", INK,   "find the matching x first"),
        ("f'(x) = 3x² + 1    f'(0) = 1",                 INK,    "evaluate f' at that x"),
        ("(f⁻¹)'(1)  =  1 / 1  =  1",                    MAROON, "answer"),
    ],
)


# ─── 14 — inverse-trig table (equation) ──────────────────────────────────
deck.equation(
    "14_inverse_trig", "Inverse-trig derivatives  ·  FUN 3.4",
    [
        ("d/dx [ arcsin x ]  =   1 / √(1 − x²)",      MAROON, "function on [−1, 1], derivative on (−1, 1)"),
        ("d/dx [ arccos x ]  =  − 1 / √(1 − x²)",     INK,    "same domain caveat — minus sign"),
        ("d/dx [ arctan x ]  =   1 / (1 + x²)",       MAROON, "differentiable everywhere on ℝ"),
        ("if argument is  u(x) — chain in  u'(x)",    MUTED,  "don't forget the inside derivative"),
    ],
)


# ─── 15 — arcsin notation trap (compare) ─────────────────────────────────
deck.compare(
    "15_arcsin_trap",
    "AP trap #2 — sin⁻¹ does NOT mean reciprocal.",
    left={
        "label": "✗ WRONG READING",
        "color": RED,
        "lines": [
            "sin⁻¹(x)  =  1 / sin(x)",
            "That would be cosecant.",
            "csc x is the reciprocal.",
            "This reading is always wrong.",
        ],
        "footnote": "Never read the −1 as a reciprocal exponent on a trig function.",
    },
    right={
        "label": "✓ RIGHT READING",
        "color": MAROON,
        "lines": [
            "sin⁻¹(x)  =  arcsin(x)",
            "The INVERSE function of sine.",
            "Output is an angle.",
            "Read context and parentheses.",
        ],
        "footnote": "On the AP exam, sin⁻¹ / cos⁻¹ / tan⁻¹ always mean arc-functions.",
    },
)


# ─── 16 — higher-order derivatives (equation) ────────────────────────────
deck.equation(
    "16_higher_order", "Higher-order derivatives  ·  FUN 3.6",
    [
        ("f''  =  (f')'      f'''  =  (f'')'",          INK,    "Leibniz:  d²y/dx²,  d³y/dx³"),
        ("f(x) = x⁴ − 2x² + 5",                          MUTED,  "polynomial warm-up"),
        ("f'(x) = 4x³ − 4x    f''(x) = 12x² − 4    f'''(x) = 24x", INK, None),
        ("For  x² + y² = 25:    d²y/dx²  =  − 25 / y³", MAROON, "substitute dy/dx back in"),
    ],
)


# ─── 17 — selecting procedures (custom decision card + nested example) ───
def selecting(img, d):
    d.text((110, 80), "Selecting procedures  ·  FUN 3.5",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160), "Look at the FORM of the expression — pick the matching tool.",
           fill=MUTED, font=font("sans", 32))

    # Decision table: 6 rows in a card
    rows = [
        ("Product  f(x) · g(x)",          "Product rule"),
        ("Quotient  f(x) / g(x)",         "Quotient rule"),
        ("Composite  f(g(x))",            "Chain rule"),
        ("Equation mixing  x  and  y",    "Implicit differentiation"),
        ("Inverse-function value",        "1 / f'(f⁻¹(x))"),
        ("arcsin / arccos / arctan",      "Inverse-trig table"),
    ]
    card_x0, card_y0 = 110, 230
    card_w, card_h = 1100, 540
    d.rounded_rectangle([card_x0, card_y0, card_x0 + card_w, card_y0 + card_h],
                        radius=20, outline=MAROON, width=4, fill=deck.card_bg)
    # header
    d.text((card_x0 + 30, card_y0 + 20), "FORM",
           fill=MAROON, font=font("sans_bold", 32))
    d.text((card_x0 + 580, card_y0 + 20), "TOOL",
           fill=MAROON, font=font("sans_bold", 32))
    d.line([(card_x0 + 20, card_y0 + 75), (card_x0 + card_w - 20, card_y0 + 75)],
           fill=MAROON, width=2)
    row_y = card_y0 + 90
    for form_txt, tool_txt in rows:
        d.text((card_x0 + 30, row_y), form_txt, fill=INK, font=font("mono", 30))
        d.text((card_x0 + 580, row_y), tool_txt, fill=MAROON, font=font("sans_bold", 30))
        row_y += 70

    # RIGHT card — nested example (the meta-skill)
    nx0 = card_x0 + card_w + 30
    nw = W - nx0 - 110
    d.rounded_rectangle([nx0, card_y0, nx0 + nw, card_y0 + card_h],
                        radius=20, outline=MAROON_DARK, width=5, fill=deck.accent_light)
    d.text((nx0 + 25, card_y0 + 20), "Nested example",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((nx0 + 25, card_y0 + 75), "d/dx [ x · sin(x²) ]",
           fill=INK, font=font("mono", 36))
    d.text((nx0 + 25, card_y0 + 145), "Outer = product",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((nx0 + 25, card_y0 + 185), "Inner =  sin(x²)  → chain",
           fill=MAROON, font=font("sans_bold", 28))
    d.line([(nx0 + 25, card_y0 + 240), (nx0 + nw - 25, card_y0 + 240)],
           fill=MAROON_DARK, width=2)
    d.text((nx0 + 25, card_y0 + 260), "= 1 · sin(x²)",
           fill=INK, font=font("mono", 30))
    d.text((nx0 + 25, card_y0 + 305), "    + x · cos(x²) · 2x",
           fill=INK, font=font("mono", 30))
    d.text((nx0 + 25, card_y0 + 380), "= sin(x²)",
           fill=MAROON, font=font("mono", 32))
    d.text((nx0 + 25, card_y0 + 425), "  + 2x²·cos(x²)",
           fill=MAROON, font=font("mono", 32))

    # Bottom strip — meta-rule
    d.rounded_rectangle([110, 810, W - 110, 960], radius=20, fill=deck.accent_light)
    centered(d, "AP problems NEST rules:  chain inside product, product inside implicit, chain inside chain.",
             font("sans_bold", 30), 830, MAROON_DARK)
    centered(d, "Identify the OUTERMOST structure first — then peel inward, layer by layer.",
             font("serif_bold", 32), 885, MAROON_DARK)


deck.custom("17_selecting", selecting)


# ─── 18 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "18_recap", "Recap.",
    [
        "Chain rule:  outside-prime at the inside  ×  inside-prime.",
        "Implicit:  every y picks up a  dy/dx,  then collect and solve.",
        "Inverse-function rule:  (f⁻¹)'(x)  =  1 / f'( f⁻¹(x) ).",
        "Inverse-trig table — and  sin⁻¹  means arcsin, NOT 1/sin.",
        "Higher-order derivatives = iterated. Seed of concavity & acceleration.",
    ],
    assignment=[
        "GIIS Assignment M3 — 12 mixed problems (all four techniques).",
        "Due before Module 4.  Submit in the Learn Portal.",
    ],
)


# ─── 19 — path ───────────────────────────────────────────────────────────
deck.path(
    "19_path",
    items=[
        ("✓",  "Watch this lesson",        "(done!)"),
        ("1.", "OpenStax Calculus Vol 1",  "Read sections 3.6 – 3.8 (chain, inverse, implicit)"),
        ("2.", "Khan Academy practice",    "AP Calc AB · Unit 3 — composite, implicit, inverse"),
        ("3.", "Assignment in dashboard",  "GIIS Assignment M3 — 12 mixed problems"),
        ("4.", "Advisor check-in",         "15-minute Zoom — bring your toughest implicit problem"),
    ],
    next_text="Next up:  Module 4 — Contextual Applications  (related rates, linear approximation, L'Hôpital).",
)


print("AP Calc AB Module 3 slides built.")

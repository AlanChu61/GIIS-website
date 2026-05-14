"""AP Calculus AB · Module 5 — MVT, EVT, and the Derivative Tests.

Built on slide_kit (math theme = gold + cream).
Custom slides:
- 02_hook              : highway + two toll booths + average-speed bubble + instant-speed callout
- 05_mvt_geometry      : curve with secant + parallel tangent at c
- 09_first_derivative_test : sign chart of f' with arrows and max/min markers
- 13_concavity         : concave-up vs concave-down cups with f'' signs
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
deck = Deck(course="AP Calculus AB", module_num=5, output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 5 — MVT, EVT & the Derivative Tests",
    "~9 minutes  ·  Unit 5(a) · FUN 5.1 – 5.7",
)


# ─── 02 — hook (custom: toll booths + highway + speed callouts) ──────────
def hook(img, d):
    d.text((110, 80), "The speed-trap theorem.",
           fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 178), "Average 75 mph between two toll booths  →  somewhere, your speedometer read exactly 75.",
           fill=MUTED, font=font("sans", 32))

    # Highway strip
    road_y = 470
    road_h = 130
    d.rectangle([110, road_y, W - 110, road_y + road_h], fill=(80, 80, 90))
    # Dashed center line
    dash_y = road_y + road_h // 2 - 4
    x = 150
    while x < W - 140:
        d.rectangle([x, dash_y, x + 40, dash_y + 8], fill=(240, 220, 120))
        x += 90

    # Toll booth A (left)
    booth_w, booth_h = 130, 170
    bxA = 160
    byA = road_y - booth_h + 30
    d.rectangle([bxA, byA, bxA + booth_w, byA + booth_h],
                fill=deck.card_bg, outline=MAROON, width=4)
    d.rectangle([bxA - 10, byA - 30, bxA + booth_w + 10, byA + 10],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((bxA + 18, byA - 22), "TOLL", fill=deck.bg, font=font("sans_bold", 28))
    d.text((bxA + 12, byA + 50), "12:00", fill=INK, font=font("mono", 30))
    d.text((bxA + 5, byA + 95), "noon", fill=MUTED, font=font("sans", 24))

    # Toll booth B (right)
    bxB = W - 160 - booth_w
    byB = byA
    d.rectangle([bxB, byB, bxB + booth_w, byB + booth_h],
                fill=deck.card_bg, outline=MAROON, width=4)
    d.rectangle([bxB - 10, byB - 30, bxB + booth_w + 10, byB + 10],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((bxB + 18, byB - 22), "TOLL", fill=deck.bg, font=font("sans_bold", 28))
    d.text((bxB + 12, byB + 50), "12:40", fill=INK, font=font("mono", 30))
    d.text((bxB - 5, byB + 95), "40 min later", fill=MUTED, font=font("sans", 22))

    # "50 miles" distance annotation between booths
    d.text((W // 2 - 80, byA - 50), "50 miles apart",
           fill=MAROON, font=font("sans_bold", 34))
    d.line([(bxA + booth_w + 20, byA - 15), (bxB - 20, byA - 15)],
           fill=MAROON, width=3)
    # arrowheads
    d.polygon([(bxA + booth_w + 20, byA - 15), (bxA + booth_w + 32, byA - 22),
               (bxA + booth_w + 32, byA - 8)], fill=MAROON)
    d.polygon([(bxB - 20, byA - 15), (bxB - 32, byA - 22),
               (bxB - 32, byA - 8)], fill=MAROON)

    # Car silhouette on the road
    car_cx = W // 2
    car_cy = road_y + road_h // 2 + 10
    d.rounded_rectangle([car_cx - 60, car_cy - 28, car_cx + 60, car_cy + 14],
                        radius=14, fill=deck.accent, outline=MAROON_DARK, width=3)
    d.rounded_rectangle([car_cx - 38, car_cy - 50, car_cx + 38, car_cy - 24],
                        radius=10, fill=deck.accent_light, outline=MAROON_DARK, width=3)
    d.ellipse([car_cx - 50, car_cy + 4, car_cx - 26, car_cy + 28], fill=INK)
    d.ellipse([car_cx + 26, car_cy + 4, car_cx + 50, car_cy + 28], fill=INK)

    # AVERAGE-SPEED bubble (under road)
    d.rounded_rectangle([200, 660, 900, 820], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((230, 680), "Average speed", fill=MAROON, font=font("sans_bold", 32))
    d.text((230, 730), "50 mi / (40/60 hr)", fill=INK, font=font("mono", 38))
    d.text((230, 778), "=  75 mph", fill=MAROON, font=font("mono", 36))

    # INSTANT bubble (under road, right side)
    d.rounded_rectangle([W - 900, 660, W - 200, 820], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    d.text((W - 870, 680), "Somewhere inside…", fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((W - 870, 730), "speedometer  =  75 mph", fill=MAROON_DARK, font=font("mono", 36))
    d.text((W - 870, 778), "instantaneous = average", fill=MAROON_DARK, font=font("sans_bold", 28))

    # Bottom strap callout
    d.rounded_rectangle([110, 870, W - 110, 990], radius=20, fill=self_accent_strap(deck))
    centered(d, "That's the Mean Value Theorem — instantaneous slope must hit the average slope at least once.",
             font("sans_bold", 32), 890, MAROON_DARK)
    centered(d, "The ticket is legal because calculus says it has to be true.",
             font("serif_bold", 32), 940, MAROON_DARK)


def self_accent_strap(deck):
    return deck.accent_light


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "Two existence theorems — MVT and EVT (what MUST be true).",
        "Critical points + First Derivative Test (where extrema live).",
        "Concavity + Second Derivative Test (the shape story).",
    ],
    footnote="Every layer is something the AP exam will absolutely ask you.",
)


# ─── 04 — MVT statement (definition card) ────────────────────────────────
deck.definition(
    "04_mvt_statement", "Mean Value Theorem  (FUN 5.1)",
    "∃ c ∈ (a, b) :  f'(c)  =  (f(b) − f(a)) / (b − a)",
    "If f is continuous on [a,b] AND differentiable on (a,b) — both hypotheses required.",
)


# ─── 05 — MVT geometry (custom: secant + parallel tangent) ───────────────
def mvt_geometry(img, d):
    d.text((110, 80), "MVT, geometrically.",
           fill=MAROON, font=font("serif_bold", 70))
    d.text((110, 170), "A tangent line, somewhere inside, parallel to the secant from  (a, f(a))  to  (b, f(b)).",
           fill=MUTED, font=font("sans", 32))

    # Graph area
    gx0, gy0 = 200, 260
    gw, gh = 1100, 620
    # axes
    d.line([(gx0, gy0 + gh), (gx0 + gw, gy0 + gh)], fill=INK, width=3)
    d.line([(gx0, gy0), (gx0, gy0 + gh)], fill=INK, width=3)
    d.text((gx0 + gw - 24, gy0 + gh + 12), "x", fill=INK, font=font("serif_ital", 32))
    d.text((gx0 - 32, gy0 - 8), "y", fill=INK, font=font("serif_ital", 32))

    # Build curve points — y = soft cubic-ish increasing curve
    # We want: monotone increase, but with varying slope so a single tangent matches secant slope somewhere in (a,b).
    # Param: k from 0..gw-20
    def curve_pt(k):
        xc = gx0 + 20 + k
        # Use a sigmoid-ish: starts shallow, steep middle, flattens
        t = k / (gw - 20)  # 0..1
        # value 0..1
        v = 0.15 * t + 0.85 * (t ** 1.6)
        yc = gy0 + gh - 30 - int(v * (gh - 80))
        return (xc, yc)

    pts = [curve_pt(k) for k in range(0, gw - 20, 4)]
    for a_pt, b_pt in zip(pts[:-1], pts[1:]):
        d.line([a_pt, b_pt], fill=MAROON, width=5)

    # Endpoints A = (a, f(a)) and B = (b, f(b))
    A = curve_pt(60)
    B = curve_pt(gw - 80)
    # Secant line from A to B (extended slightly)
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    sx_l = A[0] - int(dx * 0.05)
    sy_l = A[1] - int(dy * 0.05)
    sx_r = B[0] + int(dx * 0.05)
    sy_r = B[1] + int(dy * 0.05)
    d.line([(sx_l, sy_l), (sx_r, sy_r)], fill=MAROON_DARK, width=4)

    # Average slope:
    avg_slope = (B[1] - A[1]) / (B[0] - A[0])  # screen-y; negative because y axis is flipped

    # Find c such that tangent slope matches secant slope.
    # Numerical: sample many k, compute local slope via finite difference, pick best match.
    best_k = None
    best_diff = 1e9
    for k in range(60, gw - 80, 4):
        p0 = curve_pt(k - 4)
        p1 = curve_pt(k + 4)
        local = (p1[1] - p0[1]) / (p1[0] - p0[0])
        diff = abs(local - avg_slope)
        if diff < best_diff:
            best_diff = diff
            best_k = k
    C = curve_pt(best_k)

    # Tangent at C — parallel to secant
    tx_l = C[0] - 220
    ty_l = C[1] - int(220 * avg_slope)
    tx_r = C[0] + 220
    ty_r = C[1] + int(220 * avg_slope)
    d.line([(tx_l, ty_l), (tx_r, ty_r)], fill=deck.accent, width=6)

    # Dots and labels
    for P, lbl in [(A, "(a, f(a))"), (B, "(b, f(b))"), (C, "c")]:
        d.ellipse([P[0] - 10, P[1] - 10, P[0] + 10, P[1] + 10], fill=MAROON_DARK)
    d.text((A[0] - 130, A[1] + 18), "(a, f(a))", fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((B[0] + 16, B[1] - 18), "(b, f(b))", fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((C[0] + 14, C[1] - 56), "c", fill=MAROON, font=font("serif_bold", 36))
    d.text((C[0] - 60, C[1] + 18), "tangent here", fill=MAROON, font=font("sans_bold", 24))

    # Tick marks for a, b on x-axis
    d.line([(A[0], gy0 + gh - 6), (A[0], gy0 + gh + 14)], fill=INK, width=3)
    d.line([(B[0], gy0 + gh - 6), (B[0], gy0 + gh + 14)], fill=INK, width=3)
    d.text((A[0] - 8, gy0 + gh + 22), "a", fill=INK, font=font("serif_ital", 30))
    d.text((B[0] - 8, gy0 + gh + 22), "b", fill=INK, font=font("serif_ital", 30))
    d.line([(C[0], gy0 + gh - 6), (C[0], gy0 + gh + 14)], fill=MAROON, width=3)
    d.text((C[0] - 8, gy0 + gh + 22), "c", fill=MAROON, font=font("serif_ital", 30))

    # Side caption — worked example
    d.rounded_rectangle([1340, 280, W - 110, 600], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((1370, 305), "Example", fill=MAROON, font=font("serif_bold", 40))
    d.text((1370, 380), "f(x) = x²  on  [0, 2]", fill=INK, font=font("mono", 34))
    d.text((1370, 440), "avg slope  =  (4 − 0)/2  =  2", fill=MUTED, font=font("mono", 28))
    d.text((1370, 490), "f'(c) = 2c = 2", fill=INK, font=font("mono", 32))
    d.text((1370, 540), "→  c = 1", fill=MAROON, font=font("mono", 36))

    # Bottom strap
    d.rounded_rectangle([110, 920, W - 110, 1020], radius=18, fill=deck.accent_light)
    centered(d, "Average slope across the interval  =  instantaneous slope at c.",
             font("sans_bold", 32), 945, MAROON_DARK)


deck.custom("05_mvt_geometry", mvt_geometry)


# ─── 06 — EVT (definition card) ──────────────────────────────────────────
deck.definition(
    "06_evt", "Extreme Value Theorem  (FUN 5.2)",
    "f attains an absolute MAX and an absolute MIN on [a, b].",
    "Hypothesis: f is continuous on a closed, bounded interval [a, b].   Drop either → can fail (e.g. 1/x on (0,1]).",
)


# ─── 07 — critical points (definition card) ──────────────────────────────
deck.definition(
    "07_critical_points", "Critical points.",
    "c is critical  ⇔  f'(c) = 0  OR  f'(c) DNE  (and c in domain).",
    "Every extremum is a critical point — but NOT every CP is an extremum. (x³ at 0: f'(0)=0, no extremum.)",
)


# ─── 08 — increasing / decreasing (equation/rule card) ───────────────────
deck.equation(
    "08_increasing_decreasing", "Sign of f'  →  monotonicity.",
    [
        ("f'(x) > 0  on I    →    f is increasing on I",  INK,    "positive slope = climbing"),
        ("f'(x) < 0  on I    →    f is decreasing on I",  MAROON, "negative slope = falling"),
        ("Workflow:  find CPs  →  sign chart of f'  →  read intervals", MUTED,
         "the workhorse procedure"),
    ],
)


# ─── 09 — First Derivative Test (custom: sign chart) ─────────────────────
def first_derivative_test(img, d):
    d.text((110, 80), "First Derivative Test.",
           fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 180), "Classify a critical point by how f'  changes sign at it.",
           fill=MUTED, font=font("sans", 34))

    # Sign chart line
    line_y = 460
    line_xL = 200
    line_xR = W - 200
    d.line([(line_xL, line_y), (line_xR, line_y)], fill=INK, width=4)

    # Two critical points: c1 (max) and c2 (min)
    c1_x = line_xL + (line_xR - line_xL) // 3
    c2_x = line_xL + 2 * (line_xR - line_xL) // 3

    # Tick marks
    for cx, lbl in [(c1_x, "c₁  (max)"), (c2_x, "c₂  (min)")]:
        d.line([(cx, line_y - 18), (cx, line_y + 18)], fill=MAROON, width=4)
        d.ellipse([cx - 12, line_y - 12, cx + 12, line_y + 12], fill=MAROON)
        d.text((cx - 60, line_y + 36), lbl, fill=MAROON, font=font("sans_bold", 30))

    # Signs of f' in three intervals (above the line)
    sign_y = line_y - 90
    seg_centers = [
        (line_xL + (c1_x - line_xL) // 2, "+", "f' > 0"),
        ((c1_x + c2_x) // 2,                "−", "f' < 0"),
        (c2_x + (line_xR - c2_x) // 2,      "+", "f' > 0"),
    ]
    seg_colors = [MAROON, RED, MAROON]
    for (sx, sign, lbl), color in zip(seg_centers, seg_colors):
        tw = d.textlength(sign, font=font("serif_bold", 110))
        d.text((sx - tw / 2, sign_y - 90), sign, fill=color, font=font("serif_bold", 110))
        nw = d.textlength(lbl, font=font("mono", 34))
        d.text((sx - nw / 2, sign_y + 40), lbl, fill=color, font=font("mono", 34))

    # Arrows BELOW the line showing increasing / decreasing
    arrow_y = line_y + 130
    seg_arrows = [
        (line_xL + 30, c1_x - 30, "↗  increasing"),
        (c1_x + 30,    c2_x - 30, "↘  decreasing"),
        (c2_x + 30,    line_xR - 30, "↗  increasing"),
    ]
    for (ax_l, ax_r, lbl) in seg_arrows:
        d.line([(ax_l, arrow_y), (ax_r, arrow_y)], fill=deck.accent, width=6)
        # arrowhead at right end
        d.polygon([(ax_r, arrow_y), (ax_r - 18, arrow_y - 12), (ax_r - 18, arrow_y + 12)],
                  fill=deck.accent)
        mid_x = (ax_l + ax_r) // 2
        tw = d.textlength(lbl, font=font("sans_bold", 30))
        d.text((mid_x - tw / 2, arrow_y + 22), lbl, fill=MAROON_DARK, font=font("sans_bold", 30))

    # Rules card (bottom)
    d.rounded_rectangle([110, 780, W - 110, 1000], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((150, 800), "Rules", fill=MAROON, font=font("serif_bold", 36))
    d.text((150, 870), "+  →  −   at c    relative MAX",
           fill=INK, font=font("mono", 32))
    d.text((150, 920), "−  →  +   at c    relative MIN",
           fill=INK, font=font("mono", 32))
    d.text((1050, 870), "no sign change   →   neither (e.g. x³ at 0)",
           fill=MUTED, font=font("mono", 28))
    d.text((1050, 920), "example:  f = x³ − 3x   →   max −1,  min 1",
           fill=MAROON, font=font("mono", 28))


deck.custom("09_first_derivative_test", first_derivative_test)


# ─── 10 — pause-and-try ──────────────────────────────────────────────────
deck.pause(
    "10_pause1", "PAUSE  &  TRY",
    "Find all critical points of  f(x) = x³ − 12x  and classify each one with the First Derivative Test.",
    "x³ − 12x",
    hint="Solve  f'(x) = 3x² − 12 = 0,  then check the sign of f' on each side of every CP.",
)

# ─── 10_silence — duplicate of 10_pause1 ─────────────────────────────────
deck.duplicate("10_pause1", "10_pause1_silence")


# ─── 11 — pause solution (worked steps) ──────────────────────────────────
deck.equation(
    "11_pause1_solution", "Solution  ·  f(x) = x³ − 12x",
    [
        ("f'(x)  =  3x² − 12  =  3(x − 2)(x + 2)", INK,    "factor"),
        ("CPs at  x = ±2",                          MUTED,  "where f' = 0"),
        ("sign of f' :   + ,   − ,   +",            INK,    "test x = −3, 0, 3"),
        ("x = −2 :  + → −     relative MAX,  f(−2) = 16",  MAROON, "plus-to-minus"),
        ("x =  2 :  − → +     relative MIN,  f( 2) = −16", MAROON, "minus-to-plus"),
    ],
)


# ─── 12 — Candidates Test (equation/rule card) ───────────────────────────
deck.equation(
    "12_candidates_test", "Candidates Test  (FUN 5.5)  —  absolute extrema on [a, b].",
    [
        ("1.  List all critical points inside  [a, b]",        INK,    "f' = 0 or DNE"),
        ("2.  Add the endpoints  x = a  and  x = b",           INK,    "don't forget these"),
        ("3.  Evaluate f at every candidate",                  INK,    "plug in, compare"),
        ("largest  →  absolute MAX     smallest  →  absolute MIN", MAROON, "EVT guarantees they exist"),
    ],
)


# ─── 13 — concavity (custom: cup vs cap diagram) ─────────────────────────
def concavity(img, d):
    d.text((110, 80), "Concavity.",
           fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 180), "f''  reads the curvature  —  the shape story of the curve.",
           fill=MUTED, font=font("sans", 34))

    # Two panels: concave UP (left) and concave DOWN (right)
    panel_w = 800
    panel_h = 520
    gap = 80
    top_y = 270
    x_left = 130
    x_right = x_left + panel_w + gap

    # ── LEFT panel: concave UP ──
    d.rounded_rectangle([x_left, top_y, x_left + panel_w, top_y + panel_h],
                        radius=24, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((x_left + 40, top_y + 30), "f'' > 0   ·   concave UP",
           fill=MAROON, font=font("serif_bold", 44))
    d.text((x_left + 40, top_y + 90), "cup shape  ·  slopes increasing",
           fill=MUTED, font=font("sans", 30))

    # Draw a parabola y = x^2 sample (cup)
    cx0, cy0 = x_left + 100, top_y + 460
    cw = panel_w - 200
    ch = 300
    # axes
    d.line([(cx0, cy0), (cx0 + cw, cy0)], fill=INK, width=3)
    d.line([(cx0 + cw // 2, cy0 - ch), (cx0 + cw // 2, cy0 + 30)], fill=INK, width=3)
    # cup curve
    pts_up = []
    for k in range(-50, 51):
        xc = cx0 + cw // 2 + k * (cw // 2 // 50)
        yc = cy0 - int((k / 50) ** 2 * ch * 0.85)
        pts_up.append((xc, yc))
    for a_pt, b_pt in zip(pts_up[:-1], pts_up[1:]):
        d.line([a_pt, b_pt], fill=deck.accent, width=5)
    # small smile arc to make it readable
    d.text((cx0 + cw // 2 - 18, cy0 - 350), "↑", fill=MAROON, font=font("sans_bold", 40))

    # ── RIGHT panel: concave DOWN ──
    d.rounded_rectangle([x_right, top_y, x_right + panel_w, top_y + panel_h],
                        radius=24, outline=MAROON, width=4, fill=deck.card_bg)
    d.text((x_right + 40, top_y + 30), "f'' < 0   ·   concave DOWN",
           fill=MAROON, font=font("serif_bold", 44))
    d.text((x_right + 40, top_y + 90), "cap shape  ·  slopes decreasing",
           fill=MUTED, font=font("sans", 30))

    cx1, cy1 = x_right + 100, top_y + 200
    # axes for cap
    d.line([(cx1, cy1 + 200), (cx1 + cw, cy1 + 200)], fill=INK, width=3)
    d.line([(cx1 + cw // 2, cy1 + 200 - ch), (cx1 + cw // 2, cy1 + 230)], fill=INK, width=3)
    # cap curve y = -x^2
    pts_dn = []
    for k in range(-50, 51):
        xc = cx1 + cw // 2 + k * (cw // 2 // 50)
        yc = cy1 + 200 - ch + int((k / 50) ** 2 * ch * 0.85)
        # clip
        if yc > cy1 + 200:
            yc = cy1 + 200
        pts_dn.append((xc, yc))
    for a_pt, b_pt in zip(pts_dn[:-1], pts_dn[1:]):
        d.line([a_pt, b_pt], fill=deck.accent, width=5)
    d.text((cx1 + cw // 2 - 18, cy1 - 50), "↓", fill=MAROON, font=font("sans_bold", 40))

    # Inflection-point strap
    d.rounded_rectangle([110, 820, W - 110, 1000], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    centered(d, "Inflection point  =  where  f''  CHANGES SIGN  (and f is defined there).",
             font("sans_bold", 36), 845, MAROON_DARK)
    centered(d, "Just  f''(c) = 0  is NOT enough — you must verify the sign change.",
             font("sans", 32), 905, MAROON_DARK)
    centered(d, "(e.g.  f(x) = x⁴  has  f''(0) = 0  but f'' never changes sign at 0.)",
             font("sans", 28), 955, MAROON_DARK)


deck.custom("13_concavity", concavity)


# ─── 14 — Second Derivative Test (definition / rule card) ────────────────
deck.equation(
    "14_second_derivative_test", "Second Derivative Test  (FUN 5.7)",
    [
        ("If  f'(c) = 0  and  f''(c) > 0      relative MIN at c", MAROON, "cup at the bottom"),
        ("If  f'(c) = 0  and  f''(c) < 0      relative MAX at c", MAROON, "cap at the top"),
        ("If  f''(c) = 0      INCONCLUSIVE  —  use First Derivative Test instead",
         RED, "x⁴ vs x³ — same f''(0) = 0, different behavior"),
        ("Verify:  f = x³ − 12x  at  x = 2 :  f''(2) = 12 > 0   →   relative MIN",
         INK, "matches our pause-and-try"),
    ],
)


# ─── 15 — compare trap ───────────────────────────────────────────────────
deck.compare(
    "15_compare_trap",
    "AP trap  —  f'(c) = 0  does NOT mean extremum.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "f(x) = x³,  so  f'(0) = 0.",
            "Therefore  x = 0  is a relative min.",
            "(Conclusion from f' = 0 alone.)",
            "AP loses you the point.",
        ],
        "footnote": "Critical point ≠ extremum.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "f'(x) = 3x²  ≥  0  for all x.",
            "So  f'  does NOT change sign at 0.",
            "x = 0  is a CP — neither max nor min.",
            "It's actually an inflection point.",
        ],
        "footnote": "Verify a sign change in f',  or use the 2nd Derivative Test.",
    },
)


# ─── 16 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "16_recap", "Recap.",
    [
        "MVT — continuous on [a,b] + differentiable on (a,b) → some c with f'(c) = avg slope.",
        "EVT — continuous on closed bounded [a,b] → absolute MAX and MIN exist.",
        "Critical point — f'(c) = 0 or DNE. Necessary, not sufficient, for an extremum.",
        "First Derivative Test — classify by sign change of f' at the CP.",
        "Candidates Test — evaluate f at every CP and both endpoints; pick largest / smallest.",
        "Second Derivative Test — f'' > 0 min, f'' < 0 max, f'' = 0 inconclusive.",
    ],
    assignment=[
        "GIIS Assignment 5a  ·  8 problems:",
        "  · 2 MVT verifications  · 2 First-Derivative-Test classifications",
        "  · 2 Candidates Test on closed intervals  · 2 Second-Derivative-Test (incl. one f''=0 case)",
    ],
)


# ─── 17 — path ───────────────────────────────────────────────────────────
deck.path(
    "17_path",
    items=[
        ("✓",  "Watch this lesson",         "(done!)"),
        ("1.", "OpenStax Calculus Vol 1",   "Chapters 4.3, 4.4, 4.5, 4.6"),
        ("2.", "Khan Academy practice",     "AP Calc AB · Unit 5 (part 1) — MVT through 2nd Derivative Test"),
        ("3.", "Assignment 5a in dashboard","8 mixed problems · submit on the Learn portal"),
        ("4.", "Advisor check-in",          "Bring one Candidates Test problem you found tricky"),
    ],
    next_text="Next up:  Module 6 — Graph Sketching & Optimization  (FUN 5.8 – 5.12).",
)


print("AP Calc AB Module 5 slides built.")

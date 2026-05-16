"""AP Calculus AB · Module 9 — Differential Equations: Slope Fields & Separation of Variables.

Custom slides:
- 02_hook                   : cooling coffee cup + dT/dt = -k(T - T_room) callout
- 07_slope_field_visual     : 7x7 slope field for dy/dx = x/y with a threaded solution curve
- 15_exponential_model      : y = y0 e^(kt) headline + small growth-vs-decay curves
"""
import sys
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H, wrap,
    INK, MAROON, MAROON_DARK, MUTED, RED, GRID, CREAM,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Calculus AB", module_num=9,
            output_dir="slides", logo_path=LOGO)


# ─── 01 — title ──────────────────────────────────────────────────────────
deck.title(
    "01_title", "AP Calculus AB",
    "Module 9 — Differential Equations: Slope Fields & Separation of Variables",
    "~9 minutes  ·  Unit 7  ·  FUN 7.1 – 7.4, 7.6 – 7.8",
)


# ─── 02 — hook (custom: cooling coffee cup) ──────────────────────────────
def hook(img, d):
    d.text((110, 80), "The coffee is cooling.",
           fill=MAROON, font=font("serif_bold", 80))
    d.text((110, 178),
           "You can't write T(t) yet — but you can write a sentence about its rate.",
           fill=MUTED, font=font("sans", 34))

    # LEFT — coffee cup illustration
    cx = 460
    top_y = 300
    bot_y = 760
    rx = 200
    ry = 45

    # cup body (truncated cone — slightly narrower at bottom)
    body_top_w = rx
    body_bot_w = rx - 30
    d.polygon([
        (cx - body_top_w, top_y),
        (cx + body_top_w, top_y),
        (cx + body_bot_w, bot_y),
        (cx - body_bot_w, bot_y),
    ], fill=deck.card_bg, outline=MAROON, width=5)

    # bottom ellipse
    d.ellipse([cx - body_bot_w, bot_y - ry // 2,
               cx + body_bot_w, bot_y + ry // 2],
              fill=deck.card_bg, outline=MAROON, width=5)

    # top ellipse (the dark coffee surface)
    d.ellipse([cx - body_top_w, top_y - ry,
               cx + body_top_w, top_y + ry],
              fill=MAROON_DARK, outline=MAROON, width=5)

    # handle (right side)
    handle_x = cx + body_top_w
    handle_y_top = top_y + 90
    handle_y_bot = top_y + 290
    d.arc([handle_x - 30, handle_y_top, handle_x + 120, handle_y_bot],
          start=270, end=90, fill=MAROON, width=10)

    # steam (three wavy lines above the cup)
    for i, dx in enumerate([-60, 0, 60]):
        steam_pts = []
        for k in range(0, 18):
            sx = cx + dx + math.sin(k * 0.6 + i) * 18
            sy = top_y - 40 - k * 12
            steam_pts.append((sx, sy))
        for a, b in zip(steam_pts[:-1], steam_pts[1:]):
            d.line([a, b], fill=MUTED, width=4)

    # temperature label on the cup
    d.text((cx - 60, top_y + 360), "T(t)",
           fill=CREAM, font=font("serif_bold", 64))

    # downward heat-leaving arrows
    for ax in [cx - 280, cx + 280]:
        d.line([(ax, top_y + 40), (ax, top_y + 240)], fill=RED, width=4)
        d.polygon([
            (ax, top_y + 250),
            (ax - 12, top_y + 232),
            (ax + 12, top_y + 232),
        ], fill=RED)
    d.text((cx - 360, top_y + 130), "heat",
           fill=RED, font=font("sans_bold", 28))
    d.text((cx + 300, top_y + 130), "heat",
           fill=RED, font=font("sans_bold", 28))

    # RIGHT — the differential equation card
    card_x = 1000
    card_w = W - 110 - card_x

    d.rounded_rectangle([card_x, 300, card_x + card_w, 540], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, 320), "Newton's Law of Cooling",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((card_x + 30, 410), "dT/dt  =  −k (T − T_room)",
           fill=INK, font=font("mono", 44))
    d.text((card_x + 30, 480), "rate of cooling  ∝  temp. gap",
           fill=MUTED, font=font("sans", 30))

    d.rounded_rectangle([card_x, 570, card_x + card_w, 800], radius=20,
                        outline=MAROON, width=4, fill=deck.accent_light)
    d.text((card_x + 30, 590), "That sentence",
           fill=MAROON_DARK, font=font("serif_bold", 36))
    d.text((card_x + 30, 645), "IS the differential",
           fill=MAROON_DARK, font=font("serif_bold", 36))
    d.text((card_x + 30, 700), "equation.",
           fill=MAROON_DARK, font=font("serif_bold", 36))
    d.text((card_x + 30, 760), "Our job: turn it into T(t).",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # bottom strip
    d.rounded_rectangle([110, 870, W - 110, 1000], radius=20,
                        fill=deck.accent_light)
    centered(d, "Populations, isotopes, accounts — all written this way first.",
             font("sans_bold", 38), 900, MAROON_DARK)


deck.custom("02_hook", hook)


# ─── 03 — overview ───────────────────────────────────────────────────────
deck.overview(
    "03_overview", "Game plan.",
    [
        "What a differential equation is  +  how to verify a solution.",
        "Slope fields — a picture of every solution at once.",
        "Separation of variables  +  initial conditions.",
        "The headline:   dy/dt = ky   →   y = y₀ eᵏᵗ.",
    ],
    footnote="Unit 7 is ~6–12% of the MC.  Almost guaranteed on a FRQ.",
)


# ─── 04 — what is a DE (definition) ──────────────────────────────────────
deck.definition(
    "04_what_is_de",
    "What's a differential equation?",
    "An equation involving a function and its derivative.",
    "The unknown isn't a number — it's a whole function.  "
    "A solution is any function that makes both sides agree.",
)


# ─── 05 — verify a solution (equation) ───────────────────────────────────
deck.equation(
    "05_verify_solution",
    "Is  y = 3 e^(2x)  a solution of  dy/dx = 2y ?",
    [
        ("y      =  3 e^(2x)",          INK,    "candidate"),
        ("dy/dx  =  6 e^(2x)",          INK,    "differentiate"),
        ("2y     =  2 · 3 e^(2x) = 6 e^(2x)", MUTED, "compute RHS"),
        ("LHS  =  RHS   ✓   yes.",     MAROON, "solution verified"),
    ],
)


# ─── 06 — slope field concept (definition) ───────────────────────────────
deck.definition(
    "06_slope_field_concept",
    "What's a slope field?",
    "A grid of tiny tangent segments.",
    "At each point (x, y), draw a short segment with slope = dy/dx evaluated there.  "
    "Solutions are curves tangent to the segments.",
)


# ─── 07 — slope field visual (custom: 7x7 grid for dy/dx = x/y) ──────────
def slope_field(img, d):
    d.text((110, 60), "Slope field for  dy/dx  =  x / y.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 140),
           "Each tiny segment has slope x/y at that grid point.  "
           "Solution curves run tangent to them.",
           fill=MUTED, font=font("sans", 30))

    # LEFT — the slope-field plot
    gx0, gy0 = 130, 210
    gw, gh = 980, 780
    cx_axis = gx0 + gw // 2
    cy_axis = gy0 + gh // 2

    # plot area background
    d.rounded_rectangle([gx0, gy0, gx0 + gw, gy0 + gh], radius=18,
                        outline=MAROON, width=4, fill=deck.card_bg)

    # grid lines (very faint)
    grid_step = gw // 8  # 8 cells across → -3..3 range with margins
    for k in range(-4, 5):
        gxv = cx_axis + k * grid_step
        if gx0 < gxv < gx0 + gw:
            d.line([(gxv, gy0 + 10), (gxv, gy0 + gh - 10)],
                   fill=GRID, width=1)
        gyv = cy_axis + k * grid_step
        if gy0 < gyv < gy0 + gh:
            d.line([(gx0 + 10, gyv), (gx0 + gw - 10, gyv)],
                   fill=GRID, width=1)

    # axes
    d.line([(gx0 + 20, cy_axis), (gx0 + gw - 20, cy_axis)],
           fill=INK, width=3)
    d.line([(cx_axis, gy0 + 20), (cx_axis, gy0 + gh - 20)],
           fill=INK, width=3)
    d.text((gx0 + gw - 50, cy_axis + 12), "x",
           fill=INK, font=font("serif_ital", 28))
    d.text((cx_axis + 14, gy0 + 30), "y",
           fill=INK, font=font("serif_ital", 28))

    # axis tick labels
    for xv in [-3, -2, -1, 1, 2, 3]:
        tx = cx_axis + xv * grid_step
        d.line([(tx, cy_axis - 6), (tx, cy_axis + 6)], fill=INK, width=2)
        lbl = str(xv)
        tw = d.textlength(lbl, font=font("sans", 22))
        d.text((tx - tw / 2, cy_axis + 10), lbl,
               fill=INK, font=font("sans", 22))
    for yv in [-3, -2, -1, 1, 2, 3]:
        ty = cy_axis - yv * grid_step
        d.line([(cx_axis - 6, ty), (cx_axis + 6, ty)], fill=INK, width=2)
        lbl = str(yv)
        tw = d.textlength(lbl, font=font("sans", 22))
        d.text((cx_axis - tw - 14, ty - 12), lbl,
               fill=INK, font=font("sans", 22))

    # the tangent segments — 7x7 lattice over (x,y) ∈ {-3..3} × {-3..3}
    seg_half_px = grid_step * 0.38  # half-length of each tangent dash
    for xv in range(-3, 4):
        for yv in range(-3, 4):
            if yv == 0:
                continue  # dy/dx = x/y undefined on y = 0
            slope = xv / yv
            # convert slope (in graph units: dy per dx) to pixel dy/dx.
            # y-axis is inverted in pixel space, so dy_px = -slope * dx_px.
            # Find unit-vector along the segment in pixel space:
            dx_units = 1.0
            dy_units = slope
            mag = math.sqrt(dx_units * dx_units + dy_units * dy_units)
            ux = dx_units / mag
            uy = dy_units / mag
            cx_pt = cx_axis + xv * grid_step
            cy_pt = cy_axis - yv * grid_step
            half = seg_half_px
            x1 = cx_pt - ux * half
            y1 = cy_pt + uy * half  # +uy because pixel y is inverted
            x2 = cx_pt + ux * half
            y2 = cy_pt - uy * half
            d.line([(x1, y1), (x2, y2)], fill=MAROON_DARK, width=4)

    # threaded solution curve: y² - x² = 1 (upper branch through (0, 1))
    # → y = sqrt(1 + x²)
    curve_pts = []
    x = -3.0
    while x <= 3.0:
        yv = math.sqrt(1 + x * x)
        if abs(yv) <= 3.2:
            px = cx_axis + x * grid_step
            py = cy_axis - yv * grid_step
            if gy0 + 10 < py < gy0 + gh - 10:
                curve_pts.append((px, py))
        x += 0.05
    for a_pt, b_pt in zip(curve_pts[:-1], curve_pts[1:]):
        d.line([a_pt, b_pt], fill=deck.accent, width=6)

    # label that curve
    d.text((cx_axis + 1.6 * grid_step, cy_axis - 2.6 * grid_step - 30),
           "y² − x² = 1",
           fill=deck.accent, font=font("serif_bold", 30))

    # RIGHT — explanation cards
    card_x = 1140
    card_w = W - 110 - card_x

    d.rounded_rectangle([card_x, 210, card_x + card_w, 430], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, 230), "How to read it",
           fill=MAROON, font=font("serif_bold", 36))
    d.text((card_x + 30, 295), "At (2, 1):  slope = 2 / 1 = 2",
           fill=INK, font=font("mono", 26))
    d.text((card_x + 30, 335), "At (1, 2):  slope = 1 / 2 = 0.5",
           fill=INK, font=font("mono", 26))
    d.text((card_x + 30, 375), "At (−2, 1): slope = −2",
           fill=INK, font=font("mono", 26))

    d.rounded_rectangle([card_x, 460, card_x + card_w, 700], radius=20,
                        outline=MAROON, width=4, fill=deck.card_bg)
    d.text((card_x + 30, 480), "Solution curves",
           fill=MAROON, font=font("serif_bold", 36))
    d.text((card_x + 30, 545), "y² = x² + C",
           fill=INK, font=font("mono", 36))
    d.text((card_x + 30, 600), "→  hyperbolas",
           fill=MUTED, font=font("sans", 28))
    d.text((card_x + 30, 645), "(derivation:  next slide)",
           fill=MUTED, font=font("sans_ital" if "sans_ital" in
                                 dir() else "sans", 26))

    d.rounded_rectangle([card_x, 730, card_x + card_w, 960], radius=20,
                        fill=deck.accent_light)
    d.text((card_x + 30, 750), "Note",
           fill=MAROON_DARK, font=font("serif_bold", 32))
    d.text((card_x + 30, 810), "No segments on y = 0",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((card_x + 30, 855), "(slope x / y is undefined",
           fill=MAROON_DARK, font=font("sans", 24))
    d.text((card_x + 30, 890), "when y = 0).",
           fill=MAROON_DARK, font=font("sans", 24))


deck.custom("07_slope_field_visual", slope_field)


# ─── 08 — reading slope fields (compare: wrong vs right) ─────────────────
deck.compare(
    "08_reading_slope_field",
    "AP trap — how to read a slope field.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "Treats arrows as the graph of  y.",
            "Traces ALONG the segments.",
            "Mistakes slopes for function values.",
            "Picks the wrong matching curve.",
        ],
        "footnote": "Slope field ≠ graph of  y.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "Arrows show  dy/dx  at each point.",
            "Solution is TANGENT to the segments.",
            "It passes through each one in its direction.",
            "Match by following segment directions.",
        ],
        "footnote": "Tangent to the arrows, not along the arrows.",
    },
)


# ─── 09 — separation of variables (definition) ───────────────────────────
deck.definition(
    "09_separation_idea",
    "Separation of variables.",
    "If  dy/dx = g(x) · h(y),  then  dy / h(y)  =  g(x) dx.",
    "Get all the  y  stuff on one side, all the  x  stuff on the other, "
    "then integrate both sides.",
)


# ─── 10 — separation example (equation) ──────────────────────────────────
deck.equation(
    "10_separation_example",
    "General solution of  dy/dx = x / y.",
    [
        ("dy/dx  =  x / y",                 INK,    "given"),
        ("y dy  =  x dx",                   INK,    "separate"),
        ("∫ y dy  =  ∫ x dx",               MUTED,  "integrate both sides"),
        ("½ y²  =  ½ x²  +  C",             INK,    "antiderivatives"),
        ("y²  =  x²  +  C",                 MAROON, "general solution — family of hyperbolas"),
    ],
)


# ─── 11 — initial condition warning (compare: the big trap) ──────────────
deck.compare(
    "11_initial_condition_warning",
    "The biggest trap on the AP free response.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "Plugs IC in BEFORE integrating.",
            "Or:  forgets the  + C  entirely.",
            "Constant has nowhere to absorb IC.",
            "Particular solution is wrong.",
        ],
        "footnote": "Lose the + C point  →  lose the IC point.",
    },
    right={
        "label": "✓ RIGHT",
        "color": MAROON,
        "lines": [
            "Separate.   Integrate.   Write  + C.",
            "Exponentiate  →  constant  A  absorbs.",
            "THEN plug in the initial condition.",
            "Solve for  A.  Write the particular y.",
        ],
        "footnote": "Plus C first.  Plug in second.  Always.",
    },
)


# ─── 12 — particular solution (equation) ─────────────────────────────────
deck.equation(
    "12_particular_solution",
    "Particular solution:  dy/dx = 2xy,   y(0) = 5.",
    [
        ("dy / y  =  2x dx",              INK,    "separate"),
        ("ln |y|  =  x²  +  C",           INK,    "integrate"),
        ("y  =  A · e^(x²)",              INK,    "exponentiate  (A absorbs C)"),
        ("5  =  A · e^0  =  A",           MUTED,  "plug in  y(0) = 5"),
        ("y  =  5 e^(x²)",                MAROON, "particular solution"),
    ],
)


# ─── 13 — pause-and-try ──────────────────────────────────────────────────
deck.pause(
    "13_pause1", "PAUSE  &  TRY",
    "Solve using separation, with the initial condition  y(0) = 4:",
    "dy/dx  =  3y",
    hint="Separate, integrate, write + C, exponentiate, then plug in.  "
         "Pause.  Solve.  Press play when ready.",
)
deck.duplicate("13_pause1", "14_pause1_silence")


# ─── 15 — exponential model headline (custom) ────────────────────────────
def exponential_model(img, d):
    d.text((110, 70), "The headline of the whole unit.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 148),
           "Rate proportional to amount  →  exponential.",
           fill=MUTED, font=font("sans", 34))

    # CENTER — the big equation card
    d.rounded_rectangle([110, 230, W - 110, 470], radius=24,
                        outline=MAROON, width=5, fill=deck.card_bg)
    centered(d, "dy/dt  =  k · y    ⟹    y  =  y₀ · e^(kt)",
             font("mono", 70), 290, INK)
    centered(d, "y₀ = starting amount.   k = proportionality constant.",
             font("sans", 32), 410, MUTED)

    # LEFT — growth curve panel
    panels = [
        (110, "k > 0   growth", deck.accent, 0.35),
        (980, "k < 0   decay",  MAROON,      -0.35),
    ]
    for x0, label, col, k_val in panels:
        panel_w = 820
        panel_h = 420
        py = 510
        d.rounded_rectangle([x0, py, x0 + panel_w, py + panel_h],
                            radius=20, outline=col, width=5, fill=deck.card_bg)
        d.text((x0 + 30, py + 25), label,
               fill=col, font=font("serif_bold", 44))

        # mini axes inside the panel
        ax_x0 = x0 + 80
        ax_x1 = x0 + panel_w - 40
        ax_y0 = py + 110
        ax_y1 = py + panel_h - 60
        # x axis
        d.line([(ax_x0, ax_y1), (ax_x1, ax_y1)], fill=INK, width=3)
        # y axis
        d.line([(ax_x0, ax_y0), (ax_x0, ax_y1)], fill=INK, width=3)
        d.text((ax_x1 + 10, ax_y1 - 14), "t",
               fill=INK, font=font("serif_ital", 24))
        d.text((ax_x0 - 24, ax_y0 - 18), "y",
               fill=INK, font=font("serif_ital", 24))

        # curve y = e^(kt), scaled
        t_max = 6.0
        if k_val > 0:
            y_at_max = math.exp(k_val * t_max)
        else:
            y_at_max = 1.0  # at t=0
        # we always want to fit roughly y range [0, 3] into the box
        y_view_max = 3.5
        plot_w = ax_x1 - ax_x0
        plot_h = ax_y1 - ax_y0
        pts = []
        t = 0.0
        while t <= t_max + 0.01:
            yv = math.exp(k_val * t)
            px = ax_x0 + (t / t_max) * plot_w
            py_px = ax_y1 - (yv / y_view_max) * plot_h
            py_px = max(ax_y0 + 4, min(ax_y1 - 2, py_px))
            pts.append((px, py_px))
            t += 0.05
        for a, b in zip(pts[:-1], pts[1:]):
            d.line([a, b], fill=col, width=6)

        # mark y0 = 1 on the y axis
        y0_px = ax_y1 - (1.0 / y_view_max) * plot_h
        d.line([(ax_x0 - 6, y0_px), (ax_x0 + 6, y0_px)], fill=INK, width=2)
        d.text((ax_x0 - 50, y0_px - 14), "y₀",
               fill=INK, font=font("sans_bold", 24))

        # caption underneath
        if k_val > 0:
            cap = "Populations · interest · cell division"
        else:
            cap = "Isotopes · cooling gap · drug clearance"
        d.text((x0 + 30, py + panel_h - 42), cap,
               fill=MUTED, font=font("sans_bold", 28))


deck.custom("15_exponential_model", exponential_model)


# ─── 16 — modeling example (equation) ────────────────────────────────────
deck.equation(
    "16_modeling_example",
    "Bacteria — double every 4 hours.   Start at 100.",
    [
        ("dy/dt  =  k · y,   y(0) = 100",       INK,    "rate ∝ population"),
        ("y(t)  =  100 · e^(kt)",                INK,    "exponential form"),
        ("200  =  100 · e^(4k)   →   e^(4k) = 2", MUTED, "doubling condition"),
        ("k  =  ln(2) / 4",                      INK,    "solve for k"),
        ("y(t)  =  100 · e^((ln 2 / 4) t)",      MAROON, "final model"),
    ],
)


# ─── 17 — recap ──────────────────────────────────────────────────────────
deck.recap(
    "17_recap", "Recap.",
    [
        "DE = equation with a function + its derivative.  Verify by substituting.",
        "Slope field = grid of tangent segments.  Solutions are TANGENT to them.",
        "Separate when  dy/dx  =  g(x) · h(y).   Integrate both sides.",
        "Write  + C  BEFORE plugging in the initial condition.  Non-negotiable.",
        "Whenever  dy/dt = ky,  the solution is  y = y₀ e^(kt).",
    ],
    assignment=[
        "8 problems in the dashboard:  5 separation  +  3 slope-field matching.",
        "Plus one full free-response from the 2018 AP Calculus AB exam (Q4).",
    ],
)


# ─── 18 — path ───────────────────────────────────────────────────────────
deck.path(
    "18_path",
    items=[
        ("✓",  "Watch this lesson",        "(done!)"),
        ("1.", "OpenStax Calculus Vol 2",  "Read sections 4.1 – 4.3 (intro + separation)"),
        ("2.", "Khan Academy practice",    "AP Calc AB · Unit 7 — Differential Equations"),
        ("3.", "Assignment in dashboard",  "8 mixed:  5 separation  +  3 slope-field matching"),
        ("4.", "Advisor check-in",         "Bring one FRQ if particular solutions still feel slippery"),
    ],
    next_text="Next up:  Module 10 — Average Value & Area Between Curves.",
)


print("AP Calc AB Module 9 slides built.")

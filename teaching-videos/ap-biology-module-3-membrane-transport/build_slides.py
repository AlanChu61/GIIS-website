"""AP Biology · Module 3 — Membrane Transport.

Teal (science) theme auto-resolved by slide_kit from the "AP Biology" prefix.
16 slides total. Heavy on customs because membrane transport is visual —
bilayers, pumps, tonicity diagrams, vesicles. Pause slide is duplicated
(10 -> 11) so the same image plays during both the question and the
answer narration.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, CREAM, GOLD,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Biology", module_num=3, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# ─── tiny helpers ─────────────────────────────────────────────────────

def draw_bilayer(d, x0, y0, x1, y1, head_r=18, n_pairs=None):
    """Draw a phospholipid bilayer between (x0,y0) (top-left) and (x1,y1) (bottom-right).
    Heads at top + bottom, tails meet in the middle."""
    width = x1 - x0
    height = y1 - y0
    spacing = head_r * 2 + 6
    if n_pairs is None:
        n_pairs = max(8, width // spacing)
    tail_len = (height - 4 * head_r) / 2
    cx0 = x0 + (width - (n_pairs - 1) * spacing) // 2
    for i in range(n_pairs):
        cx = cx0 + i * spacing
        # Top head
        d.ellipse([cx - head_r, y0, cx + head_r, y0 + head_r * 2],
                  fill=ACCENT, outline=MAROON_DARK, width=2)
        # Top tails
        d.line([(cx - 5, y0 + head_r * 2),
                (cx - 5, y0 + head_r * 2 + tail_len)],
               fill=MAROON_DARK, width=3)
        d.line([(cx + 5, y0 + head_r * 2),
                (cx + 5, y0 + head_r * 2 + tail_len)],
               fill=MAROON_DARK, width=3)
        # Bottom head
        d.ellipse([cx - head_r, y1 - head_r * 2, cx + head_r, y1],
                  fill=ACCENT, outline=MAROON_DARK, width=2)
        # Bottom tails
        d.line([(cx - 5, y1 - head_r * 2),
                (cx - 5, y1 - head_r * 2 - tail_len)],
               fill=MAROON_DARK, width=3)
        d.line([(cx + 5, y1 - head_r * 2),
                (cx + 5, y1 - head_r * 2 - tail_len)],
               fill=MAROON_DARK, width=3)


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 3 — Membrane Transport",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook: Na/K pump firing 10M times / sec
def hook(img, d):
    d.text((110, 70), "Right now, in every nerve cell you have…",
           fill=MAROON, font=font("serif_bold", 56))

    # Big stat card
    d.rounded_rectangle([110, 200, W - 110, 520], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    centered(d, "~10,000,000",
             font("serif_bold", 180), 230, MAROON)
    centered(d, "sodium + potassium ions pumped",
             font("sans_bold", 42), 420, INK)
    centered(d, "every  second  ·  by one protein  ·  forever",
             font("sans", 34), 470, MUTED)

    # Two side facts
    fl_x, fl_y = 110, 580
    fl_w, fl_h = 870, 310
    d.rounded_rectangle([fl_x, fl_y, fl_x + fl_w, fl_y + fl_h], radius=22,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((fl_x + 30, fl_y + 28), "It costs you",
           fill=MAROON_DARK, font=font("sans_bold", 36))
    centered_text = "~25%"
    f = font("serif_bold", 120)
    tw = d.textlength(centered_text, font=f)
    d.text((fl_x + fl_w // 2 - tw / 2, fl_y + 80), centered_text,
           fill=MAROON, font=f)
    d.text((fl_x + 30, fl_y + 220),
           "of all the calories you eat,",
           fill=INK, font=font("sans", 30))
    d.text((fl_x + 30, fl_y + 260),
           "just sitting still.",
           fill=INK, font=font("sans_bold", 30))

    fr_x = fl_x + fl_w + 30
    fr_w = W - 110 - fr_x
    d.rounded_rectangle([fr_x, fl_y, fr_x + fr_w, fl_y + fl_h], radius=22,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((fr_x + 30, fl_y + 28), "If it stops:",
           fill=MAROON_DARK, font=font("sans_bold", 36))
    d.text((fr_x + 30, fl_y + 100),
           "·  gradients collapse in seconds",
           fill=INK, font=font("sans", 28))
    d.text((fr_x + 30, fl_y + 150),
           "·  neurons stop firing",
           fill=INK, font=font("sans", 28))
    d.text((fr_x + 30, fl_y + 200),
           "·  you lose consciousness",
           fill=INK, font=font("sans", 28))
    d.text((fr_x + 30, fl_y + 260),
           "in a few minutes.",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    # Bottom punchline
    d.rounded_rectangle([110, 920, W - 110, 1010], radius=18,
                        fill=ACCENT, outline=MAROON, width=4)
    centered(d, "That pump is what today is about.",
             font("serif_bold", 38), 940, CREAM)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "The membrane itself — fluid mosaic, and what can cross it.",
    "Passive transport — diffusion, osmosis, facilitated (free, no ATP).",
    "Active transport — pumps, cotransport, vesicles (costs ATP).",
], footnote="By the end: you can predict water + ion movement in any scenario.")


# 04 — fluid mosaic model
def fluid_mosaic(img, d):
    d.text((110, 70), "Fluid mosaic model.  (Singer & Nicolson, 1972)",
           fill=MAROON, font=font("serif_bold", 50))

    # Bilayer in the middle
    bx0, by0 = 200, 360
    bx1, by1 = W - 200, 720
    draw_bilayer(d, bx0, by0, bx1, by1, head_r=20, n_pairs=20)

    # "OUTSIDE" and "INSIDE" labels (left side, well clear of the diagram labels)
    d.text((110, 270), "EXTRACELLULAR", fill=MAROON_DARK,
           font=font("sans_bold", 30))
    d.text((110, 305), "(outside)", fill=MUTED,
           font=font("serif_ital", 24))
    d.text((110, 660), "CYTOSOL", fill=MAROON_DARK,
           font=font("sans_bold", 30))
    d.text((110, 695), "(inside)", fill=MUTED,
           font=font("serif_ital", 24))

    # Integral protein (channel) — spans bilayer
    ip_x = bx0 + 120
    d.rectangle([ip_x, by0 - 30, ip_x + 80, by1 + 30],
                fill=MAROON, outline=MAROON_DARK, width=3)
    # tunnel through it
    d.rectangle([ip_x + 30, by0 - 30, ip_x + 50, by1 + 30],
                fill=ACCENT_LT)
    d.text((ip_x - 30, by1 + 60), "channel", fill=MAROON_DARK,
           font=font("sans_bold", 24))
    d.text((ip_x - 40, by1 + 90), "(integral)", fill=MUTED,
           font=font("serif_ital", 22))

    # Carrier protein
    cp_x = bx0 + 360
    d.rounded_rectangle([cp_x, by0 - 30, cp_x + 110, by1 + 30],
                        radius=20, fill=MAROON, outline=MAROON_DARK,
                        width=3)
    d.text((cp_x - 10, by1 + 60), "carrier", fill=MAROON_DARK,
           font=font("sans_bold", 24))
    d.text((cp_x - 20, by1 + 90), "(integral)", fill=MUTED,
           font=font("serif_ital", 22))

    # Peripheral protein on inside face
    pp_x = bx0 + 580
    d.ellipse([pp_x, by1 - 10, pp_x + 90, by1 + 50],
              fill=RED, outline=MAROON_DARK, width=3)
    d.text((pp_x - 10, by1 + 60), "peripheral", fill=MAROON_DARK,
           font=font("sans_bold", 24))

    # Glycoprotein on top
    gp_x = bx0 + 760
    d.rectangle([gp_x, by0 - 30, gp_x + 60, by0 + 60],
                fill=MAROON, outline=MAROON_DARK, width=3)
    # Carbohydrate chain — zigzag of small circles
    for k, dy in enumerate([-30, -55, -80, -105]):
        d.ellipse([gp_x + 20 + (k % 2) * 30, by0 - 30 + dy - 12,
                   gp_x + 40 + (k % 2) * 30, by0 - 30 + dy + 8],
                  fill=ACCENT, outline=MAROON_DARK, width=2)
    d.text((gp_x - 30, by0 - 170), "glycoprotein",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    d.text((gp_x - 30, by0 - 145), "(cell ID)",
           fill=MUTED, font=font("serif_ital", 22))

    # Cholesterol — small marker between tails
    ch_x = bx0 + 940
    d.rectangle([ch_x, by0 + 50, ch_x + 24, by1 - 50],
                fill=GOLD, outline=MAROON_DARK, width=2)
    d.text((ch_x - 30, by1 + 60), "cholesterol",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    d.text((ch_x - 30, by1 + 90), "(fluidity)",
           fill=MUTED, font=font("serif_ital", 22))

    # Bottom legend strip
    d.rounded_rectangle([110, 880, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Bilayer  +  proteins  +  carbs  +  cholesterol  —  fluid, dynamic, selectively permeable.",
             font("sans_bold", 30), 915, MAROON_DARK)
deck.custom("04_fluid_mosaic", fluid_mosaic)


# 05 — permeability: what crosses freely vs needs help
def permeability(img, d):
    d.text((110, 70), "Selective permeability.  What gets through?",
           fill=MAROON, font=font("serif_bold", 54))

    # Three column cards
    cols = [
        ("✓  FREE",
         ACCENT,
         "small  ·  nonpolar",
         ["O₂  (oxygen)",
          "CO₂  (carbon dioxide)",
          "N₂",
          "steroid hormones",
          "small lipids"],
         "Slide right through the\nhydrophobic core."),
        ("~  SLOW",
         GOLD,  # gold for in-between
         "small  ·  polar  ·  uncharged",
         ["H₂O  (water)",
          "urea",
          "glycerol",
          "small alcohols"],
         "Cross slowly.  Cells speed\nthis up with aquaporins."),
        ("✗  BLOCKED",
         MAROON,
         "large  OR  charged",
         ["glucose, sucrose",
          "amino acids",
          "Na⁺, K⁺, Ca²⁺, Cl⁻",
          "ATP, nucleotides",
          "proteins"],
         "Need a transport protein\n(channel, carrier, pump)."),
    ]

    col_w = 540
    col_h = 700
    gap = 30
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 200
    for i, (label, color, sub, items, footnote) in enumerate(cols):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=22,
                            outline=color, width=6, fill=CARD)
        # Header bar
        d.rectangle([x, y0, x + col_w, y0 + 80], fill=color)
        centered_x = x + col_w // 2
        f_h = font("serif_bold", 46)
        tw = d.textlength(label, font=f_h)
        d.text((centered_x - tw / 2, y0 + 12), label,
               fill=CREAM, font=f_h)
        # Sub
        f_sub = font("sans_bold", 26)
        tw_sub = d.textlength(sub, font=f_sub)
        d.text((centered_x - tw_sub / 2, y0 + 100),
               sub, fill=MUTED, font=f_sub)
        # Items
        ly = y0 + 170
        for it in items:
            d.text((x + 40, ly), "·  " + it, fill=INK,
                   font=font("sans", 28))
            ly += 56
        # Footnote
        for k, line in enumerate(footnote.split("\n")):
            d.text((x + 40, y0 + col_h - 95 + k * 36), line,
                   fill=color, font=font("sans_bold", 24))

    # Bottom rule
    d.rounded_rectangle([110, 940, W - 110, 1030], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "The hydrophobic core is the gatekeeper.",
             font("serif_bold", 34), 962, MAROON_DARK)
deck.custom("05_permeability", permeability)


# 06 — passive diffusion: simple + facilitated (channels vs carriers)
def passive_diffusion(img, d):
    d.text((110, 70), "Passive transport.  Down the gradient.  No ATP.",
           fill=MAROON, font=font("serif_bold", 50))

    # Three vertical mini-panels
    panel_w = 540
    panel_h = 640
    gap = 30
    start_x = (W - (panel_w * 3 + gap * 2)) // 2
    py = 200

    panels = [
        ("SIMPLE DIFFUSION", "O₂  ·  CO₂  ·  steroids",
         "molecules cross the bilayer\ndirectly  (no protein)"),
        ("FACILITATED — CHANNEL", "Na⁺, K⁺, aquaporins",
         "hydrophilic tunnel\nopens through bilayer"),
        ("FACILITATED — CARRIER", "glucose (GLUT-1)",
         "binds, changes shape,\nreleases on other side"),
    ]

    for i, (name, ex, body) in enumerate(panels):
        x = start_x + i * (panel_w + gap)
        d.rounded_rectangle([x, py, x + panel_w, py + panel_h],
                            radius=22, outline=ACCENT, width=5, fill=CARD)
        d.text((x + 24, py + 18), name, fill=ACCENT,
               font=font("sans_bold", 32))
        d.text((x + 24, py + 70), ex, fill=MAROON_DARK,
               font=font("serif_ital", 28))

        # Diagram: a tiny bilayer with the relevant transport drawing
        bx0 = x + 60
        bx1 = x + panel_w - 60
        by0 = py + 170
        by1 = py + 380
        draw_bilayer(d, bx0, by0, bx1, by1, head_r=14, n_pairs=10)

        if i == 0:
            # Simple diffusion: small dots crossing bilayer
            for j, yy in enumerate([by0 - 30, by0 + 50, by0 + 130, by1 + 30]):
                xx = bx0 + 80 + j * 90
                d.ellipse([xx - 10, yy - 10, xx + 10, yy + 10],
                          fill=RED, outline=MAROON_DARK, width=2)
            # downward arrow
            ax = bx0 + (bx1 - bx0) // 2
            d.line([(ax, by0 - 60), (ax, by1 + 60)],
                   fill=MAROON, width=5)
            d.polygon([(ax - 12, by1 + 50), (ax + 12, by1 + 50),
                       (ax, by1 + 70)], fill=MAROON)
        elif i == 1:
            # Channel: a tunnel
            tx = bx0 + (bx1 - bx0) // 2 - 30
            d.rectangle([tx, by0 - 30, tx + 60, by1 + 30],
                        fill=MAROON, outline=MAROON_DARK, width=3)
            d.rectangle([tx + 22, by0 - 30, tx + 38, by1 + 30],
                        fill=ACCENT_LT)
            # ions flowing through
            for yy in [by0 - 10, by0 + 70, by0 + 150, by1 + 10]:
                d.ellipse([tx + 22, yy - 8, tx + 38, yy + 8],
                          fill=ACCENT, outline=MAROON_DARK, width=2)
        else:
            # Carrier: rounded protein with a "bound" molecule
            cx = bx0 + (bx1 - bx0) // 2 - 50
            d.rounded_rectangle([cx, by0 - 20, cx + 100, by1 + 20],
                                radius=24, fill=MAROON,
                                outline=MAROON_DARK, width=3)
            # bound glucose
            d.ellipse([cx + 30, by0 + 80, cx + 70, by0 + 120],
                      fill=ACCENT, outline=MAROON_DARK, width=3)
            # arrow showing shape change
            d.text((bx0 + 30, by1 + 40), "→ shape change →",
                   fill=MAROON_DARK, font=font("sans_bold", 22))

        # Body text
        for k, line in enumerate(body.split("\n")):
            d.text((x + 24, py + 470 + k * 36), line,
                   fill=INK, font=font("sans", 26))

        # No-ATP stamp
        d.rounded_rectangle([x + 24, py + 580, x + 280, py + 620],
                            radius=12, fill=ACCENT)
        d.text((x + 40, py + 588), "NO ATP NEEDED",
               fill=CREAM, font=font("sans_bold", 22))

    # Bottom rule
    d.rounded_rectangle([110, 870, W - 110, 990], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Facilitated diffusion uses a protein  —  but it is still passive.",
             font("serif_bold", 34), 900, MAROON_DARK)
deck.custom("06_passive_diffusion", passive_diffusion)


# 07 — osmosis & tonicity (3 columns: hypo / iso / hyper)
def osmosis_tonicity(img, d):
    d.text((110, 60), "Osmosis & tonicity.  (water always moves toward MORE solute.)",
           fill=MAROON, font=font("serif_bold", 44))

    cols = [
        ("HYPOTONIC", ACCENT,
         "outside has LESS solute\n→  water flows IN",
         "animal: SWELLS → LYSES",
         "plant: TURGID  (healthy)",
         "swell"),
        ("ISOTONIC", GOLD,
         "equal solute both sides\n→  no net water movement",
         "animal: normal",
         "plant: flaccid  (limp)",
         "same"),
        ("HYPERTONIC", MAROON,
         "outside has MORE solute\n→  water flows OUT",
         "animal: SHRIVELS  (crenation)",
         "plant: PLASMOLYZED",
         "shrink"),
    ]

    col_w = 540
    col_h = 720
    gap = 30
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 170

    for i, (label, color, desc, animal, plant, state) in enumerate(cols):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=22,
                            outline=color, width=6, fill=CARD)
        d.rectangle([x, y0, x + col_w, y0 + 70], fill=color)
        f_h = font("serif_bold", 42)
        tw = d.textlength(label, font=f_h)
        d.text((x + col_w // 2 - tw / 2, y0 + 12), label,
               fill=CREAM, font=f_h)
        for k, ln in enumerate(desc.split("\n")):
            d.text((x + 30, y0 + 100 + k * 38), ln, fill=INK,
                   font=font("sans_bold", 26))

        # Cell diagram (animal + plant side-by-side)
        diag_y = y0 + 230
        # Animal cell (circle) — fill depends on state
        ax = x + 140
        ay = diag_y + 100
        if state == "swell":
            r = 90
        elif state == "shrink":
            r = 50
        else:
            r = 70
        d.ellipse([ax - r, ay - r, ax + r, ay + r],
                  fill=RED if state == "swell" else ACCENT_LT,
                  outline=MAROON_DARK, width=4)
        # burst marks for swell
        if state == "swell":
            for ang_deg in (30, 110, 210, 320):
                import math as _m
                a = _m.radians(ang_deg)
                x1 = ax + (r + 8) * _m.cos(a)
                y1 = ay + (r + 8) * _m.sin(a)
                x2 = ax + (r + 35) * _m.cos(a)
                y2 = ay + (r + 35) * _m.sin(a)
                d.line([(x1, y1), (x2, y2)], fill=RED, width=4)
        d.text((ax - 35, ay + 100), "animal", fill=MUTED,
               font=font("sans_bold", 22))

        # Plant cell (square wall + inner membrane)
        px = x + 380
        py_ = diag_y + 20
        side = 160
        # Cell wall — always full square
        d.rectangle([px, py_, px + side, py_ + side],
                    outline=MAROON_DARK, width=5, fill=CARD)
        # Plasma membrane inside — sizing depends on state
        if state == "swell":
            inset = 8  # turgid, pressed against wall
            fill = ACCENT
        elif state == "shrink":
            inset = 40  # plasmolyzed, pulled away from wall
            fill = ACCENT_LT
        else:
            inset = 22  # flaccid
            fill = ACCENT_LT
        d.rounded_rectangle([px + inset, py_ + inset,
                             px + side - inset, py_ + side - inset],
                            radius=18, fill=fill,
                            outline=MAROON_DARK, width=3)
        d.text((px + 30, py_ + side + 8), "plant", fill=MUTED,
               font=font("sans_bold", 22))

        # Outcomes (text below diagram)
        d.text((x + 30, y0 + 540), animal, fill=MAROON_DARK,
               font=font("sans_bold", 24))
        d.text((x + 30, y0 + 580), plant, fill=MAROON_DARK,
               font=font("sans_bold", 24))

        # Arrow row showing water direction
        arrow_y = y0 + 640
        if state == "swell":
            # arrow pointing IN
            d.text((x + 30, arrow_y), "H₂O  →  IN",
                   fill=ACCENT, font=font("sans_bold", 32))
        elif state == "shrink":
            d.text((x + 30, arrow_y), "H₂O  →  OUT",
                   fill=MAROON, font=font("sans_bold", 32))
        else:
            d.text((x + 30, arrow_y), "H₂O  ⇌  no net",
                   fill=MUTED, font=font("sans_bold", 32))

    # Bottom trap warning
    d.rounded_rectangle([110, 920, W - 110, 1020], radius=18,
                        fill=MAROON, outline=MAROON_DARK, width=4)
    centered(d, "HYPER-tonic  =  HIGH solute, LOW water.  Cell wall is why plants don't lyse.",
             font("serif_bold", 32), 950, CREAM)
deck.custom("07_osmosis_tonicity", osmosis_tonicity)


# 08 — primary active transport: Na/K ATPase
def active_primary(img, d):
    d.text((110, 60), "Primary active transport — the Na⁺/K⁺ pump.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 130), "Uses ATP directly.  Moves ions AGAINST their gradient.",
           fill=MUTED, font=font("sans", 28))

    # Center: a bilayer with the pump (compact, leaves room top + bottom)
    bx0, by0 = 460, 280
    bx1, by1 = W - 460, 560
    draw_bilayer(d, bx0, by0, bx1, by1, head_r=16, n_pairs=12)

    # OUTSIDE / INSIDE labels (far left/right, well clear of diagram)
    d.text((140, 370), "OUTSIDE", fill=MAROON_DARK,
           font=font("sans_bold", 38))
    d.text((140, 430), "(extracellular)", fill=MUTED,
           font=font("serif_ital", 24))
    d.text((W - 280, 370), "INSIDE", fill=MAROON_DARK,
           font=font("sans_bold", 38))
    d.text((W - 280, 430), "(cytosol)", fill=MUTED,
           font=font("serif_ital", 24))

    # Pump protein
    pxc = (bx0 + bx1) // 2
    pw = 220
    d.rounded_rectangle([pxc - pw // 2, by0 - 40, pxc + pw // 2, by1 + 40],
                        radius=28, fill=MAROON,
                        outline=MAROON_DARK, width=4)
    d.text((pxc - 80, by0 + 12), "Na/K",
           fill=CREAM, font=font("sans_bold", 30))
    d.text((pxc - 80, by0 + 50), "ATPase",
           fill=CREAM, font=font("sans_bold", 30))

    # 3 Na+ above pump (going OUT — up arrow on LEFT inside pump)
    for k in range(3):
        ix = pxc - 60 + k * 40
        d.ellipse([ix - 16, by0 - 105, ix + 16, by0 - 73],
                  fill=ACCENT, outline=MAROON_DARK, width=3)
        d.text((ix - 13, by0 - 95), "Na⁺", fill=CREAM,
               font=font("sans_bold", 16))
    # Up arrow on left side of pump interior
    arr_x = pxc - 60
    d.line([(arr_x, by1 + 30), (arr_x, by0 - 60)],
           fill=ACCENT, width=10)
    d.polygon([(arr_x - 14, by0 - 50), (arr_x + 14, by0 - 50),
               (arr_x, by0 - 80)], fill=ACCENT)
    # 3 Na+ OUT label — top-left, clearly above the bilayer
    d.text((bx0 - 250, by0 - 110), "3 Na⁺  OUT",
           fill=ACCENT, font=font("sans_bold", 36))

    # 2 K+ below pump (going IN — down arrow on RIGHT inside pump)
    for k in range(2):
        ix = pxc + 20 + k * 40
        d.ellipse([ix - 16, by1 + 73, ix + 16, by1 + 105],
                  fill=RED, outline=MAROON_DARK, width=3)
        d.text((ix - 10, by1 + 82), "K⁺", fill=CREAM,
               font=font("sans_bold", 16))
    arr_x2 = pxc + 40
    d.line([(arr_x2, by0 - 30), (arr_x2, by1 + 60)],
           fill=RED, width=10)
    d.polygon([(arr_x2 - 14, by1 + 50), (arr_x2 + 14, by1 + 50),
               (arr_x2, by1 + 80)], fill=RED)
    # 2 K+ IN label — bottom-right, well below bilayer + ions
    d.text((bx1 + 10, by1 + 90), "2 K⁺  IN",
           fill=RED, font=font("sans_bold", 36))

    # ATP marker — placed clearly inside the pump, not overlapping the label
    d.rounded_rectangle([pxc + 80, by0 + 100, pxc + 80 + 100, by0 + 160],
                        radius=14, fill=GOLD,
                        outline=MAROON_DARK, width=3)
    d.text((pxc + 100, by0 + 116), "ATP",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # Bottom result strip
    d.rounded_rectangle([110, 740, W - 110, 880], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((140, 760), "Result:  electrochemical gradient.",
           fill=MAROON_DARK, font=font("serif_bold", 36))
    d.text((140, 815),
           "More Na⁺ outside  ·  more K⁺ inside  ·  inside slightly NEGATIVE",
           fill=INK, font=font("sans", 28))
    d.text((140, 848),
           "→  powers nerve impulses, muscle contraction, and cotransport.",
           fill=ACCENT, font=font("sans_bold", 26))

    # Footer ratio reminder
    d.rounded_rectangle([110, 905, W - 110, 1000], radius=18,
                        fill=MAROON, outline=MAROON_DARK, width=4)
    centered(d, "3 Na⁺ OUT   ·   2 K⁺ IN   ·   per 1 ATP",
             font("serif_bold", 44), 930, CREAM)
deck.custom("08_active_transport_primary", active_primary)


# 09 — secondary active transport: Na/glucose cotransport
def active_secondary(img, d):
    d.text((110, 70), "Secondary active transport — cotransport.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 150),
           "Use the gradient primary transport already built.  No fresh ATP at this step.",
           fill=MUTED, font=font("sans", 28))

    # Bilayer
    bx0, by0 = 200, 320
    bx1, by1 = W - 200, 680
    draw_bilayer(d, bx0, by0, bx1, by1, head_r=18, n_pairs=18)

    d.text((110, 230), "GUT LUMEN  (outside)", fill=MAROON_DARK,
           font=font("sans_bold", 30))
    d.text((110, 740), "INTESTINAL CELL  (inside)", fill=MAROON_DARK,
           font=font("sans_bold", 30))

    # Left: Na/K pump (creates the gradient)
    px1 = bx0 + 200
    d.rounded_rectangle([px1, by0 - 30, px1 + 110, by1 + 30],
                        radius=22, fill=(120, 120, 130),
                        outline=MAROON_DARK, width=3)
    d.text((px1 - 5, (by0 + by1) // 2 - 20), "Na/K",
           fill=CREAM, font=font("sans_bold", 24))
    d.text((px1 - 5, (by0 + by1) // 2 + 10), "pump",
           fill=CREAM, font=font("sans_bold", 22))
    # Down arrow on left side (Na out)
    d.text((px1 - 80, by0 - 100), "(builds Na⁺ gradient)",
           fill=MUTED, font=font("serif_ital", 22))

    # Middle: the symporter
    px2 = bx0 + 580
    d.rounded_rectangle([px2, by0 - 50, px2 + 160, by1 + 50],
                        radius=28, fill=ACCENT,
                        outline=MAROON_DARK, width=4)
    d.text((px2 + 15, (by0 + by1) // 2 - 30), "SGLT1",
           fill=CREAM, font=font("sans_bold", 28))
    d.text((px2 + 5, (by0 + by1) // 2 + 10), "symporter",
           fill=CREAM, font=font("sans_bold", 22))

    # Na+ ion going IN at top, downhill (huge gradient)
    nx = px2 + 30
    d.ellipse([nx - 18, by0 - 110, nx + 18, by0 - 74],
              fill=ACCENT, outline=MAROON_DARK, width=3)
    d.text((nx - 14, by0 - 102), "Na⁺", fill=CREAM,
           font=font("sans_bold", 18))
    d.line([(nx, by0 - 70), (nx, by1 + 70)],
           fill=ACCENT, width=8)
    d.polygon([(nx - 12, by1 + 50), (nx + 12, by1 + 50),
               (nx, by1 + 80)], fill=ACCENT)
    d.text((px2 - 130, by0 - 110), "Na⁺ downhill",
           fill=ACCENT, font=font("sans_bold", 26))

    # Glucose going IN at top, uphill — but hitched to Na+
    gx = px2 + 130
    d.ellipse([gx - 22, by0 - 110, gx + 22, by0 - 66],
              fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((gx - 22, by0 - 100), "glu", fill=CREAM,
           font=font("sans_bold", 18))
    d.line([(gx, by0 - 60), (gx, by1 + 70)],
           fill=MAROON, width=8)
    d.polygon([(gx - 12, by1 + 50), (gx + 12, by1 + 50),
               (gx, by1 + 80)], fill=MAROON)
    d.text((gx + 30, by0 - 110), "glucose uphill",
           fill=MAROON, font=font("sans_bold", 26))

    # Right side label
    d.text((bx1 - 230, by0 - 110), "(downhill Na⁺",
           fill=MUTED, font=font("serif_ital", 22))
    d.text((bx1 - 230, by0 - 80), "drags glucose along)",
           fill=MUTED, font=font("serif_ital", 22))

    # Symporter vs antiporter footer
    d.rounded_rectangle([110, 770, W // 2 - 20, 900], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((140, 790), "SYMPORT",
           fill=ACCENT, font=font("serif_bold", 38))
    d.text((140, 850), "both molecules same direction",
           fill=INK, font=font("sans", 26))
    d.text((140, 880), "(Na⁺ + glucose, intestine)",
           fill=MUTED, font=font("serif_ital", 24))

    d.rounded_rectangle([W // 2 + 20, 770, W - 110, 900], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((W // 2 + 50, 790), "ANTIPORT",
           fill=MAROON, font=font("serif_bold", 38))
    d.text((W // 2 + 50, 850), "molecules OPPOSITE directions",
           fill=INK, font=font("sans", 26))
    d.text((W // 2 + 50, 880), "(Na⁺ / Ca²⁺ exchanger, heart)",
           fill=MUTED, font=font("serif_ital", 24))

    # Bottom takeaway
    d.rounded_rectangle([110, 920, W - 110, 1010], radius=18,
                        fill=ACCENT, outline=MAROON, width=4)
    centered(d, "Still costs ATP  —  just one step removed (the Na/K pump did it earlier).",
             font("serif_bold", 32), 944, CREAM)
deck.custom("09_active_transport_secondary", active_secondary)


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Drop an animal red blood cell  AND  a plant cell  into pure distilled water.",
           "What happens to each?",
           hint="Pause now. Solve it. Press play when you're ready.")

# 11 — duplicate the pause slide for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — bulk transport: endo + exocytosis
def bulk_transport(img, d):
    d.text((110, 70), "Bulk transport.  Vesicles in, vesicles out.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 150), "For really big stuff  —  bacteria, fluid, proteins.  Uses ATP.",
           fill=MUTED, font=font("sans", 28))

    # 4 panels: phago, pino, RME, exocytosis
    panels = [
        ("PHAGOCYTOSIS", "cell eating",
         "engulfs large particles\n(amoeba, white blood cell + bacterium)",
         "in"),
        ("PINOCYTOSIS", "cell drinking",
         "engulfs extracellular fluid\n+ whatever is dissolved in it",
         "in"),
        ("RECEPTOR-MEDIATED", "selective uptake",
         "ligands bind specific receptors\n→ coated pit → vesicle",
         "in"),
        ("EXOCYTOSIS", "secretion",
         "vesicle fuses with membrane\n→ contents released OUTSIDE",
         "out"),
    ]
    pw = 410
    ph = 700
    gap = 30
    start_x = (W - (pw * 4 + gap * 3)) // 2
    py = 220

    for i, (name, sub, body, direction) in enumerate(panels):
        x = start_x + i * (pw + gap)
        color = ACCENT if direction == "in" else MAROON
        d.rounded_rectangle([x, py, x + pw, py + ph], radius=22,
                            outline=color, width=5, fill=CARD)
        d.rectangle([x, py, x + pw, py + 70], fill=color)
        f_h = font("sans_bold", 30)
        tw = d.textlength(name, font=f_h)
        d.text((x + pw // 2 - tw / 2, py + 16), name,
               fill=CREAM, font=f_h)
        d.text((x + 20, py + 90), sub, fill=MUTED,
               font=font("serif_ital", 26))

        # Diagram area: a flat membrane with a vesicle
        mem_y = py + 380
        d.line([(x + 30, mem_y), (x + pw - 30, mem_y)],
               fill=MAROON_DARK, width=6)
        if direction == "in":
            # Vesicle inside (below membrane)
            cx = x + pw // 2
            d.ellipse([cx - 60, mem_y + 30, cx + 60, mem_y + 150],
                      fill="white" if False else (255, 255, 255),
                      outline=color, width=4)
            # Cargo inside
            if i == 0:  # phago — bacterium
                d.ellipse([cx - 40, mem_y + 55, cx + 40, mem_y + 95],
                          fill=RED, outline=MAROON_DARK, width=2)
            elif i == 1:  # pino — fluid dots
                for j, dx in enumerate([-30, 0, 30]):
                    d.ellipse([cx + dx - 8, mem_y + 75 - 8,
                               cx + dx + 8, mem_y + 75 + 8],
                              fill=ACCENT_LT, outline=MAROON_DARK,
                              width=2)
            else:  # RME — specific receptors + ligands
                d.ellipse([cx - 30, mem_y + 65, cx + 30, mem_y + 105],
                          fill=ACCENT, outline=MAROON_DARK, width=2)
                d.text((cx - 25, mem_y + 75), "ligand",
                       fill=CREAM, font=font("sans_bold", 16))
            # Arrow downward
            d.line([(cx, mem_y - 30), (cx, mem_y + 25)],
                   fill=color, width=6)
            d.polygon([(cx - 10, mem_y + 15), (cx + 10, mem_y + 15),
                       (cx, mem_y + 35)], fill=color)
            d.text((cx - 40, mem_y - 60), "IN",
                   fill=color, font=font("sans_bold", 32))
        else:
            # Vesicle outside (above membrane) — exocytosis
            cx = x + pw // 2
            d.ellipse([cx - 60, mem_y - 150, cx + 60, mem_y - 30],
                      fill=(255, 255, 255), outline=color, width=4)
            # cargo: neurotransmitter dots
            for j, dx in enumerate([-30, 0, 30]):
                d.ellipse([cx + dx - 8, mem_y - 90 - 8,
                           cx + dx + 8, mem_y - 90 + 8],
                          fill=MAROON, outline=MAROON_DARK, width=2)
            d.line([(cx, mem_y + 30), (cx, mem_y - 20)],
                   fill=color, width=6)
            d.polygon([(cx - 10, mem_y - 10), (cx + 10, mem_y - 10),
                       (cx, mem_y - 30)], fill=color)
            d.text((cx - 50, mem_y + 50), "OUT",
                   fill=color, font=font("sans_bold", 32))

        # Body text
        for k, line in enumerate(body.split("\n")):
            d.text((x + 20, py + 560 + k * 36), line,
                   fill=INK, font=font("sans", 22))

    # Bottom strip
    d.rounded_rectangle([110, 950, W - 110, 1030], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "All four use ATP  —  membrane reshaping is metabolically expensive.",
             font("serif_bold", 30), 970, MAROON_DARK)
deck.custom("12_bulk_transport", bulk_transport)


# 13 — real world examples
def real_world(img, d):
    d.text((110, 70), "Where this lives in your body.",
           fill=MAROON, font=font("serif_bold", 60))

    examples = [
        ("KIDNEY",
         "Na/K pumps + aquaporins in nephrons reabsorb water and ions  —  decide what gets peed out.",
         "Tonicity gradient in the medulla  →  concentrated urine."),
        ("NEURON  /  ACTION POTENTIAL",
         "Every spike fires by collapsing the Na⁺/K⁺ gradient the pump spent ATP to build.",
         "Voltage-gated Na⁺ then K⁺ channels open in sequence."),
        ("INTESTINE  /  ABSORBING FOOD",
         "Sodium-glucose cotransport pulls sugar from gut lumen into blood — uphill into the cell.",
         "Then GLUT-2 carriers passively move glucose into capillaries."),
    ]

    y = 210
    for head, body, sub in examples:
        # Card
        d.rounded_rectangle([110, y, W - 110, y + 220], radius=22,
                            outline=ACCENT, width=5, fill=CARD)
        # Tag stripe on left
        d.rectangle([110, y, 140, y + 220], fill=ACCENT)
        d.text((180, y + 24), head, fill=MAROON_DARK,
               font=font("serif_bold", 42))
        d.text((180, y + 90), body, fill=INK, font=font("sans", 28))
        d.text((180, y + 160), sub, fill=ACCENT,
               font=font("serif_ital", 26))
        y += 250

    # Bottom punchline
    d.rounded_rectangle([110, 970, W - 110, 1040], radius=18,
                        fill=ACCENT, outline=MAROON, width=4)
    centered(d, "Membrane transport  =  how you think, absorb food, and stay hydrated.",
             font("serif_bold", 30), 990, CREAM)
deck.custom("13_real_world_examples", real_world)


# 14 — compare slide for common AP traps
deck.compare("14_compare_traps",
             "Common AP traps  —  read carefully.",
             left={
                 "label": "✗   COMMON WRONG INTUITION",
                 "color": RED,
                 "lines": [
                     "Hypertonic = high water.",
                     "",
                     "Facilitated diffusion uses ATP",
                     "(it uses a protein, so…).",
                     "",
                     "Osmosis moves solute.",
                     "",
                     "Plant cells lyse in distilled water.",
                 ],
                 "footnote": "These all look reasonable on a quick read."
             },
             right={
                 "label": "✓   ACTUALLY TRUE",
                 "color": ACCENT,
                 "lines": [
                     "Hypertonic = high SOLUTE, LOW water.",
                     "",
                     "Facilitated diffusion is PASSIVE.",
                     "Proteins ≠ ATP.",
                     "",
                     "Osmosis moves WATER.  Solute makes the gradient.",
                     "",
                     "Plant cells become TURGID — wall stops lysis.",
                 ],
                 "footnote": "Memorize the wording.  Exam questions are written around these."
             })


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Fluid mosaic: phospholipid bilayer + integral/peripheral proteins + glycoproteins + cholesterol.",
    "Selective permeability: small nonpolar = free.  Charged or large polar = needs a protein.",
    "Passive (NO ATP, downhill): simple diffusion, facilitated diffusion (channels/carriers), osmosis.",
    "Active (USES ATP, uphill): Na/K ATPase pumps 3 Na⁺ OUT and 2 K⁺ IN per ATP.",
    "Secondary active rides on the gradient primary made.  Bulk transport = vesicles (endo/exocytosis).",
], assignment=[
    "1.  Predict water movement and cell fate (animal + plant) in 3 tonicity scenarios.",
    "2.  Diagram the Na⁺/K⁺ pump showing ion stoichiometry and ATP use.",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapter 5 — Structure and Function of Plasma Membranes"),
    ("2.", "Khan Academy AP Bio",     "Membrane transport + tonicity problem sets"),
    ("3.", "Assignment in dashboard", "Tonicity scenarios + Na/K pump diagram"),
    ("4.", "Advisor check-in",        "If osmosis direction or active-vs-passive still feels slippery"),
], next_text="Next up:  Module 4 — Cell Communication.")


print("AP Biology Module 3 slides built.")

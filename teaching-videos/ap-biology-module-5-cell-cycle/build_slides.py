"""AP Biology · Module 5 — Cell Cycle and Division.

Teal (science) theme auto-resolved from "AP Biology". 16 slides total.
Heavy on customs because the cell-cycle ring, mitosis phase strip, and
cytokinesis compare each need real diagrams. Pause slide (10) is
duplicated to 11 so the same image plays during both Q and A.
"""
import sys
import math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, CREAM,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Biology", module_num=5, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 5 — Cell Cycle and Division",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook: 3.8 million cells per second + a single decision
def hook(img, d):
    d.text((110, 80), "3.8 million decisions per second.",
           fill=MAROON, font=font("serif_bold", 64))

    # Left panel: the big number
    lx, ly, lw, lh = 140, 230, 760, 540
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    big = "3,800,000"
    bf = font("serif_bold", 140)
    tw = d.textlength(big, font=bf)
    d.text((lx + lw // 2 - tw / 2, ly + 130), big,
           fill=MAROON_DARK, font=bf)
    cap = "new cells  ·  every second"
    cf = font("serif_bold", 42)
    tw2 = d.textlength(cap, font=cf)
    d.text((lx + lw // 2 - tw2 / 2, ly + 320), cap,
           fill=ACCENT, font=cf)
    sub = "Right now, in your body."
    sf = font("sans", 30)
    tw3 = d.textlength(sub, font=sf)
    d.text((lx + lw // 2 - tw3 / 2, ly + 400), sub,
           fill=MUTED, font=sf)

    # Right panel: one cell making a decision (divide / don't / die)
    rx, ry, rw, rh = 1020, 230, 760, 540
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    cap2 = "Each cell asks one question:"
    tw4 = d.textlength(cap2, font=cf)
    d.text((rx + rw // 2 - tw4 / 2, ry + 40), cap2,
           fill=MAROON_DARK, font=cf)

    # The single cell in the middle
    ccx, ccy = rx + rw // 2, ry + 230
    d.ellipse([ccx - 60, ccy - 60, ccx + 60, ccy + 60],
              fill=ACCENT_LT, outline=MAROON_DARK, width=4)
    d.text((ccx - 11, ccy - 20), "?", fill=MAROON_DARK,
           font=font("serif_bold", 56))

    # Three arrows: divide, stay, die
    arrow_y = ccy + 130
    options = [
        ("DIVIDE", rx + 100,  ACCENT),
        ("STAY",   ccx - 50,  MUTED),
        ("DIE",    rx + rw - 200, MAROON_DARK),
    ]
    for label, ox, color in options:
        # arrow line
        d.line([(ccx, ccy + 60), (ox + 50, arrow_y)],
               fill=color, width=4)
        d.text((ox, arrow_y + 10), label, fill=color,
               font=font("sans_bold", 30))

    foot = "When the answer breaks → cancer."
    ff = font("sans_bold", 30)
    tw5 = d.textlength(foot, font=ff)
    d.text((rx + rw // 2 - tw5 / 2, ry + rh - 60), foot,
           fill=MAROON_DARK, font=ff)

    # Bottom punchline strip
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Cancer = the cell-cycle decision system breaks. Today: how it normally works.",
             font("serif_bold", 36), 850, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "The cell cycle — G1, S, G2, M (and G0 as the exit ramp).",
    "Mitosis (5 phases) and cytokinesis (animal vs. plant).",
    "Regulation — cyclins, CDKs, checkpoints — and cancer when it breaks.",
], footnote="By the end: you can explain why p53 is mutated in >50% of cancers.")


# 04 — cell cycle overview (custom: ring diagram with G1/S/G2/M and G0 exit)
def cell_cycle_overview(img, d):
    d.text((110, 70), "The cell cycle  —  one full loop.",
           fill=MAROON, font=font("serif_bold", 60))

    # Big ring centered slightly left
    cx, cy = 720, 580
    R = 290
    inner = 200
    # Phase angles (degrees, 0 = right, going clockwise from top)
    # Standard pie: G1 = 40% (largest), S = 25%, G2 = 25%, M = 10%
    phases = [
        ("G1",  0,   144, ACCENT_LT, "growth"),
        ("S",   144, 234, ACCENT,    "DNA replication"),
        ("G2",  234, 324, ACCENT_LT, "more growth"),
        ("M",   324, 360, MAROON,    "mitosis + cytokinesis"),
    ]
    for name, a0, a1, col, sub in phases:
        # Shift so 0° is at the top, going clockwise
        # PIL's pieslice: 0° = 3-o'clock, going clockwise.
        # We want 0° at top (12 o'clock) → subtract 90.
        d.pieslice([cx - R, cy - R, cx + R, cy + R],
                   start=a0 - 90, end=a1 - 90,
                   fill=col, outline=MAROON_DARK, width=4)
    # Inner cutout to make it a ring
    d.ellipse([cx - inner, cy - inner, cx + inner, cy + inner],
              fill=CARD, outline=MAROON_DARK, width=4)
    # Label "INTERPHASE" in the donut hole
    centered_lbl = "INTERPHASE"
    lf = font("serif_bold", 36)
    tw = d.textlength(centered_lbl, font=lf)
    d.text((cx - tw / 2, cy - 50), centered_lbl,
           fill=MAROON, font=lf)
    sub_lbl = "G1 + S + G2"
    sf = font("sans_bold", 28)
    tw2 = d.textlength(sub_lbl, font=sf)
    d.text((cx - tw2 / 2, cy - 5), sub_lbl,
           fill=ACCENT, font=sf)
    sub3 = "→ then M phase"
    sf2 = font("sans", 26)
    tw3 = d.textlength(sub3, font=sf2)
    d.text((cx - tw3 / 2, cy + 35), sub3,
           fill=MUTED, font=sf2)

    # Phase labels around the ring
    label_positions = [
        ("G1", 72,  "growth"),
        ("S",  189, "DNA replication"),
        ("G2", 279, "prep for mitosis"),
        ("M",  342, "mitosis + cytokinesis"),
    ]
    for name, ang_deg, sub in label_positions:
        ang = math.radians(ang_deg - 90)
        lx = cx + (R + 70) * math.cos(ang)
        ly = cy + (R + 70) * math.sin(ang)
        nf = font("serif_bold", 56)
        tw = d.textlength(name, font=nf)
        d.text((lx - tw / 2, ly - 40), name,
               fill=MAROON_DARK, font=nf)
        sf3 = font("sans", 22)
        tw2 = d.textlength(sub, font=sf3)
        d.text((lx - tw2 / 2, ly + 30), sub,
               fill=MUTED, font=sf3)

    # G0 exit on the right
    g0_x, g0_y = 1380, 580
    d.ellipse([g0_x - 110, g0_y - 110, g0_x + 110, g0_y + 110],
              fill=ACCENT_LT, outline=MAROON, width=5)
    centered_g0 = "G0"
    gf = font("serif_bold", 70)
    tw = d.textlength(centered_g0, font=gf)
    d.text((g0_x - tw / 2, g0_y - 50), centered_g0,
           fill=MAROON, font=gf)
    # Arrow from G1 → G0
    d.line([(cx + R - 20, cy - 30), (g0_x - 120, g0_y - 30)],
           fill=MUTED, width=5)
    d.polygon([
        (g0_x - 120, g0_y - 30),
        (g0_x - 140, g0_y - 42),
        (g0_x - 140, g0_y - 18),
    ], fill=MUTED)
    d.text((g0_x - 130, g0_y + 130), "EXIT  —  resting",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((g0_x - 160, g0_y + 170),
           "neurons, mature muscle", fill=MUTED,
           font=font("serif_ital", 24))

    # Bottom note
    d.rounded_rectangle([110, 940, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Interphase is the long part. M phase is fast (under an hour for most cells).",
             font("sans_bold", 28), 962, MAROON_DARK)
deck.custom("04_cell_cycle_overview", cell_cycle_overview)


# 05 — interphase detail (custom: 3 cards G1 / S / G2)
def interphase_detail(img, d):
    d.text((110, 70), "Interphase  =  G1  →  S  →  G2.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160),
           "S is the key one — DNA replication happens here, BEFORE mitosis.",
           fill=MUTED, font=font("sans", 30))

    cards = [
        ("G1", "Growth",
         ["Cell grows.",
          "Makes proteins.",
          "Organelles duplicate.",
          "",
          "DNA still 1 copy",
          "per chromosome."], ACCENT_LT),
        ("S", "DNA Synthesis",
         ["DNA replication.",
          "Every chromosome",
          "is copied.",
          "",
          "Each now has",
          "2 sister chromatids",
          "joined at the",
          "centromere."], ACCENT),
        ("G2", "Final Growth",
         ["More growth.",
          "Builds centrosomes.",
          "Builds microtubules.",
          "",
          "Prep for mitosis.",
          "Final check before",
          "splitting."], ACCENT_LT),
    ]
    col_w = 540
    col_h = 660
    gap = 40
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 230
    for i, (name, sub, lines, col) in enumerate(cards):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=20,
                            outline=MAROON_DARK, width=5, fill=col)
        d.text((x + 30, y0 + 24), name, fill=MAROON_DARK,
               font=font("serif_bold", 80))
        d.text((x + 30, y0 + 130), sub, fill=MAROON,
               font=font("sans_bold", 36))
        ly = y0 + 220
        for ln in lines:
            d.text((x + 30, ly), ln, fill=INK,
                   font=font("sans", 28))
            ly += 50

        # Arrow to next card
        if i < 2:
            ax = x + col_w + 4
            ay = y0 + col_h // 2
            d.polygon([
                (ax, ay - 20),
                (ax + 30, ay),
                (ax, ay + 20),
            ], fill=ACCENT)

    # Tiny chromatid visual at the bottom
    d.rounded_rectangle([110, 920, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "1 chromosome before S  →  2 sister chromatids after S  →  separate again in anaphase.",
             font("sans_bold", 28), 945, MAROON_DARK)
deck.custom("05_interphase_detail", interphase_detail)


# 06 — mitosis overview (custom: 5-phase strip with mini-diagrams)
def mitosis_overview(img, d):
    d.text((110, 70), "Mitosis  —  5 phases.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 160),
           "Prophase  →  Prometaphase  →  Metaphase  →  Anaphase  →  Telophase",
           fill=ACCENT, font=font("sans_bold", 34))

    phases = [
        ("PROPHASE",     "chromatin condenses"),
        ("PROMETAPHASE", "envelope breaks"),
        ("METAPHASE",    "chromosomes align"),
        ("ANAPHASE",     "chromatids separate"),
        ("TELOPHASE",    "nuclei reform"),
    ]
    box_w = 320
    box_h = 540
    gap = 30
    start_x = (W - (box_w * 5 + gap * 4)) // 2
    y0 = 260
    for i, (name, sub) in enumerate(phases):
        x = start_x + i * (box_w + gap)
        d.rounded_rectangle([x, y0, x + box_w, y0 + box_h], radius=18,
                            outline=ACCENT, width=4, fill=CARD)
        # Number circle
        nc_x, nc_y = x + box_w // 2, y0 + 50
        d.ellipse([nc_x - 32, nc_y - 32, nc_x + 32, nc_y + 32],
                  fill=ACCENT, outline=MAROON_DARK, width=3)
        nf = font("serif_bold", 38)
        nstr = str(i + 1)
        tw = d.textlength(nstr, font=nf)
        d.text((nc_x - tw / 2, nc_y - 24), nstr,
               fill=CREAM, font=nf)
        # Mini-diagram for each phase
        dx, dy = x + box_w // 2, y0 + 200
        if i == 0:  # Prophase: condensed chromosomes inside intact envelope
            d.ellipse([dx - 90, dy - 90, dx + 90, dy + 90],
                      outline=MAROON_DARK, width=4, fill=CREAM)
            # 3 X-shaped chromosomes inside
            for ox, oy in [(-30, -20), (20, 10), (-10, 30)]:
                d.line([(dx + ox - 12, dy + oy - 12),
                        (dx + ox + 12, dy + oy + 12)],
                       fill=MAROON_DARK, width=5)
                d.line([(dx + ox - 12, dy + oy + 12),
                        (dx + ox + 12, dy + oy - 12)],
                       fill=MAROON_DARK, width=5)
        elif i == 1:  # Prometaphase: envelope dissolving + spindle attaches
            # dashed envelope
            for ang in range(0, 360, 25):
                a1 = math.radians(ang)
                a2 = math.radians(ang + 12)
                d.line([(dx + 90 * math.cos(a1), dy + 90 * math.sin(a1)),
                        (dx + 90 * math.cos(a2), dy + 90 * math.sin(a2))],
                       fill=MAROON_DARK, width=4)
            # Spindle lines from poles
            for ox, oy in [(-25, 0), (10, -15), (15, 20)]:
                d.line([(dx - 130, dy), (dx + ox, dy + oy)],
                       fill=ACCENT, width=2)
                d.line([(dx + 130, dy), (dx + ox, dy + oy)],
                       fill=ACCENT, width=2)
                d.line([(dx + ox - 10, dy + oy - 10),
                        (dx + ox + 10, dy + oy + 10)],
                       fill=MAROON_DARK, width=5)
                d.line([(dx + ox - 10, dy + oy + 10),
                        (dx + ox + 10, dy + oy - 10)],
                       fill=MAROON_DARK, width=5)
        elif i == 2:  # Metaphase: chromosomes lined up at the equator
            # Equator line
            d.line([(dx - 100, dy), (dx + 100, dy)],
                   fill=MUTED, width=2)
            for oy in [-50, -20, 10, 40]:
                d.line([(dx - 12, dy + oy - 12),
                        (dx + 12, dy + oy + 12)],
                       fill=MAROON_DARK, width=5)
                d.line([(dx - 12, dy + oy + 12),
                        (dx + 12, dy + oy - 12)],
                       fill=MAROON_DARK, width=5)
            # Poles
            d.ellipse([dx - 130, dy - 8, dx - 114, dy + 8], fill=ACCENT)
            d.ellipse([dx + 114, dy - 8, dx + 130, dy + 8], fill=ACCENT)
        elif i == 3:  # Anaphase: chromatids being pulled apart
            for oy in [-40, 0, 30]:
                # Left chromatid
                d.line([(dx - 70, dy + oy - 8),
                        (dx - 50, dy + oy + 8)],
                       fill=MAROON_DARK, width=5)
                # Right chromatid
                d.line([(dx + 50, dy + oy - 8),
                        (dx + 70, dy + oy + 8)],
                       fill=MAROON_DARK, width=5)
                # Arrows
                d.line([(dx - 30, dy + oy), (dx - 80, dy + oy)],
                       fill=ACCENT, width=3)
                d.line([(dx + 30, dy + oy), (dx + 80, dy + oy)],
                       fill=ACCENT, width=3)
            d.ellipse([dx - 130, dy - 8, dx - 114, dy + 8], fill=ACCENT)
            d.ellipse([dx + 114, dy - 8, dx + 130, dy + 8], fill=ACCENT)
        elif i == 4:  # Telophase: two nuclei reforming
            d.ellipse([dx - 110, dy - 60, dx - 10, dy + 60],
                      outline=MAROON_DARK, width=4, fill=CREAM)
            d.ellipse([dx + 10, dy - 60, dx + 110, dy + 60],
                      outline=MAROON_DARK, width=4, fill=CREAM)
            for ox in [-60, 60]:
                # decondensing chromatin (squiggles)
                d.text((dx + ox - 10, dy - 14), "~", fill=MAROON_DARK,
                       font=font("serif_bold", 40))

        # Name + sub
        d.text((x + 20, y0 + 380), name, fill=MAROON_DARK,
               font=font("sans_bold", 26))
        d.text((x + 20, y0 + 420), sub, fill=ACCENT,
               font=font("sans", 24))

    # Bottom mnemonic strip
    d.rounded_rectangle([110, 870, W - 110, 990], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Mnemonic:  People  Meet  At  The  Equator   then   Apart  They  Go.",
             font("serif_bold", 32), 895, MAROON_DARK)
    centered(d, "Prophase · Prometaphase · Metaphase · Anaphase · Telophase",
             font("sans", 28), 945, MUTED)
deck.custom("06_mitosis_overview", mitosis_overview)


# 07 — mitosis phases detail (custom: table of key molecular events)
def mitosis_phases_detail(img, d):
    d.text((110, 70), "What actually happens in each phase.",
           fill=MAROON, font=font("serif_bold", 56))

    headers = [("PHASE", 140), ("KEY EVENT", 530),
               ("KEY PLAYERS", 1200)]
    header_y = 200
    d.rectangle([110, header_y, W - 110, header_y + 60], fill=ACCENT)
    for label, x in headers:
        d.text((x, header_y + 14), label, fill=CREAM,
               font=font("sans_bold", 28))

    rows = [
        ("Prophase",
         "Chromatin condenses; nucleolus disappears.",
         "centrosomes, spindle begins"),
        ("Prometaphase",
         "Nuclear envelope breaks down.",
         "kinetochore + microtubule"),
        ("Metaphase",
         "Chromosomes align at the metaphase plate.",
         "spindle checkpoint here"),
        ("Anaphase",
         "Sister chromatids SEPARATE → pulled to poles.",
         "SEPARASE cleaves COHESIN"),
        ("Telophase",
         "Nuclear envelopes reform; chromosomes decondense.",
         "spindle disassembles"),
    ]
    row_h = 110
    y = header_y + 60
    for i, (phase, event, players) in enumerate(rows):
        bg = CARD if i % 2 == 0 else ACCENT_LT
        d.rectangle([110, y, W - 110, y + row_h], fill=bg)
        # Number bullet
        bx = 130
        by = y + row_h // 2
        d.ellipse([bx - 22, by - 22, bx + 22, by + 22],
                  fill=ACCENT, outline=MAROON_DARK, width=2)
        ns = str(i + 1)
        nf = font("serif_bold", 28)
        tw = d.textlength(ns, font=nf)
        d.text((bx - tw / 2, by - 18), ns, fill=CREAM, font=nf)
        d.text((175, y + 24), phase, fill=MAROON_DARK,
               font=font("sans_bold", 30))
        d.text((175, y + 64), "",
               fill=MUTED, font=font("sans", 22))
        d.text((530, y + 24), event, fill=INK,
               font=font("sans", 28))
        d.text((1200, y + 24), players, fill=MAROON_DARK,
               font=font("sans_bold", 24))
        y += row_h
    d.rectangle([110, header_y, W - 110, y], outline=MAROON, width=4)

    # Bottom note
    d.rounded_rectangle([110, y + 20, W - 110, y + 130], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Anaphase is the moment of separation. Before that, sister chromatids stay glued by cohesin.",
             font("sans_bold", 26), y + 55, MAROON_DARK)
deck.custom("07_mitosis_phases_detail", mitosis_phases_detail)


# 08 — cytokinesis compare (custom: 2-column animal vs plant with diagrams)
def cytokinesis_compare(img, d):
    d.text((110, 70), "Cytokinesis  —  animal vs. plant.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160), "Same outcome (2 cells). Completely different mechanism.",
           fill=MUTED, font=font("sans", 30))

    # Left: Animal
    lx, ly = 110, 240
    lw, lh = 870, 740
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "ANIMAL CELL", fill=ACCENT,
           font=font("sans_bold", 44))
    d.text((lx + 30, ly + 80), "Cleavage furrow",
           fill=MAROON_DARK, font=font("serif_bold", 36))
    d.text((lx + 30, ly + 130), "Actin + myosin contractile ring",
           fill=INK, font=font("sans", 28))
    d.text((lx + 30, ly + 170), "pinches the cell from the OUTSIDE IN.",
           fill=INK, font=font("sans", 28))
    d.text((lx + 30, ly + 220), "Think:  drawstring on a bag.",
           fill=ACCENT, font=font("serif_ital", 28))

    # Diagram: cell with cleavage furrow
    cx = lx + lw // 2
    cy = ly + 470
    # Original cell shape — pinched in the middle
    # Use two ellipses + connecting bulge
    d.ellipse([cx - 180, cy - 130, cx - 20, cy + 130],
              outline=MAROON_DARK, width=5, fill=ACCENT_LT)
    d.ellipse([cx + 20, cy - 130, cx + 180, cy + 130],
              outline=MAROON_DARK, width=5, fill=ACCENT_LT)
    # Nuclei
    d.ellipse([cx - 130, cy - 40, cx - 70, cy + 40],
              fill=MAROON, outline=MAROON_DARK, width=3)
    d.ellipse([cx + 70, cy - 40, cx + 130, cy + 40],
              fill=MAROON, outline=MAROON_DARK, width=3)
    # Inward arrows showing the furrow pinch
    d.polygon([(cx - 30, cy - 90), (cx - 60, cy - 100), (cx - 60, cy - 80)],
              fill=ACCENT)
    d.polygon([(cx + 30, cy - 90), (cx + 60, cy - 100), (cx + 60, cy - 80)],
              fill=ACCENT)
    d.polygon([(cx - 30, cy + 90), (cx - 60, cy + 100), (cx - 60, cy + 80)],
              fill=ACCENT)
    d.polygon([(cx + 30, cy + 90), (cx + 60, cy + 100), (cx + 60, cy + 80)],
              fill=ACCENT)
    d.text((cx - 90, cy + 160), "furrow pinches inward",
           fill=MUTED, font=font("serif_ital", 24))

    # Right: Plant
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "PLANT CELL", fill=MAROON_DARK,
           font=font("sans_bold", 44))
    d.text((rx + 30, ly + 80), "Cell plate",
           fill=MAROON_DARK, font=font("serif_bold", 36))
    d.text((rx + 30, ly + 130), "Vesicles from the Golgi fuse",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 170), "at the middle → new cell wall.",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 220), "Builds from the INSIDE OUT.",
           fill=ACCENT, font=font("serif_ital", 28))

    # Diagram: rectangular plant cell with cell plate forming in middle
    pcx = rx + rw // 2
    pcy = ly + 470
    # Outer cell wall (rectangle with rounded corners)
    d.rounded_rectangle([pcx - 220, pcy - 150, pcx + 220, pcy + 150],
                        radius=8, outline=MAROON_DARK, width=6,
                        fill=ACCENT_LT)
    # Cell plate vesicles down the middle
    for vy in range(-130, 140, 22):
        d.ellipse([pcx - 12, pcy + vy - 8, pcx + 12, pcy + vy + 8],
                  fill=MAROON, outline=MAROON_DARK, width=2)
    # Nuclei on each side
    d.ellipse([pcx - 160, pcy - 40, pcx - 100, pcy + 40],
              fill=MAROON, outline=MAROON_DARK, width=3)
    d.ellipse([pcx + 100, pcy - 40, pcx + 160, pcy + 40],
              fill=MAROON, outline=MAROON_DARK, width=3)
    # Arrows showing vesicle fusion outward
    d.line([(pcx - 50, pcy - 130), (pcx - 14, pcy - 130)],
           fill=ACCENT, width=3)
    d.polygon([(pcx - 14, pcy - 130), (pcx - 30, pcy - 138),
               (pcx - 30, pcy - 122)], fill=ACCENT)
    d.line([(pcx + 50, pcy - 130), (pcx + 14, pcy - 130)],
           fill=ACCENT, width=3)
    d.polygon([(pcx + 14, pcy - 130), (pcx + 30, pcy - 138),
               (pcx + 30, pcy - 122)], fill=ACCENT)
    d.text((pcx - 90, pcy + 175), "cell plate builds outward",
           fill=MUTED, font=font("serif_ital", 24))

    # Bottom WHY strip
    d.rounded_rectangle([110, 1000, W - 110, 1060], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "WHY different?  Plants have a rigid cell wall — they can't pinch.",
             font("sans_bold", 26), 1013, MAROON_DARK)
deck.custom("08_cytokinesis_compare", cytokinesis_compare)


# 09 — checkpoints (custom: 3 checkpoints on a horizontal timeline)
def checkpoints(img, d):
    d.text((110, 70), "Three checkpoints. One asks the most.",
           fill=MAROON, font=font("serif_bold", 56))

    # Timeline bar with stops at G1, G2, M
    bar_y = 360
    bar_x0 = 200
    bar_x1 = W - 200
    d.rectangle([bar_x0, bar_y - 8, bar_x1, bar_y + 8],
                fill=ACCENT_LT, outline=MAROON_DARK, width=3)

    # Phase labels along the bar
    seg_len = (bar_x1 - bar_x0) // 4
    seg_labels = [("G1", 0), ("S", 1), ("G2", 2), ("M", 3)]
    for name, i in seg_labels:
        sx = bar_x0 + i * seg_len + seg_len // 2
        d.text((sx - 20, bar_y - 60), name, fill=MAROON_DARK,
               font=font("serif_bold", 42))

    # Checkpoints (stop signs) at G1 boundary, G2 boundary, M (middle)
    checks = [
        ("G1 CHECKPOINT",
         "RESTRICTION POINT",
         "Divide?  Enter G0?",
         "Most important — p53 lives here.",
         bar_x0 + int(0.95 * seg_len)),
        ("G2 CHECKPOINT",
         "DNA replicated correctly?",
         "Any damage?",
         "Fixes errors before mitosis.",
         bar_x0 + int(2.95 * seg_len)),
        ("M / SPINDLE CHECKPOINT",
         "All kinetochores attached?",
         "Hold until ready.",
         "Then trigger anaphase.",
         bar_x0 + int(3.55 * seg_len)),
    ]
    for i, (title, sub1, sub2, foot, x) in enumerate(checks):
        # Stop sign octagon
        s = 50
        # 8-sided
        pts = []
        for k in range(8):
            ang = math.radians(22.5 + k * 45)
            pts.append((x + s * math.cos(ang), bar_y + s * math.sin(ang)))
        d.polygon(pts, fill=MAROON, outline=MAROON_DARK)
        # Number inside
        nf = font("serif_bold", 38)
        nstr = str(i + 1)
        tw = d.textlength(nstr, font=nf)
        d.text((x - tw / 2, bar_y - 24), nstr, fill=CREAM, font=nf)
        # Card below with details (zigzag tall/short)
        card_y = bar_y + 100 if i % 2 == 0 else bar_y + 100
        card_w = 380
        card_h = 240
        cx = x - card_w // 2
        d.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h],
                            radius=14, outline=ACCENT, width=4, fill=CARD)
        d.text((cx + 16, card_y + 12), title, fill=ACCENT,
               font=font("sans_bold", 24))
        d.text((cx + 16, card_y + 56), sub1, fill=MAROON_DARK,
               font=font("sans_bold", 22))
        d.text((cx + 16, card_y + 92), sub2, fill=INK,
               font=font("sans", 22))
        d.text((cx + 16, card_y + 180), foot, fill=MUTED,
               font=font("serif_ital", 22))

    # Bottom key takeaway
    d.rounded_rectangle([110, 940, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "The G1 restriction point is the big one — once past it, the cell is committed to dividing.",
             font("sans_bold", 28), 962, MAROON_DARK)
deck.custom("09_checkpoints", checkpoints)


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "A cell with damaged DNA enters G1.  What single protein detects it?",
           "Protein =  ?     Two outcomes  =  ?",
           hint="Pause now. Think it through. Press play when you're ready.")

# 11 — duplicate the pause slide for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — cyclins + CDKs (custom: rising/falling cyclin curve + MPF box)
def cyclins_cdks(img, d):
    d.text((110, 70), "Cyclins  +  CDKs  —  the molecular timer.",
           fill=MAROON, font=font("serif_bold", 54))

    # Left: cyclin concentration curve over the cycle
    lx, ly = 110, 200
    lw, lh = 1080, 580
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "Cyclin concentration rises and falls",
           fill=MAROON_DARK, font=font("sans_bold", 32))

    # Graph axes
    gx0 = lx + 80
    gy0 = ly + 470
    gx1 = lx + lw - 50
    gy1 = ly + 110
    # Axes
    d.line([(gx0, gy1), (gx0, gy0)], fill=MAROON_DARK, width=4)
    d.line([(gx0, gy0), (gx1, gy0)], fill=MAROON_DARK, width=4)
    d.text((lx + 10, ly + 80), "[cyclin]", fill=MAROON_DARK,
           font=font("sans_bold", 22))
    d.text((gx1 - 60, gy0 + 14), "time →", fill=MAROON_DARK,
           font=font("sans_bold", 22))

    # X-axis phase labels
    span = gx1 - gx0
    phase_widths = [0.40, 0.25, 0.25, 0.10]
    phase_names = ["G1", "S", "G2", "M"]
    sx = gx0
    for w, name in zip(phase_widths, phase_names):
        w_px = int(span * w)
        # Vertical phase divider
        d.line([(sx + w_px, gy0), (sx + w_px, gy0 + 12)],
               fill=MAROON_DARK, width=3)
        # Label centered in segment
        nf = font("sans_bold", 28)
        tw = d.textlength(name, font=nf)
        d.text((sx + w_px // 2 - tw / 2, gy0 + 20), name,
               fill=MAROON_DARK, font=nf)
        sx += w_px

    # Cyclin B curve: low through G1/S, rising through G2, peak at M, drop
    g_height = gy0 - gy1
    pts = []
    n_points = 60
    for i in range(n_points + 1):
        t = i / n_points
        # cumulative t through the phases
        # baseline + rising peak around 0.85-0.95
        # Simple: a smooth bump centered near t=0.9
        center = 0.88
        width = 0.18
        if t < center - width / 2:
            y_norm = 0.05 + 0.6 * (t / (center - width / 2)) ** 3
        elif t < center:
            # rapid rise
            x = (t - (center - width / 2)) / (width / 2)
            y_norm = 0.65 + 0.35 * x
        elif t < center + width / 4:
            # peak then sharp drop (mitosis ends → cyclin destroyed)
            x = (t - center) / (width / 4)
            y_norm = 1.0 - 0.9 * x
        else:
            y_norm = 0.1
        px = gx0 + int(t * span)
        py = gy0 - int(y_norm * g_height * 0.85)
        pts.append((px, py))
    # Draw curve
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=ACCENT, width=5)
    # Peak label
    peak_x = gx0 + int(0.88 * span)
    peak_y = gy0 - int(0.95 * g_height * 0.85)
    d.text((peak_x - 100, peak_y - 50), "MPF activates →",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    d.line([(peak_x - 5, peak_y - 18), (peak_x - 5, peak_y - 4)],
           fill=MAROON_DARK, width=3)

    # Right: MPF box
    rx = lx + lw + 30
    rw = W - 110 - rx
    rh = 580
    d.rounded_rectangle([rx, ly, rx + rw, ly + rh], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((rx + 30, ly + 20), "MPF", fill=MAROON_DARK,
           font=font("serif_bold", 64))
    d.text((rx + 30, ly + 100),
           "M-phase Promoting Factor",
           fill=MAROON_DARK, font=font("sans_bold", 22))
    # Equation
    d.text((rx + 30, ly + 170), "cyclin B", fill=ACCENT,
           font=font("sans_bold", 30))
    d.text((rx + 30, ly + 215), "      +", fill=INK,
           font=font("sans_bold", 30))
    d.text((rx + 30, ly + 260), "CDK1", fill=ACCENT,
           font=font("sans_bold", 30))
    d.text((rx + 30, ly + 320), "─────────", fill=MAROON,
           font=font("mono", 30))
    d.text((rx + 30, ly + 360), "= MPF", fill=MAROON_DARK,
           font=font("serif_bold", 38))
    d.text((rx + 30, ly + 440),
           "Triggers entry",
           fill=INK, font=font("sans", 24))
    d.text((rx + 30, ly + 470),
           "into MITOSIS.",
           fill=INK, font=font("sans", 24))
    d.text((rx + 30, ly + 520),
           "CDKs always present;",
           fill=MUTED, font=font("serif_ital", 22))
    d.text((rx + 30, ly + 548),
           "cyclins control timing.",
           fill=MUTED, font=font("serif_ital", 22))

    # Bottom takeaway
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Cyclin builds up  →  binds CDK  →  active complex phosphorylates targets  →  cell advances.",
             font("sans_bold", 28), 850, MAROON_DARK)
    centered(d, "Then cyclin is destroyed; CDK shuts off; the cycle resets.",
             font("serif_ital", 26), 895, MUTED)
deck.custom("12_cyclins_cdks", cyclins_cdks)


# 13 — cancer mechanisms (custom: 2 cards + p53 box)
def cancer_mechanisms(img, d):
    d.text((110, 70), "Cancer  =  loss of cell-cycle control.",
           fill=MAROON, font=font("serif_bold", 56))

    # Left: oncogenes
    lx, ly = 110, 200
    lw, lh = 870, 540
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "PROTO-ONCOGENE  →  ONCOGENE",
           fill=ACCENT, font=font("sans_bold", 34))
    d.text((lx + 30, ly + 80),
           "Normal job: PROMOTE division.",
           fill=INK, font=font("sans", 28))
    d.text((lx + 30, ly + 130),
           "Examples:  Ras  ·  Myc",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    # Gas-pedal-stuck visual
    pedal_y = ly + 200
    d.rounded_rectangle([lx + 30, pedal_y, lx + 220, pedal_y + 100],
                        radius=10, fill=ACCENT_LT, outline=MAROON_DARK,
                        width=4)
    d.text((lx + 50, pedal_y + 30), "GAS",
           fill=MAROON_DARK, font=font("sans_bold", 38))
    # Pedal pressed down
    d.line([(lx + 230, pedal_y + 80), (lx + 280, pedal_y + 100)],
           fill=MAROON, width=8)
    d.text((lx + 300, pedal_y + 30), "GAIN of function →",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((lx + 300, pedal_y + 65), "over-promotes division.",
           fill=INK, font=font("sans", 26))

    d.text((lx + 30, ly + 350),
           "Cellular dominance:",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((lx + 30, ly + 395),
           "ONE mutated copy is enough.",
           fill=ACCENT, font=font("serif_bold", 32))
    # Two alleles graphic
    a_y = ly + 460
    d.rectangle([lx + 30, a_y, lx + 130, a_y + 50],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((lx + 50, a_y + 8), "MUT", fill=CREAM,
           font=font("sans_bold", 24))
    d.rectangle([lx + 150, a_y, lx + 250, a_y + 50],
                fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((lx + 175, a_y + 8), "OK", fill=MAROON_DARK,
           font=font("sans_bold", 24))
    d.text((lx + 270, a_y + 8), "→  cancer-promoting",
           fill=MAROON, font=font("sans_bold", 26))

    # Right: tumor suppressors
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "TUMOR SUPPRESSOR",
           fill=MAROON_DARK, font=font("sans_bold", 34))
    d.text((rx + 30, ly + 80),
           "Normal job: RESTRAIN division.",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 130),
           "Examples:  p53  ·  Rb",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    # Brakes-cut visual
    brake_y = ly + 200
    d.rounded_rectangle([rx + 30, brake_y, rx + 220, brake_y + 100],
                        radius=10, fill=ACCENT_LT, outline=MAROON_DARK,
                        width=4)
    d.text((rx + 40, brake_y + 30), "BRAKE",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    # Brake line cut
    d.line([(rx + 230, brake_y + 50), (rx + 320, brake_y + 50)],
           fill=MUTED, width=4)
    d.line([(rx + 260, brake_y + 30), (rx + 290, brake_y + 70)],
           fill=MAROON, width=6)
    d.line([(rx + 260, brake_y + 70), (rx + 290, brake_y + 30)],
           fill=MAROON, width=6)
    d.text((rx + 340, brake_y + 30), "LOSS of function →",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 340, brake_y + 65), "no brakes on division.",
           fill=INK, font=font("sans", 26))

    d.text((rx + 30, ly + 350),
           "Cellular recessiveness:",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((rx + 30, ly + 395),
           "BOTH alleles must be knocked out.",
           fill=MAROON, font=font("serif_bold", 32))
    # Two alleles graphic — both must be mutated
    a_y = ly + 460
    d.rectangle([rx + 30, a_y, rx + 130, a_y + 50],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((rx + 50, a_y + 8), "MUT", fill=CREAM,
           font=font("sans_bold", 24))
    d.rectangle([rx + 150, a_y, rx + 250, a_y + 50],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((rx + 170, a_y + 8), "MUT", fill=CREAM,
           font=font("sans_bold", 24))
    d.text((rx + 270, a_y + 8), "→  cancer-promoting",
           fill=MAROON, font=font("sans_bold", 26))

    # Bottom p53 strip
    d.rounded_rectangle([110, 770, W - 110, 980], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    d.text((140, 790), "p53 — Guardian of the Genome.",
           fill=MAROON_DARK, font=font("serif_bold", 42))
    d.text((140, 855),
           "Detects DNA damage at G1 → halts cycle → triggers repair OR triggers apoptosis if unrepairable.",
           fill=INK, font=font("sans", 26))
    d.text((140, 905),
           "Mutated in >50% of all human cancers.",
           fill=MAROON, font=font("serif_bold", 36))
deck.custom("13_cancer_mechanisms", cancer_mechanisms)


# 14 — compare traps: oncogene vs tumor suppressor (using deck.compare)
deck.compare("14_compare_traps",
             "Common trap  —  oncogene vs. tumor suppressor.",
             left={"label": "ONCOGENE",
                   "color": MAROON,
                   "lines": [
                       "GAIN of function",
                       "(was: proto-oncogene)",
                       "",
                       "Gas pedal stuck DOWN.",
                       "",
                       "ONE bad copy is enough.",
                       "DOMINANT at cell level.",
                       "",
                       "Examples:  Ras · Myc",
                   ],
                   "footnote": "If '1 mutation caused it' → oncogene."},
             right={"label": "TUMOR SUPPRESSOR",
                    "color": ACCENT,
                    "lines": [
                        "LOSS of function",
                        "(brakes cut)",
                        "",
                        "Brakes removed entirely.",
                        "",
                        "BOTH alleles must fail.",
                        "RECESSIVE at cell level.",
                        "",
                        "Examples:  p53 · Rb",
                    ],
                    "footnote": "If 'both alleles lost' → tumor suppressor."})


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Cycle:  G1 → S → G2 → M;  G0 = exit ramp (neurons, mature muscle).",
    "DNA replicates in S → 2 sister chromatids per chromosome (until anaphase).",
    "Mitosis 5 phases:  prophase, prometaphase, metaphase, anaphase, telophase.",
    "Cytokinesis:  animal = cleavage furrow;  plant = cell plate.",
    "Cyclins + CDKs run checkpoints.  p53 guards G1.  MPF = cyclin B + CDK1 → mitosis.",
    "Cancer:  oncogenes GAIN function (dominant);  tumor suppressors LOSE function (recessive).",
], assignment=[
    "1.  Draw the cell cycle ring. Label G1, S, G2, M, G0, and all 3 checkpoints.",
    "2.  A cell has 1 mutated copy of p53 and 1 healthy copy. Will it become cancerous? Why or why not?",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapter 10 — cell cycle, mitosis, cancer"),
    ("2.", "Khan Academy AP Bio",     "Unit 4 problem sets — cell cycle and cancer"),
    ("3.", "Assignment in dashboard", "Cell cycle diagram + p53 cancer question (above)"),
    ("4.", "Advisor check-in",        "If checkpoints or oncogene-vs-suppressor still feel fuzzy"),
], next_text="Next up:  Module 6 — Mendelian Genetics  (Unit 5 begins).")


print("AP Biology Module 5 slides built.")

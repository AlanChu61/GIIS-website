"""AP Biology · Module 9 — Biotechnology.

Teal (science) theme auto-resolved from "AP Biology". 16 slides total.
Heavy on customs for the molecular tool diagrams — restriction enzyme
cut + sticky ends, gel electrophoresis ladder, PCR thermal cycler graph,
CRISPR mechanism, etc. Pause slide (10) is duplicated to 11 so the same
image plays during both Q and A sections.
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
deck = Deck(course="AP Biology", module_num=9, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 9 — Biotechnology",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook: four things parents/students touch every week, all biotech
def hook(img, d):
    d.text((110, 80), "You touch biotechnology every week.",
           fill=MAROON, font=font("serif_bold", 60))

    # Four icon cards in a row
    cards = [
        ("COVID-19 PCR", "the test in your nose", "PCR"),
        ("Insulin", "millions of diabetics", "recombinant DNA"),
        ("DNA evidence", "courtrooms worldwide", "STR fingerprinting"),
        ("Sickle-cell cure", "first patients, 2023", "CRISPR"),
    ]
    card_w = 400
    card_h = 460
    gap = 30
    start_x = (W - (card_w * 4 + gap * 3)) // 2
    y0 = 220
    for i, (title, sub, tag) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        # Card
        d.rounded_rectangle([x, y0, x + card_w, y0 + card_h], radius=22,
                            outline=ACCENT, width=5, fill=CARD)
        # Title strip at top
        d.rounded_rectangle([x, y0, x + card_w, y0 + 70], radius=22,
                            fill=ACCENT)
        d.rectangle([x, y0 + 22, x + card_w, y0 + 70], fill=ACCENT)
        tf = font("serif_bold", 34)
        tw = d.textlength(title, font=tf)
        d.text((x + card_w // 2 - tw / 2, y0 + 16), title, fill=CREAM, font=tf)

        # Tool tag — pill near bottom
        tag_y = y0 + 150
        tagf = font("sans_bold", 26)
        ttw = d.textlength(tag.upper(), font=tagf)
        d.rounded_rectangle(
            [x + card_w // 2 - ttw / 2 - 22, tag_y,
             x + card_w // 2 + ttw / 2 + 22, tag_y + 50],
            radius=14, fill=MAROON, outline=MAROON_DARK, width=3)
        d.text((x + card_w // 2 - ttw / 2, tag_y + 12),
               tag.upper(), fill=CREAM, font=tagf)

        # Sub caption (wrapped)
        sf = font("sans", 26)
        sub_lines = wrap(d, sub, sf, card_w - 60)
        sy = y0 + 270
        for line in sub_lines:
            ltw = d.textlength(line, font=sf)
            d.text((x + card_w // 2 - ltw / 2, sy), line,
                   fill=INK, font=sf)
            sy += 36

        # Connector hint
        cf = font("serif_ital", 24)
        cap = "→ biotechnology"
        cw = d.textlength(cap, font=cf)
        d.text((x + card_w // 2 - cw / 2, y0 + card_h - 60), cap,
               fill=ACCENT, font=cf)

    # Bottom punchline strip
    d.rounded_rectangle([110, 800, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Same toolkit — restriction enzymes, PCR, sequencing, CRISPR — behind every one of these.",
             font("serif_bold", 32), 832, MAROON_DARK)
    centered(d, "Today: what each tool actually does.",
             font("sans", 30), 882, MUTED)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "The toolkit — restriction enzymes, gel electrophoresis, PCR, sequencing, CRISPR.",
    "How each tool actually works at the molecular level.",
    "The applications: medicine, agriculture, forensics, diagnostics — and the ethics.",
], footnote="By the end: you can explain how a COVID PCR test detects one viral molecule.")


# 04 — restriction enzymes + ligase: EcoRI cut diagram with sticky ends
def restriction_enzymes_ligase(img, d):
    d.text((110, 70), "Restriction enzymes  +  ligase  +  plasmids.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 160),
           "EcoRI recognizes GAATTC. Cuts on a stagger → sticky ends.",
           fill=MUTED, font=font("sans", 30))

    # Top: DNA sequence with arrows showing EcoRI cut sites
    seq_top = "5'  ...G A A T T C...  3'"
    seq_bot = "3'  ...C T T A A G...  5'"
    mf = font("mono", 56)
    sy = 240
    centered(d, seq_top, mf, sy, INK)
    centered(d, seq_bot, mf, sy + 80, INK)
    # Arrows showing cuts (top: between G and A; bottom: between G and A)
    arrow_f = font("serif_bold", 40)
    # We approximate cut positions visually below.
    # Indicator labels
    d.text((W // 2 - 240, sy - 60), "cut →", fill=MAROON_DARK,
           font=font("sans_bold", 30))
    d.text((W // 2 + 110, sy + 150), "← cut", fill=MAROON_DARK,
           font=font("sans_bold", 30))

    # Middle: the result — two fragments with sticky overhangs
    y_mid = 460
    centered(d, "After the cut — sticky ends:",
             font("serif_bold", 38), y_mid, MAROON)

    # Two fragment boxes
    # Left fragment
    lx, ly_box, lw, lh = 200, 540, 720, 200
    d.rounded_rectangle([lx, ly_box, lx + lw, ly_box + lh], radius=14,
                        outline=ACCENT, width=4, fill=CARD)
    d.text((lx + 30, ly_box + 30), "5'  ...G",
           fill=INK, font=font("mono", 44))
    d.text((lx + 30, ly_box + 100), "3'  ...C T T A A",
           fill=INK, font=font("mono", 44))
    d.text((lx + lw - 320, ly_box + 165), "overhang: AATT",
           fill=ACCENT, font=font("sans_bold", 24))

    # Right fragment
    rx = W - 200 - lw
    d.rounded_rectangle([rx, ly_box, rx + lw, ly_box + lh], radius=14,
                        outline=ACCENT, width=4, fill=CARD)
    d.text((rx + 30, ly_box + 30), "A A T T C...  3'",
           fill=INK, font=font("mono", 44))
    d.text((rx + 30, ly_box + 100), "G...  5'",
           fill=INK, font=font("mono", 44))
    d.text((rx + 30, ly_box + 165), "overhang: AATT",
           fill=ACCENT, font=font("sans_bold", 24))

    # Plasmid + ligase mini-diagram on the right side bottom
    p_cx, p_cy = W // 2, 880
    d.text((110, 790), "Then:  ligase joins fragments  +  plasmid carries the insert into bacteria.",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # Plasmid icon
    d.ellipse([p_cx - 70, p_cy - 60, p_cx + 70, p_cy + 60],
              outline=MAROON, width=6)
    d.ellipse([p_cx - 40, p_cy - 30, p_cx + 40, p_cy + 30],
              outline=MAROON, width=6)
    d.text((p_cx - 50, p_cy + 70), "plasmid",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # Antibiotic-resistance tag
    d.text((p_cx + 100, p_cy - 12),
           "→ AmpR gene = selection marker",
           fill=ACCENT, font=font("sans_bold", 26))
deck.custom("04_restriction_enzymes_ligase", restriction_enzymes_ligase)


# 05 — gel electrophoresis: charge + gel ladder
def gel_electrophoresis(img, d):
    d.text((110, 70), "Gel electrophoresis  —  separating by size.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 160),
           "DNA is negatively charged → migrates toward + electrode. Smaller fragments = faster.",
           fill=MUTED, font=font("sans", 28))

    # Left: gel diagram
    gx, gy = 200, 260
    gw, gh = 800, 680
    # Gel slab
    d.rounded_rectangle([gx, gy, gx + gw, gy + gh], radius=18,
                        outline=MAROON_DARK, width=5, fill=ACCENT_LT)
    # Electrodes
    d.rectangle([gx - 60, gy + 40, gx - 20, gy + gh - 40],
                fill=INK, outline=MAROON_DARK, width=3)
    d.text((gx - 60, gy - 30), "−", fill=INK, font=font("serif_bold", 56))
    d.rectangle([gx + gw + 20, gy + 40, gx + gw + 60, gy + gh - 40],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((gx + gw + 30, gy - 30), "+", fill=MAROON, font=font("serif_bold", 56))

    # Wells at top
    well_w = 80
    well_count = 5
    well_gap = 60
    total_w = well_count * well_w + (well_count - 1) * well_gap
    start_w = gx + (gw - total_w) // 2
    for i in range(well_count):
        wx = start_w + i * (well_w + well_gap)
        d.rectangle([wx, gy + 20, wx + well_w, gy + 70],
                    fill=CARD, outline=MAROON_DARK, width=3)

    # Bands — smaller fragments travel further (further right toward +)
    # Each lane = sample with bands at different positions
    # For a ladder (lane 0), show many bands
    ladder_positions = [110, 180, 270, 380, 510, 600]  # px from top of gel
    for i in range(well_count):
        wx = start_w + i * (well_w + well_gap)
        cx_band = wx + well_w // 2
        if i == 0:
            # Ladder lane — bands at all positions
            for bp in ladder_positions:
                d.rectangle([cx_band - 38, gy + bp,
                             cx_band + 38, gy + bp + 14],
                            fill=MAROON_DARK)
        elif i == 1:
            # One big band high (large fragment)
            d.rectangle([cx_band - 38, gy + 130,
                         cx_band + 38, gy + 148],
                        fill=ACCENT)
        elif i == 2:
            # Two bands, medium
            d.rectangle([cx_band - 38, gy + 180,
                         cx_band + 38, gy + 198],
                        fill=ACCENT)
            d.rectangle([cx_band - 38, gy + 380,
                         cx_band + 38, gy + 398],
                        fill=ACCENT)
        elif i == 3:
            # Small fragment — far down
            d.rectangle([cx_band - 38, gy + 510,
                         cx_band + 38, gy + 528],
                        fill=ACCENT)
        elif i == 4:
            # Empty / control
            pass

    # Labels for lanes
    label_lanes = ["ladder", "large", "two", "small", "ctrl"]
    for i, lbl in enumerate(label_lanes):
        wx = start_w + i * (well_w + well_gap)
        cx_band = wx + well_w // 2
        lf = font("sans_bold", 22)
        tw = d.textlength(lbl, font=lf)
        d.text((cx_band - tw / 2, gy + gh - 30), lbl,
               fill=MAROON_DARK, font=lf)

    # Size labels next to ladder
    size_labels = ["10 kb", "5 kb", "2 kb", "1 kb", "500 bp", "200 bp"]
    for bp, lbl in zip(ladder_positions, size_labels):
        d.text((gx + 20, gy + bp - 6), lbl, fill=MUTED,
               font=font("sans_bold", 22))

    # Right: explainer card
    rx, ry = 1080, 260
    rw, rh = 740, 680
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((rx + 30, ry + 24), "Why it works",
           fill=ACCENT, font=font("serif_bold", 44))
    d.text((rx + 30, ry + 120),
           "DNA backbone has",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ry + 155),
           "phosphate groups → ",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ry + 190),
           "negatively charged.",
           fill=INK, font=font("sans", 28))

    d.text((rx + 30, ry + 260),
           "Apply current →",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((rx + 30, ry + 300),
           "DNA moves to + pole.",
           fill=INK, font=font("sans", 28))

    d.text((rx + 30, ry + 380),
           "Agarose gel = mesh.",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((rx + 30, ry + 420),
           "Small fragments slip",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ry + 455),
           "through easily.",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ry + 495),
           "Large fragments lag.",
           fill=INK, font=font("sans", 28))

    d.text((rx + 30, ry + 580),
           "Result: bands sorted",
           fill=ACCENT, font=font("serif_bold", 30))
    d.text((rx + 30, ry + 620),
           "by SIZE.",
           fill=ACCENT, font=font("serif_bold", 30))

    # Bottom strip
    d.rounded_rectangle([110, 960, W - 110, 1030], radius=14,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Check restriction digests · check PCR products · prep DNA fingerprinting.",
             font("sans_bold", 26), 980, MAROON_DARK)
deck.custom("05_gel_electrophoresis", gel_electrophoresis)


# 06 — PCR steps: 3 temperatures on a thermal cycler diagram
def pcr_steps(img, d):
    d.text((110, 70), "PCR  —  three temperatures, one cycle.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 160),
           "Kary Mullis, 1985.  Nobel 1993.  Taq polymerase from Thermus aquaticus.",
           fill=MUTED, font=font("sans", 28))

    # Three step cards
    steps = [
        ("1. DENATURE", "~95 °C", "DNA strands separate.",
         "Hydrogen bonds break.", ACCENT_LT),
        ("2. ANNEAL", "~55 °C", "Primers bind template.",
         "Short DNA tags find their match.", ACCENT),
        ("3. EXTEND", "~72 °C", "Taq builds new strand.",
         "Heat-stable polymerase from\nThermus aquaticus.", ACCENT_LT),
    ]
    card_w = 540
    card_h = 540
    gap = 40
    start_x = (W - (card_w * 3 + gap * 2)) // 2
    y0 = 240
    for i, (label, temp, line1, line2, col) in enumerate(steps):
        x = start_x + i * (card_w + gap)
        d.rounded_rectangle([x, y0, x + card_w, y0 + card_h], radius=22,
                            outline=MAROON_DARK, width=5, fill=col)
        # Title strip
        d.rectangle([x, y0, x + card_w, y0 + 80], fill=MAROON)
        lf = font("serif_bold", 40)
        tw = d.textlength(label, font=lf)
        d.text((x + card_w // 2 - tw / 2, y0 + 20), label,
               fill=CREAM, font=lf)

        # Big temperature
        tf = font("serif_bold", 100)
        tw_t = d.textlength(temp, font=tf)
        d.text((x + card_w // 2 - tw_t / 2, y0 + 110), temp,
               fill=MAROON_DARK, font=tf)

        # Lines
        body_y = y0 + 260
        bf = font("sans_bold", 30)
        lw_t = d.textlength(line1, font=bf)
        d.text((x + card_w // 2 - lw_t / 2, body_y), line1,
               fill=INK, font=bf)

        # line2 may be multi-line
        sf = font("sans", 26)
        l2_lines = line2.split("\n")
        sy = body_y + 60
        for ln in l2_lines:
            lw_t = d.textlength(ln, font=sf)
            d.text((x + card_w // 2 - lw_t / 2, sy), ln,
                   fill=MUTED, font=sf)
            sy += 38

        # Arrow to next
        if i < 2:
            ax = x + card_w + 4
            ay = y0 + card_h // 2
            d.polygon([
                (ax, ay - 22),
                (ax + 32, ay),
                (ax, ay + 22),
            ], fill=MAROON)

    # Bottom strip — the key insight
    d.rounded_rectangle([110, 830, W - 110, 990], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "WHY Taq?  Regular polymerase would denature at 95 °C — the whole reaction would die in cycle 1.",
             font("serif_bold", 28), 855, MAROON_DARK)
    centered(d, "Taq came from a bacterium in Yellowstone's hot springs — that is why PCR exists.",
             font("serif_ital", 28), 905, MAROON)
    centered(d, "One thermal cycler runs 30 cycles in ~2 hours.",
             font("sans_bold", 26), 950, MAROON_DARK)
deck.custom("06_pcr_steps", pcr_steps)


# 07 — PCR amplification: doubling curve + cycle table
def pcr_amplification(img, d):
    d.text((110, 70), "Each cycle doubles.  30 cycles → ~1 billion.",
           fill=MAROON, font=font("serif_bold", 56))

    # Left: doubling chart
    lx, ly = 110, 200
    lw, lh = 1080, 780
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 24), "Copies after each cycle (log scale)",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # Axes
    gx0 = lx + 100
    gy0 = ly + 700
    gx1 = lx + lw - 50
    gy1 = ly + 100
    d.line([(gx0, gy1), (gx0, gy0)], fill=MAROON_DARK, width=4)
    d.line([(gx0, gy0), (gx1, gy0)], fill=MAROON_DARK, width=4)
    d.text((lx + 20, ly + 80), "copies", fill=MAROON_DARK,
           font=font("sans_bold", 22))
    d.text((gx1 - 80, gy0 + 14), "cycles →", fill=MAROON_DARK,
           font=font("sans_bold", 22))

    # X-axis: 30 cycles in 6 ticks (0, 5, 10, 15, 20, 25, 30)
    n_cycles = 30
    x_ticks = [0, 5, 10, 15, 20, 25, 30]
    span_x = gx1 - gx0
    for c in x_ticks:
        px = gx0 + int(c / n_cycles * span_x)
        d.line([(px, gy0), (px, gy0 + 12)], fill=MAROON_DARK, width=3)
        lab = str(c)
        tf = font("sans_bold", 22)
        tw = d.textlength(lab, font=tf)
        d.text((px - tw / 2, gy0 + 20), lab,
               fill=MAROON_DARK, font=tf)

    # Y-axis: log labels 1, 10, 100, ..., 10^9
    y_labels = ["1", "10", "10²", "10⁴", "10⁶", "10⁸", "10⁹"]
    y_vals = [0, 1, 2, 4, 6, 8, 9]  # log10 values
    max_log = 9.0
    span_y = gy0 - gy1
    for lab, v in zip(y_labels, y_vals):
        py = gy0 - int(v / max_log * span_y)
        d.line([(gx0 - 10, py), (gx0, py)], fill=MAROON_DARK, width=3)
        tf = font("sans_bold", 22)
        tw = d.textlength(lab, font=tf)
        d.text((gx0 - 20 - tw, py - 14), lab,
               fill=MAROON_DARK, font=tf)

    # Plot 2^n for n=0..30
    prev = None
    for c in range(n_cycles + 1):
        copies_log = c * math.log10(2)  # log10(2^c)
        px = gx0 + int(c / n_cycles * span_x)
        py = gy0 - int(copies_log / max_log * span_y)
        if prev is not None:
            d.line([prev, (px, py)], fill=ACCENT, width=5)
        # Dot
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=MAROON)
        prev = (px, py)

    # Annotations
    # Cycle 10 marker
    c = 10
    px = gx0 + int(c / n_cycles * span_x)
    py = gy0 - int((c * math.log10(2)) / max_log * span_y)
    d.text((px + 12, py - 40), "10 cycles → 1,024 copies",
           fill=MAROON_DARK, font=font("sans_bold", 22))

    # Cycle 20 marker
    c = 20
    px = gx0 + int(c / n_cycles * span_x)
    py = gy0 - int((c * math.log10(2)) / max_log * span_y)
    d.text((px + 12, py - 40), "20 cycles → ~1 million",
           fill=MAROON_DARK, font=font("sans_bold", 22))

    # Cycle 30 marker
    c = 30
    px = gx0 + int(c / n_cycles * span_x)
    py = gy0 - int((c * math.log10(2)) / max_log * span_y)
    d.text((px - 280, py - 60), "30 cycles → ~10⁹ copies",
           fill=MAROON, font=font("serif_bold", 28))

    # Right: equation
    rx = lx + lw + 30
    rw = W - 110 - rx
    rh = 780
    d.rounded_rectangle([rx, ly, rx + rw, ly + rh], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((rx + 30, ly + 30), "FORMULA",
           fill=MAROON_DARK, font=font("serif_bold", 44))
    d.text((rx + 30, ly + 110),
           "copies = 2ⁿ",
           fill=MAROON_DARK, font=font("mono", 52))
    d.text((rx + 30, ly + 180),
           "n = # of cycles",
           fill=INK, font=font("sans", 26))
    # Examples
    rows = [
        ("n=10", "≈ 1,024"),
        ("n=20", "≈ 1,048,576"),
        ("n=30", "≈ 1.07 × 10⁹"),
    ]
    ey = ly + 260
    for left, right in rows:
        d.text((rx + 30, ey), left, fill=ACCENT,
               font=font("sans_bold", 32))
        d.text((rx + 30, ey + 40), right, fill=MAROON_DARK,
               font=font("mono", 30))
        ey += 110

    d.text((rx + 30, ly + 610),
           "Detect 1 virus →",
           fill=INK, font=font("sans_bold", 28))
    d.text((rx + 30, ly + 650),
           "10⁹ copies in 2 hrs.",
           fill=MAROON, font=font("serif_bold", 30))
    d.text((rx + 30, ly + 710),
           "→ visible band on gel.",
           fill=MUTED, font=font("serif_ital", 24))
deck.custom("07_pcr_amplification", pcr_amplification)


# 08 — sequencing: Sanger ddNTP cards + NGS parallel diagram
def sequencing(img, d):
    d.text((110, 70), "DNA sequencing  —  reading the actual bases.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 160),
           "Sanger (classic) → NGS (modern parallel).",
           fill=MUTED, font=font("sans", 30))

    # Left: Sanger
    lx, ly = 110, 240
    lw, lh = 870, 720
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 24), "SANGER SEQUENCING",
           fill=ACCENT, font=font("sans_bold", 40))
    d.text((lx + 30, ly + 90),
           "Frederick Sanger, 1977  ·  Nobel 1980.",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # ddNTP explanation
    d.text((lx + 30, ly + 160),
           "Key trick:  ddNTPs",
           fill=MAROON_DARK, font=font("serif_bold", 38))
    d.text((lx + 30, ly + 220),
           "Dideoxynucleotides lack",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 255),
           "the 3'-OH group →",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 290),
           "polymerase CANNOT add",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 325),
           "the next nucleotide.",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 375),
           "Chain TERMINATES.",
           fill=MAROON, font=font("serif_bold", 32))

    # Mini ladder visual
    ladder_x = lx + 480
    ladder_y = ly + 160
    d.text((ladder_x, ladder_y - 5), "Fragments of every length:",
           fill=MAROON_DARK, font=font("sans_bold", 22))
    bases = ["A", "T", "G", "C", "A", "G", "T"]
    for i, b in enumerate(bases):
        # Each fragment gets longer
        bar_y = ladder_y + 50 + i * 38
        d.rectangle([ladder_x, bar_y, ladder_x + 80 + i * 25, bar_y + 22],
                    fill=ACCENT_LT, outline=MAROON_DARK, width=2)
        d.text((ladder_x + 85 + i * 25, bar_y - 4), b,
               fill=MAROON, font=font("mono", 26))
    d.text((ladder_x, ladder_y + 380),
           "Read bottom to top →",
           fill=MAROON_DARK, font=font("sans_bold", 22))
    d.text((ladder_x, ladder_y + 415),
           "A T G C A G T",
           fill=MAROON, font=font("mono", 30))

    # Right: NGS
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 24), "NEXT-GEN SEQUENCING",
           fill=MAROON_DARK, font=font("sans_bold", 40))
    d.text((rx + 30, ly + 90),
           "MASSIVELY PARALLEL.",
           fill=MAROON, font=font("serif_bold", 32))
    d.text((rx + 30, ly + 150),
           "Millions of fragments",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 185),
           "read at the same time.",
           fill=INK, font=font("sans", 28))

    # Grid of mini reads
    grid_x = rx + 30
    grid_y = ly + 270
    cols = 6
    rows = 8
    cw_grid = 100
    ch_grid = 14
    gap_g = 6
    for r in range(rows):
        for c in range(cols):
            px = grid_x + c * (cw_grid + gap_g)
            py = grid_y + r * (ch_grid + gap_g)
            col_choice = ACCENT if (r + c) % 2 == 0 else ACCENT_LT
            d.rectangle([px, py, px + cw_grid, py + ch_grid],
                        fill=col_choice)
    d.text((rx + 30, grid_y + rows * (ch_grid + gap_g) + 20),
           "Cost: $3B (2003) → < $1,000 today.",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 30, grid_y + rows * (ch_grid + gap_g) + 60),
           "Used for: whole-genome,",
           fill=INK, font=font("sans", 24))
    d.text((rx + 30, grid_y + rows * (ch_grid + gap_g) + 90),
           "cancer panels, COVID variants.",
           fill=INK, font=font("sans", 24))

    # Bottom strip
    d.rounded_rectangle([110, 990, W - 110, 1050], radius=14,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Sanger: read ONE region accurately.   NGS: read EVERYTHING at once.",
             font("sans_bold", 26), 1006, MAROON_DARK)
deck.custom("08_sequencing", sequencing)


# 09 — CRISPR-Cas9 mechanism: gRNA + Cas9 → cut → repair
def crispr_cas9(img, d):
    d.text((110, 70), "CRISPR-Cas9  —  programmable scissors.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 160),
           "Doudna + Charpentier  ·  Nobel Chemistry 2020.",
           fill=MUTED, font=font("sans", 30))

    # Stage 1: gRNA + Cas9 finding target
    s1x = 110
    s1y = 250
    s1w = 580
    s1h = 700
    d.rounded_rectangle([s1x, s1y, s1x + s1w, s1y + s1h], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((s1x + 20, s1y + 20), "1.  Target",
           fill=ACCENT, font=font("serif_bold", 42))

    # Cas9 = big blob
    cx, cy = s1x + s1w // 2, s1y + 280
    d.ellipse([cx - 130, cy - 100, cx + 130, cy + 100],
              fill=ACCENT_LT, outline=MAROON_DARK, width=5)
    d.text((cx - 40, cy - 20), "Cas9",
           fill=MAROON_DARK, font=font("serif_bold", 40))

    # gRNA hanging from Cas9
    d.line([(cx, cy + 100), (cx, cy + 200)], fill=MAROON, width=8)
    d.text((cx + 20, cy + 130), "gRNA",
           fill=MAROON, font=font("sans_bold", 28))

    # Target DNA below
    dna_y = cy + 240
    d.rectangle([s1x + 40, dna_y, s1x + s1w - 40, dna_y + 20],
                fill=INK)
    d.rectangle([s1x + 40, dna_y + 40, s1x + s1w - 40, dna_y + 60],
                fill=INK)
    d.text((s1x + 20, dna_y + 90), "target DNA",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    d.text((s1x + 20, s1y + s1h - 60),
           "gRNA finds matching sequence.",
           fill=MUTED, font=font("serif_ital", 24))

    # Stage 2: cut
    s2x = s1x + s1w + 20
    s2y = s1y
    s2w = 580
    s2h = 700
    d.rounded_rectangle([s2x, s2y, s2x + s2w, s2y + s2h], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((s2x + 20, s2y + 20), "2.  Cut",
           fill=ACCENT, font=font("serif_bold", 42))

    # DNA cut diagram
    dna_y2 = s2y + 350
    d.rectangle([s2x + 40, dna_y2, s2x + s2w // 2 - 30, dna_y2 + 20],
                fill=INK)
    d.rectangle([s2x + s2w // 2 + 30, dna_y2, s2x + s2w - 40, dna_y2 + 20],
                fill=INK)
    d.rectangle([s2x + 40, dna_y2 + 40, s2x + s2w // 2 - 30, dna_y2 + 60],
                fill=INK)
    d.rectangle([s2x + s2w // 2 + 30, dna_y2 + 40, s2x + s2w - 40, dna_y2 + 60],
                fill=INK)
    # Scissors-like
    d.line([(s2x + s2w // 2 - 50, dna_y2 - 40),
            (s2x + s2w // 2 + 50, dna_y2 + 100)],
           fill=MAROON, width=8)
    d.line([(s2x + s2w // 2 + 50, dna_y2 - 40),
            (s2x + s2w // 2 - 50, dna_y2 + 100)],
           fill=MAROON, width=8)
    d.text((s2x + 20, dna_y2 + 100),
           "DOUBLE-STRAND BREAK",
           fill=MAROON, font=font("serif_bold", 30))

    d.text((s2x + 20, s2y + s2h - 60),
           "Cas9 cuts both strands.",
           fill=MUTED, font=font("serif_ital", 24))

    # Stage 3: repair
    s3x = s2x + s2w + 20
    s3y = s1y
    s3w = W - 110 - s3x
    s3h = 700
    d.rounded_rectangle([s3x, s3y, s3x + s3w, s3y + s3h], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((s3x + 20, s3y + 20), "3.  Repair",
           fill=MAROON_DARK, font=font("serif_bold", 42))

    # Two pathways
    d.text((s3x + 20, s3y + 130),
           "Cell repairs the cut:",
           fill=INK, font=font("sans_bold", 26))

    # Path A: knockout
    d.rounded_rectangle([s3x + 20, s3y + 200, s3x + s3w - 20, s3y + 380],
                        radius=14, fill=CARD, outline=ACCENT, width=4)
    d.text((s3x + 40, s3y + 220), "A. Knock OUT",
           fill=ACCENT, font=font("serif_bold", 30))
    d.text((s3x + 40, s3y + 270),
           "NHEJ — sloppy join.",
           fill=INK, font=font("sans", 24))
    d.text((s3x + 40, s3y + 305),
           "Indels → gene broken.",
           fill=INK, font=font("sans", 24))

    # Path B: insert
    d.rounded_rectangle([s3x + 20, s3y + 410, s3x + s3w - 20, s3y + 600],
                        radius=14, fill=CARD, outline=MAROON, width=4)
    d.text((s3x + 40, s3y + 430), "B. Knock IN",
           fill=MAROON, font=font("serif_bold", 30))
    d.text((s3x + 40, s3y + 480),
           "HDR + template →",
           fill=INK, font=font("sans", 24))
    d.text((s3x + 40, s3y + 515),
           "paste a new sequence.",
           fill=INK, font=font("sans", 24))
    d.text((s3x + 40, s3y + 552),
           "Correct disease genes.",
           fill=MAROON_DARK, font=font("sans_bold", 22))

    # Bottom strip
    d.rounded_rectangle([110, 980, W - 110, 1050], radius=14,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Cas9 makes the cut — the CELL does the repair. CRISPR is the scissors, not the result.",
             font("sans_bold", 26), 998, MAROON_DARK)
deck.custom("09_crispr_cas9", crispr_cas9)


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Start with 1 DNA molecule. Each PCR cycle perfectly doubles. After 10 cycles, how many copies?",
           "copies  =  2ⁿ",
           hint="Pause now. Solve it. Press play when you're ready.")

# 11 — duplicate for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — applications: medicine + agriculture
def applications_medicine_ag(img, d):
    d.text((110, 70), "Applications  —  medicine  +  agriculture.",
           fill=MAROON, font=font("serif_bold", 56))

    # Left: Medicine
    lx, ly = 110, 200
    lw, lh = 870, 780
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 24), "MEDICINE",
           fill=ACCENT, font=font("sans_bold", 44))

    med_items = [
        ("RECOMBINANT INSULIN", "1982",
         "First FDA-approved biotech drug.",
         "Human insulin gene spliced",
         "into E. coli using a plasmid."),
        ("GENE THERAPY", "1990s →",
         "Cures some forms of SCID",
         "(bubble-boy disease) by inserting",
         "a working copy of the gene."),
        ("CRISPR TRIALS", "2023 →",
         "Sickle-cell + beta-thalassemia",
         "treated by editing patients'",
         "own blood stem cells."),
    ]
    y = ly + 90
    for name, date, l1, l2, l3 in med_items:
        # Header row
        d.text((lx + 30, y), name, fill=MAROON_DARK,
               font=font("sans_bold", 28))
        df = font("serif_ital", 24)
        dw = d.textlength(date, font=df)
        d.text((lx + lw - 30 - dw, y + 2), date,
               fill=ACCENT, font=df)
        # Body
        d.text((lx + 30, y + 50), l1, fill=INK, font=font("sans", 24))
        d.text((lx + 30, y + 85), l2, fill=INK, font=font("sans", 24))
        d.text((lx + 30, y + 120), l3, fill=INK, font=font("sans", 24))
        y += 230

    # Right: Agriculture
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 24), "AGRICULTURE",
           fill=MAROON_DARK, font=font("sans_bold", 44))

    ag_items = [
        ("Bt CORN", "Bacillus thuringiensis gene",
         "→ corn makes its own",
         "insecticidal protein.",
         "Kills caterpillars; safe for"),
        ("ROUNDUP-READY", "Soybeans engineered to",
         "tolerate glyphosate herbicide.",
         "Farmers spray crops without",
         "killing them."),
        ("GOLDEN RICE", "Rice engineered to make",
         "beta-carotene (vitamin A).",
         "Designed to combat",
         "vitamin-A blindness."),
    ]
    y = ly + 90
    for name, l1, l2, l3, l4 in ag_items:
        d.text((rx + 30, y), name, fill=MAROON_DARK,
               font=font("sans_bold", 28))
        d.text((rx + 30, y + 50), l1, fill=INK, font=font("sans", 24))
        d.text((rx + 30, y + 85), l2, fill=INK, font=font("sans", 24))
        d.text((rx + 30, y + 120), l3, fill=INK, font=font("sans", 24))
        d.text((rx + 30, y + 155), l4, fill=INK, font=font("sans", 24))
        y += 230

    # Bottom ethics strip
    d.rounded_rectangle([110, 1000, W - 110, 1060], radius=14,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Ethics:  germline editing  ·  GMO patents  ·  ecological risk  ·  genetic privacy.",
             font("sans_bold", 24), 1018, MAROON_DARK)
deck.custom("12_applications_medicine_ag", applications_medicine_ag)


# 13 — applications: forensics + diagnostics
def applications_forensics_diagnostics(img, d):
    d.text((110, 70), "Forensics  +  diagnostics.",
           fill=MAROON, font=font("serif_bold", 56))

    # Left: Forensics — DNA fingerprint
    lx, ly = 110, 200
    lw, lh = 870, 780
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 24), "FORENSICS",
           fill=ACCENT, font=font("sans_bold", 44))
    d.text((lx + 30, ly + 90),
           "DNA fingerprinting",
           fill=MAROON_DARK, font=font("serif_bold", 36))

    d.text((lx + 30, ly + 160),
           "STR markers — short tandem",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 195),
           "repeats. Each person has",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 230),
           "a unique pattern of repeats.",
           fill=INK, font=font("sans", 26))

    # Mini fingerprint bands
    fy = ly + 310
    d.text((lx + 30, fy), "Crime scene vs. suspects:",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    cols_labels = ["scene", "S1", "S2", "S3"]
    col_w_lane = 110
    gap_lane = 30
    start_lane = lx + 80
    lane_y0 = fy + 50
    lane_h = 340
    # Reference profile (scene) bands at specific positions
    scene_bands = [40, 110, 200, 280]
    # Suspect band patterns — match S2
    profiles = [
        scene_bands,                  # scene
        [60, 130, 220, 300],          # S1 - different
        scene_bands,                  # S2 - MATCH
        [50, 140, 230, 290],          # S3 - different
    ]
    for i, (lbl, bands) in enumerate(zip(cols_labels, profiles)):
        lx_lane = start_lane + i * (col_w_lane + gap_lane)
        # Lane background
        d.rectangle([lx_lane, lane_y0, lx_lane + col_w_lane,
                     lane_y0 + lane_h], fill=ACCENT_LT,
                    outline=MAROON_DARK, width=3)
        # Highlight matching column (S2)
        col = MAROON if i == 2 else INK
        for b in bands:
            d.rectangle([lx_lane + 8, lane_y0 + b,
                         lx_lane + col_w_lane - 8, lane_y0 + b + 16],
                        fill=col)
        # Label
        lf = font("sans_bold", 24)
        tw = d.textlength(lbl, font=lf)
        d.text((lx_lane + col_w_lane // 2 - tw / 2, lane_y0 + lane_h + 10),
               lbl, fill=MAROON_DARK if i == 2 else INK, font=lf)
    d.text((lx + 30, ly + lh - 60), "CODIS database — FBI matches profiles nationwide.",
           fill=MAROON_DARK, font=font("sans_bold", 22))

    # Right: Diagnostics
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 24), "DIAGNOSTICS",
           fill=MAROON_DARK, font=font("sans_bold", 44))
    d.text((rx + 30, ly + 90),
           "PCR-based tests",
           fill=MAROON_DARK, font=font("serif_bold", 36))

    diags = [
        ("HIV", "PCR detects viral RNA",
         "directly — earlier than",
         "antibody tests."),
        ("COVID-19", "Nasal swab → RT-PCR",
         "amplifies viral RNA.",
         "Threshold cycle = viral load."),
        ("PRENATAL", "Cell-free fetal DNA in",
         "maternal blood. Detects",
         "Down syndrome (trisomy 21)."),
    ]
    y = ly + 160
    for name, l1, l2, l3 in diags:
        d.text((rx + 30, y), name, fill=ACCENT,
               font=font("serif_bold", 32))
        d.text((rx + 30, y + 45), l1, fill=INK, font=font("sans", 24))
        d.text((rx + 30, y + 80), l2, fill=INK, font=font("sans", 24))
        d.text((rx + 30, y + 115), l3, fill=INK, font=font("sans", 24))
        y += 195

    d.text((rx + 30, ly + lh - 60),
           "Same toolkit, different question.",
           fill=MAROON_DARK, font=font("serif_ital", 24))

    # Bottom strip
    d.rounded_rectangle([110, 1000, W - 110, 1060], radius=14,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Forensics asks WHO.  Diagnostics asks WHAT.  Both lean hard on PCR.",
             font("sans_bold", 26), 1016, MAROON_DARK)
deck.custom("13_applications_forensics_diagnostics", applications_forensics_diagnostics)


# 14 — compare traps: PCR vs sequencing (and other confusions)
deck.compare("14_compare_traps",
             "Common traps  —  what students mix up.",
             left={"label": "PCR",
                   "color": ACCENT,
                   "lines": [
                       "AMPLIFIES a known region.",
                       "",
                       "Needs primers you DESIGN",
                       "for a known target.",
                       "",
                       "Output: lots of copies",
                       "of ONE sequence.",
                       "",
                       "Used in: diagnostics,",
                       "forensics, cloning prep.",
                   ],
                   "footnote": "If 'how MUCH is there' → PCR."},
             right={"label": "SEQUENCING",
                    "color": MAROON,
                    "lines": [
                        "READS the order of bases.",
                        "",
                        "Doesn't require you to",
                        "know the sequence first.",
                        "",
                        "Output: the actual",
                        "letters of the DNA.",
                        "",
                        "Used in: genome projects,",
                        "cancer panels, variant ID.",
                    ],
                    "footnote": "If 'what IS the sequence' → sequencing."})


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Restriction enzymes cut at specific sites (EcoRI → GAATTC, sticky ends); ligase seals; plasmids carry inserts.",
    "Gel electrophoresis: DNA is negative → moves to +; smaller fragments travel farther.",
    "PCR: 95 °C denature, ~55 °C anneal, 72 °C extend with Taq. 30 cycles → ~10⁹ copies.",
    "Sanger sequencing uses ddNTPs (terminate chain). NGS reads millions of fragments in parallel.",
    "CRISPR-Cas9: gRNA targets Cas9 to make a double-strand cut; cell repair knocks out or inserts.",
    "Applications: insulin, gene therapy, sickle-cell CRISPR, Bt corn, Golden Rice, CODIS, COVID PCR.",
    "Ethics: germline editing, GMO patents, ecological risk, genetic privacy.",
], assignment=[
    "1.  Sketch a PCR cycle. Label the 3 temperatures and what happens at each step.",
    "2.  In 2-3 sentences, explain how a COVID-19 PCR test detects one viral RNA molecule.",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapter 17 — biotechnology tools and applications"),
    ("2.", "Khan Academy AP Bio",     "Unit 6 problem sets — biotech, PCR, gel, CRISPR"),
    ("3.", "Assignment in dashboard", "PCR cycle diagram + COVID test explanation (above)"),
    ("4.", "Advisor check-in",        "If PCR steps or CRISPR mechanism still feel fuzzy"),
], next_text="Next up:  Module 10 — Natural Selection  (Unit 7 begins).")


print("AP Biology Module 9 slides built.")

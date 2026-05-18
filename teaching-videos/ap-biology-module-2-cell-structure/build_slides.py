"""AP Biology · Module 2 — Cell Structure and Function.

Teal (science) theme auto-resolved by slide_kit from "AP Biology".
16 slides total. Customs for the organelle/diagram-heavy sections, the
SA:V math gets the equation slide, the pause is duplicated for the silence
reveal.
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
deck = Deck(course="AP Biology", module_num=2, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 2 — Cell Structure and Function",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook: 37 trillion cells, why are they tiny?
def hook(img, d):
    d.text((110, 80), "37 trillion cells.  All of them tiny.",
           fill=MAROON, font=font("serif_bold", 60))

    # Left panel — the number
    lx, ly, lw, lh = 140, 230, 760, 540
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    cap = "How many cells are in you?"
    cf = font("serif_bold", 38)
    tw = d.textlength(cap, font=cf)
    d.text((lx + lw // 2 - tw / 2, ly + 40), cap,
           fill=MAROON_DARK, font=cf)
    # Big number
    bignum = "~37,000,000,000,000"
    bf = font("serif_bold", 64)
    bw = d.textlength(bignum, font=bf)
    d.text((lx + lw // 2 - bw / 2, ly + 160), bignum,
           fill=ACCENT, font=bf)
    label = "thirty-seven trillion"
    lf = font("sans", 32)
    lw_t = d.textlength(label, font=lf)
    d.text((lx + lw // 2 - lw_t / 2, ly + 240), label,
           fill=MUTED, font=lf)
    # Small ovals representing cells
    import random
    rng = random.Random(2)
    for _ in range(60):
        cx = rng.randint(lx + 60, lx + lw - 60)
        cy = rng.randint(ly + 330, ly + lh - 60)
        r = rng.randint(8, 18)
        d.ellipse([cx - r, cy - r, cx + r, cy + r],
                  fill=ACCENT_LT, outline=ACCENT, width=2)

    # Right panel — scale: cells are 10-100 μm
    rx, ry, rw, rh = 1020, 230, 760, 540
    d.rounded_rectangle([rx, ry, rx + rw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    cap2 = "How big is each one?"
    tw3 = d.textlength(cap2, font=cf)
    d.text((rx + rw // 2 - tw3 / 2, ry + 40), cap2,
           fill=MAROON_DARK, font=cf)

    # Ruler / scale bar
    bar_left = rx + 80
    bar_right = rx + rw - 80
    bar_y = ry + 200
    d.line([(bar_left, bar_y), (bar_right, bar_y)],
           fill=MAROON_DARK, width=6)
    # Tick marks
    ticks = [("1 μm", 0.0), ("10 μm", 0.33), ("100 μm", 0.66), ("1 mm", 1.0)]
    for label, frac in ticks:
        tx = bar_left + int((bar_right - bar_left) * frac)
        d.line([(tx, bar_y - 14), (tx, bar_y + 14)],
               fill=MAROON_DARK, width=4)
        sf = font("sans_bold", 22)
        tw_l = d.textlength(label, font=sf)
        d.text((tx - tw_l / 2, bar_y + 26), label, fill=INK, font=sf)
    # Highlight the "typical cell" range
    h_left = bar_left + int((bar_right - bar_left) * 0.33)
    h_right = bar_left + int((bar_right - bar_left) * 0.66)
    d.rectangle([h_left, bar_y - 60, h_right, bar_y - 20], fill=ACCENT_LT)
    d.text((h_left + 10, bar_y - 55), "TYPICAL CELL", fill=MAROON_DARK,
           font=font("sans_bold", 22))
    # Caption underneath
    d.text((rx + 60, ry + 350),
           "Most cells:  10 – 100 micrometers.",
           fill=INK, font=font("sans_bold", 28))
    d.text((rx + 60, ry + 400),
           "Smaller than the width of a human hair.",
           fill=MUTED, font=font("sans", 24))
    d.text((rx + 60, ry + 460),
           "Evolution COULD make them bigger.",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 60, ry + 500),
           "It chose not to.  Why?",
           fill=ACCENT, font=font("sans_bold", 28))

    # Bottom punchline strip
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "It's a geometry problem.  By the end of this lesson, you'll know exactly why.",
             font("serif_bold", 36), 850, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Two kinds of cells:  prokaryotes vs. eukaryotes.",
    "A tour of the organelles  —  the cell's little factories.",
    "Two big ideas:  surface-area-to-volume, and endosymbiosis.",
], footnote="By the end: you can match every organelle to the job it does.")


# 04 — prok vs euk — custom side-by-side table
def prok_euk(img, d):
    d.text((110, 70), "Prokaryote  vs.  Eukaryote.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 155),
           "Same chemistry.  Very different architecture.",
           fill=MUTED, font=font("sans", 28))

    # 3-column table: feature | prokaryote | eukaryote
    headers = [("FEATURE", 140), ("PROKARYOTE", 760), ("EUKARYOTE", 1300)]
    header_y = 220
    d.rectangle([110, header_y, W - 110, header_y + 60], fill=ACCENT)
    for label, x in headers:
        d.text((x, header_y + 14), label, fill=CREAM,
               font=font("sans_bold", 28))

    rows = [
        ("Examples",            "Bacteria, Archaea",         "Protists, Plants, Fungi, Animals"),
        ("Typical size",        "0.5 – 5 μm",                "10 – 100 μm"),
        ("Membrane-bound nucleus", "No (nucleoid region)",   "Yes"),
        ("Membrane-bound organelles","No",                   "Yes"),
        ("DNA shape",           "Circular, 1 chromosome",    "Linear, multiple chromosomes"),
        ("Ribosomes",           "70S (smaller)",             "80S in cytoplasm"),
        ("Cell wall",           "Peptidoglycan / pseudo-",   "Cellulose (plants), chitin (fungi), none (animals)"),
    ]
    row_h = 78
    y = header_y + 60
    for i, (feat, p, e) in enumerate(rows):
        bg = CARD if i % 2 == 0 else ACCENT_LT
        d.rectangle([110, y, W - 110, y + row_h], fill=bg)
        d.text((140, y + 22), feat, fill=MAROON_DARK,
               font=font("sans_bold", 26))
        d.text((760, y + 22), p, fill=INK, font=font("sans", 24))
        d.text((1300, y + 22), e, fill=INK, font=font("sans", 22))
        y += row_h
    d.rectangle([110, header_y, W - 110, y], outline=MAROON, width=4)

    # Bottom strip
    d.rounded_rectangle([110, y + 30, W - 110, y + 130], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Eukaryotes are bigger  →  they had to compartmentalize.",
             font("sans_bold", 30), y + 60, MAROON_DARK)
deck.custom("04_prok_vs_euk", prok_euk)


# 05 — eukaryote organelles intro / compartmentalization
deck.definition("05_eukaryote_organelles_intro",
                "Compartmentalization.",
                "Each organelle = a room with its own job.",
                sub="Different conditions, different enzymes, different reactions — all inside one cell.")


# 06 — nucleus + ribosomes
def nucleus_ribosomes(img, d):
    d.text((110, 70), "Nucleus + Ribosomes  —  the control room and the builders.",
           fill=MAROON, font=font("serif_bold", 48))

    # Left: Nucleus diagram
    lx, ly, lw, lh = 110, 180, 870, 770
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=22,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "NUCLEUS", fill=ACCENT,
           font=font("sans_bold", 44))
    d.text((lx + 30, ly + 80),
           "Stores DNA  ·  control center.",
           fill=INK, font=font("sans", 28))

    # Big circle (outer membrane)
    cx, cy = lx + lw // 2, ly + 440
    outer_r = 200
    inner_r = outer_r - 20
    d.ellipse([cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r],
              fill=ACCENT_LT, outline=MAROON_DARK, width=5)
    d.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
              fill=CARD, outline=MAROON_DARK, width=4)
    # Nuclear pores
    for theta_deg in (10, 70, 130, 190, 250, 310):
        theta = math.radians(theta_deg)
        px = cx + int(outer_r * math.cos(theta))
        py = cy + int(outer_r * math.sin(theta))
        d.ellipse([px - 12, py - 12, px + 12, py + 12],
                  fill=CARD, outline=MAROON_DARK, width=3)
    # Nucleolus inside (smaller dense blob)
    nx, ny, nr = cx - 30, cy + 20, 60
    d.ellipse([nx - nr, ny - nr, nx + nr, ny + nr],
              fill=MAROON, outline=MAROON_DARK, width=3)
    nf = font("sans_bold", 22)
    nucl_label = "nucleolus"
    tw = d.textlength(nucl_label, font=nf)
    d.text((nx - tw / 2, ny - 12), nucl_label, fill=CREAM, font=nf)
    # Squiggle DNA strands
    for off in (-100, -40, 40, 100):
        sx = cx + off - 50
        sy = cy - 100
        for i in range(8):
            x1 = sx + i * 12
            y1 = sy + (10 if i % 2 == 0 else -10)
            x2 = sx + (i + 1) * 12
            y2 = sy + (-10 if i % 2 == 0 else 10)
            d.line([(x1, y1), (x2, y2)], fill=INK, width=2)

    # Labels
    d.text((lx + 30, ly + 200),
           "·  Double membrane (nuclear envelope)",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 240),
           "·  Nuclear pores → mRNA out, proteins in",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 280),
           "·  Nucleolus → makes rRNA + ribosome subunits",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # Right: Ribosomes
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=22,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "RIBOSOMES", fill=MAROON_DARK,
           font=font("sans_bold", 44))
    d.text((rx + 30, ly + 80),
           "One job:  build proteins.",
           fill=INK, font=font("sans", 28))

    # Two ribosome cartoons — free vs bound
    # FREE
    d.text((rx + 30, ly + 170), "FREE  (in cytosol)",
           fill=ACCENT, font=font("sans_bold", 32))
    d.text((rx + 30, ly + 215),
           "→ proteins that STAY in the cell",
           fill=INK, font=font("sans", 26))
    # Drawing: two stacked ovals
    f_cx, f_cy = rx + 120, ly + 340
    d.ellipse([f_cx - 60, f_cy - 30, f_cx + 60, f_cy + 15],
              fill=ACCENT, outline=MAROON_DARK, width=3)
    d.ellipse([f_cx - 55, f_cy - 5, f_cx + 55, f_cy + 50],
              fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((f_cx + 90, f_cy - 10), "80S in cytoplasm",
           fill=MUTED, font=font("sans", 24))

    # BOUND
    d.text((rx + 30, ly + 470), "BOUND  (to rough ER)",
           fill=MAROON, font=font("sans_bold", 32))
    d.text((rx + 30, ly + 515),
           "→ proteins for membrane, lysosome, or EXPORT",
           fill=INK, font=font("sans", 24))
    # Drawing: ER membrane with ribosomes on it
    er_left = rx + 30
    er_right = rx + rw - 30
    er_y1 = ly + 600
    er_y2 = ly + 640
    d.rectangle([er_left, er_y1, er_right, er_y2],
                fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    for ribx in range(er_left + 40, er_right - 30, 70):
        d.ellipse([ribx - 18, er_y1 - 28, ribx + 18, er_y1 - 4],
                  fill=ACCENT, outline=MAROON_DARK, width=2)
        d.ellipse([ribx - 16, er_y1 - 14, ribx + 16, er_y1 + 8],
                  fill=MAROON, outline=MAROON_DARK, width=2)
    d.text((rx + 30, ly + 670), "ribosomes studded on RER membrane",
           fill=MUTED, font=font("serif_ital", 24))
deck.custom("06_nucleus_ribosomes", nucleus_ribosomes)


# 07 — endomembrane system (flow)
def endomembrane(img, d):
    d.text((110, 70), "The endomembrane system  —  the assembly line.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 145),
           "Proteins are built, modified, packaged, and shipped.",
           fill=MUTED, font=font("sans", 28))

    # Horizontal flow: RER → Golgi → Vesicle → Membrane / Lysosome
    stages = [
        ("Rough ER",   "ribosomes synthesize\n& fold proteins"),
        ("Smooth ER",  "lipids · steroids\nCa²⁺ · detox"),
        ("Golgi",      "modify · sort\npackage"),
        ("Vesicles",   "transport\nto destinations"),
        ("Destination","membrane · lysosome\nor EXPORT (exocytosis)"),
    ]
    cols = len(stages)
    box_w = 320
    gap = 25
    total_w = box_w * cols + gap * (cols - 1)
    start_x = (W - total_w) // 2
    box_y = 240
    box_h = 280
    arrow_y = box_y + box_h // 2
    for i, (name, sub) in enumerate(stages):
        x = start_x + i * (box_w + gap)
        d.rounded_rectangle([x, box_y, x + box_w, box_y + box_h],
                            radius=22, outline=ACCENT, width=5,
                            fill=CARD)
        # Title
        nf = font("serif_bold", 36)
        tw = d.textlength(name, font=nf)
        d.text((x + box_w / 2 - tw / 2, box_y + 30), name,
               fill=MAROON_DARK, font=nf)
        # Sub lines
        sf = font("sans", 24)
        for j, line in enumerate(sub.split("\n")):
            lw = d.textlength(line, font=sf)
            d.text((x + box_w / 2 - lw / 2, box_y + 130 + j * 36),
                   line, fill=INK, font=sf)
        # Arrow to next
        if i < cols - 1:
            ax = x + box_w + 4
            ay = arrow_y
            d.polygon([
                (ax, ay - 14),
                (ax + gap - 6, ay),
                (ax, ay + 14),
            ], fill=ACCENT)

    # Bottom strip — lysosomes call-out
    d.rounded_rectangle([110, 600, W - 110, 770], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    d.text((150, 625), "Lysosomes  —  the cell's recycling center.",
           fill=MAROON_DARK, font=font("serif_bold", 36))
    d.text((150, 685),
           "Acidic (pH ~5)  ·  full of hydrolytic enzymes  ·  digest worn organelles + engulfed material",
           fill=INK, font=font("sans", 28))
    d.text((150, 725),
           "Found mainly in animal cells.  (Plants use the central vacuole for similar work.)",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # Footnote at very bottom
    d.text((110, 820),
           "Smooth ER specialties:  liver = drug detox.  Muscle = Ca²⁺ release.  Gonads = steroid hormones.",
           fill=MUTED, font=font("sans", 26))
    d.text((110, 870),
           "Golgi:  cis face RECEIVES from ER  →  trans face SHIPS out in vesicles.",
           fill=MUTED, font=font("sans", 26))
deck.custom("07_endomembrane", endomembrane)


# 08 — mitochondria + chloroplasts (energy organelles)
def energy_organelles(img, d):
    d.text((110, 70), "Energy organelles  —  mitochondria + chloroplasts.",
           fill=MAROON, font=font("serif_bold", 50))

    # Two equal panels
    lx, ly = 110, 180
    lw, lh = 870, 770
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=22,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "MITOCHONDRIA", fill=ACCENT,
           font=font("sans_bold", 42))
    d.text((lx + 30, ly + 80),
           "Cellular respiration  →  ATP",
           fill=INK, font=font("sans", 30))
    d.text((lx + 30, ly + 125),
           "Found in nearly all eukaryotic cells.",
           fill=INK, font=font("sans", 26))

    # Mitochondrion drawing
    mcx, mcy = lx + lw // 2, ly + 400
    mw, mh = 600, 280
    # Outer membrane (smooth oval)
    d.ellipse([mcx - mw // 2, mcy - mh // 2,
               mcx + mw // 2, mcy + mh // 2],
              fill=ACCENT_LT, outline=MAROON_DARK, width=5)
    # Inner membrane with cristae (wavy)
    inner_w = mw - 40
    inner_h = mh - 40
    d.ellipse([mcx - inner_w // 2, mcy - inner_h // 2,
               mcx + inner_w // 2, mcy + inner_h // 2],
              fill=ACCENT, outline=MAROON_DARK, width=4)
    # Cristae folds — draw arcs across inner
    for cx_off in (-180, -90, 0, 90, 180):
        d.ellipse([mcx + cx_off - 30, mcy - 80, mcx + cx_off + 30, mcy + 80],
                  outline=MAROON_DARK, width=3)
    # Labels with leader lines
    d.text((lx + 30, ly + 580), "·  Double membrane:  smooth OUTER + folded INNER",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((lx + 30, ly + 620), "·  Inner folds = CRISTAE  (more surface area for ATP)",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 660), "·  Own circular DNA  ·  Own 70S ribosomes",
           fill=ACCENT, font=font("sans_bold", 26))
    d.text((lx + 30, ly + 705), "·  Replicate by binary fission",
           fill=ACCENT, font=font("sans_bold", 26))

    # Right: chloroplasts
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=22,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "CHLOROPLASTS", fill=MAROON_DARK,
           font=font("sans_bold", 42))
    d.text((rx + 30, ly + 80),
           "Photosynthesis  →  glucose",
           fill=INK, font=font("sans", 30))
    d.text((rx + 30, ly + 125),
           "Plants + algae ONLY.  Never in animal cells.",
           fill=MAROON, font=font("sans_bold", 26))

    # Chloroplast drawing
    ccx, ccy = rx + rw // 2, ly + 400
    cw, ch = 580, 280
    d.ellipse([ccx - cw // 2, ccy - ch // 2,
               ccx + cw // 2, ccy + ch // 2],
              fill=ACCENT_LT, outline=MAROON_DARK, width=5)
    inner_cw = cw - 40
    inner_ch = ch - 40
    d.ellipse([ccx - inner_cw // 2, ccy - inner_ch // 2,
               ccx + inner_cw // 2, ccy + inner_ch // 2],
              fill=(180, 220, 180), outline=MAROON_DARK, width=4)
    # Thylakoid stacks (grana) — 4 stacks of 4 discs
    for gx_off in (-180, -60, 60, 180):
        for k in range(4):
            disc_y = ccy - 60 + k * 30
            d.ellipse([ccx + gx_off - 35, disc_y - 12,
                       ccx + gx_off + 35, disc_y + 12],
                      fill=(40, 130, 70), outline=MAROON_DARK, width=2)
    # Labels
    d.text((rx + 30, ly + 580), "·  Double membrane  +  internal THYLAKOIDS",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 30, ly + 620), "·  Thylakoids stack into GRANA  (light reactions)",
           fill=INK, font=font("sans", 26))
    d.text((rx + 30, ly + 660), "·  Own circular DNA  ·  Own 70S ribosomes",
           fill=ACCENT, font=font("sans_bold", 26))
    d.text((rx + 30, ly + 705), "·  Replicate by binary fission",
           fill=ACCENT, font=font("sans_bold", 26))
deck.custom("08_mitochondria_chloroplasts", energy_organelles)


# 09 — cytoskeleton (3 columns)
def cytoskeleton(img, d):
    d.text((110, 70), "Cytoskeleton  —  three filaments, three jobs.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Internal scaffolding that gives the cell shape, motion, and division.",
           fill=MUTED, font=font("sans", 28))

    cols = [
        ("MICROFILAMENTS", "actin (thinnest)", [
            "·  Cell shape",
            "·  Muscle contraction",
            "·  Cytokinesis",
            "    (cleavage furrow)",
        ], ACCENT),
        ("INTERMEDIATE", "various proteins", [
            "·  Mechanical strength",
            "·  Anchoring organelles",
            "·  Examples:",
            "    keratin (skin, hair)",
        ], MAROON),
        ("MICROTUBULES", "tubulin (thickest)", [
            "·  Tracks for motors",
            "    (kinesin, dynein)",
            "·  Mitotic spindle",
            "·  Cilia + flagella",
        ], ACCENT),
    ]

    col_w = 540
    col_h = 600
    gap = 30
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 230
    for i, (name, sub, lines, color) in enumerate(cols):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=20,
                            outline=color, width=5, fill=CARD)
        d.text((x + 26, y0 + 24), name, fill=color,
               font=font("serif_bold", 38))
        d.text((x + 26, y0 + 80), sub, fill=MUTED,
               font=font("sans_bold", 26))
        # Tiny filament icon — thickness varies by type
        thickness = [4, 8, 14][i]
        icon_y = y0 + 150
        d.line([(x + 30, icon_y), (x + col_w - 30, icon_y)],
               fill=color, width=thickness)
        # Lines
        ly = y0 + 210
        for ln in lines:
            d.text((x + 26, ly), ln, fill=INK, font=font("sans", 28))
            ly += 60

    # Bottom strip
    d.rounded_rectangle([110, 880, W - 110, 980], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Centrosomes / centrioles  =  microtubule organizing center  (animal cells).",
             font("sans_bold", 28), 910, MAROON_DARK)
deck.custom("09_cytoskeleton", cytoskeleton)


# 10 — pause: which organelles abundant in liver detox cell?
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Liver cells specialize in detoxifying drugs and alcohol.",
           "Which 3 organelles would be ABUNDANT in a liver cell?",
           hint="Hint:  one does detox  ·  one supplies ATP  ·  one handles H₂O₂.   Pause now.  Press play when ready.")

# 11 — duplicate pause for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — SA:V ratio equation slide
deck.equation("12_sa_v_ratio",
              "Why cells stay small  —  surface area vs. volume.",
              [
                  ("SA  ∝  r²        V  ∝  r³",     INK,
                   "Volume grows FASTER than surface area"),
                  ("SA : V  =  3 / r   (for a sphere)", ACCENT,
                   "Bigger r → smaller ratio"),
                  ("→  diffusion can't keep up  →  cells stay small", MAROON,
                   "Workarounds:  fold the membrane  ·  flatten  ·  compartmentalize"),
              ])


# 13 — endosymbiotic theory
def endosymbiosis(img, d):
    d.text((110, 70), "Endosymbiotic theory  —  the origin story.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Mitochondria + chloroplasts used to be free-living prokaryotes.  ~1.5–2 billion years ago.",
           fill=MUTED, font=font("sans", 26))

    # Top illustration: host engulfs bacterium
    # Three frames left-to-right
    frame_y = 220
    frame_h = 280
    frame_w = 540
    gap = 25
    total = frame_w * 3 + gap * 2
    start = (W - total) // 2
    captions = [
        "Large host cell",
        "Engulfs a prokaryote",
        "Becomes an organelle",
    ]
    for i in range(3):
        fx = start + i * (frame_w + gap)
        d.rounded_rectangle([fx, frame_y, fx + frame_w, frame_y + frame_h],
                            radius=20, outline=ACCENT, width=4, fill=CARD)
        cf = font("serif_bold", 28)
        tw = d.textlength(captions[i], font=cf)
        d.text((fx + frame_w / 2 - tw / 2, frame_y + 20),
               captions[i], fill=MAROON_DARK, font=cf)
        cx = fx + frame_w // 2
        cy = frame_y + 170
        # Host cell oval
        d.ellipse([cx - 180, cy - 90, cx + 180, cy + 90],
                  fill=ACCENT_LT, outline=MAROON_DARK, width=4)
        if i == 0:
            pass  # nothing inside
        elif i == 1:
            # Small bacterium being pulled in (near the edge / dent)
            d.ellipse([cx + 130, cy - 30, cx + 200, cy + 30],
                      fill=MAROON, outline=MAROON_DARK, width=3)
            # Arrow showing engulfment
            d.polygon([
                (cx + 90, cy),
                (cx + 120, cy - 10),
                (cx + 120, cy + 10),
            ], fill=MAROON_DARK)
        else:
            # Bacterium now INSIDE with extra (host) membrane wrapping it
            d.ellipse([cx - 50, cy - 40, cx + 50, cy + 40],
                      fill=MAROON, outline=MAROON_DARK, width=3)
            d.ellipse([cx - 60, cy - 50, cx + 60, cy + 50],
                      outline=MAROON_DARK, width=3)
            d.text((cx - 78, cy + 60), "= organelle", fill=MAROON_DARK,
                   font=font("sans_bold", 22))

    # Bottom — 4 evidence rows
    d.rounded_rectangle([110, 540, W - 110, 970], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    d.text((150, 560), "Four lines of evidence:",
           fill=MAROON_DARK, font=font("serif_bold", 38))

    evidence = [
        ("1.", "Double membrane",
         "outer = host vesicle  ·  inner = ancestral prokaryote"),
        ("2.", "Own circular DNA",
         "like bacteria  ·  not the host's linear chromosomes"),
        ("3.", "Binary fission",
         "they divide independently of the host cell cycle"),
        ("4.", "70S ribosomes",
         "the prokaryote-sized ribosome  (not 80S)"),
    ]
    ey = 640
    for num, head, sub in evidence:
        d.text((170, ey), num, fill=ACCENT, font=font("serif_bold", 36))
        d.text((230, ey - 2), head, fill=INK,
               font=font("sans_bold", 32))
        d.text((720, ey + 4), sub, fill=MAROON_DARK,
               font=font("sans", 26))
        ey += 75
deck.custom("13_endosymbiosis", endosymbiosis)


# 14 — common AP traps
deck.compare("14_compare_traps", "Common AP traps  —  read carefully.",
             left={
                 "label": "✗  WRONG ASSUMPTIONS",
                 "color": RED,
                 "lines": [
                     "“All cells have lysosomes.”",
                     "→ Mostly ANIMAL cells.",
                     "",
                     "“All eukaryotes have chloroplasts.”",
                     "→ Only PLANTS + algae.",
                     "→ Never in animals.",
                 ],
                 "footnote": "Animal vs. plant matters on the AP exam."
             },
             right={
                 "label": "✓  RIGHT IDEA",
                 "color": ACCENT,
                 "lines": [
                     "Plants have a CENTRAL VACUOLE.",
                     "→ Stores water, maintains turgor.",
                     "→ Also does digestive / storage work",
                     "    similar to a lysosome.",
                     "",
                     "Same problem, different organelle.",
                 ],
                 "footnote": "Match the organelle to the cell type."
             })


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Prokaryotes:  no nucleus, no organelles, small.  Eukaryotes:  nucleus, organelles, big.",
    "Each organelle = a room with a job  (nucleus, ribosomes, ER, Golgi, lysosome, mitochondria, etc.).",
    "Mitochondria → ATP.  Chloroplasts → glucose, PLANTS ONLY.",
    "SA:V ratio  =  why cells stay small.  V grows as r³, SA only as r².",
    "Endosymbiosis evidence:  double membrane, circular DNA, binary fission, 70S ribosomes.",
], assignment=[
    "1.  Map each organelle to its function from memory  (10 items).",
    "2.  Predict which organelles dominate in:  pancreas (secretes), muscle (Ca²⁺), neuron (ATP).",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapter 4 — Cell Structure"),
    ("2.", "Khan Academy AP Bio",     "Unit 2 problem sets — organelles + compartmentalization"),
    ("3.", "Assignment in dashboard", "Organelle-to-function mapping + structure prediction"),
    ("4.", "Advisor check-in",        "If endomembrane flow or endosymbiosis evidence feel fuzzy"),
], next_text="Next up:  Module 3 — Membrane Transport.")


print("AP Biology Module 2 slides built.")

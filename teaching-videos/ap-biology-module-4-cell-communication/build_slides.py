"""AP Biology · Module 4 — Cell Communication.

Teal (science) theme auto-resolved by slide_kit from the "AP Biology" prefix.
16 slides total. Pause slide is duplicated (10 -> 11) so the same image plays
during both the question and the answer narration.
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
deck = Deck(course="AP Biology", module_num=4, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 4 — Cell Communication",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook: adrenaline cascade (one molecule, huge response)
def hook(img, d):
    d.text((110, 80), "One molecule.  Massive response.",
           fill=MAROON, font=font("serif_bold", 64))

    # Left panel — adrenaline molecule (small circle)
    lx, ly, lw, lh = 140, 230, 760, 540
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    cap = "1 adrenaline molecule"
    cf = font("serif_bold", 38)
    tw = d.textlength(cap, font=cf)
    d.text((lx + lw // 2 - tw / 2, ly + 40), cap,
           fill=MAROON_DARK, font=cf)
    sub = "lands on a receptor on your heart cell"
    sf = font("sans", 26)
    tw2 = d.textlength(sub, font=sf)
    d.text((lx + lw // 2 - tw2 / 2, ly + 100), sub,
           fill=MUTED, font=sf)

    # Tiny dot for the molecule
    mol_cx = lx + lw // 2
    mol_cy = ly + 260
    d.ellipse([mol_cx - 18, mol_cy - 18, mol_cx + 18, mol_cy + 18],
              fill=RED, outline=MAROON_DARK, width=3)
    d.text((mol_cx + 35, mol_cy - 16), "adrenaline",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # Cell membrane line with receptor
    mem_y = ly + 360
    d.line([(lx + 60, mem_y), (lx + lw - 60, mem_y)],
           fill=ACCENT, width=8)
    d.line([(lx + 60, mem_y + 20), (lx + lw - 60, mem_y + 20)],
           fill=ACCENT, width=8)
    # Receptor "Y" shape
    rec_cx = mol_cx
    d.line([(rec_cx, mem_y - 40), (rec_cx, mem_y + 60)],
           fill=MAROON_DARK, width=6)
    d.line([(rec_cx, mem_y - 40), (rec_cx - 25, mem_y - 70)],
           fill=MAROON_DARK, width=6)
    d.line([(rec_cx, mem_y - 40), (rec_cx + 25, mem_y - 70)],
           fill=MAROON_DARK, width=6)
    d.text((lx + 60, mem_y + 80), "receptor on cell surface",
           fill=MUTED, font=font("sans", 24))

    # Right panel — explosion of effects
    rx, ry, rw, rh = 1020, 230, 760, 540
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    cap2 = "Inside the cell:  millions of changes"
    tw3 = d.textlength(cap2, font=cf)
    d.text((rx + rw // 2 - tw3 / 2, ry + 40), cap2,
           fill=MAROON_DARK, font=cf)

    effects = [
        "heart rate ↑",
        "blood vessels constrict",
        "pupils dilate",
        "glycogen → glucose",
        "airways open",
    ]
    ey = ry + 130
    for e in effects:
        d.ellipse([rx + 60, ey + 16, rx + 80, ey + 36],
                  fill=ACCENT)
        d.text((rx + 110, ey + 8), e, fill=INK,
               font=font("sans_bold", 32))
        ey += 70

    # Bottom punchline strip
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "How does ONE molecule outside cause MILLIONS of changes inside?",
             font("serif_bold", 36), 850, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Reception — the ligand binds a receptor.",
    "Transduction — the message is relayed AND amplified inside.",
    "Response — the cell changes what it's doing.",
], footnote="Sutherland's 3 stages.  Every signaling question on the AP assumes this order.")


# 04 — signal types (custom: 3 columns by distance)
def signal_types(img, d):
    d.text((110, 70), "Cells signal over different distances.",
           fill=MAROON, font=font("serif_bold", 56))

    cols = [
        ("DIRECT CONTACT", "touching cells", [
            "Gap junctions",
            "  (animals)",
            "Plasmodesmata",
            "  (plants)",
            "",
            "Cell-cell recognition",
            "via surface proteins.",
        ], "no signal travels"),
        ("LOCAL", "short distance", [
            "Paracrine —",
            "  growth factors",
            "  on neighbors.",
            "",
            "Synaptic —",
            "  neurotransmitter",
            "  across a synapse.",
        ], "diffuses a few cells"),
        ("LONG-DISTANCE", "across the body", [
            "Endocrine —",
            "  hormones in",
            "  the bloodstream.",
            "",
            "Neuroendocrine —",
            "  nerve releases",
            "  hormone to blood.",
        ], "anywhere in the body"),
    ]

    col_w = 540
    col_h = 660
    gap = 30
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 200
    for i, (name, sub, lines, foot) in enumerate(cols):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=20,
                            outline=ACCENT, width=5, fill=CARD)
        d.text((x + 26, y0 + 24), name, fill=ACCENT,
               font=font("serif_bold", 40))
        d.text((x + 26, y0 + 80), sub, fill=MUTED,
               font=font("sans_bold", 28))
        ly = y0 + 160
        for ln in lines:
            d.text((x + 26, ly), ln, fill=INK, font=font("sans", 28))
            ly += 52
        d.text((x + 26, y0 + col_h - 50), foot, fill=MAROON_DARK,
               font=font("sans_bold", 26))

    # Bottom note
    d.rounded_rectangle([110, 900, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Same 3 stages (reception → transduction → response) — only the delivery method changes.",
             font("sans_bold", 28), 930, MAROON_DARK)
deck.custom("04_signal_types", signal_types)


# 05 — reception → transduction → response (Sutherland)
def three_stages(img, d):
    d.text((110, 70), "Sutherland's 3 stages.  Always in this order.",
           fill=MAROON, font=font("serif_bold", 54))
    d.text((110, 160),
           "Earl Sutherland, 1950s — studied adrenaline acting on liver cells.  Nobel 1971.",
           fill=MUTED, font=font("sans", 28))

    stages = [
        ("1.  RECEPTION",
         "Ligand binds the receptor.",
         "Signal molecule lands on a specific receptor protein."),
        ("2.  TRANSDUCTION",
         "Receptor activates a relay.",
         "Inside the cell: a cascade of molecules passes the message along (often phosphorylation)."),
        ("3.  RESPONSE",
         "Cell behavior changes.",
         "Gene expression, enzyme activation, cytoskeleton rearrangement."),
    ]
    box_w = W - 220
    box_h = 200
    gap = 25
    y = 250
    for head, body, foot in stages:
        d.rounded_rectangle([110, y, 110 + box_w, y + box_h],
                            radius=20, outline=ACCENT, width=5,
                            fill=CARD)
        d.text((140, y + 20), head, fill=ACCENT,
               font=font("serif_bold", 44))
        d.text((140, y + 85), body, fill=MAROON_DARK,
               font=font("sans_bold", 32))
        d.text((140, y + 135), foot, fill=INK,
               font=font("sans", 28))
        y += box_h + gap

    # Down arrows between stages
    arrow_x = 110 + box_w // 2
    for ay in [y - 2 * (box_h + gap) - gap // 2,
               y - (box_h + gap) - gap // 2]:
        d.polygon([
            (arrow_x - 18, ay - 10),
            (arrow_x + 18, ay - 10),
            (arrow_x, ay + 14),
        ], fill=MAROON)
deck.custom("05_reception_3stages", three_stages)


# 06 — GPCR (custom: 7-pass diagram + G protein swap)
def gpcr_slide(img, d):
    d.text((110, 70), "G protein-coupled receptors  (GPCRs).",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "7-transmembrane protein.  Largest receptor family.  Targets: taste, smell, vision, ~30% of drugs.",
           fill=MUTED, font=font("sans", 26))

    # Left: 7-pass receptor membrane diagram
    lx, ly = 140, 240
    lw, lh = 800, 600
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=22,
                        outline=ACCENT, width=5, fill=CARD)

    # Membrane bands
    mem_top = ly + 200
    mem_bot = ly + 380
    d.rectangle([lx + 30, mem_top, lx + lw - 30, mem_bot],
                fill=ACCENT_LT)
    d.line([(lx + 30, mem_top), (lx + lw - 30, mem_top)],
           fill=ACCENT, width=4)
    d.line([(lx + 30, mem_bot), (lx + lw - 30, mem_bot)],
           fill=ACCENT, width=4)
    d.text((lx + 40, ly + 30), "outside", fill=MUTED,
           font=font("sans_bold", 26))
    d.text((lx + 40, ly + lh - 70), "inside", fill=MUTED,
           font=font("sans_bold", 26))

    # 7 transmembrane helices (zig-zag through membrane)
    helix_xs = [lx + 220, lx + 290, lx + 360, lx + 430, lx + 500, lx + 570, lx + 640]
    for i, hx in enumerate(helix_xs):
        d.rectangle([hx - 16, mem_top - 10, hx + 16, mem_bot + 10],
                    fill=MAROON, outline=MAROON_DARK, width=3)
        d.text((hx - 8, (mem_top + mem_bot) // 2 - 14),
               str(i + 1), fill=CREAM, font=font("sans_bold", 24))

    # Connecting loops above and below (alternating)
    for i in range(6):
        x1 = helix_xs[i]
        x2 = helix_xs[i + 1]
        if i % 2 == 0:
            # loop above
            d.arc([x1 - 5, mem_top - 50, x2 + 5, mem_top + 10],
                  180, 360, fill=MAROON, width=4)
        else:
            # loop below
            d.arc([x1 - 5, mem_bot - 10, x2 + 5, mem_bot + 50],
                  0, 180, fill=MAROON, width=4)

    # Ligand on top
    lig_cx = (helix_xs[2] + helix_xs[4]) // 2
    d.ellipse([lig_cx - 24, mem_top - 110, lig_cx + 24, mem_top - 62],
              fill=RED, outline=MAROON_DARK, width=3)
    d.text((lig_cx + 35, mem_top - 105), "ligand",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # G protein blob below
    gx = (helix_xs[3] + helix_xs[5]) // 2
    gy = mem_bot + 80
    d.ellipse([gx - 90, gy - 40, gx + 90, gy + 40],
              fill=ACCENT, outline=MAROON_DARK, width=4)
    d.text((gx - 60, gy - 14), "G protein", fill=CREAM,
           font=font("sans_bold", 26))

    # Caption
    centered(d, "7 transmembrane passes  ·  G protein attached on the inside",
             font("sans_bold", 26), ly + lh - 40, MAROON_DARK)

    # Right: GDP → GTP swap
    rx = lx + lw + 30
    rw = W - 110 - rx
    rh = 600
    d.rounded_rectangle([rx, ly, rx + rw, ly + rh], radius=22,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "The activation switch:",
           fill=MAROON_DARK, font=font("serif_bold", 36))

    d.rounded_rectangle([rx + 30, ly + 100, rx + rw - 30, ly + 220],
                        radius=14, outline=ACCENT, width=4,
                        fill=ACCENT_LT)
    centered_x = rx + rw // 2
    of_text = "OFF state:  G protein has GDP bound"
    tw_o = d.textlength(of_text, font=font("sans_bold", 26))
    d.text((centered_x - tw_o / 2, ly + 130),
           of_text, fill=MAROON_DARK, font=font("sans_bold", 26))
    centered(d, "GDP",
             font("mono", 60), ly + 165, MAROON)

    # Arrow down
    d.polygon([
        (centered_x - 22, ly + 245),
        (centered_x + 22, ly + 245),
        (centered_x, ly + 280),
    ], fill=MAROON)
    d.text((rx + 30, ly + 250), "ligand binds  →  swap",
           fill=ACCENT, font=font("sans_bold", 24))

    d.rounded_rectangle([rx + 30, ly + 300, rx + rw - 30, ly + 420],
                        radius=14, outline=ACCENT, width=4,
                        fill=ACCENT_LT)
    on_text = "ON state:  G protein has GTP bound"
    tw_n = d.textlength(on_text, font=font("sans_bold", 26))
    d.text((centered_x - tw_n / 2, ly + 330),
           on_text, fill=MAROON_DARK, font=font("sans_bold", 26))
    centered(d, "GTP",
             font("mono", 60), ly + 365, ACCENT)

    # Downstream
    d.text((rx + 30, ly + 460),
           "Active G protein →  adenylyl cyclase  →  cAMP",
           fill=INK, font=font("sans", 26))
    d.text((rx + 30, ly + 505),
           "(NOTE:  GTP swap — NOT ATP at this step.)",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # Bottom strip
    d.rounded_rectangle([110, 900, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "GPCR rule:  ligand on outside  →  G protein swaps GDP for GTP  →  cascade begins.",
             font("sans_bold", 28), 930, MAROON_DARK)
deck.custom("06_receptor_gpcr", gpcr_slide)


# 07 — RTK (custom: dimerization + cross-phosphorylation)
def rtk_slide(img, d):
    d.text((110, 70), "Receptor tyrosine kinases  (RTKs).",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Single-pass membrane proteins.  Examples: insulin receptor, growth factor receptors.",
           fill=MUTED, font=font("sans", 26))

    # Membrane band across the slide
    mem_top = 380
    mem_bot = 480
    d.rectangle([110, mem_top, W - 110, mem_bot], fill=ACCENT_LT)
    d.line([(110, mem_top), (W - 110, mem_top)], fill=ACCENT, width=4)
    d.line([(110, mem_bot), (W - 110, mem_bot)], fill=ACCENT, width=4)
    d.text((130, 250), "outside", fill=MUTED, font=font("sans_bold", 24))
    d.text((130, mem_bot + 200), "inside", fill=MUTED, font=font("sans_bold", 24))

    # State 1 — two separate monomers (left)
    state1_x = 360
    for offset in (-100, 100):
        x = state1_x + offset
        # extracellular domain (ball)
        d.ellipse([x - 36, 250, x + 36, 322],
                  fill=MAROON, outline=MAROON_DARK, width=3)
        # transmembrane bar
        d.rectangle([x - 14, 322, x + 14, mem_bot + 30],
                    fill=MAROON, outline=MAROON_DARK, width=3)
        # intracellular kinase domain
        d.rectangle([x - 60, mem_bot + 30, x + 60, mem_bot + 130],
                    fill=ACCENT, outline=MAROON_DARK, width=3)
        d.text((x - 38, mem_bot + 60), "kinase",
               fill=CREAM, font=font("sans_bold", 22))

    centered(d, "BEFORE  —  2 separate monomers",
             font("sans_bold", 30), 180, MAROON_DARK)
    centered_x = state1_x
    cap = "no ligand bound"
    cf2 = font("sans", 24)
    tw_cap = d.textlength(cap, font=cf2)
    d.text((centered_x - tw_cap / 2, mem_bot + 160),
           cap, fill=MUTED, font=cf2)

    # Arrow ligand → middle
    arrow_y = (mem_top + mem_bot) // 2
    d.polygon([
        (state1_x + 180, arrow_y - 14),
        (state1_x + 240, arrow_y),
        (state1_x + 180, arrow_y + 14),
    ], fill=MAROON)
    d.text((state1_x + 175, arrow_y + 28),
           "ligand binds  →  dimerize",
           fill=ACCENT, font=font("sans_bold", 22))

    # State 2 — dimerized RTK (right)
    state2_x = 1350
    for offset in (-40, 40):
        x = state2_x + offset
        d.ellipse([x - 36, 250, x + 36, 322],
                  fill=MAROON, outline=MAROON_DARK, width=3)
        d.rectangle([x - 14, 322, x + 14, mem_bot + 30],
                    fill=MAROON, outline=MAROON_DARK, width=3)
        d.rectangle([x - 60, mem_bot + 30, x + 60, mem_bot + 130],
                    fill=ACCENT, outline=MAROON_DARK, width=3)
        d.text((x - 38, mem_bot + 60), "kinase",
               fill=CREAM, font=font("sans_bold", 22))

    # Ligand sitting on top of dimer
    lig_cx = state2_x
    d.ellipse([lig_cx - 80, 180, lig_cx + 80, 240],
              fill=RED, outline=MAROON_DARK, width=3)
    centered_x2 = lig_cx
    lig_text = "ligand"
    tw_l = d.textlength(lig_text, font=font("sans_bold", 26))
    d.text((centered_x2 - tw_l / 2, 195),
           lig_text, fill=CREAM, font=font("sans_bold", 26))

    centered(d, "AFTER  —  dimer cross-phosphorylates",
             font("sans_bold", 30), 180, MAROON_DARK)

    # P-Y tags on each kinase
    for offset in (-100, 100):
        px = state2_x + offset
        for dy in (45, 90):
            d.ellipse([px - 12, mem_bot + 30 + dy,
                       px + 12, mem_bot + 54 + dy],
                      fill=RED, outline=MAROON_DARK, width=2)
            d.text((px - 8, mem_bot + 34 + dy), "P",
                   fill=CREAM, font=font("sans_bold", 18))

    d.text((state2_x - 130, mem_bot + 160),
           "tyrosines phosphorylated",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # Bottom rule strip
    d.rounded_rectangle([110, 880, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "RTK rule:  ligand binds  →  dimerize  →  cross-phosphorylate tyrosines (uses ATP).",
             font("sans_bold", 30), 905, MAROON_DARK)
    centered(d, "Phospho-tyrosines = docking sites for many relay proteins  →  one RTK triggers many pathways.",
             font("sans", 26), 955, INK)
deck.custom("07_receptor_rtk", rtk_slide)


# 08 — other receptors (ligand-gated + intracellular)
def other_receptors(img, d):
    d.text((110, 70), "Two more receptor types to know.",
           fill=MAROON, font=font("serif_bold", 56))

    # Left card: ligand-gated ion channel
    lx, ly = 110, 200
    lw, lh = 870, 700
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=22,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "LIGAND-GATED ION CHANNEL",
           fill=ACCENT, font=font("sans_bold", 32))
    d.text((lx + 30, ly + 70), "ligand opens the gate  →  ions flow",
           fill=MUTED, font=font("sans", 26))

    # Membrane
    mem_top = ly + 280
    mem_bot = ly + 380
    d.rectangle([lx + 30, mem_top, lx + lw - 30, mem_bot],
                fill=ACCENT_LT)
    d.line([(lx + 30, mem_top), (lx + lw - 30, mem_top)],
           fill=ACCENT, width=4)
    d.line([(lx + 30, mem_bot), (lx + lw - 30, mem_bot)],
           fill=ACCENT, width=4)

    # Channel (two posts with gap)
    chx = lx + lw // 2
    d.rectangle([chx - 70, mem_top - 30, chx - 30, mem_bot + 30],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.rectangle([chx + 30, mem_top - 30, chx + 70, mem_bot + 30],
                fill=MAROON, outline=MAROON_DARK, width=3)

    # Ligand above
    d.ellipse([chx - 18, mem_top - 90, chx + 18, mem_top - 54],
              fill=RED, outline=MAROON_DARK, width=3)
    d.text((chx + 30, mem_top - 80), "ligand",
           fill=MAROON_DARK, font=font("sans_bold", 22))

    # Ions flowing through (small circles)
    for i, iy in enumerate([mem_top - 20, mem_top + 30, mem_bot - 20, mem_bot + 30]):
        d.ellipse([chx - 10, iy - 8, chx + 10, iy + 8],
                  fill=ACCENT, outline=MAROON_DARK, width=2)
    d.text((chx + 90, mem_top + 10), "ions →",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    d.text((lx + 30, ly + lh - 180), "Classic example:",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((lx + 30, ly + lh - 130),
           "acetylcholine receptor at",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + lh - 95),
           "the neuromuscular junction.",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + lh - 50),
           "Fast — milliseconds to respond.",
           fill=ACCENT, font=font("sans_bold", 24))

    # Right card: intracellular receptors
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=22,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "INTRACELLULAR RECEPTORS",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((rx + 30, ly + 70),
           "for NONPOLAR ligands that cross the membrane",
           fill=MUTED, font=font("sans", 26))

    # Membrane
    mem_top2 = ly + 200
    mem_bot2 = ly + 280
    d.rectangle([rx + 30, mem_top2, rx + rw - 30, mem_bot2],
                fill=ACCENT_LT)
    d.line([(rx + 30, mem_top2), (rx + rw - 30, mem_top2)],
           fill=ACCENT, width=4)
    d.line([(rx + 30, mem_bot2), (rx + rw - 30, mem_bot2)],
           fill=ACCENT, width=4)

    # Steroid molecules crossing through (3 dots staircased)
    base_x = rx + 150
    for i, off in enumerate([(0, -120), (60, -40), (120, 30)]):
        cx = base_x + off[0]
        cy = mem_top2 + off[1] + 60
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16],
                  fill=RED, outline=MAROON_DARK, width=3)
    d.text((base_x - 30, mem_top2 - 160), "steroid",
           fill=MAROON_DARK, font=font("sans_bold", 24))
    d.text((base_x - 30, mem_top2 - 125), "hormone",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # Nucleus inside cell
    nx = rx + rw // 2 + 90
    ny = ly + 480
    d.ellipse([nx - 130, ny - 80, nx + 130, ny + 80],
              fill=ACCENT_LT, outline=MAROON_DARK, width=4)
    d.text((nx - 50, ny - 14), "NUCLEUS",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # Steroid + receptor complex entering nucleus
    d.ellipse([nx - 20, ny - 14, nx + 20, ny + 14],
              fill=RED, outline=MAROON_DARK, width=2)

    d.text((rx + 30, ly + lh - 220),
           "Examples:  steroid hormones,",
           fill=INK, font=font("sans", 26))
    d.text((rx + 30, ly + lh - 185),
           "thyroid hormone, NO.",
           fill=INK, font=font("sans", 26))
    d.text((rx + 30, ly + lh - 130),
           "Complex enters nucleus →",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 30, ly + lh - 95),
           "acts as transcription factor.",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 30, ly + lh - 50),
           "Slow — hours of response.",
           fill=ACCENT, font=font("sans_bold", 24))

    # Bottom rule
    d.rounded_rectangle([110, 920, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Polar ligand → surface receptor.  Nonpolar ligand → intracellular receptor.",
             font("sans_bold", 28), 940, MAROON_DARK)
deck.custom("08_receptor_other", other_receptors)


# 09 — transduction cascade + amplification
def cascade_slide(img, d):
    d.text((110, 70), "Transduction:  phosphorylation cascade.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Kinases add phosphate (from ATP).  Phosphatases remove it.  Each step amplifies.",
           fill=MUTED, font=font("sans", 28))

    # Cascade diagram: receptor → 100 → 10,000 → 1,000,000
    levels = [
        ("1 receptor", 1, 240),
        ("~100 active kinases", 100, 420),
        ("~10,000 active kinases", 10000, 600),
        ("~1,000,000 products", 1000000, 780),
    ]
    cx = W // 2
    for i, (label, count, y) in enumerate(levels):
        # Row of dots — capped visually at ~10 dots per row
        visible = min(count, 12)
        if count >= 1000:
            visible = 12
        dot_r = max(8, 24 - i * 4)
        spacing = 50
        total_w = (visible - 1) * spacing
        start_dx = cx - total_w // 2
        for j in range(visible):
            dx = start_dx + j * spacing
            color = MAROON if i == 0 else ACCENT
            d.ellipse([dx - dot_r, y - dot_r, dx + dot_r, y + dot_r],
                      fill=color, outline=MAROON_DARK, width=2)
        # Label on left
        d.text((140, y - 16), label, fill=MAROON_DARK,
               font=font("sans_bold", 30))
        # Count on right
        count_str = f"{count:,}" if count >= 100 else str(count)
        d.text((W - 380, y - 18), count_str + "  molecules",
               fill=ACCENT, font=font("sans_bold", 30))
        # Arrow down (between rows)
        if i < len(levels) - 1:
            ay = y + 50
            d.polygon([
                (cx - 18, ay), (cx + 18, ay),
                (cx, ay + 30),
            ], fill=MAROON)
            d.text((cx + 40, ay + 4), "×100",
                   fill=ACCENT, font=font("sans_bold", 26))

    # Bottom rule strip
    d.rounded_rectangle([110, 900, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Kinases add P from ATP  ·  phosphatases remove P  ·  3 layers ≈ 10⁶ amplification.",
             font("sans_bold", 28), 930, MAROON_DARK)
deck.custom("09_transduction_cascade", cascade_slide)


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "A cell needs to amplify a signal 1,000,000 ×.",
           "1 receptor + 1 intracellular molecule  —  enough?",
           hint="What mechanism actually achieves this?  Pause. Think. Press play.")

# 11 — duplicate pause for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — second messengers (custom: 3 columns)
def second_messengers(img, d):
    d.text((110, 70), "Second messengers  —  spread the signal fast.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Small molecules that diffuse rapidly through the cell.",
           fill=MUTED, font=font("sans", 28))

    cols = [
        ("cAMP", "cyclic AMP",
         ["Made from ATP by",
          "adenylyl cyclase.",
          "",
          "Downstream of GPCRs.",
          "",
          "Activates PKA →",
          "phosphorylation cascade."],
         "Classic 2nd messenger"),
        ("Ca²⁺", "calcium ions",
         ["Released from ER",
          "stores.",
          "",
          "Activates many",
          "enzymes + muscle",
          "contraction.",
          ""],
         "Most versatile"),
        ("IP₃ + DAG", "from PIP₂",
         ["PIP₂ (membrane lipid)",
          "is cleaved →",
          "",
          "IP₃ → opens Ca²⁺",
          "channels on ER.",
          "",
          "DAG → activates PKC."],
         "Tag-team messengers"),
    ]
    col_w = 540
    col_h = 660
    gap = 30
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 230
    for i, (name, sub, lines, foot) in enumerate(cols):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=20,
                            outline=ACCENT, width=5, fill=CARD)
        d.text((x + 26, y0 + 24), name, fill=ACCENT,
               font=font("serif_bold", 46))
        d.text((x + 26, y0 + 90), sub, fill=MUTED,
               font=font("sans_bold", 28))
        ly = y0 + 170
        for ln in lines:
            d.text((x + 26, ly), ln, fill=INK, font=font("sans", 26))
            ly += 50
        d.text((x + 26, y0 + col_h - 50), foot, fill=MAROON_DARK,
               font=font("sans_bold", 26))

    # Bottom strip
    d.rounded_rectangle([110, 920, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "cAMP from ATP via adenylyl cyclase  ·  Ca²⁺ from ER  ·  IP₃ + DAG from PIP₂.",
             font("sans_bold", 28), 940, MAROON_DARK)
deck.custom("12_second_messengers", second_messengers)


# 13 — apoptosis (custom)
def apoptosis_slide(img, d):
    d.text((110, 70), "Response example:  apoptosis.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160),
           "Programmed cell death.  Clean, quiet, controlled.",
           fill=MUTED, font=font("sans", 28))

    # Sequence of 4 cell stages
    stages = [
        ("Healthy", "round cell, intact"),
        ("Shrinking", "cytoskeleton breaks down"),
        ("Fragmenting", "membrane-bound apoptotic bodies"),
        ("Phagocytosed", "engulfed — no inflammation"),
    ]
    box_w = 380
    box_h = 380
    gap = 30
    total_w = box_w * 4 + gap * 3
    start_x = (W - total_w) // 2
    y0 = 260

    for i, (name, sub) in enumerate(stages):
        x = start_x + i * (box_w + gap)
        d.rounded_rectangle([x, y0, x + box_w, y0 + box_h],
                            radius=20, outline=ACCENT, width=5,
                            fill=CARD)

        cell_cx = x + box_w // 2
        cell_cy = y0 + 160
        if i == 0:
            r = 90
            d.ellipse([cell_cx - r, cell_cy - r, cell_cx + r, cell_cy + r],
                      fill=ACCENT_LT, outline=MAROON_DARK, width=4)
        elif i == 1:
            r = 60
            d.ellipse([cell_cx - r, cell_cy - r, cell_cx + r, cell_cy + r],
                      fill=ACCENT_LT, outline=MAROON_DARK, width=4)
            # Inward arrows
            for ang in (0, 90, 180, 270):
                ax = cell_cx + int(85 * math.cos(math.radians(ang)))
                ay = cell_cy + int(85 * math.sin(math.radians(ang)))
                bx = cell_cx + int(65 * math.cos(math.radians(ang)))
                by = cell_cy + int(65 * math.sin(math.radians(ang)))
                d.line([(ax, ay), (bx, by)], fill=MAROON, width=4)
        elif i == 2:
            # Several small blebs
            for off in [(-50, -30), (40, -40), (-30, 40), (50, 30), (0, 0)]:
                r = 30
                bx = cell_cx + off[0]
                by = cell_cy + off[1]
                d.ellipse([bx - r, by - r, bx + r, by + r],
                          fill=ACCENT_LT, outline=MAROON_DARK, width=3)
        else:
            # Big phagocyte (gray blob) with small cell inside
            r = 100
            d.ellipse([cell_cx - r, cell_cy - r, cell_cx + r, cell_cy + r],
                      fill=(200, 200, 200), outline=MAROON_DARK, width=4)
            # small bits inside
            for off in [(-25, -10), (15, -20), (10, 20), (-20, 25)]:
                rb = 14
                bx = cell_cx + off[0]
                by = cell_cy + off[1]
                d.ellipse([bx - rb, by - rb, bx + rb, by + rb],
                          fill=ACCENT_LT, outline=MAROON_DARK, width=2)
            d.text((x + 20, y0 + 30), "phagocyte",
                   fill=MUTED, font=font("sans_bold", 22))

        # Labels
        cap_y = y0 + box_h - 110
        nf = font("sans_bold", 32)
        tw_n = d.textlength(name, font=nf)
        d.text((cell_cx - tw_n / 2, cap_y),
               name, fill=MAROON_DARK, font=nf)
        sf = font("sans", 22)
        tw_s = d.textlength(sub, font=sf)
        d.text((cell_cx - tw_s / 2, cap_y + 45),
               sub, fill=INK, font=sf)

        # Arrow between
        if i < 3:
            ay_mid = y0 + box_h // 2
            ax_mid = x + box_w + 5
            d.polygon([
                (ax_mid, ay_mid - 14),
                (ax_mid + 18, ay_mid),
                (ax_mid, ay_mid + 14),
            ], fill=MAROON)

    # Bottom strip
    d.rounded_rectangle([110, 770, W - 110, 1000], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    d.text((140, 800), "Mechanism", fill=MAROON_DARK,
           font=font("serif_bold", 38))
    d.text((140, 860),
           "Triggers (DNA damage, immune signals)  →  activate CASPASES (proteases).",
           fill=INK, font=font("sans", 28))
    d.text((140, 905),
           "Caspases cleave cytoskeleton, DNA, organelles  →  cell fragments  →  phagocytosed.",
           fill=INK, font=font("sans", 28))
    d.text((140, 950),
           "vs. NECROSIS:  apoptosis is CLEAN — no inflammation.",
           fill=MAROON_DARK, font=font("sans_bold", 28))
deck.custom("13_response_apoptosis", apoptosis_slide)


# 14 — GPCR vs RTK compare (using deck.compare)
deck.compare("14_compare_traps", "Common trap:  GPCR vs RTK.",
    left={
        "label": "GPCR",
        "color": ACCENT,
        "lines": [
            "• 7-transmembrane passes",
            "• Works through G protein",
            "• G protein swaps GDP → GTP",
            "• NO ATP at the switch",
            "• Triggers ONE main pathway",
            "  (e.g., cAMP)",
            "• Targets: taste, smell, vision",
        ],
        "footnote": "Activation = nucleotide swap",
    },
    right={
        "label": "RTK",
        "color": MAROON,
        "lines": [
            "• Single-pass membrane",
            "• Two monomers DIMERIZE",
            "• Cross-phosphorylate tyrosines",
            "• Uses ATP to phosphorylate",
            "• Triggers MULTIPLE pathways",
            "  (many docking sites)",
            "• Example: insulin receptor",
        ],
        "footnote": "Activation = phosphorylation",
    })


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "3 stages (Sutherland):  reception → transduction → response.",
    "4 receptor types:  GPCR, RTK, ligand-gated channel, intracellular (steroids).",
    "Phosphorylation cascade amplifies — kinases add P (from ATP), phosphatases remove P.",
    "2nd messengers:  cAMP (from ATP), Ca²⁺ (from ER), IP₃ + DAG (from PIP₂).",
    "Apoptosis = caspase-driven, clean, no inflammation.  Bacteria use quorum sensing.",
], assignment=[
    "1.  Compare GPCR vs RTK — structure, switch mechanism, ATP use, examples.",
    "2.  Explain how a phosphorylation cascade amplifies a signal 1,000,000×.",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapter 9 — cell communication, all signaling pathways"),
    ("2.", "Khan Academy AP Bio",     "Unit 4 problem sets — receptor types, second messengers, amplification"),
    ("3.", "Assignment in dashboard", "GPCR vs RTK + amplification calculation (above)"),
    ("4.", "Advisor check-in",        "If GPCR vs RTK or the cascade math still feels fuzzy"),
], next_text="Next up:  Module 5 — Cell Cycle and Division.")


print("AP Biology Module 4 slides built.")

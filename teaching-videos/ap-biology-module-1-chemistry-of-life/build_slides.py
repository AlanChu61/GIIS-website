"""AP Biology · Module 1 — Chemistry of Life.

Teal (science) theme auto-resolved by slide_kit from the "AP Biology" prefix.
16 slides total. Heavy on customs because the macromolecule slides each pack
a lot of vocab and need real layout. Pause slide is duplicated (10 -> 11) so
the same image plays during both the question and the answer narration.
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
deck = Deck(course="AP Biology", module_num=1, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 1 — Chemistry of Life",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook: ice floats + water climbs a tree
def hook(img, d):
    d.text((110, 80), "Two weird things about water.",
           fill=MAROON, font=font("serif_bold", 64))

    # Left panel: ice cube floating on water
    lx, ly, lw, lh = 140, 230, 760, 540
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    # Water surface line
    water_y = ly + 340
    d.rectangle([lx + 30, water_y, lx + lw - 30, ly + lh - 40],
                fill=ACCENT_LT)
    # Surface ripple
    d.line([(lx + 30, water_y), (lx + lw - 30, water_y)],
           fill=ACCENT, width=4)
    # Ice cube partially above the line
    cube_w = 180
    cube_cx = lx + lw // 2
    d.polygon([
        (cube_cx - cube_w // 2, water_y - 90),
        (cube_cx + cube_w // 2, water_y - 90),
        (cube_cx + cube_w // 2 + 30, water_y + 40),
        (cube_cx - cube_w // 2 + 30, water_y + 40),
    ], fill=(235, 245, 250), outline=MAROON_DARK, width=4)
    # Top face
    d.polygon([
        (cube_cx - cube_w // 2, water_y - 90),
        (cube_cx + cube_w // 2, water_y - 90),
        (cube_cx + cube_w // 2 + 30, water_y - 60),
        (cube_cx - cube_w // 2 + 30, water_y - 60),
    ], fill=(250, 252, 255), outline=MAROON_DARK, width=4)
    # Caption
    centered_x = lx + lw // 2
    cap = "Why does ice float?"
    cf = font("serif_bold", 38)
    tw = d.textlength(cap, font=cf)
    d.text((centered_x - tw / 2, ly + 40), cap, fill=MAROON_DARK, font=cf)
    sub = "Solids almost always sink in their own liquid."
    sf = font("sans", 26)
    tw2 = d.textlength(sub, font=sf)
    d.text((centered_x - tw2 / 2, ly + 100), sub, fill=MUTED, font=sf)

    # Right panel: tree with water climbing up
    rx, ry, rw, rh = 1020, 230, 760, 540
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    cap2 = "Why does water climb a tree?"
    tw3 = d.textlength(cap2, font=cf)
    d.text((rx + rw // 2 - tw3 / 2, ry + 40), cap2,
           fill=MAROON_DARK, font=cf)
    sub2 = "100 feet up the trunk, against gravity."
    tw4 = d.textlength(sub2, font=sf)
    d.text((rx + rw // 2 - tw4 / 2, ry + 100), sub2, fill=MUTED, font=sf)

    # Tree trunk
    trunk_cx = rx + rw // 2
    trunk_top = ry + 180
    trunk_bot = ry + rh - 50
    d.rectangle([trunk_cx - 40, trunk_top, trunk_cx + 40, trunk_bot],
                fill=(120, 80, 50), outline=MAROON_DARK, width=3)
    # Leaf canopy
    d.ellipse([trunk_cx - 170, trunk_top - 110, trunk_cx + 170, trunk_top + 70],
              fill=(70, 140, 90), outline=MAROON_DARK, width=3)
    # Water droplets climbing up trunk
    for i, dy in enumerate([60, 130, 200, 270]):
        y_drop = trunk_bot - dy
        d.ellipse([trunk_cx - 10, y_drop - 10, trunk_cx + 10, y_drop + 10],
                  fill=ACCENT_LT, outline=ACCENT, width=2)
        # Up arrow next to it
        d.polygon([
            (trunk_cx + 60, y_drop),
            (trunk_cx + 78, y_drop + 10),
            (trunk_cx + 78, y_drop - 10),
        ], fill=ACCENT)

    # Bottom punchline strip
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Both answers come from one tiny feature of the water molecule.",
             font("serif_bold", 38), 850, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Water and carbon — the chemistry that makes life possible.",
    "The four macromolecules — carbs, lipids, proteins, nucleic acids.",
    "Build and break — dehydration synthesis vs. hydrolysis.",
], footnote="By the end: you can name any molecule's monomer and reaction.")


# 04 — elements of life
deck.definition("04_elements_of_life",
                "Elements of life.",
                "C · H · O · N  =  96% of living matter (by mass)",
                sub="Add P and S → CHNOPS.  ~25 elements total are essential to life.")


# 05 — bonds compare (3-way custom because slide_kit.compare is 2-column)
def bonds_compare(img, d):
    d.text((110, 80), "Three bond types you must know.",
           fill=MAROON, font=font("serif_bold", 60))

    cols = [
        ("COVALENT", "Share electrons", [
            "Strong.",
            "C–C, C–H,",
            "peptide bonds.",
            "",
            "Polar (O–H)",
            "vs. nonpolar (C–H).",
        ], "100% strength", ACCENT),
        ("IONIC", "Transfer electrons", [
            "Medium.",
            "Opposite charges",
            "attract.",
            "",
            "Weakens in water.",
            "(NaCl dissolves)",
        ], "Medium strength", MAROON),
        ("HYDROGEN", "Donor + acceptor", [
            "Weak alone,",
            "strong in bulk.",
            "",
            "DONOR: H on N/O/F",
            "ACCEPTOR: N/O/F",
            "with a lone pair.",
        ], "~5% of covalent", ACCENT),
    ]

    col_w = 540
    col_h = 600
    gap = 30
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 220
    for i, (name, sub, lines, foot, color) in enumerate(cols):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=20,
                            outline=color, width=5, fill=CARD)
        d.text((x + 26, y0 + 24), name, fill=color,
               font=font("serif_bold", 44))
        d.text((x + 26, y0 + 88), sub, fill=MUTED,
               font=font("sans_bold", 28))
        ly = y0 + 160
        for ln in lines:
            d.text((x + 26, ly), ln, fill=INK, font=font("sans", 28))
            ly += 50
        d.text((x + 26, y0 + col_h - 50), foot, fill=color,
               font=font("sans_bold", 26))

    # Bottom note on polar vs nonpolar
    d.rounded_rectangle([110, 870, W - 110, 970], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Polar covalent: electrons shared unequally (O–H).  Nonpolar covalent: shared equally (C–H).",
             font("sans_bold", 28), 900, MAROON_DARK)
deck.custom("05_bonds_compare", bonds_compare)


# 06 — water properties (custom: water molecule diagram + 6 properties)
def water_properties(img, d):
    d.text((110, 70), "Water is polar.  That changes everything.",
           fill=MAROON, font=font("serif_bold", 56))

    # Water molecule diagram (left side)
    mx, my = 380, 480
    # Bent geometry: O at center, two H below-left and below-right
    o_r = 90
    h_r = 55
    angle_offset = math.radians(52)  # half of ~104.5°
    h_dist = 180
    h1 = (mx - h_dist * math.sin(angle_offset),
          my + h_dist * math.cos(angle_offset))
    h2 = (mx + h_dist * math.sin(angle_offset),
          my + h_dist * math.cos(angle_offset))
    # Bonds
    d.line([(mx, my), h1], fill=MAROON_DARK, width=8)
    d.line([(mx, my), h2], fill=MAROON_DARK, width=8)
    # O atom
    d.ellipse([mx - o_r, my - o_r, mx + o_r, my + o_r],
              fill=RED, outline=MAROON_DARK, width=4)
    centered_o = "O"
    of = font("serif_bold", 80)
    tw_o = d.textlength(centered_o, font=of)
    d.text((mx - tw_o / 2, my - 50), centered_o, fill=CREAM, font=of)
    # δ- on oxygen
    d.text((mx + 100, my - 100), "δ−", fill=RED, font=font("sans_bold", 44))
    # H atoms
    for hx, hy in [h1, h2]:
        d.ellipse([hx - h_r, hy - h_r, hx + h_r, hy + h_r],
                  fill=ACCENT_LT, outline=MAROON_DARK, width=4)
        hf = font("serif_bold", 56)
        tw_h = d.textlength("H", font=hf)
        d.text((hx - tw_h / 2, hy - 35), "H", fill=MAROON_DARK, font=hf)
    # δ+ labels near each H
    d.text((h1[0] - 90, h1[1] + 30), "δ+", fill=ACCENT,
           font=font("sans_bold", 44))
    d.text((h2[0] + 50, h2[1] + 30), "δ+", fill=ACCENT,
           font=font("sans_bold", 44))
    # Angle annotation
    d.text((mx - 80, my + 240), "~104.5°", fill=MUTED,
           font=font("sans_bold", 32))
    # Caption under molecule
    centered_cap = "Bent  ·  polar"
    cf = font("serif_bold", 36)
    tw_c = d.textlength(centered_cap, font=cf)
    d.text((mx - tw_c / 2, my + 300), centered_cap,
           fill=MAROON_DARK, font=cf)

    # Right side: 6 properties
    rx = 820
    ry = 200
    d.text((rx, ry), "6 emergent properties:",
           fill=MAROON, font=font("serif_bold", 40))
    props = [
        ("Cohesion", "water sticks to water"),
        ("Adhesion", "water sticks to other surfaces"),
        ("High specific heat", "stable temperatures"),
        ("High heat of vaporization", "evaporative cooling"),
        ("Ice less dense", "ice floats on water"),
        ("Versatile solvent", "polar + ionic only"),
    ]
    py = ry + 70
    for name, sub in props:
        d.ellipse([rx, py + 14, rx + 18, py + 32], fill=ACCENT)
        d.text((rx + 40, py), name, fill=INK, font=font("sans_bold", 30))
        d.text((rx + 40, py + 40), sub, fill=MUTED, font=font("sans", 24))
        py += 90

    # Bottom warning strip
    d.rounded_rectangle([110, 900, W - 110, 1000], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Water does NOT dissolve nonpolar substances → they get pushed together (hydrophobic effect).",
             font("sans_bold", 28), 930, MAROON_DARK)
deck.custom("06_water_properties", water_properties)


# 07 — water examples (custom: 5 examples mapped to properties)
def water_examples(img, d):
    d.text((110, 80), "Water properties → real biology.",
           fill=MAROON, font=font("serif_bold", 60))

    examples = [
        ("Trees pull water up the xylem",
         "cohesion + adhesion → capillary action",
         "TREE"),
        ("Sweating cools you down",
         "high heat of vaporization → evaporation removes heat",
         "SWEAT"),
        ("Lakes freeze top-down",
         "ice is less dense → it floats and insulates the fish below",
         "ICE"),
        ("Salt (NaCl) dissolves in water",
         "versatile solvent → hydration shells around each ion",
         "SALT"),
        ("Your body holds 98.6 °F",
         "high specific heat → resists temperature swings",
         "BODY"),
    ]
    y = 220
    for i, (head, sub, tag) in enumerate(examples):
        # Tag circle on left
        cx, cy = 180, y + 50
        d.ellipse([cx - 60, cy - 60, cx + 60, cy + 60],
                  fill=ACCENT_LT, outline=ACCENT, width=4)
        tf = font("sans_bold", 24)
        tw = d.textlength(tag, font=tf)
        d.text((cx - tw / 2, cy - 13), tag, fill=MAROON_DARK, font=tf)
        # Head + sub
        d.text((280, y + 8), head, fill=INK, font=font("sans_bold", 34))
        d.text((280, y + 60), sub, fill=ACCENT, font=font("sans", 28))
        y += 140
deck.custom("07_water_examples", water_examples)


# 08 — carbon chemistry (custom: functional groups table)
def carbon_chem(img, d):
    d.text((110, 70), "Carbon  +  7 functional groups.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160),
           "4 valence electrons → 4 covalent bonds.  Single + double bonds.  Straight / branched / ring.",
           fill=MUTED, font=font("sans", 28))

    # Table layout
    headers = [("GROUP", 130), ("FORMULA", 470), ("PROPERTY", 800),
               ("WHERE YOU SEE IT", 1240)]
    header_y = 230
    d.rectangle([110, header_y, W - 110, header_y + 60], fill=ACCENT)
    for label, x in headers:
        d.text((x, header_y + 14), label, fill=CREAM,
               font=font("sans_bold", 28))

    rows = [
        ("Hydroxyl",  "–OH",        "polar (H-bonds)",      "sugars, serine"),
        ("Carbonyl",  "C=O",        "polar",                "peptide bonds"),
        ("Carboxyl",  "–COOH",      "acidic, –COO⁻ at pH 7","amino acids, fatty acids"),
        ("Amino",     "–NH₂",       "basic, –NH₃⁺ at pH 7", "amino acids"),
        ("Sulfhydryl","–SH",        "forms –S–S– bridges",  "cysteine (tertiary)"),
        ("Phosphate", "–OPO₃²⁻",    "strongly negative",    "nucleotides, ATP, phospholipids"),
        ("Methyl",    "–CH₃",       "nonpolar / hydrophobic","DNA + protein methylation"),
    ]
    row_h = 80
    y = header_y + 60
    for i, (name, formula, prop, where) in enumerate(rows):
        bg = CARD if i % 2 == 0 else ACCENT_LT
        d.rectangle([110, y, W - 110, y + row_h], fill=bg)
        d.text((130, y + 24), name, fill=MAROON_DARK,
               font=font("sans_bold", 30))
        d.text((470, y + 24), formula, fill=INK, font=font("mono", 30))
        d.text((800, y + 24), prop, fill=INK, font=font("sans", 26))
        d.text((1240, y + 24), where, fill=MUTED,
               font=font("serif_ital", 26))
        y += row_h
    # Border
    d.rectangle([110, header_y, W - 110, y], outline=MAROON, width=4)
deck.custom("08_carbon_chemistry", carbon_chem)


# 09 — dehydration synthesis / hydrolysis (equation slide)
deck.equation("09_dehydration_hydrolysis",
              "Build  and  break  — the two reactions.",
              [
                  ("monomer + monomer  →  polymer + H₂O", ACCENT,
                   "DEHYDRATION SYNTHESIS — remove water to build"),
                  ("polymer + H₂O  →  monomer + monomer", MAROON,
                   "HYDROLYSIS — add water to break"),
                  ("(lipids: NOT polymers, but STILL built by dehydration)",
                   MUTED, None),
              ])


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Protein digestion breaks a polypeptide into amino acids.  Then: a ribosome builds a new protein.",
           "Which reaction?  Water consumed or released?",
           hint="Pause now. Solve it. Press play when you're ready.")

# 11 — duplicate the pause slide for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — carbohydrates + lipids (custom — half/half)
def carbs_lipids(img, d):
    d.text((110, 70), "Carbohydrates  +  Lipids.",
           fill=MAROON, font=font("serif_bold", 60))

    # Left: carbs
    lx, ly = 110, 180
    lw, lh = 880, 770
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=22,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "CARBOHYDRATES", fill=ACCENT,
           font=font("sans_bold", 40))
    d.text((lx + 30, ly + 80), "Monomer: monosaccharide  (glucose C₆H₁₂O₆)",
           fill=INK, font=font("sans", 28))
    d.text((lx + 30, ly + 130), "Disaccharides: sucrose, lactose, maltose",
           fill=INK, font=font("sans", 28))
    d.text((lx + 30, ly + 200), "Polysaccharides — same monomer, different bond:",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    carb_rows = [
        ("Starch",    "α-1,4 bonds",  "plant storage · digestible"),
        ("Glycogen",  "α-1,4 + α-1,6", "animal storage (liver/muscle)"),
        ("Cellulose", "β-1,4 bonds",  "plant cell wall · we CAN'T digest"),
        ("Chitin",    "mod. β-glucose","fungi + arthropods"),
    ]
    cy = ly + 260
    for name, bond, role in carb_rows:
        d.rounded_rectangle([lx + 30, cy, lx + lw - 30, cy + 100],
                            radius=14, outline=ACCENT, width=3,
                            fill=ACCENT_LT)
        d.text((lx + 50, cy + 8), name, fill=MAROON_DARK,
               font=font("sans_bold", 30))
        d.text((lx + 50, cy + 50), bond, fill=ACCENT,
               font=font("mono", 24))
        d.text((lx + 350, cy + 30), role, fill=INK,
               font=font("sans", 24))
        cy += 115

    # Right: lipids
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=22,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "LIPIDS", fill=MAROON_DARK,
           font=font("sans_bold", 40))
    d.text((rx + 30, ly + 80), "NOT true polymers — but built by dehydration",
           fill=INK, font=font("sans", 26))

    # Saturated vs unsaturated geometry
    d.text((rx + 30, ly + 150), "Triglyceride = glycerol + 3 fatty acids",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 30, ly + 200), "Saturated  →  no C=C, packs tight  →  SOLID",
           fill=INK, font=font("sans", 26))
    d.text((rx + 30, ly + 240), "Unsaturated → C=C kinks, can't pack → LIQUID",
           fill=INK, font=font("sans", 26))

    # Visual: straight chain vs kinked chain
    sx = rx + 50
    sy = ly + 310
    # Straight chain (saturated)
    d.text((sx, sy), "Saturated:", fill=MUTED, font=font("sans_bold", 22))
    chain_y = sy + 38
    px = sx + 130
    for i in range(8):
        d.line([(px + i * 36, chain_y), (px + (i + 1) * 36, chain_y)],
               fill=MAROON_DARK, width=4)
    d.ellipse([px - 10, chain_y - 10, px + 10, chain_y + 10],
              fill=ACCENT)
    # Unsaturated chain (with a kink)
    sy2 = sy + 80
    d.text((sx, sy2), "Unsaturated:", fill=MUTED,
           font=font("sans_bold", 22))
    chain_y2 = sy2 + 38
    px2 = sx + 130
    # First half flat, then kink up
    for i in range(4):
        d.line([(px2 + i * 36, chain_y2),
                (px2 + (i + 1) * 36, chain_y2)],
               fill=MAROON_DARK, width=4)
    # Kink
    kink_x = px2 + 4 * 36
    d.line([(kink_x, chain_y2), (kink_x + 36, chain_y2 - 30)],
           fill=MAROON_DARK, width=4)
    d.line([(kink_x + 36, chain_y2 - 30), (kink_x + 72, chain_y2 - 30)],
           fill=MAROON_DARK, width=4)
    d.line([(kink_x + 72, chain_y2 - 30), (kink_x + 108, chain_y2)],
           fill=MAROON_DARK, width=4)
    d.ellipse([px2 - 10, chain_y2 - 10, px2 + 10, chain_y2 + 10],
              fill=ACCENT)

    # Phospholipid + steroid notes
    d.text((rx + 30, ly + 510),
           "Phospholipid: hydrophilic HEAD + 2 hydrophobic TAILS",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 30, ly + 550),
           "→ amphipathic → forms the lipid BILAYER of every cell membrane",
           fill=INK, font=font("sans", 24))
    d.text((rx + 30, ly + 620),
           "Steroids: 4 fused rings  (cholesterol, testosterone, estrogen)",
           fill=INK, font=font("sans", 26))

    # Tiny phospholipid drawing
    plx = rx + 30
    ply = ly + 680
    head_r = 18
    d.ellipse([plx, ply, plx + head_r * 2, ply + head_r * 2],
              fill=ACCENT, outline=MAROON_DARK, width=2)
    d.ellipse([plx + 50, ply, plx + 50 + head_r * 2, ply + head_r * 2],
              fill=ACCENT, outline=MAROON_DARK, width=2)
    for tx in (plx + 8, plx + 58):
        d.line([(tx + 10, ply + 36), (tx + 10, ply + 70)],
               fill=MAROON_DARK, width=4)
        d.line([(tx + 10, ply + 36), (tx + 24, ply + 70)],
               fill=MAROON_DARK, width=4)
    d.text((plx + 130, ply + 20),
           "head (loves water)  ·  tails (avoid water)",
           fill=MUTED, font=font("sans", 22))
deck.custom("12_carbs_lipids", carbs_lipids)


# 13 — proteins (custom)
def proteins(img, d):
    d.text((110, 70), "Proteins  —  20 amino acids, 4 levels of folding.",
           fill=MAROON, font=font("serif_bold", 50))

    # Amino acid skeleton row
    d.rounded_rectangle([110, 160, W - 110, 280], radius=18,
                        outline=ACCENT, width=4, fill=ACCENT_LT)
    d.text((140, 180), "Amino acid:", fill=MAROON_DARK,
           font=font("sans_bold", 30))
    d.text((140, 220),
           "α-carbon  +  –NH₂  +  –COOH  +  H  +  R-group",
           fill=INK, font=font("mono", 32))
    d.text((1280, 220), "linked by PEPTIDE BONDS", fill=ACCENT,
           font=font("sans_bold", 28))

    # Four levels — each in its own card
    levels = [
        ("1°  Primary",
         "Linear sequence of amino acids.",
         "Held by:  peptide (covalent) bonds."),
        ("2°  Secondary",
         "α-helix  +  β-pleated sheet.",
         "Held by:  BACKBONE H-bonds (not R-groups)."),
        ("3°  Tertiary",
         "Overall 3D fold from R-group interactions.",
         "H-bonds · ionic · disulfide · hydrophobic effect."),
        ("4°  Quaternary",
         "Multiple subunits assembled.",
         "Hemoglobin = 4 subunits."),
    ]
    box_w = 870
    box_h = 175
    gap = 20
    grid_x = 110
    grid_y = 320
    for i, (head, body, foot) in enumerate(levels):
        col = i % 2
        row = i // 2
        bx = grid_x + col * (box_w + gap)
        by = grid_y + row * (box_h + gap)
        d.rounded_rectangle([bx, by, bx + box_w, by + box_h],
                            radius=16, outline=ACCENT, width=4,
                            fill=CARD)
        d.text((bx + 24, by + 16), head, fill=ACCENT,
               font=font("sans_bold", 34))
        d.text((bx + 24, by + 70), body, fill=INK,
               font=font("sans", 26))
        d.text((bx + 24, by + 115), foot, fill=MAROON_DARK,
               font=font("sans_bold", 24))

    # Bottom: denaturation + functions
    d.rounded_rectangle([110, 730, W - 110, 970], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((140, 750), "Denaturation",
           fill=MAROON_DARK, font=font("serif_bold", 38))
    d.text((140, 810),
           "Heat / pH / salt disrupt 2°/3°/4°  →  shape lost  →  function lost.",
           fill=INK, font=font("sans", 28))
    d.text((140, 855),
           "But peptide bonds (primary sequence) are NOT broken.",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((140, 910),
           "Functions: enzymes · collagen + keratin · hemoglobin · antibodies · signaling · motor",
           fill=ACCENT, font=font("sans_bold", 26))
deck.custom("13_proteins", proteins)


# 14 — nucleic acids (custom)
def nucleic_acids(img, d):
    d.text((110, 70), "Nucleic acids  —  the information molecules.",
           fill=MAROON, font=font("serif_bold", 54))

    # Top strip: nucleotide = sugar + phosphate + base
    d.rounded_rectangle([110, 160, W - 110, 270], radius=18,
                        outline=ACCENT, width=4, fill=ACCENT_LT)
    centered(d, "Nucleotide  =  sugar  +  phosphate  +  nitrogenous base",
             font("sans_bold", 38), 195, MAROON_DARK)
    centered(d, "Nucleotides link by PHOSPHODIESTER BONDS  (3′ –OH  +  5′ phosphate, releases H₂O)",
             font("sans", 28), 240, INK)

    # Left card: DNA features
    lx, ly = 110, 310
    lw, lh = 870, 470
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "DNA", fill=ACCENT,
           font=font("sans_bold", 44))
    d.text((lx + 30, ly + 80), "deoxyribose  ·  double-stranded",
           fill=INK, font=font("sans", 30))
    d.text((lx + 30, ly + 130), "bases:  A · T · G · C",
           fill=INK, font=font("sans", 30))
    d.text((lx + 30, ly + 190), "ANTIPARALLEL strands",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((lx + 30, ly + 230), "one runs 5′ → 3′,  partner 3′ → 5′",
           fill=MUTED, font=font("sans", 26))
    d.text((lx + 30, ly + 290), "Backbone OUTSIDE  ·  bases INSIDE",
           fill=MAROON_DARK, font=font("sans_bold", 30))
    d.text((lx + 30, ly + 360), "A=T  (2 H-bonds)    G≡C  (3 H-bonds)",
           fill=ACCENT, font=font("mono", 30))
    d.text((lx + 30, ly + 410), "GC-rich  →  more stable",
           fill=MUTED, font=font("serif_ital", 26))

    # Right card: simple ladder diagram + RNA + ATP
    rx = lx + lw + 30
    rw = W - 110 - rx
    rh = lh
    d.rounded_rectangle([rx, ly, rx + rw, ly + rh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "Structure", fill=MAROON_DARK,
           font=font("sans_bold", 38))
    # Mini ladder
    ladder_x = rx + 60
    ladder_top = ly + 90
    rung_count = 6
    rung_h = 36
    # Two backbone lines
    d.line([(ladder_x, ladder_top), (ladder_x, ladder_top + rung_count * rung_h)],
           fill=MAROON_DARK, width=6)
    d.line([(ladder_x + 200, ladder_top),
            (ladder_x + 200, ladder_top + rung_count * rung_h)],
           fill=MAROON_DARK, width=6)
    bases = ["A=T", "T=A", "G≡C", "C≡G", "A=T", "G≡C"]
    bf = font("mono", 22)
    for i, b in enumerate(bases):
        ry_rung = ladder_top + i * rung_h + rung_h // 2
        d.line([(ladder_x, ry_rung), (ladder_x + 200, ry_rung)],
               fill=ACCENT, width=3)
        tw = d.textlength(b, font=bf)
        d.text((ladder_x + 100 - tw / 2, ry_rung - 14),
               b, fill=MAROON_DARK, font=bf)
    # 5' / 3' labels
    d.text((ladder_x - 50, ladder_top - 30), "5′",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((ladder_x - 50, ladder_top + rung_count * rung_h),
           "3′", fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((ladder_x + 210, ladder_top - 30), "3′",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((ladder_x + 210, ladder_top + rung_count * rung_h),
           "5′", fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((ladder_x - 30, ladder_top + rung_count * rung_h + 40),
           "antiparallel", fill=MUTED, font=font("serif_ital", 22))

    # RNA + ATP side notes
    nx = rx + 380
    d.text((nx, ly + 90), "RNA", fill=ACCENT,
           font=font("sans_bold", 36))
    d.text((nx, ly + 140), "ribose  ·  single strand",
           fill=INK, font=font("sans", 26))
    d.text((nx, ly + 175), "bases:  A · U · G · C",
           fill=INK, font=font("sans", 26))
    d.text((nx, ly + 260), "ATP", fill=ACCENT,
           font=font("sans_bold", 36))
    d.text((nx, ly + 310), "is also a nucleotide —",
           fill=INK, font=font("sans", 26))
    d.text((nx, ly + 345), "the cell's energy currency.",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # Bottom rule strip
    d.rounded_rectangle([110, 820, W - 110, 940], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Function: store + transmit genetic information.",
             font("serif_bold", 38), 850, MAROON_DARK)
deck.custom("14_nucleic_acids", nucleic_acids)


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Water is polar → 6 properties; dissolves polar/ionic, excludes nonpolar (hydrophobic effect).",
    "Carbon: 4 bonds + 7 functional groups → molecular diversity.",
    "4 macromolecules: carbs, lipids, proteins, nucleic acids — only lipids aren't polymers.",
    "Proteins: 4 levels — 1° peptide, 2° backbone H-bonds, 3° R-groups, 4° subunits.",
    "Dehydration synthesis BUILDS (removes H₂O).  Hydrolysis BREAKS (adds H₂O).",
], assignment=[
    "1.  Label the functional groups on a given amino acid; predict charge at physiological pH.",
    "2.  Pick 2 properties of water and give a biological example of each.",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapters 2 and 3 — atoms, water, carbon, macromolecules"),
    ("2.", "Khan Academy AP Bio",     "Unit 1 problem sets — water, macromolecules, functional groups"),
    ("3.", "Assignment in dashboard", "Functional groups + water properties (above)"),
    ("4.", "Advisor check-in",        "If functional groups or protein folding still feel fuzzy"),
], next_text="Next up:  Module 2 — Cell Structure.")


print("AP Biology Module 1 slides built.")

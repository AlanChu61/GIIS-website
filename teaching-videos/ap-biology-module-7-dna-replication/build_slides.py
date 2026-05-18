"""AP Biology · Module 7 — DNA Structure and Replication.

Teal (science) theme auto-resolved from "AP Biology". 16 slides total.
Heavy on customs because the double helix, base-pairing rungs, replication
fork with leading/lagging strands, and telomere shortening each need real
diagrams. Pause slide (10) is duplicated to 11 so the same image plays
during both Q and A.
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
deck = Deck(course="AP Biology", module_num=7, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 7 — DNA Structure and Replication",
           "Sample lesson  ·  ~8 minutes")


# 02 — hook: 2 meters of DNA + error rate
def hook(img, d):
    d.text((110, 80), "Two meters of DNA. One error per billion bases.",
           fill=MAROON, font=font("serif_bold", 56))

    # Left panel: 2 meters
    lx, ly, lw, lh = 140, 230, 760, 540
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    big = "2  meters"
    bf = font("serif_bold", 130)
    tw = d.textlength(big, font=bf)
    d.text((lx + lw // 2 - tw / 2, ly + 110), big,
           fill=MAROON_DARK, font=bf)
    cap = "of DNA  ·  in every cell"
    cf = font("serif_bold", 40)
    tw2 = d.textlength(cap, font=cf)
    d.text((lx + lw // 2 - tw2 / 2, ly + 290), cap,
           fill=ACCENT, font=cf)
    sub = "Packed into a nucleus 6 microns across."
    sf = font("sans", 28)
    tw3 = d.textlength(sub, font=sf)
    d.text((lx + lw // 2 - tw3 / 2, ly + 380), sub,
           fill=MUTED, font=sf)
    sub2 = "(roughly 3 billion base pairs)"
    sf2 = font("serif_ital", 26)
    tw4 = d.textlength(sub2, font=sf2)
    d.text((lx + lw // 2 - tw4 / 2, ly + 430), sub2,
           fill=MUTED, font=sf2)

    # Right panel: error rate
    rx, ry, rw, rh = 1020, 230, 760, 540
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    cap2 = "Copied with"
    tw5 = d.textlength(cap2, font=cf)
    d.text((rx + rw // 2 - tw5 / 2, ry + 60), cap2,
           fill=MAROON_DARK, font=cf)

    err = "1 error"
    ef = font("serif_bold", 110)
    tw6 = d.textlength(err, font=ef)
    d.text((rx + rw // 2 - tw6 / 2, ry + 150), err,
           fill=MAROON, font=ef)
    err2 = "per  1,000,000,000  bases"
    ef2 = font("sans_bold", 36)
    tw7 = d.textlength(err2, font=ef2)
    d.text((rx + rw // 2 - tw7 / 2, ry + 290), err2,
           fill=ACCENT, font=ef2)
    sub3 = "How?  An assembly line of about 7 proteins."
    sf3 = font("serif_ital", 28)
    tw8 = d.textlength(sub3, font=sf3)
    d.text((rx + rw // 2 - tw8 / 2, ry + 400), sub3,
           fill=MUTED, font=sf3)

    # Bottom punchline strip
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Today: the molecular machinery that makes that accuracy possible.",
             font("serif_bold", 36), 850, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "DNA structure — double helix, antiparallel, base pairing.",
    "Replication — semiconservative, the enzymes, leading vs. lagging.",
    "Proofreading, repair, and the telomere problem.",
], footnote="By the end:  you can list the 7 enzymes of replication in order.")


# 04 — DNA structure (custom: double helix diagram + key facts)
def dna_structure(img, d):
    d.text((110, 70), "DNA  —  the double helix.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 160),
           "Watson & Crick, 1953  ·  using Rosalind Franklin's X-ray data.",
           fill=ACCENT, font=font("sans_bold", 32))

    # Left side: double helix drawing
    lx, ly = 140, 220
    lw, lh = 700, 740
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=24,
                        outline=ACCENT, width=5, fill=CARD)

    # Draw two sine-wave strands twisting around each other
    cx = lx + lw // 2
    top_y = ly + 60
    bot_y = ly + lh - 60
    n_steps = 60
    amp = 130
    freq = 2.5  # number of full twists down the column
    left_pts = []
    right_pts = []
    for i in range(n_steps + 1):
        t = i / n_steps
        y = top_y + t * (bot_y - top_y)
        phase = t * freq * 2 * math.pi
        x_l = cx + amp * math.sin(phase)
        x_r = cx - amp * math.sin(phase)
        left_pts.append((x_l, y))
        right_pts.append((x_r, y))

    # Rungs (base pairs) at intervals
    rung_step = 4
    for i in range(0, n_steps + 1, rung_step):
        # Color: alternate A-T (red-ish) and G-C (accent)
        col = MAROON if (i // rung_step) % 2 == 0 else ACCENT
        d.line([left_pts[i], right_pts[i]], fill=col, width=4)

    # Two backbones drawn after rungs so they're on top
    for i in range(len(left_pts) - 1):
        d.line([left_pts[i], left_pts[i + 1]], fill=MAROON_DARK, width=6)
        d.line([right_pts[i], right_pts[i + 1]], fill=MAROON_DARK, width=6)

    # Labels: 5' and 3' ends
    d.text((lx + 30, top_y - 30), "5'", fill=ACCENT,
           font=font("serif_bold", 38))
    d.text((lx + lw - 60, top_y - 30), "3'", fill=ACCENT,
           font=font("serif_bold", 38))
    d.text((lx + 30, bot_y + 10), "3'", fill=ACCENT,
           font=font("serif_bold", 38))
    d.text((lx + lw - 60, bot_y + 10), "5'", fill=ACCENT,
           font=font("serif_bold", 38))

    # Arrow showing antiparallel directions
    d.text((lx + 20, ly + lh // 2 - 100), "↓", fill=MAROON_DARK,
           font=font("serif_bold", 50))
    d.text((lx + lw - 50, ly + lh // 2 - 100), "↑", fill=MAROON_DARK,
           font=font("serif_bold", 50))

    # Right side: key facts panel
    rx = lx + lw + 40
    rw = W - 110 - rx
    rh = 740
    d.rounded_rectangle([rx, ly, rx + rw, ly + rh], radius=24,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((rx + 30, ly + 30), "Key features",
           fill=MAROON_DARK, font=font("serif_bold", 48))

    facts = [
        ("Backbone", "Sugar (deoxyribose) + phosphate"),
        ("Bases", "Stick inward, pair across"),
        ("Antiparallel", "One strand 5'→3', other 3'→5'"),
        ("Grooves", "Major & minor — proteins read here"),
        ("Diameter", "2 nm — uniform along whole length"),
    ]
    fy = ly + 120
    for label, body in facts:
        d.text((rx + 30, fy), label, fill=ACCENT,
               font=font("sans_bold", 32))
        d.text((rx + 30, fy + 45), body, fill=INK,
               font=font("sans", 26))
        fy += 115

    # Bottom strip — credit Rosalind Franklin
    d.rounded_rectangle([110, 990, W - 110, 1060], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Franklin's Photo 51 was the X-ray that revealed the helix — Watson & Crick saw it before publishing.",
             font("serif_ital", 26), 1010, MAROON_DARK)
deck.custom("04_dna_structure", dna_structure)


# 05 — Chargaff + base pairing (custom: A-T and G-C base-pair diagrams)
def base_pairing(img, d):
    d.text((110, 70), "Chargaff  +  base pairing.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 160),
           "%A = %T   and   %G = %C   ·  in any double-stranded DNA.",
           fill=ACCENT, font=font("sans_bold", 34))

    # Left: A-T pair (2 H-bonds)
    lx, ly = 140, 240
    lw, lh = 760, 560
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=24,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "A   —   T",
           fill=MAROON_DARK, font=font("serif_bold", 80))
    d.text((lx + 30, ly + 130), "Adenine  ·  Thymine",
           fill=ACCENT, font=font("sans_bold", 32))

    # Two base hexagons + 2 H-bonds between them
    bx_left = lx + 150
    bx_right = lx + lw - 290
    by = ly + 320
    bw = 140
    # Left base (A)
    d.rounded_rectangle([bx_left, by - 60, bx_left + bw, by + 60], radius=14,
                        outline=MAROON_DARK, width=4, fill=ACCENT_LT)
    d.text((bx_left + 50, by - 35), "A", fill=MAROON_DARK,
           font=font("serif_bold", 72))
    # Right base (T)
    d.rounded_rectangle([bx_right, by - 60, bx_right + bw, by + 60], radius=14,
                        outline=MAROON_DARK, width=4, fill=ACCENT_LT)
    d.text((bx_right + 50, by - 35), "T", fill=MAROON_DARK,
           font=font("serif_bold", 72))
    # Two H-bonds (dashed lines)
    for off in [-20, 20]:
        # Dashed line
        x0 = bx_left + bw
        x1 = bx_right
        for seg in range(0, int(x1 - x0), 16):
            d.line([(x0 + seg, by + off), (x0 + seg + 8, by + off)],
                   fill=MAROON, width=4)

    d.text((lx + 30, ly + 450), "2 hydrogen bonds",
           fill=MAROON, font=font("serif_bold", 38))

    # Right: G-C pair (3 H-bonds)
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=24,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "G   —   C",
           fill=MAROON_DARK, font=font("serif_bold", 80))
    d.text((rx + 30, ly + 130), "Guanine  ·  Cytosine",
           fill=ACCENT, font=font("sans_bold", 32))

    bx_left2 = rx + 150
    bx_right2 = rx + rw - 290
    by2 = ly + 320
    d.rounded_rectangle([bx_left2, by2 - 60, bx_left2 + bw, by2 + 60], radius=14,
                        outline=MAROON_DARK, width=4, fill=ACCENT_LT)
    d.text((bx_left2 + 50, by2 - 35), "G", fill=MAROON_DARK,
           font=font("serif_bold", 72))
    d.rounded_rectangle([bx_right2, by2 - 60, bx_right2 + bw, by2 + 60], radius=14,
                        outline=MAROON_DARK, width=4, fill=ACCENT_LT)
    d.text((bx_right2 + 50, by2 - 35), "C", fill=MAROON_DARK,
           font=font("serif_bold", 72))
    # Three H-bonds
    for off in [-30, 0, 30]:
        x0 = bx_left2 + bw
        x1 = bx_right2
        for seg in range(0, int(x1 - x0), 16):
            d.line([(x0 + seg, by2 + off), (x0 + seg + 8, by2 + off)],
                   fill=MAROON, width=4)

    d.text((rx + 30, ly + 450), "3 hydrogen bonds",
           fill=MAROON, font=font("serif_bold", 38))

    # Bottom strip
    d.rounded_rectangle([110, 830, W - 110, 950], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "G-C rich regions are harder to pull apart — relevant when helicase tries to unwind.",
             font("sans_bold", 30), 855, MAROON_DARK)
    centered(d, "Purines (A, G) always pair with pyrimidines (T, C) → uniform 2 nm helix width.",
             font("serif_ital", 26), 905, MUTED)
deck.custom("05_chargaff_base_pairing", base_pairing)


# 06 — semiconservative (custom: Meselson-Stahl 3 generations)
def semiconservative(img, d):
    d.text((110, 70), "Semiconservative  —  Meselson & Stahl, 1958.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Each daughter helix has ONE old strand + ONE new strand.",
           fill=ACCENT, font=font("sans_bold", 32))

    # Three generation columns
    col_w = 540
    col_h = 720
    gap = 30
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 220

    generations = [
        ("PARENT",
         [("heavy", "heavy")],
         "Grown in heavy nitrogen (¹⁵N)"),
        ("1 GENERATION",
         [("heavy", "light"), ("heavy", "light")],
         "All hybrid — proves NOT conservative"),
        ("2 GENERATIONS",
         [("heavy", "light"), ("light", "light"),
          ("heavy", "light"), ("light", "light")],
         "Half hybrid, half light — proves NOT dispersive"),
    ]

    for i, (label, helices, caption) in enumerate(generations):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=20,
                            outline=ACCENT, width=5, fill=CARD)
        # Header
        d.rectangle([x, y0, x + col_w, y0 + 70], fill=ACCENT)
        cf = font("sans_bold", 32)
        tw = d.textlength(label, font=cf)
        d.text((x + col_w // 2 - tw / 2, y0 + 18), label,
               fill=CREAM, font=cf)

        # Draw helices in the column
        n_helices = len(helices)
        h_y_step = 460 // max(n_helices, 1)
        for j, (s1, s2) in enumerate(helices):
            hy = y0 + 130 + j * h_y_step
            # Two parallel strands per helix
            for k, strand in enumerate([s1, s2]):
                stroke_color = MAROON_DARK if strand == "heavy" else ACCENT
                stroke_w = 10 if strand == "heavy" else 6
                strand_y = hy + k * 20
                d.line([(x + 40, strand_y), (x + col_w - 40, strand_y)],
                       fill=stroke_color, width=stroke_w)
            # Rungs (base pairs)
            for rx_off in range(50, col_w - 50, 26):
                d.line([(x + rx_off, hy), (x + rx_off, hy + 20)],
                       fill=MUTED, width=2)

        # Caption
        cap_lines = wrap(d, caption, font("sans", 24), col_w - 60)
        cy = y0 + col_h - 100
        for line in cap_lines:
            tw_l = d.textlength(line, font=font("sans", 24))
            d.text((x + col_w // 2 - tw_l / 2, cy), line,
                   fill=MUTED, font=font("sans", 24))
            cy += 32

    # Legend
    leg_y = 980
    d.line([(140, leg_y + 10), (200, leg_y + 10)], fill=MAROON_DARK, width=10)
    d.text((210, leg_y - 5), "= old (parental) strand", fill=INK,
           font=font("sans", 26))
    d.line([(700, leg_y + 10), (760, leg_y + 10)], fill=ACCENT, width=6)
    d.text((770, leg_y - 5), "= new (daughter) strand", fill=INK,
           font=font("sans", 26))
deck.custom("06_semiconservative", semiconservative)


# 07 — replication enzymes (custom: replication fork with helicase, SSBPs, topo, primase)
def replication_enzymes(img, d):
    d.text((110, 70), "The fork  —  helicase, SSBPs, topoisomerase, primase.",
           fill=MAROON, font=font("serif_bold", 48))
    d.text((110, 140),
           "Four enzymes open up the DNA  before  polymerase can start.",
           fill=ACCENT, font=font("sans_bold", 30))

    # Draw the replication fork
    fork_x = 700           # the vertex of the fork
    fork_y = 540           # vertical center
    arm_len = 480          # how far the unwound arms extend
    closed_len = 380       # how far the closed double helix extends right

    # Closed double helix on the right (still wound)
    for k in range(2):
        sy = fork_y - 25 + k * 50
        d.line([(fork_x, sy), (fork_x + closed_len, sy)],
               fill=MAROON_DARK, width=8)
    # Rungs on closed section
    for rx_off in range(20, closed_len, 22):
        d.line([(fork_x + rx_off, fork_y - 25),
                (fork_x + rx_off, fork_y + 25)],
               fill=MUTED, width=2)

    # Two open arms going left from the fork
    # Top arm
    top_end_x = fork_x - arm_len
    top_end_y = fork_y - 180
    d.line([(fork_x, fork_y - 25), (top_end_x, top_end_y)],
           fill=MAROON_DARK, width=8)
    # Bottom arm
    bot_end_x = fork_x - arm_len
    bot_end_y = fork_y + 180
    d.line([(fork_x, fork_y + 25), (bot_end_x, bot_end_y)],
           fill=MAROON_DARK, width=8)

    # SSBPs (small circles) on the open arms
    for arm_y0, arm_y1 in [(fork_y - 25, top_end_y), (fork_y + 25, bot_end_y)]:
        for frac in [0.25, 0.5, 0.75]:
            sx = fork_x + frac * (top_end_x - fork_x)
            sy = arm_y0 + frac * (arm_y1 - arm_y0)
            d.ellipse([sx - 18, sy - 18, sx + 18, sy + 18],
                      fill=ACCENT_LT, outline=MAROON_DARK, width=3)
            d.text((sx - 14, sy - 12), "SS", fill=MAROON_DARK,
                   font=font("sans_bold", 18))

    # Helicase at the fork vertex
    d.ellipse([fork_x - 55, fork_y - 55, fork_x + 55, fork_y + 55],
              fill=MAROON, outline=MAROON_DARK, width=4)
    d.text((fork_x - 50, fork_y - 22), "HEL", fill=CREAM,
           font=font("sans_bold", 26))

    # Topoisomerase ahead of the fork (right side, on the closed DNA)
    topo_x = fork_x + closed_len - 60
    d.ellipse([topo_x - 50, fork_y - 50, topo_x + 50, fork_y + 50],
              fill=ACCENT, outline=MAROON_DARK, width=4)
    d.text((topo_x - 38, fork_y - 18), "TOPO", fill=CREAM,
           font=font("sans_bold", 22))

    # Primase laying down a primer on the top arm
    prim_frac = 0.5
    prim_x = fork_x + prim_frac * (top_end_x - fork_x)
    prim_y = fork_y - 25 + prim_frac * (top_end_y - (fork_y - 25))
    # Primer as a short red segment
    d.line([(prim_x - 30, prim_y + 12), (prim_x + 30, prim_y + 12)],
           fill=RED, width=6)
    d.text((prim_x - 30, prim_y + 24), "RNA primer",
           fill=RED, font=font("sans_bold", 22))
    # Primase blob
    d.ellipse([prim_x - 38, prim_y - 38, prim_x + 38, prim_y + 38],
              fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((prim_x - 38, prim_y - 16), "PRIM", fill=MAROON_DARK,
           font=font("sans_bold", 22))

    # Labels with leader lines
    # Helicase
    d.line([(fork_x, fork_y + 60), (fork_x, fork_y + 130)],
           fill=MAROON_DARK, width=2)
    d.text((fork_x - 90, fork_y + 135), "HELICASE",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((fork_x - 220, fork_y + 175), "unwinds the helix",
           fill=MUTED, font=font("sans", 24))

    # SSBP label
    d.text((180, 280), "SSBPs", fill=ACCENT,
           font=font("sans_bold", 32))
    d.text((180, 320), "Single-strand binding proteins",
           fill=INK, font=font("sans", 24))
    d.text((180, 355), "keep strands from re-annealing.",
           fill=MUTED, font=font("sans", 22))

    # Topo label
    d.text((1380, 280), "TOPOISOMERASE",
           fill=ACCENT, font=font("sans_bold", 28))
    d.text((1380, 320), "Relieves supercoiling",
           fill=INK, font=font("sans", 24))
    d.text((1380, 355), "ahead of the fork.",
           fill=MUTED, font=font("sans", 22))

    # Primase label
    d.text((180, 800), "PRIMASE",
           fill=ACCENT, font=font("sans_bold", 32))
    d.text((180, 840), "Lays RNA primer — provides a 3' OH",
           fill=INK, font=font("sans", 24))
    d.text((180, 870), "for DNA polymerase to build from.",
           fill=MUTED, font=font("sans", 22))

    # Bottom strip — the order
    d.rounded_rectangle([110, 940, W - 110, 1020], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "ORDER:  helicase  →  SSBPs  →  topoisomerase  →  primase  →  (then polymerase)",
             font("sans_bold", 30), 962, MAROON_DARK)
deck.custom("07_replication_enzymes", replication_enzymes)


# 08 — polymerase directionality (leading vs lagging + Okazaki)
def polymerase_directionality(img, d):
    d.text((110, 70), "Polymerase  —  always 5' → 3'.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 150),
           "Same rule creates two very different strands.",
           fill=ACCENT, font=font("sans_bold", 32))

    # Replication fork in the middle
    fork_x = W // 2
    fork_y = 580
    arm_len = 600

    # Template strands diverging left (open arms of the fork)
    # Top template: runs 3' (at fork) → 5' (at left end)
    # Bottom template: runs 5' (at fork) → 3' (at left end)
    top_y = fork_y - 100
    bot_y = fork_y + 100
    # Top template
    d.line([(fork_x, top_y), (fork_x - arm_len, top_y)],
           fill=MAROON_DARK, width=8)
    d.text((fork_x + 10, top_y - 38), "3'",
           fill=MAROON, font=font("serif_bold", 36))
    d.text((fork_x - arm_len - 50, top_y - 38), "5'",
           fill=MAROON, font=font("serif_bold", 36))
    d.text((fork_x - arm_len + 80, top_y - 50), "template",
           fill=MUTED, font=font("serif_ital", 24))

    # Bottom template
    d.line([(fork_x, bot_y), (fork_x - arm_len, bot_y)],
           fill=MAROON_DARK, width=8)
    d.text((fork_x + 10, bot_y + 12), "5'",
           fill=MAROON, font=font("serif_bold", 36))
    d.text((fork_x - arm_len - 50, bot_y + 12), "3'",
           fill=MAROON, font=font("serif_bold", 36))
    d.text((fork_x - arm_len + 80, bot_y + 30), "template",
           fill=MUTED, font=font("serif_ital", 24))

    # Closed double helix to the right of the fork
    closed_x = fork_x + 280
    for k in range(2):
        sy = fork_y - 25 + k * 50
        d.line([(fork_x, sy), (closed_x, sy)],
               fill=MAROON_DARK, width=8)
    for rx_off in range(20, 280, 22):
        d.line([(fork_x + rx_off, fork_y - 25),
                (fork_x + rx_off, fork_y + 25)],
               fill=MUTED, width=2)
    # Helicase at fork
    d.ellipse([fork_x - 40, fork_y - 40, fork_x + 40, fork_y + 40],
              fill=MAROON, outline=MAROON_DARK, width=4)
    d.text((fork_x - 30, fork_y - 16), "HEL", fill=CREAM,
           font=font("sans_bold", 22))
    # Fork direction arrow
    d.text((closed_x + 20, fork_y - 20), "→",
           fill=MAROON_DARK, font=font("serif_bold", 50))
    d.text((closed_x + 70, fork_y + 35), "fork moves",
           fill=MUTED, font=font("sans", 22))

    # LEADING strand: continuous, on the top template
    # New strand drawn just below the top template, going 5'→3' toward the fork
    lead_y = top_y + 36
    d.line([(fork_x - arm_len + 60, lead_y), (fork_x - 30, lead_y)],
           fill=ACCENT, width=8)
    # Arrow at the fork end showing direction of synthesis (toward fork = right)
    d.polygon([(fork_x - 30, lead_y - 10),
               (fork_x - 8, lead_y),
               (fork_x - 30, lead_y + 10)], fill=ACCENT)
    d.text((fork_x - arm_len + 60, lead_y - 36), "5'",
           fill=ACCENT, font=font("serif_bold", 30))
    d.text((fork_x - 30, lead_y + 18), "3'",
           fill=ACCENT, font=font("serif_bold", 30))
    d.text((fork_x - arm_len + 60, lead_y + 30), "LEADING — continuous",
           fill=ACCENT, font=font("sans_bold", 26))

    # LAGGING strand: 3 Okazaki fragments on the bottom template
    lag_y = bot_y - 36
    frag_w = 150
    starts = [fork_x - 90, fork_x - 270, fork_x - 450]
    for i, sx in enumerate(starts):
        # Fragment built 5'→3', moving away from the fork (so leftward)
        d.line([(sx, lag_y), (sx - frag_w, lag_y)], fill=ACCENT, width=8)
        # Arrowhead at left end (3' end of fragment)
        d.polygon([(sx - frag_w, lag_y - 10),
                   (sx - frag_w - 22, lag_y),
                   (sx - frag_w, lag_y + 10)], fill=ACCENT)
        # 5' label at fragment start (closer to fork)
        d.text((sx + 4, lag_y - 36), "5'",
               fill=ACCENT, font=font("serif_bold", 26))
        # 3' label at fragment end
        d.text((sx - frag_w - 30, lag_y - 36), "3'",
               fill=ACCENT, font=font("serif_bold", 26))
        # RNA primer at the 5' end of each fragment
        d.line([(sx + 4, lag_y - 12), (sx - 32, lag_y - 12)],
               fill=RED, width=6)
        d.text((sx - 4, lag_y - 80), f"#{3 - i}",
               fill=MAROON, font=font("sans_bold", 22))
    d.text((fork_x - arm_len + 60, lag_y + 30),
           "LAGGING — short Okazaki fragments",
           fill=ACCENT, font=font("sans_bold", 26))
    # Red primer legend dot
    d.line([(fork_x - arm_len + 60, lag_y + 70),
            (fork_x - arm_len + 130, lag_y + 70)],
           fill=RED, width=6)
    d.text((fork_x - arm_len + 145, lag_y + 56), "= RNA primer",
           fill=RED, font=font("sans", 22))

    # Bottom strip
    d.rounded_rectangle([110, 940, W - 110, 1020], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "BOTH strands are built 5' → 3'.  The lagging strand just does it in pieces, away from the fork.",
             font("sans_bold", 28), 962, MAROON_DARK)
deck.custom("08_polymerase_directionality", polymerase_directionality)


# 09 — finishing steps (Pol I + ligase)
def finishing_steps(img, d):
    d.text((110, 70), "Finishing  —  Pol I  +  ligase.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 150),
           "Two cleanup enzymes turn Okazaki fragments into one continuous strand.",
           fill=ACCENT, font=font("sans_bold", 30))

    # Three rows: BEFORE, POL I REPLACES PRIMER, LIGASE SEALS
    row_h = 230
    y0 = 230
    label_x = 110
    diag_x = 480
    diag_w = 1320

    def draw_strand_with_segments(y, segments):
        """segments: list of (start_frac, end_frac, color)."""
        for s, e, col in segments:
            x0 = diag_x + s * diag_w
            x1 = diag_x + e * diag_w
            d.line([(x0, y), (x1, y)], fill=col, width=14)

    def draw_nick(y, frac):
        """Small gap mark indicating a nick."""
        x = diag_x + frac * diag_w
        d.line([(x - 4, y - 18), (x - 4, y + 18)], fill=MAROON_DARK, width=2)
        d.line([(x + 4, y - 18), (x + 4, y + 18)], fill=MAROON_DARK, width=2)
        d.text((x - 18, y - 50), "nick", fill=MAROON,
               font=font("sans_bold", 22))

    # Row 1: BEFORE — Okazaki fragments with red RNA primers
    y1 = y0 + row_h * 0 + 60
    d.text((label_x, y1 - 20), "1. BEFORE",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((label_x, y1 + 20), "Okazaki + primers",
           fill=MUTED, font=font("sans", 22))
    # Three Okazaki fragments: red primer + teal DNA
    fragments = [
        (0.00, 0.05, RED), (0.05, 0.30, ACCENT),
        (0.32, 0.37, RED), (0.37, 0.62, ACCENT),
        (0.64, 0.69, RED), (0.69, 0.94, ACCENT),
    ]
    draw_strand_with_segments(y1 + 10, fragments)

    # Row 2: POL I replaces primer with DNA
    y2 = y0 + row_h * 1 + 60
    d.text((label_x, y2 - 20), "2. POL I",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((label_x, y2 + 20), "replaces RNA → DNA",
           fill=MUTED, font=font("sans", 22))
    fragments2 = [
        (0.00, 0.30, ACCENT),
        (0.32, 0.62, ACCENT),
        (0.64, 0.94, ACCENT),
    ]
    draw_strand_with_segments(y2 + 10, fragments2)
    # Show the two nicks remaining
    draw_nick(y2 + 10, 0.31)
    draw_nick(y2 + 10, 0.63)

    # Row 3: LIGASE seals the nicks
    y3 = y0 + row_h * 2 + 60
    d.text((label_x, y3 - 20), "3. LIGASE",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((label_x, y3 + 20), "seals nicks",
           fill=MUTED, font=font("sans", 22))
    fragments3 = [(0.00, 0.94, ACCENT)]
    draw_strand_with_segments(y3 + 10, fragments3)

    # Legend for colors
    leg_y = y3 + 90
    d.line([(diag_x, leg_y), (diag_x + 60, leg_y)], fill=RED, width=10)
    d.text((diag_x + 70, leg_y - 14), "RNA primer", fill=RED,
           font=font("sans_bold", 24))
    d.line([(diag_x + 300, leg_y), (diag_x + 360, leg_y)], fill=ACCENT, width=10)
    d.text((diag_x + 370, leg_y - 14), "DNA", fill=ACCENT,
           font=font("sans_bold", 24))

    # Bottom strip
    d.rounded_rectangle([110, 970, W - 110, 1050], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Ligase forms the final phosphodiester bond — joining everything into one continuous strand.",
             font("sans_bold", 28), 995, MAROON_DARK)
deck.custom("09_finishing_steps", finishing_steps)


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Template:   3' — T A C G G T — 5'.   Write the new strand. Which direction?",
           "3' — T A C G G T — 5'",
           hint="Pause now. Solve it. Press play when you're ready.")

# 11 — duplicate the pause slide for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — proofreading + repair (custom: 3 layers stacked)
def proofreading_repair(img, d):
    d.text((110, 70), "How we get to 1 error per billion bases.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Three layers of accuracy  —  stack the odds.",
           fill=ACCENT, font=font("sans_bold", 32))

    layers = [
        ("LAYER  1",
         "PROOFREADING",
         "DNA polymerase has 3' → 5' exonuclease activity.",
         "Backs up and removes a wrong base it just added.",
         "~1 error per 10⁷ bases  →  10⁹ after proofreading"),
        ("LAYER  2",
         "MISMATCH  REPAIR",
         "Protein patrols scan freshly-replicated DNA.",
         "Cut out and re-synthesize errors that slipped past.",
         "Defects → Lynch syndrome (hereditary colon cancer)"),
        ("LAYER  3",
         "NUCLEOTIDE  EXCISION  REPAIR  (NER)",
         "Handles bulky damage — especially UV thymine dimers.",
         "Removes a patch of nucleotides, fills, ligates.",
         "Defective in xeroderma pigmentosum"),
    ]

    box_h = 220
    gap = 16
    y = 240
    for i, (tag, title, line1, line2, footnote) in enumerate(layers):
        # Alternate colors for visual rhythm
        bg = ACCENT_LT if i % 2 == 0 else CARD
        d.rounded_rectangle([110, y, W - 110, y + box_h], radius=18,
                            outline=ACCENT, width=5, fill=bg)
        # Big layer number badge on the left
        bx = 160
        by = y + box_h // 2
        d.ellipse([bx - 50, by - 50, bx + 50, by + 50],
                  fill=ACCENT, outline=MAROON_DARK, width=4)
        ns = str(i + 1)
        nf = font("serif_bold", 56)
        tw = d.textlength(ns, font=nf)
        d.text((bx - tw / 2, by - 38), ns, fill=CREAM, font=nf)

        # Body content
        d.text((240, y + 24), tag, fill=ACCENT,
               font=font("sans_bold", 22))
        d.text((240, y + 56), title, fill=MAROON_DARK,
               font=font("serif_bold", 40))
        d.text((240, y + 120), line1, fill=INK, font=font("sans", 26))
        d.text((240, y + 158), line2, fill=INK, font=font("sans", 26))
        # Footnote on the right
        d.text((1240, y + 100), footnote, fill=MAROON,
               font=font("sans_bold", 24))

        y += box_h + gap

    # Bottom strip
    d.rounded_rectangle([110, y + 6, W - 110, y + 76], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Xeroderma pigmentosum patients can't repair UV damage → severe sunlight-induced skin cancer.",
             font("sans_bold", 26), y + 26, MAROON_DARK)
deck.custom("12_proofreading_repair", proofreading_repair)


# 13 — telomeres (custom: shortening over generations + telomerase callout)
def telomeres(img, d):
    d.text((110, 70), "Telomeres  —  the end replication problem.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Human telomere sequence:    T T A G G G   ·   repeated thousands of times.",
           fill=ACCENT, font=font("sans_bold", 30))

    # Left: chromosomes shortening
    lx, ly = 110, 230
    lw, lh = 1090, 740
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "Each division → telomere shortens",
           fill=MAROON_DARK, font=font("sans_bold", 32))

    # 4 chromosomes with shrinking telomere caps
    base_chrom_x = lx + 60
    chrom_y_step = 150
    chrom_y0 = ly + 110
    body_len = 600
    # Telomere lengths in pixels
    tel_lens = [180, 130, 80, 30]
    labels = ["Newborn cell", "Division 20", "Division 50", "Division 70 (senescence)"]

    for i, (tlen, label) in enumerate(zip(tel_lens, labels)):
        cy = chrom_y0 + i * chrom_y_step
        # Left telomere (red cap)
        d.rounded_rectangle([base_chrom_x, cy - 18,
                              base_chrom_x + tlen, cy + 18], radius=10,
                             fill=MAROON, outline=MAROON_DARK, width=3)
        # Chromosome body (teal)
        d.rounded_rectangle([base_chrom_x + tlen + 4, cy - 18,
                              base_chrom_x + tlen + 4 + body_len, cy + 18], radius=10,
                             fill=ACCENT_LT, outline=MAROON_DARK, width=3)
        # Right telomere
        d.rounded_rectangle([base_chrom_x + tlen + 4 + body_len + 4, cy - 18,
                              base_chrom_x + tlen + 4 + body_len + 4 + tlen, cy + 18], radius=10,
                             fill=MAROON, outline=MAROON_DARK, width=3)
        # Label on the right side
        right_edge = base_chrom_x + 2 * tlen + body_len + 8
        d.text((right_edge + 30, cy - 16), label, fill=INK,
               font=font("sans_bold", 26))

    # Legend
    d.rounded_rectangle([lx + 30, ly + lh - 110, lx + lw - 30, ly + lh - 30],
                        radius=14, fill=ACCENT_LT, outline=MAROON, width=3)
    d.rectangle([lx + 60, ly + lh - 85, lx + 100, ly + lh - 55], fill=MAROON)
    d.text((lx + 115, ly + lh - 90), "= telomere (TTAGGG repeats)",
           fill=INK, font=font("sans_bold", 24))
    d.rectangle([lx + 560, ly + lh - 85, lx + 600, ly + lh - 55],
                fill=ACCENT_LT, outline=MAROON_DARK, width=2)
    d.text((lx + 615, ly + lh - 90), "= rest of chromosome",
           fill=INK, font=font("sans_bold", 24))

    # Right: TELOMERASE box
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((rx + 30, ly + 20), "TELOMERASE",
           fill=MAROON_DARK, font=font("serif_bold", 50))
    d.text((rx + 30, ly + 100),
           "Carries its own",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 138),
           "RNA template.",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 200),
           "Extends telomeres",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 238),
           "back out.",
           fill=INK, font=font("sans", 28))

    d.text((rx + 30, ly + 320), "ACTIVE in:",
           fill=MAROON, font=font("sans_bold", 30))
    for i, bullet in enumerate(["·  germ cells",
                                 "·  stem cells",
                                 "·  most cancers"]):
        d.text((rx + 30, ly + 370 + i * 46), bullet,
               fill=MAROON_DARK, font=font("sans_bold", 28))

    d.text((rx + 30, ly + 540), "SILENT in:",
           fill=MUTED, font=font("sans_bold", 30))
    d.text((rx + 30, ly + 585), "·  most adult cells",
           fill=INK, font=font("sans", 28))
    d.text((rx + 30, ly + 625), "·  → contributes to aging",
           fill=INK, font=font("serif_ital", 26))

    # Bottom strip
    d.rounded_rectangle([110, 990, W - 110, 1060], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Cancer cells reactivate telomerase  →  effectively immortal division.",
             font("sans_bold", 28), 1012, MAROON_DARK)
deck.custom("13_telomeres", telomeres)


# 14 — compare traps: lagging strand directionality + primer requirement
deck.compare("14_compare_traps",
             "Common traps  —  three to memorize.",
             left={"label": "WRONG  ✗",
                   "color": MAROON,
                   "lines": [
                       "Lagging strand is built",
                       "3' → 5'.",
                       "",
                       "DNA polymerase can",
                       "start from scratch.",
                       "",
                       "Semiconservative =",
                       "all-old or all-new",
                       "daughter strands.",
                   ],
                   "footnote": "These are the three most-missed answers on this topic."},
             right={"label": "RIGHT  ✓",
                    "color": ACCENT,
                    "lines": [
                        "BOTH strands built 5' → 3'.",
                        "Lagging just does it backward",
                        "in short Okazaki fragments.",
                        "",
                        "Polymerase needs a primer.",
                        "Primase lays it down first.",
                        "",
                        "Semiconservative = one old",
                        "+ one new strand per daughter.",
                    ],
                    "footnote": "Get these three right → most of the points on this topic."})


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "DNA = double helix, antiparallel; A-T (2 H-bonds), G-C (3 H-bonds).",
    "Replication is semiconservative — Meselson & Stahl, 1958.",
    "Enzyme order:  helicase  →  SSBPs  →  topoisomerase  →  primase  →  Pol III.",
    "Pol III builds 5' → 3':  leading continuous;  lagging in Okazaki fragments.",
    "Pol I replaces RNA primer with DNA;  ligase seals nicks.",
    "Proofreading (3'→5' exo) + mismatch repair + NER → ~1 error per 10⁹ bases.",
    "Telomeres shrink with each division;  telomerase rebuilds them (germ, stem, cancer).",
], assignment=[
    "1.  Write the new strand for template  3'-CGTAAG-5'.  Show direction of synthesis.",
    "2.  List the 7 replication enzymes in order, with one sentence on what each does.",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapter 14 — DNA structure and replication"),
    ("2.", "Khan Academy AP Bio",     "Unit 6 problem sets — DNA replication and repair"),
    ("3.", "Assignment in dashboard", "Complementary strand + enzyme order (above)"),
    ("4.", "Advisor check-in",        "If 5'→3' directionality or Okazaki logic still feels fuzzy"),
], next_text="Next up:  Module 8 — Transcription and Translation  (DNA → RNA → protein).")


print("AP Biology Module 7 slides built.")

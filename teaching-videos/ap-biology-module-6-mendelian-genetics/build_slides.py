"""AP Biology · Module 6 — Mendelian Genetics.

Teal (science) theme auto-resolved from "AP Biology". 16 slides total.
Heavy on customs because Punnett squares, dihybrid grids, pedigrees, and
meiosis I/II side-by-sides all need real diagrams. Pause slide (10) is
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
deck = Deck(course="AP Biology", module_num=6, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 6 — Mendelian Genetics",
           "Sample lesson  ·  ~9 minutes")


# 02 — hook: two brown-eyed parents, one blue-eyed child
def hook(img, d):
    d.text((110, 70), "Two brown-eyed parents.  One blue-eyed kid.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150), "Not the mailman. Just hidden alleles.",
           fill=MUTED, font=font("sans", 32))

    # Left: parent silhouettes with brown eyes
    lx, ly, lw, lh = 140, 230, 760, 600
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    centered_lbl = "PARENTS"
    cf = font("serif_bold", 42)
    tw = d.textlength(centered_lbl, font=cf)
    d.text((lx + lw // 2 - tw / 2, ly + 30), centered_lbl,
           fill=MAROON_DARK, font=cf)

    # Two heads side by side
    head_y = ly + 200
    for i, head_x in enumerate([lx + 220, lx + 540]):
        # face
        d.ellipse([head_x - 80, head_y - 80, head_x + 80, head_y + 80],
                  outline=MAROON_DARK, width=4, fill=ACCENT_LT)
        # brown eyes
        d.ellipse([head_x - 40, head_y - 20, head_x - 16, head_y + 4],
                  fill=(101, 67, 33), outline=MAROON_DARK, width=2)
        d.ellipse([head_x + 16, head_y - 20, head_x + 40, head_y + 4],
                  fill=(101, 67, 33), outline=MAROON_DARK, width=2)
        # genotype label
        gf = font("mono", 42)
        gtxt = "Bb"
        tw2 = d.textlength(gtxt, font=gf)
        d.text((head_x - tw2 / 2, head_y + 110), gtxt,
               fill=MAROON, font=gf)
        d.text((head_x - 50, head_y + 165), "brown-eyed",
               fill=MUTED, font=font("sans", 24))

    # Footnote in left card
    foot = "Both are heterozygous: Bb."
    ff = font("serif_bold", 32)
    tw = d.textlength(foot, font=ff)
    d.text((lx + lw // 2 - tw / 2, ly + lh - 90), foot,
           fill=MAROON_DARK, font=ff)
    foot2 = "Each carries one hidden b allele."
    sf = font("serif_ital", 26)
    tw = d.textlength(foot2, font=sf)
    d.text((lx + lw // 2 - tw / 2, ly + lh - 50), foot2,
           fill=MUTED, font=sf)

    # Right: child with blue eyes
    rx, ry, rw, rh = 1020, 230, 760, 600
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=28,
                        outline=MAROON, width=6, fill=CARD)
    centered_lbl2 = "CHILD"
    tw = d.textlength(centered_lbl2, font=cf)
    d.text((rx + rw // 2 - tw / 2, ry + 30), centered_lbl2,
           fill=MAROON_DARK, font=cf)

    # One smaller head, blue eyes
    chx, chy = rx + rw // 2, ry + 220
    d.ellipse([chx - 90, chy - 90, chx + 90, chy + 90],
              outline=MAROON_DARK, width=4, fill=ACCENT_LT)
    d.ellipse([chx - 45, chy - 22, chx - 18, chy + 5],
              fill=(70, 130, 200), outline=MAROON_DARK, width=2)
    d.ellipse([chx + 18, chy - 22, chx + 45, chy + 5],
              fill=(70, 130, 200), outline=MAROON_DARK, width=2)
    gtxt2 = "bb"
    gf2 = font("mono", 52)
    tw = d.textlength(gtxt2, font=gf2)
    d.text((chx - tw / 2, chy + 120), gtxt2,
           fill=MAROON, font=gf2)
    d.text((chx - 60, chy + 190), "blue-eyed",
           fill=MUTED, font=font("sans", 28))

    # Probability
    prob = "P(blue eyes)  =  1/4"
    pf = font("serif_bold", 36)
    tw = d.textlength(prob, font=pf)
    d.text((rx + rw // 2 - tw / 2, ry + rh - 90), prob,
           fill=ACCENT, font=pf)
    d.text((rx + 130, ry + rh - 50), "(Mendel predicted this in 1865.)",
           fill=MUTED, font=font("serif_ital", 24))

    # Bottom punchline strip
    d.rounded_rectangle([110, 870, W - 110, 990], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "One man with pea plants figured out 99% of inheritance — 100 years before we knew what DNA was.",
             font("serif_bold", 32), 905, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Mendel's three laws — segregation, independent assortment, dominance.",
    "Punnett squares — 3:1 monohybrid and 9:3:3:1 dihybrid.",
    "When Mendel breaks — incomplete dominance, codominance, sex-linked, more.",
    "Meiosis, linkage, and chromosomal disorders.",
], footnote="Unit 5 is heredity — 8 to 11% of the AP exam. Lots of free points if you drill the crosses.")


# 04 — Mendel's three laws (custom: 3 cards)
def mendel_laws(img, d):
    d.text((110, 70), "Mendel's three laws.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 160),
           "Pea plants. Seven traits. About 28,000 crosses.",
           fill=MUTED, font=font("sans", 32))

    laws = [
        ("1.", "SEGREGATION",
         "Each parent has 2 alleles per gene.",
         "Gametes carry only 1.",
         "(Alleles split in meiosis I.)",
         ACCENT_LT),
        ("2.", "INDEPENDENT",
         "Alleles for different genes",
         "sort independently —",
         "IF on different chromosomes.",
         ACCENT),
        ("3.", "DOMINANCE",
         "In a heterozygote (Aa),",
         "the dominant allele shows;",
         "the recessive is masked.",
         ACCENT_LT),
    ]
    col_w = 540
    col_h = 600
    gap = 40
    start_x = (W - (col_w * 3 + gap * 2)) // 2
    y0 = 270
    for i, (num, name, l1, l2, l3, col) in enumerate(laws):
        x = start_x + i * (col_w + gap)
        d.rounded_rectangle([x, y0, x + col_w, y0 + col_h], radius=20,
                            outline=MAROON_DARK, width=5, fill=col)
        # Number in big circle
        nc_x, nc_y = x + 80, y0 + 80
        d.ellipse([nc_x - 50, nc_y - 50, nc_x + 50, nc_y + 50],
                  fill=MAROON, outline=MAROON_DARK, width=4)
        nf = font("serif_bold", 52)
        ns = num.rstrip(".")
        tw = d.textlength(ns, font=nf)
        d.text((nc_x - tw / 2, nc_y - 36), ns, fill=CREAM, font=nf)
        # Law name
        d.text((x + 160, y0 + 60), name, fill=MAROON_DARK,
               font=font("sans_bold", 40))
        # Body text
        ly = y0 + 220
        for ln in [l1, l2, l3]:
            d.text((x + 30, ly), ln, fill=INK, font=font("sans", 30))
            ly += 60

    # Bottom: the "second law footnote"
    d.rounded_rectangle([110, 920, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Important caveat:  independent assortment fails for LINKED genes (covered in slide 12).",
             font("sans_bold", 28), 945, MAROON_DARK)
deck.custom("04_mendel_laws", mendel_laws)


# 05 — monohybrid Punnett 3:1 (custom: 2x2 grid with worked Aa x Aa)
def monohybrid_punnett(img, d):
    d.text((110, 70), "Monohybrid cross  —  Aa × Aa  →  3:1.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 155),
           "One trait, two heterozygous parents. The classic.",
           fill=MUTED, font=font("sans", 30))

    # Big 2x2 Punnett on the left
    grid_x = 200
    grid_y = 260
    cell = 170
    # Column headers (mother's gametes): A, a
    d.text((grid_x + cell // 2 + 20, grid_y - 110), "A", fill=MAROON_DARK,
           font=font("serif_bold", 80))
    d.text((grid_x + cell + cell // 2 + 30, grid_y - 110), "a", fill=MAROON_DARK,
           font=font("serif_bold", 80))
    d.text((grid_x + cell - 30, grid_y - 160), "mother:  Aa", fill=ACCENT,
           font=font("sans_bold", 28))
    # Row headers (father's gametes): A, a
    d.text((grid_x - 100, grid_y + cell // 2 - 30), "A", fill=MAROON_DARK,
           font=font("serif_bold", 80))
    d.text((grid_x - 100, grid_y + cell + cell // 2 - 30), "a", fill=MAROON_DARK,
           font=font("serif_bold", 80))
    # Rotated father label (just text to the left)
    d.text((grid_x - 180, grid_y - 50), "father:", fill=ACCENT,
           font=font("sans_bold", 28))
    d.text((grid_x - 180, grid_y - 20), "Aa", fill=ACCENT,
           font=font("sans_bold", 28))

    # Grid cells with offspring
    cells = [
        ("AA", MAROON_DARK, ACCENT_LT),   # row 0 col 0
        ("Aa", INK,        CARD),         # row 0 col 1
        ("Aa", INK,        CARD),         # row 1 col 0
        ("aa", MAROON,     CREAM),        # row 1 col 1
    ]
    for i, (geno, color, bg) in enumerate(cells):
        r = i // 2
        c = i % 2
        x0 = grid_x + c * cell
        y0 = grid_y + r * cell
        d.rectangle([x0, y0, x0 + cell, y0 + cell],
                    fill=bg, outline=MAROON_DARK, width=4)
        gf = font("mono", 76)
        tw = d.textlength(geno, font=gf)
        d.text((x0 + cell / 2 - tw / 2, y0 + 40), geno,
               fill=color, font=gf)

    # Right: outcome breakdown
    rx = grid_x + cell * 2 + 200
    ry = 240
    rw = W - 110 - rx
    rh = 620
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((rx + 30, ry + 20), "OFFSPRING", fill=MAROON_DARK,
           font=font("sans_bold", 38))

    # Genotype ratio
    d.text((rx + 30, ry + 90), "Genotype ratio",
           fill=ACCENT, font=font("sans_bold", 32))
    d.text((rx + 30, ry + 140), "1  AA  :  2  Aa  :  1  aa",
           fill=MAROON_DARK, font=font("mono", 44))

    # divider line
    d.line([(rx + 30, ry + 230), (rx + rw - 30, ry + 230)],
           fill=MUTED, width=2)

    # Phenotype ratio
    d.text((rx + 30, ry + 260), "Phenotype ratio",
           fill=ACCENT, font=font("sans_bold", 32))
    d.text((rx + 30, ry + 310), "3  dominant  :  1  recessive",
           fill=MAROON_DARK, font=font("mono", 38))
    d.text((rx + 30, ry + 370),
           "(AA + Aa + Aa = 3 show A;  aa = 1 shows a)",
           fill=MUTED, font=font("serif_ital", 26))

    # Probabilities
    d.line([(rx + 30, ry + 430), (rx + rw - 30, ry + 430)],
           fill=MUTED, width=2)
    d.text((rx + 30, ry + 460), "P(recessive phenotype)",
           fill=ACCENT, font=font("sans_bold", 30))
    d.text((rx + 30, ry + 510), "=  1/4  =  25%",
           fill=MAROON, font=font("serif_bold", 44))

    # Bottom takeaway
    d.rounded_rectangle([110, 920, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Memorize this:  Aa × Aa  →  1 : 2 : 1 genotype,  3 : 1 phenotype.",
             font("serif_bold", 32), 947, MAROON_DARK)
deck.custom("05_monohybrid_punnett", monohybrid_punnett)


# 06 — dihybrid Punnett 9:3:3:1 (custom: 4x4 grid)
def dihybrid_punnett(img, d):
    d.text((110, 60), "Dihybrid cross  —  AaBb × AaBb  →  9 : 3 : 3 : 1.",
           fill=MAROON, font=font("serif_bold", 52))
    d.text((110, 135),
           "Two traits, both heterozygous. Only works if A and B are unlinked.",
           fill=MUTED, font=font("sans", 28))

    # 4x4 grid on the left
    grid_x = 200
    grid_y = 280
    cell = 130
    gametes = ["AB", "Ab", "aB", "ab"]

    # Column headers
    for c, g in enumerate(gametes):
        gf = font("mono", 46)
        tw = d.textlength(g, font=gf)
        d.text((grid_x + c * cell + cell / 2 - tw / 2, grid_y - 70), g,
               fill=MAROON_DARK, font=gf)
    # Row headers
    for r, g in enumerate(gametes):
        gf = font("mono", 46)
        d.text((grid_x - 100, grid_y + r * cell + cell / 2 - 30), g,
               fill=MAROON_DARK, font=gf)

    # Parent labels
    d.text((grid_x + cell * 2 - 50, grid_y - 140), "mother:  AaBb",
           fill=ACCENT, font=font("sans_bold", 28))
    d.text((grid_x - 200, grid_y - 60), "father:",
           fill=ACCENT, font=font("sans_bold", 28))
    d.text((grid_x - 200, grid_y - 30), "AaBb",
           fill=ACCENT, font=font("sans_bold", 28))

    # Fill the grid. We'll compute each offspring genotype and color by phenotype.
    # 4 phenotype categories:
    #   A_B_ (both dominant)        — 9 cells → ACCENT (teal)
    #   A_bb (A dominant, b recessive) — 3 cells → ACCENT_LT
    #   aaB_ (a recessive, B dominant) — 3 cells → MAROON
    #   aabb (both recessive)       — 1 cell → MAROON_DARK
    def combine(g1, g2):
        # g1 and g2 each two chars; combine to a sorted 4-letter genotype
        # but for display, just concatenate in convention (e.g., "AB"+"Ab"= "AABb")
        # We'll sort within each gene pair (capital first).
        a_pair = "".join(sorted([g1[0], g2[0]], key=lambda x: (x.lower(), x.islower())))
        b_pair = "".join(sorted([g1[1], g2[1]], key=lambda x: (x.lower(), x.islower())))
        return a_pair + b_pair

    def phen_color(geno):
        # Has uppercase A? Has uppercase B?
        has_A = "A" in geno[:2]
        has_B = "B" in geno[2:]
        if has_A and has_B:
            return ACCENT_LT, MAROON_DARK
        elif has_A and not has_B:
            return CARD, INK
        elif not has_A and has_B:
            return CREAM, MAROON
        else:
            return MAROON, CREAM

    for r, g_row in enumerate(gametes):
        for c, g_col in enumerate(gametes):
            geno = combine(g_col, g_row)  # row=father, col=mother (any order)
            bg, text_color = phen_color(geno)
            x0 = grid_x + c * cell
            y0 = grid_y + r * cell
            d.rectangle([x0, y0, x0 + cell, y0 + cell],
                        fill=bg, outline=MAROON_DARK, width=3)
            gf = font("mono", 32)
            tw = d.textlength(geno, font=gf)
            d.text((x0 + cell / 2 - tw / 2, y0 + cell / 2 - 22), geno,
                   fill=text_color, font=gf)

    # Right side: ratio breakdown
    rx = grid_x + cell * 4 + 100
    ry = 230
    rw = W - 110 - rx
    rh = 650
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((rx + 30, ry + 20), "PHENOTYPE  RATIO",
           fill=MAROON_DARK, font=font("sans_bold", 32))

    rows = [
        ("9", "A_  B_", "both dominant", ACCENT_LT),
        ("3", "A_  bb", "A dom, b rec",   CARD),
        ("3", "aa  B_", "a rec, B dom",   CREAM),
        ("1", "aa  bb", "both recessive", MAROON),
    ]
    ly = ry + 90
    for num, geno, label, swatch in rows:
        # Swatch
        d.rectangle([rx + 30, ly + 4, rx + 90, ly + 60],
                    fill=swatch, outline=MAROON_DARK, width=3)
        d.text((rx + 110, ly), num, fill=MAROON_DARK,
               font=font("serif_bold", 56))
        d.text((rx + 190, ly + 10), geno, fill=INK,
               font=font("mono", 38))
        d.text((rx + 190, ly + 70), label, fill=MUTED,
               font=font("sans", 22))
        ly += 130

    # Bottom takeaway
    d.rounded_rectangle([110, 940, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Shortcut:  9 + 3 + 3 + 1 = 16 cells.  9:3:3:1 collapses to 3:1 for each gene alone.",
             font("sans_bold", 28), 962, MAROON_DARK)
deck.custom("06_dihybrid_punnett", dihybrid_punnett)


# 07 — non-Mendelian inheritance (custom: 6-cell grid)
def non_mendelian(img, d):
    d.text((110, 70), "When Mendel \"breaks.\"",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 155),
           "Six patterns AP loves to test. (None actually break Mendel —",
           fill=MUTED, font=font("sans", 28))
    d.text((110, 195),
           "they just go beyond his original 1:1 dominant/recessive model.)",
           fill=MUTED, font=font("sans", 28))

    items = [
        ("INCOMPLETE\nDOMINANCE",
         "Heterozygote shows BLEND.",
         "Red × white → PINK.",
         "Ratio 1 : 2 : 1.",
         ACCENT_LT),
        ("CO-\nDOMINANCE",
         "BOTH alleles fully show.",
         "ABO blood type: AB shows",
         "both A and B antigens.",
         ACCENT),
        ("MULTIPLE\nALLELES",
         ">2 alleles in population.",
         "ABO has Iᴬ, Iᴮ, i.",
         "Each person still has 2.",
         ACCENT_LT),
        ("PLEIOTROPY",
         "ONE gene → MANY traits.",
         "Sickle-cell: anemia,",
         "organ damage, malaria.",
         ACCENT),
        ("POLYGENIC",
         "MANY genes → ONE trait.",
         "Height, skin color.",
         "Continuous distribution.",
         ACCENT_LT),
        ("EPISTASIS",
         "Gene A masks gene B.",
         "Labrador coat: E/e gates",
         "whether B/b color shows.",
         ACCENT),
    ]
    col_w = 580
    col_h = 240
    gap = 30
    grid_x = 110
    grid_y = 260
    for i, (name, l1, l2, l3, col) in enumerate(items):
        r = i // 3
        c = i % 3
        x = grid_x + c * (col_w + gap)
        y = grid_y + r * (col_h + gap)
        d.rounded_rectangle([x, y, x + col_w, y + col_h], radius=18,
                            outline=MAROON_DARK, width=4, fill=col)
        # Label box on the left
        d.rectangle([x, y, x + 200, y + col_h], fill=MAROON_DARK)
        # Name (may be 2 lines)
        ny = y + 30
        for piece in name.split("\n"):
            tw = d.textlength(piece, font=font("sans_bold", 24))
            d.text((x + 100 - tw / 2, ny), piece,
                   fill=CREAM, font=font("sans_bold", 24))
            ny += 36
        # Right side body
        body_x = x + 220
        d.text((body_x, y + 30), l1, fill=MAROON_DARK,
               font=font("sans_bold", 24))
        d.text((body_x, y + 80), l2, fill=INK,
               font=font("sans", 22))
        d.text((body_x, y + 130), l3, fill=INK,
               font=font("sans", 22))

    # Bottom takeaway
    d.rounded_rectangle([110, 800, W - 110, 880], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "ABO blood type touches THREE of these:  multiple alleles  +  codominance  (A,B over i).",
             font("sans_bold", 28), 822, MAROON_DARK)

    # Sickle-cell pleiotropy footnote
    d.rounded_rectangle([110, 900, W - 110, 1020], radius=18,
                        fill=CARD, outline=MAROON, width=4)
    d.text((140, 920), "Sickle-cell allele  —  a single base swap (A→T)  causes:",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((140, 965),
           "anemia · organ damage · pain crises · BUT also protects heterozygotes from malaria.",
           fill=INK, font=font("sans", 24))
deck.custom("07_non_mendelian", non_mendelian)


# 08 — sex-linked (custom: pedigree + X-linked recessive logic)
def sex_linked(img, d):
    d.text((110, 70), "Sex-linked inheritance  —  X chromosome.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Males are HEMIZYGOUS:  one X. So one recessive allele = expressed.",
           fill=MUTED, font=font("sans", 28))

    # Left: cross diagram — carrier mother XᴮXᵇ × normal father XᴮY
    lx, ly = 110, 230
    lw, lh = 1020, 660
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "Carrier mother  ×  normal father",
           fill=MAROON_DARK, font=font("sans_bold", 34))
    d.text((lx + 30, ly + 70), "X^B X^b  ×  X^B Y",
           fill=ACCENT, font=font("mono", 38))

    # Punnett 2x2
    grid_x = lx + 250
    grid_y = ly + 200
    cell = 170
    # Column headers (mother's gametes)
    headers_top = ["X^B", "X^b"]
    for c, g in enumerate(headers_top):
        d.text((grid_x + c * cell + cell / 2 - 50, grid_y - 60), g,
               fill=MAROON_DARK, font=font("mono", 38))
    # Row headers (father's gametes)
    headers_left = ["X^B", "Y"]
    for r, g in enumerate(headers_left):
        d.text((grid_x - 110, grid_y + r * cell + cell / 2 - 26), g,
               fill=MAROON_DARK, font=font("mono", 38))

    # Cells
    cells = [
        # (row, col, genotype, label, bg, text_color)
        ("X^B X^B", "normal F",   ACCENT_LT, MAROON_DARK),
        ("X^B X^b", "carrier F",  CARD,      MAROON_DARK),
        ("X^B Y",   "normal M",   ACCENT_LT, MAROON_DARK),
        ("X^b Y",   "AFFECTED M", MAROON,    CREAM),
    ]
    for i, (geno, label, bg, color) in enumerate(cells):
        r = i // 2
        c = i % 2
        x0 = grid_x + c * cell
        y0 = grid_y + r * cell
        d.rectangle([x0, y0, x0 + cell, y0 + cell],
                    fill=bg, outline=MAROON_DARK, width=4)
        gf = font("mono", 30)
        tw = d.textlength(geno, font=gf)
        d.text((x0 + cell / 2 - tw / 2, y0 + 30), geno,
               fill=color, font=gf)
        sf = font("sans_bold", 22)
        tw = d.textlength(label, font=sf)
        d.text((x0 + cell / 2 - tw / 2, y0 + 100), label,
               fill=color, font=sf)

    # Right: key rules + examples
    rx = lx + lw + 30
    ry = ly
    rw = W - 110 - rx
    rh = lh
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((rx + 30, ry + 20), "X-linked recessive",
           fill=MAROON_DARK, font=font("serif_bold", 44))
    d.text((rx + 30, ry + 90), "rules:",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    rules = [
        "Affects males MORE often.",
        "Skips generations.",
        "Passed mother → son.",
        "Fathers can't pass to sons",
        "(sons get Y from dad).",
        "",
        "Examples:",
        "  ·  color blindness",
        "  ·  hemophilia",
        "  ·  Duchenne MD",
    ]
    rly = ry + 140
    for line in rules:
        d.text((rx + 30, rly), line, fill=INK,
               font=font("sans", 26))
        rly += 42

    # Bottom takeaway
    d.rounded_rectangle([110, 920, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Carrier mother  +  normal father  →  half her sons will be affected,  half her daughters carriers.",
             font("sans_bold", 28), 947, MAROON_DARK)
deck.custom("08_sex_linked", sex_linked)


# 09 — meiosis overview (custom: meiosis I vs II side-by-side)
def meiosis_overview(img, d):
    d.text((110, 70), "Meiosis  —  one cell  →  four haploid gametes.",
           fill=MAROON, font=font("serif_bold", 56))
    d.text((110, 150),
           "Two divisions back-to-back. Replication only happens once (before).",
           fill=MUTED, font=font("sans", 28))

    # Left card: Meiosis I (reductional)
    lx, ly = 110, 230
    lw, lh = 870, 720
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "MEIOSIS I", fill=ACCENT,
           font=font("serif_bold", 56))
    d.text((lx + 30, ly + 90), "REDUCTIONAL",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((lx + 30, ly + 140),
           "diploid  →  haploid  (2n → n)",
           fill=INK, font=font("sans", 28))

    # Diagram: homologous pair, synapsis, crossover, separate
    cy = ly + 360
    # Left: synapsed homologs (one maroon, one teal)
    sx = lx + 100
    d.line([(sx, cy - 70), (sx, cy + 70)], fill=MAROON_DARK, width=12)
    d.line([(sx + 6, cy - 70), (sx + 6, cy + 70)], fill=MAROON_DARK, width=12)
    d.line([(sx + 30, cy - 70), (sx + 30, cy + 70)], fill=ACCENT, width=12)
    d.line([(sx + 36, cy - 70), (sx + 36, cy + 70)], fill=ACCENT, width=12)
    # Chiasma (crossover X)
    d.line([(sx + 6, cy - 30), (sx + 30, cy - 10)],
           fill=RED, width=4)
    d.line([(sx + 30, cy - 30), (sx + 6, cy - 10)],
           fill=RED, width=4)
    d.text((sx - 30, cy + 100), "synapsis +", fill=MAROON_DARK,
           font=font("sans_bold", 22))
    d.text((sx - 30, cy + 130), "crossing over", fill=MAROON_DARK,
           font=font("sans_bold", 22))

    # Arrow →
    d.line([(sx + 150, cy), (sx + 250, cy)], fill=MAROON_DARK, width=4)
    d.polygon([(sx + 250, cy), (sx + 230, cy - 12), (sx + 230, cy + 12)],
              fill=MAROON_DARK)
    d.text((sx + 160, cy + 30), "homologs", fill=MUTED, font=font("sans", 22))
    d.text((sx + 160, cy + 55), "SEPARATE", fill=MUTED, font=font("sans_bold", 24))

    # Right: two daughter cells, each with a chromosome (still 2 chromatids)
    cell_x = sx + 350
    for i, col in enumerate([MAROON_DARK, ACCENT]):
        ccx = cell_x + i * 200
        d.ellipse([ccx - 70, cy - 90, ccx + 70, cy + 90],
                  outline=MAROON_DARK, width=4, fill=CREAM)
        d.line([(ccx - 10, cy - 50), (ccx - 10, cy + 50)], fill=col, width=10)
        d.line([(ccx + 6, cy - 50), (ccx + 6, cy + 50)], fill=col, width=10)
    d.text((cell_x + 30, cy + 110), "2 haploid cells  ·  each still 2 chromatids",
           fill=MUTED, font=font("sans_bold", 22))

    # Key facts box
    d.rounded_rectangle([lx + 30, ly + 580, lx + lw - 30, ly + lh - 20],
                        radius=12, fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((lx + 50, ly + 600), "Crossing over (Prophase I)",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((lx + 50, ly + 640), "Independent assortment (Metaphase I)",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((lx + 50, ly + 680), "→ most genetic variation happens here.",
           fill=MAROON, font=font("serif_ital", 26))

    # Right card: Meiosis II (equational)
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "MEIOSIS II", fill=ACCENT,
           font=font("serif_bold", 56))
    d.text((rx + 30, ly + 90), "EQUATIONAL",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((rx + 30, ly + 140),
           "haploid  →  haploid  (n → n)",
           fill=INK, font=font("sans", 28))

    # Diagram: sister chromatids separate (like mitosis)
    cy2 = ly + 360
    sx2 = rx + 60
    # One haploid cell with 2 chromatids
    d.ellipse([sx2 - 30, cy2 - 90, sx2 + 110, cy2 + 90],
              outline=MAROON_DARK, width=4, fill=CREAM)
    d.line([(sx2 + 30, cy2 - 50), (sx2 + 30, cy2 + 50)], fill=MAROON_DARK, width=10)
    d.line([(sx2 + 46, cy2 - 50), (sx2 + 46, cy2 + 50)], fill=MAROON_DARK, width=10)
    d.text((sx2 - 10, cy2 + 110), "sisters",
           fill=MUTED, font=font("sans_bold", 22))

    # Arrow →
    d.line([(sx2 + 150, cy2), (sx2 + 230, cy2)], fill=MAROON_DARK, width=4)
    d.polygon([(sx2 + 230, cy2), (sx2 + 210, cy2 - 12), (sx2 + 210, cy2 + 12)],
              fill=MAROON_DARK)

    # Two haploid cells with 1 chromatid each
    for i in range(2):
        ccx = sx2 + 270 + i * 130
        d.ellipse([ccx - 50, cy2 - 70, ccx + 50, cy2 + 70],
                  outline=MAROON_DARK, width=4, fill=CREAM)
        d.line([(ccx, cy2 - 40), (ccx, cy2 + 40)], fill=MAROON_DARK, width=10)
    d.text((sx2 + 240, cy2 + 110), "single chromatids",
           fill=MUTED, font=font("sans_bold", 22))

    # Key facts
    d.rounded_rectangle([rx + 30, ly + 580, rx + rw - 30, ly + lh - 20],
                        radius=12, fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((rx + 50, ly + 600), "Just like mitosis,",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 50, ly + 640), "but on haploid cells.",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((rx + 50, ly + 680),
           "Result: 4 unique gametes.",
           fill=MAROON, font=font("serif_ital", 26))

    # Bottom: sources of variation
    d.rounded_rectangle([110, 970, W - 110, 1050], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "3 sources of variation:  crossing over  +  independent assortment  +  random fertilization.",
             font("sans_bold", 26), 992, MAROON_DARK)
deck.custom("09_meiosis_overview", meiosis_overview)


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "A man with hemophilia (X-linked recessive) marries a non-carrier woman.",
           "Daughters?     Sons?",
           hint="Pause now. Work the Punnett. Press play when you're ready.")

# 11 — duplicate for the answer-reveal section
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — linkage and recombination (custom: linkage map + recombination frequency)
def linkage_recombination(img, d):
    d.text((110, 70), "Linkage  &  recombination.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 155),
           "Two genes on the same chromosome can be inherited together — and crossing over breaks the link.",
           fill=MUTED, font=font("sans", 26))

    # Left: chromosome diagram with 3 gene loci
    lx, ly = 110, 240
    lw, lh = 1020, 620
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "Linkage map",
           fill=MAROON_DARK, font=font("sans_bold", 34))
    d.text((lx + 30, ly + 70),
           "Distance is measured in centimorgans (cM).",
           fill=MUTED, font=font("sans", 26))
    d.text((lx + 30, ly + 110),
           "1 cM  =  1% recombination frequency.",
           fill=ACCENT, font=font("sans_bold", 26))

    # Horizontal chromosome
    chrx0 = lx + 80
    chrx1 = lx + lw - 80
    chr_y = ly + 280
    d.rectangle([chrx0, chr_y - 20, chrx1, chr_y + 20],
                fill=ACCENT_LT, outline=MAROON_DARK, width=4)
    # Centromere
    cmx = chrx0 + 130
    d.ellipse([cmx - 18, chr_y - 22, cmx + 18, chr_y + 22],
              fill=MAROON, outline=MAROON_DARK, width=3)

    # 3 gene loci: A, B, C at varying distances
    loci = [
        ("A", chrx0 + 230),
        ("B", chrx0 + 460),
        ("C", chrx0 + 770),
    ]
    for name, x in loci:
        d.line([(x, chr_y - 40), (x, chr_y + 40)], fill=MAROON_DARK, width=4)
        d.ellipse([x - 16, chr_y - 16, x + 16, chr_y + 16],
                  fill=ACCENT, outline=MAROON_DARK, width=3)
        d.text((x - 16, chr_y + 50), name, fill=MAROON_DARK,
               font=font("serif_bold", 44))

    # Distances
    pairs = [
        ("A", "B", loci[0][1], loci[1][1], "8 cM",  ly + 410),
        ("B", "C", loci[1][1], loci[2][1], "18 cM", ly + 410),
        ("A", "C", loci[0][1], loci[2][1], "26 cM", ly + 480),
    ]
    for n1, n2, x1, x2, label, ydis in pairs:
        d.line([(x1, ydis), (x2, ydis)], fill=ACCENT, width=3)
        d.line([(x1, ydis - 8), (x1, ydis + 8)], fill=ACCENT, width=3)
        d.line([(x2, ydis - 8), (x2, ydis + 8)], fill=ACCENT, width=3)
        midx = (x1 + x2) / 2
        lf = font("sans_bold", 26)
        tw = d.textlength(label, font=lf)
        d.text((midx - tw / 2, ydis + 15), label, fill=MAROON_DARK, font=lf)

    # Bottom note in card
    d.text((lx + 30, ly + 540),
           "A and B are close (8 cM)  →  tightly linked, often inherited together.",
           fill=INK, font=font("sans", 24))
    d.text((lx + 30, ly + 575),
           "A and C are far (26 cM)  →  closer to independent assortment.",
           fill=INK, font=font("sans", 24))

    # Right: recombination frequency rule
    rx = lx + lw + 30
    rw = W - 110 - rx
    rh = 620
    d.rounded_rectangle([rx, ly, rx + rw, ly + rh], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((rx + 30, ly + 30), "Recombination",
           fill=MAROON_DARK, font=font("serif_bold", 38))
    d.text((rx + 30, ly + 80), "frequency",
           fill=MAROON_DARK, font=font("serif_bold", 38))

    d.text((rx + 30, ly + 170),
           "% recombinant",
           fill=ACCENT, font=font("sans_bold", 26))
    d.text((rx + 30, ly + 205),
           "offspring",
           fill=ACCENT, font=font("sans_bold", 26))
    d.text((rx + 30, ly + 260), "─────────", fill=MAROON, font=font("mono", 28))

    d.text((rx + 30, ly + 320), "0%  →  fully linked",
           fill=INK, font=font("sans_bold", 24))
    d.text((rx + 30, ly + 360), "50% →  unlinked",
           fill=INK, font=font("sans_bold", 24))
    d.text((rx + 30, ly + 400), "         (independent)",
           fill=MUTED, font=font("sans", 22))
    d.text((rx + 30, ly + 460),
           "Max possible = 50%",
           fill=MAROON, font=font("serif_bold", 28))
    d.text((rx + 30, ly + 510),
           "because half the time",
           fill=MUTED, font=font("serif_ital", 22))
    d.text((rx + 30, ly + 540),
           "crossover swaps; half doesn't.",
           fill=MUTED, font=font("serif_ital", 22))

    # Bottom takeaway
    d.rounded_rectangle([110, 920, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Sturtevant, 1913:  used recombination frequencies to build the first gene map  —  as a college sophomore.",
             font("sans_bold", 28), 947, MAROON_DARK)
deck.custom("12_linkage_recombination", linkage_recombination)


# 13 — chromosomal disorders (custom: nondisjunction + 3 example cards)
def chromosomal_disorders(img, d):
    d.text((110, 70), "Nondisjunction  →  aneuploidy.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 155),
           "Chromosomes fail to separate in meiosis. Gametes end up with 1 too many or 1 too few.",
           fill=MUTED, font=font("sans", 26))

    # Top: nondisjunction diagram
    nx, ny = 110, 240
    nw, nh = W - 220, 260
    d.rounded_rectangle([nx, ny, nx + nw, ny + nh], radius=18,
                        outline=ACCENT, width=4, fill=CARD)
    d.text((nx + 30, ny + 20), "Normal vs. nondisjunction in meiosis I",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # Left: normal — 2 cells with 1 chromosome each
    cy_n = ny + 160
    d.text((nx + 30, ny + 80), "NORMAL", fill=ACCENT,
           font=font("sans_bold", 28))
    for i in range(2):
        ccx = nx + 100 + i * 130
        d.ellipse([ccx - 40, cy_n - 50, ccx + 40, cy_n + 50],
                  outline=MAROON_DARK, width=3, fill=ACCENT_LT)
        d.line([(ccx, cy_n - 25), (ccx, cy_n + 25)], fill=MAROON_DARK, width=8)
    d.text((nx + 70, ny + 220), "1 + 1  =  2  ✓",
           fill=MAROON_DARK, font=font("sans_bold", 26))

    # Right: nondisjunction — 1 cell has 2, 1 has 0
    d.text((nx + 600, ny + 80), "NONDISJUNCTION", fill=MAROON,
           font=font("sans_bold", 28))
    # Cell with 2 chromosomes
    ccx = nx + 700
    d.ellipse([ccx - 50, cy_n - 50, ccx + 50, cy_n + 50],
              outline=MAROON_DARK, width=3, fill=ACCENT_LT)
    d.line([(ccx - 20, cy_n - 25), (ccx - 20, cy_n + 25)], fill=MAROON_DARK, width=8)
    d.line([(ccx + 20, cy_n - 25), (ccx + 20, cy_n + 25)], fill=MAROON_DARK, width=8)
    # Cell with 0
    ccx2 = nx + 850
    d.ellipse([ccx2 - 50, cy_n - 50, ccx2 + 50, cy_n + 50],
              outline=MAROON_DARK, width=3, fill=ACCENT_LT)
    d.text((ccx2 - 10, cy_n - 10), "—", fill=MUTED, font=font("serif_bold", 36))
    d.text((nx + 600, ny + 220), "2 + 0  →  trisomy + monosomy",
           fill=MAROON, font=font("sans_bold", 26))

    # Three result cards
    results = [
        ("Trisomy 21", "Down syndrome",
         "Extra chromosome 21.",
         "Most common viable",
         "autosomal trisomy."),
        ("XXY", "Klinefelter syndrome",
         "Extra X in a male.",
         "Tall, often infertile,",
         "reduced testosterone."),
        ("XO", "Turner syndrome",
         "Only one X (no second).",
         "Female, short stature,",
         "often infertile."),
    ]
    cy_r = 580
    card_w = 580
    card_h = 320
    gap = 30
    start_x = (W - (card_w * 3 + gap * 2)) // 2
    for i, (name, sub, l1, l2, l3) in enumerate(results):
        x = start_x + i * (card_w + gap)
        d.rounded_rectangle([x, cy_r, x + card_w, cy_r + card_h], radius=18,
                            outline=MAROON_DARK, width=4, fill=ACCENT_LT)
        d.text((x + 30, cy_r + 20), name, fill=MAROON_DARK,
               font=font("serif_bold", 46))
        d.text((x + 30, cy_r + 90), sub, fill=ACCENT,
               font=font("sans_bold", 30))
        d.text((x + 30, cy_r + 160), l1, fill=INK, font=font("sans", 26))
        d.text((x + 30, cy_r + 200), l2, fill=INK, font=font("sans", 26))
        d.text((x + 30, cy_r + 240), l3, fill=INK, font=font("sans", 26))

    # Bottom polyploidy note
    d.rounded_rectangle([110, 940, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "Polyploidy  =  whole extra SETS.  Common in plants (wheat, strawberries).  Usually lethal in animals.",
             font("sans_bold", 28), 962, MAROON_DARK)
deck.custom("13_chromosomal_disorders", chromosomal_disorders)


# 14 — compare traps: incomplete dominance vs codominance
deck.compare("14_compare_traps",
             "Common trap  —  incomplete dominance vs. codominance.",
             left={"label": "INCOMPLETE DOMINANCE",
                   "color": MAROON,
                   "lines": [
                       "Heterozygote = BLEND.",
                       "(intermediate phenotype)",
                       "",
                       "Red × white  →  PINK.",
                       "",
                       "One new phenotype.",
                       "",
                       "Ratio 1 : 2 : 1",
                       "(no 3:1, het is distinct).",
                   ],
                   "footnote": "If heterozygote is a NEW look → incomplete."},
             right={"label": "CO-DOMINANCE",
                    "color": ACCENT,
                    "lines": [
                        "BOTH alleles fully shown.",
                        "(no blending — both visible)",
                        "",
                        "Type A + Type B  →  AB.",
                        "",
                        "Both phenotypes at once.",
                        "",
                        "Heterozygote shows",
                        "BOTH parents' traits.",
                    ],
                    "footnote": "If heterozygote shows BOTH → codominance."})


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Three laws:  segregation, independent assortment, dominance.",
    "Monohybrid Aa × Aa  →  1:2:1 genotype,  3:1 phenotype.",
    "Dihybrid AaBb × AaBb  →  9:3:3:1 phenotype (only if unlinked).",
    "Non-Mendelian:  incomplete dominance, codominance, multiple alleles, pleiotropy, polygenic, epistasis.",
    "X-linked recessive:  hemizygous males, skips generations, mother → son.",
    "Meiosis I separates HOMOLOGS; meiosis II separates SISTER CHROMATIDS.",
    "Linkage:  recombination frequency in cM measures map distance (max 50%).",
    "Nondisjunction  →  Trisomy 21, XXY Klinefelter, XO Turner.",
], assignment=[
    "1.  Work a full AaBb × AaBb dihybrid cross. Verify you get 9:3:3:1.",
    "2.  Pedigree challenge:  a trait skips generations and only affects males.  X-linked recessive — explain.",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Read OpenStax Biology",   "Chapters 12 and 13 — Mendel, meiosis, modern inheritance"),
    ("2.", "Khan Academy AP Bio",     "Unit 5 problem sets — Punnett squares, pedigrees, linkage"),
    ("3.", "Assignment in dashboard", "Dihybrid cross + X-linked pedigree question (above)"),
    ("4.", "Advisor check-in",        "If 9:3:3:1 or non-Mendelian patterns still feel fuzzy"),
], next_text="Next up:  Module 7 — DNA Structure and Replication  (Unit 6 begins).")


print("AP Biology Module 6 slides built.")

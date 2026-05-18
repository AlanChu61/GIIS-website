"""AP Biology · Module 8 — Gene Expression: Transcription and Translation.

Teal (science) theme auto-resolved from "AP Biology". 16 slides total.
Heavy on customs because the central dogma flow, the mRNA processing
diagram, the ribosome A/P/E sites, and the lac/trp operons each need
real visuals. Pause slide (10) is duplicated to 11 so the same image
plays during both Q and A.
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
deck = Deck(course="AP Biology", module_num=8, output_dir="slides", logo_path=LOGO)

ACCENT = deck.accent           # teal
ACCENT_LT = deck.accent_light  # light teal
CARD = deck.card_bg


# 01 — title
deck.title("01_title", "AP Biology",
           "Module 8 — Gene Expression: Transcription & Translation",
           "Sample lesson  ·  ~9 minutes")


# 02 — hook: 20,000 genes, 100,000 proteins + sickle-cell single-base story
def hook(img, d):
    d.text((110, 70), "20,000 genes.  100,000 proteins.",
           fill=MAROON, font=font("serif_bold", 64))

    # Left panel: the gene/protein math
    lx, ly, lw, lh = 140, 220, 760, 560
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    n1 = "~20,000"
    bf = font("serif_bold", 130)
    tw = d.textlength(n1, font=bf)
    d.text((lx + lw // 2 - tw / 2, ly + 60), n1,
           fill=MAROON_DARK, font=bf)
    cap = "genes in your genome"
    cf = font("sans_bold", 36)
    tw2 = d.textlength(cap, font=cf)
    d.text((lx + lw // 2 - tw2 / 2, ly + 220), cap,
           fill=ACCENT, font=cf)

    # Arrow down
    ax = lx + lw // 2
    d.line([(ax, ly + 290), (ax, ly + 340)], fill=MAROON_DARK, width=5)
    d.polygon([(ax, ly + 340), (ax - 14, ly + 322), (ax + 14, ly + 322)],
              fill=MAROON_DARK)
    splice_lbl = "alternative splicing"
    sf = font("serif_ital", 30)
    tw3 = d.textlength(splice_lbl, font=sf)
    d.text((lx + lw // 2 - tw3 / 2, ly + 350), splice_lbl,
           fill=MUTED, font=sf)

    n2 = "~100,000"
    tw4 = d.textlength(n2, font=bf)
    d.text((lx + lw // 2 - tw4 / 2, ly + 400), n2,
           fill=MAROON, font=bf)
    cap2 = "proteins your cells make"
    tw5 = d.textlength(cap2, font=cf)
    d.text((lx + lw // 2 - tw5 / 2, ly + 510), cap2,
           fill=ACCENT, font=cf)

    # Right panel: sickle-cell single-base story
    rx, ry, rw, rh = 1020, 220, 760, 560
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=28,
                        outline=ACCENT, width=6, fill=CARD)
    title2 = "One base.  Sickle-cell disease."
    t2f = font("serif_bold", 38)
    tw6 = d.textlength(title2, font=t2f)
    d.text((rx + rw // 2 - tw6 / 2, ry + 30), title2,
           fill=MAROON_DARK, font=t2f)

    # DNA codon swap visual
    code_y = ry + 130
    codon_f = font("mono", 72)
    # Normal
    d.text((rx + 50, code_y), "G A G", fill=MAROON_DARK, font=codon_f)
    d.text((rx + 280, code_y), "→", fill=MUTED, font=font("serif_bold", 60))
    d.text((rx + 360, code_y), "Glu", fill=ACCENT, font=font("serif_bold", 60))
    d.text((rx + 520, code_y + 5), "(normal)", fill=MUTED,
           font=font("serif_ital", 28))
    # Mutated
    d.text((rx + 50, code_y + 130), "G T G", fill=MAROON, font=codon_f)
    d.text((rx + 280, code_y + 130), "→", fill=MUTED, font=font("serif_bold", 60))
    d.text((rx + 360, code_y + 130), "Val", fill=MAROON, font=font("serif_bold", 60))
    d.text((rx + 520, code_y + 135), "(sickle)", fill=MAROON,
           font=font("serif_ital", 28))

    # Highlight the single base swap
    d.rectangle([rx + 110, code_y + 124, rx + 150, code_y + 200],
                outline=MAROON, width=4)
    d.text((rx + 50, code_y + 220), "A → T",
           fill=MAROON, font=font("sans_bold", 32))
    d.text((rx + 50, code_y + 270),
           "one nucleotide.",
           fill=INK, font=font("sans", 28))
    d.text((rx + 50, code_y + 310),
           "Whole-body disease.",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    # Bottom punchline strip
    d.rounded_rectangle([110, 820, W - 110, 940], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Today: how one letter of DNA becomes a protein — and what breaks when it goes wrong.",
             font("serif_bold", 32), 855, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Central dogma — DNA → RNA → protein (and the one exception).",
    "Transcription + mRNA processing in eukaryotes.",
    "Translation at the ribosome — codons, tRNAs, the genetic code.",
    "Gene regulation: prokaryote operons vs. eukaryote layers + mutations.",
], footnote="By the end: you can explain sickle-cell at the molecular level.")


# 04 — central dogma (custom: DNA → RNA → Protein horizontal flow)
def central_dogma(img, d):
    d.text((110, 70), "The central dogma  —  Crick, 1958.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160), "Information flows from DNA out to working protein.",
           fill=MUTED, font=font("sans", 30))

    # Three big boxes in a row
    boxes = [
        ("DNA", "stores info", "double helix", ACCENT_LT),
        ("mRNA", "the messenger", "single-stranded", ACCENT),
        ("PROTEIN", "does the work", "folded polypeptide", MAROON_DARK),
    ]
    box_w = 460
    box_h = 360
    gap = 130
    start_x = (W - (box_w * 3 + gap * 2)) // 2
    y0 = 260
    for i, (name, sub, sub2, col) in enumerate(boxes):
        x = start_x + i * (box_w + gap)
        # Use MAROON ink color on light, CREAM ink on dark
        ink_col = CREAM if col == MAROON_DARK else MAROON_DARK
        sub_col = ACCENT_LT if col == MAROON_DARK else MAROON
        d.rounded_rectangle([x, y0, x + box_w, y0 + box_h], radius=24,
                            outline=MAROON_DARK, width=6, fill=col)
        nf = font("serif_bold", 90)
        tw = d.textlength(name, font=nf)
        d.text((x + box_w // 2 - tw / 2, y0 + 60), name,
               fill=ink_col, font=nf)
        sf = font("sans_bold", 34)
        tw2 = d.textlength(sub, font=sf)
        d.text((x + box_w // 2 - tw2 / 2, y0 + 200), sub,
               fill=sub_col, font=sf)
        sf2 = font("serif_ital", 28)
        tw3 = d.textlength(sub2, font=sf2)
        d.text((x + box_w // 2 - tw3 / 2, y0 + 260), sub2,
               fill=ink_col, font=sf2)

        # Arrow + label between boxes
        if i < 2:
            ax = x + box_w + 10
            ay = y0 + box_h // 2
            d.line([(ax, ay), (ax + gap - 20, ay)],
                   fill=MAROON, width=6)
            d.polygon([(ax + gap - 20, ay),
                       (ax + gap - 40, ay - 16),
                       (ax + gap - 40, ay + 16)], fill=MAROON)
            arrow_lbl = "TRANSCRIPTION" if i == 0 else "TRANSLATION"
            af = font("sans_bold", 26)
            tw4 = d.textlength(arrow_lbl, font=af)
            d.text((ax + gap // 2 - tw4 / 2 - 10, ay - 50), arrow_lbl,
                   fill=MAROON_DARK, font=af)
            arrow_sub = "RNA pol" if i == 0 else "ribosome"
            sf3 = font("serif_ital", 22)
            tw5 = d.textlength(arrow_sub, font=sf3)
            d.text((ax + gap // 2 - tw5 / 2 - 10, ay + 18), arrow_sub,
                   fill=MUTED, font=sf3)

    # The exception arrow — RNA back to DNA (reverse transcriptase)
    rt_y = y0 + box_h + 100
    d.rounded_rectangle([start_x + box_w + gap - 30,
                         rt_y,
                         start_x + box_w + gap + box_w + 30,
                         rt_y + 110],
                        radius=18,
                        outline=MAROON, width=4, fill=ACCENT_LT)
    d.text((start_x + box_w + gap, rt_y + 14),
           "EXCEPTION  —  retroviruses",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((start_x + box_w + gap, rt_y + 56),
           "RNA → DNA via reverse transcriptase (HIV).",
           fill=INK, font=font("sans", 24))

    # Bottom note
    d.rounded_rectangle([110, 940, W - 110, 1020], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "DNA = library.  mRNA = photocopy you take out.  Protein = the thing you actually build.",
             font("sans_bold", 28), 962, MAROON_DARK)
deck.custom("04_central_dogma", central_dogma)


# 05 — transcription (custom: 3-step initiation/elongation/termination + strand directions)
def transcription(img, d):
    d.text((110, 70), "Transcription  —  eukaryotic.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160),
           "RNA Pol II reads template  3'→5'.  Builds mRNA  5'→3'.  U replaces T.",
           fill=ACCENT, font=font("sans_bold", 30))

    # Three stage cards
    stages = [
        ("1. INITIATION",
         "TATA box  ~25 bp upstream",
         "General TFs find the promoter.",
         "RNA Pol II locks on."),
        ("2. ELONGATION",
         "Template strand:  3' → 5'",
         "mRNA built:  5' → 3'",
         "U replaces T."),
        ("3. TERMINATION",
         "Terminator sequence reached.",
         "Pre-mRNA released.",
         "Ready for processing."),
    ]
    box_w = 540
    box_h = 480
    gap = 40
    start_x = (W - (box_w * 3 + gap * 2)) // 2
    y0 = 230
    for i, (name, line1, line2, line3) in enumerate(stages):
        x = start_x + i * (box_w + gap)
        col = ACCENT_LT if i % 2 == 0 else CARD
        d.rounded_rectangle([x, y0, x + box_w, y0 + box_h], radius=20,
                            outline=ACCENT, width=5, fill=col)
        d.text((x + 30, y0 + 24), name, fill=MAROON_DARK,
               font=font("sans_bold", 38))
        d.text((x + 30, y0 + 120), line1, fill=MAROON,
               font=font("sans_bold", 28))
        d.text((x + 30, y0 + 200), line2, fill=INK,
               font=font("sans", 28))
        d.text((x + 30, y0 + 260), line3, fill=INK,
               font=font("sans", 28))

        # Mini visual for each stage
        viz_y = y0 + 340
        if i == 0:
            # Promoter / TATA box
            d.rectangle([x + 30, viz_y, x + box_w - 30, viz_y + 30],
                        fill=ACCENT, outline=MAROON_DARK, width=3)
            d.text((x + 60, viz_y + 4), "TATA", fill=CREAM,
                   font=font("mono", 22))
            d.text((x + box_w - 200, viz_y + 4), "gene →",
                   fill=CREAM, font=font("mono", 22))
            d.text((x + 30, viz_y + 50),
                   "~25 bp upstream of gene",
                   fill=MUTED, font=font("serif_ital", 22))
        elif i == 1:
            # Polymerase reading template
            f_mono = font("mono", 26)
            d.text((x + 30, viz_y),
                   "DNA  3' ─T─A─C─G─T─T─ 5'", fill=MAROON_DARK,
                   font=f_mono)
            d.text((x + 30, viz_y + 36),
                   "mRNA 5' ─A─U─G─C─A─A─ 3'", fill=ACCENT,
                   font=f_mono)
            d.text((x + 30, viz_y + 76),
                   "(U not T)", fill=MAROON,
                   font=font("serif_ital", 22))
        elif i == 2:
            # Pre-mRNA released
            d.rectangle([x + 30, viz_y, x + box_w - 30, viz_y + 30],
                        fill=ACCENT_LT, outline=MAROON_DARK, width=3)
            d.text((x + 60, viz_y + 4), "pre-mRNA",
                   fill=MAROON_DARK, font=font("sans_bold", 22))
            d.text((x + 30, viz_y + 50),
                   "Next: 5' cap, poly-A, splicing",
                   fill=MUTED, font=font("serif_ital", 22))

    # Bottom directionality note
    d.rounded_rectangle([110, 740, W - 110, 870], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    d.text((140, 760),
           "Direction trap:",
           fill=MAROON, font=font("serif_bold", 32))
    d.text((140, 810),
           "Polymerase reads template 3'→5', but the mRNA grows 5'→3'.  Always opposite.",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((140, 920),
           "Coding strand = same sequence as mRNA (with T for U).  Template strand is what's read.",
           fill=INK, font=font("sans", 26))
deck.custom("05_transcription", transcription)


# 06 — mRNA processing (custom: pre-mRNA → mature mRNA with cap, tail, splicing)
def mrna_processing(img, d):
    d.text((110, 70), "mRNA processing  —  eukaryotes only.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160),
           "Three modifications before mRNA leaves the nucleus.",
           fill=MUTED, font=font("sans", 30))

    # Pre-mRNA bar with introns and exons
    bar_y = 280
    bar_h = 70
    bar_x0 = 180
    bar_x1 = W - 180
    span = bar_x1 - bar_x0

    # Segments: exon, intron, exon, intron, exon, intron, exon
    segs = [
        ("EXON",   ACCENT,    0.13),
        ("intron", ACCENT_LT, 0.12),
        ("EXON",   ACCENT,    0.17),
        ("intron", ACCENT_LT, 0.10),
        ("EXON",   ACCENT,    0.18),
        ("intron", ACCENT_LT, 0.10),
        ("EXON",   ACCENT,    0.20),
    ]
    d.text((110, bar_y - 50), "Pre-mRNA  (just transcribed):",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    sx = bar_x0
    for label, col, frac in segs:
        w = int(span * frac)
        d.rectangle([sx, bar_y, sx + w, bar_y + bar_h],
                    fill=col, outline=MAROON_DARK, width=3)
        lf = font("sans_bold", 22) if label == "EXON" else font("sans", 20)
        ink_c = CREAM if label == "EXON" else MAROON_DARK
        tw = d.textlength(label, font=lf)
        if w > tw + 10:
            d.text((sx + w // 2 - tw / 2, bar_y + 22), label,
                   fill=ink_c, font=lf)
        sx += w

    # Arrow down + spliceosome label
    arrow_x = W // 2
    d.line([(arrow_x, bar_y + bar_h + 30), (arrow_x, bar_y + bar_h + 130)],
           fill=MAROON, width=6)
    d.polygon([(arrow_x, bar_y + bar_h + 130),
               (arrow_x - 16, bar_y + bar_h + 110),
               (arrow_x + 16, bar_y + bar_h + 110)], fill=MAROON)
    d.text((arrow_x + 30, bar_y + bar_h + 50),
           "spliceosome  (snRNPs)",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((arrow_x + 30, bar_y + bar_h + 90),
           "removes introns,  joins exons",
           fill=INK, font=font("sans", 26))

    # Mature mRNA bar
    mat_y = bar_y + bar_h + 180
    d.text((110, mat_y - 50), "Mature mRNA  (ready to leave nucleus):",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    # 5' cap (a small G ball on the left)
    cap_x = bar_x0
    d.ellipse([cap_x - 40, mat_y - 5, cap_x + 30, mat_y + bar_h + 5],
              fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((cap_x - 25, mat_y + 18), "G", fill=CREAM,
           font=font("serif_bold", 38))
    d.text((cap_x - 60, mat_y + bar_h + 15), "5' cap",
           fill=MAROON_DARK, font=font("sans_bold", 22))
    d.text((cap_x - 70, mat_y + bar_h + 45), "(mod. guanine)",
           fill=MUTED, font=font("serif_ital", 20))

    # 4 exons joined
    exon_fracs = [0.18, 0.22, 0.22, 0.24]
    sx = bar_x0 + 40
    avail = bar_x1 - 40 - sx - 120  # leave room for tail
    total_frac = sum(exon_fracs)
    for i, frac in enumerate(exon_fracs):
        w = int(avail * (frac / total_frac))
        d.rectangle([sx, mat_y, sx + w, mat_y + bar_h],
                    fill=ACCENT, outline=MAROON_DARK, width=3)
        lf = font("sans_bold", 22)
        lbl = "EXON"
        tw = d.textlength(lbl, font=lf)
        d.text((sx + w // 2 - tw / 2, mat_y + 22), lbl,
               fill=CREAM, font=lf)
        sx += w

    # Poly-A tail — string of A's
    tail_x = sx + 5
    f_mono = font("mono", 30)
    d.text((tail_x, mat_y + 18), "AAAAAAA...",
           fill=MAROON_DARK, font=f_mono)
    d.text((tail_x, mat_y + bar_h + 15), "3' poly-A tail",
           fill=MAROON_DARK, font=font("sans_bold", 22))
    d.text((tail_x, mat_y + bar_h + 45), "(~200 A's)",
           fill=MUTED, font=font("serif_ital", 20))

    # Bottom three-up: cap / tail / splicing roles
    box_y = mat_y + bar_h + 120
    boxes = [
        ("5' CAP",
         "modified guanine",
         "protects mRNA  +  ribosome binding"),
        ("3' POLY-A TAIL",
         "~200 adenines",
         "protects mRNA  +  helps export"),
        ("SPLICING",
         "spliceosome / snRNPs",
         "alternative splicing → many proteins per gene"),
    ]
    bw = 540
    bh = 140
    bg = 40
    sx2 = (W - (bw * 3 + bg * 2)) // 2
    for i, (title, sub, foot) in enumerate(boxes):
        x = sx2 + i * (bw + bg)
        d.rounded_rectangle([x, box_y, x + bw, box_y + bh], radius=18,
                            outline=ACCENT, width=4, fill=CARD)
        d.text((x + 20, box_y + 14), title, fill=MAROON_DARK,
               font=font("sans_bold", 28))
        d.text((x + 20, box_y + 54), sub, fill=ACCENT,
               font=font("sans_bold", 22))
        d.text((x + 20, box_y + 90), foot, fill=INK,
               font=font("sans", 22))

    # Prokaryote contrast strip
    d.rounded_rectangle([110, 1010, W - 110, 1060], radius=14,
                        fill=ACCENT_LT, outline=MAROON, width=3)
    centered(d, "Prokaryotes skip ALL of this  —  no nucleus, no introns, transcription + translation coupled.",
             font("sans_bold", 24), 1022, MAROON_DARK)
deck.custom("06_mrna_processing", mrna_processing)


# 07 — translation machinery (custom: ribosome with A/P/E + codon table)
def translation_machinery(img, d):
    d.text((110, 70), "Translation machinery  —  ribosome  +  tRNAs  +  codons.",
           fill=MAROON, font=font("serif_bold", 50))

    # Left: ribosome with A/P/E sites
    lx, ly, lw, lh = 110, 180, 880, 760
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "Ribosome  (80S in eukaryotes)",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    d.text((lx + 30, ly + 70), "60S large  +  40S small  =  80S",
           fill=ACCENT, font=font("sans_bold", 26))

    # Large subunit (top half, blob)
    rcx = lx + lw // 2
    rcy = ly + 320
    d.ellipse([rcx - 280, rcy - 150, rcx + 280, rcy + 30],
              fill=ACCENT, outline=MAROON_DARK, width=4)
    d.text((rcx - 60, rcy - 100), "LARGE  (60S)",
           fill=CREAM, font=font("sans_bold", 28))

    # Small subunit (bottom half, slimmer blob)
    d.ellipse([rcx - 280, rcy + 30, rcx + 280, rcy + 150],
              fill=ACCENT_LT, outline=MAROON_DARK, width=4)
    d.text((rcx - 60, rcy + 70), "SMALL  (40S)",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    # mRNA strand running through
    mrna_y = rcy + 30
    d.line([(lx + 40, mrna_y), (lx + lw - 40, mrna_y)],
           fill=MAROON_DARK, width=6)
    d.text((lx + 50, mrna_y + 18), "5'", fill=MAROON,
           font=font("sans_bold", 24))
    d.text((lx + lw - 80, mrna_y + 18), "3'", fill=MAROON,
           font=font("sans_bold", 24))

    # Three sites E / P / A (left to right)
    site_y_top = rcy - 30
    site_y_bot = rcy + 30
    site_w = 80
    sites = [("E", rcx - 130), ("P", rcx - 25), ("A", rcx + 80)]
    for name, sx in sites:
        d.rectangle([sx, site_y_top, sx + site_w, site_y_bot],
                    fill=CARD, outline=MAROON_DARK, width=3)
        nf = font("serif_bold", 42)
        tw = d.textlength(name, font=nf)
        d.text((sx + site_w // 2 - tw / 2, site_y_top + 4), name,
               fill=MAROON, font=nf)

    # Labels under the ribosome
    d.text((lx + 60, ly + 540), "E site",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((lx + 60, ly + 580), "exit",
           fill=MUTED, font=font("serif_ital", 24))
    d.text((lx + 330, ly + 540), "P site",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((lx + 330, ly + 580), "peptidyl-tRNA",
           fill=MUTED, font=font("serif_ital", 24))
    d.text((lx + 600, ly + 540), "A site",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((lx + 600, ly + 580), "incoming aa-tRNA",
           fill=MUTED, font=font("serif_ital", 24))

    d.text((lx + 30, ly + 660),
           "tRNA  =  carries amino acid;  anticodon pairs with mRNA codon.",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 700),
           "Codon  =  3 mRNA bases  =  1 amino acid.",
           fill=INK, font=font("sans", 26))

    # Right: codon stats card
    rx = lx + lw + 30
    rw = W - 110 - rx
    rh = 760
    d.rounded_rectangle([rx, ly, rx + rw, ly + rh], radius=20,
                        outline=MAROON, width=5, fill=ACCENT_LT)
    d.text((rx + 30, ly + 20), "The genetic code",
           fill=MAROON_DARK, font=font("serif_bold", 44))

    # Big numbers
    d.text((rx + 30, ly + 110), "64", fill=MAROON,
           font=font("serif_bold", 90))
    d.text((rx + 180, ly + 140), "total codons",
           fill=MAROON_DARK, font=font("sans_bold", 30))

    d.text((rx + 30, ly + 240), "61", fill=MAROON,
           font=font("serif_bold", 70))
    d.text((rx + 160, ly + 260), "→ amino acids",
           fill=MAROON_DARK, font=font("sans_bold", 28))

    d.text((rx + 30, ly + 340), "3", fill=MAROON,
           font=font("serif_bold", 70))
    d.text((rx + 110, ly + 360), "→ STOP",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((rx + 110, ly + 400), "UAA · UAG · UGA",
           fill=MAROON_DARK, font=font("mono", 26))

    # START codon
    d.rounded_rectangle([rx + 30, ly + 470, rx + rw - 30, ly + 580],
                        radius=14, fill=CARD, outline=MAROON_DARK,
                        width=4)
    d.text((rx + 50, ly + 485), "START codon",
           fill=MAROON, font=font("sans_bold", 26))
    d.text((rx + 50, ly + 525), "AUG  =  Methionine",
           fill=MAROON_DARK, font=font("mono", 32))

    # Redundant + universal
    d.text((rx + 30, ly + 610),
           "Redundant",
           fill=ACCENT, font=font("sans_bold", 28))
    d.text((rx + 30, ly + 645),
           "(many codons → same",
           fill=INK, font=font("sans", 22))
    d.text((rx + 30, ly + 672),
           " amino acid)",
           fill=INK, font=font("sans", 22))
    d.text((rx + 30, ly + 705),
           "Nearly universal",
           fill=ACCENT, font=font("sans_bold", 28))
deck.custom("07_translation_machinery", translation_machinery)


# 08 — translation steps (custom: initiation/elongation/termination + ribozyme box)
def translation_steps(img, d):
    d.text((110, 70), "Translation steps  —  3 acts.",
           fill=MAROON, font=font("serif_bold", 60))

    stages = [
        ("1. INITIATION",
         "Small subunit binds 5' cap.",
         "Scans to first AUG.",
         "Large subunit joins.",
         "Met-tRNA in P site."),
        ("2. ELONGATION",
         "aa-tRNA enters A site.",
         "Peptide bond forms (rRNA!)",
         "Ribosome translocates.",
         "tRNA shifts A → P → E."),
        ("3. TERMINATION",
         "Stop codon enters A site.",
         "Release factor binds.",
         "Polypeptide released.",
         "Ribosome disassembles."),
    ]
    box_w = 540
    box_h = 520
    gap = 40
    start_x = (W - (box_w * 3 + gap * 2)) // 2
    y0 = 200
    for i, (name, l1, l2, l3, l4) in enumerate(stages):
        x = start_x + i * (box_w + gap)
        col = ACCENT_LT if i % 2 == 0 else CARD
        d.rounded_rectangle([x, y0, x + box_w, y0 + box_h], radius=20,
                            outline=ACCENT, width=5, fill=col)
        d.text((x + 30, y0 + 24), name, fill=MAROON_DARK,
               font=font("sans_bold", 38))
        lines = [l1, l2, l3, l4]
        ly = y0 + 110
        for ln in lines:
            d.text((x + 30, ly), "·", fill=MAROON,
                   font=font("serif_bold", 36))
            d.text((x + 60, ly + 4), ln, fill=INK,
                   font=font("sans", 28))
            ly += 70

        # Arrow to next
        if i < 2:
            ax = x + box_w + 4
            ay = y0 + box_h // 2
            d.polygon([(ax, ay - 22),
                       (ax + 30, ay),
                       (ax, ay + 22)], fill=ACCENT)

    # Bottom ribozyme box — the beautiful detail
    d.rounded_rectangle([110, 760, W - 110, 970], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    d.text((150, 780),
           "Key detail  —  the peptide bond is catalyzed by rRNA.",
           fill=MAROON_DARK, font=font("serif_bold", 38))
    d.text((150, 850),
           "rRNA = ribosomal RNA = RNA acting as an enzyme = a RIBOZYME.",
           fill=MAROON, font=font("sans_bold", 30))
    d.text((150, 905),
           "Evidence that early life was RNA-based — RNA can both store info and catalyze reactions.",
           fill=INK, font=font("serif_ital", 26))
deck.custom("08_translation_steps", translation_steps)


# 09 — prokaryote operons (custom: lac inducible vs trp repressible)
def prokaryote_operons(img, d):
    d.text((110, 70), "Prokaryote operons  —  lac vs. trp.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160),
           "lac is INDUCIBLE.  trp is REPRESSIBLE.  Opposite logic.",
           fill=ACCENT, font=font("sans_bold", 30))

    # Left: lac operon
    lx, ly = 110, 230
    lw, lh = 870, 740
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=20,
                        outline=ACCENT, width=5, fill=CARD)
    d.text((lx + 30, ly + 20), "lac OPERON  —  INDUCIBLE",
           fill=ACCENT, font=font("sans_bold", 38))
    d.text((lx + 30, ly + 80), "Default state:  OFF",
           fill=MAROON_DARK, font=font("serif_bold", 30))
    d.text((lx + 30, ly + 130), "Job:  digest lactose.",
           fill=INK, font=font("sans", 28))

    # ON when lactose present
    d.text((lx + 30, ly + 200), "When lactose is around:",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((lx + 60, ly + 250),
           "1.  lactose → allolactose",
           fill=INK, font=font("sans", 26))
    d.text((lx + 60, ly + 290),
           "2.  allolactose disables the repressor",
           fill=INK, font=font("sans", 26))
    d.text((lx + 60, ly + 330),
           "3.  RNA pol transcribes the operon",
           fill=INK, font=font("sans", 26))
    d.text((lx + 60, ly + 370),
           "4.  enzymes digest lactose  ✓",
           fill=ACCENT, font=font("sans_bold", 26))

    # Mini gene strip with promoter, operator, genes
    strip_y = ly + 440
    d.rectangle([lx + 30, strip_y, lx + 130, strip_y + 60],
                fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((lx + 40, strip_y + 18), "Prom.", fill=MAROON_DARK,
           font=font("sans_bold", 22))
    d.rectangle([lx + 130, strip_y, lx + 240, strip_y + 60],
                fill=ACCENT, outline=MAROON_DARK, width=3)
    d.text((lx + 145, strip_y + 18), "Op.", fill=CREAM,
           font=font("sans_bold", 22))
    d.rectangle([lx + 240, strip_y, lx + lw - 30, strip_y + 60],
                fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((lx + 360, strip_y + 14), "lacZ · lacY · lacA",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # CAP boost note
    d.text((lx + 30, ly + 560),
           "Boost  —  if glucose is ALSO low:",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((lx + 60, ly + 605),
           "cAMP rises → binds CAP",
           fill=INK, font=font("sans", 26))
    d.text((lx + 60, ly + 640),
           "→ CAP boosts transcription further.",
           fill=INK, font=font("sans", 26))
    d.text((lx + 30, ly + 690),
           "Cell would rather use glucose than lactose.",
           fill=MUTED, font=font("serif_ital", 24))

    # Right: trp operon
    rx = lx + lw + 30
    rw = W - 110 - rx
    d.rounded_rectangle([rx, ly, rx + rw, ly + lh], radius=20,
                        outline=MAROON, width=5, fill=CARD)
    d.text((rx + 30, ly + 20), "trp OPERON  —  REPRESSIBLE",
           fill=MAROON_DARK, font=font("sans_bold", 38))
    d.text((rx + 30, ly + 80), "Default state:  ON",
           fill=MAROON_DARK, font=font("serif_bold", 30))
    d.text((rx + 30, ly + 130), "Job:  build tryptophan.",
           fill=INK, font=font("sans", 28))

    # OFF when trp abundant
    d.text((rx + 30, ly + 200), "When tryptophan is abundant:",
           fill=MAROON, font=font("sans_bold", 28))
    d.text((rx + 60, ly + 250),
           "1.  trp binds the repressor",
           fill=INK, font=font("sans", 26))
    d.text((rx + 60, ly + 290),
           "2.  active repressor binds operator",
           fill=INK, font=font("sans", 26))
    d.text((rx + 60, ly + 330),
           "3.  RNA pol blocked",
           fill=INK, font=font("sans", 26))
    d.text((rx + 60, ly + 370),
           "4.  trp synthesis stops  ✓",
           fill=MAROON, font=font("sans_bold", 26))

    # Mini gene strip
    strip_y = ly + 440
    d.rectangle([rx + 30, strip_y, rx + 130, strip_y + 60],
                fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((rx + 40, strip_y + 18), "Prom.", fill=MAROON_DARK,
           font=font("sans_bold", 22))
    d.rectangle([rx + 130, strip_y, rx + 240, strip_y + 60],
                fill=MAROON, outline=MAROON_DARK, width=3)
    d.text((rx + 145, strip_y + 18), "Op.", fill=CREAM,
           font=font("sans_bold", 22))
    d.rectangle([rx + 240, strip_y, rx + rw - 30, strip_y + 60],
                fill=ACCENT_LT, outline=MAROON_DARK, width=3)
    d.text((rx + 320, strip_y + 14), "trpE · D · C · B · A",
           fill=MAROON_DARK, font=font("sans_bold", 24))

    # Logic summary
    d.text((rx + 30, ly + 560),
           "Cell logic:",
           fill=MAROON_DARK, font=font("sans_bold", 28))
    d.text((rx + 60, ly + 605),
           "If we already have trp,",
           fill=INK, font=font("sans", 26))
    d.text((rx + 60, ly + 640),
           "stop making more.",
           fill=INK, font=font("sans", 26))
    d.text((rx + 30, ly + 690),
           "Negative feedback at the gene level.",
           fill=MUTED, font=font("serif_ital", 24))

    # Bottom summary strip
    d.rounded_rectangle([110, 990, W - 110, 1060], radius=18,
                        fill=ACCENT_LT, outline=MAROON, width=4)
    centered(d, "lac:  lactose turns it ON  (catabolism).      trp:  tryptophan turns it OFF  (biosynthesis).",
             font("sans_bold", 28), 1010, MAROON_DARK)
deck.custom("09_prokaryote_operons", prokaryote_operons)


# 10 — pause + try
deck.pause("10_pause1", "PAUSE  &  TRY",
           "Given an mRNA:  how many amino acids will the finished protein contain?",
           "5'-AUG-CCA-UAG-3'",
           hint="Pause now. Solve it. Press play when you're ready.")

# 11 — duplicate the pause slide
deck.duplicate("10_pause1", "11_pause1_silence")


# 12 — eukaryote regulation (custom: 5 layers of regulation)
def eukaryote_regulation(img, d):
    d.text((110, 70), "Eukaryote regulation  —  5 layers.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 160),
           "Each layer is a separate place to control which gene gets used.",
           fill=MUTED, font=font("sans", 30))

    layers = [
        ("1.  CHROMATIN",
         "DNA methylation = repressed",
         "Histone acetylation = activated",
         "(epigenetics — heritable but not mutation)"),
        ("2.  TRANSCRIPTION FACTORS",
         "Bind enhancers / silencers",
         "Mediator bridges to RNA Pol II",
         "Different TFs in different cell types"),
        ("3.  ALTERNATIVE SPLICING",
         "Different exon combinations",
         "→ many proteins from one gene",
         "(~20K genes → ~100K proteins)"),
        ("4.  miRNA  /  RNAi",
         "Short RNAs degrade mRNA",
         "Or block translation",
         "Post-transcriptional control"),
        ("5.  PROTEIN DEGRADATION",
         "Ubiquitin tags target",
         "Proteasome destroys it",
         "Post-translational control"),
    ]
    box_w = 360
    box_h = 460
    gap = 16
    start_x = (W - (box_w * 5 + gap * 4)) // 2
    y0 = 240
    for i, (name, l1, l2, l3) in enumerate(layers):
        x = start_x + i * (box_w + gap)
        col = ACCENT_LT if i % 2 == 0 else CARD
        d.rounded_rectangle([x, y0, x + box_w, y0 + box_h], radius=18,
                            outline=ACCENT, width=4, fill=col)
        d.text((x + 20, y0 + 20), name, fill=MAROON_DARK,
               font=font("sans_bold", 26))
        d.text((x + 20, y0 + 110), l1, fill=INK,
               font=font("sans", 22))
        d.text((x + 20, y0 + 180), l2, fill=INK,
               font=font("sans", 22))
        d.text((x + 20, y0 + 290), l3, fill=ACCENT,
               font=font("serif_ital", 22))
        # Stage marker
        marker = ["DNA", "DNA →", "RNA →", "mRNA", "protein"][i]
        d.text((x + 20, y0 + 400), marker, fill=MAROON,
               font=font("sans_bold", 24))

    # Bottom takeaway strip
    d.rounded_rectangle([110, 760, W - 110, 880], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    centered(d, "Where it goes wrong is where disease lives  —  each layer can be hijacked.",
             font("serif_bold", 32), 790, MAROON_DARK)
    centered(d, "Cancer therapy targets several of these layers (HDAC inhibitors, miRNA drugs, proteasome blockers).",
             font("serif_ital", 24), 840, MUTED)
deck.custom("12_eukaryote_regulation", eukaryote_regulation)


# 13 — mutations (custom: 4 types of point mutations + sickle-cell story)
def mutations(img, d):
    d.text((110, 70), "Mutations  —  4 types  +  sickle-cell.",
           fill=MAROON, font=font("serif_bold", 60))

    # Original reference sequence at the top
    f_mono = font("mono", 38)
    ref_y = 180
    d.text((110, ref_y - 40), "Original:",
           fill=MAROON_DARK, font=font("sans_bold", 26))
    d.text((110, ref_y), "AUG  CCA  GAG  UUU  UAA",
           fill=ACCENT, font=f_mono)
    d.text((110, ref_y + 50),
           "Met  Pro  Glu  Phe  STOP",
           fill=MAROON_DARK, font=font("mono", 28))

    # Four mutation cards
    muts = [
        ("SILENT",
         "AUG  CCA  GAA  UUU  UAA",
         "Met  Pro  Glu  Phe  STOP",
         "Glu still Glu  —  no protein change.",
         "Genetic code is redundant.",
         ACCENT),
        ("MISSENSE",
         "AUG  CCA  GUG  UUU  UAA",
         "Met  Pro  VAL  Phe  STOP",
         "Glu → Val.  Different amino acid.",
         "Sickle-cell:  β-globin pos 6.",
         MAROON),
        ("NONSENSE",
         "AUG  CCA  UAG  UUU  UAA",
         "Met  Pro  STOP  —  —",
         "Premature stop.",
         "Truncated, broken protein.",
         MAROON),
        ("FRAMESHIFT",
         "AUG  CCA  GAGU  UUU  AA",
         "Met  Pro  ???  ???  ???",
         "Insert/delete not ÷ 3.",
         "Reading frame ruined.",
         MAROON_DARK),
    ]
    bw = 410
    bh = 380
    bg = 14
    sx0 = (W - (bw * 4 + bg * 3)) // 2
    y0 = 290
    for i, (name, codons, aas, l1, l2, col) in enumerate(muts):
        x = sx0 + i * (bw + bg)
        d.rounded_rectangle([x, y0, x + bw, y0 + bh], radius=18,
                            outline=col, width=5, fill=CARD)
        d.text((x + 20, y0 + 14), name, fill=col,
               font=font("sans_bold", 32))
        d.text((x + 20, y0 + 80), codons, fill=ACCENT,
               font=font("mono", 22))
        d.text((x + 20, y0 + 125), aas, fill=MAROON_DARK,
               font=font("mono", 20))
        d.text((x + 20, y0 + 200), l1, fill=INK,
               font=font("sans", 22))
        d.text((x + 20, y0 + 250), l2, fill=col,
               font=font("serif_ital", 22))

    # Bottom sickle-cell highlight
    d.rounded_rectangle([110, 720, W - 110, 1000], radius=20,
                        fill=ACCENT_LT, outline=MAROON, width=5)
    d.text((140, 740), "Sickle-cell anemia  —  one base. One disease.",
           fill=MAROON_DARK, font=font("serif_bold", 40))
    d.text((140, 810),
           "β-globin gene, position 6:  codon  GAG  →  GTG  (one A→T in DNA).",
           fill=MAROON, font=font("mono", 26))
    d.text((140, 855),
           "Glutamate (polar, negative)  →  Valine (nonpolar).",
           fill=INK, font=font("sans", 28))
    d.text((140, 900),
           "Hemoglobin sticks together under low O₂  →  sickled red cells  →  pain crises, organ damage.",
           fill=INK, font=font("sans", 26))
    d.text((140, 945),
           "Mutations  =  ultimate source of new genetic variation for evolution.",
           fill=MAROON_DARK, font=font("serif_bold", 30))
deck.custom("13_mutations", mutations)


# 14 — compare traps: template strand vs coding strand
deck.compare("14_compare_traps",
             "Common traps  —  4 you must not mix up.",
             left={"label": "TEMPLATE STRAND",
                   "color": ACCENT,
                   "lines": [
                       "What RNA Pol reads.",
                       "Direction:  3' → 5'",
                       "",
                       "mRNA is COMPLEMENTARY",
                       "to template strand.",
                       "",
                       "AUG start always means",
                       "Methionine.",
                       "",
                       "Alt. splicing ≠ mutation.",
                   ],
                   "footnote": "If asked 'what is read' → template strand."},
             right={"label": "CODING STRAND",
                    "color": MAROON,
                    "lines": [
                        "NOT read by polymerase.",
                        "",
                        "Same sequence as mRNA",
                        "(with T instead of U).",
                        "",
                        "lac:  lactose turns ON.",
                        "trp:  tryptophan turns OFF.",
                        "",
                        "Mutations change DNA.",
                        "Splicing just picks exons.",
                    ],
                    "footnote": "If asked 'what matches mRNA' → coding strand."})


# 15 — recap
deck.recap("15_recap", "Recap.", [
    "Central dogma:  DNA → mRNA → protein.  Reverse transcriptase = the exception.",
    "Transcription:  RNA Pol II reads template 3'→5', builds mRNA 5'→3', U replaces T.",
    "mRNA processing (euk only):  5' cap, poly-A tail, splicing (spliceosome / snRNPs).",
    "Translation:  AUG starts (Met);  UAA, UAG, UGA stop;  rRNA catalyzes peptide bond (ribozyme).",
    "Prokaryote operons:  lac inducible (lactose ON);  trp repressible (tryptophan OFF).",
    "Eukaryote regulation:  chromatin, TFs, alt. splicing, miRNA, protein degradation.",
    "Mutations:  silent / missense / nonsense / frameshift.  Sickle-cell = missense, GAG→GTG.",
], assignment=[
    "1.  Write the mRNA for template strand  3'-TAC GGT TCA ATT-5'.  Translate to amino acids.",
    "2.  Explain in 3 sentences why one base change in β-globin causes sickle-cell.",
])


# 16 — path
deck.path("16_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read OpenStax Biology",    "Chapters 15 & 16 — transcription, translation, regulation"),
    ("2.", "Khan Academy AP Bio",      "Unit 6 problem sets — codon table + lac operon are exam staples"),
    ("3.", "Assignment in dashboard",  "Translate the mRNA + sickle-cell explanation (above)"),
    ("4.", "Advisor check-in",         "If the codon table or lac-vs-trp logic still feels fuzzy"),
], next_text="Next up:  Module 9 — Biotechnology  (PCR, gel electrophoresis, CRISPR).")


print("AP Biology Module 8 slides built.")

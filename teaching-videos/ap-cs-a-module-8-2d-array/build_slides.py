"""Module 8 — 2D Array (AP Computer Science A).

CS theme = steel-blue accent (auto-resolved from course name).
Java code rendered via deck.equation() — mono font. Lines kept short
(<=32 chars at 80pt) so they don't overflow. Two custom slides:
the hook (familiar grids — chess, image, spreadsheet) and the
applications (tic-tac-toe, gradebook, image grids).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED, GRID, CREAM,
)

deck = Deck(course="AP Computer Science A", module_num=8,
            output_dir="slides", logo_path="../../src/img/logo_nobg.png")

ACCENT = deck.accent
ACCENT_LT = deck.accent_light
CARD = deck.card_bg


# ── 01 — title ──────────────────────────────────────────────────────────
deck.title("01_title", "AP Computer Science A",
           "Module 8 — 2D Array",
           "Sample lesson  ·  ~7 minutes")


# ── 02 — hook (custom: chess + image + spreadsheet) ────────────────────
def hook_render(img, d):
    d.text((110, 90), "Anywhere data is GRID-shaped.",
           fill=MAROON, font=font("serif_bold", 72))
    d.text((110, 180), "rows × columns",
           fill=ACCENT, font=font("sans_bold", 40))

    # Three grids side by side
    grid_y = 290
    grid_h = 480

    # Chess board (8x8, alternating)
    cb_x, cb_w = 130, 480
    cell = cb_w // 8
    for r in range(8):
        for c in range(8):
            color = CREAM if (r + c) % 2 == 0 else INK
            d.rectangle([cb_x + c * cell, grid_y + r * cell,
                         cb_x + (c + 1) * cell, grid_y + (r + 1) * cell],
                        fill=color)
    d.rectangle([cb_x, grid_y, cb_x + 8 * cell, grid_y + 8 * cell],
                outline=MAROON, width=4)
    centered_in(d, "CHESS  ·  8 × 8",
                font("sans_bold", 32), cb_x, cb_x + 8 * cell,
                grid_y + 8 * cell + 30, MAROON)

    # Image pixels (12x12, colored gradient)
    im_x, im_w = 730, 480
    px = im_w // 12
    for r in range(12):
        for c in range(12):
            # gradient-ish RGB
            red = 60 + r * 15
            green = 80 + c * 12
            blue = 160 - (r + c) * 5
            color = (max(0, min(255, red)),
                     max(0, min(255, green)),
                     max(0, min(255, blue)))
            d.rectangle([im_x + c * px, grid_y + r * px,
                         im_x + (c + 1) * px, grid_y + (r + 1) * px],
                        fill=color)
    d.rectangle([im_x, grid_y, im_x + 12 * px, grid_y + 12 * px],
                outline=MAROON, width=4)
    centered_in(d, "IMAGE  ·  rows × cols of pixels",
                font("sans_bold", 32), im_x, im_x + 12 * px,
                grid_y + 12 * px + 30, MAROON)

    # Spreadsheet (5 rows x 4 cols)
    sh_x, sh_w = 1330, 460
    rows, cols = 5, 4
    cw = sh_w // cols
    ch = grid_h // (rows + 1)
    # header row in accent
    d.rectangle([sh_x, grid_y, sh_x + cols * cw, grid_y + ch], fill=ACCENT)
    headers = ["A", "B", "C", "D"]
    for c in range(cols):
        hf = font("sans_bold", 30)
        cx = sh_x + c * cw + cw // 2
        tw = d.textlength(headers[c], font=hf)
        d.text((cx - tw / 2, grid_y + ch / 2 - 18), headers[c],
               fill=CREAM, font=hf)
    # body
    body_y = grid_y + ch
    for r in range(rows):
        for c in range(cols):
            x0 = sh_x + c * cw
            y0 = body_y + r * ch
            d.rectangle([x0, y0, x0 + cw, y0 + ch],
                        outline=GRID, width=2, fill=CARD)
    d.rectangle([sh_x, grid_y, sh_x + cols * cw, body_y + rows * ch],
                outline=MAROON, width=4)
    centered_in(d, "SPREADSHEET  ·  rows × cols",
                font("sans_bold", 32), sh_x, sh_x + cols * cw,
                body_y + rows * ch + 30, MAROON)

    d.text((110, 880),
           "Chess. Images. Spreadsheets. All grids → all 2D arrays.",
           fill=ACCENT, font=font("sans_bold", 36))


def centered_in(d, text, fnt, x0, x1, y, color):
    tw = d.textlength(text, font=fnt)
    d.text((x0 + (x1 - x0 - tw) / 2, y), text, fill=color, font=fnt)


deck.custom("02_hook", hook_render)


# ── 03 — overview ──────────────────────────────────────────────────────
deck.overview("03_overview", "Game plan.", [
    "Declare a 2D array and index into it.",
    "Traverse it — row-major and column-major.",
    "Real applications & the row/col confusion trap.",
], footnote="By the end you'll walk a grid as easily as a 1D array.")


# ── 04 — declaration ────────────────────────────────────────────────────
deck.equation("04_declaration", "Two ways to declare.", [
    ("int[][] grid =",         INK,    None),
    ("  new int[3][4];",       MAROON, "3 rows × 4 cols, all 0"),
    ("int[][] g =",            INK,    None),
    ("  {{1,2},{3,4},{5,6}};", MAROON, "literal — 3 rows × 2 cols"),
])


# ── 05 — dimensions ─────────────────────────────────────────────────────
deck.equation("05_dimensions", "A 2D array = array of arrays.", [
    ("grid.length",           MAROON, "→ number of rows (outer)"),
    ("grid[0].length",        MAROON, "→ number of cols (inner)"),
    ("int rows = grid.length;",   INK, None),
    ("int cols = grid[0].length;",INK, None),
])


# ── 06 — access ─────────────────────────────────────────────────────────
deck.equation("06_access", "Access by  [row][col].", [
    ("int[][] g = {{1,2},{3,4}};", INK,    None),
    ("g[0][0]  →  1",              MAROON, "top-left"),
    ("g[1][0]  →  3",              MAROON, "2nd row, 1st col"),
    ("g[0][1]  →  2",              MAROON, "1st row, 2nd col"),
])


# ── 07 — row-major traversal ────────────────────────────────────────────
deck.equation("07_row_major", "Row-major — nested for loops.", [
    ("for (int r=0; r<g.length; r++) {",    INK, None),
    ("  for (int c=0;",                     INK, None),
    ("       c<g[0].length; c++) {",        INK, "outer = row · inner = col"),
    ("    sum += g[r][c];",                 MAROON, None),
    ("  }",                                 INK, None),
    ("}",                                   INK, None),
])


# ── 08 — pause1 ─────────────────────────────────────────────────────────
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Sum all 9 elements of a 3×3 int grid",
           "with nested for loops.",
           hint="Outer loop rows 0–2, inner loop cols 0–2.")
deck.duplicate("08_pause1", "09_pause1_silence")


# ── 10 — column-major traversal ─────────────────────────────────────────
deck.equation("10_col_major", "Column-major — swap the loops.", [
    ("for (int c=0; c<cols; c++) {",  INK, None),
    ("  for (int r=0; r<rows; r++) {",INK, "outer = col · inner = row"),
    ("    print(g[r][c]);",           MAROON, "still [row][col] inside!"),
    ("  }",                           INK, None),
    ("}",                             INK, None),
])


# ── 11 — enhanced for, 2D ───────────────────────────────────────────────
deck.equation("11_enhanced_for_2d", "Nested enhanced-for.", [
    ("for (int[] row : g) {",  INK,    "each row is an int[]"),
    ("  for (int v : row) {",  INK,    "each v is one element"),
    ("    print(v);",          MAROON, None),
    ("  }",                    INK,    None),
    ("}",                      INK,    None),
])


# ── 12 — applications (custom: 3 small grids) ──────────────────────────
def applications_render(img, d):
    d.text((110, 90), "Real grids, real 2D arrays.",
           fill=MAROON, font=font("serif_bold", 72))

    g_y = 280
    g_h = 360

    # Tic-tac-toe (3x3 with X / O)
    tt_x, tt_w = 130, 460
    cell = tt_w // 3
    board = [["X", "O", "X"],
             [" ", "X", "O"],
             ["O", " ", "X"]]
    for r in range(3):
        for c in range(3):
            x0 = tt_x + c * cell
            y0 = g_y + r * cell
            d.rectangle([x0, y0, x0 + cell, y0 + cell],
                        outline=MAROON, width=4, fill=CARD)
            ch = board[r][c]
            if ch.strip():
                f = font("serif_bold", 110)
                tw = d.textlength(ch, font=f)
                color = ACCENT if ch == "X" else MAROON
                d.text((x0 + (cell - tw) / 2, y0 + 10), ch,
                       fill=color, font=f)
    centered_in(d, "TIC-TAC-TOE",
                font("sans_bold", 36), tt_x, tt_x + tt_w,
                g_y + 3 * cell + 30, MAROON)
    centered_in(d, "char[3][3]",
                font("sans", 28), tt_x, tt_x + tt_w,
                g_y + 3 * cell + 75, MUTED)

    # Gradebook (4 students x 4 tests)
    gb_x, gb_w = 730, 460
    rows, cols = 4, 4
    cw = gb_w // (cols + 1)  # +1 for student-name col
    ch_ = g_h // (rows + 1)  # +1 for header row
    students = ["Yunfan", "Baoyi", "Ruwen", "Tao"]
    tests = ["T1", "T2", "T3", "T4"]
    scores = [
        [92, 88, 95, 90],
        [78, 85, 82, 88],
        [88, 91, 87, 93],
        [95, 92, 96, 94],
    ]
    # header
    d.rectangle([gb_x, g_y, gb_x + (cols + 1) * cw, g_y + ch_],
                fill=ACCENT)
    for c in range(cols):
        hf = font("sans_bold", 26)
        x = gb_x + (c + 1) * cw + cw / 2
        tw = d.textlength(tests[c], font=hf)
        d.text((x - tw / 2, g_y + ch_ / 2 - 16), tests[c],
               fill=CREAM, font=hf)
    # body
    for r in range(rows):
        y0 = g_y + (r + 1) * ch_
        # name cell
        d.rectangle([gb_x, y0, gb_x + cw, y0 + ch_],
                    outline=GRID, width=2, fill=CARD)
        nf = font("sans_bold", 22)
        d.text((gb_x + 8, y0 + ch_ / 2 - 13), students[r],
               fill=INK, font=nf)
        for c in range(cols):
            x0 = gb_x + (c + 1) * cw
            d.rectangle([x0, y0, x0 + cw, y0 + ch_],
                        outline=GRID, width=2, fill=CARD)
            sf = font("sans_bold", 24)
            txt = str(scores[r][c])
            tw = d.textlength(txt, font=sf)
            d.text((x0 + (cw - tw) / 2, y0 + ch_ / 2 - 14), txt,
                   fill=INK, font=sf)
    d.rectangle([gb_x, g_y, gb_x + (cols + 1) * cw, g_y + (rows + 1) * ch_],
                outline=MAROON, width=4)
    centered_in(d, "GRADEBOOK",
                font("sans_bold", 36), gb_x, gb_x + (cols + 1) * cw,
                g_y + (rows + 1) * ch_ + 30, MAROON)
    centered_in(d, "int[students][tests]",
                font("sans", 28), gb_x, gb_x + (cols + 1) * cw,
                g_y + (rows + 1) * ch_ + 75, MUTED)

    # Image pixels (10x10)
    im_x, im_w = 1330, 460
    px = im_w // 10
    import math
    for r in range(10):
        for c in range(10):
            red   = max(0, min(255, 50 + r * 20 + c * 5))
            green = max(0, min(255, 100 + c * 15))
            blue  = max(0, min(255, 200 - r * 15))
            d.rectangle([im_x + c * px, g_y + r * px,
                         im_x + (c + 1) * px, g_y + (r + 1) * px],
                        fill=(red, green, blue))
    d.rectangle([im_x, g_y, im_x + 10 * px, g_y + 10 * px],
                outline=MAROON, width=4)
    centered_in(d, "IMAGE PIXELS",
                font("sans_bold", 36), im_x, im_x + 10 * px,
                g_y + 10 * px + 30, MAROON)
    centered_in(d, "Color[rows][cols]",
                font("sans", 28), im_x, im_x + 10 * px,
                g_y + 10 * px + 75, MUTED)

    d.text((110, 870),
           "Same nested-for pattern handles all three.",
           fill=ACCENT, font=font("sans_bold", 36))


deck.custom("12_applications", applications_render)


# ── 13 — compare (the row/col trap) ─────────────────────────────────────
deck.compare("13_compare", "The single most common 2D bug.",
    left={
        "label": "✗ WRONG",
        "color": RED,
        "lines": [
            "g[col][row]",
            "",
            "Swapping the order.",
            "First index ≠ column.",
            "First index = ROW.",
        ],
        "footnote": "This compiles and 'runs' — but reads the wrong cells.",
    },
    right={
        "label": "✓ RIGHT",
        "color": ACCENT,
        "lines": [
            "g[row][col]",
            "",
            "ALWAYS row first.",
            "1st index moves DOWN.",
            "2nd index moves ACROSS.",
        ],
        "footnote": "Picture the grid. Down, then across.",
    })


# ── 14 — recap ─────────────────────────────────────────────────────────
deck.recap("14_recap", "Recap.", [
    "2D array = array of arrays.",
    "Always  [row][col]  — never  [col][row].",
    "grid.length = rows · grid[0].length = cols.",
    "Nested for loops to traverse. Row-major is standard.",
    "Tic-tac-toe, gradebook, image — all 2D grids.",
], assignment=[
    "Print a 4×4 multiplication table using nested for loops.",
    "Row r × column c → cell (r+1) * (c+1).",
])


# ── 15 — path ──────────────────────────────────────────────────────────
deck.path("15_path", [
    ("✓",  "Watch this lesson",       "(done!)"),
    ("1.", "Runestone 2D Array",      "Interactive code traces — chapter on 2D arrays"),
    ("2.", "Codingbat AP-1 2D",       "Practice the 2D array problem set"),
    ("3.", "Assignment in dashboard", "4×4 multiplication table with nested for loops"),
    ("4.", "Advisor check-in",        "Book a session if column-major still feels fuzzy"),
], next_text="Next up:  Module 9 — Inheritance.")


print("Module 8 (2D Array) slides built via slide_kit.")

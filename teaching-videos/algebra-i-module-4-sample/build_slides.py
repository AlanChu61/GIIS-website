"""Render branded slides for Algebra I — Module 4 sample lecture (1920x1080).

Slide IDs match the section IDs in script.json so merge_lesson.py can pair them.
"""
from PIL import Image, ImageDraw, ImageFont
import os, shutil

OUT_DIR = "slides"
if os.path.exists(OUT_DIR):
    shutil.rmtree(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 1920, 1080
MAROON      = (107, 31, 42)
MAROON_DARK = (60, 0, 0)
GOLD        = (212, 166, 52)
GOLD_LIGHT  = (224, 192, 96)
CREAM       = (250, 246, 236)
INK         = (26, 29, 36)
MUTED       = (92, 101, 120)

SANS       = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD  = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
MONO       = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def font(p, s): return ImageFont.truetype(p, s)
def base(bg=CREAM, accent=True):
    img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
    if accent:
        d.rectangle([0, 0, W, 16], fill=MAROON)
        d.rectangle([0, 16, W, 22], fill=GOLD)
        d.rectangle([0, H-12, W, H], fill=MAROON)
        ft = font(SANS, 24)
        d.text((60, H-50), "GIIS  ·  Algebra I  ·  Module 4", fill=MUTED, font=ft)
        d.text((W-260, H-50), "Genesis of Ideas Intl.", fill=MUTED, font=ft)
    return img, d
def centered(d, text, fnt, y, color=INK):
    tw = d.textlength(text, font=fnt); d.text(((W-tw)/2, y), text, fill=color, font=fnt)

# IMPORTANT: filename must equal the section id in script.json so merge_lesson.py can find it.

# 01_title
def slide_01_title():
    img, d = base(bg=MAROON, accent=False)
    d.rectangle([0, H-160, W, H-152], fill=GOLD); d.rectangle([0, H-152, W, H-90], fill=MAROON_DARK)
    try:
        logo = Image.open("../../src/img/logo_nobg.png").convert("RGBA")
        logo.thumbnail((280, 280)); img.paste(logo, ((W-logo.width)//2, 110), logo)
    except Exception: pass
    centered(d, "GENESIS OF IDEAS INTERNATIONAL", font(SERIF_BOLD, 44), 410, GOLD)
    centered(d, "Algebra I", font(SERIF_BOLD, 96), 500, CREAM)
    centered(d, "Module 4 — Solving One-Step", font(SANS, 52), 640, CREAM)
    centered(d, "and Two-Step Equations", font(SANS, 52), 700, CREAM)
    centered(d, "Sample lesson  ·  ~6 minutes", font(SANS, 32), H-130, GOLD_LIGHT)
    img.save(f"{OUT_DIR}/01_title.png", optimize=True)

# 02_hook  — bubble tea opening
def slide_02_hook():
    img, d = base()
    d.text((110, 90), "You've done this before.", fill=MAROON, font=font(SERIF_BOLD, 76))
    d.text((110, 220), "Bubble tea, large.   Hand over $500.", fill=INK, font=font(SANS, 44))
    # Visual: receipt-like box
    box_x = 280; box_y = 360
    d.rounded_rectangle([box_x, box_y, box_x+700, box_y+340], radius=20, outline=MAROON, width=5)
    f_lab = font(SANS, 38); f_val = font(MONO, 48)
    d.text((box_x+50, box_y+50), "Tea price", fill=MUTED, font=f_lab)
    d.text((box_x+550, box_y+50), "$200", fill=INK, font=f_val)
    d.text((box_x+50, box_y+130), "You paid", fill=MUTED, font=f_lab)
    d.text((box_x+550, box_y+130), "$500", fill=INK, font=f_val)
    d.line([(box_x+40, box_y+200), (box_x+660, box_y+200)], fill=MAROON, width=2)
    d.text((box_x+50, box_y+220), "Change   $x", fill=MAROON, font=font(SANS_BOLD, 44))
    d.text((box_x+550, box_y+220), "$300", fill=GOLD, font=font(MONO, 56))
    d.text((1080, 480), "$200 + x = $500", fill=MAROON, font=font(MONO, 64))
    d.text((1080, 580), "x = $300", fill=GOLD, font=font(MONO, 64))
    d.text((1080, 680), "= algebra.", fill=INK, font=font(SERIF_BOLD, 60))
    # Caption removed — narration says it; on-slide text here collides with subs.
    img.save(f"{OUT_DIR}/02_hook.png", optimize=True)

# 03_overview
def slide_03_overview():
    img, d = base()
    d.text((110, 90), "Game plan", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        ("1.", "Equation = balance scale."),
        ("2.", "Inverse operations — the only move you need."),
        ("3.", "Knock out one-step equations."),
        ("4.", "Two-step equations — same idea, just stacked."),
        ("5.", "Always check by plugging back in."),
    ]
    y = 250
    for n, t in items:
        d.text((140, y), n, fill=GOLD, font=font(SERIF_BOLD, 64))
        d.text((250, y+10), t, fill=INK, font=font(SANS, 44))
        y += 110
    img.save(f"{OUT_DIR}/03_overview.png", optimize=True)

# 04_balance
def slide_04_balance():
    img, d = base()
    d.text((110, 90), "An equation is a balance.", fill=MAROON, font=font(SERIF_BOLD, 80))
    eq = "5 + x  =  12"; tw = d.textlength(eq, font=font(MONO, 96))
    d.text(((W-tw)/2, 280), eq, fill=INK, font=font(MONO, 96))
    cx, cy = W//2, 540
    d.rectangle([cx-360, cy-12, cx+360, cy+12], fill=MAROON)
    d.polygon([(cx-50, cy+12), (cx+50, cy+12), (cx, cy+120)], fill=GOLD)
    d.rectangle([cx-380, cy-50, cx-200, cy-12], outline=MAROON, width=4)
    d.text((cx-355, cy-46), "5 + x", fill=INK, font=font(MONO, 36))
    d.rectangle([cx+200, cy-50, cx+380, cy-12], outline=MAROON, width=4)
    d.text((cx+275, cy-46), "12", fill=INK, font=font(MONO, 36))
    d.text((110, 800), "Whatever you do to one side — do it to the other.", fill=GOLD, font=font(SANS_BOLD, 42))
    img.save(f"{OUT_DIR}/04_balance.png", optimize=True)

# 05_inverse
def slide_05_inverse():
    img, d = base()
    d.text((110, 90), "Inverse operations.", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.text((110, 210), "Operations that undo each other.", fill=MUTED, font=font(SANS, 38))
    pairs = [("+", "−"), ("×", "÷")]
    for i, (a, b) in enumerate(pairs):
        x = 200 + i*820; y = 360
        d.rounded_rectangle([x, y, x+720, y+280], radius=24, outline=MAROON, width=6)
        d.text((x+80, y+90), a, fill=MAROON, font=font(MONO, 140))
        d.text((x+340, y+105), "↔", fill=GOLD, font=font(SANS_BOLD, 110))
        d.text((x+520, y+90), b, fill=MAROON, font=font(MONO, 140))
    d.text((110, 750), "Use the inverse to peel off whatever is stuck to x.", fill=INK, font=font(SANS, 38))
    img.save(f"{OUT_DIR}/05_inverse.png", optimize=True)

def example_slide(title, lines, fname):
    img, d = base()
    d.text((110, 90), title, fill=MAROON, font=font(SERIF_BOLD, 72))
    f_eq = font(MONO, 80); f_n = font(SANS, 30)
    y = 240
    for t, c, note in lines:
        tw = d.textlength(t, font=f_eq)
        d.text(((W-tw)/2, y), t, fill=c, font=f_eq)
        if note:
            nw = d.textlength(note, font=f_n)
            d.text(((W-nw)/2, y+95), note, fill=GOLD, font=f_n)
        y += 150
    img.save(f"{OUT_DIR}/{fname}.png", optimize=True)

# 06_onestep1
def slide_06_onestep1():
    example_slide("Example 1 — One-step (addition)", [
        ("x + 5 = 12", INK, ""),
        ("x + 5 − 5 = 12 − 5", MUTED, "subtract 5 from both sides"),
        ("x = 7", MAROON, "solution"),
    ], "06_onestep1")

# 07_onestep2
def slide_07_onestep2():
    example_slide("Example 2 — One-step (multiplication)", [
        ("3x = 15", INK, ""),
        ("3x ÷ 3 = 15 ÷ 3", MUTED, "divide both sides by 3"),
        ("x = 5", MAROON, "solution"),
    ], "07_onestep2")

# 08_pause1 / 09_pause1_silence — same slide for both (the pause slide)
def slide_08_pause1():
    img, d = base()
    # Yellow pause banner
    d.rectangle([0, 80, W, 220], fill=GOLD)
    centered(d, "PAUSE  &  TRY", font(SERIF_BOLD, 96), 100, MAROON_DARK)
    d.text((110, 320), "Solve this on your own:", fill=INK, font=font(SANS, 48))
    centered(d, "x − 7 = 10", font(MONO, 160), 460, MAROON)
    d.text((110, 720), "Pause the video.", fill=MUTED, font=font(SANS, 40))
    d.text((110, 780), "Try it.", fill=MUTED, font=font(SANS, 40))
    d.text((110, 840), "Press play when you're ready.", fill=MUTED, font=font(SANS, 40))
    img.save(f"{OUT_DIR}/08_pause1.png", optimize=True)
    # 09 reuses the same slide (so the answer-reveal section keeps the question on screen)
    img.save(f"{OUT_DIR}/09_pause1_silence.png", optimize=True)

# 10_twostep_intro
def slide_10_twostep_intro():
    img, d = base()
    d.text((110, 90), "Two-step equations.", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.text((110, 220), "Two one-step problems stacked together.", fill=MUTED, font=font(SANS, 42))
    d.rounded_rectangle([110, 360, W-110, 720], radius=24, outline=MAROON, width=5)
    d.text((150, 400), "Order matters:", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((150, 510), "1. Undo  +  or  −  first.", fill=INK, font=font(SANS, 48))
    d.text((150, 600), "2. Then undo  ×  or  ÷.", fill=INK, font=font(SANS, 48))
    d.text((110, 770), "(PEMDAS — but in reverse.)", fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT_DIR}/10_twostep_intro.png", optimize=True)

# 11_twostep1
def slide_11_twostep1():
    img, d = base()
    d.text((110, 90), "Example 3 — Two-step", fill=MAROON, font=font(SERIF_BOLD, 72))
    f_eq = font(MONO, 76); f_n = font(SANS, 28)
    lines = [
        ("2x + 3 = 11", INK, ""),
        ("2x + 3 − 3 = 11 − 3", MUTED, "step 1: subtract 3 from both sides"),
        ("2x = 8", INK, ""),
        ("2x ÷ 2 = 8 ÷ 2", MUTED, "step 2: divide both sides by 2"),
        ("x = 4", MAROON, "solution"),
    ]
    y = 220
    for t, c, note in lines:
        tw = d.textlength(t, font=f_eq); d.text(((W-tw)/2, y), t, fill=c, font=f_eq)
        if note:
            nw = d.textlength(note, font=f_n); d.text(((W-nw)/2, y+88), note, fill=GOLD, font=f_n)
        y += 145
    img.save(f"{OUT_DIR}/11_twostep1.png", optimize=True)

# 12_pause2 / 13_pause2_silence
def slide_12_pause2():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    centered(d, "PAUSE  &  TRY  #2", font(SERIF_BOLD, 96), 100, MAROON_DARK)
    d.text((110, 320), "Two-step. You've got this:", fill=INK, font=font(SANS, 48))
    centered(d, "5x − 2 = 13", font(MONO, 160), 460, MAROON)
    d.text((110, 720), "Subtract / add first.  Then divide.", fill=MUTED, font=font(SANS, 40))
    d.text((110, 780), "Press play when you have x.", fill=MUTED, font=font(SANS, 40))
    img.save(f"{OUT_DIR}/12_pause2.png", optimize=True)
    img.save(f"{OUT_DIR}/13_pause2_silence.png", optimize=True)

# 14_twostep2
def slide_14_twostep2():
    img, d = base()
    d.text((110, 90), "Example 4 — Two-step", fill=MAROON, font=font(SERIF_BOLD, 72))
    f_eq = font(MONO, 76); f_n = font(SANS, 28)
    lines = [
        ("x/4 − 2 = 5", INK, ""),
        ("x/4 − 2 + 2 = 5 + 2", MUTED, "step 1: add 2 to both sides"),
        ("x/4 = 7", INK, ""),
        ("x/4 × 4 = 7 × 4", MUTED, "step 2: multiply both sides by 4"),
        ("x = 28", MAROON, "solution"),
    ]
    y = 220
    for t, c, note in lines:
        tw = d.textlength(t, font=f_eq); d.text(((W-tw)/2, y), t, fill=c, font=f_eq)
        if note:
            nw = d.textlength(note, font=f_n); d.text(((W-nw)/2, y+88), note, fill=GOLD, font=f_n)
        y += 145
    img.save(f"{OUT_DIR}/14_twostep2.png", optimize=True)

# 15_check
def slide_15_check():
    img, d = base()
    d.text((110, 90), "Check it. Always.", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.text((110, 220), "Substitute  x = 28  back into the original equation:", fill=INK, font=font(SANS, 36))
    f_eq = font(MONO, 80)
    lines = [("x/4 − 2 = 5", INK), ("28/4 − 2 = 5", MUTED), ("7 − 2 = 5", MUTED), ("5 = 5  ✓", MAROON)]
    y = 360
    for t, c in lines:
        tw = d.textlength(t, font=f_eq); d.text(((W-tw)/2, y), t, fill=c, font=f_eq); y += 130
    img.save(f"{OUT_DIR}/15_check.png", optimize=True)

# 16_recap
def slide_16_recap():
    img, d = base()
    d.text((110, 90), "Recap.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        "Equation = balance. Same move on both sides.",
        "Inverse operations isolate x.",
        "Two-step:  + / −  first, then  × / ÷.",
        "Always check by substituting back.",
    ]
    y = 230
    for t in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((200, y+10), t, fill=INK, font=font(SANS, 40))
        y += 95
    d.rounded_rectangle([110, 660, W-110, 920], radius=20, outline=MAROON, width=5)
    d.text((150, 690), "Assignment", fill=MAROON, font=font(SERIF_BOLD, 48))
    d.text((150, 770), "5 practice problems + 3 word problems in the dashboard.", fill=INK, font=font(SANS, 32))
    d.text((150, 820), "Next up: Module 5 — variables on both sides. Get spicy.", fill=INK, font=font(SANS, 32))
    img.save(f"{OUT_DIR}/16_recap.png", optimize=True)

for fn in [slide_01_title, slide_02_hook, slide_03_overview, slide_04_balance,
           slide_05_inverse, slide_06_onestep1, slide_07_onestep2,
           slide_08_pause1, slide_10_twostep_intro, slide_11_twostep1,
           slide_12_pause2, slide_14_twostep2, slide_15_check, slide_16_recap]:
    fn()
print("Slides built.")

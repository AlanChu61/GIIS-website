"""Render slides for Algebra I — Module 9 (Slope & Rate of Change). 1920x1080."""
from PIL import Image, ImageDraw, ImageFont
import os, shutil, math

OUT = "slides"
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT, exist_ok=True)

W, H = 1920, 1080
MAROON      = (107, 31, 42)
MAROON_DARK = (60, 0, 0)
GOLD        = (212, 166, 52)
GOLD_LIGHT  = (224, 192, 96)
CREAM       = (250, 246, 236)
INK         = (26, 29, 36)
MUTED       = (92, 101, 120)
GRID        = (210, 200, 180)

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
        d.text((60, H-50), "GIIS  ·  Algebra I  ·  Module 9", fill=MUTED, font=ft)
        d.text((W-260, H-50), "Genesis of Ideas Intl.", fill=MUTED, font=ft)
    return img, d
def centered(d, t, fnt, y, color=INK):
    tw = d.textlength(t, font=fnt); d.text(((W-tw)/2, y), t, fill=color, font=fnt)

def draw_axes(d, cx, cy, span=300, step=50, label=True):
    """Draw a Cartesian grid centered at (cx, cy) with given pixel span half-width and grid step."""
    # Grid lines
    for i in range(-span, span+1, step):
        d.line([(cx-span, cy+i), (cx+span, cy+i)], fill=GRID, width=1)
        d.line([(cx+i, cy-span), (cx+i, cy+span)], fill=GRID, width=1)
    # Axes
    d.line([(cx-span, cy), (cx+span, cy)], fill=INK, width=3)
    d.line([(cx, cy-span), (cx, cy+span)], fill=INK, width=3)
    # Tick labels (a few)
    fnt = font(SANS, 22)
    for i in [-200, -100, 100, 200]:
        if abs(i) <= span:
            n = i // step
            d.text((cx + i - 8, cy + 8), str(n), fill=MUTED, font=fnt)
            d.text((cx + 8, cy - i - 12), str(n), fill=MUTED, font=fnt)
    if label:
        d.text((cx + span + 20, cy - 10), "x", fill=INK, font=font(SANS_BOLD, 32))
        d.text((cx - 12, cy - span - 40), "y", fill=INK, font=font(SANS_BOLD, 32))

def to_px(cx, cy, x, y, step=50):
    return cx + x*step, cy - y*step

# 01_title
def s_01_title():
    img, d = base(bg=MAROON, accent=False)
    d.rectangle([0, H-160, W, H-152], fill=GOLD); d.rectangle([0, H-152, W, H-90], fill=MAROON_DARK)
    try:
        logo = Image.open("../../src/img/logo_nobg.png").convert("RGBA")
        logo.thumbnail((280, 280)); img.paste(logo, ((W-logo.width)//2, 110), logo)
    except Exception: pass
    centered(d, "GENESIS OF IDEAS INTERNATIONAL", font(SERIF_BOLD, 44), 410, GOLD)
    centered(d, "Algebra I", font(SERIF_BOLD, 96), 500, CREAM)
    centered(d, "Module 9 — Slope & Rate of Change", font(SANS, 52), 640, CREAM)
    centered(d, "Sample lesson  ·  ~6 minutes", font(SANS, 32), H-130, GOLD_LIGHT)
    img.save(f"{OUT}/01_title.png", optimize=True)

# 02_hook  — staircases gentle vs steep
def s_02_hook():
    img, d = base()
    d.text((110, 90), "Two staircases.", fill=MAROON, font=font(SERIF_BOLD, 80))
    # Left: gentle staircase
    sx, sy = 200, 750
    d.text((sx + 50, 250), "Gentle", fill=MUTED, font=font(SANS_BOLD, 36))
    for i in range(8):
        x0 = sx + i*60; y0 = sy - i*30
        d.rectangle([x0, y0, x0+60, y0+30], fill=GOLD_LIGHT, outline=MAROON, width=3)
    # Right: steep staircase
    sx2 = 1100
    d.text((sx2 + 50, 250), "Steep", fill=MUTED, font=font(SANS_BOLD, 36))
    for i in range(8):
        x0 = sx2 + i*40; y0 = sy - i*60
        d.rectangle([x0, y0, x0+40, y0+60], fill=MAROON, outline=MAROON_DARK, width=3)
    # Caption removed — the narration says it, and a slide caption here would
    # collide with the burned-in subtitle. Keep bottom 200 px clear.
    img.save(f"{OUT}/02_hook.png", optimize=True)

# 03_overview
def s_03_overview():
    img, d = base()
    d.text((110, 90), "Game plan", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        ("1.", "The formula:  rise over run."),
        ("2.", "Slope from two points."),
        ("3.", "Slope from a graph."),
        ("4.", "Positive, negative, zero, undefined."),
        ("5.", "Slope = rate of change in real life."),
    ]
    y = 250
    for n, t in items:
        d.text((140, y), n, fill=GOLD, font=font(SERIF_BOLD, 64))
        d.text((250, y+10), t, fill=INK, font=font(SANS, 44))
        y += 110
    img.save(f"{OUT}/03_overview.png", optimize=True)

# 04_formula
def s_04_formula():
    img, d = base()
    d.text((110, 90), "The formula.", fill=MAROON, font=font(SERIF_BOLD, 80))
    centered(d, "rise", font(SERIF_BOLD, 88), 290, INK)
    d.line([(W//2 - 130, 410), (W//2 + 130, 410)], fill=INK, width=6)
    centered(d, "run", font(SERIF_BOLD, 88), 425, INK)
    centered(d, "slope  =", font(SERIF_BOLD, 76), 340, MAROON)
    # actually re-layout cleaner:
    # Clear and redraw
    img2 = Image.new("RGB", (W, H), CREAM)
    d2 = ImageDraw.Draw(img2)
    d2.rectangle([0, 0, W, 16], fill=MAROON); d2.rectangle([0, 16, W, 22], fill=GOLD)
    d2.rectangle([0, H-12, W, H], fill=MAROON)
    ft = font(SANS, 24)
    d2.text((60, H-50), "GIIS  ·  Algebra I  ·  Module 9", fill=MUTED, font=ft)
    d2.text((W-260, H-50), "Genesis of Ideas Intl.", fill=MUTED, font=ft)
    d2.text((110, 90), "The formula.", fill=MAROON, font=font(SERIF_BOLD, 80))
    # Word form centered
    centered(d2, "slope  =  rise / run", font(SERIF_BOLD, 88), 290, INK)
    # Algebraic form
    f_eq = font(MONO, 92)
    centered(d2, "m  =  (y₂ − y₁) / (x₂ − x₁)", f_eq, 470, MAROON)
    # Caption
    centered(d2, "Two points.  Four numbers.  One division.", font(SANS, 42), 700, GOLD)
    img2.save(f"{OUT}/04_formula.png", optimize=True)

def graph_with_line(cx, cy, p1, p2, color=MAROON, label_p=True, span=300, step=50):
    """Helper used by example slides."""
    img, d = base()
    d.text((110, 90), "Find the slope", fill=MAROON, font=font(SERIF_BOLD, 72))
    draw_axes(d, cx, cy, span=span, step=step)
    x1, y1 = p1; x2, y2 = p2
    px1, py1 = to_px(cx, cy, x1, y1, step); px2, py2 = to_px(cx, cy, x2, y2, step)
    # Line through the two points (extend a bit)
    dx, dy = (px2 - px1), (py2 - py1)
    mag = max(1, math.hypot(dx, dy))
    ux, uy = dx/mag, dy/mag
    extend = span
    d.line([(px1 - ux*extend, py1 - uy*extend), (px2 + ux*extend, py2 + uy*extend)],
           fill=color, width=5)
    # Rise + run construction
    d.line([(px1, py1), (px2, py1)], fill=GOLD, width=4)   # run
    d.line([(px2, py1), (px2, py2)], fill=GOLD, width=4)   # rise
    # Points
    for px, py in [(px1, py1), (px2, py2)]:
        d.ellipse([px-12, py-12, px+12, py+12], fill=MAROON_DARK, outline=CREAM, width=3)
    if label_p:
        d.text((px1+18, py1-40), f"({x1}, {y1})", fill=INK, font=font(SANS_BOLD, 28))
        d.text((px2+18, py2-40), f"({x2}, {y2})", fill=INK, font=font(SANS_BOLD, 28))
    return img, d

# 05_example1
def s_05_example1():
    img, d = graph_with_line(W//2 - 250, 600, (1, 2), (4, 8), color=MAROON)
    # Right column: math
    rx = W - 700
    d.text((rx, 200), "(1, 2)  →  (4, 8)", fill=INK, font=font(MONO, 48))
    d.text((rx, 290), "rise = 8 − 2 = 6", fill=MUTED, font=font(MONO, 44))
    d.text((rx, 360), "run  = 4 − 1 = 3", fill=MUTED, font=font(MONO, 44))
    d.line([(rx, 440), (rx + 600, 440)], fill=INK, width=3)
    d.text((rx, 460), "m = 6 / 3 = 2", fill=MAROON, font=font(MONO, 56))
    d.text((rx, 560), "Up 2 for every right 1.", fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/05_example1.png", optimize=True)

# 06_example2 — negative slope
def s_06_example2():
    img, d = graph_with_line(W//2 - 250, 540, (-2, 5), (3, -5), color=MAROON, span=300, step=40)
    rx = W - 700
    d.text((rx, 200), "(−2, 5) → (3, −5)", fill=INK, font=font(MONO, 44))
    d.text((rx, 290), "rise = −5 − 5 = −10", fill=MUTED, font=font(MONO, 40))
    d.text((rx, 360), "run  = 3 − (−2) = 5", fill=MUTED, font=font(MONO, 40))
    d.line([(rx, 440), (rx + 620, 440)], fill=INK, width=3)
    d.text((rx, 460), "m = −10 / 5 = −2", fill=MAROON, font=font(MONO, 52))
    d.text((rx, 560), "Negative = downhill.", fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/06_example2.png", optimize=True)

# 07_pause1 / 08_pause1_silence
def s_07_pause1():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    centered(d, "PAUSE  &  TRY", font(SERIF_BOLD, 96), 100, MAROON_DARK)
    d.text((110, 320), "Find the slope between:", fill=INK, font=font(SANS, 48))
    centered(d, "(0, 4)   and   (6, 16)", font(MONO, 130), 470, MAROON)
    d.text((110, 720), "Pause. Solve. Press play when ready.", fill=MUTED, font=font(SANS, 40))
    img.save(f"{OUT}/07_pause1.png", optimize=True)
    img.save(f"{OUT}/08_pause1_silence.png", optimize=True)

# 09_from_graph
def s_09_from_graph():
    img, d = base()
    d.text((110, 90), "From a graph: count squares.", fill=MAROON, font=font(SERIF_BOLD, 64))
    cx, cy = W//2, 580
    draw_axes(d, cx, cy, span=300, step=50)
    p1 = (-3, -2); p2 = (3, 2)
    px1, py1 = to_px(cx, cy, *p1); px2, py2 = to_px(cx, cy, *p2)
    # Line
    dx, dy = px2-px1, py2-py1; mag = max(1, math.hypot(dx,dy)); ux, uy = dx/mag, dy/mag
    d.line([(px1-ux*250, py1-uy*250), (px2+ux*250, py2+uy*250)], fill=MAROON, width=5)
    d.line([(px1, py1), (px2, py1)], fill=GOLD, width=5)
    d.line([(px2, py1), (px2, py2)], fill=GOLD, width=5)
    for px, py in [(px1, py1), (px2, py2)]:
        d.ellipse([px-12, py-12, px+12, py+12], fill=MAROON_DARK, outline=CREAM, width=3)
    # Annotations
    d.text((px2 + 20, (py1+py2)//2 - 20), "rise = 4", fill=GOLD, font=font(SANS_BOLD, 32))
    d.text(((px1+px2)//2 - 50, py1 + 20), "run = 6", fill=GOLD, font=font(SANS_BOLD, 32))
    d.text((1380, 350), "rise / run", fill=MUTED, font=font(SANS_BOLD, 40))
    d.text((1380, 410), "= 4 / 6", fill=INK, font=font(MONO, 56))
    d.text((1380, 480), "= 2/3", fill=MAROON, font=font(MONO, 64))
    img.save(f"{OUT}/09_from_graph.png", optimize=True)

# 10_four_types
def s_10_four_types():
    img, d = base()
    d.text((110, 90), "Four flavors of slope.", fill=MAROON, font=font(SERIF_BOLD, 72))
    types = [
        ("Positive", "uphill", lambda d2, cx, cy: d2.line([(cx-100, cy+80), (cx+100, cy-80)], fill=MAROON, width=6)),
        ("Negative", "downhill", lambda d2, cx, cy: d2.line([(cx-100, cy-80), (cx+100, cy+80)], fill=MAROON, width=6)),
        ("Zero", "flat", lambda d2, cx, cy: d2.line([(cx-100, cy), (cx+100, cy)], fill=MAROON, width=6)),
        ("Undefined", "vertical", lambda d2, cx, cy: d2.line([(cx, cy-100), (cx, cy+100)], fill=MAROON, width=6)),
    ]
    for i, (name, sub, drawer) in enumerate(types):
        col = i % 2; row = i // 2
        x0 = 200 + col*820; y0 = 240 + row*340
        d.rounded_rectangle([x0, y0, x0+700, y0+280], radius=24, outline=MAROON, width=4)
        # mini axes
        cx = x0 + 230; cy = y0 + 140
        d.line([(cx-110, cy), (cx+110, cy)], fill=MUTED, width=2)
        d.line([(cx, cy-110), (cx, cy+110)], fill=MUTED, width=2)
        drawer(d, cx, cy)
        d.text((x0 + 470, y0 + 60), name, fill=MAROON, font=font(SERIF_BOLD, 44))
        d.text((x0 + 470, y0 + 130), sub, fill=GOLD, font=font(SANS, 32))
    img.save(f"{OUT}/10_four_types.png", optimize=True)

# 11_real_world
def s_11_real_world():
    img, d = base()
    d.text((110, 90), "Slope is everywhere.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        ("60 km/h", "60 km per 1 hour", "speed"),
        ("$500/mo", "$500 per 1 month", "savings rate"),
        ("8% grade", "0.08 rise per run", "road sign"),
        ("3 °C/hr", "3°C per 1 hour", "cooling rate"),
    ]
    y = 240
    for big, ratio, label in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 64))
        d.text((200, y+5), big, fill=MAROON, font=font(SERIF_BOLD, 56))
        d.text((600, y+18), f"= {ratio}", fill=INK, font=font(MONO, 38))
        d.text((1300, y+18), f"({label})", fill=MUTED, font=font(SANS, 34))
        y += 120
    d.text((110, 800), "When you hear 'rate of change' — that's just slope, dressed differently.",
           fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/11_real_world.png", optimize=True)

# 12_pause2 / 13_pause2_silence
def s_12_pause2():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    centered(d, "PAUSE  &  TRY  #2", font(SERIF_BOLD, 88), 105, MAROON_DARK)
    d.text((110, 290), "A water tank starts with 50 L.", fill=INK, font=font(SANS, 44))
    d.text((110, 370), "After 6 hours, 32 L remain.", fill=INK, font=font(SANS, 44))
    centered(d, "Find the rate of change", font(SERIF_BOLD, 56), 510, MAROON)
    centered(d, "(liters per hour)", font(SANS, 40), 580, MUTED)
    d.text((110, 760), "Time = x.   Water = y.   Hint: it'll be negative.",
           fill=MUTED, font=font(SANS, 36))
    img.save(f"{OUT}/12_pause2.png", optimize=True)
    img.save(f"{OUT}/13_pause2_silence.png", optimize=True)

# 14_warning
def s_14_warning():
    img, d = base()
    d.text((110, 90), "One trap to avoid.", fill=MAROON, font=font(SERIF_BOLD, 80))
    f_eq = font(MONO, 64)
    # Wrong / right
    d.rounded_rectangle([110, 240, 920, 720], radius=20, outline=(180, 50, 50), width=5)
    d.text((150, 270), "❌  WRONG", fill=(180, 50, 50), font=font(SERIF_BOLD, 48))
    d.text((150, 360), "y₂ − y₁", fill=INK, font=f_eq)
    d.line([(150, 440), (700, 440)], fill=INK, width=3)
    d.text((150, 460), "x₁ − x₂", fill=(180, 50, 50), font=f_eq)
    d.text((150, 600), "Mixed-up order", fill=MUTED, font=font(SANS, 32))
    d.text((150, 640), "→ flips the sign of m", fill=MUTED, font=font(SANS, 32))

    d.rounded_rectangle([1000, 240, 1810, 720], radius=20, outline=MAROON, width=5)
    d.text((1040, 270), "✓  RIGHT", fill=MAROON, font=font(SERIF_BOLD, 48))
    d.text((1040, 360), "y₂ − y₁", fill=INK, font=f_eq)
    d.line([(1040, 440), (1590, 440)], fill=INK, width=3)
    d.text((1040, 460), "x₂ − x₁", fill=INK, font=f_eq)
    d.text((1040, 600), "Pick point 1 — stay", fill=MUTED, font=font(SANS, 32))
    d.text((1040, 640), "consistent on top + bottom.", fill=MUTED, font=font(SANS, 32))
    img.save(f"{OUT}/14_warning.png", optimize=True)

# 15_recap
def s_15_recap():
    img, d = base()
    d.text((110, 90), "Recap.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        "Slope = rise / run = (y₂ − y₁) / (x₂ − x₁).",
        "Positive uphill, negative downhill, zero flat, vertical undefined.",
        "Slope = rate of change. Speed, savings, leakage — anything per anything.",
        "Pick point 1 — stay consistent on numerator and denominator.",
    ]
    y = 230
    for t in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((200, y+10), t, fill=INK, font=font(SANS, 36))
        y += 95
    d.rounded_rectangle([110, 660, W-110, 920], radius=20, outline=MAROON, width=5)
    d.text((150, 690), "Assignment", fill=MAROON, font=font(SERIF_BOLD, 48))
    d.text((150, 770), "10 point pairs to compute  +  1 real-world dataset to plot.",
           fill=INK, font=font(SANS, 32))
    d.text((150, 820), "Next: Module 10 — using slope to write line equations.",
           fill=INK, font=font(SANS, 32))
    img.save(f"{OUT}/15_recap.png", optimize=True)

for fn in [s_01_title, s_02_hook, s_03_overview, s_04_formula, s_05_example1,
           s_06_example2, s_07_pause1, s_09_from_graph, s_10_four_types,
           s_11_real_world, s_12_pause2, s_14_warning, s_15_recap]:
    fn()
print("Slides built.")

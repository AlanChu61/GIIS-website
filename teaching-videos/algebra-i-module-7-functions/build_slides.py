"""Slides for Algebra I — Module 7 (Introduction to Functions). 1920x1080."""
from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = "slides"
os.makedirs(OUT, exist_ok=True)

W, H = 1920, 1080
MAROON = (107, 31, 42); MAROON_DARK = (60, 0, 0)
GOLD = (212, 166, 52); GOLD_LIGHT = (224, 192, 96)
CREAM = (250, 246, 236); PARCHMENT = (244, 235, 215)
INK = (26, 29, 36); MUTED = (92, 101, 120)
GRID = (210, 200, 180)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def font(p, s): return ImageFont.truetype(p, s)
def base(bg=CREAM, accent=True):
    img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
    if accent:
        d.rectangle([0,0,W,16], fill=MAROON); d.rectangle([0,16,W,22], fill=GOLD)
        d.rectangle([0,H-12,W,H], fill=MAROON)
        ft = font(SANS, 24)
        d.text((60, H-50), "GIIS  ·  Algebra I  ·  Module 7", fill=MUTED, font=ft)
        d.text((W-260, H-50), "Genesis of Ideas Intl.", fill=MUTED, font=ft)
    return img, d
def cen(d, t, fnt, y, c=INK):
    tw = d.textlength(t, font=fnt); d.text(((W-tw)/2, y), t, fill=c, font=fnt)

def s_01_title():
    img, d = base(bg=MAROON, accent=False)
    d.rectangle([0,H-160,W,H-152], fill=GOLD); d.rectangle([0,H-152,W,H-90], fill=MAROON_DARK)
    try:
        logo = Image.open("../../src/img/logo_nobg.png").convert("RGBA")
        logo.thumbnail((280,280)); img.paste(logo, ((W-logo.width)//2, 110), logo)
    except: pass
    cen(d, "GENESIS OF IDEAS INTERNATIONAL", font(SERIF_BOLD, 44), 410, GOLD)
    cen(d, "Algebra I", font(SERIF_BOLD, 96), 500, CREAM)
    cen(d, "Module 7 — Introduction to Functions", font(SANS, 50), 640, CREAM)
    cen(d, "Sample lesson  ·  ~9 minutes", font(SANS, 32), H-130, GOLD_LIGHT)
    img.save(f"{OUT}/01_title.png", optimize=True)

def s_02_hook():
    img, d = base()
    d.text((110, 90), "It's just a vending machine.", fill=MAROON, font=font(SERIF_BOLD, 70))
    # Vending machine box
    vx, vy = 200, 240
    d.rounded_rectangle([vx, vy, vx+700, vy+560], radius=20, outline=MAROON, width=6)
    d.rounded_rectangle([vx+30, vy+30, vx+670, vy+360], radius=10, fill=PARCHMENT)
    # 6 product slots
    for i in range(2):
        for j in range(3):
            sx = vx + 60 + j*200; sy = vy + 60 + i*150
            d.rounded_rectangle([sx, sy, sx+170, sy+120], radius=8, outline=MUTED, width=2)
            label = ["A1","A2","A3","B1","B2","B3"][i*3+j]
            d.text((sx+55, sy+45), label, fill=MAROON, font=font(MONO, 36))
    # keypad
    d.rounded_rectangle([vx+250, vy+400, vx+450, vy+520], radius=10, fill=MUTED)
    d.text((vx+275, vy+430), "input: A1", fill=CREAM, font=font(MONO, 32))
    d.text((vx+295, vy+475), "→  Snickers", fill=GOLD, font=font(SANS_BOLD, 28))
    # Right side mapping diagram
    d.text((1100, 280), "input  →  output", fill=MAROON, font=font(SERIF_BOLD, 56))
    arrows = [("A1", "Snickers"), ("A2", "Doritos"), ("B1", "Coke")]
    for i, (k, v) in enumerate(arrows):
        y = 380 + i*90
        d.text((1100, y), k, fill=INK, font=font(MONO, 44))
        d.text((1180, y), "→", fill=GOLD, font=font(SANS_BOLD, 44))
        d.text((1240, y), v, fill=INK, font=font(SANS_BOLD, 38))
    d.text((1100, 690), "Same input always", fill=GOLD, font=font(SANS_BOLD, 36))
    d.text((1100, 740), "gives same output.", fill=GOLD, font=font(SANS_BOLD, 36))
    d.text((1100, 800), "= a function.", fill=MAROON, font=font(SERIF_BOLD, 56))
    img.save(f"{OUT}/02_hook.png", optimize=True)

def s_03_overview():
    img, d = base()
    d.text((110, 90), "Six things to cover.", fill=MAROON, font=font(SERIF_BOLD, 76))
    items = [("1.","What a function actually is"),
             ("2.","Function notation — that f(x) thing"),
             ("3.","Domain and range"),
             ("4.","Evaluating a function"),
             ("5.","Vertical line test"),
             ("6.","Real-world functions")]
    y = 230
    for n, t in items:
        d.text((140, y), n, fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((240, y+8), t, fill=INK, font=font(SANS, 40))
        y += 100
    img.save(f"{OUT}/03_overview.png", optimize=True)

def s_04_definition():
    img, d = base()
    d.text((110, 90), "What's a function?", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.rounded_rectangle([110, 250, W-110, 540], radius=24, outline=MAROON, width=5, fill=PARCHMENT)
    cen(d, "A rule where every input", font(SERIF_BOLD, 60), 290, INK)
    cen(d, "has", font(SERIF_BOLD, 50), 380, INK)
    cen(d, "EXACTLY ONE OUTPUT.", font(SERIF_BOLD, 64), 440, MAROON)
    # Visual: input → output
    cx = W // 2
    d.rounded_rectangle([cx-250, 660, cx-100, 760], radius=14, outline=MAROON, width=4)
    d.text((cx-220, 685), "input", fill=INK, font=font(SANS_BOLD, 40))
    d.text((cx-90, 690), "→", fill=GOLD, font=font(SANS_BOLD, 60))
    d.rounded_rectangle([cx+30, 660, cx+260, 760], radius=14, outline=MAROON, width=4, fill=PARCHMENT)
    d.text((cx+45, 685), "one output", fill=INK, font=font(SANS_BOLD, 40))
    d.text((110, 850), "Not zero.  Not two.  Exactly one.", fill=GOLD, font=font(SANS_BOLD, 38))
    img.save(f"{OUT}/04_definition.png", optimize=True)

def s_05_notation():
    img, d = base()
    d.text((110, 90), "Function notation.", fill=MAROON, font=font(SERIF_BOLD, 80))
    eq = "f(x) = 2x + 3"
    f_eq = font(MONO, 160)
    eq_w = d.textlength(eq, font=f_eq)
    eq_x = (W - eq_w) / 2
    d.text((eq_x, 280), eq, fill=INK, font=f_eq)
    f_lab = font(SANS_BOLD, 32); f_def = font(SANS, 28)
    # f
    d.line([(eq_x+20, 470), (eq_x-30, 580)], fill=GOLD, width=4)
    d.text((eq_x-200, 580), "name", fill=GOLD, font=f_lab)
    d.text((eq_x-200, 620), "of the function", fill=MUTED, font=f_def)
    # x
    d.line([(eq_x+90, 470), (eq_x+30, 580)], fill=MAROON, width=4)
    d.text((eq_x-50, 580), "input", fill=MAROON, font=f_lab)
    # = and beyond
    d.line([(eq_x+eq_w-100, 470), (eq_x+eq_w-150, 580)], fill=GOLD, width=4)
    d.text((eq_x+eq_w-280, 580), "the rule", fill=GOLD, font=f_lab)
    d.text((eq_x+eq_w-280, 620), "what the function does", fill=MUTED, font=f_def)
    cen(d, '"f of x"  — said out loud', font(SANS, 38), 760, MUTED)
    img.save(f"{OUT}/05_notation.png", optimize=True)

def s_06_evaluate():
    img, d = base()
    d.text((110, 90), "Evaluate  f(5).", fill=MAROON, font=font(SERIF_BOLD, 76))
    d.text((110, 200), "Given  f(x) = 2x + 3.   What's f(5)?", fill=INK, font=font(SANS, 40))
    f_eq = font(MONO, 80)
    lines = [("f(5) = 2(5) + 3", INK, "replace x with 5"),
             ("= 10 + 3", MUTED, "multiply"),
             ("= 13", MAROON, "answer")]
    y = 360
    for t, c, note in lines:
        tw = d.textlength(t, font=f_eq); d.text(((W-tw)/2, y), t, fill=c, font=f_eq)
        if note:
            f_n = font(SANS, 30); nw = d.textlength(note, font=f_n)
            d.text(((W-nw)/2, y+95), note, fill=GOLD, font=f_n)
        y += 150
    img.save(f"{OUT}/06_evaluate.png", optimize=True)

def s_07_warning():
    img, d = base()
    d.text((110, 90), "Read this twice.", fill=MAROON, font=font(SERIF_BOLD, 80))
    # WRONG
    d.rounded_rectangle([110, 270, 920, 720], radius=20, outline=(180,50,50), width=5, fill=PARCHMENT)
    d.text((150, 300), "❌  WRONG", fill=(180,50,50), font=font(SERIF_BOLD, 48))
    cen_wrong = "f(2)  =  f × 2"
    cen_wrong_w = d.textlength(cen_wrong, font=font(MONO, 80))
    d.text(((920+110-cen_wrong_w)/2, 460), cen_wrong, fill=INK, font=font(MONO, 80))
    d.text((150, 600), "f(2) is NOT f times 2.", fill=MUTED, font=font(SANS, 32))
    d.text((150, 650), "It's not multiplication.", fill=MUTED, font=font(SANS, 32))
    # RIGHT
    d.rounded_rectangle([1000, 270, 1810, 720], radius=20, outline=MAROON, width=5, fill=PARCHMENT)
    d.text((1040, 300), "✓  RIGHT", fill=MAROON, font=font(SERIF_BOLD, 48))
    cen_r = "f(2)  =  f at 2"
    cen_r_w = d.textlength(cen_r, font=font(MONO, 80))
    d.text(((1810+1000-cen_r_w)/2, 460), cen_r, fill=MAROON, font=font(MONO, 80))
    d.text((1040, 600), "Means: evaluate f", fill=INK, font=font(SANS, 32))
    d.text((1040, 650), "at the input  2.", fill=INK, font=font(SANS, 32))
    d.text((110, 800), "Memorize it.  This is on every quiz.", fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/07_warning.png", optimize=True)

def s_08_domain_range():
    img, d = base()
    d.text((110, 90), "Domain and range.", fill=MAROON, font=font(SERIF_BOLD, 80))
    # Domain box
    d.rounded_rectangle([110, 250, 920, 700], radius=20, outline=MAROON, width=5, fill=PARCHMENT)
    d.text((150, 280), "Domain", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((150, 360), "All allowed inputs.", fill=INK, font=font(SANS, 38))
    d.text((150, 480), "f(x) = 2x + 3", fill=INK, font=font(MONO, 44))
    d.text((150, 540), "→  all real numbers", fill=GOLD, font=font(SANS_BOLD, 36))
    d.text((150, 620), "(any x works)", fill=MUTED, font=font(SANS, 30))
    # Range box
    d.rounded_rectangle([1000, 250, 1810, 700], radius=20, outline=MAROON, width=5, fill=PARCHMENT)
    d.text((1040, 280), "Range", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((1040, 360), "All possible outputs.", fill=INK, font=font(SANS, 38))
    d.text((1040, 480), "f(x) = 2x + 3", fill=INK, font=font(MONO, 44))
    d.text((1040, 540), "→  all real numbers", fill=GOLD, font=font(SANS_BOLD, 36))
    d.text((1040, 620), "(any output reachable)", fill=MUTED, font=font(SANS, 30))
    # Caveat
    d.text((110, 780), "Watch out:  f(x) = 1/x  excludes  x = 0  (can't divide by zero).",
           fill=GOLD, font=font(SANS_BOLD, 32))
    img.save(f"{OUT}/08_domain_range.png", optimize=True)

def s_09_vertical_line():
    img, d = base()
    d.text((110, 90), "Vertical line test.", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.text((110, 200), "Vertical line crosses the graph more than once?  →  NOT a function.",
           fill=INK, font=font(SANS, 32))
    # Pass: parabola
    cx, cy = 480, 600
    span = 220
    for i in range(-span, span+1, 50):
        d.line([(cx-span, cy+i), (cx+span, cy+i)], fill=GRID, width=1)
        d.line([(cx+i, cy-span), (cx+i, cy+span)], fill=GRID, width=1)
    d.line([(cx-span, cy), (cx+span, cy)], fill=INK, width=2)
    d.line([(cx, cy-span), (cx, cy+span)], fill=INK, width=2)
    # Parabola y = x^2 / 50 (visual)
    pts = []
    for x_pix in range(-180, 181, 4):
        y_pix = (x_pix * x_pix) / 100
        if abs(y_pix) <= span:
            pts.append((cx + x_pix, cy - y_pix))
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=MAROON, width=4)
    # Vertical test line
    d.line([(cx+80, cy-span), (cx+80, cy+span)], fill=GOLD, width=3)
    d.text((280, 360), "y = x²", fill=INK, font=font(MONO, 36))
    d.text((280, 870), "✓  Function", fill=MAROON, font=font(SERIF_BOLD, 48))
    # Fail: circle
    cx2, cy2 = 1400, 600
    for i in range(-span, span+1, 50):
        d.line([(cx2-span, cy2+i), (cx2+span, cy2+i)], fill=GRID, width=1)
        d.line([(cx2+i, cy2-span), (cx2+i, cy2+span)], fill=GRID, width=1)
    d.line([(cx2-span, cy2), (cx2+span, cy2)], fill=INK, width=2)
    d.line([(cx2, cy2-span), (cx2, cy2+span)], fill=INK, width=2)
    d.ellipse([cx2-150, cy2-150, cx2+150, cy2+150], outline=MAROON, width=4)
    d.line([(cx2+50, cy2-span), (cx2+50, cy2+span)], fill=GOLD, width=3)
    d.text((1200, 360), "circle", fill=INK, font=font(MONO, 36))
    d.text((1200, 870), "✗  NOT a function", fill=(180,50,50), font=font(SERIF_BOLD, 48))
    img.save(f"{OUT}/09_vertical_line.png", optimize=True)

def s_10_pause1():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    cen(d, "PAUSE  &  TRY", font(SERIF_BOLD, 96), 100, MAROON_DARK)
    d.text((110, 320), "Given  f(x) = 3x − 4,  find:", fill=INK, font=font(SANS, 48))
    cen(d, "f(2)   and   f(−1)", font(MONO, 130), 470, MAROON)
    d.text((110, 720), "Pause and solve both.", fill=MUTED, font=font(SANS, 40))
    img.save(f"{OUT}/10_pause1.png", optimize=True)
    img.save(f"{OUT}/11_pause1_silence.png", optimize=True)

def s_12_real_world():
    img, d = base()
    d.text((110, 90), "Functions are everywhere.", fill=MAROON, font=font(SERIF_BOLD, 70))
    items = [
        ("Cost of x apples (50¢ each)",  "c(x) = 0.5x"),
        ("Celsius → Fahrenheit",          "f(c) = (9/5)c + 32"),
        ("15% income tax",                "t(x) = 0.15x"),
        ("Distance fallen in t seconds",  "d(t) = 4.9 t²"),
    ]
    y = 240
    for label, eq in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((200, y+12), label, fill=INK, font=font(SANS, 36))
        d.text((1080, y+12), eq, fill=MAROON, font=font(MONO, 44))
        y += 110
    d.text((110, 800), "Anything 'one number → one other number' is a function.",
           fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/12_real_world.png", optimize=True)

def s_13_pause2():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    cen(d, "PAUSE  &  TRY  #2", font(SERIF_BOLD, 88), 105, MAROON_DARK)
    d.text((110, 290), "g(x) = x² .  Find:", fill=INK, font=font(SANS, 44))
    cen(d, "g(3)   and   g(−3)", font(MONO, 130), 420, MAROON)
    d.text((110, 700), "Bonus:  same answer for both?  Why?",
           fill=GOLD, font=font(SANS_BOLD, 36))
    d.text((110, 760), "(Hint: it doesn't break the 'one input → one output' rule.)",
           fill=MUTED, font=font(SANS, 30))
    img.save(f"{OUT}/13_pause2.png", optimize=True)
    img.save(f"{OUT}/14_pause2_silence.png", optimize=True)

def s_15_recap():
    img, d = base()
    d.text((110, 90), "Recap.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        "Function — one input gives exactly one output.",
        "Notation — f(x).  NOT multiplication.",
        "Domain — allowed inputs.  Range — possible outputs.",
        "Vertical line test — crosses graph >1 time → not a function.",
        "Functions are everywhere: cost, conversion, tax, time.",
    ]
    y = 230
    for t in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((200, y+10), t, fill=INK, font=font(SANS, 34))
        y += 95
    img.save(f"{OUT}/15_recap.png", optimize=True)

def s_16_path():
    img, d = base()
    d.text((110, 80), "How to actually master this module.", fill=MAROON, font=font(SERIF_BOLD, 60))
    d.text((110, 170), "This video is ~15% of the work.  Here's the rest:",
           fill=MUTED, font=font(SANS, 34))
    items = [
        ("✓", "Watch this lesson", "(done!)", GOLD, GOLD),
        ("1.", "Read OpenStax  Ch 3.5", "Relations & Functions", MAROON, INK),
        ("2.", "Khan Academy practice", "Evaluating Functions", MAROON, INK),
        ("3.", "Assignment in dashboard", "Classify 5 relations · evaluate 10 inputs · state domain & range", MAROON, INK),
        ("4.", "Advisor check-in", "Function notation often clicks faster in 1-on-1", MAROON, INK),
    ]
    y = 280
    for n, head, sub, nc, hc in items:
        d.text((140, y), n, fill=nc, font=font(SERIF_BOLD, 44))
        d.text((230, y), head, fill=hc, font=font(SERIF_BOLD, 38))
        d.text((230, y+50), sub, fill=MUTED, font=font(SANS, 28))
        y += 110
    d.text((110, 870), "Next:  Module 8 — graphing linear functions.",
           fill=GOLD, font=font(SANS_BOLD, 32))
    img.save(f"{OUT}/16_path.png", optimize=True)

for fn in [s_01_title, s_02_hook, s_03_overview, s_04_definition, s_05_notation,
           s_06_evaluate, s_07_warning, s_08_domain_range, s_09_vertical_line,
           s_10_pause1, s_12_real_world, s_13_pause2, s_15_recap, s_16_path]:
    fn()
print("Module 7 slides built.")

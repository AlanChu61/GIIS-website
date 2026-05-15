"""Slides for Algebra I — Module 14 (Quadratic Equations). 1920x1080."""
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
        d.text((60, H-50), "GIIS  ·  Algebra I  ·  Module 14", fill=MUTED, font=ft)
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
    cen(d, "Module 14 — Quadratic Equations", font(SANS, 50), 640, CREAM)
    cen(d, "The boss fight  ·  ~12 minutes", font(SANS, 32), H-130, GOLD_LIGHT)
    img.save(f"{OUT}/01_title.png", optimize=True)

def s_02_hook():
    img, d = base()
    d.text((110, 90), "Throw a ball.", fill=MAROON, font=font(SERIF_BOLD, 80))
    # Parabola arc
    cx, cy = W//2, 700
    pts = []
    for x_pix in range(-700, 701, 8):
        y_pix = -(x_pix*x_pix) / 1500 + 350
        pts.append((cx + x_pix, cy - y_pix))
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=MAROON, width=6)
    # Ball at peak
    d.ellipse([cx-25, cy-340-25, cx+25, cy-340+25], fill=GOLD, outline=MAROON_DARK, width=3)
    # Ground
    d.line([(100, cy), (W-100, cy)], fill=INK, width=4)
    # Labels
    d.text((150, 250), "The path:", fill=MUTED, font=font(SANS_BOLD, 36))
    d.text((150, 300), "a parabola", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((1500, 250), "The math:", fill=MUTED, font=font(SANS_BOLD, 36))
    d.text((1380, 300), "quadratic", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((1480, 360), "equations", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((110, 850), "Physics. Engineering. Business. Anything that curves.",
           fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/02_hook.png", optimize=True)

def s_03_overview():
    img, d = base()
    d.text((110, 90), "Six big ideas.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [("1.","What a quadratic equation looks like"),
             ("2.","Method One — factoring"),
             ("3.","Method Two — completing the square"),
             ("4.","Method Three — quadratic formula"),
             ("5.","The discriminant — predict # of solutions"),
             ("6.","When to use which method")]
    y = 230
    for n, t in items:
        d.text((140, y), n, fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((240, y+8), t, fill=INK, font=font(SANS, 38))
        y += 100
    img.save(f"{OUT}/03_overview.png", optimize=True)

def s_04_form():
    img, d = base()
    d.text((110, 90), "Standard form.", fill=MAROON, font=font(SERIF_BOLD, 80))
    eq = "ax² + bx + c = 0"
    f_eq = font(MONO, 160)
    eq_w = d.textlength(eq, font=f_eq)
    eq_x = (W - eq_w) / 2
    d.text((eq_x, 320), eq, fill=INK, font=f_eq)
    # Annotation labels
    f_lab = font(SANS_BOLD, 32)
    d.line([(eq_x+90, 510), (eq_x+50, 600)], fill=GOLD, width=4)
    d.text((eq_x-50, 600), "x²  is the boss", fill=GOLD, font=f_lab)
    d.text((eq_x-50, 640), "(makes it quadratic)", fill=MUTED, font=font(SANS, 28))
    d.line([(eq_x+eq_w-150, 510), (eq_x+eq_w-100, 600)], fill=MAROON, width=4)
    d.text((eq_x+eq_w-180, 600), "= 0", fill=MAROON, font=f_lab)
    d.text((eq_x+eq_w-180, 640), "always equals zero", fill=MUTED, font=font(SANS, 28))
    d.text((110, 800), "a, b, c are just numbers.   Only rule:  a ≠ 0",
           fill=INK, font=font(SANS, 38))
    d.text((110, 850), "(if a = 0, the x² disappears and we're back to linear)",
           fill=MUTED, font=font(SANS, 30))
    img.save(f"{OUT}/04_form.png", optimize=True)

def method_intro_slide(method_num, method_name, idea, fname):
    img, d = base()
    d.text((110, 90), f"Method {method_num}.", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((110, 170), method_name, fill=MAROON, font=font(SERIF_BOLD, 80))
    d.rounded_rectangle([110, 350, W-110, 800], radius=24, outline=MAROON, width=5, fill=PARCHMENT)
    f_idea = font(SANS, 38); y = 400
    for line in idea:
        d.text((150, y), line, fill=INK, font=f_idea); y += 60
    img.save(f"{OUT}/{fname}.png", optimize=True)

def s_05_factoring_intro():
    method_intro_slide("1", "Factoring.", [
        "Rewrite as  (x − r)(x − s) = 0",
        "Two things multiply to zero  →  one of them must be zero.",
        "So  x = r  or  x = s.",
        "",
        "Fast — when the numbers are nice.",
    ], "05_factoring_intro")

def example_steps_slide(title, lines, fname):
    img, d = base()
    d.text((110, 90), title, fill=MAROON, font=font(SERIF_BOLD, 60))
    f_eq = font(MONO, 70); f_n = font(SANS, 28)
    y = 220
    for t, c, note in lines:
        tw = d.textlength(t, font=f_eq); d.text(((W-tw)/2, y), t, fill=c, font=f_eq)
        if note:
            nw = d.textlength(note, font=f_n)
            d.text(((W-nw)/2, y+85), note, fill=GOLD, font=f_n)
        y += 130
    img.save(f"{OUT}/{fname}.png", optimize=True)

def s_06_factoring_example():
    example_steps_slide("Example  ·  x² + 5x + 6 = 0", [
        ("x² + 5x + 6 = 0", INK, ""),
        ("(x + 2)(x + 3) = 0", MUTED, "two numbers multiply to 6, add to 5  →  2, 3"),
        ("x + 2 = 0   or   x + 3 = 0", MUTED, "set each factor to zero"),
        ("x = −2   or   x = −3", MAROON, "two solutions"),
    ], "06_factoring_example")

def s_07_pause1():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    cen(d, "PAUSE  &  TRY", font(SERIF_BOLD, 96), 100, MAROON_DARK)
    d.text((110, 320), "Solve by factoring:", fill=INK, font=font(SANS, 48))
    cen(d, "x² − 7x + 12 = 0", font(MONO, 140), 470, MAROON)
    d.text((110, 700), "Hint:  two numbers multiply to 12, add to −7.",
           fill=MUTED, font=font(SANS, 36))
    img.save(f"{OUT}/07_pause1.png", optimize=True)
    img.save(f"{OUT}/08_pause1_silence.png", optimize=True)

def s_09_completing_square_intro():
    method_intro_slide("2", "Completing the square.", [
        "Manipulate into  (x + p)² = q  form.",
        "Take square root of both sides.",
        "Solve.",
        "",
        "More steps than factoring — but it ALWAYS works.",
        "Also the proof technique behind the quadratic formula.",
    ], "09_completing_square_intro")

def s_10_completing_square_example():
    example_steps_slide("Example  ·  x² + 6x + 5 = 0", [
        ("x² + 6x + 5 = 0", INK, ""),
        ("x² + 6x = −5", MUTED, "move constant to right"),
        ("x² + 6x + 9 = 4", MUTED, "add (6/2)² = 9 to both sides"),
        ("(x + 3)² = 4", MUTED, "left side is now a perfect square"),
        ("x + 3 = ± 2", MUTED, "take square root — both signs"),
        ("x = −1   or   x = −5", MAROON, "two solutions"),
    ], "10_completing_square_example")

def s_11_quadratic_formula_intro():
    method_intro_slide("3", "The quadratic formula.", [
        "The universal solver.",
        "Works for EVERY quadratic — even ugly ones.",
        "",
        "Memorise this if you memorise nothing else.",
        "Pays rent for the next four years of math.",
    ], "11_quadratic_formula_intro")

def s_12_quadratic_formula():
    img, d = base()
    d.text((110, 90), "The quadratic formula.", fill=MAROON, font=font(SERIF_BOLD, 70))
    # Render as: x = -b ± √(b²-4ac) / 2a
    cx = W // 2
    f_main = font(MONO, 100)
    # Row 1: x =
    d.text((cx-450, 380), "x  =  ", fill=INK, font=f_main)
    # Numerator: -b ± √(b² - 4ac)
    num = "−b ± √(b² − 4ac)"
    num_w = d.textlength(num, font=f_main)
    d.text((cx-150, 320), num, fill=MAROON, font=f_main)
    # Bar
    d.line([(cx-160, 450), (cx+360, 450)], fill=INK, width=6)
    # Denominator: 2a
    den = "2a"
    den_w = d.textlength(den, font=f_main)
    d.text((cx+90 - den_w/2, 470), den, fill=MAROON, font=f_main)
    cen(d, "say it out loud until it's muscle memory", font(SANS_BOLD, 36), 700, GOLD)
    cen(d, "negative b, plus or minus, square root of b squared minus four ac, over two a",
        font(SANS, 28), 770, MUTED)
    img.save(f"{OUT}/12_quadratic_formula.png", optimize=True)

def s_13_quadratic_formula_example():
    example_steps_slide("Example  ·  x² − 4x − 5 = 0    (a=1, b=−4, c=−5)", [
        ("x = (4 ± √(16 + 20)) / 2", INK, "plug in"),
        ("x = (4 ± √36) / 2", MUTED, "simplify under root"),
        ("x = (4 ± 6) / 2", MUTED, ""),
        ("x = 5   or   x = −1", MAROON, "two solutions"),
    ], "13_quadratic_formula_example")

def s_14_pause2():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    cen(d, "PAUSE  &  TRY  #2", font(SERIF_BOLD, 88), 105, MAROON_DARK)
    d.text((110, 320), "Use the quadratic formula:", fill=INK, font=font(SANS, 48))
    cen(d, "2x² + 3x − 5 = 0", font(MONO, 130), 470, MAROON)
    d.text((110, 720), "a = 2,  b = 3,  c = −5", fill=MUTED, font=font(MONO, 40))
    img.save(f"{OUT}/14_pause2.png", optimize=True)
    img.save(f"{OUT}/15_pause2_silence.png", optimize=True)

def s_16_discriminant():
    img, d = base()
    d.text((110, 90), "The discriminant.", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.text((110, 220), "The bit under the square root.  By itself it tells you HOW MANY solutions.",
           fill=INK, font=font(SANS, 32))
    cen(d, "Δ  =  b² − 4ac", font(MONO, 130), 380, MAROON)
    d.text((110, 600), "Compute it BEFORE you start solving — saves time.",
           fill=GOLD, font=font(SANS_BOLD, 36))
    d.text((110, 660), "Three possible cases coming up.", fill=MUTED, font=font(SANS, 32))
    img.save(f"{OUT}/16_discriminant.png", optimize=True)

def s_17_three_cases():
    img, d = base()
    d.text((110, 90), "Three cases of  b² − 4ac.", fill=MAROON, font=font(SERIF_BOLD, 64))
    cases = [
        (">  0", "Two real solutions",  "parabola crosses x-axis twice"),
        ("=  0", "One solution (repeated)", "parabola just touches x-axis"),
        ("<  0", "Zero real solutions", "parabola never touches x-axis"),
    ]
    y = 250
    for cond, count, vis in cases:
        d.rounded_rectangle([110, y, W-110, y+170], radius=18, outline=MAROON, width=4, fill=PARCHMENT)
        d.text((150, y+30), f"Δ {cond}", fill=MAROON, font=font(MONO, 56))
        d.text((520, y+30), count, fill=INK, font=font(SERIF_BOLD, 44))
        d.text((520, y+95), vis, fill=MUTED, font=font(SANS, 30))
        y += 200
    img.save(f"{OUT}/17_three_cases.png", optimize=True)

def s_18_when_to_use():
    img, d = base()
    d.text((110, 90), "When to use which method.", fill=MAROON, font=font(SERIF_BOLD, 64))
    rows = [
        ("Factoring",          "Small whole-number coefficients.  Fastest when it works."),
        ("Completing square",  "When  a = 1  and  b  is even.  Clean arithmetic."),
        ("Quadratic formula",  "Always works.  Use when factoring fails or numbers are ugly."),
        ("Discriminant first", "Only need to know HOW MANY solutions — not what they are."),
    ]
    y = 240
    for name, when in rows:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 50))
        d.text((200, y+5), name, fill=MAROON, font=font(SERIF_BOLD, 40))
        d.text((720, y+15), when, fill=INK, font=font(SANS, 30))
        y += 110
    img.save(f"{OUT}/18_when_to_use.png", optimize=True)

def s_19_common_mistakes():
    img, d = base()
    d.text((110, 90), "Common mistakes.", fill=MAROON, font=font(SERIF_BOLD, 76))
    items = [
        ("1.", "Sign errors on b and c.",
               "Write a, b, c with their signs FIRST."),
        ("2.", "Forgetting BOTH ± solutions.",
               "Quadratics give two answers. Always."),
        ("3.", "Misreading the formula.",
               "Whole numerator over 2a. Not just −b over 2a."),
    ]
    y = 250
    for n, head, sub in items:
        d.text((140, y), n, fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((230, y+5), head, fill=INK, font=font(SERIF_BOLD, 42))
        d.text((230, y+65), sub, fill=MUTED, font=font(SANS, 32))
        y += 180
    img.save(f"{OUT}/19_common_mistakes.png", optimize=True)

def s_20_recap():
    img, d = base()
    d.text((110, 90), "Recap.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        "Quadratic form:  ax² + bx + c = 0.",
        "Three solving methods:  factoring, completing the square, quadratic formula.",
        "Discriminant  Δ = b² − 4ac  →  +/0/− tells you 2 / 1 / 0 real solutions.",
        "Try factoring first.  Fall back to the formula when things get ugly.",
    ]
    y = 250
    for t in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((200, y+10), t, fill=INK, font=font(SANS, 32))
        y += 100
    img.save(f"{OUT}/20_recap.png", optimize=True)

def s_21_path():
    img, d = base()
    d.text((110, 80), "How to actually master this module.", fill=MAROON, font=font(SERIF_BOLD, 60))
    d.text((110, 170), "This video is ~10% of the work.  Quadratics need REPS.",
           fill=MUTED, font=font(SANS, 34))
    items = [
        ("✓", "Watch this lesson", "(done!)", GOLD, GOLD),
        ("1.", "Read OpenStax  Ch 10.1–10.3", "Quadratic Equations", MAROON, INK),
        ("2.", "Khan Academy practice", "Quadratic Equations Practice — full set", MAROON, INK),
        ("3.", "Assignment in dashboard", "Solve 12 quadratics — 4 each method, verify with alternative", MAROON, INK),
        ("4.", "Advisor check-in", "20 minutes here unblocks the whole module", MAROON, INK),
    ]
    y = 280
    for n, head, sub, nc, hc in items:
        d.text((140, y), n, fill=nc, font=font(SERIF_BOLD, 44))
        d.text((230, y), head, fill=hc, font=font(SERIF_BOLD, 38))
        d.text((230, y+50), sub, fill=MUTED, font=font(SANS, 28))
        y += 110
    d.text((110, 870), "You've finished Algebra I.  Massive job.  See you in Geometry.",
           fill=GOLD, font=font(SANS_BOLD, 32))
    img.save(f"{OUT}/21_path.png", optimize=True)

for fn in [s_01_title, s_02_hook, s_03_overview, s_04_form,
           s_05_factoring_intro, s_06_factoring_example, s_07_pause1,
           s_09_completing_square_intro, s_10_completing_square_example,
           s_11_quadratic_formula_intro, s_12_quadratic_formula, s_13_quadratic_formula_example,
           s_14_pause2,
           s_16_discriminant, s_17_three_cases, s_18_when_to_use,
           s_19_common_mistakes, s_20_recap, s_21_path]:
    fn()
print("Module 14 slides built.")

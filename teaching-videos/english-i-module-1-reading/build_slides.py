"""Render slides for English I — Module 1 (Reading Comprehension Strategies). 1920x1080.

Different visual challenge from math: no equations, mostly text. Use:
  - Quote cards / passage excerpts in serif italic
  - Highlighted spans within passages
  - Side-by-side comparison cards
  - Annotation arrows
"""
from PIL import Image, ImageDraw, ImageFont
import os, shutil

OUT = "slides"
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT, exist_ok=True)

W, H = 1920, 1080
MAROON      = (107, 31, 42)
MAROON_DARK = (60, 0, 0)
GOLD        = (212, 166, 52)
GOLD_LIGHT  = (224, 192, 96)
CREAM       = (250, 246, 236)
PARCHMENT   = (244, 235, 215)   # warmer for passage backgrounds
INK         = (26, 29, 36)
MUTED       = (92, 101, 120)

SANS       = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD  = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF      = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_ITAL = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def font(p, s): return ImageFont.truetype(p, s)

def base(bg=CREAM, accent=True):
    img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
    if accent:
        d.rectangle([0, 0, W, 16], fill=MAROON)
        d.rectangle([0, 16, W, 22], fill=GOLD)
        d.rectangle([0, H-12, W, H], fill=MAROON)
        ft = font(SANS, 24)
        d.text((60, H-50), "GIIS  ·  English I  ·  Module 1", fill=MUTED, font=ft)
        d.text((W-260, H-50), "Genesis of Ideas Intl.", fill=MUTED, font=ft)
    return img, d

def centered(d, t, fnt, y, color=INK):
    tw = d.textlength(t, font=fnt); d.text(((W-tw)/2, y), t, fill=color, font=fnt)

def wrap(d, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if d.textlength(test, font=fnt) <= max_w:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

# 01_title
def s_01_title():
    img, d = base(bg=MAROON, accent=False)
    d.rectangle([0, H-160, W, H-152], fill=GOLD); d.rectangle([0, H-152, W, H-90], fill=MAROON_DARK)
    try:
        logo = Image.open("../../src/img/logo_nobg.png").convert("RGBA")
        logo.thumbnail((280, 280)); img.paste(logo, ((W-logo.width)//2, 110), logo)
    except Exception: pass
    centered(d, "GENESIS OF IDEAS INTERNATIONAL", font(SERIF_BOLD, 44), 410, GOLD)
    centered(d, "English I", font(SERIF_BOLD, 96), 500, CREAM)
    centered(d, "Module 1 — Reading Comprehension Strategies", font(SANS, 46), 640, CREAM)
    centered(d, "Sample lesson  ·  ~6 minutes", font(SANS, 32), H-130, GOLD_LIGHT)
    img.save(f"{OUT}/01_title.png", optimize=True)

# 02_hook  — eyes on page but mind elsewhere
def s_02_hook():
    img, d = base()
    d.text((110, 90), "Real talk.", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.rounded_rectangle([110, 240, W-110, 720], radius=24, outline=MAROON, width=4, fill=PARCHMENT)
    d.text((150, 270), "What just happened?", fill=MUTED, font=font(SANS, 32))
    sample = ("\"The mitochondria, often called the powerhouse of the cell, "
              "convert nutrients into ATP through oxidative phosphorylation, "
              "which involves a series of redox reactions across the inner "
              "membrane.\"")
    fnt = font(SERIF_ITAL, 38)
    y = 340
    for line in wrap(d, sample, fnt, W - 280):
        d.text((150, y), line, fill=INK, font=fnt); y += 56
    d.text((150, 620), "Eyes:  ✓ saw every word.", fill=MAROON_DARK, font=font(SANS_BOLD, 32))
    d.text((150, 670), "Brain: ✗ already in the lunch line.", fill=GOLD, font=font(SANS_BOLD, 32))
    d.text((110, 800), "Reading comprehension = keeping your brain in the room.",
           fill=INK, font=font(SANS, 40))
    img.save(f"{OUT}/02_hook.png", optimize=True)

# 03_overview — four tools
def s_03_overview():
    img, d = base()
    d.text((110, 90), "Four tools.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        ("1.", "Main idea", "the one-sentence summary"),
        ("2.", "Supporting details", "the evidence"),
        ("3.", "Inference", "reading between the lines"),
        ("4.", "Text structure", "the shape of the writing"),
    ]
    y = 250
    for n, name, sub in items:
        d.text((140, y), n, fill=GOLD, font=font(SERIF_BOLD, 64))
        d.text((250, y+5), name, fill=INK, font=font(SERIF_BOLD, 56))
        d.text((250, y+85), sub, fill=MUTED, font=font(SANS, 34))
        y += 160
    img.save(f"{OUT}/03_overview.png", optimize=True)

# 04_main_idea
def s_04_main_idea():
    img, d = base()
    d.text((110, 90), "Main idea — the writer's claim.", fill=MAROON, font=font(SERIF_BOLD, 64))
    # Bad vs good
    d.rounded_rectangle([110, 240, 920, 580], radius=20, outline=MUTED, width=4, fill=PARCHMENT)
    d.text((150, 270), "Topic", fill=MUTED, font=font(SANS_BOLD, 36))
    d.text((150, 330), "Cats.", fill=INK, font=font(SERIF_BOLD, 80))
    d.text((150, 460), "← too small. Just a noun.", fill=MUTED, font=font(SANS_ITAL_FALLBACK := SANS, 32))

    d.rounded_rectangle([1000, 240, 1810, 580], radius=20, outline=MAROON, width=4, fill=PARCHMENT)
    d.text((1040, 270), "Main idea", fill=MAROON, font=font(SANS_BOLD, 36))
    f_mi = font(SERIF_BOLD, 36)
    for i, line in enumerate([
        "Cats may be small,",
        "but they hunt like",
        "miniature engineers.",
    ]):
        d.text((1040, 340 + i*55), line, fill=INK, font=f_mi)
    d.text((1040, 530), "← topic + claim about it.", fill=GOLD, font=font(SANS, 32))

    d.text((110, 720), "Pro tip:  in nonfiction, look at the first or last paragraph.",
           fill=INK, font=font(SANS, 36))
    d.text((110, 780), "In fiction, ask:  what is the story trying to teach?",
           fill=INK, font=font(SANS, 36))
    img.save(f"{OUT}/04_main_idea.png", optimize=True)

# 05_supporting_details
def s_05_supporting_details():
    img, d = base()
    d.text((110, 90), "Supporting details — the evidence.", fill=MAROON, font=font(SERIF_BOLD, 60))
    # central main idea on top
    d.rounded_rectangle([300, 220, W-300, 360], radius=20, fill=MAROON, outline=MAROON_DARK, width=3)
    centered(d, "MAIN IDEA", font(SANS_BOLD, 30), 240, GOLD_LIGHT)
    centered(d, "Coral reefs are critical and in danger.", font(SERIF_BOLD, 42), 280, CREAM)
    # Three detail boxes below
    details = [
        "Shelter 25% of marine species",
        "Protect coastlines from storms",
        "Generate billions in tourism",
    ]
    box_y = 470
    for i, t in enumerate(details):
        x = 200 + i*540
        d.rounded_rectangle([x, box_y, x+480, box_y+200], radius=18, outline=GOLD, width=4, fill=PARCHMENT)
        d.text((x + 30, box_y + 30), f"detail {i+1}", fill=GOLD, font=font(SANS_BOLD, 28))
        for j, line in enumerate(wrap(d, t, font(SERIF_BOLD, 32), 420)):
            d.text((x + 30, box_y + 80 + j*42), line, fill=INK, font=font(SERIF_BOLD, 32))
        # Arrow up
        d.line([(x+240, box_y - 20), (x+240, box_y - 80)], fill=MAROON, width=4)
        d.polygon([(x+225, box_y - 20), (x+255, box_y - 20), (x+240, box_y)], fill=MAROON)
    d.text((110, 800), "Test:  does this sentence make the main idea more believable?",
           fill=GOLD, font=font(SANS_BOLD, 32))
    img.save(f"{OUT}/05_supporting_details.png", optimize=True)

# 06_pause1 / 07_pause1_silence — coral passage
def s_06_pause1():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    centered(d, "PAUSE  &  TRY", font(SERIF_BOLD, 96), 100, MAROON_DARK)
    # Passage
    d.rounded_rectangle([110, 270, W-110, 760], radius=20, outline=MAROON, width=4, fill=PARCHMENT)
    passage = ("Coral reefs cover less than one percent of the ocean floor, yet they are "
               "home to twenty-five percent of all marine species. They protect coastlines "
               "from storms, feed millions of people, and generate billions of dollars in "
               "tourism. But rising ocean temperatures are killing them faster than they "
               "can recover.")
    fnt = font(SERIF, 36)
    y = 310
    for line in wrap(d, passage, fnt, W - 280):
        d.text((150, y), line, fill=INK, font=fnt); y += 52
    d.text((110, 800), "Find:  the main idea  +  one supporting detail.", fill=MAROON, font=font(SANS_BOLD, 38))
    d.text((110, 860), "Pause now.  Press play when you're ready.", fill=MUTED, font=font(SANS, 32))
    img.save(f"{OUT}/06_pause1.png", optimize=True)
    img.save(f"{OUT}/07_pause1_silence.png", optimize=True)

# 08_inference  — Maya at the test
def s_08_inference():
    img, d = base()
    d.text((110, 90), "Inference — clues + your knowledge.", fill=MAROON, font=font(SERIF_BOLD, 56))
    # Quote
    d.rounded_rectangle([110, 230, W-110, 460], radius=20, outline=MAROON, width=3, fill=PARCHMENT)
    txt = '"Maya stared at the test paper, her hands trembling. She had studied for weeks, but now every formula felt like a stranger."'
    fnt = font(SERIF_ITAL, 38)
    y = 260
    for line in wrap(d, txt, fnt, W - 280):
        d.text((150, y), line, fill=INK, font=fnt); y += 56
    # Below: "what we read" → "what we infer"
    d.text((110, 510), "What the writer says:", fill=MUTED, font=font(SANS_BOLD, 32))
    d.text((150, 560), "•  hands trembling", fill=INK, font=font(SANS, 36))
    d.text((150, 610), "•  formulas felt like strangers", fill=INK, font=font(SANS, 36))

    # Right column: inference
    d.text((1000, 510), "What we infer:", fill=GOLD, font=font(SANS_BOLD, 32))
    d.text((1040, 560), "Maya is nervous.", fill=MAROON, font=font(SERIF_BOLD, 56))
    d.text((1040, 640), "Anxiety is common before exams.", fill=MUTED, font=font(SANS, 30))

    # Arrow
    d.line([(870, 580), (1000, 580)], fill=MAROON, width=4)
    d.polygon([(1000, 570), (1000, 590), (1015, 580)], fill=MAROON)

    d.text((110, 770), "The text never says \"Maya is nervous\" —", fill=INK, font=font(SANS, 36))
    d.text((110, 820), "but the clues add up.", fill=INK, font=font(SANS, 36))
    img.save(f"{OUT}/08_inference.png", optimize=True)

# 09_inference_rule
def s_09_inference_rule():
    img, d = base()
    d.text((110, 90), "Rule of inference.", fill=MAROON, font=font(SERIF_BOLD, 80))
    # Big rule card
    d.rounded_rectangle([110, 270, W-110, 560], radius=24, outline=MAROON, width=5, fill=PARCHMENT)
    centered(d, "If you can't point to it in the text,", font(SERIF_BOLD, 56), 320, INK)
    centered(d, "it's not an inference.", font(SERIF_BOLD, 64), 410, MAROON)
    centered(d, "It's a guess.", font(SERIF_BOLD, 56), 490, MUTED)
    # Two-column: inference vs guess
    d.rounded_rectangle([110, 620, 920, 920], radius=20, outline=MAROON, width=4, fill=PARCHMENT)
    d.text((150, 650), "✓  Inference", fill=MAROON, font=font(SERIF_BOLD, 44))
    d.text((150, 730), "\"Maya is nervous,", fill=INK, font=font(SERIF, 36))
    d.text((150, 780), "  because her hands tremble.\"", fill=INK, font=font(SERIF, 36))
    d.text((150, 850), "Evidence-based.", fill=GOLD, font=font(SANS_BOLD, 32))

    d.rounded_rectangle([1000, 620, 1810, 920], radius=20, outline=(180, 50, 50), width=4, fill=PARCHMENT)
    d.text((1040, 650), "✗  Guess", fill=(180, 50, 50), font=font(SERIF_BOLD, 44))
    d.text((1040, 730), "\"Maya hates math.\"", fill=INK, font=font(SERIF, 36))
    d.text((1040, 850), "No supporting evidence.", fill=MUTED, font=font(SANS_BOLD, 32))
    img.save(f"{OUT}/09_inference_rule.png", optimize=True)

# 10_text_structure — five common types
def s_10_text_structure():
    img, d = base()
    d.text((110, 90), "Five common text structures.", fill=MAROON, font=font(SERIF_BOLD, 60))
    items = [
        ("Chronological",      "events in time order",      "first → next → finally"),
        ("Cause & effect",     "why something happened",    "because → therefore"),
        ("Compare & contrast", "two things side by side",   "similarly / however"),
        ("Problem & solution", "issue + proposed fix",      "challenge → answer"),
        ("Description",        "painting a picture",        "sensory details"),
    ]
    y = 240
    for name, sub, sig in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((200, y+5), name, fill=MAROON, font=font(SERIF_BOLD, 40))
        d.text((680, y+15), sub, fill=INK, font=font(SANS, 32))
        d.text((1300, y+15), f"signal:  {sig}", fill=MUTED, font=font(SANS_BOLD, 28))
        y += 100
    d.text((110, 780), "Recognizing structure tells you what the writer is trying to do.",
           fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/10_text_structure.png", optimize=True)

# 11_pause2 / 12_pause2_silence  — germ theory
def s_11_pause2():
    img, d = base()
    d.rectangle([0, 80, W, 220], fill=GOLD)
    centered(d, "PAUSE  &  TRY  #2", font(SERIF_BOLD, 88), 105, MAROON_DARK)
    d.rounded_rectangle([110, 290, W-110, 580], radius=20, outline=MAROON, width=4, fill=PARCHMENT)
    txt = ('"In the 1800s, doctors believed bad smells caused disease. '
           'By 1900, scientists had proven it was actually invisible germs."')
    fnt = font(SERIF_ITAL, 42)
    y = 330
    for line in wrap(d, txt, fnt, W - 280):
        d.text((150, y), line, fill=INK, font=fnt); y += 60
    d.text((110, 660), "1.  What text structure is this?", fill=INK, font=font(SANS_BOLD, 36))
    d.text((110, 720), "2.  What can you infer about how science changes?", fill=INK, font=font(SANS_BOLD, 36))
    d.text((110, 820), "Pause.  Two answers.  Then press play.", fill=MUTED, font=font(SANS, 32))
    img.save(f"{OUT}/11_pause2.png", optimize=True)
    img.save(f"{OUT}/12_pause2_silence.png", optimize=True)

# 13_strategy — three-pass method
def s_13_strategy():
    img, d = base()
    d.text((110, 90), "Three-pass method.", fill=MAROON, font=font(SERIF_BOLD, 80))
    d.text((110, 220), "Before you read in detail, ask:", fill=MUTED, font=font(SANS, 38))
    items = [
        ("1.", "What is this about?",       "skim for topic + structure"),
        ("2.", "What is the writer claiming?", "main idea"),
        ("3.", "What's the evidence?",        "supporting details"),
    ]
    y = 360
    for n, q, label in items:
        d.text((140, y), n, fill=GOLD, font=font(SERIF_BOLD, 64))
        d.text((250, y+5), q, fill=INK, font=font(SERIF_BOLD, 50))
        d.text((250, y+80), f"→ {label}", fill=MUTED, font=font(SANS, 32))
        y += 160
    d.text((110, 880), "After that, slow down and read for inference.",
           fill=GOLD, font=font(SANS_BOLD, 36))
    img.save(f"{OUT}/13_strategy.png", optimize=True)

# 14_recap
def s_14_recap():
    img, d = base()
    d.text((110, 90), "Recap.", fill=MAROON, font=font(SERIF_BOLD, 80))
    items = [
        "Main idea — the writer's one-sentence claim.",
        "Supporting details — evidence that backs the claim.",
        "Inference — logical guess + text evidence (not feelings).",
        "Text structure — chronological, cause/effect, compare, problem/solution, description.",
    ]
    y = 230
    for t in items:
        d.text((140, y), "·", fill=GOLD, font=font(SERIF_BOLD, 56))
        d.text((200, y+10), t, fill=INK, font=font(SANS, 34))
        y += 90
    d.rounded_rectangle([110, 660, W-110, 920], radius=20, outline=MAROON, width=5)
    d.text((150, 690), "Assignment", fill=MAROON, font=font(SERIF_BOLD, 48))
    d.text((150, 770), "Read 1 informational article + 1 short story on CommonLit.",
           fill=INK, font=font(SANS, 32))
    d.text((150, 820), "Apply all 4 tools to each.  Next: Module 2 — parts of speech.",
           fill=INK, font=font(SANS, 32))
    img.save(f"{OUT}/14_recap.png", optimize=True)

for fn in [s_01_title, s_02_hook, s_03_overview, s_04_main_idea, s_05_supporting_details,
           s_06_pause1, s_08_inference, s_09_inference_rule, s_10_text_structure,
           s_11_pause2, s_13_strategy, s_14_recap]:
    fn()
print("Slides built.")

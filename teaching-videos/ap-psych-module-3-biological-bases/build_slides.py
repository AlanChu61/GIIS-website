"""AP Psychology · Module 3 — Biological Bases of Behavior.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
14 slides. Heavy on slide_kit primitives; 4 customs:
  - 02_hook              : 2am scrolling — dopamine + caffeine + adenosine
  - 04_neuron            : labeled neuron diagram (dendrites → soma → axon → terminals)
  - 07_neurotransmitters : 6-NT effects table
  - 09_pause1_answer     : GABA = inhibitory answer reveal
  - 11_cortex            : 4-lobe brain diagram with color-coded regions
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED, RED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=3, output_dir="slides", logo_path=LOGO)


# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 3 — Biological Bases of Behavior",
           "~7 minutes  ·  Neurons, neurotransmitters, brains, hormones, genes")


# 02 — hook (2am scrolling — dopamine + blocked adenosine)
def hook(img, d):
    d.text((110, 70), "It's 2 a.m.  You're still scrolling.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "Why?  Because your brain is doing chemistry.",
           fill=MAROON_DARK, font=font("serif_ital", 44))

    # Phone-style card on left showing the late-night feed
    px, py, pw, ph = 160, 250, 660, 600
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=44,
                        outline=MAROON, width=8, fill=deck.card_bg)
    # Header strip with time
    d.rounded_rectangle([px + 24, py + 24, px + pw - 24, py + 90], radius=18,
                        fill=MAROON_DARK)
    d.text((px + 50, py + 40), "02:13",
           fill=deck.accent_light, font=font("sans_bold", 30))
    d.text((px + 240, py + 40), "you said midnight 😴",
           fill=deck.accent_light, font=font("sans", 26))

    # Three "post" lines (engagement bait)
    for i, (icon, lbl) in enumerate([
        ("👍",  "+1 like      → tiny hit"),
        ("🔔",  "notification → tiny hit"),
        ("😂",  "funny clip   → tiny hit"),
        ("❤",   "DM reply     → tiny hit"),
    ]):
        ly = py + 130 + i * 100
        d.rounded_rectangle([px + 30, ly, px + pw - 30, ly + 80], radius=16,
                            outline=deck.accent, width=3, fill=deck.bg)
        d.text((px + 50, ly + 24), icon, fill=INK, font=font("sans_bold", 36))
        d.text((px + 130, ly + 28), lbl, fill=INK, font=font("sans", 28))

    # Right side: the chemistry callouts
    cx = 920
    d.rounded_rectangle([cx, 270, W - 110, 470], radius=24,
                        outline=deck.accent, width=6, fill=deck.card_bg)
    d.text((cx + 30, 290), "DOPAMINE", fill=deck.accent,
           font=font("sans_bold", 44))
    d.text((cx + 30, 360), "every like = tiny dose.",
           fill=INK, font=font("sans", 32))
    d.text((cx + 30, 405), "your brain says \"do that again.\"",
           fill=INK, font=font("sans", 32))

    d.rounded_rectangle([cx, 510, W - 110, 720], radius=24,
                        outline=MAROON, width=6, fill=deck.card_bg)
    d.text((cx + 30, 530), "CAFFEINE  (4 p.m.)", fill=MAROON,
           font=font("sans_bold", 44))
    d.text((cx + 30, 600), "still blocking adenosine —",
           fill=INK, font=font("sans", 32))
    d.text((cx + 30, 645), "the molecule that makes",
           fill=INK, font=font("sans", 32))
    d.text((cx + 30, 685), "you feel sleepy.",
           fill=INK, font=font("sans", 32))

    centered(d, "You're not weak-willed.  You're a biological machine.",
             font("serif_bold", 38), 890, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "The neuron — the basic unit.",
    "How neurons talk + the 6 neurotransmitters AP wants.",
    "Brain regions — brainstem to cortex.",
    "Endocrine system + nature × nurture.",
], footnote="Heavy vocab today. No shortcut here. Memorize.")


# 04 — neuron anatomy (custom labeled diagram)
def neuron(img, d):
    d.text((110, 70), "The neuron.", fill=MAROON, font=font("serif_bold", 76))
    d.text((110, 168), "~86 billion of these in your skull. Same basic shape.",
           fill=MUTED, font=font("sans", 32))

    # Diagram coordinates
    # Soma (cell body) — circle on the left
    soma_cx, soma_cy = 480, 540
    soma_r = 110
    d.ellipse([soma_cx - soma_r, soma_cy - soma_r,
               soma_cx + soma_r, soma_cy + soma_r],
              outline=MAROON, width=6, fill=deck.accent_light)

    # Dendrites — branchy lines coming out of the left side of the soma
    branch_starts = [(soma_cx - 90, soma_cy - 60),
                     (soma_cx - 110, soma_cy),
                     (soma_cx - 90, soma_cy + 60)]
    for sx, sy in branch_starts:
        # Main branch
        ex, ey = sx - 180, sy + (sy - soma_cy) // 2
        d.line([sx, sy, ex, ey], fill=MAROON, width=6)
        # Sub-branches
        d.line([ex, ey, ex - 70, ey - 40], fill=MAROON, width=5)
        d.line([ex, ey, ex - 80, ey + 30], fill=MAROON, width=5)
        d.line([ex, ey, ex - 60, ey + 60], fill=MAROON, width=5)

    # Axon — long horizontal line going right
    axon_y = soma_cy
    axon_start = soma_cx + soma_r
    axon_end = 1480
    # Myelin sheath segments — thicker rounded segments along the axon
    seg_len = 130
    seg_gap = 35
    x = axon_start + 30
    while x + seg_len < axon_end - 50:
        d.rounded_rectangle([x, axon_y - 26, x + seg_len, axon_y + 26],
                            radius=16, fill=deck.accent, outline=MAROON_DARK, width=3)
        x += seg_len + seg_gap
    # Thin axon line underneath the gaps so it reads as a continuous cable
    d.line([axon_start, axon_y, axon_end, axon_y], fill=MAROON_DARK, width=4)

    # Terminal buttons — three little knobs at the right end
    for ty in [axon_y - 70, axon_y, axon_y + 70]:
        d.line([axon_end, axon_y, axon_end + 80, ty], fill=MAROON_DARK, width=4)
        d.ellipse([axon_end + 70, ty - 22, axon_end + 114, ty + 22],
                  fill=MAROON, outline=MAROON_DARK, width=3)

    # Labels with leader lines
    # Dendrites label
    d.text((110, 380), "DENDRITES", fill=deck.accent, font=font("sans_bold", 32))
    d.text((110, 420), "receive signals", fill=INK, font=font("sans", 26))

    # Soma label
    d.text((soma_cx - 60, 690), "SOMA", fill=deck.accent, font=font("sans_bold", 32))
    d.text((soma_cx - 100, 730), "cell body / HQ", fill=INK, font=font("sans", 26))

    # Axon label
    d.text((780, 410), "AXON", fill=deck.accent, font=font("sans_bold", 32))
    d.text((780, 450), "carries the signal away",
           fill=INK, font=font("sans", 26))

    # Myelin label
    d.text((780, 620), "MYELIN SHEATH", fill=deck.accent,
           font=font("sans_bold", 32))
    d.text((780, 660), "fatty insulation — speeds it up",
           fill=INK, font=font("sans", 26))

    # Terminal buttons label
    d.text((1430, 700), "TERMINAL", fill=deck.accent,
           font=font("sans_bold", 32))
    d.text((1430, 740), "BUTTONS", fill=deck.accent,
           font=font("sans_bold", 32))
    d.text((1430, 780), "pass signal on", fill=INK,
           font=font("sans", 26))

    # Bottom mnemonic banner
    d.rounded_rectangle([110, 880, W - 110, 980], radius=20,
                        fill=deck.accent_light, outline=MAROON, width=4)
    centered(d, "Dendrites in.   Soma processes.   Axon out.   Terminals deliver.",
             font("serif_bold", 36), 905, MAROON_DARK)
deck.custom("04_neuron", neuron)


# 05 — action potential (definition card)
deck.definition("05_action_potential",
                "Action potential  =  the all-or-nothing spike.",
                "Hit threshold → sodium rushes in → wave races down the axon → reset.",
                sub="Stronger stimulus doesn't make a bigger spike. It makes the neuron spike MORE OFTEN.")


# 06 — synapse (definition card)
deck.definition("06_synapse",
                "Synapse  =  the gap between neurons.",
                "Neurotransmitter floats across, binds to a receptor, then is recycled (reuptake).",
                sub="SSRIs block serotonin reuptake. That's why \"reuptake\" is on the AP exam.")


# 07 — neurotransmitter table (custom)
def neurotransmitters(img, d):
    d.text((110, 60), "The 6 neurotransmitters AP wants.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 142), "Memorize the name → effect → clinical link.",
           fill=MUTED, font=font("sans", 30))

    # Header row
    header_y = 210
    headers = [(140, "NEUROTRANSMITTER"), (640, "MAIN JOB"), (1280, "WHEN IT GOES WRONG")]
    d.rounded_rectangle([110, header_y, W - 110, header_y + 70], radius=14,
                        fill=MAROON)
    for x, h in headers:
        d.text((x, header_y + 18), h, fill=deck.accent_light,
               font=font("sans_bold", 28))

    # Rows
    rows = [
        ("DOPAMINE",       "reward · motivation · movement",
         "low → Parkinson's;  high → schizophrenia"),
        ("SEROTONIN",      "mood · sleep · appetite",
         "low → depression (SSRIs target this)"),
        ("GLUTAMATE",      "main EXCITATORY — \"GO\"",
         "too much → seizures"),
        ("GABA",           "main INHIBITORY — \"STOP\"",
         "low → anxiety (benzos boost it)"),
        ("ACETYLCHOLINE",  "memory · muscle movement",
         "loss → Alzheimer's"),
        ("ENDORPHINS",     "natural painkillers",
         "released by exercise · runner's high"),
    ]
    row_h = 105
    row_y = header_y + 80
    for i, (name, job, fail) in enumerate(rows):
        y = row_y + i * row_h
        # Alternate row backgrounds
        bg = deck.card_bg if i % 2 == 0 else deck.bg
        d.rounded_rectangle([110, y, W - 110, y + row_h - 8], radius=12,
                            fill=bg, outline=deck.accent, width=2)
        d.text((140, y + 28), name, fill=deck.accent,
               font=font("sans_bold", 32))
        d.text((640, y + 32), job, fill=INK, font=font("sans", 28))
        d.text((1280, y + 32), fail, fill=MAROON_DARK,
               font=font("serif_ital", 26))

    # Bottom mnemonic
    d.rounded_rectangle([110, 920, W - 110, 1010], radius=18,
                        fill=deck.accent_light, outline=MAROON, width=3)
    centered(d, "GLUTAMATE = gas.   GABA = brake.   The pair you cannot forget.",
             font("serif_bold", 32), 945, MAROON_DARK)
deck.custom("07_neurotransmitters", neurotransmitters)


# 08 — pause + try
deck.pause("08_pause1", "PAUSE  &  TRY",
           "A new med makes people calmer and less anxious by boosting one specific neurotransmitter.",
           "Which one?  Excitatory or inhibitory?",
           hint="Pause. Decide. Press play.")


# 09 — pause answer (custom)
def pause_answer(img, d):
    d.text((110, 70), "Answer:  GABA, inhibitory.",
           fill=MAROON, font=font("serif_bold", 76))

    # Three answer chips
    chips = [
        ("WHICH",  "GABA  (gamma-aminobutyric acid)"),
        ("TYPE",   "INHIBITORY  —  it calms neurons down"),
        ("WHY",    "benzodiazepines treat anxiety by boosting GABA"),
    ]
    for i, (label, body) in enumerate(chips):
        y = 230 + i * 140
        d.rounded_rectangle([110, y, W - 110, y + 110], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((150, y + 28), label, fill=deck.accent,
               font=font("sans_bold", 40))
        d.text((430, y + 32), body, fill=INK, font=font("sans", 34))

    # Footer — gas + brake mnemonic
    d.rounded_rectangle([110, 720, W - 110, 940], radius=24,
                        fill=deck.accent_light, outline=MAROON, width=5)
    centered(d, "GLUTAMATE = gas.    GABA = brake.",
             font("serif_bold", 56), 750, MAROON_DARK)
    centered(d, "Serotonin was a fair guess — but \"calmer\" + \"inhibitory\" points at GABA.",
             font("sans", 32), 850, MAROON_DARK)
    centered(d, "AP loves this pair. Memorize.",
             font("sans_bold", 34), 895, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)


# 10 — brain regions: hindbrain / midbrain / forebrain (compare)
deck.compare("10_brain_regions", "Brain divisions:  oldest → newest.",
    {"label": "HINDBRAIN  (survival)",
     "color": MAROON,
     "lines": [
         "MEDULLA — heartbeat,",
         "PONS — sleep, coord,",
         "CEREBELLUM — balance,",
         "fine motor skills.",
         "Without this you die.",
     ],
     "footnote": "Sits on top of the spinal cord."},
    {"label": "FOREBRAIN  (the human stuff)",
     "color": deck.accent,
     "lines": [
         "THALAMUS — sensory relay,",
         "HYPOTHALAMUS — homeostasis,",
         "HIPPOCAMPUS — memory,",
         "AMYGDALA — fear, emotion.",
         "Last 4  =  LIMBIC SYSTEM.",
     ],
     "footnote": "Midbrain (in between): arousal + reflex."})


# 11 — cerebral cortex 4 lobes (custom diagram)
def cortex(img, d):
    d.text((110, 60), "The cerebral cortex — four lobes.",
           fill=MAROON, font=font("serif_bold", 60))
    d.text((110, 142), "AP will give you a damage scenario. You name the lobe.",
           fill=MUTED, font=font("sans", 30))

    # Brain silhouette — pulled up so legend at the bottom has clean space
    cx, cy = 960, 480

    frontal_color = (118, 92, 168)   # lavender accent
    parietal_color = (160, 130, 200)
    temporal_color = (200, 100, 130) # warm contrast
    occipital_color = (90, 130, 180) # cool

    # Frontal lobe (front/left)
    d.ellipse([cx - 460, cy - 240, cx - 80, cy + 100],
              fill=frontal_color, outline=MAROON_DARK, width=4)
    # Parietal lobe (top)
    d.ellipse([cx - 200, cy - 290, cx + 220, cy + 30],
              fill=parietal_color, outline=MAROON_DARK, width=4)
    # Temporal lobe (bottom)
    d.ellipse([cx - 320, cy + 20, cx + 80, cy + 240],
              fill=temporal_color, outline=MAROON_DARK, width=4)
    # Occipital lobe (back/right)
    d.ellipse([cx + 100, cy - 180, cx + 460, cy + 180],
              fill=occipital_color, outline=MAROON_DARK, width=4)

    # Cerebellum (small bump under occipital — tucked further right)
    d.ellipse([cx + 320, cy + 140, cx + 500, cy + 260],
              fill=deck.accent_light, outline=MAROON_DARK, width=3)
    d.text((cx + 340, cy + 185), "cerebellum",
           fill=MAROON_DARK, font=font("sans", 22))

    # Brainstem stub (centered below)
    d.rounded_rectangle([cx + 80, cy + 220, cx + 260, cy + 320], radius=14,
                        fill=deck.accent_light, outline=MAROON_DARK, width=3)
    d.text((cx + 100, cy + 252), "brainstem",
           fill=MAROON_DARK, font=font("sans", 22))

    # Lobe labels INSIDE colored regions
    d.text((cx - 380, cy - 80), "FRONTAL", fill=(255, 255, 255),
           font=font("sans_bold", 30))
    d.text((cx - 80, cy - 160), "PARIETAL", fill=(255, 255, 255),
           font=font("sans_bold", 30))
    d.text((cx - 230, cy + 100), "TEMPORAL", fill=(255, 255, 255),
           font=font("sans_bold", 30))
    d.text((cx + 200, cy - 30), "OCCIPITAL", fill=(255, 255, 255),
           font=font("sans_bold", 30))

    # Legend strip at the bottom — short labels so nothing clips
    items = [
        ("FRONTAL",   "plan · Broca's (speech)",        frontal_color),
        ("PARIETAL",  "touch · body position",          parietal_color),
        ("TEMPORAL",  "hearing · Wernicke's",           temporal_color),
        ("OCCIPITAL", "vision",                         occipital_color),
    ]
    legend_top = 880
    legend_bottom = 1000
    box_w = (W - 220) // 4
    for i, (name, job, col) in enumerate(items):
        x = 110 + i * box_w
        d.rounded_rectangle([x + 10, legend_top, x + box_w - 10, legend_bottom],
                            radius=14, fill=col, outline=MAROON_DARK, width=3)
        d.text((x + 30, legend_top + 12), name, fill=(255, 255, 255),
               font=font("sans_bold", 28))
        d.text((x + 30, legend_top + 60), job, fill=(255, 255, 255),
               font=font("sans", 22))
deck.custom("11_cortex", cortex)


# 12 — endocrine + nature×nurture (recap-style)
deck.recap("12_endocrine_genes", "Endocrine + nature × nurture.", [
    "Endocrine system = glands releasing hormones into blood. Slower than neurons, longer-lasting.",
    "PITUITARY = master gland (under hypothalamus). Tells the others what to do.",
    "ADRENAL glands → adrenaline → fight-or-flight. (That pre-presentation jolt.)",
    "THYROID → metabolism.",
    "Twin studies: identical twins share 100% DNA; fraternal share 50%. Higher similarity = genes matter.",
    "Heritability ≠ destiny. Nature loads the gun. Nurture pulls the trigger.",
])


# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Neuron parts: dendrites · soma · axon · myelin · terminals.",
    "Action potential = all-or-nothing. Strength = FREQUENCY.",
    "Synapse: neurotransmitter crosses, binds, then reuptake.",
    "Big 6: dopamine · serotonin · glutamate · GABA · ACh · endorphins.",
    "Hindbrain = survival. Limbic = emotion. Cortex = 4 lobes.",
    "Endocrine: pituitary master · adrenal fight-or-flight · thyroid.",
])


# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",        "(done!)"),
    ("1.", "Read Myers Module 3",      "Brain & neural communication — read it twice"),
    ("2.", "AP Classroom · 15 MCQ",    "Neuron parts, neurotransmitters, brain regions"),
    ("3.", "Assignment in dashboard",  "Match 10 brain-damage scenarios to the region"),
    ("4.", "Make a brain map",         "Draw + label every region. Advisor check-in if fuzzy."),
], next_text="Next up:  Module 4 — Sensation & Perception.")


print("AP Psych Module 3 slides built.")

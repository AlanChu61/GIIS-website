"""AP Psychology · Module 6 — Learning & Conditioning.

Lavender theme (auto-resolved by slide_kit from "AP Psychology" prefix).
Heavy on slide_kit primitives + a handful of custom diagrams that earn their
keep: classical conditioning chain, operant 2x2, reinforcement schedules
quadrant, Bobo doll observational learning, Garcia/instinctive drift.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "lesson-video"))

from slide_kit import (
    Deck, font, centered, wrap, W, H,
    INK, MAROON, MAROON_DARK, MUTED,
)

LOGO = "../../src/img/logo_nobg.png"
deck = Deck(course="AP Psychology", module_num=6, output_dir="slides", logo_path=LOGO)


# 01 — title
deck.title("01_title", "AP Psychology",
           "Module 6 — Learning & Conditioning",
           "~7 minutes  ·  Pavlov · Skinner · Bandura  ·  the AP trap")


# 02 — hook (phone buzz → reach for it)
def hook(img, d):
    d.text((110, 80), "Your phone buzzes.", fill=MAROON, font=font("serif_bold", 84))
    d.text((110, 178), "Your hand moves before you read the screen.",
           fill=MAROON_DARK, font=font("serif", 44))

    # Phone illustration (center-left)
    px, py = 470, 540
    d.rounded_rectangle([px-90, py-180, px+90, py+180], radius=24,
                        outline=MAROON, width=8, fill=deck.card_bg)
    d.rounded_rectangle([px-72, py-150, px+72, py+130], radius=12,
                        outline=MUTED, width=3, fill=(245, 240, 250))
    # Notification bar with vibrate squiggles
    d.rounded_rectangle([px-66, py-130, px+66, py-60], radius=8,
                        fill=deck.accent_light)
    d.text((px-50, py-118), "DISCORD", fill=MAROON_DARK, font=font("sans_bold", 22))
    d.text((px-50, py-92), "new ping", fill=INK, font=font("sans", 20))
    # vibrate squiggles
    for i, dy in enumerate([-220, -200]):
        d.arc([px-150-i*20, py+dy, px-90-i*20, py+dy+40], 90, 270,
              fill=deck.accent, width=4)
        d.arc([px+90+i*20, py+dy, px+150+i*20, py+dy+40], 270, 90,
              fill=deck.accent, width=4)

    # Arrow → trained response
    d.line([px+170, py, 1100, py], fill=MAROON, width=8)
    d.polygon([(1100, py-20), (1140, py), (1100, py+20)], fill=MAROON)
    d.text((600, py-50), "trained response", fill=deck.accent,
           font=font("sans_bold", 28))

    # Right card: "you reach for it"
    rx = 1180
    d.rounded_rectangle([rx, py-160, rx+560, py+160], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((rx+30, py-130), "YOU CHECK", fill=deck.accent,
           font=font("sans_bold", 40))
    d.text((rx+30, py-70), "before you decide to.", fill=INK,
           font=font("sans", 32))
    d.text((rx+30, py-10), "buzz  →  little reward", fill=MUTED,
           font=font("sans", 28))
    d.text((rx+30, py+30), "buzz  →  little reward", fill=MUTED,
           font=font("sans", 28))
    d.text((rx+30, py+70), "buzz  →  little reward", fill=MUTED,
           font=font("sans", 28))
    d.text((rx+30, py+110), "→ you're conditioned.", fill=MAROON,
           font=font("sans_bold", 30))

    centered(d, "Same machinery as a slot machine.   Same machinery Pavlov used in 1897.",
             font("serif_bold", 34), 870, MAROON_DARK)
deck.custom("02_hook", hook)


# 03 — overview
deck.overview("03_overview", "Game plan.", [
    "Three paradigms — classical, operant, observational.",
    "The AP trap — negative reinforcement is NOT punishment.",
    "Reinforcement schedules — why some habits are unbreakable.",
], footnote="By end: identify reinforcement vs punishment from any real-life scenario.")


# 04 — classical conditioning chain (custom diagram)
def classical(img, d):
    d.text((110, 70), "Classical conditioning  ·  Pavlov",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "A neutral stimulus becomes a trigger by pairing.",
           fill=MUTED, font=font("sans", 32))

    # Four-step chain. Each row: label, stimulus, arrow, response.
    rows = [
        ("BEFORE",  "FOOD  (UCS)",       "→",  "drool  (UCR)",       "built-in. unlearned."),
        ("BEFORE",  "BELL  (Neutral)",   "→",  "no response",         "bell means nothing yet."),
        ("PAIRING", "BELL  +  FOOD",     "→",  "drool  (UCR)",        "ring, then feed.  repeat."),
        ("AFTER",   "BELL  (CS)",        "→",  "drool  (CR)",         "the bell alone now triggers it."),
    ]
    y0 = 240
    rh = 150
    for i, (phase, stim, arrow, resp, note) in enumerate(rows):
        y = y0 + i * (rh + 20)
        # Phase tag
        d.rounded_rectangle([110, y, 280, y + rh], radius=14,
                            fill=deck.accent if i == 3 else MAROON_DARK)
        centered_x = 195
        ph_font = font("sans_bold", 28)
        tw = d.textlength(phase, font=ph_font)
        d.text((centered_x - tw/2, y + rh/2 - 16), phase,
               fill=(255, 255, 255), font=ph_font)

        # Main row card
        d.rounded_rectangle([300, y, W - 110, y + rh], radius=16,
                            outline=deck.accent if i == 3 else MAROON,
                            width=4 if i == 3 else 3,
                            fill=deck.card_bg)
        # Stimulus
        d.text((330, y + 24), stim, fill=INK, font=font("sans_bold", 36))
        # Arrow
        d.text((850, y + 24), arrow, fill=deck.accent,
               font=font("serif_bold", 56))
        # Response
        resp_color = MAROON if i == 3 else INK
        d.text((950, y + 24), resp, fill=resp_color,
               font=font("sans_bold", 36))
        # Note
        d.text((330, y + 90), note, fill=MUTED, font=font("sans", 26))
deck.custom("04_classical", classical)


# 05 — classical terms (recap-style list)
deck.recap("05_classical_terms", "Five terms AP loves.", [
    "Acquisition — the link is being learned (bell + food, repeated).",
    "Extinction — bell with no food, over and over → drooling fades.",
    "Spontaneous recovery — wait a day, ring again → drool partially returns.",
    "Generalization — dog drools to a buzzer, a chime, anything bell-like.",
    "Discrimination — dog learns to drool only to THAT bell, not others.",
])


# 06 — operant conditioning (Skinner + shaping)
def operant_intro(img, d):
    d.text((110, 70), "Operant conditioning  ·  Skinner",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "Behavior is shaped by what happens AFTER it.",
           fill=MUTED, font=font("sans", 32))

    # Left: Skinner box illustration
    bx, by, bw, bh = 130, 260, 760, 600
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((bx + 30, by + 20), "SKINNER BOX", fill=deck.accent,
           font=font("sans_bold", 36))

    # Lever
    d.line([bx + 90, by + 380, bx + 240, by + 330], fill=INK, width=10)
    d.rectangle([bx + 230, by + 325, bx + 270, by + 345], fill=INK)
    d.text((bx + 80, by + 410), "lever", fill=MUTED, font=font("sans", 26))

    # Rat (stylized)
    rx, ry = bx + 380, by + 350
    d.ellipse([rx, ry, rx + 140, ry + 90], fill=MAROON_DARK)  # body
    d.ellipse([rx + 110, ry - 10, rx + 180, ry + 50], fill=MAROON_DARK)  # head
    d.ellipse([rx + 155, ry + 5, rx + 170, ry + 20], fill=(255, 255, 255))  # eye
    d.line([rx, ry + 70, rx - 60, ry + 90], fill=MAROON_DARK, width=6)  # tail

    # Food chute
    d.rectangle([bx + 600, by + 60, bx + 700, by + 200], outline=INK, width=4)
    d.text((bx + 590, by + 220), "food drops", fill=MUTED, font=font("sans", 24))
    d.ellipse([bx + 625, by + 160, bx + 655, by + 190], fill=deck.accent)
    d.ellipse([bx + 640, by + 170, bx + 670, by + 200], fill=deck.accent)

    # Caption (two lines to fit inside the box)
    d.text((bx + 30, by + bh - 90),
           "Press lever  →  food drops.",
           fill=INK, font=font("sans_bold", 28))
    d.text((bx + 30, by + bh - 50),
           "→ rat presses the lever MORE.",
           fill=MAROON, font=font("sans_bold", 28))

    # Right column: shaping
    sx, sy = 940, 260
    d.rounded_rectangle([sx, sy, W - 110, sy + 600], radius=16,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((sx + 30, sy + 20), "SHAPING", fill=deck.accent,
           font=font("sans_bold", 40))
    d.text((sx + 30, sy + 80), "by successive approximations",
           fill=MUTED, font=font("sans_italic" if False else "sans", 28))

    steps = [
        "1.  Reward turning toward the lever.",
        "2.  Then reward stepping toward it.",
        "3.  Then reward touching it.",
        "4.  Then reward pressing it.",
        "5.  Now you have a lever-pressing rat.",
    ]
    for i, s in enumerate(steps):
        d.text((sx + 30, sy + 150 + i * 70), s, fill=INK, font=font("sans", 30))

    d.text((sx + 30, sy + 540), "Every animal trainer on Earth uses this.",
           fill=deck.accent, font=font("sans_bold", 26))
deck.custom("06_operant", operant_intro)


# 07 — operant 2x2 matrix (THE big slide)
def operant_2x2(img, d):
    d.text((110, 50), "The operant 2 × 2.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 130), "Positive = ADD.   Negative = REMOVE.   "
                       "Reinforce = behavior UP.   Punish = behavior DOWN.",
           fill=MUTED, font=font("sans", 26))

    # Grid layout — pulled right so left row-headers fit
    cell_w, cell_h = 750, 310
    gx, gy = 240, 245   # top-left of grid
    gap = 16

    # Column headers
    d.text((gx + cell_w / 2 - 110, gy - 60), "REINFORCE  (↑)",
           fill=deck.accent, font=font("sans_bold", 36))
    d.text((gx + cell_w + gap + cell_w / 2 - 100, gy - 60), "PUNISH  (↓)",
           fill=MAROON, font=font("sans_bold", 36))

    # Row headers — narrower and inside left margin
    rh_x = 70
    d.text((rh_x, gy + cell_h / 2 - 36), "ADD",
           fill=INK, font=font("sans_bold", 38))
    d.text((rh_x + 30, gy + cell_h / 2 + 14), "(+)",
           fill=INK, font=font("sans_bold", 32))
    d.text((rh_x - 20, gy + cell_h + gap + cell_h / 2 - 36), "REMOVE",
           fill=INK, font=font("sans_bold", 34))
    d.text((rh_x + 30, gy + cell_h + gap + cell_h / 2 + 14), "(−)",
           fill=INK, font=font("sans_bold", 32))

    cells = [
        # (col, row, title, sign, examples)
        (0, 0, "POSITIVE REINFORCEMENT", "Behavior goes UP",
         ["Add a gold star → study more.",
          "Add a treat → dog sits more.",
          "Add Insta likes → post more."]),
        (1, 0, "POSITIVE PUNISHMENT", "Behavior goes DOWN",
         ["Add a parking ticket → park better.",
          "Add a scolding → swear less.",
          "Add a hangover → drink less (maybe)."]),
        (0, 1, "NEGATIVE REINFORCEMENT", "Behavior goes UP",
         ["REMOVE seatbelt beep → buckle faster.",
          "REMOVE headache (aspirin) → take aspirin.",
          "REMOVE nagging (clean room) → clean more."]),
        (1, 1, "NEGATIVE PUNISHMENT", "Behavior goes DOWN",
         ["REMOVE phone → break curfew less.",
          "REMOVE allowance → talk back less.",
          "REMOVE screen time → fight less."]),
    ]

    for col, row, title, sign, lines in cells:
        x = gx + col * (cell_w + gap)
        y = gy + row * (cell_h + gap)
        is_reinforce = (col == 0)
        is_negative_reinforce = (col == 0 and row == 1)
        # Highlight the trap quadrant
        outline = deck.accent if is_reinforce else MAROON
        width = 8 if is_negative_reinforce else 4
        fill = deck.accent_light if is_negative_reinforce else deck.card_bg
        d.rounded_rectangle([x, y, x + cell_w, y + cell_h],
                            radius=18, outline=outline, width=width, fill=fill)
        d.text((x + 24, y + 18), title,
               fill=outline, font=font("sans_bold", 30))
        d.text((x + 24, y + 60), sign, fill=MUTED, font=font("sans", 24))
        for i, ln in enumerate(lines):
            d.text((x + 24, y + 110 + i * 60), ln, fill=INK, font=font("sans", 26))

    # Footer warning — single tight line
    warn_y = gy + 2 * cell_h + 2 * gap + 14
    d.text((110, warn_y),
           "★  THE TRAP →  Negative reinforcement is NOT punishment — it makes behavior INCREASE.",
           fill=MAROON_DARK, font=font("sans_bold", 26))
deck.custom("07_2x2", operant_2x2)


# 08 — pause + try
deck.pause("08_pause1", "PAUSE  &  TRY",
           "Your seatbelt beeps when you sit down without it. As soon as you buckle, the beep stops. Next time you sit down, you buckle FASTER.",
           "Reinforcement or punishment?  Positive or negative?",
           hint="Pause. Decide. Press play.")


# 09 — pause answer (custom — the AP trap fully explained)
def pause_answer(img, d):
    d.text((110, 70), "The answer:  NEGATIVE  REINFORCEMENT.",
           fill=MAROON, font=font("serif_bold", 60))

    # Step 1
    d.rounded_rectangle([110, 200, W - 110, 380], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((140, 220), "Step 1 — did the behavior go UP or DOWN?",
           fill=deck.accent, font=font("sans_bold", 32))
    d.text((140, 270), "You buckle FASTER.  Behavior went UP.",
           fill=INK, font=font("sans", 32))
    d.text((140, 320), "→  REINFORCEMENT.  (Punishment makes behavior go DOWN.)",
           fill=MAROON, font=font("sans_bold", 30))

    # Step 2
    d.rounded_rectangle([110, 410, W - 110, 590], radius=20,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((140, 430), "Step 2 — was something ADDED or REMOVED?",
           fill=deck.accent, font=font("sans_bold", 32))
    d.text((140, 480), "The annoying beep was REMOVED when you buckled.",
           fill=INK, font=font("sans", 32))
    d.text((140, 530), "→  NEGATIVE.  (Negative means remove. Not 'bad.')",
           fill=MAROON, font=font("sans_bold", 30))

    # Final box
    d.rounded_rectangle([110, 620, W - 110, 880], radius=24,
                        fill=deck.accent_light, outline=MAROON_DARK, width=6)
    centered(d, "NEGATIVE  REINFORCEMENT", font("serif_bold", 64), 650, MAROON_DARK)
    centered(d, "REMOVE the aversive  →  behavior INCREASES.",
             font("sans_bold", 38), 740, MAROON_DARK)
    centered(d, "Aspirin removes headache → you take aspirin more.  Same logic.",
             font("sans", 32), 800, MAROON_DARK)
deck.custom("09_pause1_answer", pause_answer)


# 10 — reinforcement schedules (FR / VR / FI / VI quadrants)
def schedules(img, d):
    d.text((110, 50), "Reinforcement schedules.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 130), "How OFTEN you reward changes how STUBBORN the behavior gets.",
           fill=MUTED, font=font("sans", 28))

    # Column headers — RATIO vs INTERVAL
    cell_w, cell_h = 750, 310
    gx, gy = 240, 245
    gap = 16

    d.text((gx + cell_w / 2 - 60, gy - 70), "RATIO",
           fill=deck.accent, font=font("sans_bold", 36))
    d.text((gx + cell_w / 2 - 130, gy - 32), "(per # of responses)",
           fill=MUTED, font=font("sans", 24))
    d.text((gx + cell_w + gap + cell_w / 2 - 90, gy - 70), "INTERVAL",
           fill=deck.accent, font=font("sans_bold", 36))
    d.text((gx + cell_w + gap + cell_w / 2 - 130, gy - 32), "(per amount of time)",
           fill=MUTED, font=font("sans", 24))

    rh_x = 60
    d.text((rh_x + 30, gy + cell_h / 2 - 18), "FIXED",
           fill=INK, font=font("sans_bold", 32))
    d.text((rh_x, gy + cell_h + gap + cell_h / 2 - 18), "VARIABLE",
           fill=INK, font=font("sans_bold", 32))

    cells = [
        (0, 0, "FIXED RATIO  (FR)",
         "reward every Nth response",
         ["Pieceworker paid per",
          "10 shirts sewn.",
          "→ high steady output."],
         False),
        (1, 0, "FIXED INTERVAL  (FI)",
         "reward after a set time",
         ["Paycheck every 2 weeks.",
          "→ work spikes near payday,",
          "   slows after."],
         False),
        (0, 1, "VARIABLE RATIO  (VR)",
         "reward after unpredictable # of responses",
         ["Slot machines.  Lottery.",
          "Instagram likes.",
          "→ MOST addictive.  ★"],
         True),
        (1, 1, "VARIABLE INTERVAL  (VI)",
         "reward after unpredictable time",
         ["Checking email for a reply.",
          "Pop quizzes.",
          "→ slow, steady checking."],
         False),
    ]

    for col, row, title, subtitle, lines, highlight in cells:
        x = gx + col * (cell_w + gap)
        y = gy + row * (cell_h + gap)
        outline = MAROON_DARK if highlight else deck.accent
        width_ = 8 if highlight else 4
        fill = deck.accent_light if highlight else deck.card_bg
        d.rounded_rectangle([x, y, x + cell_w, y + cell_h],
                            radius=18, outline=outline, width=width_, fill=fill)
        d.text((x + 24, y + 18), title,
               fill=outline, font=font("sans_bold", 32))
        d.text((x + 24, y + 64), subtitle, fill=MUTED, font=font("sans", 24))
        for i, ln in enumerate(lines):
            d.text((x + 24, y + 120 + i * 56), ln, fill=INK, font=font("sans", 28))

    warn_y = gy + 2 * cell_h + 2 * gap + 14
    d.text((110, warn_y),
           "★  Variable RATIO = most resistant to extinction. Slot machines, social media, your phone.",
           fill=MAROON_DARK, font=font("sans_bold", 26))
deck.custom("10_schedules", schedules)


# 11 — observational learning (Bobo doll + mirror neurons)
def observational(img, d):
    d.text((110, 70), "Observational learning  ·  Bandura",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "You don't have to do it.  You can learn just by watching.",
           fill=MUTED, font=font("sans", 32))

    # Left: Bobo doll experiment
    lx, ly = 130, 260
    lw, lh = 850, 600
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=16,
                        outline=MAROON, width=5, fill=deck.card_bg)
    d.text((lx + 24, ly + 20), "BOBO DOLL  ·  1961",
           fill=deck.accent, font=font("sans_bold", 36))

    # Adult figure (left) hits Bobo (right). Compact stick figure.
    ax, ay = lx + 90, ly + 380
    d.ellipse([ax, ay, ax + 70, ay + 70], fill=MAROON_DARK)  # adult head
    d.line([ax + 35, ay + 70, ax + 35, ay + 200], fill=MAROON_DARK, width=10)  # body
    d.line([ax + 35, ay + 110, ax + 180, ay + 100], fill=MAROON_DARK, width=10)  # arm hitting →
    d.line([ax + 35, ay + 200, ax, ay + 280], fill=MAROON_DARK, width=10)  # leg
    d.line([ax + 35, ay + 200, ax + 70, ay + 280], fill=MAROON_DARK, width=10)  # leg
    d.text((ax - 10, ay + 290), "adult", fill=MUTED, font=font("sans", 24))

    # Action lines — POW (placed in the gap between adult and Bobo)
    d.text((lx + 290, ly + 360), "POW!", fill=MAROON,
           font=font("serif_bold", 56))

    # Bobo (clown doll) — shifted further right and shrunk so the body doesn't
    # cover the POW or the adult's arm
    bx_, by_ = lx + 470, ly + 380
    d.ellipse([bx_, by_, bx_ + 90, by_ + 90], fill=deck.accent_light,
              outline=MAROON, width=4)  # head
    d.ellipse([bx_ + 22, by_ + 28, bx_ + 36, by_ + 42], fill=INK)
    d.ellipse([bx_ + 54, by_ + 28, bx_ + 68, by_ + 42], fill=INK)
    d.ellipse([bx_ + 36, by_ + 58, bx_ + 54, by_ + 72], fill=MAROON)  # nose
    d.polygon([(bx_, by_ + 90), (bx_ + 90, by_ + 90),
               (bx_ + 120, by_ + 240), (bx_ - 30, by_ + 240)],
              fill=deck.accent, outline=MAROON_DARK, width=4)
    d.text((bx_ + 10, by_ + 250), "Bobo", fill=MUTED, font=font("sans", 24))

    # Bottom: arrow → child copies
    d.line([lx + 60, ly + lh - 110, lx + lw - 60, ly + lh - 110],
           fill=deck.accent, width=6)
    d.polygon([(lx + lw - 60, ly + lh - 130), (lx + lw - 30, ly + lh - 110),
               (lx + lw - 60, ly + lh - 90)], fill=deck.accent)
    d.text((lx + 60, ly + lh - 80),
           "Kids who watched → ATTACKED.   Others played calmly.",
           fill=INK, font=font("sans_bold", 26))

    # Right: mirror neurons + modeling
    rx, ry = 1010, 260
    rw, rh = W - 110 - rx, 600
    d.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=16,
                        outline=deck.accent, width=5, fill=deck.card_bg)
    d.text((rx + 24, ry + 20), "MODELING", fill=deck.accent,
           font=font("sans_bold", 40))
    d.text((rx + 24, ry + 78), "copying behavior you observed",
           fill=MUTED, font=font("sans", 28))

    examples = [
        "Kids talk like their parents.",
        "Athletes copy their coaches.",
        "You catch your friend's catchphrases.",
    ]
    for i, ex in enumerate(examples):
        d.text((rx + 24, ry + 150 + i * 50), "·  " + ex,
               fill=INK, font=font("sans", 28))

    # Mirror neurons strip
    d.rounded_rectangle([rx + 20, ry + 360, rx + rw - 20, ry + 560],
                        radius=14, fill=deck.accent_light)
    d.text((rx + 40, ry + 380), "MIRROR NEURONS",
           fill=MAROON_DARK, font=font("sans_bold", 32))
    body = wrap(d, "Neurons that fire BOTH when you do an action AND when you watch someone else do it.",
                font("sans", 26), rw - 60)
    for i, ln in enumerate(body):
        d.text((rx + 40, ry + 430 + i * 36), ln,
               fill=MAROON_DARK, font=font("sans", 26))
deck.custom("11_observational", observational)


# 12 — biological constraints (Garcia + instinctive drift)
def biology(img, d):
    d.text((110, 70), "Biology constrains learning.",
           fill=MAROON, font=font("serif_bold", 64))
    d.text((110, 158), "Not all associations are equally easy. The blank slate is wrong.",
           fill=MUTED, font=font("sans", 32))

    # Two cards
    for i, (title, lead, lines, footer) in enumerate([
        ("GARCIA EFFECT  ·  taste aversion",
         "ONE trial.  Lifelong avoidance.",
         ["Eat a weird food.",
          "Get sick hours later.",
          "→ avoid that food for years.",
          "",
          "Brain easily links taste → nausea.",
          "Will NOT easily link light → nausea.",
          "Survival logic is baked in."],
         "Pavlov's bell needed dozens of trials. Garcia needed ONE."),
        ("INSTINCTIVE DRIFT",
         "Trained behaviors revert to instinct.",
         ["Pig is trained to drop coins",
          "in a piggy bank for food.",
          "",
          "Eventually, the pig starts",
          "rooting around with the coins",
          "like food on the ground.",
          "Instinct wins."],
         "Some links are easy. Some are nearly impossible. Biology decides."),
    ]):
        x = 110 + i * 870
        d.rounded_rectangle([x, 240, x + 800, 940], radius=20,
                            outline=deck.accent, width=5, fill=deck.card_bg)
        d.text((x + 30, 270), title, fill=deck.accent,
               font=font("sans_bold", 36))
        d.text((x + 30, 330), lead, fill=MAROON_DARK,
               font=font("sans_bold", 30))
        for j, ln in enumerate(lines):
            d.text((x + 30, 390 + j * 50), ln, fill=INK, font=font("sans", 28))
        d.text((x + 30, 880), footer, fill=MUTED,
               font=font("sans", 24))
deck.custom("12_biology", biology)


# 13 — recap
deck.recap("13_recap", "Recap.", [
    "Classical (Pavlov): a neutral stimulus becomes a conditioned trigger.",
    "Operant (Skinner): consequences shape behavior.",
    "Positive = ADD.  Negative = REMOVE.  NOT good vs bad.",
    "Negative reinforcement is NOT punishment — it makes behavior GO UP.",
    "Variable Ratio = the most addictive schedule (slot machines, your phone).",
    "Observational (Bandura): we learn by watching. Bobo + mirror neurons.",
])


# 14 — path
deck.path("14_path", [
    ("✓",  "Watch this lesson",         "(done!)"),
    ("1.", "Read Myers Module 6",       "Especially the operant 2×2 + schedules"),
    ("2.", "AP Classroom · 15 MCQ",     "Identify reinforcement vs punishment from scenarios"),
    ("3.", "Assignment in dashboard",    "Label 10 scenarios — pos/neg, reinforce/punish"),
    ("4.", "Advisor check-in",           "Negative reinforcement trips up everyone"),
], next_text="Next up:  Module 7 — Memory.  Why you remember a 3rd-grade song lyric "
              "but forget what you ate yesterday.")


print("AP Psych Module 6 slides built.")

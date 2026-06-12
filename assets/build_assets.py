"""
Build synthetic demo assets for the Journal App public showcase.
Outputs:
  screenshots/01-capture-demo.png
  screenshots/02-idea-demo.png
  screenshots/03-history-demo.png
  diagrams/context-diagram.png
  diagrams/data-flow.png
  diagrams/privacy-boundary.png

All content is synthetic. No real journal text, names, or private data.
Run from the assets/ directory or adjust BASE_DIR below.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

# ── paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
SCREENSHOTS = BASE_DIR / "screenshots"
DIAGRAMS = BASE_DIR / "diagrams"

# ── palette (mobile-app dark-ish neutral) ────────────────────────────────────
BG       = (18, 18, 22)       # page background
SURFACE  = (28, 28, 34)       # card / input surface
SURFACE2 = (38, 38, 46)       # elevated card
BORDER   = (60, 60, 72)       # subtle border
ACCENT   = (99, 179, 237)     # blue accent
ACCENT2  = (154, 117, 236)    # purple accent (idea mode)
SUCCESS  = (72, 199, 142)     # green
TEXT1    = (240, 240, 248)    # primary text
TEXT2    = (160, 160, 178)    # secondary text
TEXT3    = (100, 100, 118)    # muted text
WHITE    = (255, 255, 255)

# ── font helpers ─────────────────────────────────────────────────────────────
def load_font(size, bold=False):
    """Try system fonts; fall back to PIL default."""
    candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()


def text_size(draw, text, font):
    """Return (width, height) for text with given font."""
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


# ── drawing primitives ────────────────────────────────────────────────────────
PHONE_W, PHONE_H = 390, 780   # portrait phone canvas

def new_phone_canvas():
    img = Image.new("RGB", (PHONE_W, PHONE_H), BG)
    return img, ImageDraw.Draw(img)


def rounded_rect(draw, xy, radius=12, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                           outline=outline, width=width)


def status_bar(draw, label="Demo App"):
    """Fake phone status bar."""
    draw.rectangle([0, 0, PHONE_W, 44], fill=SURFACE)
    font = load_font(13)
    draw.text((16, 14), "9:41", fill=TEXT2, font=font)
    draw.text((PHONE_W // 2 - 30, 14), label, fill=TEXT2, font=font)
    draw.text((PHONE_W - 60, 14), "●●● 100%", fill=TEXT2, font=font)


def nav_tab_bar(draw, active="journal"):
    """Bottom tab bar: Journal | Ideas | History."""
    tabs = [("Journal", "journal"), ("Ideas", "ideas"), ("History", "history")]
    bar_y = PHONE_H - 62
    draw.rectangle([0, bar_y, PHONE_W, PHONE_H], fill=SURFACE)
    draw.line([0, bar_y, PHONE_W, bar_y], fill=BORDER, width=1)
    tab_w = PHONE_W // len(tabs)
    font_sm = load_font(12)
    for i, (label, key) in enumerate(tabs):
        cx = i * tab_w + tab_w // 2
        color = ACCENT if key == active else TEXT3
        draw.text((cx - text_size(draw, label, font_sm)[0] // 2, bar_y + 20),
                  label, fill=color, font=font_sm)
        if key == active:
            dot_y = bar_y + 10
            draw.ellipse([cx - 3, dot_y - 3, cx + 3, dot_y + 3], fill=ACCENT)


def section_label(draw, y, text):
    font = load_font(11)
    draw.text((16, y), text.upper(), fill=TEXT3, font=font)
    return y + 20


# ── SCREENSHOT 1 — Capture screen ────────────────────────────────────────────
def make_capture_screen():
    img, draw = new_phone_canvas()
    status_bar(draw, "Journal")

    # Header
    f_title = load_font(20, bold=True)
    f_body  = load_font(15)
    f_sm    = load_font(13)
    f_xs    = load_font(11)

    draw.text((16, 56), "Today", fill=TEXT1, font=f_title)
    draw.text((16, 82), "14 Jun 2026", fill=TEXT2, font=f_sm)

    # Score row
    rounded_rect(draw, [16, 110, PHONE_W - 16, 154], radius=10, fill=SURFACE2)
    draw.text((24, 120), "Daily score", fill=TEXT2, font=f_sm)
    # Score dots
    for i in range(1, 6):
        cx = 200 + i * 28
        color = ACCENT if i <= 3 else SURFACE
        draw.ellipse([cx - 10, 126, cx + 10, 146], fill=color)
    draw.text((200 + 1 * 28 - 12, 128), "3", fill=TEXT1 if True else TEXT3, font=f_xs)

    # Entry textarea
    rounded_rect(draw, [16, 166, PHONE_W - 16, 380], radius=12,
                 fill=SURFACE2, outline=BORDER, width=1)
    draw.text((28, 178), "What's on your mind?", fill=TEXT3, font=f_sm)

    # Synthetic text lines
    lines = [
        "Finished the morning walk earlier",
        "than planned — felt good.",
        "",
        "Need to revisit the project brief",
        "before the end of the week.",
        "",
        "Reminder: call back re: Thursday.",
    ]
    y = 208
    for line in lines:
        col = TEXT1 if line else BG
        draw.text((28, y), line, fill=col, font=f_body)
        y += 22

    # Tags row
    rounded_rect(draw, [16, 392, PHONE_W - 16, 428], radius=8, fill=SURFACE2)
    draw.text((24, 404), "Tags:", fill=TEXT2, font=f_sm)
    tags = ["morning", "work", "+ add"]
    tx = 72
    for tag in tags:
        tw, _ = text_size(draw, tag, f_xs)
        col = ACCENT if tag != "+ add" else TEXT3
        outline_col = ACCENT if tag != "+ add" else BORDER
        rounded_rect(draw, [tx - 6, 402, tx + tw + 6, 422],
                     radius=6, outline=outline_col, width=1)
        draw.text((tx, 406), tag, fill=col, font=f_xs)
        tx += tw + 18

    # Idea toggle
    rounded_rect(draw, [16, 440, PHONE_W - 16, 482], radius=10, fill=SURFACE2)
    draw.text((24, 454), "Mark as Idea", fill=TEXT2, font=f_sm)
    # Toggle off
    draw.rounded_rectangle([PHONE_W - 68, 456, PHONE_W - 28, 476],
                           radius=10, fill=BORDER)
    draw.ellipse([PHONE_W - 66, 458, PHONE_W - 46, 474], fill=TEXT3)

    # Save button
    rounded_rect(draw, [16, 500, PHONE_W - 16, 546], radius=12, fill=ACCENT)
    label = "Save entry"
    lw, _ = text_size(draw, label, f_body)
    draw.text(((PHONE_W - lw) // 2, 516), label, fill=BG, font=f_body)

    nav_tab_bar(draw, active="journal")
    img.save(SCREENSHOTS / "01-capture-demo.png")
    print("  OK 01-capture-demo.png")


# ── SCREENSHOT 2 — Idea mode ──────────────────────────────────────────────────
def make_idea_screen():
    img, draw = new_phone_canvas()
    status_bar(draw, "Ideas")

    f_title = load_font(20, bold=True)
    f_body  = load_font(15)
    f_sm    = load_font(13)
    f_xs    = load_font(11)

    draw.text((16, 56), "Ideas", fill=TEXT1, font=f_title)
    draw.text((16, 82), "Capture and revisit evolving thoughts", fill=TEXT2, font=f_sm)

    # Idea title field
    rounded_rect(draw, [16, 110, PHONE_W - 16, 154], radius=10,
                 fill=SURFACE2, outline=ACCENT2, width=2)
    draw.text((24, 122), "Title", fill=TEXT3, font=f_xs)
    draw.text((24, 136), "A framework for weekly planning", fill=TEXT1, font=f_sm)

    # Body area
    rounded_rect(draw, [16, 166, PHONE_W - 16, 400], radius=12,
                 fill=SURFACE2, outline=BORDER, width=1)
    draw.text((28, 178), "Notes", fill=TEXT3, font=f_xs)

    idea_lines = [
        "The current weekly review is inconsistent.",
        "",
        "Idea: start with three questions —",
        "  · What moved forward this week?",
        "  · What got stuck?",
        "  · What is the one priority for",
        "    the next seven days?",
        "",
        "Keep the format short enough to",
        "actually use on a Sunday evening.",
    ]
    y = 202
    for line in idea_lines:
        col = TEXT1 if line.strip() else BG
        draw.text((28, y), line, fill=col, font=load_font(14))
        y += 20

    # Revision note
    rounded_rect(draw, [16, 412, PHONE_W - 16, 452], radius=8, fill=SURFACE2)
    draw.text((24, 422), "Last edited:", fill=TEXT3, font=f_xs)
    draw.text((100, 422), "13 Jun 2026", fill=TEXT2, font=f_xs)
    draw.text((24, 436), "Revision:", fill=TEXT3, font=f_xs)
    draw.text((100, 436), "v3", fill=ACCENT2, font=f_xs)

    # Tags
    rounded_rect(draw, [16, 464, PHONE_W - 16, 500], radius=8, fill=SURFACE2)
    draw.text((24, 476), "Tags:", fill=TEXT2, font=f_sm)
    tags2 = ["planning", "habits"]
    tx = 72
    for tag in tags2:
        tw, _ = text_size(draw, tag, f_xs)
        rounded_rect(draw, [tx - 6, 474, tx + tw + 6, 494],
                     radius=6, outline=ACCENT2, width=1)
        draw.text((tx, 478), tag, fill=ACCENT2, font=f_xs)
        tx += tw + 14

    # Save button (purple for idea mode)
    rounded_rect(draw, [16, 514, PHONE_W - 16, 558], radius=12, fill=ACCENT2)
    label = "Save idea"
    lw, _ = text_size(draw, label, f_body)
    draw.text(((PHONE_W - lw) // 2, 530), label, fill=WHITE, font=f_body)

    nav_tab_bar(draw, active="ideas")
    img.save(SCREENSHOTS / "02-idea-demo.png")
    print("  OK 02-idea-demo.png")


# ── SCREENSHOT 3 — History / list view ───────────────────────────────────────
def make_history_screen():
    img, draw = new_phone_canvas()
    status_bar(draw, "History")

    f_title = load_font(20, bold=True)
    f_body  = load_font(15)
    f_sm    = load_font(13)
    f_xs    = load_font(11)

    draw.text((16, 56), "History", fill=TEXT1, font=f_title)

    # Search bar
    rounded_rect(draw, [16, 90, PHONE_W - 16, 128], radius=10,
                 fill=SURFACE2, outline=BORDER, width=1)
    draw.text((28, 105), "🔍  Search entries and ideas…", fill=TEXT3, font=f_sm)

    # Entry rows
    entries = [
        ("14 Jun 2026", "journal", "Finished the morning walk earlier…", ["morning", "work"], "3"),
        ("13 Jun 2026", "idea",    "A framework for weekly planning — keep the…", ["planning"], ""),
        ("12 Jun 2026", "journal", "Good session. Needed to adjust scope on…", ["work"], "4"),
        ("11 Jun 2026", "journal", "Quiet day. Read for an hour in the evening.", ["reading"], "2"),
        ("10 Jun 2026", "idea",    "Offline-first notes app pattern — revisit…", ["tech"], ""),
        ("09 Jun 2026", "journal", "Walked to the coffee place, then worked from…", ["morning"], "5"),
    ]

    y = 142
    for date, kind, snippet, tags, score in entries:
        row_h = 86
        fill_col = SURFACE2
        rounded_rect(draw, [16, y, PHONE_W - 16, y + row_h - 4],
                     radius=10, fill=fill_col)

        # Type badge
        badge_col = ACCENT2 if kind == "idea" else ACCENT
        badge_label = "idea" if kind == "idea" else "journal"
        bw, _ = text_size(draw, badge_label, f_xs)
        rounded_rect(draw, [24, y + 8, 24 + bw + 12, y + 24],
                     radius=5, fill=badge_col)
        draw.text((30, y + 10), badge_label, fill=WHITE, font=f_xs)

        # Date
        draw.text((24 + bw + 18, y + 10), date, fill=TEXT3, font=f_xs)

        # Score dot
        if score:
            draw.text((PHONE_W - 40, y + 10), f"●{score}", fill=ACCENT, font=f_xs)

        # Snippet
        draw.text((24, y + 32), snippet[:48] + ("…" if len(snippet) > 48 else ""),
                  fill=TEXT2, font=f_xs)

        # Tags
        tx = 24
        ty = y + 54
        for tag in tags:
            tw, _ = text_size(draw, tag, f_xs)
            rounded_rect(draw, [tx - 4, ty - 2, tx + tw + 4, ty + 14],
                         radius=4, outline=BORDER, width=1)
            draw.text((tx, ty), tag, fill=TEXT3, font=f_xs)
            tx += tw + 12

        y += row_h

    nav_tab_bar(draw, active="history")
    img.save(SCREENSHOTS / "03-history-demo.png")
    print("  OK 03-history-demo.png")


# ── DIAGRAM helpers ───────────────────────────────────────────────────────────
DIAG_W, DIAG_H = 800, 520
DIAG_BG     = (245, 247, 252)
DIAG_BOX    = (255, 255, 255)
DIAG_BORDER = (180, 190, 210)
DIAG_ACCENT = (59, 130, 246)    # blue
DIAG_PURPLE = (124, 58, 237)
DIAG_GREEN  = (16, 185, 129)
DIAG_TEXT   = (30, 30, 50)
DIAG_MUTED  = (100, 110, 130)
DIAG_ARROW  = (80, 90, 110)


def new_diag_canvas(title):
    img = Image.new("RGB", (DIAG_W, DIAG_H), DIAG_BG)
    draw = ImageDraw.Draw(img)
    # header band
    draw.rectangle([0, 0, DIAG_W, 48], fill=DIAG_ACCENT)
    f = load_font(16, bold=True)
    draw.text((20, 14), title, fill=WHITE, font=f)
    draw.text((DIAG_W - 200, 14), "— synthetic demo —", fill=(200, 220, 255), font=load_font(12))
    return img, draw


def box(draw, cx, cy, w, h, label, sublabel=None, color=DIAG_ACCENT, radius=10):
    x0, y0 = cx - w // 2, cy - h // 2
    x1, y1 = cx + w // 2, cy + h // 2
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius,
                           fill=DIAG_BOX, outline=color, width=2)
    f_main = load_font(13, bold=True)
    f_sub  = load_font(11)
    tw, th = text_size(draw, label, f_main)
    draw.text((cx - tw // 2, cy - th // 2 - (8 if sublabel else 0)),
              label, fill=DIAG_TEXT, font=f_main)
    if sublabel:
        sw, _ = text_size(draw, sublabel, f_sub)
        draw.text((cx - sw // 2, cy + th // 2 - 4), sublabel,
                  fill=DIAG_MUTED, font=f_sub)


def arrow(draw, x0, y0, x1, y1, label=None):
    draw.line([x0, y0, x1, y1], fill=DIAG_ARROW, width=2)
    # arrowhead
    import math
    angle = math.atan2(y1 - y0, x1 - x0)
    size = 8
    for da in (0.4, -0.4):
        ax = x1 - size * math.cos(angle - da)
        ay = y1 - size * math.sin(angle - da)
        draw.line([x1, y1, int(ax), int(ay)], fill=DIAG_ARROW, width=2)
    if label:
        mx, my = (x0 + x1) // 2, (y0 + y1) // 2
        draw.text((mx + 4, my - 14), label, fill=DIAG_MUTED, font=load_font(10))


# ── DIAGRAM 1 — Context diagram ───────────────────────────────────────────────
def make_context_diagram():
    img, draw = new_diag_canvas("Journal App — Context Diagram")

    # Person
    cx, cy = 400, 110
    draw.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=DIAG_ACCENT)
    draw.text((cx - 12, cy - 10), "👤", fill=WHITE, font=load_font(20))
    draw.text((cx - 12, cy + 28), "User", fill=DIAG_TEXT, font=load_font(12))

    # Mobile PWA
    box(draw, 400, 230, 190, 60, "Mobile PWA",
        "Svelte + Vite, offline-first", color=DIAG_ACCENT)
    arrow(draw, 400, 132, 400, 198, "writes")

    # Private file store
    box(draw, 200, 370, 200, 60, "Private file store",
        "OneDrive · Markdown/JSON", color=DIAG_GREEN)
    arrow(draw, 315, 252, 235, 338, "saves records")

    # My Life desktop
    box(draw, 600, 370, 200, 60, "My Life (desktop)",
        "local projection · search", color=DIAG_PURPLE)
    arrow(draw, 485, 252, 565, 338, "indexes into")

    # AI layer
    box(draw, 400, 470, 200, 50, "AI-assisted layer",
        "summarise · retrieve · human oversight", color=(200, 80, 80))
    arrow(draw, 600, 400, 490, 458, "feeds")
    arrow(draw, 200, 400, 310, 458, "feeds")

    img.save(DIAGRAMS / "context-diagram.png")
    print("  OK context-diagram.png")


# ── DIAGRAM 2 — Data flow ─────────────────────────────────────────────────────
def make_data_flow():
    img, draw = new_diag_canvas("Journal App — Data Flow")

    steps = [
        (100, 240, "Capture", "Mobile PWA\nentry / idea", DIAG_ACCENT),
        (260, 240, "Local store", "IndexedDB\ncache + queue", DIAG_MUTED),
        (420, 240, "Write queue", "serialised\nasync writes", DIAG_ARROW),
        (580, 240, "File record", "Markdown/YAML\nor JSON", DIAG_GREEN),
        (740, 240, "File store", "OneDrive\nprivate folder", DIAG_GREEN),
    ]

    for i, (cx, cy, title, sub, col) in enumerate(steps):
        box(draw, cx, cy, 130, 80, title, sub, color=col)
        if i < len(steps) - 1:
            arrow(draw, cx + 65, cy, cx + 130 - 65 + (260 - 130), cy)

    # Desktop projection row
    box(draw, 580, 390, 160, 60, "Desktop projection",
        "local index · search", color=DIAG_PURPLE)
    arrow(draw, 740, 280, 740, 340)
    arrow(draw, 740, 340, 650, 358)

    box(draw, 200, 390, 160, 60, "Recovery path",
        "in-progress text\nrestore on reopen", color=(180, 120, 0))
    arrow(draw, 200, 280, 200, 358)

    img.save(DIAGRAMS / "data-flow.png")
    print("  OK data-flow.png")


# ── DIAGRAM 3 — Privacy boundary ─────────────────────────────────────────────
def make_privacy_boundary():
    img, draw = new_diag_canvas("Journal App — Privacy Boundary")

    # Private zone
    draw.rounded_rectangle([40, 70, 500, 460], radius=16,
                           fill=(255, 240, 240), outline=(220, 80, 80), width=2)
    draw.text((50, 78), "🔒  Private zone — never published", fill=(180, 50, 50),
              font=load_font(12, bold=True))

    private_items = [
        (270, 150, "Real journal entries", "actual thoughts and records"),
        (270, 240, "Personal tags / context", "real categories and life context"),
        (270, 330, "Private file paths", "OneDrive folder locations"),
        (270, 400, "Account identifiers", "user IDs, tokens, emails"),
    ]
    for cx, cy, title, sub in private_items:
        box(draw, cx, cy, 340, 56, title, sub, color=(220, 80, 80), radius=8)

    # Public zone
    draw.rounded_rectangle([520, 70, 770, 460], radius=16,
                           fill=(240, 255, 245), outline=(16, 185, 129), width=2)
    draw.text((530, 78), "✅  Public zone", fill=(10, 130, 80),
              font=load_font(12, bold=True))

    public_items = [
        (645, 155, "Synthetic\nscreenshots", DIAG_GREEN),
        (645, 260, "Architecture\ndiagrams", DIAG_GREEN),
        (645, 355, "Design\ntrade-offs", DIAG_GREEN),
        (645, 440, "AI-assisted\nbuilder notes", DIAG_GREEN),
    ]
    for cx, cy, title, col in public_items:
        lines = title.split("\n")
        x0, y0 = cx - 80, cy - 34
        draw.rounded_rectangle([x0, y0, x0 + 160, y0 + 68],
                               radius=8, fill=DIAG_BOX, outline=col, width=2)
        f = load_font(12, bold=True)
        for j, line in enumerate(lines):
            lw, _ = text_size(draw, line, f)
            draw.text((cx - lw // 2, cy - 12 + j * 18), line, fill=DIAG_TEXT, font=f)

    img.save(DIAGRAMS / "privacy-boundary.png")
    print("  OK privacy-boundary.png")


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Building screenshots…")
    make_capture_screen()
    make_idea_screen()
    make_history_screen()

    print("Building diagrams…")
    make_context_diagram()
    make_data_flow()
    make_privacy_boundary()

    print("\nDone. All assets written to assets/screenshots/ and assets/diagrams/")

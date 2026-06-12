"""
Build synthetic demo assets for the Journal App public showcase.
Outputs:
  screenshots/01-capture-demo.png
  screenshots/02-idea-demo.png
  screenshots/03-history-demo.png

All content is synthetic. No real journal text, names, or private data.
Run from the assets/ directory or adjust BASE_DIR below.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

# ── paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
SCREENSHOTS = BASE_DIR / "screenshots"

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
        "The current weekly planning loop is inconsistent.",
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


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Building screenshots…")
    make_capture_screen()
    make_idea_screen()
    make_history_screen()

    print("\nDone. Screenshot assets written to assets/screenshots/")

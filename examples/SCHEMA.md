# Journal App — Example Data Schema

> **All example content in this directory is entirely fabricated synthetic demo data.**
> No real journal entries, ideas, or personal information are present anywhere in this folder.
> Files are provided solely to illustrate the data format for the showcase repository.

---

## Overview

The Life Journal app stores two kinds of records: **journal entries** and **ideas**.
Both kinds live in a personal OneDrive folder that syncs across devices.
A local SQLite database (managed by the desktop portal's Rust backend) indexes the files for fast search, tagging, and timeline views.

---

## File Naming

| Kind | Real app | Showcase examples |
|------|----------|-------------------|
| Journal entry | `entries/<UUID>.md` | `journal/YYYY-MM-DD.md` |
| Idea | `ideas/<UUID>.md` | `ideas/YYYY-MM-DD.md` |

In production, files use UUID v5 names so that the same entry always resolves to the same path regardless of the device that created it. The showcase uses date-based names for human readability only.

---

## Markdown Format

Every file is a Markdown document with optional YAML frontmatter, followed by the entry body.

### Frontmatter fields

```yaml
id: string          # UUID v5 — stable unique identifier
kind: entry | idea  # record type
captured_on: string # YYYY-MM-DD — the local calendar date the entry belongs to
created_at: string  # ISO 8601 UTC — when the record was first written
updated_at: string  # ISO 8601 UTC — when the record was last modified
source: string      # "phone" | "laptop" — which device created/last edited it
title: string|null  # Optional for entries; required for ideas
tags:               # zero or more taxonomy tags
  - slug: string    # e.g. "health/sport", "reflection/general"
    label: string   # human-readable label, e.g. "Sport"
primary_category_key:   string|null  # top-level category slug, e.g. "health"
primary_category_label: string|null  # e.g. "Health"
primary_sub_label:      string|null  # sub-category label, e.g. "Sport"
# Ideas only:
revisions: []       # array of prior revision snapshots (see below)
```

### Revision snapshots (ideas only)

When an idea body is meaningfully edited, the previous version is archived as a revision:

```yaml
revisions:
  - rev_index: 0          # 0 = oldest archived revision
    rev_at: string        # ISO 8601 UTC timestamp of that version
    rev_source: string    # "phone" | "laptop"
    title: string|null    # title at the time of that revision
    body: string          # body text at the time of that revision
```

The current (live) body is always in the Markdown body section below the frontmatter.

---

## Entry types

### Journal entry (`kind: entry`)

A free-form daily reflection. One entry per day is typical but not enforced.
`title` is nullable — most mobile entries are untitled.
`kids_score` (not shown in file examples; stored in a separate scores table) is an optional integer rating 1–5 for the day.

### Idea (`kind: idea`)

A candidate thought that has been captured for later consideration.
`title` is required. Ideas carry a `revisions` array that preserves the full edit history.
An idea's status (candidate → decided / abandoned) is tracked as a freeform note in the body rather than a formal state field.

---

## Tag taxonomy

Tags follow a `category/subcategory` slug convention. Examples:

| Slug | Label |
|------|-------|
| `reflection/general` | Reflection |
| `mindset/clarity` | Clarity |
| `daily/recap` | Daily Recap |
| `productivity/systems` | Systems |
| `productivity/focus` | Focus |
| `habits/morning` | Morning Routine |

The full taxonomy is stored in `taxonomy.json` at the OneDrive root and versioned alongside the app.

---

## Storage

Files sync via OneDrive. The desktop portal reads the synced local copy and maintains a SQLite index for fast querying. The mobile PWA writes directly to the OneDrive folder; the portal detects changes on next open.

---

## Example files in this directory

| File | Kind | Date | Notes |
|------|------|------|-------|
| `journal/2026-04-15.md` | entry | 2026-04-15 | Reflective tone, two tags |
| `journal/2026-04-18.md` | entry | 2026-04-18 | Quick daily recap, one tag |
| `journal/2026-04-22.md` | entry | 2026-04-22 | Thought captured mid-walk |
| `ideas/2026-04-16.md` | idea | 2026-04-16 | Candidate idea, no revisions |
| `ideas/2026-04-20.md` | idea | 2026-04-20 | Candidate idea, one archived revision |

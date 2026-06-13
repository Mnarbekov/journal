# How it works

The Journal app has two sides: a phone app for fast capture, and my desktop app (My Life) for searching and reflecting later.

```text
[Phone app]
  - write a journal note or switch to idea mode
  - saves on the device first, so nothing is lost on a bad connection
        |
        v
[Private files, synced through OneDrive]
  - journal entries and ideas as simple text files
  - light tags and a small daily score
        |
        v
[My Life on the laptop]
  - reads those files into a local search view
  - browse, search, and reflect on past writing
```

## A few design choices

1. **Capture first, organise later.** The phone screen stays small: write, tag if it helps, save. Anything heavier belongs on the desktop.
2. **Notes and ideas are different things.** A journal note is a record of a moment. An idea is something I come back to and reshape, so it gets a title and can keep its earlier versions.
3. **Plain, portable files.** Entries are saved as simple text files that are easy to keep, read, and search years later.
4. **One light signal, not a dashboard.** There's a single daily score for a sense of trend, not a wall of charts that turns journaling into admin.

## The example entries

The `examples/` folder shows the format I save in, with made-up journal notes and ideas. `examples/SCHEMA.md` explains what each entry contains.

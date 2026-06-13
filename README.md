# Journal App

A private-first journaling app I built to make daily writing quick to capture and easy to come back to later.

This repo is a demo-safe version. It explains how the app works and includes example entry files, but none of my real journal content.

## Why I built it

I've journaled for about five years. Paper was too slow because I needed the notebook on me at the exact moment. Apple Notes was easier, but it turned into one long stream I almost never went back to. Capturing was fine; returning to anything was the problem.

So I built a small app for it: something that opens fast on my phone, keeps writing simple, and lets longer-running ideas stay alive instead of getting buried. The captured writing then connects to my desktop app, My Life, where I can search and reflect on it.

## What it does

- Captures quick journal entries from a phone-first screen.
- Keeps everyday notes separate from ideas that need more time.
- Allows light categories and a simple daily signal, without turning writing into admin.
- Saves entries as portable files that sync through OneDrive.
- Connects captured writing to a desktop search and reflection workflow.

## Screenshots and workflow

![Journal app phone capture screen](assets/screenshots/journal-phone-capture.png)

The phone capture screen, using demo content.

![How phone capture connects to storage and desktop search](assets/diagrams/journal-bridge.png)

The flow: capture on the phone, save and sync through OneDrive, search and reflect on the desktop.

## What's in this repo

- `examples/journal/` and `examples/ideas/` — example entry files that show the format I save in (all made up).
- `examples/SCHEMA.md` — a plain description of what each entry contains.
- `docs/architecture.md` — a short walkthrough of how phone capture connects to desktop search.

## Privacy

This is a demo-safe version. My real journal entries stay private and are not in this repo. The example entries are invented.

## Built with AI assistance

I'm not a software developer. I shaped the idea, the way capture should feel, and the decisions about what to leave out, then used AI tools to help build it. The value here is fixing a real habit of mine and turning it into something that works.

## Related

- Portfolio: https://www.mikhailnarbekov.com
- Medium story: [I Built a Journaling App Because I Kept Losing My Own Thinking](https://medium.com/@mikhail.narbekov/i-built-a-journaling-app-because-i-kept-losing-my-own-thinking-e86cfc0177d2)
- GitHub: https://github.com/Mnarbekov

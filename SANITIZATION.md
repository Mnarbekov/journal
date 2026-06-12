# Journal App — Sanitization Checklist

Use this checklist for anything from this showcase that appears in a public repository or portfolio page.

## Publishing rule

This package explains the product, workflow, architecture, and AI-assisted build process. It must not expose the real contents of the journal system.

## Never publish

- [ ] Real journal entries, idea text, scores, tags, schedules, messages, health notes, finance notes, or personal records.
- [ ] Names, emails, account identifiers, browser chrome, notifications, or private relationship context visible in screenshots.
- [ ] Local machine paths, private folder names, raw database files, logs, exports, or run history.
- [ ] Sensitive configuration, browser session details, or private service setup.
- [ ] Full private source files copied from the working app.
- [ ] Screenshots taken from the live private dataset.

## Safe public material

- [ ] Product narrative in first-person voice.
- [ ] Written architecture notes with generic component names.
- [ ] Screenshots recreated with synthetic demo records and synthetic categories only.
- [ ] Small pseudocode or simplified snippets that explain a pattern without exposing implementation detail.
- [x] High-level technology choices such as PWA, Svelte, IndexedDB, OneDrive, Markdown/YAML, and JSON.

## Screenshot safety

1. Create demo records that are obviously fictional.
2. Use generic names such as “Demo reflection”, “Project idea”, and “Weekly note”.
3. Use synthetic categories such as “Ideas”, “Reflection”, and “Work demo”; do not expose real category names if they reveal private life context.
4. Check the whole image, including browser/app chrome, tabs, account UI, dates, and notifications.
5. Save only final public-safe images under `assets/screenshots/`.
6. Re-open the saved image before publishing and inspect it at full size.

## Snippet safety

1. Prefer pseudocode or trimmed examples.
2. Use fake IDs, fake dates, fake tags, and generic body text.
3. Remove endpoints, local paths, account values, logs, and implementation-only comments.
4. Keep snippets explanatory rather than comprehensive.

## Safety search

Search the showcase folder for:

- private path markers;
- live account identifiers;
- private configuration values;
- raw journal phrases;
- names, emails, phone numbers, or addresses;
- source-only implementation comments that reveal private operations.

## Current public package state

- [x] Public-facing files use generic wording.
- [x] No real journal content intentionally included.
- [x] Screenshot references require approved public-safe demo content only.

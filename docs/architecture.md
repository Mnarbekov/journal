# Journal App — Architecture

## Architecture summary

The system is a private-first journaling workflow with two complementary surfaces: a mobile PWA for fast capture and the My Life laptop app for reflection, search, and future analysis. The mobile app keeps a local cache and write queue, saves portable records as Markdown/YAML or JSON through OneDrive, and treats the desktop database as a projection rather than the source of truth.

## Public-safe context model

```text
[Me]
  |
  v
[Mobile PWA]
  |-- local cache + in-progress text recovery
  |-- foreground write queue
  |
  v
[Private app-folder file store]
  |-- journal entries as Markdown/YAML
  |-- ideas as Markdown/YAML
  |-- scores and taxonomy as JSON
  |
  v
[My Life desktop projection]
  |-- local index
  |-- search and reflect
  |-- future AI-assisted reflection with human oversight
```

The public showcase focuses on one approved screenshot and written architecture notes rather than generated placeholder visuals.

## Main components

| Component | Role | Public showcase treatment |
|---|---|---|
| Mobile PWA | Fast capture surface for entries, ideas, tags, and score updates. | Show only through the approved public screenshot. |
| Local browser store | Holds in-progress text, caches, scores, taxonomy, and queued writes. | Explain conceptually; no real data exports. |
| Write queue | Serializes writes and protects against fragile mobile lifecycle events. | Explain conceptually; do not publish logs. |
| File records | Portable Markdown/YAML and JSON records. | Use tiny synthetic examples only if needed. |
| My Life desktop projection | Indexes private files into a local searchable view for reflection and search. | Describe as projection/cache, not source data. |
| AI-assisted layer | Future summarization, reflection, and retrieval workflows. | Emphasize human oversight and privacy boundary. |

## Technology choices

- **Svelte + Vite PWA:** small mobile surface, fast iteration, simple static deployment.
- **IndexedDB via Dexie:** practical local cache, in-progress text recovery, and queue storage.
- **Service worker:** app shell availability and update flow; business writes remain app-controlled.
- **OneDrive private app folder:** browser-based write path for portable record storage.
- **Markdown/YAML and JSON:** portable, inspectable record formats that are easy to index later.
- **Local desktop projection:** search and insight workflows can run against a disposable local index instead of mutating source records directly.

## Data model, public version

### Journal entry

A journal entry is a timestamped Markdown record with frontmatter for metadata such as ID, type, capture date, tags, and schema version. The body stays plain text/Markdown.

### Idea

An idea is similar to an entry, but has a title and is designed to be revisited. Earlier versions can be preserved so refinement does not erase the thinking trail.

### Taxonomy

The tag vocabulary is stored separately as a versioned JSON document. The phone can add lightweight tags; deeper cleanup belongs in the desktop layer.

### Score

A small monthly JSON record stores the daily score signal. The point is trend awareness, not turning reflection into a metrics dashboard.

## Reliability and conflict approach

- In-progress text is saved locally while typing.
- Blank records are discarded rather than cluttering history.
- Mobile lifecycle events trigger save attempts where possible.
- Writes are queued and serialized to reduce race conditions.
- Editable idea records use optimistic concurrency where needed.
- The private file store remains the durable truth; local browser and desktop databases are caches/projections.

## Privacy boundary

Public material may show:

- written component notes;
- the approved public screenshot;
- generic file-shape examples;
- product trade-offs;
- AI-assisted workflow notes.

Public material must not show:

- real journal text;
- real tags if they reveal private life context;
- real schedules, people, health, finance, or messages;
- local machine paths;
- private account identifiers;
- private configuration values;
- raw database exports or logs.

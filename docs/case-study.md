# Journal App — Case Study

## Summary

I have been journaling for about five years. Paper did not work because I needed the notebook with me all the time. Apple Notes worked better, but it slowly became a capture-and-forget habit: I would write something down, then almost never return to it. I built this app to make capture fast, keep my thoughts organised, and connect them to my laptop app, My Life, so the things I have written are easier to revisit and use.

## Problem

My notes and reflections were valuable, but the workflow had predictable failure points:

- capture needed to be faster than opening a heavyweight system;
- paper was too easy to leave behind;
- Apple Notes was convenient, but one long note was a poor place for long-term retrieval;
- ideas and diary-style reflections needed different treatment;
- categories and scores were useful only if they stayed lightweight;
- private content could not become portfolio material;
- long-term value required a format I could keep, inspect, and index.

The product challenge was to design for the real behaviour: short bursts of mobile capture, ideas that evolve over time, occasional desktop working sessions in My Life, and a strong privacy boundary.

## Product approach

I shaped the app around four principles.

### 1. Capture first, analysis later

The phone surface is deliberately small: write, tag when helpful, mark an idea if needed, save. The architecture supports later search and reflection, but the capture moment is protected from complexity.

### 2. Journal entries and ideas are different objects

A journal entry is a record of a moment. An idea is something I may revisit and reshape. Separating them made the product clearer: quick reflection stays quick, while reusable thoughts get a title and can evolve.

### 3. My Life makes the archive useful again

The mobile app is for capture. My Life, the laptop app, is where the archive becomes easier to search, revisit, and connect with other personal context. I am not claiming that AI magically remembers my life; the point is more practical: thoughts I already captured are now easier to find and work with.

### 4. Privacy is a product feature

The public story can show the workflow, architecture, and design thinking without exposing the actual contents. This showcase uses one approved public-safe screenshot and synthetic examples only.

## Workflow

1. Open the mobile app.
2. Capture a journal note or switch into idea mode.
3. Add a category only if it helps future retrieval.
4. Save into portable private records.
5. Revisit entries later through history, search, or My Life on the laptop.
6. Use AI-assisted workflows only where human oversight remains in control.

## AI-assisted builder framing

My role was to define the problem, keep the product honest, make trade-offs, and test whether the workflow fit real life. AI tools helped accelerate implementation, documentation, refactoring, and option generation. I treated AI output as useful acceleration, always subject to product judgement and testing.

## Trade-offs

| Decision | Why it mattered |
|---|---|
| Local-first cache plus cloud-backed files | Fast capture and portable records without making a server the centre of the system. |
| Plain Markdown/YAML and JSON records | Long-term readability and easy indexing into other tools. |
| Mobile adds lightweight categories; desktop can curate taxonomy | Keeps phone capture simple while preserving richer management later. |
| One lightweight score, not a dashboard of metrics | Reduces tracking fatigue and protects the reflective feel of the app. |
| Public showcase uses one approved visual and synthetic examples | Demonstrates the system without turning private life into content. |

## Outcome

This project gives me a practical example of AI-assisted product building: not “prompt to app”, but an iterative loop of problem framing, architecture choices, implementation help, real testing, and privacy-aware documentation. More importantly, it changed the journaling loop from “capture and forget” to “capture, organise, and come back when the thought is useful again.”

Observable outcomes:

- faster mobile capture for journal notes and ideas;
- clearer separation between fleeting reflections and reusable ideas;
- a reusable local-first pattern for other personal systems;
- a safer bridge between mobile capture and laptop-based reflection in My Life;
- a safe public story that proves capability without exposing private data.

## What it proves

This project demonstrates that I can:

- spot a real workflow problem in my own life;
- turn it into a simple product shape;
- guide AI-assisted implementation without pretending the AI was not involved;
- make architecture choices around privacy, portability, and future use;
- package the result for a public audience responsibly.

## Approved public screenshot

The public repository intentionally references one visual only: [`assets/screenshots/journal-phone-capture.png`](../assets/screenshots/journal-phone-capture.png).

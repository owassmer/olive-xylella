---
title: CORDON Wiki Schema
created: 2026-08-15
updated: 2026-08-15
type: schema
tags: [meta]
---

# Wiki Schema

## Domain

Project CORDON — the Apulian *Xylella fastidiosa* / olive-quick-decline crisis, the evidence for detection and resistance, and the computational program that Owen + Connor are running.

This wiki lives **inside the project**, not at `~/wiki`:

`/Users/owenwassmer/Desktop/Connor/olive-xylella/`

Contract of record: [[CORDON]] (`CORDON.md` at repo root).

## Conventions

- File names: lowercase, hyphens, no spaces
- Every wiki page starts with YAML frontmatter
- Use `[[wikilinks]]` (minimum 2 outbound links per page)
- Bump `updated` on every edit
- Every new page goes in `index.md`
- Every action is appended to `log.md`
- On pages synthesizing 3+ sources, mark claims `^[raw/...]`
- **raw/ is immutable.** Corrections go in wiki pages.
- Tree-count and euro figures that disagree stay contested. Never collapse them.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: []
sources: []
confidence: high | medium | low
contested: false
---
```

Raw sources also carry `source_url`, `ingested`, `sha256` of the body.

## Tag taxonomy

Add a tag here before using it.

- organism, pathogen, vector, cultivar, disease
- mechanism, resistance, detection, epidemiology, economics
- policy, dataset, method, project, person, org, place
- comparison, timeline, controversy, open-question
- meta

## Page thresholds

- Create a page when an entity/concept appears in 2+ sources OR is central to one source or to CORDON
- Don't create pages for passing mentions
- Split above ~200 lines
- Archive superseded pages to `_archive/`

## Update policy

Newer primary sources generally supersede older ones. If genuinely contradictory: keep both, date them, set `contested: true`, link `contradictions`.

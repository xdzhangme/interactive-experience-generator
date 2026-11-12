# Maintaining the offline pattern library

This is reference curation, not model training or a company-experience build.
The initial library has 30 original pattern descriptions. Later updates may
add records, improve evidence or remove unsupported entries with an explicit
replacement and explanation; do not keep a fixed-size quota at quality's expense.

## Research bounds

The approved local weekly job runs Mondays at 09:00 in the computer's local
time when the app/computer is available. Inspect at most 10 public
primary-source pages per run and add at most three genuinely useful patterns.
These limits apply to recurring refreshes, not the initial research batch.
Adding none is a valid result. No automatic commits, pushes or publication.

Start with Codrops Creative Hub and React Bits, then follow exact relevant
demo, documentation or source links. Focus on mechanisms that extend useful
coverage, not more color variants of the same background. Respect access
restrictions, each project's terms and React Bits' Commons Clause restriction
on redistributing component collections. Do not copy code, media, ports,
screenshots or substantial source prose into this library.

Inspect git status before editing. If overlapping uncommitted changes or
concurrent work make a safe update uncertain, stop and report the conflict.
Do not stash, reset, change branches or overwrite another session's changes.
Do not modify installed skill directories or other repositories.

## Record contract

`patterns.json` is UTF-8 JSON with `schema_version: 1` and a `patterns` array.
Each record uses these fields:

| Field | Required content |
|---|---|
| `id`, `name` | Stable, unique kebab-case ID and readable name. Do not rename IDs merely for style. |
| `source_family` | `codrops` or `react-bits`. |
| `source_url`, `reviewed_on` | Exact primary-source HTTPS URL and actual ISO review date. |
| `evidence` | `documentation`, `source-inspection` or `rendered-observation`. |
| `evidence_note` | What was inspected, discovery/provenance where needed, and what was not verified. |
| `mechanism`, `input`, `response` | Original factual summary of the reference's mechanism, input and response. |
| `user_goals`, `tags` | Nonempty arrays of useful visitor needs and retrieval terms. |
| `layout`, `motion` | Original analysis of structural use and motion relationships, without invented measurements. |
| `accessibility`, `offline`, `avoid` | Generator recommendations: equivalent operation, standalone implementation principles and situations where the pattern is a bad fit. |
| `licensing` | Exact-project reuse caution; inspiration does not imply code/asset permission. |

Keep all prose fields nonempty. Use one mechanism per record, clear enough
to apply without opening the link. Accessible/offline adaptations are proposed
alternatives, not assertions about the source's implementation.

Deduplicate by input, response and visitor purpose, not by component name,
color or framework. Compare candidate records against the existing library.
Update an existing entry when the mechanism is already covered. Recheck
changed source terms before reusing code; the library itself contains only
original analytical descriptions and source links.
Keep the stored-pattern directory in `INDEX.md` aligned with added or
removed IDs so agents can retrieve records without reading the whole JSON.

Do not mark rendered observation after reading code or a poster. Record
unavailable pages and unresolved behavior, and leave unsupported claims out.
Retain last-verified metadata when a source cannot be rechecked rather than
advancing its review date without inspection.

## Validate and package

From the repository root, using Python 3's standard library:

```powershell
python scripts\manage_patterns.py --check
python -m unittest discover -s evals -p "test_*.py"
python scripts\manage_patterns.py --package
```

`--check` validates record shape, IDs, dates, source URLs, evidence labels,
local workflow references and minimum library coverage. It does not open
URLs, evaluate visual quality or prove an interaction works.

`--package` repeats the static checks, writes only the approved skill
files into `dist\interactive-experience-generator.skill`, verifies every
archived byte against the source, then updates README package/pattern/eval
counts and SHA-256. README and evaluations stay outside the archive.
The optional bundled management script is included; Python is not needed
to read or use the library.

Inspect the diff and report changed IDs, sources, evidence limitations and
actual checks. Leave edits local for review. A human must approve subsequent
commit/push/publication; installed copies need re-importing after distribution.
If source or packaging checks fail, report the exact failure rather than
claiming a refresh succeeded.

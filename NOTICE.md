# Notice

This skill package is original work written for the interactive experience
generator workflow. Several reference files condense and adapt ideas from
the following third-party skills. Instruction references are original,
scoped summaries rather than verbatim skill copies. Third-party licence
and notice files are preserved as supplied. Attribution and the relevant
licence obligations are retained here and in the bundled legal files.

## Apache License 2.0 — Anthropic (github.com/anthropics/skills)

- **`skills/frontend-design`** — informs `references/art-direction.md`
  (subject-grounded design, typography and motion principles, anti-template
  critique, self-critique test).
- **`skills/webapp-testing`** — informs the inspection-and-revision section
  of `references/build-and-delivery.md` (reconnaissance-then-action review
  pattern).

Copyright Anthropic. Licensed under the Apache License, Version 2.0
(http://www.apache.org/licenses/LICENSE-2.0). This package is a derivative,
condensed work; the full licence text governs the original repository.

## Apache License 2.0 — Impeccable

- **Author/source:** Paul Bakaus and contributors,
  https://github.com/pbakaus/impeccable .
- **Source version:** installed Impeccable 4.8.0, pinned upstream tag
  `cli-v4.8.0`.
- **Adapted sources:** `.github/skills/impeccable/SKILL.md` (Experience
  mode and brief-preserving design principles),
  `reference/critique.md` (design specificity, visual inspection and
  separation of judgment from mechanical evidence), and
  `reference/polish.md` (prioritised refinement, scope preservation and
  complete-path verification).
- **Changed/derived file:** `references/experience-critique-polish.md`
  is an original web/standalone-HTML adaptation for this generator.
  `SKILL.md`, `references/art-direction.md` and
  `references/build-and-delivery.md` were changed to integrate that
  guidance beneath the existing message-first workflow.
- **Not bundled or required:** upstream binaries, commands, hooks,
  detector, live-edit servers, concept randomisation, native-platform
  references, mandatory multi-agent orchestration or external services.
  This package does not claim that the full Impeccable workflow ran.

Licensed under Apache License 2.0. The complete upstream licence is
included in `licenses/impeccable/Apache-2.0.txt`. The upstream notice is
preserved unmodified in `licenses/impeccable/UPSTREAM-NOTICE.md`; its
native-platform references are not included in this adaptation. Source
texts are available at
https://github.com/pbakaus/impeccable/tree/cli-v4.8.0 .
No endorsement or trademark rights are granted by this adaptation.

## MIT License

- **`arvindrk/extract-design-system`** — informs the brand-token fallback
  guidance in `references/art-direction.md` (extracting verified colour,
  type, and imagery directly from a company's official site when
  guidelines are unavailable).
- **`majidmanzarpour/threejs-game-skills`** (`threejs-aaa-graphics-builder`)
  — informs `references/threejs-craft.md` (authored-forms-first ordering,
  procedural geometry in place of absent official 3D assets, environment
  and surface coverage), with game-specific material removed.

Both are MIT-licensed; attribution to the original authors and repositories
is preserved here.

## Before external or customer-facing distribution
Facts, logos, and brand imagery used inside any generated experience come
from the target company's own official sources, not from this package.
Confirm logo/trademark usage and licensing terms with your own legal or
brand team before showing a generated experience outside your organization
— this package does not grant or verify those rights.

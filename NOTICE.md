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
  `reference/new-work.md` (respecting existing visual authority and
  resolving a coherent visual direction within scope),
  `reference/animate.md` (purposeful motion, input feedback, continuity,
  interruption and reduced-motion behavior),
  `reference/layout.md` (priority-led reading order, proximity, spacing
  rhythm, density and responsive/focus-order checks),
  `reference/critique.md` (design specificity, visual inspection and
  separation of judgment from mechanical evidence), and
  `reference/polish.md` (prioritised refinement, scope preservation and
  complete-path verification).
- **Changed/derived file:** `references/experience-critique-polish.md`
  is an original web/standalone-HTML adaptation for this generator.
  `references/art-direction.md` also adapts visual-direction guidance.
  `SKILL.md`, `references/art-direction.md` and
  `references/build-and-delivery.md` were changed to integrate that
  guidance beneath the existing message-first workflow.
- **Generator revision, 2026-11-04:** the integration now explicitly runs
  during builds and applicable revisions. Added original generator-specific
  intent/revision contracts, authored-input/privacy rules, route-state
  regression coverage and concrete web usability checks. These additions
  are not represented as verbatim upstream Impeccable instructions or a
  new upstream release.
- **Generator revision, 2026-11-09:** expanded the self-contained adaptation
  from late critique/polish to surface-mode selection, selected-concept
  execution direction and purposeful motion/feedback. Added original
  generator-specific interaction choreography, execution-history comparison,
  and a representative-scene checkpoint separating core meaning, visual
  character and interaction feel. Further original direction makes
  showcases scene-led and official-imagery/model-led, with restrained
  supporting art and actual-treatment proof in existing previews; it
  preserves practical task layouts rather than banning rectangular UI.
  These additions preserve approved concepts,
  brand constraints, accessible input and offline delivery. They do not
  bundle the full upstream skill/runtime or claim upstream commands ran.
- **Generator revision, 2026-11-11:** added
  `references/layout-motion-inspiration.md`, an original scoped adaptation
  of the pinned `reference/layout.md` and `reference/animate.md`. Combines
  structural layout checks and purpose-led timing/feedback with the
  existing scene gate. No detector, live-mode parameters, upstream skill
  invocation or agent orchestration is required.
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

## MIT License - Emil Kowalski

- **Author/source:** Emil Kowalski,
  https://github.com/emilkowalski/skills .
- **Source revision:** `715c1807e08c497cfd1dc4feb450a2a3300ef2a9`,
  inspected 2026-11-11; `skills/animate/SKILL.md`.
- **Changed/derived file:** `references/layout-motion-inspiration.md`
  contains an original scoped adaptation of motion-purpose/frequency
  decisions, existing-token reuse, economical tool selection, timing and
  easing, interruption, exit, reduced motion and hover gating.
- **Scope adjustments:** preserves this generator's approved gesture and
  keyboard equivalents, existing runtime, brand motion rules and factual
  evidence. Timing ranges are starting points, not universal bans or
  claims that CSS/transform animation is always hardware accelerated.
  Does not copy the upstream startup response, component-library skill
  dependency or recipe collection.

Copyright (c) 2026 Emil Kowalski. Licensed under MIT; the complete licence
is included in `licenses/emil-kowalski/MIT.txt`. No endorsement is implied.
Pinned source:
https://github.com/emilkowalski/skills/blob/715c1807e08c497cfd1dc4feb450a2a3300ef2a9/skills/animate/SKILL.md .

## Linked inspiration only - Codrops Creative Hub and React Bits

- **Codrops Creative Hub:** https://tympanus.net/codrops/hub/ .
  Links to demos by different creators. Check each selected project's
  terms; the hub does not grant blanket rights to linked code or assets.
- **React Bits:** https://reactbits.dev/ ,
  https://github.com/DavidHDev/react-bits . The repository's `LICENSE.md`,
  checked 2026-11-11, uses MIT plus a Commons Clause condition restricting
  redistribution of components, ports, tools and standalone exports.
  Do not describe it as unrestricted MIT.
- No Codrops or React Bits source code, media, component collection or
  tools are bundled here. `references/layout-motion-inspiration.md`
  supplies original reference-selection and offline-delivery instructions.
  Actual reuse in a generated experience requires checking the selected
  version's applicable terms and preserving its notices.

## Before external or customer-facing distribution
The subsequent actual-assets implementation clarification requires official
asset files to be used in the built page after plan approval, rather than
only prioritised in research. It distinguishes plan/style approval from
explicit object-specific substitution approval.

The 2026-11-04 official-first revision adds original generator instructions
prioritising actual official products/assets before construction and
requiring approved, disclosed fallbacks. It does not change the bundled
third-party licences or imply additional asset/trademark permissions.

Facts, logos, and brand imagery used inside any generated experience come
from the target company's own official sources, not from this package.
Confirm logo/trademark usage and licensing terms with your own legal or
brand team before showing a generated experience outside your organization
— this package does not grant or verify those rights.

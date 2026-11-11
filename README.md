# interactive-experience-generator

Turn a company's verified story into a full-screen interactive experience.
Deliver one offline HTML file with English/Dutch, sources, and a download button.
Experiences are based only on publicly available resources, not private or
internal material.

Every experience includes this visible disclaimer (with a Dutch equivalent):

> This experience is generated entirely with Microsoft Copilot Cowork based on publicly available resources and for demonstration purposes only.

## Install

This repository is public; no GitHub sign-in is required to download the skill.

**Cowork:** Open
[`dist/interactive-experience-generator.skill`](dist/interactive-experience-generator.skill)
and choose **Download raw file**. Import the file into Cowork. Re-import after
updates.

**Other agents:** Copy `SKILL.md`, `references/`, `NOTICE.md`, and `licenses/`
into an `interactive-experience-generator` folder in your agent's skill
location. Keep the directory structure; `SKILL.md` alone is not enough.

## What it does

- Research official sources and connect the company message to visitor actions.
- Keep approved concepts while resolving subject-specific composition,
  scale, materials/light, typography, motion and control placement.
- Default showcases to scene-led, official-imagery/model-led composition
  rather than enclosing the whole experience in a card. Be bold when useful,
  not experimental by default; keep task tools practical.
- Keep supporting artwork restrained. Build visual richness through
  asset scale, framing, layering, depth and brand typography, not clutter.
- Prove the actual visual treatment in the existing concept preview at its
  intended scale and placement. No extra concept or approval round.
- Design the main action before choosing widgets: before/during/after
  feedback, interruption, recovery, and equivalent keyboard/touch access.
- Prove one representative scene before expanding: meaningful action,
  visual character and interaction feel are inspected separately. Camera
  rotation alone suits only an approved inspection viewer.
- Place the company promise and current benefit in the scene without covering
  gestures or forms.
- Use actual permitted logos, photos, packaging, and models, not drawn lookalikes.
- Download assets through available tools, curl/Python, or a browser; check the
  files and embed them for offline use.
- Report the exact download error or missing capability before asking for files.
- Preserve approved choices during revisions, including genuine visitor input.
- Carry forward supplied project authorization; ask only about specific gaps,
  conflicting terms, or uses outside the approved scope.
- Reuse a current preview and repeatable build/export checks. Review the opening,
  interaction, and takeaway separately from technical test counts.
- Compare layout, navigation, controls and feedback with supplied examples
  or available design history. Retain useful conventions with a reason,
  not novelty quotas or blanket bans on cards, sliders or buttons.
- Include bundled Impeccable-adapted surface modes, visual direction,
  motion, critique and polish. No separate install, launcher or runtime.
- Apply Impeccable layout/animate and Emil Kowalski's animation guidance:
  clear grouping and hierarchy, responsive order, purposeful timing,
  interruptible feedback, touch/keyboard access and reduced motion.
- Use Codrops Creative Hub and React Bits selectively for interaction
  inspiration, not as required services or copied component packs.
  Check selected-project terms before code reuse; React Bits' current
  licence is MIT plus a restrictive Commons Clause condition.

The Impeccable integration is an attributed, scoped adaptation, not the
full upstream skill or its command suite. It runs as guidance within this
generator's normal workflow. Visual craft starts before expansion rather
than being deferred to a final cosmetic pass.

For revisions such as "the concept is good but it looks generic" or "all
the interactions feel the same", repair the requested execution axis.
Preserve the concept, official assets and frozen behavior; do not restart
intake or silently redesign approved work.

The skill cannot grant network access or reuse rights. Missing required assets
block completion unless you approve a specific substitute. Plan approval alone
does not permit substitutions; existing approved exceptions remain valid.

## Package

The `.skill` file is a ZIP containing 15 files under
`interactive-experience-generator/`. Package only `SKILL.md`, `references/`,
`NOTICE.md`, and `licenses/`. Exclude README, evaluations, generated experiences,
and local artifacts. Compare archive contents with source and update this
SHA-256 after rebuilding:

```text
56bbe3399c6a55329666caec064cb6853b04703d735d7d71633ffce312b6eb7e
```

[`evals/evals.json`](evals/evals.json) contains 29 evaluation prompts; `evals/files/`
contains a fictional SVG fixture. These stay outside the package. Their presence
does not prove they passed or that Cowork downloads were tested.
The execution probes cover visual staging, interaction choreography,
representative-scene evidence, familiar task controls, standalone
Impeccable integration and honest comparison/feedback limits. Text-only
answers cannot establish improved rendered quality or interaction feel.
Additional art-direction probes cover official-imagery dominance, useful
unboxed composition, restrained supporting art and actual-treatment previews.
Layout/motion probes cover grouping, responsive focus order, interruption,
reduced motion and optional reference/licensing/offline boundaries.

Keep [`NOTICE.md`](NOTICE.md) and [`licenses/`](licenses/) with redistributed
copies for attribution and license terms.

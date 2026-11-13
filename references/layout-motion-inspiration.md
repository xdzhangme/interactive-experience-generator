# Layout, motion and interaction inspiration

Read during concept composition, selected-concept implementation and
layout/motion revisions (steps 5-8). This bundles scoped, original
adaptations of Impeccable layout/animate and Emil Kowalski's animation
guidance. See `NOTICE.md` for pinned sources and bundled licences.
Codrops Creative Hub, React Bits, MotionSites and Recent.design are optional live references, not
required installations, copied component collections or runtime services.
Use `pattern-library/INDEX.md` and `pattern-library/patterns.json` for
stored examples before optional live study. Their original analyses
retain source dates, evidence limits, appropriate uses and accessible
offline adaptations; source descriptions are not rendered observations.
Follow the guidance-role and concept/build/review handoffs in
`pattern-library/INDEX.md`. Apply these layout and motion principles
while developing all four options, revisit them for the selected working
scene, and compare their accepted adaptations during critique. They
supplement the generator's own guides rather than replace them.

The approved message, identity, medium, gesture and selected composition
take priority. These techniques improve how that experience communicates;
they do not authorise a new concept, drawn branded substitutes, extra
approval rounds or a conventional landing-page template.

## Layout: make priority visible

Before moving elements, identify the structural problem in the existing
preview or rendered state. Add a short spatial thesis to the existing
execution direction contract, not another document:

- What leads, what supports, and in what order should the eye travel?
- Which object, action, consequence and explanation belong together?
- Where should density be high for useful work and low for attention?
- How will those relationships reflow on a phone, at zoom and in Dutch?

Use proximity before containers. Group related controls and explanations
tightly, then leave more space between different purposes. Use a small
semantic spacing scale, usually with 4 CSS px increments as a starting
point, rather than unrelated offsets or the same padding everywhere.
Let established project tokens win over a newly imposed scale.

Use Grid for two-dimensional relationships and Flexbox for a row or column;
use `gap` for sibling rhythm. Keep reading content in normal flow.
Position spatial scene elements when necessary, checking their actual
transformed bounds. A panel should earn its space through reading or task
needs, not compensate for weak grouping.

Give the authentic hero, main action and associated explanation clear
priority over utilities. Retain reachable Sources, language, download and
recovery controls. A scene-led showcase may be asymmetric; an operating
surface can retain stable forms, grids and familiar controls. Neither is
an excuse to hide useful content or impose a universal composition.

Adapt structure, not merely scale: reflow, wrap or reorganise the scene
while preserving the object/action/explanation relationship. Keep DOM,
reading and keyboard focus order consistent with the meaningful visual
order. Preserve in-progress input through layout and locale changes.

Inspect the opening, meaningful intermediate state, completion and
overlays at the existing delivery widths. Include long Dutch labels,
empty/error states where applicable, safe areas and zoom. Squint or blur
the view: can the primary element and major groups still be distinguished?
Pair that judgment with bounds/overlap checks. No overflow does not prove
good hierarchy, and an attractive screenshot does not prove usable focus.

## Motion: decide the job before the curve

Combine Impeccable's purpose-led motion assessment with Emil's ordered
implementation decisions:

1. Decide whether motion helps at all. Frequent/repeated utilities should
   be immediate or very subtle; reserve authored spectacle for an earned
   story moment. Do not animate readable evidence just to make it move.
2. Name its job: input feedback, state indication, spatial continuity,
   explanation or a rare purposeful delight. If none applies, leave it still.
3. Use the cheapest suitable facility already available: CSS transitions
   for state/press/hover; bounded keyframes for predetermined sequences;
   Web Animations API or the existing runtime for dynamic sequencing.
   Add no library merely for a fade.
4. Choose properties, timing and easing, then specify interruption, exit
   and reduced-motion behavior before polishing.

Record focal moment, continuity, feedback and expensive-effect budget in
the existing choreography. One sequence may lead; routine controls should
not wait for it. No animation may gate access to the meaningful action or
delay the visitor's input acknowledgment.

### Practical motion ingredients

Treat these as starting ranges to inspect, not mandated durations or a
new parallel token system. Reuse existing motion tokens and approved brand
motion rules. Directly manipulated position/angle follows input rather than
receiving a decorative transition that makes the object lag behind.

| Purpose | Starting treatment |
|---|---|
| Press or immediate feedback | About 100-160 ms, or instantaneous for frequent actions. |
| Routine state/control transition | About 150-250 ms; ordinarily stay below 300 ms. |
| Larger overlay or spatial transition | About 200-500 ms when the distance and continuity justify it. |
| Rare focal sequence | About 500-800 ms if earned; input stays available. |

Use deceleration for arriving UI, smooth acceleration/deceleration for
on-screen movement, and linear motion only for a constant-rate meaning.
One available UI ease-out starting point from Emil is
`cubic-bezier(0.23, 1, 0.32, 1)`; prefer the project's existing suitable
curve rather than multiplying nearly identical tokens. Avoid slow-starting
UI feedback and reflexive bounce. Springs suit interruptible, playful
settling when useful, not every control or factual claims of real physics.
An exit normally preserves its entry's spatial relationship and may be faster.

Prefer transforms and opacity where they express the state. Name exact
transition properties rather than `transition: all`. Avoid layout-heavy
animation where a transform works; masks, clipping or bounded shader work
may serve an approved reveal, but inspect their actual cost. Do not assume
every transform is composited or every CSS animation is inexpensive.
Anchor popover motion to its trigger without scaling readable content
from nothing. Use normal accessible dialog/focus behavior, not a bespoke
animated shell that loses keyboard control.

Retarget rapid transitions from their current visual state; do not restart
a canned sequence from zero on every input. Keep one authoritative object
state so repeat input, reversal, pointer release/cancel, locale change and
reset reconcile the visual and semantic result. Bound spring settling and
expensive effects; stop nonessential loops when hidden or offscreen.

Gate hover-only embellishments with `(hover: hover) and (pointer: fine)`;
essential information and actions remain available by touch and keyboard.
Honor `prefers-reduced-motion` with less travel, parallax, distortion and
looping while retaining the complete state, explanation and confirmation.
Keyboard equivalents still control meaningful state; restrained motion is
not permission to remove accessible operation.

Exercise interruption, rapid repeat input, reversal, reset, keyboard,
touch and reduced motion in the representative scene. Inspect target
viewports/devices for responsiveness; measure if claiming a frame rate.
Slowed playback can reveal discontinuities but is not performance evidence.
Report missing browser/device observations as unverified, not smoothness
inferred from source.

## Optional inspiration: study a mechanism, not a whole skin

| Source | Look for | Translate into this generator |
|---|---|---|
| [Codrops Creative Hub](https://tympanus.net/codrops/hub/) | Creative coding demos, composition, transitions, direct manipulation and unusual reveals. Follow a useful entry's demo and tutorial/code links. | Extract a specific input-to-response or spatial principle only when it serves the approved subject and company message. |
| [React Bits](https://reactbits.dev/) | Text treatments, backgrounds, components and micro-interactions, with live demos and component source. | Prefer an earned response or supporting cue; do not let an animated background or text effect become the company story. |
| [MotionSites](https://motionsites.org/) | Layout-and-motion directions, website prompts and animated examples; start with relevant public catalogue entries. | Extract hierarchy, spatial continuity and input/response principles, not a whole website template or source prompt. Preserve the approved experience rather than turning it into a landing page. |
| [Recent.design](https://recent.design/) | Composition, typography, art direction and visual references, with creator/source links. | Extract type roles, focal/supporting balance and imagery relationships under the target brand. A poster or curator description does not establish working input, motion or responsive behavior. |
| [Details.so](https://www.details.so/inspo) | Optional manual study of production-site navigation, buttons, scroll effects, section transitions and micro-interactions. | Follow the manual-only boundary below. For an individual project, use permitted study to inform original decisions through concept, build and review; never treat it as an offline-library or automated-research source. |

Use the same concept/build/review handoff for the four library sources. Static
references can improve composition without providing an interaction:
record "no interactive input/motion documented" rather than inventing one.
For Recent.design, retain the exact item and creator/source attribution;
follow the creator link when accessible and useful. Distinguish the
curator's description from a creator statement or inspected live site.
For MotionSites, public catalogue metadata may be the only readable
evidence; say so. Do not fetch locked prompts or require an account.

### Details.so: manual project reference, not a library source

The public inspiration page and terms were checked 2026-11-13:
https://www.details.so/legal/terms . The terms prohibit scraping, crawling,
indexing, harvesting and mass downloads outside expressly provided
functionality. They also prohibit using the service to build, train,
evaluate or enrich competing libraries, datasets, models or design
inspiration databases, and restrict standalone Vault redistribution.

Keep Details.so as an optional link for the person's manual, individual
project study under applicable terms, not an instruction for automated
agent browsing. Do not ingest its listings, captures, metadata, snippets,
prompts or derived example records into this skill, evaluations or offline
library. Exclude it from scheduled refreshes even if an entry is public.
Do not bypass account/payment controls or require a subscription.

When permitted manual study informs a specific project, carry the person's
design decision into concept composition, original implementation and
observed review, just as with other references. Retain at most the link
and project-specific decision in that project's existing notes, not a
reusable extraction of the source. A capture does not establish live
input, accessibility, timing or performance; verify the generated result
independently. Do not relabel Details-derived records as another source
to evade these restrictions. Without appropriate permission, use the
existing 50 stored examples and bundled guidance instead. Any later
library integration requires explicit permission covering that use.

### Live study of library sources

During ideation, inspect a small relevant sample when live access is
available for the four library sources above, not Details.so. Stop when a
useful principle is found; do not browse a whole
catalogue or force a reference into every concept. During a narrow revision,
skip browsing when the approved preview and requested correction suffice.
Without browsing, retrieve and map relevant stored patterns instead of
falling back to generic rules alone. Cite their IDs and recorded dates
in the existing concept notes. Library knowledge does not supply missing
official company evidence, assets, permissions or visual/input validation.

Record a compact inspiration note in the existing concept/execution record:
exact demo URL and access date, observed input and response, useful
principle, its company-message fit, and what will deliberately not be copied.
Preserve any specific reference supplied by the person. Distinguish a
rendered observation from a site's description: reading text or seeing a
poster does not establish timing, interruption or interaction feel.
Use a live browser or recording when available to inspect those behaviors.

When browsing is unavailable or a demo fails, use the bundled guidance and
say which reference behavior could not be inspected. This is not a blocker
for an otherwise supported build and does not erase existing official
company research. Never invent a demo observation or require a paid account.
Design-inspiration sites are not evidence for company/product claims and
do not replace official sources or assets.

### Reuse, framework and offline boundaries

MotionSites' terms checked 2026-11-13 restrict standalone redistribution
of source prompts/protected materials and bypassing access controls or
bulk-exporting protected content. A free listing is not a redistribution
licence. Recent.design showcases independently owned work; no blanket
code, font, image or artwork reuse permission was established. Store only
original analytical descriptions and attribution links, not prompts,
Design.md files, screenshots, videos, fonts, artwork or template/code packs.
If access or rights are unclear, use the stored general principle or an
original solution, not a purchase, bypass or copied brand treatment.

Linking to inspiration is not permission to copy code, imagery or audio.
Check the exact demo/component repository and applicable terms before
reuse, preserving required notices. Codrops Hub links to different authors;
its catalogue does not grant one licence over all linked projects.

React Bits' checked repository licence is MIT plus a Commons Clause
condition, not unrestricted MIT. It permits use as part of applications,
websites or products but restricts redistributing the components, ports,
tools or standalone exports themselves, including bundles. No React Bits
code, assets or component pack ships with this skill. Recheck the selected
version's terms before any generated-page reuse; unresolved conflicts
require an original implementation of the general principle or a targeted
permission decision, not a copied component renamed as original.

Do not turn this HTML workflow into a React project just because an example
uses React. Prefer a small original implementation in the approved runtime
when appropriate. Where permitted component reuse genuinely helps, adapt
or build it with all necessary dependencies embedded in the final HTML and
retain its notices. A React snippet, remote import, iframe or link to a
hosted demo is not the finished standalone experience.

Verify the actual downloaded file in its declared mode. The online version
may load official company assets, not component demos, from recorded URLs.
For explicitly requested offline export, verify with networking disabled;
no essential action, font, asset or script may depend on external sites.
Inspiration links may remain optional citations. Keep the four acceptance gates and
the separate visual-character/interaction-feel evidence unchanged.

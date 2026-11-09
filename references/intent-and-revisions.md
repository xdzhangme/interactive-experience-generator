# Intent, object truth and complete revisions

Use this contract in the existing brief or session record. Its purpose is
to stop forgotten decisions and disconnected patches, not create more
documents, interviews or approvals.

## Retain decisions before changing anything

Recover the latest accepted artifact and explicit corrections. Distinguish:

- **Confirmed:** what the person actually requested or approved.
- **Proposed:** your recommendation, not yet their decision.
- **Unresolved:** only uncertainty consequential enough to ask about.
- **Frozen:** approved objects, assets, behavior or direction outside this
  revision. A later explicit correction supersedes the earlier decision.

Record a short revision delta: change X; preserve Y; inspect affected Z.
Do not reopen a frozen hero because a nearby stamp, label, caption or
input control needs correction. If changing Y is genuinely necessary,
explain the dependency and seek a targeted decision. Do not silently drop
requirements to simplify the build.

Reuse already approved subjects, rights scope, concepts and mockups. A
concrete correction is not a request for four new concepts. Once the person
clarifies an ambiguity, implement that meaning rather than keep searching.

Treat "there is no interactive experience" as a behavior diagnosis:
recheck the representative-scene/core-loop gate in `build-and-delivery.md`, not merely the
presence of a canvas, buttons or animation. Treat an in-scene/floating
message correction as a composition change using `message-and-brand.md`,
not just additional copy below the existing experience. Preserve the
approved identity and medium while repairing the reported axis.

Treat "the concept is good but the visual execution is weak" as a staging
revision, not a request for new concepts. Recover the direction contract
and inspect composition, subject scale, materials/light, typography and
interface prominence. Treat "all interactions feel the same" as an
execution diagnosis: compare targets, before/during/after feedback,
navigation and recovery, not just control names.

Record what may change and what stays frozen for each axis. A request to
change interaction execution can justify replacing incidental widgets,
but not a specifically approved gesture without agreement. A request to
improve visuals can change unpinned staging, but not remove real assets,
claims, content or accessibility paths. Use the representative-scene gate
on the affected action before propagating the repair; no extra concept
tournament or blanket approval round is needed.

## Describe each important object along three independent axes

For real-company implementation after plan approval, the identity contract
includes the actual official asset file and where it renders in the page.
An official drawing reference followed by an agent-authored substitute
does not satisfy that contract. A plan or style approval does not grant
an object-specific substitution exception.

| Axis | Record | Evidence |
|---|---|---|
| Identity and provenance | Exact offering/variant, official or authorised source, reuse scope, illustrative substitutions. | Inspected reference and permitted asset, not a logo on a generic prop. |
| Rendering medium | Photo, SVG/illustration, spatial mesh, or an explicitly mixed scene. | Actual rendered medium; a flat image or CSS rotation is not spatial 3D. |
| Behavior and agency | What the visitor controls, resulting state, feedback and accessible equivalents. | Exercised input and state change, not merely an animation starting. |

Interpret "real" from context. An actual product image can be the correct
stamp while a drawn signature needs real visitor input, not a model of a
signing device. When unclear, ask one focused question about the ambiguous
object; do not launch an open-ended model hunt or replace approved objects.
Choose the simplest medium satisfying the confirmed contract.

For genuine spatial 3D, inspect scene geometry, depth/camera behavior and
the requested object interaction in the renderer. A canvas element or an
imported library alone proves none of these. Follow `threejs-craft.md`;
do not force its pipeline onto flat assets or drawing controls.

Keep physical/service steps truthful across routes. A service requiring
staff handover should not inherit a self-service slot because that UI
already exists. An official photo may depict a different transaction;
disclose the actual depiction and any illustrative overlay. Do not turn
an expired product, invalid label or unrelated photo into current evidence.
If a demo substitute is necessary, obtain agreement, label it visibly and
in Sources, and do not imply official validity.

## Genuine authored input

When visitors draw, sign or compose, use their actual input. Different
strokes/text/configurations should produce correspondingly different
results; a preset path, progress gesture or confirmation button alone is
not the requested authorship.

For drawing/signing, support pointer and touch plus an accessible
alternative appropriate to the approved requirement. Provide clear
instructions, correction (such as Undo/Clear) and explicit confirmation.
Reject accidental empty/tap-only completion when meaningful ink is
required. Preserve in-progress input across language/layout changes;
define reset behavior and avoid silently confirming it.

Treat signatures and similar personal input as sensitive. Default to local
ephemeral state, no upload, analytics payload, persistent storage or
inclusion in Download HTML. Clear it on explicit reset and a fresh session.
Verify the actual downloaded file starts without another visitor's input.
If persistence is explicitly requested, resolve consent, purpose and data
handling before implementing it. A demonstration signature is not evidence
of a legally valid signing process.

## Trace the change through a small route-state matrix

List relevant routes and states before editing, using only existing
surfaces. For example:

| Route | Preparation | Applied/completed | Handover/interaction | Ending/replay |
|---|---|---|---|---|
| Self-service | Correct product asset and cue | Applied asset; original token no longer intercepts input | Correct self-service target | Consistent message and reset |
| Staff-assisted | Correct label and cue | Same label on the carried object | Correct staffed target, not a copied slot | Consistent proof/receipt and reset |

This is an example, not a prescribed mail-service story. Adapt the rows
to the actual experience. Include all affected copies: draggable token,
applied object, texture, thumbnail, alternate/fallback view, caption,
accessible label, Sources, both languages and downloaded initial state.
Share asset/state definitions where practical so they cannot drift.

For a reported defect, capture its failing state before fixing it when
possible. Verify the exact outcome afterward: the correct image is
visible, an applied token is actually hidden/non-intercepting, the right
route target appears, or unique strokes reach the ink layer. DOM presence,
an enabled button and aggregate test counts are not substitutes.

Replay the changed route and relevant unaffected route(s), including
switching routes, revisiting, reset and language changes. Confirm overlays
and retired controls do not intercept taps or focus. When a focused action
disappears, move focus to a sensible visible destination. Preserve frozen
assets/geometry; use an asset/source comparison where useful, not a claim
that unchanged bytes prove the whole scene still works.

## Separate the evidence

For each material requirement, record the observable outcome, inspected
route/state, input/locale/viewport and evidence or limitation. Keep technical
operation, visual craft, interaction fidelity and message/brand judgment
distinct. The four delivery gates in `build-and-delivery.md` remain intact;
visual findings are not a fifth score that can average away a failure.

Perform targeted regression checks first, then the relevant full journey
after a coherent batch of fixes. Keep prior accepted deliverables intact,
write a new output version, and export from understandable editable source.
Do not accumulate brittle generated-file patches as the permanent source.
Do not claim an audience understood the message, a browser was inspected,
or a device/accessibility audit passed unless that work actually happened.

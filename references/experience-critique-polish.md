# Experience, critique and polish

Original, scoped adaptation of selected guidance from Impeccable 4.8.0
(`pbakaus/impeccable`, tag `cli-v4.8.0`): its Experience mode and web
critique/polish principles. See `NOTICE.md` and `licenses/impeccable/`.
This is not the full Impeccable runner or command workflow.
Read this bundled guidance during normal builds and revisions; do not wait
for a separate request to "use Impeccable." Its original scoped adaptation
is extended here with the generator's own revision and usability rules.

## Boundaries and priority

The approved company message, actual identity, factual evidence and user
scope govern visual decisions. Quality refinement helps communicate them;
it cannot substitute for them or overrule their acceptance gates.

Keep the priority: company meaning -> authentic identity -> meaningful,
usable interaction -> visual refinement. Preserve the selected scene,
gesture, complete requested range, EN/NL, Sources, Download HTML and
offline delivery. Do not invent a new aesthetic, rewrite claims or remove
products to make the screen look cleaner.

This file is usable without Impeccable installed. Do not run or install its
launcher, detector, hooks, live server, catalogue randomiser or other
commands as a requirement of this generator. No agent fan-out, external
image service, extra planning files or runtime dependencies are introduced.
The native-platform playbooks are not part of this adaptation.

## Experience-led composition

For a showcase, make the visitor feel present with the real offering from
the first viewport, rather than looking at a conventional marketing page
with a small demonstration embedded in it.

- Give the hero, purposeful action and company promise clear hierarchy.
  Keep the visible interaction cue understandable without a tutorial wall.
- Let utility controls recede in visual weight without hiding language,
  Sources, download, accessibility or the next meaningful action.
- Place the explanation where the visitor can see the relevant object
  and consequence together. A phone layout should reorganise that
  relationship, not merely shrink it or send the message below the action.
- Give a complete catalogue a discoverable exploration layer without
  letting equally weighted cards drown out the main story.
- Use the approved materials, imagery, typography and palette consistently.
  Respect real brand fonts and their rights; embed permitted fonts or use
  a disclosed local fallback, never a runtime CDN dependency.
- Make motion respond to action or clarify a transition. Keep it
  interruptible and provide reduced-motion equivalents; do not add effects
  simply to make the polish visible.

Choose emphasis from the requested surface, not the industry. If the
approved brief is task/training-led, keep familiar, readable task controls
and clear state feedback. Do not hide useful controls to force a dramatic
showcase treatment.

## Critique before polishing

Start with a **cold-start review**: open the experience in its fresh state
and judge it from the visible cues rather than the implementation brief.
Identify the first meaningful action, perform it, inspect the object/task
change and associated benefit, then follow the path to its company
takeaway. Use an uninstructed reviewer when one is available; otherwise
label this an agent self-review, not independent audience evidence.

If the approved task promises operating an offering but the visitor can
only rotate its model, or if the company story becomes clear only after
reading a detached explanation, repair that experience gap before cosmetic
polish. Apply the core-loop gate in `build-and-delivery.md` and the spatial
message checks in `message-and-brand.md`. A successful technical run is
not a reason to postpone this review until after delivery.

Inspect the actual rendered opening, a meaningful intermediate state,
recovery/replay and ending. Include representative desktop, phone and any
important intermediate widths, using both EN and NL where copy expands.
Record viewport, state and screenshot reference for each visual finding.
If suitable visual tooling is unavailable, state that limitation; markup
inspection is not a completed visual critique.

First form a visual/communication judgment, then consult mechanical QA:

1. **Specificity and meaning:** does this look and behave like this
   company's offering? Can the intended promise be inferred from what is
   experienced? Keep the message review in `message-and-brand.md`.
2. **Hierarchy and clarity:** does the eye find the object, the action and
   its relevant explanation before utility chrome or decoration?
3. **Interaction and cognitive load:** are controls discoverable, state
   changes evident and recovery possible? Remove unexplained choices and
   precision that does not serve the approved goal.
4. **Composition and craft:** examine spacing, alignment, type roles,
   imagery proportions, materials, lighting and motion as one coherent
   scene. Check the real asset renders, not just its URL.
5. **Responsive and accessible use:** inspect touch targets, text wrapping,
   contrast, keyboard focus/order, labels, zoom and reduced motion.
   A no-overflow result alone does not establish a good phone experience.

Functional tests, linters or an optional detector can provide defect
evidence. A clean result is not proof of good design, brand authenticity
or company-message delivery. This adapted critique is not a claim that
Impeccable's full detector, dual-agent assessment or scoring system ran.

## Prioritise findings

Tie each finding to an observed state and a narrow correction:

- **Must fix:** a wrong/absent company message or identity, a blocked or
  misleading action, an inaccessible path, missing required content, or
  broken offline delivery.
- **Should fix:** unclear hierarchy, excessive interaction effort, text
  collisions, weak phone composition, inconsistent states, awkward
  localisation, or a rendering/performance problem.
- **Could improve:** spacing, typography, material or motion refinements
  that preserve a working, understandable experience.

Retain two or three strengths so refinement does not destroy what works.
Do not use a numeric design score to average away any failed acceptance
gate. State unverified observations and reviewer limitations explicitly.

## Polish without concealed redesign

Fix the narrowest cause, in priority order, then inspect the batch:

- Reuse a small coherent set of inline tokens for same-role spacing,
  typography, colour, radii and motion instead of scattered exceptions.
  Do not introduce a framework or new design-system project for one file.
- Correct optical alignment, text measure and line wrapping, including long
  product names, Dutch expansion, source labels and completion states.
- Preserve official asset proportions and real brand colours. Do not
  replace an authentic asset with a convenient generic illustration.
- Keep gestures, keyboard equivalents, state transitions and visible
  feedback consistent. Retain all exact catalogue identities and source
  relationships while simplifying their presentation.
- Refine authored forms and material/light relationships before effects.
  Do not hide weak geometry with glow or excessive animation.
- Do not add a theme toggle, dark palette, new claim, action, product,
  sales call to action or visual world just because a general design
  playbook recommends one.

If the approved concept cannot carry the message, report the conceptual
problem and seek a targeted direction change. Do not disguise a replacement
concept as a polish pass.

## Concrete web craft checks

Treat these as starting targets, not a substitute for inspecting the actual
scene. Respect approved brand typography and justified accessibility needs.

- Aim for at least 16 CSS px for body/instructions and 12 px for secondary
  captions; do not shrink essential text to hide a collision. Check actual
  readability, wrapping and hierarchy, not just computed size.
- Use at least 44 by 44 CSS px for interactive hit areas and 48 px height
  for primary actions where practical. Include compact language, chapter,
  camera, reset and dialog controls, not only the main button.
- Check ordinary text against WCAG AA contrast (4.5:1; 3:1 for qualifying
  large text), plus visible focus and required control boundaries. Measure
  the actual background/composite state; a static selector warning alone
  is neither a failure nor a pass.
- Prefer normal flow, grid/flex and adequate scene height for explanatory
  copy, object, caption and action. Recompose at tablet/phone widths rather
  than pile on absolute offsets or smaller fonts. Spatial elements may
  need positioning; verify their transformed/rotated screen bounds.
- Inspect not only overflow but overlaps, click interception, cropped
  addresses/labels, footer disclosures and controls hidden by overlays.
  Exercise dialogs, completion and input states, not just the opening.
- Use one coherent set of semantic tokens for type, spacing, action colour,
  focus and target size. Resolve undefined variables and inconsistent
  overrides rather than masking them with another exception.
- Preserve in-progress input through responsive/localisation changes.
  Give stage changes a sensible heading/focus destination and avoid
  stranding focus on a removed control. Keep keyboard and reduced-motion
  equivalents; no gratuitous entrance animation is needed to show polish.

Normally inspect desktop, an intermediate/tablet layout and a narrow phone
in both EN/NL, plus the narrowest supported width. Useful starting widths
are 1280, 768, 375 and 320 CSS px, adapted to the real brief. Record viewport
height too. Inspect zoom when possible and label it unverified otherwise.
Compare matching before/after route-states so an unrelated attractive
screenshot cannot stand in for the corrected defect.

## Verify the whole path again

Replay the core action and recovery with applicable pointer, touch and
keyboard inputs. Recheck the rendered states at the delivery widths,
EN/NL switching, required controls, asset loading, runtime errors and
the downloaded file's offline operation. For spatial scenes, use actual
renderer/performance observations rather than assuming a clean screenshot
proves responsiveness.

Compare the revised result against the approved concept and the recorded
findings. Report separately what was fixed, what was observed and what is
still unverified. Leave the generator's four independent acceptance gates
intact; visual polish is never permission to mark a blocked brand/message
gate passed.
Use the affected route-state matrix in `intent-and-revisions.md` and replay
relevant unaffected branches too. A detector can locate candidates, not
certify visual quality, privacy, authentic assets or completed interaction.

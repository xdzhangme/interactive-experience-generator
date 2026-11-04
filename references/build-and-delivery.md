# Build and delivery

## The single file
Everything — markup, styles, scripts, and any embedded assets — lives in one
offline-capable HTML file. No runtime CDN script tags, no remote font or
texture fetches. Inline or embed every dependency the experience needs to
run.

Keep editable source separate from generated output when complexity
warrants it, with a reproducible export into the one HTML deliverable.
Prefer shared assets, explicit state and coherent styles over a chain of
fragile string replacements or repeated CSS overrides. This is a source
quality rule, not permission to deliver a folder instead of the required
single file. Preserve earlier accepted files when publishing a revision.

**Completion gate, not a formality:** before calling the build done, verify
it loads and runs with the network disconnected (or by equivalent means
available this session). If that verification isn't possible — for example,
only a hosted managed-runtime app can be produced — say so plainly at
delivery. Never substitute a non-portable result without saying so.

## Required elements
- The full-screen interactive experience itself.
- A complete EN/NL language switch covering every piece of copy, not a
  partial translation.
- A **Sources** button opening the sources panel described in
  `sources-and-labeling.md` (citations, illustrative disclosures, or the
  "No research performed" label).
- A **Download HTML** action that saves the complete, working file.

## The inspection and revision loop
Adapted in spirit from Anthropic's `webapp-testing` skill
(github.com/anthropics/skills, Apache-2.0) — see `NOTICE.md`. Where a real
browser or screenshot tool is available this session, use it: load the
build, take a screenshot, and read it against the selected mockup and the
art-direction brief. Where no such tool is available, carefully read the
rendered HTML structure and preview pane instead of assuming the markup is
correct because it compiles.
Reading markup is a static review, not evidence that the scene renders,
that a gesture works, or that the object is recognizable. Record those
checks as unverified if no suitable inspection tool is available.

Either way, this is a real check against the chosen concept's mockup and the
art-direction brief — fix what's weak (clutter, flat lighting, inconsistent
type, a motion effect that doesn't answer any action) before moving on.

Apply the scoped Impeccable-inspired loop in
`references/experience-critique-polish.md`: form a rendered
visual/communication judgment, consult functional evidence, prioritise
must/should/could fixes, polish without changing the approved direction,
then replay the whole path. This adaptation does not require the upstream
CLI, detector, hooks, servers or dual-agent workflow. Do not claim those ran.

## Final checklist, before delivery
Use four independent acceptance gates. For each check record pass, fail,
or unverified and the evidence (reference comparison, observed interaction,
reviewer observation or test result). Do not combine them into one score:
technical success, catalogue coverage and interaction checks cannot
compensate for failed branding or communication. Mark inapplicable checks explicitly
with the reason rather than counting them as passes.

### Brand authenticity
- [ ] After plan approval, actual official model/image/asset files were
      embedded/imported and visibly used for primary and secondary branded
      objects in the delivered page, including affected interaction states.
      A source link, unused asset, or agent-drawn lookalike based on an
      official reference does not pass. Any substitute has explicit
      object-specific approval; general concept/style approval is not enough.
      Record each file's provenance, permission and rendered location.
- [ ] Actual company logo and real products/services are recognisable in
      the delivered view, not only in source links, unless explicitly
      excluded by the brief. Typed lettering and generic props do not
      stand in for official assets.
- [ ] Embedded brand assets have verified provenance and applicable reuse
      permission. Supplied authorisation scope and remaining limits are
      recorded, not expanded into a blanket public licence.
- [ ] The real hero was visually compared with inspected official
      references; identifying form, markings and official-versus-
      illustrative status are clear.
- [ ] Approval of an illustrative style or an unbranded prototype has not
      been counted as authentic branded delivery.

### Company-message delivery
- [ ] The approved one-sentence message is understandable from the actual
      opening, consequential interaction moments and ending.
- [ ] Each main action has an observable consequence that demonstrates a
      source-backed company benefit/approach; unrelated facts after
      gestures do not count as evidence.
- [ ] Actual offerings and relevant proof make the story specific to this
      company without inventing exclusivity, superior outcomes or claims.
- [ ] The visitor can understand the main story without completing a
      catalogue quota; all requested range entries remain discoverable.
- [ ] The ending connects the actions to the company takeaway, rather than
      saying only "complete" or celebrating a visited-item count.
- [ ] Message review follows `references/message-and-brand.md`. Record
      what a brief-naive reviewer inferred when available. Clearly label
      author/agent review and unobserved human comprehension; functional
      pass counts are not evidence that an audience understood the company.

### Interaction and intent fidelity
- [ ] The revision delta and frozen approvals from
      `references/intent-and-revisions.md` were preserved. Identity,
      rendering medium and behavior match each important object's contract.
- [ ] Every affected route/state copy uses the correct asset and target,
      including applied/hidden states, alternate views, accessible labels,
      textures, both languages, Sources and export. Unaffected relevant
      branches were replayed, not assumed safe from one screenshot.
- [ ] Authored input comes from the actual visitor, with correction and
      confirmation where applicable; empty/preset completion is not
      substituted. Personal input is ephemeral by default and absent from
      the downloaded fresh copy.
- [ ] Confirmed company, exact product/variant, subject, scene, medium,
      gesture, and exclusions survived concept selection and implementation.
- [ ] Consequential assumptions and substitutions were resolved with the
      person; no invented branded prop is presented as an official product.
- [ ] The visitor directly controls the requested gesture and meaningful
      state changes; merely starting an animation is not treated as equivalent.
- [ ] Relevant sourced explanations appear during the corresponding action,
      not solely in a static panel or an unrelated timer-driven ticker.
- [ ] A visitor can discover the action, read and revisit its explanations,
      and understand the selected concept's stated takeaway.
- [ ] Gesture precision, timing and extra steps are justified by the agreed
      learning goal or explicit training scope, not added for their own sake.
- [ ] Product-range completeness preserves exact required identities;
      coverage does not replace the message or turn the main journey into
      a catalogue hunt.
- [ ] The rendered result matches the chosen mockup, is subject-specific,
      and is ready for the person's visual review, not self-certified as
      satisfying their aesthetic preferences.
- [ ] Rendered critique findings are tied to viewport/state evidence.
      Polish preserved the approved meaning, real assets, gestures,
      source relationships and full requested range rather than silently
      redesigning them.

### Technical correctness
- [ ] Runs with no network connection (or the blocker is reported instead).
      Test the exported file from disk with requests blocked, including a
      reload and the main interaction; checking for CDN tags alone is not
      offline verification.
- [ ] Pointer, touch and keyboard equivalents reach the intended states;
      contact/threshold transitions, release/cancel, bounds, and replay work.
- [ ] Explanations agree with object state during forward movement,
      revisiting and reset; illustrative timing is not claimed as real physics.
- [ ] Both languages are complete, with no untranslated or placeholder text.
      Switch language mid-interaction and verify the currently visible
      explanation, controls, accessible labels, Sources and completion state.
- [ ] Sources panel is present and matches what was actually used.
- [ ] Every illustrative element is labelled as such, in the panel or inline.
- [ ] Brand guidelines are followed, or the compliance gap is disclosed.
- [ ] Embedded assets have documented permitted reuse; unclear rights were
      resolved or the blocked asset was not embedded.
- [ ] Download HTML works and produces the complete file.
      Reopen that downloaded file and repeat the main interaction offline.
- [ ] No leftover lorem ipsum, placeholder imagery, or TODO text remains.
- [ ] No runtime errors; the scene and explanations remain usable on narrow
      screens, with visible focus, readable contrast and reduced motion.
- [ ] Actual transformed bounds, readable captions, touch targets, dialog
      focus and input interception were checked where relevant. CSS sizes
      or no-overflow assertions alone are not visual/usability acceptance.
- [ ] The polished path was replayed at representative desktop, phone and
      relevant intermediate widths, including EN/NL expansion, dialogs,
      recovery and ending states. Record untested surfaces honestly; a
      clean detector or no-overflow check is not visual acceptance.

A blocked or unverified requirement is not a pass. Report status separately
for all four gates. A useful interaction prototype or technically ready
review build can be shared as such; do not call it the finished branded
experience while authenticity or message delivery is blocked. Do not claim
measured human comprehension from an author checklist or reviewer proxy.
Ask for visual/message feedback separately from checks actually performed.

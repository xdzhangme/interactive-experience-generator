# Concepts and interaction

For revisions to an approved experience, use the fast path in `SKILL.md`
and `intent-and-revisions.md`; do not reopen concept selection. Keep the
identity, medium and behavior of each object separate. A real product
image, a spatial model and genuine visitor input solve different needs;
mix them deliberately without claiming they are all 3D.

## Choosing the subject
A subject is the focal thing inside the broader brief — for a railway
operator, perhaps the train itself, a ticket, or the network; for a
semiconductor company, perhaps the lithography machine or a single chip.
If the person already named the subject, preserve it rather than offering
replacements. Otherwise offer 2–4 subjects grounded in research, accept a subject the
person names themselves, and accept "no single subject" as a valid answer —
some briefs are better served staying at the company or product level.

## The four concepts
Start from the confirmed message brief in `references/message-and-brand.md`.
All four communicate that same company message and takeaway. Vary how the
visitor experiences the evidence, not what the company is meant to say.
Before shaping the options, combine the relevant generator guidance with
the bundled Impeccable and Emil advice in `layout-motion-inspiration.md`.
Use `pattern-library/INDEX.md` to retrieve helpful examples and follow its
concept/build/review handoffs. These are simultaneous design inputs, not
an inspiration pass followed by a late visual/motion pass.

Three solid concepts and one wild card. Each concept is a short pitch
stating:
- **Visual medium**: spatial 3D, technical cutaway illustration, a
  scroll-led journey, a diorama, a dashboard, or another medium entirely —
  whichever genuinely suits the subject (see `art-direction.md` for how to
  choose).
- **The visitor's main action**: what they do with their hands or attention
  — fly through, scrub a cutaway, scroll a journey, adjust a control,
  compare two states.
- **Composition and hierarchy**: what leads, where the action and current
  explanation sit, and how the arrangement remains useful on a phone.
- **Motion purpose and feel**: what movement explains or acknowledges,
  what stays still, and how direct feedback, interruption and reduced
  motion preserve the action. Exact curves/durations can be refined in code.
- **The company message and takeaway**: what the visitor should understand
  about the company afterward, and which real offering provides the proof.
  Completing a task or counting explored products is not that takeaway.
- **Why this subject**: what about this specific company or product this
  concept is built from — not a generic template with its name swapped in.
- **Intent check**: which confirmed product, scene, gesture, and exclusions
  this concept preserves, and any unresolved dependency.
- **Interaction mapping**: visitor input -> observable consequence ->
  company meaning/benefit -> official proof -> touch/keyboard equivalent.
  Specify why the consequence demonstrates the message, not just a trigger
  for "interactive facts."
- **Story arc**: how the opening frames the message, the main moments
  demonstrate it and the ending connects the visitor's actions to the
  company takeaway. Include real permitted identity in the composition.
- **Reference adaptation**: which relevant generator/principle guidance
  and stored pattern IDs inform this option, what is adapted or rejected,
  and why it fits the message. Keep source dates/evidence limits in the
  existing notes. Explain an original mechanism when no stored one fits;
  no source quota or pasted component is required.

Carry the selected option's reference decisions into its execution
contract and choreography. Revisit the relevant guidance while building
and reviewing, rather than treating references as exhausted after ideation.

The wild card takes a genuine conceptual risk — an unexpected angle, an
unusual medium, an unconventional entry point — while still respecting the
hard rules on facts, branding, and sourcing. It is not permission to invent
unverified facts or override brand guidelines.
It also preserves explicit requirements. Take risks in treatment, viewpoint,
or choreography, not by replacing a requested physical action with a
different story.
A mood-only wild card with no company meaning fails even if it is striking.

## Interaction that carries the explanation

When the subject and brief have a physical action, let the visitor perform
it on the object: drag, dip, scan, twist, place, or another appropriate
gesture. Input changes meaningful object state; explanation appears at the
relevant contact, position, angle, or stage. Present it in the scene without
obscuring the object, and keep it available long enough to read, pause, or
revisit. Do not depend solely on hovering or fleeting animation.
The response must support the approved company message. A history fact
after a physical gesture is not a meaningful connection by itself.

A button that merely starts a movie, an unrelated rotating fact ticker, or
hotspots opening static panels is not a substitute for the requested
gesture. Hotspots and panels may supplement it. If the subject is abstract
or has no physical action, choose a meaningful exploration or comparison;
do not force a drag gesture onto every company.

For each mapping, describe starting state, useful intermediate states,
completion, and restart/revisit behavior. Reversal need not undo an
irreversible real process: explain that distinction and make replay explicit.
Use pointer/touch and keyboard controls for equivalent outcomes, with
visible instructions and readable, accessible explanations.
Remove additional precision, orientation or timing requirements that add
effort without helping the approved takeaway. Preserve them when they are
an explicit training requirement; do not default to a training simulator.

## Range coverage without losing the story

When the brief includes a complete product range, keep every required entry
identifiable and reachable. Use selected offerings as evidence in the
coherent main story, with complete optional exploration alongside it.
Do not silently remove entries, make all entries interchangeable generic
props, or require visiting the whole catalogue to understand the message.

## Choreograph the selected action before choosing widgets

Keep the approved concept, message and requested gesture. Work out how the
visitor acts on the subject and perceives the consequence; then choose
controls. Do not start with a standard chip/slider/Next shell and assign
every activity to it.

Record one compact choreography alongside the execution direction contract
in `art-direction.md`:

| Moment | Define |
|---|---|
| Before input | Starting object/task state, discoverable cue, target and instruction; what the visitor can infer without reading a tutorial wall. |
| During input | What position, angle, pressure-free hold, choice or authored content controls; how the subject and relevant explanation respond while input changes. |
| After input | Visible result, meaningful completion or confirmation, associated benefit/proof, and the next available action. |
| Interrupted or wrong input | Release/cancel, bounds, invalid choice, correction and reset; no stuck capture, surprise completion or unexplained dead end. |
| Equivalent access | Touch and keyboard or another appropriate accessible path to the same meaningful state and explanation, without requiring identical motor movements. |

Prefer direct manipulation when it clarifies the approved action: input
should affect the offering or evidence, not merely advance a progress
meter. Abstract tasks can instead use comparison, composition, navigation
or a meaningful decision. Familiar forms and selection controls may be
the best fit for a workshop or operational tool. Do not make everything
draggable or add dexterity tests to manufacture novelty.

Feedback begins during input when the action is continuous; do not withhold
every response until completion. For discrete actions, acknowledge the
choice promptly and make its consequence legible. Specify the relevant
visual change: position, opening, population, relationship, content or
another subject-grounded state. Use stable labels and accessible state
announcements as appropriate, not just colour, particles or a success toast.
Completion effects must not imply unsupported physical behavior.

Match motion to material and meaning without making speculative physics
claims. A long transition should preserve continuity, not delay input
acknowledgment. Handle repeat input and interruptions through the shared
state; avoid canned animation that continues after cancellation. Sound or
haptics are optional, not dependencies or substitutes for visible feedback.

Compare the choreography with available recent work using `design-log.md`.
The same verb can feel different through target behavior, feedback and
spatial organization; a different verb can still hide the same staged
quiz. Do not count control types as creativity. Justify retained patterns
by their usefulness and change only the repetitive execution within scope.
Prove this choreography in the representative-scene gate in
`build-and-delivery.md`, not only in a pitch or static three-state sketch.

## Interaction catalogue (inspiration only)
A broad set of interaction families to draw on, never a menu to pick from
mechanically:
- **Explore in 3D**: hotspot explorer, exploded/cutaway scrub, fly-through,
  configurator.
- **Tell a story**: scrollytelling, timeline, parallax world, guided tour.
- **Play and try**: sandbox with controls, what-if calculator, card-based
  exploration.
- **Show data and place**: route or network map, isometric diorama,
  dashboard.
- **Compare**: before/after slider, side-by-side comparison.

Combine two of these only when the second genuinely adds value to this
specific subject; one exceptional interaction, well executed, beats two
mediocre ones bolted together. A subject may also suggest an interaction
entirely outside this list — follow the subject, not the list.

## Variety across the three solid concepts
Vary composition, navigation, camera or scroll behaviour, palette (within
brand constraints), typography pairing, motion, and the opening moment
independently across the three solid concepts, so they read as genuinely
different experiences — not one template re-skinned three times. The wild
card may depart from the format entirely.
All variations stay within the confirmed requirements and verified brand
constraints. If variation would break them, vary treatment instead.

## The visual preview
Before anything is built, produce one lightweight mockup per concept:
its actual composition, palette, typography, and the cue for its primary
interaction. This is a static preview of the real proposed design, not a
mood board and not a working prototype. Only after the person selects one
does it get built.
Include the reference-backed hero silhouette, interaction cue, and one
visible action-linked explanation of company meaning. Show authentic
permitted branding/products plus the opening promise and ending takeaway.
If rights or files are pending, mark a preview as a wireframe/prototype,
not evidence of final brand fidelity. Mark untested behavior as proposed.
For showcases, also prove the imagery-led, scene-led treatment in
`art-direction.md`: actual asset scale/framing and one meaningful action
state, with restrained supporting art and readable controls. Reuse this
preview; do not add another concept-selection round to resolve execution.

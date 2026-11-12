# Offline pattern library

This is a curated reference library, not model training, a component pack
or a set of finished company concepts. `patterns.json` contains original
analytical descriptions grounded in Codrops and React Bits primary sources.
No third-party source code, media or component ports are included.

## Guidance roles and priority

The library is one resource within the skill, not its whole design method.
Confirmed intent and the generator's factual, asset, accessibility and
delivery-mode requirements govern all reference use.

| Resource | Role throughout the work |
|---|---|
| Generator's own guidance | Company storytelling, source-backed meaning, interaction choices, art direction, official assets, 3D craft, revisions, accessibility, delivery and design history. |
| Bundled Impeccable adaptation | Composition, hierarchy, grouping, motion purpose, critique and polish, beginning with concept development. |
| Bundled Emil adaptation | Animation purpose/frequency, timing and easing choices, input feedback, interruption and recovery; plan the behavior during concepts and refine values in working code. |
| Stored patterns and optional live examples | Concrete mechanisms to keep, adapt or reject according to the brief; examples are neither rules nor complete concepts. |

Use the relevant generator guides together with
`references/layout-motion-inspiration.md` and
`references/experience-critique-polish.md`. Do not defer Impeccable or Emil
until implementation, or discard the skill's original guidance in favor
of a visually impressive example.

## Carry references from concepts through review

- **Concepts and previews:** read relevant guidance and candidate records
  together. For each option, state composition, input/consequence/message,
  motion purpose, accessible alternatives and the reference principles
  being adapted. If no stored mechanism fits, explain the original choice
  rather than forcing a match. Static previews show direction, not working feel.
- **Selected-concept build:** reopen the selected records and relevant
  guidance before code. Translate accepted principles into responsive
  layout, state/feedback, timing/easing, interruption/reset and the declared
  delivery mode. Retain the approved subject, gesture, medium and brand.
  Refine values through the representative scene, not a new concept round.
- **Critique and delivery:** compare the rendered scene and exercised input
  with those accepted adaptations. Check meaningful state, visual character,
  accessible paths and technical delivery separately. Source resemblance,
  a cited pattern or passing controls cannot establish company meaning.

Keep a compact reference-use note in the existing concept/execution record:
option or stage, guide/principle or pattern ID, what is kept/adapted/rejected,
the concrete design decision and what evidence will check it. For stored
patterns retain source dates and observation limits. Carry the selected
note forward; do not make a new mandatory file, source-count quota,
external install or extra approval round. Revisit only relevant guidance
during a scoped revision rather than rereading the whole catalogue.

## Match the visitor's need before the effect

Read this index during concept development, then retrieve relevant records
from `patterns.json`. Text search is sufficient; Python, a database,
embeddings and network access are not required to use the knowledge.

1. Start with the approved company message, subject, medium and gesture.
   Name the visitor's job: compare, discover, manipulate, follow a process,
   configure, navigate or understand a consequence.
2. Search `user_goals`, `tags`, `input` and `response` for that job.
   Optional terminal search: `python scripts\manage_patterns.py --search compare`.
   Search is lexical retrieval, not a relevance guarantee.
3. Read the full candidate records, including `avoid`, `accessibility`,
   `offline` and `licensing`. Reject effects that obscure the actual offering,
   replace the requested gesture, create unsupported claims or require an
   unapproved change of medium.
4. Usually shortlist two to four relevant mechanisms, not thirty effects.
   Map each to visitor input, observable result, company meaning and official
   proof. Explain why the mechanism helps that story.
5. Develop the normal three concepts and one wild card through genuinely
   different treatments. Do not equate four records with four complete
   concepts or let the library limit a better subject-specific idea.

### Retrieval guide

| Visitor need | Search terms | Check before proposing |
|---|---|---|
| Compare alternatives or before/after states | compare, reveal, slider, split | Both states remain understandable without precise dragging. |
| Discover a range without a catalogue hunt | gallery, grid, carousel, navigation | All requested entries remain accessible; the main message needs no quota. |
| Follow a sequence or process | scroll, journey, timeline, progress | Motion follows meaningful progress, not an unrelated autoplay clock. |
| Manipulate an object or inspect a relationship | drag, pointer, rotation, depth | Input changes approved state; camera motion alone is not operating a product. |
| Focus attention or explain a transition | mask, reveal, transition, text | Evidence stays readable and motion does not replace the explanation. |
| Choose, configure or recover | selection, feedback, menu, navigation | State, focus, cancellation and reset remain explicit and accessible. |

These are starting queries, not a promise that every verb has a matching
record. No match is permission to design an original mechanism, not to
mislabel a decorative effect as the requested action.

## Stored pattern directory

Retrieve each ID's full record from `patterns.json`; this directory is not
a replacement for reading its evidence and avoid cases. Entries marked
advanced or decorative should rarely lead an ordinary company story.

| Pattern ID | Mechanism / primary use |
|---|---|
| `codrops-astro-page-transition-cover` | Cover/reveal continuity between chapters. |
| `codrops-wide-persistent-card-reflow` | Recompose the same items to explain different groupings. |
| `codrops-sticky-grid-scroll-timeline` | Let scroll control meaningful phases within a stable stage. |
| `codrops-image-tiles-menu` | Preview a destination, then assemble its selected image. |
| `codrops-gooey-cursor-trail` | Decorative merging field around pointer activity. |
| `codrops-progressive-enhancement-webgl-layout` | Keep semantic content authoritative under optional rich rendering. |
| `codrops-cursor-memory-grid-trail` | Separate recent input history from a temporary visual trace. |
| `codrops-card-to-3d-scene` | Open a compact offering into actual spatial detail. |
| `codrops-webcam-landmark-mask` | Advanced, opt-in live-input/overlay alignment; not a default. |
| `codrops-sketch-029-infinite-loop-3d` | Optional looping gallery with perspective on flat tiles. |
| `codrops-sketch-025-infinite-loop-horizontal` | Optional horizontal exploration with finite navigation alternatives. |
| `codrops-sketch-019-image-svg-filter-motion` | Decorative image-treatment intensity tied to pointer movement. |
| `codrops-record-player-direct-manipulation` | Advanced audio-object explanation; source gestures only partly documented. |
| `codrops-earthlight-data-scene` | Coordinate spatial view, time and revisitable state. |
| `codrops-kinetic-typography-scroll` | Short, readable message beats paced by scroll. |
| `reactbits-scroll-stack` | Keep process stages related through a receding stack. |
| `reactbits-accordion-gallery` | Expand a selected item within a compact visual group. |
| `reactbits-scroll-expand` | Move from framed media to a broader story scene. |
| `reactbits-card-nav` | Disclose a small hierarchy of grouped navigation links. |
| `reactbits-stack` | Explore a small revisitable pile through manipulation or buttons. |
| `reactbits-hold-button` | Illustrate deliberate commitment with visible cancellation. |
| `reactbits-slide-commit` | Distinguish manipulation, pending state and confirmation. |
| `reactbits-scrub-field` | Combine exploratory value adjustment with typed precision. |
| `reactbits-code-slots` | Explain fictional code entry without collecting real codes. |
| `reactbits-swipe-row` | Expose item-specific actions with accessible visible alternatives. |
| `reactbits-halftone-reveal` | Inspect image detail with a full-detail alternative. |
| `reactbits-target-cursor` | Supplement target discovery with a pointer framing cue. |
| `reactbits-masonry` | Explore visual evidence and open a readable detail view. |
| `reactbits-swipe-toast` | Acknowledge actions through dismissible temporary status. |
| `reactbits-rubber-segment` | Switch comparable states with a shared selection marker. |

## Offline behavior and evidence

Without browsing, use the stored mechanisms and adaptations directly.
Identify the pattern IDs and recorded source dates in the existing concept
notes. Say "based on stored documentation/source inspection" where that is
the evidence; do not claim a fresh visit, measured performance, tested
interaction feel or observed motion.

`mechanism`, `input`, `response` and source metadata describe the reference.
`user_goals`, `layout`, `motion`, `accessibility`, `offline` and `avoid`
include generator-authored analysis or recommendations. Those adaptations
are not claims that the reference already implements accessible equivalents
or offline behavior. Numerical animation parameters must not be invented.

With browsing, selectively verify a current example when it materially
helps. The library remains usable if a link breaks. Missing inspiration
access does not erase official company research, and stored patterns do
not supply missing company facts, brand files or asset permissions.

Descriptions are not executable examples or approved visual mockups.
Build and exercise the selected mechanism in the representative scene;
then retain the generator's separate brand, message, intent and technical
acceptance gates. A recorded effect never certifies the generated result.

## Maintenance and distribution

Use `MAINTENANCE.md` for source research, deduplication, record requirements
and package validation. Refreshing records changes local files, not model
weights. An app-local weekly automation is not shipped with the skill and
does not run on another person's installation.

After review, rebuild the `.skill` file. Installed copies remain snapshots
until re-imported; no background update code or network fetch runs inside
the generated HTML.

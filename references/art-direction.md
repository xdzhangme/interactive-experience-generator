# Art direction

Adapted and condensed from Anthropic's `frontend-design` skill
(github.com/anthropics/skills, Apache-2.0) and `arvindrk/extract-design-system`
(MIT) — see `NOTICE.md` for full attribution. This file is an original,
condensed summary for this workflow, not a verbatim copy.

For the scoped Impeccable adaptation, also read
`references/experience-critique-polish.md`. Together these files bundle
surface-mode selection, visual direction, motion and an observed
critique/polish loop under the approved message, real branding and delivery-mode
constraints. The visual-direction guidance also draws on Impeccable 4.8.0
`reference/new-work.md`; this is an original scoped adaptation, not its
concept-randomisation or runner workflow. See `NOTICE.md`.
For practical grouping, spacing, responsive order and motion decisions,
also use `layout-motion-inspiration.md`. Its Codrops Creative Hub and
React Bits references are optional inspiration, not brand authority or
permission to change the approved medium.

## Separate the idea from its execution

The concept states what the visitor experiences and understands. Its
execution determines how the work occupies the screen and responds to
input. A good concept can fail through a generic layout or lifeless
feedback; do not replace the concept to hide that failure.

For new work, derive visual authority from the approved brief, real assets
and selected mockup. For revisions, inspect the incumbent rendered page
and separate frozen choices from the axis the person wants changed.
Approval of an idea does not automatically freeze every incidental widget.
Approval of an exact composition does constrain changes to it. Do not
silently replace either a pinned visual world or an approved behavior.

## Execution direction contract

After concept selection, resolve these choices in the existing brief or
session record before artifact code. Infer small details from approved
evidence; do not turn this into another questionnaire or design document.

| Choice | Describe concretely |
|---|---|
| Surface mode | Whether the visitor is experiencing, operating, reading or deciding; let that purpose determine the interface's prominence. |
| Composition and scale | What dominates the first viewport, its relative size, eye path, depth or flat hierarchy, and where the main action and explanation live. |
| Imagery and supporting art | Which actual official asset leads, how framing/layering makes it carry the visual story, and which restrained supporting elements earn their place. |
| Materials and light | The chosen image treatment or scene surfaces, light/shadow and background relationship; deliberate flat graphics are valid, not failed 3D. |
| Typography | Verified brand type or disclosed fallback, display/body roles, reading measure and how labels relate to the subject. |
| Motion | One earned focal moment if useful, plus state continuity and immediate input feedback; identify what stays still. |
| Controls and utilities | Where the visitor acts, how that action is cued, and how language, Sources, download and recovery remain reachable without dominating. |
| Responsive staging | How phone and desktop preserve the subject/action/explanation relationship, including Dutch expansion and reduced motion. |

Use decisions that can be drawn and inspected, not adjectives such as
"premium", "immersive" or "creative" alone. For example, specify whether
the subject fills the scene or sits on a work surface, how it is framed,
and where a changing result appears. Do not prescribe one layout for all
subjects. Keep brand rules and authentic asset proportions intact.

Show the selected opening and the primary action before, during and after
input in the existing preview, reusing approved mockups where they already
answer these choices. Plan enough type, scale and feedback detail to guide
the representative scene, not an entire polished journey upfront.
Static states communicate direction; they do not prove responsiveness.

## Official imagery leads; composition supplies the ambition

For real-company showcases, keep official imagery dominant. When spatial
3D is the approved medium, let the actual official model lead rather than
substituting photographs or newly authored branded geometry. Preserve
explicit object-specific exceptions and fictional briefs.

Asset presence is not art direction: a small packshot, a token logo or a
washed-out photo behind large instruction panels is not an imagery-led
showcase. Give the relevant authentic asset enough scale, clear framing
and visual weight to carry the scene and remain recognizable.

Develop richness through deliberate subject scale, photographic framing,
foreground/background relationships, layering, negative space, depth and
brand typography. Use only the techniques the subject earns; do not turn
this list into a new template. Keep type and other graphic elements in
support of the imagery rather than competing for attention.

Supporting artwork stays restrained. Neutral staging, a useful texture,
an annotation or a quiet graphic motif can clarify the world. Do not
compensate for weak composition with unrelated illustration, particles,
gradients, generated lookalikes or decorative clutter. Authored supporting
art must not impersonate an official asset or invent company evidence.
A missing usable official asset is still a blocker, not a reason to draw it.
An official asset that loads by URL is usable online even without a local file.

Respect asset terms and brand rules when cropping, masking or layering.
Do not distort logos/products, hide identifying details needed for the
story, or composite an unsupported factual product configuration.
Distinguish illustrative staging from a documentary depiction.

## Scene-led showcases can escape enclosing panels

For an Experience/showcase surface, start from a scene occupying the
browser, not a demonstration placed inside a large rectangular container.
Let the subject and intended action determine spatial organization. A
full-bleed photographic field, an oversized isolated product, an asymmetric
image composition or a layered scene are possible treatments, not presets.

Be bold when it improves the subject's presence or meaning; do not make
every page experimental. The browser remains rectangular, but the
experience need not inherit nested boxes, a centred max-width card or an
identical left-demo/right-instructions split. Removing borders alone does
not change that composition.

Integrate cues and contextual explanations into readable scene regions
where useful; keep utility controls reachable and gesture targets clear.
Do not make labels chase moving objects or hide controls to look artistic.
Keep intentional frames, dialogs and bounded reading surfaces where the
content benefits. Operate/task surfaces keep efficient, familiar layouts.
There is no blanket ban on cards, grids or rectangles.

In the existing concept preview, show the actual asset treatment, scale,
framing, supporting art and control placement in the opening and a
meaningful interaction state. Reuse the selected preview rather than
adding another approval round or four more concepts. A textual promise,
mood board or generic wireframe cannot prove this treatment. If the
required assets are unresolved, label that preview's limitation honestly.
The later representative scene proves working input, not a second choice
of concept.

## Prevent the interface from becoming the subject

Compose around the offering, evidence or actual work. Do not automatically
wrap it in a title bar, left stage rail, centre demo and right instruction
card. A different logo, background or 3D object inside that shell is not a
new visual execution.

Place relevant explanations near the affected state, in a clear scene
region or an integrated task surface. They need not float, animate, attach
to every object or cover the hero. Persistent panels, cards, sliders and
Next buttons remain appropriate when they serve the task, sequence,
readability or accessibility. Give each dominant pattern a brief
subject/task reason instead of adopting it because the last build used it.

Use `design-log.md` to compare execution with available recent work before
building. Inspect the subject's scale, composition, navigation, input and
feedback separately. When these repeat without a task reason, change the
relevant execution choices within scope; do not merely recolour them.
Do not force a new gesture to meet a variety quota or claim uniqueness
without comparison evidence.

## Ground every concept in the subject, not the industry
Begin with the approved company message, actual offerings and proof points
in `references/message-and-brand.md`. Make the scene express that meaning,
not just evoke the industry. Recognisable identity and clear communication
are separate: extra logos cannot repair a message the experience never
demonstrates.

A distinctive look comes from the subject's real forms, materials, scale,
environment, and vernacular — a train's choice of materials and vernacular
differs enormously from a chip's. Build from the brief's real content
throughout; never fall back to a generic template and swap in a logo.

**Self-critique test, applied to every concept before it's shown:** if the
brand name and logo were removed, would this still look like a generic
experience for any company? If yes, push further into subject-specific
detail — composition, interaction, and story, not just colour.

## Recognizable does not mean merely branded

Once the plan is approved, compose the page around the actual permitted
official models/images/assets, not newly drawn imitations of them.
Follow `sources-and-labeling.md`. Official references establish identity;
they are not equivalent to official files actually used in the page.
Concept/style approval is not permission to redraw the products.
Obtain explicit object-specific approval for necessary substitutions.

Before styling a real hero object, inspect official reference photos of the
confirmed variant. Preserve the identifying silhouette, proportions,
control layout, packaging and markings. Check those features side by side
with the rendered object; a generic primitive bearing a logo is not enough.
Stylization of a branded object is allowed only as an explicit agreed
exception and disclosed; it cannot hide a change of product. Never present
a reconstruction as an official model.

Compose the scene around the confirmed gesture and its learning moments:
the visitor should see what can be manipulated and what changed because
of their action. In-scene explanations are part of the composition, not a
fact panel added after the visual work. Their appearance should follow
relevant object states and remain readable without chasing animated text.

## Brand guidelines govern
When official brand guidelines exist, follow them for colour, type, and
logo usage without exception. Spend creative effort on composition,
storytelling, interaction, and motion instead — these are where this
experience earns its distinctiveness, not brand colour substitution.

When no official guidelines can be found, extract verified brand elements
directly from the official site rather than approximating them:
- Capture exact colour values, the real typeface stack, logo files and their
  official usage context, and the tone of real product imagery — read these
  off rendered brand pages, don't guess at them.
- Record exactly where each element was found, and disclose in the Sources
  panel that full guideline compliance could not be established.

Use the real permitted logo, not typeset brand-name imitation. Carry brand
identity through recognisable offerings, appropriate imagery, materials,
voice and interactions; do not scatter logos merely to increase a count.
Permission gaps block authentic branded delivery even when a neutral
prototype can still be useful. Resolve and label that distinction early.

## Choosing the medium
Recommend whichever rendering medium best serves this specific subject;
there is no default medium. Scene-led composition does not require 3D or
override an approved medium:
- **Precise spatial 3D** suits a subject whose physical form or mechanism is
  the point (a machine, a vehicle, an instrument).
- **Technical cutaway illustration** suits infrastructure or systems better
  shown in cross-section than navigated in free 3D.
- **Scrollytelling / journey** suits a process or a path (water from source
  to tap, a request through a system).
- **Dashboard, map, or diorama** suits data, geography, or a network.

Photorealism is not the default quality bar — recommend the treatment
(precise technical illustration, stylised 3D, cinematic realism, or
otherwise) that best serves this brief.
An explicitly requested medium or scene remains a requirement. Recommend a
different one only as a proposed change, with its tradeoff explained.

## Typography, hero, and motion
- Open with the most characteristic thing in the subject's world — not
  automatically a headline-plus-stat-plus-gradient block.
- Make the opening's company promise understandable, demonstrate it through
  the core actions and give the ending a company takeaway. Do not reserve
  the actual message for optional copy or the Sources panel.
- Use one or two typefaces chosen for this subject, not default safe
  choices; if two, make them clearly distinct in role.
- Use one orchestrated motion moment — an opening sequence or one reveal —
  rather than scattered hover effects and fade-ins on every element. Motion
  that responds to the visitor's own action (opening, scrubbing, revealing)
  is always welcome.
- Avoid generic AI-design tells: a single accented word in a headline,
  tracked-out all-caps labels everywhere, numbered markers on content that
  isn't actually a sequence, identical rounded cards with the same soft
  shadow regardless of hierarchy.

## Restraint
Spend boldness in one place per concept. Keep everything around it quiet
and disciplined. Build to a quality floor without announcing it:
responsive, visible keyboard focus, reduced-motion respected, legible
contrast.

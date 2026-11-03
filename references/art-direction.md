# Art direction

Adapted and condensed from Anthropic's `frontend-design` skill
(github.com/anthropics/skills, Apache-2.0) and `arvindrk/extract-design-system`
(MIT) — see `NOTICE.md` for full attribution. This file is an original,
condensed summary for this workflow, not a verbatim copy.

For the scoped Impeccable adaptation, also read
`references/experience-critique-polish.md`. It adds Experience-led
composition and an observed critique/polish loop under the approved
message, real branding and offline constraints; it does not select a
replacement visual world or add an external skill dependency.

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

Before styling a real hero object, inspect official reference photos of the
confirmed variant. Preserve the identifying silhouette, proportions,
control layout, packaging and markings. Check those features side by side
with the rendered object; a generic primitive bearing a logo is not enough.
Stylization is allowed when agreed and disclosed, but cannot hide a change
of product. Never present a reconstruction as an official model.

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
Recommend whichever medium best serves this specific subject — there is no
default:
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

# Three.js craft (read only when the chosen concept uses spatial 3D)

Condensed from `majidmanzarpour/threejs-game-skills`
(`threejs-aaa-graphics-builder`, MIT) — see `NOTICE.md` for attribution.
This file is an original, condensed summary for this workflow, not a
verbatim copy, and strips the parts of that skill specific to games.

## Core rule
Load the actual permitted official model first, then compose materials,
lighting and effects around it. Glow, bloom and particles do not substitute
for authentic geometry. Author branded geometry yourself only under an
explicit object-specific reconstruction exception, not merely plan approval.

## Official models first; reconstruction is an approved fallback
Look for a suitable official model of the exact offering and check reuse
terms before constructing geometry. Do not assume official models exist,
but do not assume they are absent or procedural geometry is the first choice.
Follow the official-first selection order in `sources-and-labeling.md`.
When no suitable usable official model is available, explain the gap and
obtain approval for a verified licensed third-party model or reconstruction;
reuse existing explicit approval rather than asking again.

Only when reconstruction itself was explicitly approved, build procedural
geometry from inspected official reference photos of the confirmed variant.
Do not treat reference inspection as permission to substitute a model.
Use verified dimensions
where published; identify photo-estimated proportions as approximations
rather than claiming measured accuracy. Label the result
**illustrative geometry** — a reconstruction for this experience, not a
certified replica of the real object.
Preserve identifying features before adding effects. If references cannot
be inspected, resolve the gap instead of inventing recognizable geometry.

## Upgrade every visible surface
Not only the hero object: the ground or environment it sits in, secondary
props, material variation, and lighting all read as either considered or
neglected. A single detailed hero model in an empty grey void reads as
unfinished.

## Keep it genuinely offline
A single offline HTML file means no runtime dependency on a CDN, remote
texture host, or external font service. Embed or inline the Three.js
runtime, shaders, and any textures the scene needs. Keep the polygon and
texture budget practical for a file that must load and run entirely from
disk, with no network connection.

## Camera and interaction
Match the camera behaviour to the concept's chosen interaction — a
fly-through for a hotspot explorer, an orbit for a configurator, a fixed or
scroll-tied camera for a cutaway or scrollytelling piece. The camera itself
is part of the art direction, not an afterthought bolted onto a finished
scene.
Camera controls must not steal the requested object gesture. Separate orbit
and manipulation targets, use pointer capture where appropriate, and
exercise touch and keyboard equivalents. Drive responses and explanations
from the shared interaction state, not independent timers.

For an approved operating task, connect input to the relevant mesh or
component state: inspect the hinge, opening, placement or other observable
consequence, including reversal/reset. Camera movement and a changed caption
alone do not establish that behavior. Prove the core-loop gate in
`build-and-delivery.md` before refining lighting and effects. If inspection
itself is the approved purpose, assess the information revealed by its
camera and exploration controls rather than inventing operating steps.

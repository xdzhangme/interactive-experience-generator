# Interactive experience generator

**Turn a company's story into something people can explore, not just read.**

A skill for Microsoft Copilot Cowork and other skill-enabled agents. Start with
a company or product; the agent researches official sources, develops concepts,
and builds your chosen direction as **one offline HTML file**.

![Illustrated workflow: start with a company, research official sources, design a meaningful interaction, and deliver an offline HTML file.](assets/readme/workflow.svg)

*Workflow illustration, not a screenshot of a generated experience.*

## What you get

A full-screen interactive experience rather than a conventional website or slide
deck. Each experience includes:

- **A company story you can interact with** — visitor actions reveal a sourced
  benefit or message, using actual permitted company assets.
- **English and Dutch** — with keyboard and touch access, plus reduced motion.
- **Sources and Download HTML buttons** — with assets embedded for offline use.

Visual direction, interaction design, critique, and polish guidance are bundled.
No separate design-skill installation is needed.

## Install

### Microsoft Copilot Cowork

1. Open the [skill package](dist/interactive-experience-generator.skill).
2. Choose **Download raw file**. This public download needs no GitHub sign-in.
3. Import the `.skill` file into Cowork. Re-import it after updates.

### Other agents

Copy these files and folders into an `interactive-experience-generator` folder
in your agent's skill location, preserving the directory structure:

```text
interactive-experience-generator/
  SKILL.md
  references/
  NOTICE.md
  licenses/
```

`SKILL.md` alone is not enough.

## Try it

After installing, ask your agent:

```text
Use interactive-experience-generator
to create an interactive experience
for [company or product].
Research official public sources.
Recommend a message and concepts
before building.
```

A company name is enough to start. Add a specific product, audience, or visitor
action if you already have one in mind.

**Research → choose → build → refine.** The agent recommends a source-backed
message, presents four concepts with visual previews, and builds the one you
select. It checks a representative interactive scene before expanding, then
reviews the result and offline export. For revisions, it preserves approved
choices and changes the requested part instead of restarting.

## Important limits

Research and company assets must come from **publicly available resources**,
not private or internal material. Building needs an agent with research,
asset-download, file-output, and visual-inspection capabilities; the skill
does not provide those tools or grant asset reuse rights.

Required official images, logos, packaging, and models must be obtained and
permitted for use. Missing assets block completion unless you explicitly approve
a specific substitute. Approving a concept does not approve drawn lookalikes.

Every experience visibly includes this disclaimer, with a Dutch equivalent:

> This experience is generated entirely with Microsoft Copilot Cowork based on publicly available resources and for demonstration purposes only.

## Under the hood

The detailed guidance stays in the skill, so you do not need to read it to start:

- [Full workflow and requirements](SKILL.md)
- [Visual direction](references/art-direction.md) and
  [interaction design](references/concepts-and-interaction.md)
- [Critique and polish](references/experience-critique-polish.md)
- [Sources and asset rules](references/sources-and-labeling.md)
- [Build and delivery checks](references/build-and-delivery.md)
- [Attribution and license terms](NOTICE.md)

Keep `NOTICE.md` and [`licenses/`](licenses/) with redistributed copies. The
bundled Impeccable guidance is an attributed, scoped adaptation, not the full
upstream skill or command suite. Optional external inspiration is not a runtime
dependency; check each project's terms before reusing its code.

<details>
<summary>Package contents and evaluation notes</summary>

The `.skill` file is a ZIP containing 15 files under
`interactive-experience-generator/`. Package only `SKILL.md`, `references/`,
`NOTICE.md`, and `licenses/`; exclude the README, README assets, evaluations,
generated experiences, and local artifacts.

After rebuilding, compare the archive with the source files and update its
SHA-256 here:

```text
56bbe3399c6a55329666caec064cb6853b04703d735d7d71633ffce312b6eb7e
```

[`evals/evals.json`](evals/evals.json) contains 29 evaluation prompts;
[`evals/files/`](evals/files/) holds a fictional SVG fixture. Neither is included
in the package. Their presence does not prove they passed or that Cowork
downloads were tested. Text-only answers cannot establish rendered visual
quality or interaction feel.

</details>

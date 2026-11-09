# interactive-experience-generator

Turn a company's verified story into a full-screen interactive experience.
Deliver one offline HTML file with English/Dutch, sources, and a download button.

## Install

This repository is private. Sign in to GitHub with an account that has access.

**Cowork:** Open
[`dist/interactive-experience-generator.skill`](dist/interactive-experience-generator.skill)
and choose **Download raw file**. Import the file into Cowork. Re-import after
updates.

**Other agents:** Copy `SKILL.md`, `references/`, `NOTICE.md`, and `licenses/`
into an `interactive-experience-generator` folder in your agent's skill
location. Keep the directory structure; `SKILL.md` alone is not enough.

## What it does

- Research official sources and connect the company message to visitor actions.
- Use actual permitted logos, photos, packaging, and models, not drawn lookalikes.
- Download assets through available tools, curl/Python, or a browser; check the
  files and embed them for offline use.
- Report the exact download error or missing capability before asking for files.
- Preserve approved choices during revisions, including genuine visitor input.
- Include adapted Impeccable critique and polish guidance. No separate install.

The skill cannot grant network access or reuse rights. Missing required assets
block completion unless you approve a specific substitute. Plan approval alone
does not permit substitutions; existing approved exceptions remain valid.

## Package

The `.skill` file is a ZIP containing 13 files under
`interactive-experience-generator/`. Package only `SKILL.md`, `references/`,
`NOTICE.md`, and `licenses/`. Exclude README, evaluations, generated experiences,
and local artifacts. Compare archive contents with source and update this
SHA-256 after rebuilding:

```text
15da77e9ba39b8f25c1222d64460115d14f728050d03a4e216a33f588a6860fa
```

[`evals/evals.json`](evals/evals.json) contains 13 evaluation prompts; `evals/files/`
contains a fictional SVG fixture. These stay outside the package. Their presence
does not prove they passed or that Cowork downloads were tested.

Keep [`NOTICE.md`](NOTICE.md) and [`licenses/`](licenses/) with redistributed
copies for attribution and license terms.

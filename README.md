# interactive-experience-generator

A message-first skill that turns a company's verified story, products, and
services into a distinctive full-screen interactive experience. It delivers a
single offline HTML file with English/Dutch support, sources, and HTML download.

The self-contained package includes selected adapted Impeccable Experience,
critique, and polish guidance, not the full Impeccable runner. No separate
Impeccable installation, binaries, or commands are required.

After plan approval, the built page must embed/import and visibly use actual
permitted official model, product-image, packaging, logo, and other relevant
asset files, not agent-drawn SVG/CSS lookalikes or procedural recreations
based only on official references. General plan or style approval does not
permit substitutions. Missing required assets are blockers unless an explicit
object-specific exception is approved; existing approved reconstructions
remain preserved.

Revisions retain frozen approvals and separate each object's identity,
rendering medium, and visitor behavior. The bundled guidance also covers
genuine visitor input, ephemeral signature privacy, affected routes/states,
EN/NL and export coverage, and scoped critique/polish without redesigning
approved work.

## Access and install

This repository is private. Downloads and cloning require a GitHub account with
access to this repository; a repository link alone does not grant access.

**Cowork:** While signed in to GitHub with repository access, open
[`dist/interactive-experience-generator.skill`](dist/interactive-experience-generator.skill)
and use **Download raw file** to save the original `.skill` archive. Upload/import
that file through Cowork's skill-management interface.

**Other agents:** Clone or download the repository using an authorized GitHub
account. Copy the root `SKILL.md`, `references/`, `NOTICE.md`, and `licenses/`
together into an `interactive-experience-generator/` folder in your agent's
supported skill location. Preserve their directory structure; `SKILL.md` alone
is not the complete skill.

## Package and attribution

The root `SKILL.md`, `references/`, `NOTICE.md`, `licenses/`, and `evals/`
match the approved source. The distributable
`dist/interactive-experience-generator.skill` contains the 13 runtime/legal
files under its `interactive-experience-generator/` directory; the two
evaluation files remain repository-only. The archive's SHA-256 is:

```text
9cf314b1bc156f23d9cbc2feef42a78cb6ff506f38f3eaea66128340e8367f17
```

For future releases, package only `SKILL.md`, `references/`, `NOTICE.md`,
and `licenses/` into a ZIP-format `.skill` archive with that top-level
directory. Do not include the repository README, `evals/`, `dist/`, generated
experiences, or local session artifacts. Verify every archive member against
its source file and update the checksum above when replacing the package.

[`evals/evals.json`](evals/evals.json) includes ten reusable probes and an
authorised fictional SVG fixture in `evals/files/`. They cover intake,
interaction, company-message readiness, asset handling, scoped polish,
revisions, and actual official assets in the built page. Bundling these
probes does not claim that they were executed or that generated HTML,
browser behavior, or audience comprehension was verified.

See [`NOTICE.md`](NOTICE.md) and the bundled [`licenses/`](licenses/) for
third-party attribution and applicable terms. Keep these files with the skill
when copying or redistributing it.

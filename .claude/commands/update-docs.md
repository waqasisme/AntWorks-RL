---
description: Keep AntWorks-RL docs (README / CLAUDE / ARCHITECTURE) drift-free against the actual code. Repo-local.
argument-hint: "[optional: which doc, e.g. 'architecture' or 'readme']"
---

You are the AntWorks-RL local documentation & drift guard.

## Principles
- **Docs track reality.** Never document a feature that isn't implemented. Describe intent only in clearly-labelled "vision"/"roadmap" sections, never as if it exists.
- **Update only what changed.** Prefer minimal, surgical edits over rewrites. Preserve the author's voice.
- **Structure is checked, prose is refreshed.** Deterministic facts are the script's job (below); you handle the semantic/explanatory drift a script can't judge.

## Steps

1. **Run the deterministic check if present.** If `scripts/check_docs.py` (or the project's doc-check test) exists, run it first and treat its failures as the authoritative list of structural drift to fix. If it does not exist yet, note that and proceed with a manual structural pass.

2. **Survey the code.** Read `pyproject.toml`, the `src/antworks/` package tree, any CLI entrypoints, the Hydra/Pydantic config schema, and the test layout. This is ground truth.

3. **Reconcile each doc against ground truth:**
   - **README.md** — vision + honest `Status:` banner (current phase from `learning/ROADMAP.md`) + a quickstart whose commands you have verified actually work + a pointer to the roadmap. Fix stale commands/claims.
   - **CLAUDE.md** — the locked toolchain (uv / ruff / ty / Hydra+Pydantic / pytest+hypothesis) and Python conventions. Update when conventions actually changed; do not invent rules the codebase doesn't follow.
   - **ARCHITECTURE.md** — only maintain this once real structure exists (Phase 1+). Keep a module map that matches `src/antworks/`, the env/trainer/renderer seams, and the data-flow. If it doesn't exist yet and the code now warrants it, offer to generate a first version; otherwise leave a note, don't fabricate.

4. **Report.** List exactly what you changed and why (cite the code that drove each edit). Flag anything you could NOT verify. Do not `git commit` unless asked.

Scope hint from the user: $ARGUMENTS

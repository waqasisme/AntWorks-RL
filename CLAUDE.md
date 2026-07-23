# CLAUDE.md — AntWorks-RL

Guidance for Claude working in this repository.

This is a living document: seeded early and formalized in Lesson 0.6. Keep it honest. Document conventions the code actually follows today, and label planned work as vision/roadmap.

## What this project is
AntWorks-RL is a biologically-grounded, multi-agent RL ant-colony simulation where ant behaviour is **learned** (not scripted) and colony intelligence emerges from learned stigmergy.

Current status: Foundation (Phase 0) is complete; the full simulation starts in Phase 1.

References:
- `learning/learning-records/0002-locked-design-decisions.md` for locked design decisions.
- `learning/ROADMAP.md` for current phase and lesson.

## ⚠️ Teaching mode — the most important rule
This is a **learning project**. The user writes ALL project code themselves, one lesson at a time, via the `/teach` loop in `learning/`.

- **Do NOT implement lessons, features, or exercises for the user.** Teach, explain, review, and coach instead.
- When the user is mid-lesson, your job is feedback and hints — never the finished answer.
- Exceptions (things Claude may author): the `learning/` teaching workspace, `.claude/` commands, and this file.
- To advance a lesson use the `/next-lesson` command; to refresh docs use `/update-docs`.

## Locked toolchain (do not substitute without the user's say-so)
- **Package/deps**: `uv` (lockfile committed). **Python** ≥ 3.12.
- **Lint/format**: `ruff`. **Type checker**: `ty`.
- **Config**: `Hydra` (compose/CLI/sweeps) + `Pydantic` (typed validation of the composed config).
- **Tests**: `pytest` + `hypothesis` (property-based invariants).
- **RL**: `PyTorch`; custom MAPPO is the from-scratch centrepiece; `PettingZoo` Parallel API is the env contract; `RLlib` is the second Trainer backend.
- **Logging**: stdlib `logging` + `structlog` (JSON in prod) + `rich` (dev). **Metrics/experiments**: Weights & Biases (behind a logger interface; TensorBoard fallback).
- **Persistence**: `SQLite` via a repository layer (SQLModel) for persistent-mode history + per-ant event log.

## Conventions (formalized in Lesson 0.6)
- **Docs track reality**: describe what exists today; clearly label vision/future work.
- **Package and layout**: project package name is `antworks_rl`; source code lives in `src/antworks_rl/`; tests target the installed package API, not ad-hoc path hacks.
- **Toolchain and quality gates**: use `uv` for env/deps/commands, `ruff` for lint and format, and `ty` for type checking; in CI, lint, format-check, type-check, and tests all run and are required to pass.
- **Config spine**: Hydra composes configuration from `src/conf/`; Pydantic validates the composed config object; config groups are first-class (for example `logging=debug`); Hydra relative `config_path` behavior is module-relative and depends on `conf/__init__.py` existing.
- **Reproducibility**: all stochastic behavior must use injected, seeded RNG instances; do not use global `random` or global `np.random` state.
- **Logging**: logging is structured and config-driven (renderer/level selected by config); event names plus key-value fields are preferred over free-form log text; Hydra owns root logging setup, so application logging setup should force handler configuration to avoid collisions.
- **Test layout**: test modules stay flat under `tests/` with unique basenames; avoid nested test packages that can shadow stdlib names (for example `logging`) or create import-mismatch collisions.
- **Forward-looking sim conventions (for Phase 1+)**: sim/render decoupling (headless sim, serializable snapshots for renderers); episode boundaries belong in wrappers/runners, not the sim core.

## Where things live
- `learning/` — the teaching workspace (MISSION, ROADMAP, GLOSSARY, RESOURCES, learning-records, explainers). Terminology follows `learning/GLOSSARY.md`.
- `src/antworks_rl/` — the package (as it grows, lesson by lesson).
- `.claude/commands/` — repo-local `/next-lesson` and `/update-docs`.

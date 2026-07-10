# CLAUDE.md — AntWorks-RL

Guidance for Claude working in this repository. This is a **living document**: it is seeded early and formalized in Lesson 0.6. Keep it honest — document conventions the code actually follows, not aspirations.

## What this project is
AntWorks-RL is a biologically-grounded, multi-agent RL ant-colony simulation where ant behaviour is **learned** (not scripted) and colony intelligence **emerges** from learned stigmergy. See `learning/learning-records/0002-locked-design-decisions.md` for the full locked design and `learning/ROADMAP.md` for current phase/lesson.

## ⚠️ Teaching mode — the most important rule
This is a **learning project**. The user writes ALL project code themselves, one lesson at a time, via the `/teach` loop in `learning/`.

- **Do NOT implement lessons, features, or exercises for the user.** Teach, explain, review, and coach instead.
- When the user is mid-lesson, your job is feedback and hints — never the finished answer.
- Exceptions (things Claude may author): the `learning/` teaching workspace, `.claude/` commands, and this file.
- To advance a lesson use the `/next-lesson` command; to refresh docs use `/update-docs`.

## Locked toolchain (do not substitute without the user's say-so)
- **Package/deps**: `uv` (lockfile committed). **Python** ≥ 3.12.
- **Lint/format**: `ruff`. **Type checker**: `ty` (Astral; beta → non-blocking in CI, mypy/pyright are the fallback).
- **Config**: `Hydra` (compose/CLI/sweeps) + `Pydantic` (typed validation of the composed config).
- **Tests**: `pytest` + `hypothesis` (property-based invariants).
- **RL**: `PyTorch`; custom MAPPO is the from-scratch centrepiece; `PettingZoo` Parallel API is the env contract; `RLlib` is the second Trainer backend.
- **Logging**: stdlib `logging` + `structlog` (JSON in prod) + `rich` (dev). **Metrics/experiments**: Weights & Biases (behind a logger interface; TensorBoard fallback).
- **Persistence**: `SQLite` via a repository layer (SQLModel) for persistent-mode history + per-ant event log.

## Conventions (grow this list through Phase 0; formalize in 0.6)
- **src-layout**: code in `src/antworks_rl/`; tests exercise the installed package.
- **Reproducibility**: every stochastic component draws from an **injected, seeded RNG**; the seed comes from config. No global `random`/`np.random`.
- **Sim/render decoupling**: the simulation is headless; it emits a serializable `StateSnapshot` that renderers consume. Never couple sim logic to a renderer.
- **Episode boundaries live in the runner/wrapper, not the sim core** (enables persistent mode).
- **Docs track reality**: never document unimplemented features as if they exist; intent goes in clearly-labelled vision/roadmap sections only.

## Where things live
- `learning/` — the teaching workspace (MISSION, ROADMAP, GLOSSARY, RESOURCES, learning-records, explainers). Terminology follows `learning/GLOSSARY.md`.
- `src/antworks_rl/` — the package (as it grows, lesson by lesson).
- `.claude/commands/` — repo-local `/next-lesson` and `/update-docs`.

# AntWorks-RL

Learned multi-agent ant-colony simulation, built lesson-by-lesson as a production-grade RL project.

> **Status: Phase 0 (foundation) complete - not yet a runnable simulation.**
> The toolchain, config spine, logging, and test harness are in place.
> The ant simulation itself starts in Phase 1.

## What Works Today

- Installable Python package: `antworks_rl` (CLI entrypoint: `antworks-rl`).
- Config composition with Hydra and typed validation with Pydantic.
- Structured, config-driven logging via `structlog`.
- Lint, format, type, and test gates wired locally and in CI.

## Quickstart

### 1) Sync dependencies

```bash
uv sync --dev
```

### 2) Run the current CLI

```bash
uv run antworks-rl
```

Current behavior (today):
- Loads config from `src/conf/config.yaml` (plus config group defaults).
- Validates the composed config with Pydantic.
- Configures logging and emits a startup log line with the seed.

### 3) Run tests

```bash
uv run pytest
```

### 4) Run quality gates

```bash
uv run ruff check .
uv run ruff format --check .
uv run ty check .
```

## Useful Overrides

Hydra overrides can be passed on the CLI:

```bash
uv run antworks-rl logging=debug run_name=local-dev seed=42
```

## Vision (Where This Is Going)

AntWorks-RL is designed to become a biologically-grounded, multi-agent RL ant-colony simulation where colony intelligence emerges from learned stigmergy rather than scripted behavior.

Planned milestones include:
- Headless simulation core with seeded reproducibility and invariants.
- Renderer and observability improvements.
- PettingZoo environment integration.
- Custom MAPPO training, baselines, and experiment tracking.
- Multi-colony dynamics and persistent mode.

See `learning/ROADMAP.md` for the authoritative phase-by-phase plan.

## Project Layout

```text
src/antworks_rl/   # package code
src/conf/          # Hydra config root and config groups
tests/             # flat test modules
learning/          # lesson material, explainers, learning records, roadmap
```

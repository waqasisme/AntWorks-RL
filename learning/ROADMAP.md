# AntWorks-RL Learning Roadmap

The course. 11 dependency-ordered phases; each decomposes into lesson-sized `/teach` units. **Near-term phases (0–1) are decomposed now; later phases stay as outlines and are decomposed just-in-time** so they adapt to what you actually built.

Every lesson follows the same loop: **knowledge** (HTML explainer, grounded in [[RESOURCES.md]]) → **skill** (you code it) → **feedback** (review + tests) → **references** (deep-dive links) → graduate terms into [[GLOSSARY.md]].

Legend: ⬜ not started · 🟦 in progress · ✅ done

---

## Phase 0 — Foundation (lean production-Python scaffold)
*Goal: a modern, typed, tested, config-driven repo skeleton. Learn the Astral toolchain + project hygiene.*

- ✅ **0.1 — Modern Python scaffolding**: `uv` project, src-layout, `pyproject.toml`, dependency groups. *Deliverable: installable `antworks_rl` package.*
- 🟦 **0.2 — Lint/format/type gates**: `ruff` + `ty`, pre-commit hooks, editor integration.
- ⬜ **0.3 — Config spine**: Hydra composition + Pydantic validation; a `Config` object loaded from YAML with a CLI override.
- ⬜ **0.4 — Test + CI harness**: `pytest` layout, first `hypothesis` test, GitHub Actions running lint/type/test.
- ⬜ **0.5 — Logging**: stdlib `logging` + `structlog` (JSON) + `rich` console, level driven by config.
- ⬜ **0.6 — Docs that lead the code**: *formalize* the seeded `CLAUDE.md` with the conventions established across 0.1–0.5, and write a lean, honestly-labelled `README.md` (vision + status banner + roadmap pointer). *CLAUDE.md seeded at repo root already; ARCHITECTURE.md intentionally deferred to end of Phase 1.*

## Phase 1 — Core simulation (headless, NO RL)
*Goal: a correct, seeded, serializable world with scripted ants. Learn clean sim design, numpy vectorization, invariant testing.*

- ⬜ **1.1 — Grid & entities**: world grid, ant/food/nest entities, stable per-ant IDs, injected seeded RNG.
- ⬜ **1.2 — Movement & occupancy**: 8-dir moves, per-cell occupancy caps, collisions/jostling.
- ⬜ **1.3 — Energy & metabolism**: per-ant energy, consumption, death; conservation bookkeeping.
- ⬜ **1.4 — Pheromone field**: 5-channel deposit / evaporate / diffuse math (the stigmergy substrate); non-negativity + decay invariants.
- ⬜ **1.5 — Weather model**: stochastic Markov weather + seasons, fully config-seeded.
- ⬜ **1.6 — StateSnapshot & serialization**: render-agnostic snapshot; full-world save/load round-trip test.
- ⬜ **1.7 — Scripted ants + invariants**: random/scripted policy to exercise mechanics; `hypothesis` conservation-law suite (food, population, pheromone).

## Phase 2 — Visualization (pygame)
*Goal: watch it. Learn decoupled rendering.* → Renderer seam, pygame viewer, pheromone overlays, weather dials, pause/step/speed, zoom, click-to-inspect. **Motivation payoff before any RL.**

## Phase 3 — RL environment (PettingZoo)
*Goal: a spec-compliant learnable env.* → obs/action spaces, hybrid reward (potential-based shaping + colony term), episode wrapper, `parallel_api_test` in CI.

## Phase 4 — Custom MAPPO (the centrepiece)
*Goal: implement MARL from scratch.* → actor/critic nets, parameter sharing, rollout buffer, GAE, PPO-clip, **centralized critic (CTDE)**, training loop, W&B. First learning run on a trivial task.

## Phase 5 — IPPO baseline + benchmark harness
*Goal: your first real result.* → ablate the centralized critic; MAPPO-vs-IPPO curves. Learn experimental rigor.

## Phase 6 — Richer biology + scale-up
*Goal: emergent foraging.* → castes, emergent task allocation, trophallaxis, curriculum + domain-randomized weather, reward debugging, scale from ~20–50 ants upward.

## Phase 7 — RLlib integration
*Goal: industrial tooling.* → `RLlibTrainer` backend via the Trainer protocol; compare against custom MAPPO.

## Phase 8 — Rival species / multi-colony
*Goal: competitive MARL.* → second species trait-profile, combat, colony-identity pheromone, mixed/competitive training.

## Phase 9 — Persistent mode + web viewer + hosting
*Goal: the living colony.* → continuous run loop, SQLite history, web dashboard, deploy.

## Phase 10 — Evolutionary outer loop (Alife stretch)
*Goal: colonies that literally evolve.* → PBT / GA over trait-configs; morphology co-adapting to environment & rivals.

## Phase N — Narrative flavour
*Goal: RimWorld/DF texture.* → ant life-stories generated from the event log.

---

### Documentation & drift cadence (standing practice — repo-local, NOT cdm-corgi)
- `CLAUDE.md` + `README.md` are born in **Lesson 0.6** and updated in-lesson as conventions/quickstart change.
- `ARCHITECTURE.md` is first written at the **end of Phase 1**, when real structure exists.
- **Deterministic guard**: a `scripts/check_docs.py` (coded as a lesson) verifies structural claims — module map matches `src/antworks/`, documented commands exist, config examples validate against the Pydantic schema — and runs in CI (wired once CI exists in 0.4).
- **Prose refresh**: run the repo-local `/update-docs` command at **every phase boundary** for the semantic drift a script can't judge.
- **Advancing lessons**: run the repo-local `/next-lesson` command (or ping in chat) to review the finished exercise and unlock the next lesson.
- We deliberately do **not** use the cdm-corgi `architecture-*` / `drift-*` agents — those are work-team-specific.

### How we track progress
- This file's checkboxes are the source of truth for *where we are*.
- Decision-grade insights land in `learning-records/`.
- Understood terms graduate into `GLOSSARY.md`.
- Each completed lesson leaves a saved HTML explainer in `learning/explainers/`.

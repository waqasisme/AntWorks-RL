# Locked design decisions (from the design interview)

The design tree resolved during the `/grill-me` session. These are settled; teach *within* them. (Fuller narrative lives in the project's future ARCHITECTURE.md.)

## Paradigm & world
- **Paradigm A**: learned per-ant policies; colony intelligence *emerges* from learned stigmergy. Research framing: "can learned policies reproduce/exceed emergent foraging?"
- Grid world, 8-dir + stay, per-cell occupancy caps. Realism budget → pheromone chemistry + behavioural state, **not** locomotion physics.
- 5 pheromone channels: food-trail, home-trail, alarm, colony-identity, repellent.

## Agent interface
- **Obs** (egocentric, local): local patches of all 5 channels + food/obstacle/nest/density, internal state (energy, health, carrying, caste/task one-hot, age), noisy path-integration home vector (degrades in dark/rain), weather scalars.
- **Action** (MultiDiscrete): move-9, deposit-channel-6, deposit-strength-4 (graded recruitment), interact-6 (pickup/drop/eat/attack/trophallaxis/none). Communication = pheromones + contact verbs; learned-symbol language = deferred stretch.

## Learning
- **Hybrid reward**: potential-based individual shaping + shared colony term + **centralized critic (CTDE)**. Colony-size / life-expectancy are **metrics, not rewards** (Goodhart).
- Fixed-horizon "season" episodes, in-episode birth/death; domain-randomized stochastic weather + curriculum.
- Castes: birth-assigned morphological trait (sensed) + emergent behavioural role via one caste-conditioned policy per species; queen = env entity.
- v1 = RL learning + behavioural flexibility only (labelled honestly). Evolutionary outer loop = Phase-10 stretch; trait-configs built now so it's cheap later.

## Framework & infra
- PyTorch; custom MAPPO centrepiece; **PettingZoo** env contract; shared env/config/eval/logging + thin two-backend **Trainer protocol** (custom + RLlib); **IPPO-vs-MAPPO** first benchmark.
- Species = config-driven trait profiles; multi-colony-capable from day one (single colony = N=1).
- Config: **Hydra** (compose/CLI/sweeps) + **Pydantic** (typed validation). Deps: **uv**. Lint/format: **ruff**. Types: **ty**. Tests: **pytest** + **hypothesis**. Seed from config, injected RNG everywhere.
- Logging: stdlib `logging` + `structlog` (JSON prod) + `rich` (dev). Metrics: **W&B** primary + TensorBoard fallback, behind a logger interface.
- **SQLite** (repository layer, SQLModel) = persistent-mode history + per-ant event log (narrative hooks).

## Runtime, viz, persistence
- Sim/render decoupled: `Env → StateSnapshot → Renderer{pygame | web | video}`. Headless training; pygame viewer first, web viewer later (hosted persistent colony).
- Episode boundaries live in the runner/wrapper, **not** the sim core (enables persistent mode). Full-world save/load serialization. Stable per-ant IDs + event log now; narrative generation later.

## Testing
- Seeded determinism → unit (mechanics) + hypothesis invariants (conservation laws) + PettingZoo `api_test` in CI; learning smoke + seeded-rollout regression gated/nightly.

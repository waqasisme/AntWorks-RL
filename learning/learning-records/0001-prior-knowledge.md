# Prior knowledge established (baseline)

The user is an experienced engineer, not a beginner. Do not re-teach these; pitch lessons above them.

- **Python**: Strong. Knows how to code in Python well. The gap is *modern production-grade tooling/practice* (uv, ruff, ty, Hydra+Pydantic, src-layout, typed config, property-based testing), not the language.
- **RL/MARL**: Prior hands-on experience with **Stable-Baselines3** and **MAPPO/MARL** conceptually. Understands agents/environments/training pipelines. The goal is *depth* — implementing MAPPO from scratch — not first exposure.
- **New/target tooling this project introduces**: RLlib, PettingZoo, Hydra, `uv`/`ruff`/`ty`, W&B, `hypothesis`.

## Evidence
Demonstrated strong conceptual grip during the design interview: independently raised the domain-randomization concern (fixed season order → policy memorizes the clock), intuited a Goodhart-style objection (metrics vs rewards), and correctly pushed back on continuous locomotion physics being irrelevant to colony-level behaviour.

## Implications
- ZPD entry point is *modern Python project setup* (Phase 0) and *clean simulation design* (Phase 1), then straight into from-scratch MARL. Skip RL-101 and Python-101.

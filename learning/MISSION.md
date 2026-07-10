# Mission: Learn modern production Python + MARL by building AntWorks-RL

## Why
Build a portfolio-grade, biologically-grounded ant-colony simulation where ant behaviour is *learned* via multi-agent RL, in order to (a) deeply understand MARL by implementing MAPPO from scratch, (b) sharpen modern production-grade Python, and (c) ship a distinctive, watchable, hostable artifact for a CV. The learning is the point: the user writes the code, one lesson at a time.

## Success looks like
- Can implement MAPPO from scratch (actor/critic, parameter sharing, GAE, PPO-clip, centralized critic / CTDE) and explain *why* the centralized critic matters, evidenced by an IPPO-vs-MAPPO benchmark.
- Can design a clean, tested, config-driven MARL codebase: PettingZoo env, Hydra+Pydantic config, `uv`/`ruff`/`ty`, `pytest`+`hypothesis`, W&B.
- Can articulate the biology → mechanism → RL mapping (stigmergy, response-threshold task allocation, graded recruitment) and defend design choices on scientific grounds.
- Ships emergent foraging from learned policies, then rival species, then a hosted persistent colony.

## Constraints
- **User codes everything, guided lesson-by-lesson via `/teach`.** Claude teaches and reviews; it does not build the project.
- Prior experience: strong Python, SB3, MAPPO/MARL concepts (see [[learning-records/0001-prior-knowledge]]). Do not re-teach basics.
- Lessons must be small (ZPD-tight) and each ends with curated deep-dive references (Python / ML / RL / ant biology).
- Toolchain is locked (see [[learning-records/0002-locked-design-decisions]]); teach within it.

## Out of scope (for now)
- Front-end/web viewer engineering (Phase 9 — deferred).
- Literal evolutionary/genetic outer loop (Phase 10 — deferred).
- Narrative/story generation (Phase N — only the data hooks are built early).
- Continuous-control locomotion physics (deliberately excluded; realism budget goes to pheromone chemistry + behaviour).

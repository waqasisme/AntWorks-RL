# AntWorks-RL Resources

Curated, high-trust sources grounding the teaching. Explainers draw knowledge from here — not from parametric guesses.

## Knowledge — Reinforcement Learning

- [OpenAI Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/) ([code](https://github.com/openai/spinningup))
  The canonical educational bridge from RL theory to implementation. Use for: policy gradients, PPO, GAE, actor-critic intuition before writing MAPPO.
- [MAPPO paper — "The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games" (Yu et al., NeurIPS 2022)](https://arxiv.org/abs/2103.01955) ([project site](https://sites.google.com/view/mappo), [BAIR blog](https://bair.berkeley.edu/blog/2021/07/14/mappo/))
  Primary source for the centerpiece algorithm. Use for: centralized critic design, parameter sharing, the five implementation tricks that make MAPPO work.
- [MAPPO official implementation (marlbenchmark/on-policy)](https://github.com/marlbenchmark/on-policy)
  Reference code to check your from-scratch MAPPO against. Use for: sanity-checking the buffer, GAE, and critic input construction.
- [Sutton & Barto, *Reinforcement Learning: An Introduction* (2nd ed., free PDF)](http://incompleteideas.net/book/the-book-2nd.html)
  The foundational textbook. Use for: value functions, TD, advantage, the vocabulary underneath everything.

## Knowledge — MARL Tooling

- [PettingZoo documentation](https://pettingzoo.farama.org/) — [Parallel API](https://pettingzoo.farama.org/api/parallel/) — [paper](https://arxiv.org/abs/2009.14471)
  The env-contract standard. Use for: env API shape, `parallel_api_test`, wrapping conventions.
- [Ray RLlib documentation](https://docs.ray.io/en/latest/rllib/index.html) — [Multi-agent envs](https://docs.ray.io/en/latest/rllib/rllib-env.html)
  Industrial MARL library for the second `Trainer` backend. Use for: Phase 7 RLlib integration and the MAPPO-vs-library benchmark.
- [Using PettingZoo with RLlib (Jordan Terry)](https://medium.com/data-science/using-pettingzoo-with-rllib-for-multi-agent-deep-reinforcement-learning-5ff47c677abd)
  Bridge tutorial. Use for: plugging the AntWorks env into RLlib without an adapter rewrite.

## Knowledge — Modern Production Python

- [uv documentation (Astral)](https://docs.astral.sh/uv/) ([repo](https://github.com/astral-sh/uv))
  The package/project manager. Use for: project init, dependency groups, lockfile, reproducible envs.
- [Ruff documentation](https://docs.astral.sh/ruff/)
  Linter + formatter. Use for: lint rule selection, format-on-save, pre-commit config.
- [ty documentation (Astral type checker)](https://docs.astral.sh/ty/)
  The chosen (beta) type checker. Use for: local typechecking; note maturity caveat — mypy/pyright are the drop-in fallback.
- [Hydra documentation](https://hydra.cc/)
  Hierarchical config composition + multirun sweeps. Use for: the config-driven pipeline and MAPPO-vs-IPPO sweeps.
- [Pydantic documentation](https://docs.pydantic.dev/)
  Runtime-validated typed models. Use for: validating composed Hydra configs into typed objects.
- [Hypothesis documentation](https://hypothesis.readthedocs.io/)
  Property-based testing. Use for: conservation-law invariants over random rollouts.
- [structlog documentation](https://www.structlog.org/en/stable/) — [Standard Library Logging integration](https://www.structlog.org/en/stable/standard-library.html)
  Structured logging with pluggable processors/renderers. Use for: JSON logs in prod, `ConsoleRenderer` in dev, routing through stdlib `logging` so third-party libraries' log records are captured too.
- [Rich documentation — Logging Handler](https://rich.readthedocs.io/en/stable/logging.html) ([reference](https://rich.readthedocs.io/en/stable/reference/logging.html))
  `RichHandler` for colorized, columnar console log output. Use for: the dev-console renderer wired in Lesson 0.5.

## Knowledge — Ant Biology (the science we honour)

- [Deborah M. Gordon, *Ant Encounters: Interaction Networks and Colony Behavior* (Princeton)](https://press.princeton.edu/books/paperback/9780691138794/ant-encounters)
  Modern, systems-view account of task allocation via interaction rate. Use for: why "task allocation" ≠ "division of labour", and emergent role-switching.
- [Hölldobler & Wilson, *Journey to the Ants* / *The Ants*](https://www.hup.harvard.edu/books/9780674485266)
  Foundational natural history of ant communication and castes. Use for: pheromone types, caste morphology, trophallaxis, species diversity.
- [Evolution of self-organised division of labour driven by stigmergy in leaf-cutter ants (*Scientific Reports*, 2022)](https://www.nature.com/articles/s41598-022-26324-6)
  Primary research linking stigmergy → division of labour. Use for: grounding the emergent-task-allocation claim.
- [Response thresholds alone cannot explain empirical patterns of division of labor (*PLOS Biology*, 2021)](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001269)
  Critical view of the response-threshold model. Use for: not over-claiming; nuance for the caste/task design.

## Wisdom (Communities)

- [r/reinforcementlearning](https://reddit.com/r/reinforcementlearning)
  Use for: MAPPO/CTDE implementation troubleshooting, reward-design critique.
- [Farama Foundation Discord](https://farama.org/) (PettingZoo/Gymnasium)
  Use for: env-API edge cases, library-specific questions.
- [Ray Slack / Discourse](https://discuss.ray.io/)
  Use for: RLlib multi-agent configuration help (Phase 7).
- [r/artificial / Alife & complex-systems communities](https://reddit.com/r/artificial)
  Use for: emergence, stigmergy, and the eventual evolutionary loop (Phase 10).

## Gaps
- No single trusted source combines *learned* (RL) ant policies with biological stigmergy — this project sits in that gap, which is precisely its novelty. Watch for recent arXiv work on "learned stigmergy" / "neural swarm foraging" to fill in as it appears.

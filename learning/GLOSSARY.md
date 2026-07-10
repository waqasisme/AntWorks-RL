# AntWorks-RL Glossary

Canonical language for the project. All explainers, roadmap entries, and code should adhere to these terms. Terms are added here only once the user has demonstrated understanding; freshly-introduced concepts live in explainers until they graduate.

## Reinforcement Learning

**MARL (Multi-Agent Reinforcement Learning)**:
RL where multiple agents learn policies while sharing an environment, so each agent's optimal behaviour depends on the others'.
_Avoid_: multi-bot RL

**MAPPO (Multi-Agent PPO)**:
PPO adapted to cooperative MARL, typically with a centralized critic and parameter sharing. The project's from-scratch centrepiece.

**CTDE (Centralized Training, Decentralized Execution)**:
Training regime where the critic sees global state (centralized) but each agent acts from only its own local observation (decentralized). The mechanism that makes credit assignment tractable.
_Avoid_: shared-brain training

**Centralized critic**:
A value function that conditions on global state during training, used to reduce variance and assign credit that a per-agent local critic cannot. The single difference between IPPO and MAPPO.

**IPPO (Independent PPO)**:
Every agent runs PPO with its own *decentralized* critic, treating others as part of the environment. Serves as the baseline that isolates the value of the centralized critic.

**Parameter sharing**:
One policy network whose weights are shared across many homogeneous agents; each agent still acts on its own observation. Lets one policy scale to thousands of ants.

**Potential-based reward shaping**:
Adding a shaping term derived from a potential function so that the optimal policy is provably unchanged — dense guidance without distorting the true objective.

**Domain randomization**:
Randomizing environment parameters (here: weather schedule, severity, spawn) across episodes so the policy learns to *respond to sensed conditions* rather than memorize a fixed schedule.

**Goodhart failure (reward hacking)**:
When optimizing a proxy metric produces degenerate behaviour that scores well but violates intent (e.g. rewarding life-expectancy → ants that hide and never forage). Reason metrics ≠ rewards.

## Simulation & Biology

**Stigmergy**:
Indirect coordination in which agents modify a shared environment (pheromone field) and others respond to those modifications, producing a positive-feedback loop — the substrate of emergent colony intelligence.

**Emergence**:
Colony-level behaviour (trails, task allocation, defence) that arises from many simple local agent interactions rather than being programmed centrally.

**Graded recruitment**:
Real ants modulate *how much* trail pheromone they deposit based on food quality/assessment; this graded positive feedback (checked by evaporation) is how a colony collectively chooses between food sources. Modelled by the deposit-strength action head.

**Response-threshold model**:
Model of division of labour where an ant performs a task once its associated stimulus exceeds that ant's personal threshold; performing the task lowers the stimulus. A target *emergent* behaviour, not something to script.

**Task allocation**:
The dynamic, decentralized assignment of which worker does which job right now (forage/nurse/defend). Preferred (per Gordon) over "division of labour" for the dynamic behavioural axis.
_Avoid_: division of labour (reserve for the morphological/caste axis)

**Path integration**:
An ant's continuously-updated internal estimate of the direction+distance home; modelled as a noisy "home vector" observation that degrades in dark/rain.

**Caste (morphological)**:
A birth-assigned body type with distinct traits (minor / major-soldier / queen), sensed in the observation. Distinct from dynamic task allocation.

## Engineering

**PettingZoo Parallel API**:
The Farama-Foundation standard MARL environment interface where all agents step simultaneously via per-agent observation/reward dicts. The project's env contract; enables algorithm-agnostic benchmarking.

**StateSnapshot**:
A serializable, render-agnostic description of world state emitted each step; decouples the headless simulation from any renderer (pygame / web / video).

**Trainer protocol**:
A thin interface (`setup / train_iteration / evaluate / checkpoint`) with two backends — custom-MAPPO and RLlib — so the same env/config/eval powers a fair benchmark.

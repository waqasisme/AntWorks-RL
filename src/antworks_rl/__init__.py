# entrypoint
import hydra
import numpy as np
from omegaconf import DictConfig, OmegaConf
from pydantic import BaseModel

from antworks_rl.constants import ANT_EMOJI
from antworks_rl.logging import LoggingConfig, setup_logging
from antworks_rl.world import WorldConfig, make_world


class Config(BaseModel):
    seed: int
    run_name: str
    logging: LoggingConfig
    world: WorldConfig


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: DictConfig) -> None:
    config = Config.model_validate(OmegaConf.to_container(cfg, resolve=True))
    log = setup_logging(config.logging)

    log.info(
        f"{ANT_EMOJI}{ANT_EMOJI}{ANT_EMOJI}Starting AntWorks RL "
        f"{ANT_EMOJI}{ANT_EMOJI}{ANT_EMOJI} seed: {config.seed}"
    )
    log.debug(f"Configuration: {config.model_dump()}")

    log.info("Initializing world...")
    make_world(config.world, rng=np.random.default_rng(config.seed))
    log.info("World initialized successfully.")


__version__ = "0.1.0"

# entrypoint
import hydra
from omegaconf import DictConfig, OmegaConf
from pydantic import BaseModel


class LoggingConfig(BaseModel):
    level: str = "INFO"


class Config(BaseModel):
    seed: int
    run_name: str
    logging: LoggingConfig


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: DictConfig) -> None:
    config = Config.model_validate(OmegaConf.to_container(cfg, resolve=True))
    print(config)


__version__ = "0.1.0"

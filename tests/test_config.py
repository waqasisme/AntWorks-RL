import pytest
from hydra import compose, initialize
from hydra.core.global_hydra import GlobalHydra
from omegaconf import OmegaConf
from pydantic import ValidationError

from antworks_rl import Config


def test_config_loads_and_validates():
    GlobalHydra.instance().clear()  # reset Hydra state
    with initialize(version_base=None, config_path="../src/conf"):
        cfg = compose(config_name="config")
        config = Config(**OmegaConf.to_container(cfg, resolve=True))  # type: ignore
    assert config.seed == 0
    assert isinstance(config.run_name, str)


def test_config_rejects_bad_type():
    GlobalHydra.instance().clear()
    with initialize(version_base=None, config_path="../src/conf"):
        cfg = compose(config_name="config", overrides=["logging.level=123"])
        with pytest.raises(ValidationError):
            Config(**OmegaConf.to_container(cfg, resolve=True))  # type: ignore

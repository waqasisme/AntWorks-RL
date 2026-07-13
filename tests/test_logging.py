import json
import logging

import pytest

from antworks_rl.logging import LoggingConfig, setup_logging


@pytest.fixture(autouse=True)
def reset_logging():
    """Keep global logging state from leaking between tests."""
    yield
    root = logging.getLogger()
    for h in root.handlers[:]:
        root.removeHandler(h)


def test_json_renderer_round_trips(capsys):
    log = setup_logging(LoggingConfig(renderer="json", level="INFO"))
    log.info("ant_spawned", ant_id=7)
    err = capsys.readouterr().err
    parsed = json.loads(err.splitlines()[0])
    assert parsed["event"] == "ant_spawned"
    assert parsed["ant_id"] == 7
    assert parsed["level"] == "info" and "timestamp" in parsed


def test_level_filtering(capsys):
    log = setup_logging(LoggingConfig(renderer="json", level="INFO"))
    log.debug("ant_debug", ant_id=7)
    log.info("ant_info", ant_id=7)
    err = capsys.readouterr().err
    assert "ant_debug" not in err
    assert "ant_info" in err
    log = setup_logging(LoggingConfig(renderer="json", level="DEBUG"))
    log.debug("ant_debug", ant_id=7)
    err = capsys.readouterr().err
    assert "ant_debug" in err

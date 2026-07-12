import numpy as np


def make_rng(seed: int) -> np.random.Generator:
    """Create a random number generator with a given seed.

    Args:
        seed: An integer seed for the random number generator.

    Returns:
        A numpy random number generator instance.
    """
    return np.random.default_rng(seed)

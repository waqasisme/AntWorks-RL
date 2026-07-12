import numpy as np

from antworks_rl.rng import make_rng


def test_rng():
    seed = 42
    rng1 = make_rng(seed)
    rng2 = make_rng(seed)

    # Generate some random numbers and check if they are the same
    random_numbers1 = rng1.random(5)
    random_numbers2 = rng2.random(5)

    assert np.array_equal(random_numbers1, random_numbers2), (
        "RNGs with the same seed should produce the same output"
    )

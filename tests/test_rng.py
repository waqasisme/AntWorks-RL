import numpy as np
from hypothesis import given
from hypothesis import strategies as st

from antworks_rl.rng import make_rng


@given(st.integers(min_value=0), st.integers(min_value=0))
def test_rng_with_hypothesis(seed: int, another_seed: int):
    rng1 = make_rng(seed)
    rng2 = make_rng(another_seed)

    # Generate some random numbers and check if they are the same
    random_numbers1 = rng1.random(5)
    random_numbers2 = rng2.random(5)

    if seed == another_seed:
        assert np.array_equal(random_numbers1, random_numbers2), (
            "RNGs with the same seed should produce the same output"
        )
    else:
        assert not np.array_equal(random_numbers1, random_numbers2), (
            "RNGs with different seeds should produce different outputs"
        )

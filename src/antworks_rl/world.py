from dataclasses import dataclass, field
from typing import Self

import numpy as np
from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt, model_validator


class WorldConfig(BaseModel):
    width: PositiveInt = Field(default=100, le=1024)
    height: PositiveInt = Field(default=100, le=1024)
    n_ants: PositiveInt = Field(default=50, le=10_000)
    n_food: NonNegativeInt = Field(default=30)
    occupancy_cap: PositiveInt = Field(default=3, le=8)

    @model_validator(mode="after")
    def check_ants_fit(self) -> Self:
        if self.n_ants > self.width * self.height * self.occupancy_cap:
            raise ValueError("Number of ants exceeds the maximum occupancy of the grid.")

        return self


@dataclass
class World:
    """
    The world is a 2D grid of cells. Each cell can be empty or contain food.
    Ants can move around the grid and collect food.
    """

    # config driven
    width: int
    height: int
    occupancy_cap: int
    ant_alive: np.ndarray = field(repr=False)
    # randomized
    nest_location: tuple[int, int] = field(repr=True)
    ant_positions: np.ndarray = field(repr=False)
    food: np.ndarray = field(repr=False)
    # computed
    ant_ids: np.ndarray = field(init=False, repr=False)
    _id_to_row: dict[int, int] = field(init=False, repr=False)
    next_ant_id: int = field(init=False, repr=True, compare=False)

    def __post_init__(self):
        if len(self.ant_alive) > self.width * self.height * self.occupancy_cap:
            raise ValueError("Provided number of ants exceeds the maximum occupancy of the grid.")

        self.ant_ids = np.arange(len(self.ant_alive), dtype=np.int64)
        self.next_ant_id = int(self.ant_ids[-1]) + 1 if len(self.ant_ids) else 0
        self._id_to_row = {int(ant_id): i for i, ant_id in enumerate(self.ant_ids)}

    def issue_next_ant_id(self) -> int:
        """
        Get a new ant ID and increment the next_ant_id counter.
        """
        next_id = self.next_ant_id
        self.next_ant_id += 1
        return next_id

    def __repr__(self) -> str:
        return (
            f"World(width={self.width}, height={self.height}, occupancy_cap={self.occupancy_cap}, "
            f"nest_location={self.nest_location}, "
            f"n_ants={len(self.ant_alive)}(alive={np.sum(self.ant_alive)}), "
            f"n_food={np.sum(self.food)})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, World):
            return False
        return (
            self.width == other.width
            and self.height == other.height
            and self.occupancy_cap == other.occupancy_cap
            and self.nest_location == other.nest_location
            and np.array_equal(self.ant_alive, other.ant_alive)
            and np.array_equal(self.food, other.food)
            and np.array_equal(self.ant_positions, other.ant_positions)
        )

    __hash__ = object.__hash__


def make_world(config: WorldConfig, rng: np.random.Generator) -> World:
    """
    Initialize the world with random food and ant positions.
    """

    # TODO: decide later if food can stack in the same cell or not. For now, we will assume it can't
    food_locations = rng.choice(config.width * config.height, size=config.n_food, replace=False)
    food = np.zeros((config.width, config.height), dtype=np.int32)
    x, y = np.unravel_index(food_locations, (config.width, config.height), order="C")
    food[x, y] = 1

    ant_locations = rng.choice(
        config.width * config.height * config.occupancy_cap, size=config.n_ants, replace=False
    )
    x, y, _ = np.unravel_index(
        ant_locations, (config.width, config.height, config.occupancy_cap), order="C"
    )
    ant_positions = np.stack((x, y), axis=-1).astype(np.int32)

    nest_location = (
        rng.integers(0, config.width, dtype=int),
        rng.integers(0, config.height, dtype=int),
    )

    return World(
        width=config.width,
        height=config.height,
        occupancy_cap=config.occupancy_cap,
        ant_alive=np.ones(config.n_ants, dtype=bool),
        food=food,
        nest_location=nest_location,
        ant_positions=ant_positions,
    )

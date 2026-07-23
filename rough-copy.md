### occupancy-caps

- do we want different occupancy caps based on terrain type? do we want terrain types?
- what should be the max_occupancy_cap? 8 seems reasonable, but maybe we want to allow more for certain terrain types (like a nest) and less for others (like a narrow tunnel).

#### nest
- does the nest occupy a slot? is it terrain? an ant? how many ants can come to the nest? is the nest just one slot?


### n_food

- how much food can accumulate in the grid? how is food produced? how much can be stacked on one cell in the grid?
- Stacking reasons: windfall, storage, surplus, etc.


### ids / queen
- is queen one of the ants? is she always id 0? is she a special ant with special behavior? is she a separate entity from the ants? if so, how do we model her? if not, how do we model her?
- is queen location always the nest location? i think it should be, but maybe we want to allow the queen to move around the nest. if so, how do we model that?



#### future music
- would be great if we could have underground/overground for the ants, so tunnels under nest etc, still not clear how our 2d grid actually looks, how would overworld work with large objects (for example large food or carcasses etc)
- spatial domain decomposition: viable because interaction radius is bounded; blocked on deterministic seam reconciliation; revisit only if single-machine profiling shows the grid step (not the policy net) is the bottleneck after GPU.
from state.abstract_state import AbstractState
from state.bleed_state import BleedState
from state.burn_state import BurnState
from state.confused_state import ConfusedState
from state.weak_state import WeaknessState


weapons_effects: dict[int, AbstractState] = {
    0: BleedState(),
    1: BurnState(),
    2: ConfusedState(),
    3: WeaknessState(),
}

from math import floor
from abstract.entity import Entity
from game.enums.states import EnumStates
from state.abstract_state import AbstractState


class WeaknessState(AbstractState):

    DEFAULT_POINTS = 0

    def __init__(self) -> None:
        super().__init__(
            EnumStates.WEAKNESS, WeaknessState.DEFAULT_POINTS, EnumStates.BURN
        )

    def hit(self, reciever: Entity):
        if not self._base_hit(reciever):
            return

        reciever.dmg = floor(reciever.default_dmg / 2)
        print(
            f"   [🤕 {self} 🤕] O efeito faz com que {reciever} cause metade do dano. {self.get_formatted_current_duration()}\n"
        )

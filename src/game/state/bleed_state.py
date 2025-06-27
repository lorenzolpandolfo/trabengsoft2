from random import randint
from abstract.entity import Entity
from game.enums.states import EnumStates
from state.abstract_state import AbstractState


class BleedState(AbstractState):

    DEFAULT_POINTS = 2

    def __init__(self) -> None:
        super().__init__(
            EnumStates.BLEEDING, BleedState.DEFAULT_POINTS, EnumStates.BURN
        )

    def hit(self, reciever: Entity):
        if not self._base_hit(reciever):
            return

        bleed_dmg = randint(self.points, 10)

        reciever.hp -= bleed_dmg
        print(
            f"   [{self}] O efeito causa {bleed_dmg} de dano. {self.get_formatted_current_duration()}\n"
        )

    def _get_duration(self) -> int:
        """Returns the number of rounds that the state will be applied."""
        return randint(1, 3)

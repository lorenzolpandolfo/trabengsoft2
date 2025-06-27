from random import randint
from abstract.entity import Entity
from game.enums.states import EnumStates
from state.abstract_state import AbstractState


class ConfusedState(AbstractState):

    DEFAULT_POINTS = 9999999

    def __init__(self) -> None:
        super().__init__(
            EnumStates.CONFUSED, ConfusedState.DEFAULT_POINTS, EnumStates.BURN
        )

    def hit(self, reciever: Entity):
        if not self._base_hit(reciever):
            return

        reciever.crit_chance = self.points
        print(
            f"   [{self}] O efeito faz {reciever} errar críticos por {self.initial_duration} rodadas. {self.get_formatted_current_duration()}\n"
        )
    
    def _get_duration(self) -> int:
        """Returns the number of rounds that the state will be applied."""
        return randint(5, 10)

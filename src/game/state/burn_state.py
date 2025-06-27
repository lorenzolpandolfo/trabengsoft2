from random import randint
from abstract.entity import Entity
from game.enums.states import EnumStates
from state.abstract_state import AbstractState


class BurnState(AbstractState):

    DEFAULT_POINTS = 5

    def __init__(self) -> None:
        super().__init__(EnumStates.BURN, BurnState.DEFAULT_POINTS, EnumStates.BURN)

    def hit(self, reciever: Entity):
        if not self._base_hit(reciever):
            return

        reciever.hp -= self.points
        print(
            f"   [🔥 {self} 🔥] O efeito queima e causa {self.points} pontos de dano. {self.get_formatted_current_duration()}\n"
        )
    
    def _get_duration(self) -> int:
        """Returns the number of rounds that the state will be applied."""
        return randint(3, 10)

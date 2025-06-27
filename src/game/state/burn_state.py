from abstract.entity import Entity
from game.enums.states import EnumStates
from state.abstract_state import AbstractState


class BurnState(AbstractState):

    DEFAULT_POINTS = 2

    def __init__(self) -> None:
        super().__init__(EnumStates.BURN, BurnState.DEFAULT_POINTS, EnumStates.BURN)

    def hit(self, reciever: Entity):
        self._base_hit(reciever)
        reciever.hp -= self.points
        print(
            f"[~] O efeito de {self} causa {self.points} de dano. {self.get_formatted_current_duration()}\n"
        )

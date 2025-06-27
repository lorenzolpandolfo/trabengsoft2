from random import randint
from abc import ABC, abstractmethod

from enums.states import EnumStates


class AbstractState(ABC):

    def __init__(
        self, title: str | EnumStates, points: int, state_type: EnumStates
    ) -> None:
        self.title = str(title)
        self.points = points
        self.state_type = state_type

    def set(self, reciever):
        self.initial_duration = self.duration = self._get_duration()
        reciever.set_current_state(self)

        if reciever.current_state == self:
            self.entity_linked = reciever

    def _get_duration(self) -> int:
        """Returns the number of rounds that the state will be applied."""
        return randint(1, 4)

    @abstractmethod
    def hit(self, reciever):
        pass

    def _base_hit(self, reciever):
        if reciever.current_state.duration <= 0:
            reciever.current_state = None
            return

        reciever.current_state.duration -= 1

    def get_formatted_current_duration(self):
        return f"({self.duration}/{self.initial_duration})"

    def __str__(self) -> str:
        return self.title.capitalize()

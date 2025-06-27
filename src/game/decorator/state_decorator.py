from abstract.entity import Entity
from state.abstract_state import AbstractState


class StateDecorator:

    @staticmethod
    def set_special_state(reciever: Entity, state: AbstractState | None):
        reciever.special_attack_state = state

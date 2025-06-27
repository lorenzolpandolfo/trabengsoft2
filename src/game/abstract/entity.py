from abc import ABC, abstractmethod
from strategy.attack_strategy import AttackStrategy
from state.abstract_state import AbstractState


class Entity(ABC):

    def __init__(
        self,
        hp: int,
        dmg: int,
        name: str,
        crit_chance: int,
        attack_strategy: AttackStrategy,
        special_attack: AbstractState | None,
    ) -> None:
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.crit_chance = crit_chance

        self.default_dmg = dmg
        self.default_crit_chance = crit_chance

        self.attack_strategy = attack_strategy
        self.current_state: AbstractState | None = None
        self.special_attack_state: AbstractState | None = special_attack

    def is_alive(self) -> bool:
        return self.hp > 0

    @abstractmethod
    def war_cry(self) -> str:
        pass

    @abstractmethod
    def use_magic(self) -> str:
        pass

    def _format_magic_msg(self, msg) -> str:
        return f"   [🪄*~.] {self} usou seu poder mágico! {msg}.\n"

    def set_current_state(self, state: AbstractState):
        if not self.current_state:
            self.current_state = state

    def reset_debuffs(self):
        self.crit_chance = self.default_crit_chance

    def __str__(self) -> str:
        return self.name

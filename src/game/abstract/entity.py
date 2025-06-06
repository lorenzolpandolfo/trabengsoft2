from abc import ABC, abstractmethod
from strategy.attack_strategy import AttackStrategy


class Entity(ABC):

    def __init__(
        self,
        hp: int,
        dmg: int,
        name: str,
        crit_chance: int,
        attack_strategy: AttackStrategy,
    ) -> None:
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.crit_chance = crit_chance
        self.attack_strategy = attack_strategy

    def is_alive(self) -> bool:
        return self.hp > 0

    @abstractmethod
    def war_cry(self) -> str:
        pass

    @abstractmethod
    def use_magic(self) -> str:
        pass

    def _format_magic_msg(self, msg) -> str:
        return f"[*~.] {self} usou seu poder mágico! {msg}.\n"

    def __str__(self) -> str:
        return self.name

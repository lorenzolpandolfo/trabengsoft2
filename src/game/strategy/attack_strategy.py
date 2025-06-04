from abc import ABC, abstractmethod


class AttackStrategy(ABC):

    @abstractmethod
    def calculate_damage(self, attacker, critical: bool) -> int:
        pass

    @abstractmethod
    def is_critical(self, attacker) -> bool:
        pass

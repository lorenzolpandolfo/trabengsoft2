from random import randint

from abstract.entity import Entity
from strategy.attack_strategy import AttackStrategy


class DefaultAttackStrategy(AttackStrategy):
    def calculate_damage(self, attacker: Entity, critical: bool) -> int:
        return attacker.dmg * 2 if critical else attacker.dmg

    def is_critical(self, attacker: Entity) -> bool:
        return randint(0, attacker.crit_chance) == attacker.crit_chance

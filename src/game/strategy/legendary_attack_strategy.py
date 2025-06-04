from random import randint
from math import floor

from abstract.entity import Entity
from strategy.attack_strategy import AttackStrategy

INCREASED_DAMAGE_POINTS = 5
INCREASED_CRITICAL_MULTIPLIER = 3


class LegendaryAttackStrategy(AttackStrategy):
    """Legendary enemies critical multiplier is 3, the critical chance is 50% bigger and base damage increase by 5 points."""

    def calculate_damage(self, attacker: Entity, critical: bool) -> int:
        return (
            attacker.dmg * INCREASED_CRITICAL_MULTIPLIER
            if critical
            else attacker.dmg + INCREASED_DAMAGE_POINTS
        )

    def is_critical(self, attacker: Entity) -> bool:
        return randint(0, floor(attacker.crit_chance / 2)) == 0

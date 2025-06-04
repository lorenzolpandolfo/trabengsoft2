from random import choice, random

from abstract.entity import Entity

from domain.player import Player
from domain.orc import Orc
from domain.ghost import Ghost

from strategy.attack_strategy import AttackStrategy
from strategy.default_attack_strategy import DefaultAttackStrategy
from strategy.legendary_attack_strategy import LegendaryAttackStrategy

PREFIXES = [
    "Grande",
    "Macabro",
    "Maníaco",
    "Monstruoso",
    "Sanguinário",
    "Chefe",
]

SUFFIXES = [
    "Guerreiro",
    "Gatuno",
    "Forte",
    "Monstruoso",
    "Maligno",
    "Demoníaco",
    "Vampírico",
]


class EntityFactory:
    def __init__(self, legendary_chance: float = 0.2):
        self.legendary_chance = legendary_chance

    def create_player(self, name) -> Player:
        return Player(name=name, attackStrategy=DefaultAttackStrategy())

    def create_random_enemy(self) -> Entity:
        enemy_creators = [self.create_orc, self.create_ghost]
        return choice(enemy_creators)()

    def create_orc(self) -> Orc:
        attack_strategy = self._select_attack_strategy()
        name = self._create_enemy_name("👺 Orc", attack_strategy)
        return Orc(name=name, attackStrategy=attack_strategy)

    def create_ghost(self) -> Ghost:
        attack_strategy = self._select_attack_strategy()
        name = self._create_enemy_name("👻 Fantasma", attack_strategy)
        return Ghost(name=name, attackStrategy=attack_strategy)

    def _create_enemy_name(self, base_name: str, strategy: AttackStrategy) -> str:
        prefix = choice(PREFIXES).capitalize()
        suffix = choice(SUFFIXES).capitalize()
        full_name = f"{prefix} {base_name} {suffix}"

        if isinstance(strategy, LegendaryAttackStrategy):
            full_name += " (Lendário)"

        return full_name

    def _select_attack_strategy(self) -> AttackStrategy:
        if random() < self.legendary_chance:
            return LegendaryAttackStrategy()
        return DefaultAttackStrategy()

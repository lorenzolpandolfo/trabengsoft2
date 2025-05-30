from random import choice

from abstract.entity import Entity
from domain.player import Player
from domain.orc import Orc
from domain.ghost import Ghost

PREFIXES = [
    "Grande",
    "Macabro",
    "Maníaco",
    "Monstruoso",
    "Sanguinário",
    "Lendário",
    "Chefe",
]

SUFIXES = [
    "Guerreiro",
    "Gatuno",
    "Forte",
    "Monstruoso",
    "Maligno",
    "Demoníaco",
    "Vampírico",
]

class EntityFactory:


    @staticmethod
    def create_player() -> Player:
        return Player("Lorenzo")
    
    @staticmethod
    def create_random_enemy() -> Entity:
        enemy_creators = [EntityFactory.create_orc, EntityFactory.create_ghost]
        return choice(enemy_creators)()

    @staticmethod
    def create_orc() -> Orc:
        return Orc(EntityFactory.__create_enemy_name("👺 Orc"))

    @staticmethod
    def create_ghost() -> Ghost:
        return Ghost(EntityFactory.__create_enemy_name("👻 Fantasma"))

    @staticmethod
    def __create_enemy_name(name: str) -> str:
        return f"{choice(PREFIXES).capitalize()} {name} {choice(SUFIXES).capitalize()}"

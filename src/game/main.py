from factory.entity_factory import EntityFactory
from service.battle_service import BattleService


class Game:

    def __init__(self):
        self.player = EntityFactory.create_player()
        self.enemy = EntityFactory.create_random_enemy()
        self.battle_service = BattleService(self.player, self.enemy)
        self.battle_service.game_loop(self.player)


if __name__ == "__main__":
    Game()

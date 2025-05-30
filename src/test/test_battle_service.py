from unittest import TestCase
from unittest.mock import patch
from service.battle_service import BattleService
from domain.player import Player
from domain.ghost import Ghost
from itertools import cycle


class TestBattleService(TestCase):

    def setUp(self):
        self.player = Player(name="Player")
        self.enemy = Ghost(name="Enemy")
        self.service = BattleService(self.player, self.enemy)

    @patch("service.battle_service.sleep")
    @patch("service.battle_service.randint", side_effect=[1, 6, 2, 2])
    def test_battle_enemy_attacks(self, mock_randint, mock_sleep):
        initial_hp = self.player.hp
        self.service.battle(self.player, self.enemy)
        self.assertLess(self.player.hp, initial_hp)

    @patch("service.battle_service.sleep")
    @patch("service.battle_service.randint", side_effect=[0, 6, 2, 2])
    def test_battle_player_attacks_no_magic(self, mock_randint, mock_sleep):
        initial_hp = self.enemy.hp
        self.service.battle(self.player, self.enemy)
        self.assertLess(self.enemy.hp, initial_hp)

    @patch("service.battle_service.sleep")
    @patch("service.battle_service.randint", side_effect=[0, 0, 2, 2])
    def test_player_uses_magic(self, mock_randint, mock_sleep):
        player = Player(name="Mago")
        service = BattleService(player, self.enemy)
        service.battle(player, self.enemy)
        self.assertEqual(player.crit_chance, 4)

    @patch("service.battle_service.sleep")
    @patch("service.battle_service.randint", side_effect=[0, 6, 2, 2])
    def test_non_critical_attack(self, mock_randint, mock_sleep):
        self.enemy.hp = 15
        self.player.dmg = 10
        self.player.crit_chance = 2
        self.service.battle(self.player, self.enemy)
        self.assertEqual(self.enemy.hp, 0)

    @patch("service.battle_service.sleep")
    @patch("service.battle_service.randint", side_effect=[0, 6, 2, 2])
    def test_kill_enemy(self, mock_randint, mock_sleep):
        self.enemy.hp = 10
        self.player.dmg = 10
        self.player.crit_chance = 0
        self.service.battle(self.player, self.enemy)
        self.assertEqual(self.enemy.hp, 0)

    @patch("service.battle_service.sleep")
    @patch("service.battle_service.randint", side_effect=cycle([0, 6, 2, 0]))
    def test_critical_hit(self, mock_randint, mock_sleep):
        self.enemy.hp = 100
        self.player.dmg = 10
        self.player.crit_chance = 0
        self.service.battle(self.player, self.enemy)
        self.assertEqual(self.enemy.hp, 80)

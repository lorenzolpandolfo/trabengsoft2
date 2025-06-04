from time import sleep
from random import randint, random

from factory.entity_factory import EntityFactory
from abstract.entity import Entity


COOLDOWN_TIME = 2


class BattleService:

    def __init__(self, player_name: str) -> None:
        self.entity_factory: EntityFactory = EntityFactory()
        self.player: Entity = self.entity_factory.create_player(player_name)
        self.enemy: Entity = self.entity_factory.create_random_enemy()

    def game_loop(self):
        sleep(COOLDOWN_TIME)

        while self.player.is_alive():
            self.battle(self.player, self.enemy)

            if not self.enemy.is_alive():
                print(f"{self.player} venceu o {self.enemy}! Lá vem mais um...\n\n")
                self.enemy = self.entity_factory.create_random_enemy()
                sleep(3)

        print("[end] O jogador morreu...\n")

    def battle(self, player: Entity, enemy: Entity) -> Entity:
        attacker: Entity = player if random() < 0.5 else enemy
        reciever: Entity = player if attacker == enemy else enemy

        print(f"> {attacker} ataca...\n")
        sleep(COOLDOWN_TIME)
        self.attack(attacker, reciever)
        return player

    def attack(self, attacker: Entity, reciever: Entity):
        self.war_cry(attacker)
        self.magic(attacker)

        critical = attacker.attack_strategy.is_critical(attacker)
        dmg = attacker.attack_strategy.calculate_damage(attacker, critical)

        msg = (
            f"[!!!] {attacker} ACERTA A CABEÇA DE {reciever} E CAUSA {dmg} DE DANO! (CRÍTICO)\n"
            if critical
            else f"[!] {attacker} ataca {reciever} e causa {dmg} de dano!\n"
        )

        print(msg)
        sleep(COOLDOWN_TIME)
        self.recieve_damage(reciever, dmg)

    def magic(self, attacker: Entity):
        if randint(0, 6) == 0:
            msg = attacker.use_magic()
            print(msg)
            sleep(COOLDOWN_TIME)

    def war_cry(self, attacker: Entity):
        if randint(0, 3) == 0:
            print(f"[!] {attacker} grita: {attacker.war_cry()}\n")
            sleep(COOLDOWN_TIME)

    def recieve_damage(self, reciever: Entity, dmg: int) -> None:
        if reciever.hp - dmg <= 0:
            reciever.hp = 0
            print(f"[x] {reciever} está morto!\n")
            return

        reciever.hp = reciever.hp - dmg
        print(f"(-) {reciever} está com {reciever.hp} pontos de vida.\n\n")
        sleep(COOLDOWN_TIME)

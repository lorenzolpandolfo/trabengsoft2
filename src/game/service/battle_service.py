from time import sleep
from random import randint

from factory.entity_factory import EntityFactory
from abstract.entity import Entity


COOLDOWN_TIME = 2


class BattleService:

    def __init__(self, player: Entity, enemy: Entity) -> None:
        self.player: Entity = player
        self.enemy: Entity = enemy

    def game_loop(self, player: Entity):

        while player.is_alive():
            self.battle(player, self.enemy)

            if not player.is_alive():
                print("[end] O jogador morreu...\n")
                return

            if not self.enemy.is_alive():
                print(f"{player} venceu o {self.enemy}! Lá vem mais um...\n\n")
                self.enemy = EntityFactory.create_random_enemy()
                sleep(3)

    def battle(self, player: Entity, enemy: Entity) -> Entity:
        n: int = randint(0, 3)

        attacker: Entity = player if n == 0 else enemy
        reciever: Entity = player if attacker == enemy else enemy

        print(f"> {attacker} ataca...\n")
        sleep(COOLDOWN_TIME)
        self.attack(attacker, reciever)
        return player

    def attack(self, attacker: Entity, reciever: Entity):
        self.war_cry(attacker)
        self.magic(attacker)

        critical = self.is_critical_attack(attacker)

        dmg = attacker.dmg * 2 if critical else attacker.dmg

        msg = (
            f"[!!!] {attacker} ACERTA A CABEÇA DE {reciever} E CAUSA {dmg} DE DANO! (CRÍTICO)\n"
            if critical
            else f"[!] {attacker} ataca {reciever} e causa {dmg} de dano!\n"
        )

        print(msg)
        sleep(COOLDOWN_TIME)
        self.recieve_damage(reciever, dmg)

    def magic(self, attacker: Entity):
        n: int = randint(0, 6)
        if n == 0:
            msg = attacker.use_magic()
            print(msg)
            sleep(COOLDOWN_TIME)

    def war_cry(self, attacker: Entity):
        n: int = randint(0, 3)
        if n == 0:
            print(f"[!] {attacker} grita: {attacker.war_cry()}\n")
            sleep(COOLDOWN_TIME)

    def is_critical_attack(self, attacker: Entity) -> bool:
        return randint(0, attacker.crit_chance) == attacker.crit_chance

    def recieve_damage(self, reciever: Entity, dmg: int) -> None:
        if reciever.hp - dmg <= 0:
            reciever.hp = 0
            print(f" [x] {reciever} está morto!\n")
            return

        reciever.hp = reciever.hp - dmg
        print(f" [x] {reciever} está com {reciever.hp} pontos de vida.\n\n")
        sleep(COOLDOWN_TIME)

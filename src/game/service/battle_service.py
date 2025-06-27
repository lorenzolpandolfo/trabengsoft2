from time import sleep
from random import randint, random


from abstract.entity import Entity
from factory.entity_factory import EntityFactory
from state.abstract_state import AbstractState


COOLDOWN_TIME = 2
BATTLES_TO_WIN = 10


class BattleService:

    def __init__(self, player_name: str, special_state: AbstractState | None) -> None:
        self.entity_factory: EntityFactory = EntityFactory()
        self.player: Entity = self.entity_factory.create_player(
            player_name, special_state
        )
        self.enemy: Entity = self.entity_factory.create_random_enemy()
        self.current_battle_count = 1

    def game_loop(self):
        sleep(COOLDOWN_TIME)

        while self.player.is_alive():
            self.battle(self.player, self.enemy)

            if not self.enemy.is_alive():
                print(f"{self.player} venceu o {self.enemy}!\n\n")
                self.current_battle_count += 1

                if self.current_battle_count == BATTLES_TO_WIN:
                    print(
                        f"\n[*] Vitória! {self.player} venceu todos os inimigos! Parabéns!\n"
                    )
                    exit(0)

                self.enemy = self.entity_factory.create_random_enemy()
                print(f"Cuidado! {self.enemy} se aproxima...\n")
                print(
                    f"Aperte [ENTER] para iniciar a próxima batalha ({self.current_battle_count}/{BATTLES_TO_WIN})"
                )
                input()
                print(f"\n\n\n[ Batalha {self.current_battle_count}/{BATTLES_TO_WIN} ]\n")

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
            f"   [!!!] {attacker} ACERTA A CABEÇA DE {reciever} E CAUSA {dmg} DE DANO! (CRÍTICO)\n"
            if critical
            else f"   [!] {attacker} ataca {reciever} e causa {dmg} de dano!\n"
        )

        print(msg)
        self.special_state_handler(attacker, reciever)

        sleep(COOLDOWN_TIME)
        self.recieve_damage(reciever, dmg)

    def recieve_damage(self, reciever: Entity, dmg: int) -> None:
        if reciever.hp - dmg <= 0:
            reciever.hp = 0
            print(f"[x] {reciever} está morto!\n")
            return

        reciever.hp = reciever.hp - dmg
        print(f"(-) {reciever} está com {reciever.hp} pontos de vida.\n\n")
        sleep(COOLDOWN_TIME)

    def special_state_handler(self, attacker: Entity, reciever: Entity):
        self.apply_special_state(attacker, reciever)
        self.hit_state(reciever)

    def apply_special_state(self, attacker: Entity, reciever: Entity):
        if randint(0, 2) == 0:
            attacker_state = attacker.special_attack_state

            if not attacker_state or reciever.current_state:
                return

            attacker_state.set(reciever)

            print(
                f"   [!] O ataque de {attacker} causa {str(attacker_state)} nas próximas {attacker_state.duration} rodadas...\n"
            )

            reciever.set_current_state(attacker_state)

    def hit_state(self, reciever: Entity):
        if not reciever.current_state:
            return

        reciever.current_state.hit(reciever)

    def magic(self, attacker: Entity):
        if randint(0, 6) == 0:
            msg = attacker.use_magic()
            print(msg)
            sleep(COOLDOWN_TIME)

    def war_cry(self, attacker: Entity):
        if randint(0, 3) == 0:
            print(f"  [!] {attacker} grita: {attacker.war_cry()}\n")
            sleep(COOLDOWN_TIME)

from abstract.entity import Entity
from strategy.attack_strategy import AttackStrategy
from state.burn_state import BurnState


class Orc(Entity):

    DEFAULT_HP = 15
    DEFAULT_DAMAGE = 8
    DEFAULT_CRIT_CHANCE = 8
    WAR_CRY = "Um Orc nunca foge da guerra..!"
    SPECIAL_ATTACK = BurnState()

    def __init__(self, name: str, attackStrategy: AttackStrategy) -> None:
        super().__init__(
            Orc.DEFAULT_HP,
            Orc.DEFAULT_DAMAGE,
            name,
            Orc.DEFAULT_CRIT_CHANCE,
            attackStrategy,
            Orc.SPECIAL_ATTACK,
        )

    def war_cry(self) -> str:
        return self.WAR_CRY

    def use_magic(self) -> str:
        self.default_dmg = self.dmg = self.dmg + 3
        self.hp = self.hp + 3
        
        return super()._format_magic_msg(
            f"Ataque e vida aumentam em 3 pontos.\n- Atual dano: {self.dmg}, vida: {self.hp}"
        )

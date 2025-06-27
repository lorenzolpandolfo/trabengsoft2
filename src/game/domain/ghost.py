from abstract.entity import Entity
from strategy.attack_strategy import AttackStrategy
from state.burn_state import BurnState


class Ghost(Entity):

    DEFAULT_HP = 5
    DEFAULT_DAMAGE = 10
    DEFAULT_CRIT_CHANCE = 3
    WAR_CRY = "Sua alma será minha!"
    SPECIAL_ATTACK = BurnState()

    def __init__(self, name: str, attackStrategy: AttackStrategy) -> None:
        super().__init__(
            Ghost.DEFAULT_HP,
            Ghost.DEFAULT_DAMAGE,
            name,
            Ghost.DEFAULT_CRIT_CHANCE,
            attackStrategy,
            Ghost.SPECIAL_ATTACK,
        )

    def war_cry(self) -> str:
        return self.WAR_CRY

    def use_magic(self) -> str:
        self.crit_chance = 0
        return super()._format_magic_msg(
            "Seus próximos ataques serão críticos (2x dano)"
        )

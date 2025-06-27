from abstract.entity import Entity
from strategy.attack_strategy import AttackStrategy
from state.burn_state import BurnState


class Player(Entity):
    DEFAULT_HP = 30
    DEFAULT_DAMAGE = 10
    DEFAULT_CRIT_CHANCE = 4
    WAR_CRY = "Atacaaaarr!!!"
    SPECIAL_ATTACK = BurnState()

    def __init__(self, name: str, attackStrategy: AttackStrategy) -> None:
        super().__init__(
            Player.DEFAULT_HP,
            Player.DEFAULT_DAMAGE,
            name,
            Player.DEFAULT_CRIT_CHANCE,
            attackStrategy,
            Player.SPECIAL_ATTACK,
        )

    def war_cry(self) -> str:
        return self.WAR_CRY

    def use_magic(self) -> str:
        self.hp = self.hp + 15
        return f"[*~.] {self} usou seu poder mágico e restaurou 15 pontos de vida!\n- Atual: {self.hp} pontos"

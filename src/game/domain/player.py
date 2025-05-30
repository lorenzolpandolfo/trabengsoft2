from abstract.entity import Entity


class Player(Entity):
    DEFAULT_HP = 30
    DEFAULT_DAMAGE = 10
    DEFAULT_CRIT_CHANCE = 4

    def __init__(self, name: str) -> None:
        super().__init__(Player.DEFAULT_HP, Player.DEFAULT_DAMAGE, name, Player.DEFAULT_CRIT_CHANCE)

    WAR_CRY = "Atacaaaarr!!!"

    def war_cry(self) -> str:
        return self.WAR_CRY

    def use_magic(self) -> str:
        self.hp = self.hp + 15
        return f"[*~.] {self} usou seu poder mágico e restaurou 15 pontos de vida!\n- Atual: {self.hp} pontos"

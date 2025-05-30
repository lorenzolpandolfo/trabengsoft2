from abstract.entity import Entity


class Ghost(Entity):

    DEFAULT_HP = 5
    DEFAULT_DAMAGE = 10
    DEFAULT_CRIT_CHANCE = 3

    def __init__(self, name: str) -> None:
        super().__init__(Ghost.DEFAULT_HP, Ghost.DEFAULT_DAMAGE, name, Ghost.DEFAULT_CRIT_CHANCE)

    WAR_CRY = "Sua alma será minha!"

    def war_cry(self) -> str:
        return self.WAR_CRY

    def use_magic(self) -> str:
        self.crit_chance = 0
        return super()._format_magic_msg("Seus próximos ataques serão críticos (2x dano)")
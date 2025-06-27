from enum import Enum


class EnumStates(Enum):
    BURN = 0
    BLEEDING = 1
    WEAKNESS = 2
    CONFUSED = 3

    def __str__(self) -> str:
        return self.name.capitalize()

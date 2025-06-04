from utils.terminal import clear_terminal
from service.battle_service import BattleService


class GameFacade:
    def __init__(self) -> None:
        self._battle_service: BattleService | None = None

    def start_game(self):
        self._intro()
        name = self._set_player_name()
        self._battle_service = BattleService(name)
        self._battle_service.game_loop()

    def _intro(self):
        clear_terminal()
        print("Ao caminhar pelo vale das sombras...")
        print("Um guerreiro percebe que caiu em uma armadilha!\n")

    def _set_player_name(self) -> str:
        name = input("> Digite seu nome: ")
        name = name if name else "Guerreiro"
        print(f"\n{name} diz: parece que vou ter que batalhar até a morte..!\n\n")
        return name

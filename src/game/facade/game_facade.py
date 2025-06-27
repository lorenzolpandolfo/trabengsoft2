from state.abstract_state import AbstractState
from service.battle_service import BattleService

from utils.terminal import clear_terminal
from utils.constants import weapons_effects


class GameFacade:
    def __init__(self) -> None:
        self._battle_service: BattleService | None = None

    def start_game(self):
        self._intro()
        name = self._set_player_name()
        special_state = self._set_player_weapon()
        self._battle_service = BattleService(name, special_state)
        self._battle_service.game_loop()

    def _intro(self):
        clear_terminal()
        print("Ao caminhar pelo vale das sombras...")
        print("Um guerreiro percebe que caiu em uma armadilha!\n")
        print(
            "Dez inimigos misteriosos se aproximam... Para sair vivo, você deve derrotá-los.\n"
        )

    def _set_player_name(self) -> str:
        name = input("> Digite seu nome: ")
        name = name if name else "Guerreiro"
        print(f"\n{name} diz: parece que vou ter que batalhar pela minha vida..!\n\n")
        return name

    def _set_player_weapon(self) -> AbstractState | None:
        print("Escolha uma arma para lutar:")
        print("(1) - Espada Samurai (Bleed - Sangramento)")
        print("(2) - Chicote Flamejante (Burn - Queimação)")
        print("(3) - Adagas Eletrizantes (Confusion - Confusão)")
        print("(4) - Martelo Esmagador (Weakness - Fraqueza)")
        print("\n(Cada arma tem chance de aplicar o efeito específicado)")
        choice = int(input("\n> Selecione uma arma: ")) - 1
        print("\n")
        return weapons_effects.get(choice)

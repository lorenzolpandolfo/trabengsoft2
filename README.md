# Trabalho Eng. Software 2

Consiste em um jogo estilo RPG de terminal, no qual o jogador deve enfrentar inimigos até que seja derrotado.
Contém 2 tipos de inimigos: Orc e Ghost. Cada um tem seus atributos, magia e grito de guerra.

### Quais padrões foram utilizados

- **Factory Method**: Criação de jogadores, inimigos, itens, etc.
- **Strategy**: Para ataques e magias personalizadas.
- **Facade**: Para abstração da lógica ao iniciar o jogo.
- **Layered Architecture**: Separação clara entre `domain`, `service`, `abstract`, etc.

### Por que foi escolhido cada padrão

Porque esse conjuntos de padrões define uma boa organização para um jogo, permitindo escalabilidade e simplicidade. Adicionar novos inimigos é muito simples, basta criar uma nova classe de domínio herdando a classe Entity, implementar os métodos abstratos, criar um método na EntityFactory e adicioná-lo ao universo de métodos que podem ser chamados na função `create_random_enemy()`.

### Como foi implementado no projeto:

---

#### Factory Method

Uma fábrica (`EntityFactory`) cria entidades, como o jogador e inimigos (Orc ou Ghost), conforme parâmetros.

---

#### Facade

Consiste em uma classe que abstrai a lógica para iniciar o jogo. É utilizada em main.py com o método `start_game()`.

---

#### Strategy

Ataques normais, mágicos e críticos têm comportamentos diferentes implementados em métodos separados.

---

#### Layered Architecture

O código está organizado em camadas, cada uma com sua responsabilidade:

- `domain` entidades
- `service` regras de negócio e lógica complexa
- `abstract` classes abstratas (Entity)
- `strategy` classes de strategy (AttackStrategy)
- `facade` classe GameFacade
- `utils` utilitários

run game (Python 3.11+):
`python src/game/main.py`

_caso o Python não encontre o módulo game, tente o comando abaixo_
`PYTHONPATH=./src/ python ./src/game/main.py`

run tests:
`PYTHONPATH=./src/game/ python -m unittest src/test/test_battle_service.py`

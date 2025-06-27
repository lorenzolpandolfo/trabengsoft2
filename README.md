# Trabalho Eng. Software 2

Consiste em um jogo estilo RPG de terminal, no qual o jogador deve enfrentar 10 inimigos. Caso consiga, vence o jogo.
Contém 2 tipos de inimigos: *Orc* e *Ghost*. Cada um tem seus atributos, magia, grito de guerra e ataque especial.

### Quais padrões foram utilizados

- **Factory Method**: Criação de jogadores, inimigos, itens, etc.
- **Strategy**: Para ataques e magias personalizadas.
- **Facade**: Para abstração da lógica ao iniciar o jogo.
- **State**: Para implementar estados de ataques especiais em entidades (Bleed, Burn, Confusion e Weakness)
- **Decorator**: Para aplicar, em instâncias das entidades, os ataques especiais padrão
- **Layered Architecture**: Separação clara entre `domain`, `service`, etc.

### Por que foi escolhido cada padrão

Porque esse conjuntos de padrões define uma boa organização para um jogo, permitindo escalabilidade e simplicidade. Adicionar novos inimigos é muito simples, basta criar uma nova classe de domínio herdando a classe Entity, implementar os métodos abstratos, criar um método na EntityFactory e adicioná-lo ao universo de métodos que podem ser chamados na função `create_random_enemy()`.

### Como foi implementado no projeto:

---

#### Factory Method

Uma fábrica (`entity_factory.py`) cria entidades, como o jogador e inimigos (Orc ou Ghost), conforme parâmetros.

---

### Decorate

Utilizado para decorar regras de negócio em objetos. Foi utilizado junto com a factory, para decorar ao `player.py` o tipo de ataque especial que ele escolhe no menu, conforme a arma escolhida.

---

### State

Utilizado para implementar as regras de negócio referentes aos tipos de ataques especiais, no caso Bleed, Burn, Confusion e Weakness. Cada um modifica a forma como a mecânica da batalha funciona, e pode estar ativo por um número limitado de turnos.

- *Bleed*: Causa de *2 a 10 pontos* de dano durante *1 a 3 rodadas* 
- *Burn*: Causa *5 pontos* de dano durante *3 a 10 rodadas* 
- *Confusion*: A entidade não consegue acertar críticos durante *5 a 10 rodadas*
- *Weakness*: A entidade causa *metade do dano* durante *1 a 4 rodadas*

Inimigos Ghost vêm, por padrão, com o ataque especial *Weakness*. E, inimigos Orc vêm, por padrão, com o ataque especial *Burn*.

---

#### Facade

Consiste em uma classe `game_facade.py` que abstrai a lógica para iniciar o jogo. É utilizada em main.py com o método `start_game()`.

---

#### Strategy

Os inimigos podem ser do tipo *Lendário*, o que aumenta em 2x a chance de crítico nos ataques, 3x o dano do crítico e têm +5 dano de ataque por padrão.
Para a implementação dessa lógica, foi utilizado o padrão strategy. Temos uma classe `default_attack_strategy.py`, que define a estratégia de ataque comum, e a `legendary_attack_strategy.py`, com a implementação da regra de negócio especificada.

Caso um inimigo seja lendário, a sua estratégia de ataque será uma instância da `legendary_attack_strategy.py`.

---

#### Layered Architecture

O código está organizado em camadas, cada uma com sua responsabilidade:

- `domain` entidades
- `enums` enums (`states.py`)
- `service` regras de negócio e lógica complexa
- `abstract` classes abstratas (Entity)
- `strategy` classes de strategy (`attack_strategy.py`, `default_attack_strategy.py` e `legendary_attack_strategy.py`)
- `state` classes de estado (`bleed_state.py`, `burn_state.py`, `confused_state.py` e `weak_state.py`)
- `facade` classe `game_facade.py`
- `utils` utilitários

run game (Python 3.11+):
`python src/game/main.py`

_caso o Python não encontre o módulo game, tente o comando abaixo_
`PYTHONPATH=./src/ python ./src/game/main.py`

run tests:
`PYTHONPATH=./src/game/ python -m unittest src/test/test_battle_service.py`

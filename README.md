<<<<<<< HEAD
# trabengsoft2

run tests:
`PYTHONPATH=./src/game/ python -m unittest src/test/test_battle_service.py`
=======
# Trabalho Eng. Software 2
Consiste em um jogo estilo RPG de terminal, no qual o jogador deve enfrentar inimigos até que seja derrotado.
Contém 2 tipos de inimigos: Orc e Ghost. Cada um tem seus atributos, magia e grito de guerra.

### Quais padrões foram utilizados
- **Factory Method**: Criação de jogadores, inimigos, itens, etc.
- **Singleton**: Classe principal `Game` com instância única.
- **Layered Architecture**: Separação clara entre `domain`, `service`, `abstract`, etc.

### Por que foi escolhido cada padrão
Porque esse conjuntos de padrões define uma boa organização para um jogo, permitindo escalabilidade e simplicidade. Adicionar novos inimigos é muito simples, basta criar uma nova classe de domínio herdando a classe Entity, implementar os métodos abstratos, criar um método na EntityFactory e adicioná-lo ao universo de métodos que podem ser chamados na função `create_random_enemy()`.

### Como foi implementado no projeto:

---

#### Factory Method  
Uma fábrica (`EntityFactory`) cria entidades, como o  jogador e inimigos (Orc ou Ghost), conforme parâmetros.

---

#### Singleton  
A classe `Game` garante que exista apenas uma instância usada em todo o jogo.

---

#### Strategy (implícito)  
Ataques normais, mágicos e críticos têm comportamentos diferentes implementados em métodos separados.

---

#### Layered Architecture  
O código está organizado em camadas:  
- `domain` para entidades  
- `service` para regras e lógica  
- `abstract` para classes abstratas (Entity)


run game (Python 3.11+):
`python src/game/main.py`

run tests:
`PYTHONPATH=./src/game/ python -m unittest src/test/test_battle_service.py`
>>>>>>> cfaf80d23924390ec66987fd4df10b1c4627a931

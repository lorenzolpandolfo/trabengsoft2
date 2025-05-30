# trabengsoft2

### Qual(is) padrão(ões) foram utilizados
- **Factory Method**: Criação de jogadores, inimigos, itens, etc.
- **Singleton**: Classe principal `Game` com instância única.
- **(implicito) Strategy**: Ataques com variações (normal, crítico, mágico).
- **Layered Architecture**: Separação clara entre `domain`, `service`, `abstract`, etc.

### Por que foi escolhido cada padrão
Porque esse conjuntos de padrão define uma boa organização para um jogo, permitindo escalabilidade e simplicidade.
### Como foi implementado no projeto:

---

#### Factory Method  
Uma fábrica (`EntityFactory`) cria jogadores, inimigos e itens conforme parâmetros.

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
- `abstract` para interfaces base


run game (Python 3.11+):
`python src/game/main.py`

run tests:
`PYTHONPATH=./src/game/ python -m unittest src/test/test_battle_service.py`

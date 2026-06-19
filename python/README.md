# Gilded Rose em Python

Este projeto implementa a lógica do kata Gilded Rose com uma refatoração orientada a regras específicas de cada tipo de item. O objetivo é manter o código legível, facilitar testes e permitir a execução do sistema com poucos comandos.

## 1. Resumo da solução adotada

A solução foi organizada em torno de duas ideias principais:

- O método `update_quality()` agora delega a atualização para classes especializadas, em vez de concentrar toda a lógica em um único bloco com muitas condições.
- Cada tipo de item possui sua própria regra de atualização, o que deixa o código mais fácil de manter e evoluir.

As regras principais implementadas são:

- Itens normais perdem qualidade ao longo do tempo.
- `Aged Brie` aumenta sua qualidade com o tempo.
- `Backstage passes` aumentam a qualidade conforme o evento se aproxima.
- `Sulfuras` não sofrem alterações.
- Itens `Conjured` perdem qualidade com velocidade maior que os itens comuns.

## 2. Principais decisões de refatoração

- Separação da lógica em classes específicas dentro da pasta `Utilities`.
- Criação de uma base comum (`Item`) para evitar duplicação de atributos.
- Centralização da criação do objeto correto por meio de um método responsável por identificar o tipo do item.
- Preservação da interface pública do sistema, mantendo o fluxo principal simples e previsível.

## 3. Pré-requisitos

Certifique-se de ter instalado:

- Python 3.10 ou superior
- `pip` (geralmente já vem com o Python)

## 4. Instalação das dependências

No diretório `python` do projeto, execute:

```bash
python -m pip install -r requirements.txt
```

> Se preferir, você pode criar um ambiente virtual antes de instalar as dependências.

## 5. Como executar o sistema

O projeto possui um script de exemplo que imprime a evolução dos itens dia a dia:

```bash
python texttest_fixture.py 10
```

Esse comando executa a simulação por 10 dias e mostra o estado dos itens a cada iteração.

## 6. Como rodar os testes

### Testes unitários

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### Teste de aprovação

```bash
python tests/test_gilded_rose_approvals.py
```

Esse teste gera uma saída esperada e compara com o arquivo de aprovação armazenado na pasta `tests/approved_files`.

## 7. Estrutura de pastas

```text
python/
├── gilded_rose.py            # lógica principal da atualização dos itens
├── texttest_fixture.py       # exemplo executável do sistema
├── requirements.txt          # dependências do projeto
├── Utilities/                # classes especializadas para cada tipo de item
│   ├── item.py
│   ├── normal_item.py
│   ├── aged_brie.py
│   ├── backstage_pass.py
│   ├── conjured.py
│   ├── sulfuras.py
│   └── __init__.py
└── tests/                    # testes do projeto
    ├── test_gilded_rose.py
    ├── test_gilded_rose_approvals.py
    ├── conftest.py
    ├── approved_files/
    └── approvaltests_config.json
```

## 8. Observações úteis

- O arquivo principal da lógica está em `gilded_rose.py`.
- A pasta `Utilities` concentra as regras específicas dos diferentes itens.
- Os testes ficam em `tests/` e podem ser usados tanto para validação rápida quanto para regressão do comportamento do sistema.


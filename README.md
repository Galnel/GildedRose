# UNIVERSIDADE SENAI CIMATEC

**Gabriel Almeida Vergne De Menezes**  
**Antônio Ivan Messias Soares Júnior**  
**Rafael Nascimento de Menezes**  
**Lucca Reis**  
**Arthur Ribeiro de Cerqueira**  

## TRABALHO DE REFATORAÇÃO DO PROGRAMA LEGADO

**Salvador - BA**  
**2026**

---

## 1. Leitura e compreensão do problema

### Atributos principais

- **Quality**: valor de qualidade do item
- **SellIn**: número de dias restantes para vender o item

### Regras do sistema

- A cada dia, `SellIn` e `Quality` são atualizados pelo método `update_quality()`.
- A qualidade nunca pode ultrapassar `50`.
- A qualidade nunca pode ficar abaixo de `0`.
- Para itens comuns, a qualidade diminui em `1` antes da data de vencimento e em `2` após o vencimento.
- Para `Aged Brie`, a qualidade aumenta com o passar do tempo.
- Para `Backstage Passes`, a qualidade aumenta mais rapidamente quanto mais próximo o evento.
- Para `Sulfuras`, a qualidade e o `SellIn` não mudam.
- Para itens `Conjured`, a qualidade diminui duas vezes mais rápido.

---

## 2. Execução inicial do sistema

Os testes originais foram executados com:

```bash
python -m unittest
```

O resultado esperado era identificar que alguns testes ainda estavam com comportamento incorreto em relação ao comportamento esperado do sistema legado.

---

## 3. Diagnóstico técnico do código legado

O código original apresentava problemas relacionados à complexidade da lógica e à repetição de regras.

### Pontos principais observados

- Muitos `if`/`else` encadeados tornavam a leitura difícil.
- A lógica para atualização de qualidade estava espalhada em várias partes do método.
- Há repetição de condições para itens comuns e regras de limites de qualidade.
- Algumas regras, como a atualização de `Backstage Passes`, não estavam claras e dificultavam a manutenção.

---

## 4. Problema e contexto

O sistema legado possuía regras específicas para diferentes tipos de itens, porém a implementação concentrava essas regras em um único fluxo complexo. Isso dificultava a leitura, a manutenção e a validação correta do comportamento esperado.

---

## 5. Requisitos

O projeto precisava atender aos seguintes requisitos:

- manter a lógica de negócio correta para todos os tipos de item;
- preservar o comportamento esperado do sistema;
- facilitar a manutenção e a expansão futura;
- permitir a execução e validação por meio de testes automatizados.

---

## 6. Riscos e contingências

Os principais riscos da refatoração foram:

- alterar o comportamento esperado de itens já conhecidos;
- introduzir regressões durante a reorganização do código;
- dificultar a leitura ao simplificar demais a lógica.

Como contingência, foram utilizados testes para verificar o comportamento antes e depois da refatoração.

---

## 7. Testes e validação

### Como executar todos os testes

#### Testes unitários

Para rodar a suíte completa de testes com `unittest`, execute:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Também é possível executar diretamente o arquivo principal com os cenários de validação:

```bash
python tests/test_gilded_rose.py
```

Esse arquivo contém os testes que verificam o comportamento esperado para itens comuns, `Aged Brie`, `Backstage Passes`, `Sulfuras` e itens `Conjured`.

#### Teste de aprovação

Para executar apenas o teste de aprovação:

```bash
python tests/test_gilded_rose_approvals.py
```

#### Execução individual de cada arquivo de teste

- Arquivo principal dos testes unitários:

```bash
python tests/test_gilded_rose.py
```

- Arquivo de aprovação:

```bash
python tests/test_gilded_rose_approvals.py
```

- Execução da suíte completa:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

#### Simulação do sistema

```bash
python texttest_fixture.py 10
```

Esses comandos permitem validar tanto o comportamento funcional quanto a saída esperada do sistema.

---

## 8. Melhoria realizada

A refatoração foi realizada com base na separação das regras em classes especializadas, mantendo uma estrutura mais clara e previsível.

### Principais decisões adotadas

- criação de classes específicas para cada tipo de item;
- centralização dos atributos comuns em uma classe base;
- redução da duplicação de lógica;
- organização do código para facilitar a leitura e a manutenção;
- preservação das regras principais do domínio do problema.

---

## 9. Lições aprendidas

A principal lição foi compreender que, em sistemas legados, a complexidade não está apenas na quantidade de código, mas também na forma como as regras estão distribuídas. A refatoração ajudou a tornar a lógica mais explícita e facilitou a análise do comportamento do sistema.

---

## 10. Estrutura do projeto

```text
GildedRose/
├── README.md
└── python/
    ├── gilded_rose.py
    ├── texttest_fixture.py
    ├── requirements.txt
    ├── Utilities/
    │   ├── item.py
    │   ├── normal_item.py
    │   ├── aged_brie.py
    │   ├── backstage_pass.py
    │   ├── conjured.py
    │   └── sulfuras.py
    └── tests/
        ├── test_gilded_rose.py
        ├── test_gilded_rose_approvals.py
        ├── approved_files/
        └── approvaltests_config.json
```

---

## 11. Como executar o projeto do zero

Siga estes passos na ordem para executar o sistema sem depender de nenhuma explicação externa:

### Passo 1: abrir o projeto

Entre na pasta raiz do repositório:

```bash
cd GildedRose
```

### Passo 2: criar o ambiente virtual

```bash
python -m venv .venv
```

No Windows, ative o ambiente com:

```bash
.\.venv\Scripts\Activate
```

### Passo 3: entrar na pasta da implementação em Python

```bash
cd python
```

### Passo 4: instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### Passo 5: executar os testes unitários

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### Passo 6: executar o arquivo principal de testes

```bash
python tests/test_gilded_rose.py
```

### Passo 7: executar o teste de aprovação

```bash
python tests/test_gilded_rose_approvals.py
```

### Passo 8: executar a simulação do sistema

```bash
python texttest_fixture.py 10
```

Esse fluxo completo garante que qualquer pessoa consiga preparar o ambiente, rodar os testes e visualizar o comportamento do sistema sem precisar de instruções adicionais.



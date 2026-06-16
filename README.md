## 🛠️ Configuração do Ambiente Virtual (venv)

Antes de instalar os requisitos, é altamente recomendável criar e ativar um ambiente virtual para manter as dependências do projeto isoladas.

### Criar o ambiente virtual
No terminal, execute o seguinte comando para criar a venv:
```
python -m venv nome_da_sua_venv
```
Após isso, ative seu ambiente virtual:
```
.\nome_da_sua_venv\Scripts\Activate
```
<br>

## 📋 Como Instalar os Requisitos

 Encontre o arquivo `requirements.txt`
```
 neste projeto, ele está localizado na pasta `GildedRose\python`.
```
Acesse a pasta pelo terminal:
```
 Verifique se você está navegando dentro dessa pasta. Se não estiver, use o comando `cd`:
   cd GildedRose_Refactored/python
```



## **Pra rodar teste:**

### Rode os testes unitarios colocando o comando no terminal e apertando enter:

```
python -m unittest
```

### Execute o teste de exemplo TextTest rodando no terminal e apertando enter:

para 10 dias, por exemplo:

```
python texttest_fixture.py 10
```

Você deve garantir que o comando mostrado acima funcione ao executar em um terminal antes de tentar usar o TextTest.


### Execute o teste utilizando o ApprovalTests.Python.

```
python tests/test_gilded_rose_approvals.py
```

Quando o arquivo de saída for gerado na pasta "approved_files", aprove renomeando de "xxx.received.txt" para "xxx.approved.txt".

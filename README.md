# Calculadora de Boas Práticas de Código

Este repositório contém uma **calculadora web** simples desenvolvida em Python com Flask, criada como um exercício acadêmico focado em boas práticas de design de código. O objetivo é demonstrar uma estrutura de código organizada, separação de responsabilidades e uso de testes automatizados para garantir qualidade. Seguir tais práticas ajuda a **assegurar legibilidade, qualidade e escalabilidade** do código. A interface permite executar operações matemáticas básicas (adição, subtração, multiplicação e divisão) de forma clara e didática.

## Tecnologias Utilizadas

O projeto foi implementado em **Python**, uma linguagem de programação de alto nível e multiparadigma. Utiliza o micro-framework **Flask** para criar as rotas web de forma simples e flexível. Os testes automatizados são escritos com **Pytest**, um framework de testes de software para Python que facilita a criação de testes legíveis e reutilizáveis.

* **Python**: Linguagem principal do projeto (versão 3.x), escolhida por sua sintaxe clara e grande suporte a bibliotecas.
* **Flask**: Micro-framework web usado para gerenciar as rotas e renderizar templates HTML da calculadora.
* **Pytest**: Framework de teste em Python utilizado para escrever e executar os testes automatizados da aplicação.

## Estrutura do Projeto

* **`run.py`** (ou **`main.py`**): Arquivo principal que inicializa a aplicação Flask.
* **`requirements.txt`**: Lista de dependências do projeto (Flask, Pytest, etc.) para instalação via `pip`.
* **`src/`**: Pasta com os arquivos da aplicação.
* **`src calculators/`**: Pasta que contém a lógica de da calculadora 4 e o classe de teste da calculadora 4.
* **`src erros/`** Pasta que contém o tratamento de erros da aplicação.
* **`main/`** Pasta que contém a criação de fabrica, as rotas e o servidor.
## Como Executar o Projeto Localmente

1. Faça o clone do repositório e entre na pasta do projeto:

   ```bash
   git clone https://github.com/JtRibeiro/Desafio-introducao-design-codigo.git
   cd Desafio-introducao-design-codigo
   ```
2. Crie um ambiente virtual (recomendado) e instale as dependências:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # no Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Execute a aplicação Flask:

   * Configure a variável de ambiente (se necessário):

     ```bash
     export FLASK_APP=app.py    # no Windows: set FLASK_APP=app.py
     ```
   * Inicie o servidor:

     ```bash
     flask run
     ```

   Acesse a calculadora em `http://localhost:3000/calculator/4` pelo navegador.

## Como Rodar os Testes com Pytest

Com o ambiente configurado (e o diretório do projeto atual), execute o comando abaixo para rodar todos os testes automatizados:

```bash
pytest -s -v
```

Isso executará os testes no diretório `tests/` e exibirá um resumo dos resultados.


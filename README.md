# DuckDB

DuckDB é um sistema de banco de dados relacional orientado a colunas, projetado para ser rápido, leve e eficiente. Focado em OLAP (Online Analytical Processing), DuckDB é ideal para execução de consultas analíticas rápidas em grandes volumes de dados. Ele se integra facilmente com linguagens de programação como Python, R e C++, e pode ser embutido em aplicações, eliminando a necessidade de um servidor de banco de dados separado. Suportando uma ampla gama de operações SQL, DuckDB é otimizado para uso em laptops, servidores e ambientes de nuvem, facilitando a execução de consultas complexas diretamente na memória e proporcionando alta performance em análise de dados.


# Harlequin

Harlequin é uma IDE usada para conexão com diversos bancos de dados como DuckDB , SQLite, Postgres, MySQl, BigQuery e outros, ela pode ser implementada fácilmenete pelo pip, usando Python utilizada diretamente no terminal.

# Projeto de Ambiente Virtual com Pyenv

Este projeto descreve como configurar um ambiente virtual, instalar dependências, criar um script Python para manipulação de dados e acessar um banco de dados DuckDB.

## Passos

1. Criar ambiente virtual `env` com `pyenv` na versão 3.12.1.
2. Instalar `pandas`, `harlequin`, `duckdb` e suas dependências.
3. Criar um script em Python `APP.py`, criando um DataFrame com dados e inserindo no banco de forma persistente, gerando o arquivo `teste.duckdb`.
4. Acessar o arquivo `teste.duckdb` via CLI com DuckDB usando `.OPEN teste.duckdb`.
5. Acessar o arquivo com Harlequin usando o comando `harlequin -r "./teste.duckdb"`.

## Fluxograma

```mermaid
flowchart TD
    A[Criar ambiente virtual com pyenv] -->|Versão 3.12.1| B[Instalar dependências]
    B --> C[Pandas]
    B --> D[Harlequin]
    B --> E[DuckDB]
    B --> F[Criar script app.py]
    F --> G[Criar DataFrame com dados]
    G --> H[Inserir dados no banco DuckDB de forma persistente]
    H --> I[Gerar arquivo teste.duckdb]
    I --> J[Acessar via CLI com DuckDB]
    J --> K[Acessar com Harlequin]

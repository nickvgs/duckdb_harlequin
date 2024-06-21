# DuckDB

DuckDB é um sistema de banco de dados relacional orientado a colunas, projetado para ser rápido, leve e eficiente. Focado em OLAP (Online Analytical Processing), DuckDB é ideal para execução de consultas analíticas rápidas em grandes volumes de dados. Ele se integra facilmente com linguagens de programação como Python, R e C++, e pode ser embutido em aplicações, eliminando a necessidade de um servidor de banco de dados separado. Suportando uma ampla gama de operações SQL, DuckDB é otimizado para uso em laptops, servidores e ambientes de nuvem, facilitando a execução de consultas complexas diretamente na memória e proporcionando alta performance em análise de dados.


# Harlequin

Harlequin é uma IDE usada para conexão com diversos bancos de dados como DuckDB , SQLite, Postgres, MySQl, BigQuery e outros, ela pode ser implementada fácilmenete pelo pip, usando Python utilizada diretamente no terminal.

```mermaid
flowchart TD
    A[Criar ambiente virtual com pyenv] -->|Versão 3.12.1| B[Instalar dependências]
    B --> C[Pandas]
    B --> D[Harlequin]
    B --> E[DuckDB]
    B --> F[Criar script APP.py]
    F --> G[Criar DataFrame com dados]
    G --> H[Inserir dados no banco DuckDB de forma persistente]
    H --> I[Gerar arquivo teste.duckdb]
    I --> J[Acessar via CLI com DuckDB]
    J --> K[.OPEN teste.duckdb]
    I --> L[Acessar com Harlequin]
    L --> M[harlequin -r ".\teste.duckdb"]
def main():
    import duckdb
    import pandas as pd

    #Conectar ao banco de dados
    con = duckdb.connect(database='teste.duckdb')


    # Carregar dados de um arquivo CSV (simulação de dados)
    data = {
        'nome': ['Nicolas Vogiantzis', 'Paulo Cézar', 'Angela Maria'],
        'valor': [1, 2, 23]

    }
    df = pd.DataFrame(data)

    print(df)

    con.execute("CREATE TABLE IF NOT EXISTS teste (nome varchar, valor int)")
    con.append('teste', df)

    result = con.execute("SELECT * FROM teste").fetchdf()
    print(result)


    con.close()

if __name__ == '__main__':
    main()
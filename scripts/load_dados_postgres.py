import pandas as pd
import os
from db_postgres import get_conexao_postgres

def load_csv_to_postgres(file_path, table_name, conn):
    try:
        df = pd.read_csv(file_path)
        cursor = conn.cursor()

        cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
        colunas_sql = ', '.join([f'"{col}" TEXT' for col in df.columns])
        cursor.execute(f'CREATE TABLE {table_name} ({colunas_sql});')

        for _, row in df.iterrows():
            valores = tuple(row.astype(str))
            placeholders = ', '.join(['%s'] * len(valores))
            cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', valores)

        conn.commit()
        cursor.close()
        print(f"✅ Tabela '{table_name}' enviada com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao carregar '{table_name}': {e}")

def main():
    arquivos_tabelas = {
    'data/processed/clientes.csv': 'clientes',
    'data/processed/pedidos.csv': 'pedidos'
}


    conn = get_conexao_postgres()

    for arquivo, tabela in arquivos_tabelas.items():
        if os.path.exists(arquivo):
            load_csv_to_postgres(arquivo, tabela, conn)
        else:
            print(f"⚠️ Arquivo não encontrado: {arquivo}")

    conn.close()

if __name__ == "__main__":
    main()

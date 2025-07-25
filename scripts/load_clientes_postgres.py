from pathlib import Path
import pandas as pd
from db_postgres import get_conexao_postgres
import psycopg2


def carregar_clientes_para_postgres(csv_path: Path) -> None:
    print("📥 Iniciando carga de clientes no PostgreSQL...")

    if not csv_path.exists():
        print(f"❌ Arquivo transformado não encontrado: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    conn = get_conexao_postgres()

    cursor = conn.cursor()

    try:
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO clientes (
                    nome, first_name, last_name, email, telefone, endereco
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (email) DO UPDATE SET
                    nome = EXCLUDED.nome,
                    first_name = EXCLUDED.first_name,
                    last_name = EXCLUDED.last_name,
                    telefone = EXCLUDED.telefone,
                    endereco = EXCLUDED.endereco;
            """, (
                row["nome"], row.get("first_name"), row.get("last_name"),
                row["email"], row["telefone"], row["endereco"]
            ))
        conn.commit()
        print("✅ Carga finalizada com sucesso.")

    except psycopg2.Error as e:
        print(f"❌ Erro ao inserir dados: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    carregar_clientes_para_postgres(Path("data/processed/clientes_transformado.csv"))

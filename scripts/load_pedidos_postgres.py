from pathlib import Path
import pandas as pd
from db_postgres import conectar_db
import psycopg2


def carregar_pedidos_para_postgres(csv_path: Path) -> None:
    print("📥 Iniciando carga de pedidos no PostgreSQL...")

    if not csv_path.exists():
        print(f"❌ Arquivo transformado não encontrado: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    conn = conectar_db()
    cursor = conn.cursor()

    try:
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO pedidos (
                    cliente_email, produto, quantidade, preco
                )
                VALUES (%s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
            """, (
                row["cliente_email"], row["produto"], row["quantidade"], row["preco"]
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
    carregar_pedidos_para_postgres(Path("data/processed/pedidos_transformado.csv"))

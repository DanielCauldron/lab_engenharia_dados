from db_postgres import get_conexao_postgres

def main():
    try:
        conn = get_conexao_postgres()
        print("✅ Conexão com o PostgreSQL realizada com sucesso!")
        conn.close()
    except Exception as e:
        print("❌ Erro ao conectar no PostgreSQL:")
        print(e)

if __name__ == "__main__":
    main()

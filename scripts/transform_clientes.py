from pathlib import Path
import pandas as pd


def transformar_dados_clientes(input_path: Path, output_path: Path) -> None:
    print("🔧 Iniciando transformação de dados de clientes...")

    if not input_path.exists():
        print(f"❌ Arquivo não encontrado: {input_path}")
        return

    df = pd.read_csv(input_path)

    # Limpeza e padronização
    df["nome"] = df["nome"].str.strip().str.title()
    df["email"] = df["email"].str.strip().str.lower()
    df["telefone"] = df["telefone"].str.strip()
    df["endereco"] = df["endereco"].str.strip().str.title()

    # Você pode separar nome completo em primeiro nome e sobrenome se quiser:
    df[["first_name", "last_name"]] = df["nome"].str.split(" ", n=1, expand=True)


    # Remove linhas sem e-mail válido
    df = df[df["email"].str.contains("@", na=False)]

    # Salva dados transformados
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✅ Dados transformados salvos em: {output_path}")


if __name__ == "__main__":
    transformar_dados_clientes(
        input_path=Path("data/raw/clientes.csv"),
        output_path=Path("data/processed/clientes_transformado.csv")
    )

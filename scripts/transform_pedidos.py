from pathlib import Path
import pandas as pd


def transformar_dados_pedidos(input_path: Path, output_path: Path) -> None:
    print("🔧 Iniciando transformação de dados de pedidos...")

    if not input_path.exists():
        print(f"❌ Arquivo não encontrado: {input_path}")
        return

    df = pd.read_csv(input_path)

    # Limpeza e padronização básica
    df["cliente_email"] = df["cliente_email"].str.strip().str.lower()
    df["produto"] = df["produto"].str.strip().str.title()

    df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce").fillna(0).astype(int)
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce").fillna(0.0)

    # Remove linhas sem cliente_email válido
    df = df[df["cliente_email"].str.contains("@", na=False)]

    # Salva dados tratados
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✅ Dados transformados salvos em: {output_path}")


if __name__ == "__main__":
    transformar_dados_pedidos(
        input_path=Path("data/raw/pedidos.csv"),
        output_path=Path("data/processed/pedidos_transformado.csv")
    )

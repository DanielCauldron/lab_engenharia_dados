# Laboratório de Engenharia de Dados

Este repositório é um laboratório prático e evolutivo de Engenharia de Dados, criado para simular cenários reais de geração, transformação, armazenamento e análise de dados. O objetivo é desenvolver habilidades técnicas, explorar ferramentas do ecossistema de dados e compartilhar conhecimento.

## 📁 Estrutura do Projeto

```
├── data/                # Dados brutos e processados (sintéticos)
├── env/, .venv/         # Ambientes virtuais Python (não versionados)
├── gcp/                 # Schemas e arquivos para integração com Google Cloud
├── notebooks/           # Notebooks de exploração e análise
├── publicacao/          # Materiais para divulgação e documentação
├── scripts/             # Scripts de geração, transformação e integração de dados
├── sql/                 # Scripts SQL para criação de tabelas e schemas
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos e pastas ignorados pelo Git
└── README.md            # Este arquivo
```

## ✔️ Funcionalidades já implementadas

- **Geração de dados sintéticos**  
  Scripts em Python usando Faker para criar bases fictícias de clientes e pedidos.  
  _Arquivo:_ `scripts/gerar_dados_faker.py`

- **Transformação de dados**  
  Limpeza, padronização e enriquecimento dos dados com pandas.  
  _Arquivos:_ `scripts/transform_clientes.py`, `scripts/transform_pedidos.py`

- **Exportação e integração com PostgreSQL**  
  Scripts para exportar dados e carregar em banco relacional.  
  _Arquivos:_ `scripts/db_postgres.py`, `scripts/export_postgres_csv.py`, `scripts/load_clientes_postgres.py`, `scripts/load_pedidos_postgres.py`

- **Notebooks de análise exploratória**  
  Exemplos de análise dos dados sintéticos gerados.  
  _Arquivos:_ `notebooks/exploracao_clientes.ipynb`, `notebooks/exploracao_pedidos.ipynb`

- **Documentação e divulgação**  
  Materiais para publicação em redes sociais e resumo do projeto.  
  _Pasta:_ `publicacao/`

## 🚧 Em desenvolvimento / Próximos passos

- **Integração com Google BigQuery**  
  Scripts para carga e consulta de dados em ambiente cloud.

- **Pipelines ETL automatizados**  
  Orquestração do fluxo de ingestão, transformação e carga de dados.

- **Testes automatizados**  
  Implementação de testes unitários para garantir a qualidade dos scripts.

- **Dashboards e visualizações**  
  Exemplos de dashboards e relatórios com ferramentas como Power BI ou Google Data Studio.

- **Documentação detalhada e tutoriais**  
  Expansão do README e criação de guias para facilitar o uso e a colaboração.

## 💡 Objetivo

Evoluir continuamente este laboratório, incorporando novas tecnologias, boas práticas e desafios reais do mercado de dados.  
Ideal para quem deseja praticar, aprender e demonstrar habilidades em Engenharia de Dados.

---

**Contato:**  
[LinkedIn](https://linkedin.com/in/daniel-cauldron)  
[GitHub](https://github.com/DanielCauldron?tab=repositories)

---

> _Projeto em constante evolução. Sinta-se à vontade para acompanhar, contribuir ou entrar em contato!_
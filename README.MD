# Laboratório de Engenharia de Dados

Este repositório é um laboratório prático de Engenharia de Dados, com foco em simular o ciclo completo de ingestão, transformação, armazenamento e análise de dados.

## 🎯 Objetivo

Desenvolver e demonstrar habilidades essenciais para atuar como Engenheiro de Dados Júnior, utilizando ferramentas e práticas adotadas no mercado.

## 🛠️ Tecnologias Utilizadas

- Python 3.10  
- Pandas  
- Faker (simulação de dados)  
- PostgreSQL  
- psycopg2  
- Jupyter Notebooks  
- SQL  
- Ambiente Linux (WSL) + VSCode  

## 📂 Estrutura do Projeto

lab_engdados/
├── data/
│ ├── raw/ # Dados brutos
│ └── processed/ # Dados transformados
├── env/ # Ambiente virtual Python
├── notebooks/ # Notebooks de exploração
│ ├── exploracao_clientes.ipynb
│ └── exploracao_pedidos.ipynb
├── requirements.txt # Dependências
├── scripts/ # Scripts principais
│ ├── gerar_dados_faker.py
│ ├── transform_clientes.py
│ ├── transform_pedidos.py
│ ├── load_clientes_postgres.py
│ ├── load_pedidos_postgres.py
│ └── db_postgres.py
├── sql/
│ └── create_tables.sql # Script de criação de tabelas
└── export_postgres_csv.py # Exportação de dados

markdown
Copiar
Editar

## 🔄 Pipeline de Dados

### Geração de Dados Sintéticos  
`gerar_dados_faker.py`: cria datasets realistas de clientes e pedidos.

### Transformação  
`transform_clientes.py` e `transform_pedidos.py`: padronizam, limpam e enriquecem os dados.

### Carga  
`load_clientes_postgres.py` e `load_pedidos_postgres.py`: inserem os dados no banco PostgreSQL.

### Exploração  
Notebooks com análises iniciais dos dados transformados.

### Exportação  
`export_postgres_csv.py`: extrai dados do banco para arquivos CSV.

## ✅ Competências Demonstradas

- Modelagem de tabelas relacionais  
- Criação de scripts ETL com Python  
- Manipulação e transformação com pandas  
- Integração com banco de dados PostgreSQL  
- Organização de projeto com boas práticas  
- Uso de notebooks para análises exploratórias  

## 📫 Contato

- [LinkedIn](https://linkedin.com/in/daniel-cauldron)  
- [GitHub](https://github.com/DanielCauldron?tab=repositories)  

---

> _Projeto em constante evolução. Sinta-se à vontade para acompanhar, contribuir

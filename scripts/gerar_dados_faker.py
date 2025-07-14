from faker import Faker
import random
import csv
import os

fake = Faker()

def gerar_clientes(n=100):
    clientes = []
    for _ in range(n):
        clientes.append({
            'nome': fake.name(),
            'email': fake.unique.email(),
            'telefone': fake.phone_number(),
            'endereco': fake.address().replace('\n', ', ')
        })
    return clientes

def gerar_pedidos(clientes, n=200):
    produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Impressora']
    pedidos = []
    for _ in range(n):
        cliente = random.choice(clientes)
        pedidos.append({
            'cliente_email': cliente['email'],
            'produto': random.choice(produtos),
            'quantidade': random.randint(1, 5),
            'preco': round(random.uniform(50, 1000), 2)
        })
    return pedidos

def salvar_csv(dados, path, colunas):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(dados)

if __name__ == '__main__':
    clientes = gerar_clientes()
    pedidos = gerar_pedidos(clientes)

    salvar_csv(clientes, 'data/raw/clientes.csv', ['nome', 'email', 'telefone', 'endereco'])
    salvar_csv(pedidos, 'data/raw/pedidos.csv', ['cliente_email', 'produto', 'quantidade', 'preco'])

    print("Dados fake gerados e salvos em 'data/raw/'")

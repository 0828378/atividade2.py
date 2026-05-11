import pandas as pd
from io import StringIO

# DESAFIO 1 — ANÁLISE DE VENDAS

dados = """produto_id,mes,quantidade_vendida
1,2024-01,10
1,2024-02,15
2,2024-01,50
2,2024-02,65
3,2024-01,5
3,2024-02,8
4,2024-01,2
4,2024-02,3
5,2024-01,30
5,2024-02,25
6,2024-02,10"""

df = pd.read_csv(StringIO(dados))

# TAREFA 1
print("=== HEAD (10 primeiras linhas) ===")
print(df.head(10))

print("\n=== INFO ===")
df.info()

# TAREFA 2
df['preco_unitario'] = [100, 100, 50, 50, 200, 200, 500, 500, 40, 40, 150]
df['total_venda'] = df['quantidade_vendida'] * df['preco_unitario']

print("\n=== DATAFRAME COM TOTAL_VENDA ===")
print(df)

# TAREFA 3
df['categoria'] = [
    'Eletrônicos', 'Eletrônicos',
    'Alimentos', 'Alimentos',
    'Eletrônicos', 'Eletrônicos',
    'Móveis', 'Móveis',
    'Eletrônicos', 'Eletrônicos',
    'Eletrônicos'
]
filtro = (
    (df['categoria'] == 'Eletrônicos') &
    (df['total_venda'] > 1000)
)

print("\n=== VENDAS DE ELETRÔNICOS ACIMA DE 1000 ===")
print(df[filtro])

# TAREFA 4
df['cidade'] = [
    'Brasília', 'Brasília',
    'São Paulo', 'São Paulo',
    'Rio de Janeiro', 'Rio de Janeiro',
    'Salvador', 'Salvador',
    'Curitiba', 'Curitiba',
    'Brasília'
]

media_cidade = (
    df.groupby('cidade')['total_venda']
    .mean()
    .sort_values(ascending=False)
)

print("\n=== MÉDIA DE TOTAL_VENDA POR CIDADE ===")
print(media_cidade)

import pandas as pd

# DESAFIO 1 — ANÁLISE DE VENDAS

df = pd.read_csv("vendas.csv")

# TAREFA 1
print("=== HEAD (10 primeiras linhas) ===")
print(df.head(10))
print("\n=== INFO ===")
df.info()

# TAREFA 2
df['total_venda'] = df['quantidade'] * df['preco_unitario']

print("\n=== DATAFRAME COM TOTAL_VENDA ===")
print(df.head())

# TAREFA 3
filtro = (df['categoria'] == 'Eletrônicos') & (df['total_venda'] > 1000)

print("\n=== VENDAS DE ELETRÔNICOS ACIMA DE 1000 ===")
print(df[filtro])

# TAREFA 4
media_cidade = (
    df.groupby('cidade')['total_venda']
    .mean()
    .sort_values(ascending=False)
)

print("\n=== MÉDIA DE TOTAL_VENDA POR CIDADE ===")
print(media_cidade)

import pandas as pd
from io import StringIO

# DESAFIO 1 — ANÁLISE DE VENDAS

dados = """data,produto,categoria,quantidade,preco_unitario,cidade
2024-03-01,Notebook,Eletrônicos,2,3500.00,São Paulo
2024-03-02,Mouse Sem Fio,Eletrônicos,10,120.50,Rio de Janeiro
2024-03-02,Cadeira Ergonômica,Móveis,1,1200.00,Belo Horizonte
2024-03-03,Teclado Mecânico,Eletrônicos,5,350.00,São Paulo
2024-03-04,Monitor 24",Eletrônicos,3,850.00,Curitiba
2024-03-05,Mesa de Escritório,Móveis,2,900.00,Porto Alegre
2024-03-05,Mouse Sem Fio,Eletrônicos,3,120.50,São Paulo
2024-03-06,Notebook,Eletrônicos,1,3500.00,Belo Horizonte
2024-03-07,Webcam 1080p,Eletrônicos,4,250.00,Rio de Janeiro
2024-03-08,Cadeira Ergonômica,Móveis,3,1200.00,Curitiba
2024-03-09,Estante de Livros,Móveis,1,450.00,São Paulo
2024-03-10,Monitor 24",Eletrônicos,2,850.00,Rio de Janeiro
2024-03-11,Mousepad Gigante,Eletrônicos,15,45.00,Porto Alegre
2024-03-12,Teclado Mecânico,Eletrônicos,2,350.00,Belo Horizonte
2024-03-13,Mesa de Escritório,Móveis,1,900.00,São Paulo"""

df = pd.read_csv(StringIO(dados))

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
filtro = (
    (df['categoria'] == 'Eletrônicos') &
    (df['total_venda'] > 1000)
)

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

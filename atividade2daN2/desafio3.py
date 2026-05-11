import pandas as pd
from io import StringIO

# DESAFIO 3 — CONSOLIDAÇÃO DE DADOS DE ESTOQUE

# DATASET 1 — ESTOQUE ATUAL
estoque_dados = """produto_id,quantidade,armazem
1,50,SP
2,200,SP
2,80,RJ
3,20,MG
4,15,SP
5,100,RJ
5,30,MG
6,40,SP"""

estoque_df = pd.read_csv(StringIO(estoque_dados))

# DATASET 2 — PRODUTOS
produtos_dados = """produto_id,nome,categoria,preco_custo
1,Notebook X,Eletrônicos,2500.00
2,Mouse Gamer,Eletrônicos,80.00
3,Cadeira Office,Móveis,450.00
4,Mesa em L,Móveis,600.00
5,Teclado Mecânico,Eletrônicos,150.00
6,Monitor 27",Eletrônicos,900.00"""

produtos_df = pd.read_csv(StringIO(produtos_dados))

# DATASET 3 — VENDAS MENSAIS
vendas_dados = """produto_id,mes,quantidade_vendida
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

vendas_df = pd.read_csv(StringIO(vendas_dados))

# TAREFA 1
df = pd.merge(estoque_df, produtos_df, on='produto_id')

df = pd.merge(df, vendas_df, on='produto_id')

print("=== DATAFRAME CONSOLIDADO ===")
print(df.head())

# TAREFA 2
df['custo_total_estoque'] = (
    df['quantidade'] * df['preco_custo']
)

df['valor_venda_mes'] = (
    df['quantidade_vendida'] * df['preco_custo'] * 1.5
)

print("\n=== CUSTOS E VENDAS ===")
print(df.head())

# TAREFA 3
estoque_critico = df[df['quantidade'] <= 0]

print("\n=== ESTOQUE ZERADO OU NEGATIVO ===")
print(estoque_critico)

estoque_insuficiente = (
    df[df['quantidade_vendida'] > df['quantidade']]
)

print("\n=== ESTOQUE INSUFICIENTE ===")
print(estoque_insuficiente)

# TAREFA 4
df['margem_bruta'] = (
    df['valor_venda_mes'] -
    (df['quantidade_vendida'] * df['preco_custo'])
)

resumo_categoria = df.groupby('categoria').agg({
    'quantidade': 'sum',
    'quantidade_vendida': 'sum',
    'margem_bruta': 'sum'
})

estoque_critico_categoria = (
    df[df['quantidade'] < 10]
    .groupby('categoria')['produto_id']
    .count()
)

resumo_categoria['produtos_estoque_critico'] = (
    estoque_critico_categoria
)

resumo_categoria = resumo_categoria.fillna(0)

print("\n=== RESUMO POR CATEGORIA ===")
print(resumo_categoria)

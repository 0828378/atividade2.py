import pandas as pd

# DESAFIO 2 — LIMPEZA DE DADOS DE RH

df = pd.read_csv("funcionarios.csv")

# TAREFA 1
print("=== VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())

# TAREFA 2
df = df.dropna(subset=['salario'])

media_idade_departamento = (
    df.groupby('departamento')['idade']
    .transform('mean')
)

df['idade'] = df['idade'].fillna(media_idade_departamento)

print("\n=== DATAFRAME APÓS LIMPEZA ===")
print(df.head())

# TAREFA 3
df['data_admissao'] = pd.to_datetime(df['data_admissao'])

df['anos_empresa'] = (
    (pd.Timestamp.today() - df['data_admissao'])
    .dt.days // 365
)

print("\n=== ANOS DE EMPRESA ===")
print(df[['nome', 'data_admissao', 'anos_empresa']].head())

# TAREFA 4
media_salario_departamento = (
    df.groupby('departamento')['salario']
    .transform('mean')
)

filtro = (
    (df['anos_empresa'] > 5) &
    (df['salario'] < media_salario_departamento)
)

print("\n=== FUNCIONÁRIOS COM MAIS DE 5 ANOS E SALÁRIO ABAIXO DA MÉDIA ===")
print(df[filtro])

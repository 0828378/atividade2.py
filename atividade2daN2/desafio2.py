import pandas as pd
from io import StringIO

# DESAFIO 2 — LIMPEZA DE DADOS DE RH

dados = """nome,departamento,salario,data_admissao,idade,status
João Silva,TI,7500.00,2020-01-15,35,Ativo
Maria Souza,RH,5200.00,2021-03-10,28,Ativo
Carlos Santos,TI,,2022-07-01,40,Inativo
Ana Costa,Vendas,4800.00,,25,Ativo
Pedro Alves,Financeiro,8000.00,2019-11-20,,Ativo
Lucas Lima,Vendas,4500.00,2023-01-05,23,
Juliana Mota,,9500.00,2018-05-15,45,Ativo
Marcos Gomes,TI,6000.00,2021-08-25,31,Ativo
Fernanda Dias,RH,,2022-02-14,29,Ativo
Roberto Nunes,Financeiro,7200.00,2020-10-10,,Inativo
Aline Rocha,TI,8500.00,,38,Ativo
,Vendas,3900.00,2023-04-12,21,Ativo
Tiago Mendes,TI,6800.00,2021-11-05,32,Ativo
Camila Ribeiro,RH,4900.00,2023-08-01,26,"""

df = pd.read_csv(StringIO(dados))

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

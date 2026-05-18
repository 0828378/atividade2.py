import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

dados_csv = StringIO("""Bug_ID,Modulo,Severidade,Tempo_Resolucao_Horas
1,Backend,Alta,12
2,Frontend,Média,8
3,DB,Alta,15
4,Backend,Baixa,5
5,Frontend,Alta,10
6,DB,Média,-4
7,Backend,Média,7
8,Frontend,Baixa,
9,DB,Alta,20
10,Backend,Alta,14
11,Frontend,Média,9
12,DB,Baixa,6
13,Backend,Média,11
14,Frontend,Alta,13
15,DB,Média,16
""")

df = pd.read_csv(dados_csv)

print("DATAFRAME ORIGINAL:")
print(df)

df["Tempo_Resolucao_Horas"] = pd.to_numeric(
    df["Tempo_Resolucao_Horas"],
    errors="coerce"
)

media_geral = df.loc[
    df["Tempo_Resolucao_Horas"] >= 0,
    "Tempo_Resolucao_Horas"
].mean()

df["Tempo_Resolucao_Horas"] = df["Tempo_Resolucao_Horas"].apply(
    lambda x: media_geral if pd.isnull(x) or x < 0 else x
)

print("\nDATAFRAME LIMPO:")
print(df)

media_por_modulo = (
    df.groupby("Modulo")["Tempo_Resolucao_Horas"]
    .mean()
    .sort_values(ascending=False)
)

print("\nMÉDIA POR MÓDULO:")
print(media_por_modulo)

plt.figure(figsize=(8,5))

media_por_modulo.plot(
    kind="bar",
    color="skyblue"
)

plt.title("Tempo Médio de Resolução por Módulo")
plt.xlabel("Módulo")
plt.ylabel("Horas")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

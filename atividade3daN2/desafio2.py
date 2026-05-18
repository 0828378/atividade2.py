import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Data": [
        "2026-05-01","2026-05-02","2026-05-03",
        "2026-05-04","2026-05-05","2026-05-06",
        "2026-05-07","2026-05-08","2026-05-09",
        "2026-05-10"
    ],

    "Desenvolvedor": [
        "Ana","Carlos","Ana",
        "João","Carlos","Ana",
        "João","Carlos","Ana",
        "João"
    ],

    "Linhas_Adicionadas": [
        120,200,150,
        90,300,180,
        110,250,210,
        130
    ],

    "Linhas_Removidas": [
        20,50,30,
        15,80,40,
        25,60,35,
        20
    ],

    "Bugs_Gerados": [
        2,5,1,
        3,6,2,
        4,5,1,
        2
    ]
}

df = pd.DataFrame(dados)

df["Data"] = pd.to_datetime(df["Data"])

st.title("Dashboard do Engenheiro de Qualidade")

dev = st.sidebar.radio(
    "Selecione o Desenvolvedor",
    df["Desenvolvedor"].unique()
)

df_filtrado = df[df["Desenvolvedor"] == dev]

total_linhas = df_filtrado["Linhas_Adicionadas"].sum()

st.metric(
    "Total de Linhas Adicionadas",
    total_linhas
)

st.subheader("Evolução Temporal de Bugs Gerados")

fig, ax = plt.subplots(figsize=(8,4))

ax.plot(
    df_filtrado["Data"],
    df_filtrado["Bugs_Gerados"],
    marker="o"
)

ax.set_xlabel("Data")
ax.set_ylabel("Bugs Gerados")
ax.set_title(f"Bugs Gerados por {dev}")

plt.xticks(rotation=45)

st.pyplot(fig)

if st.button("Mostrar Dev com Maior Média de Bugs"):

    media_bugs = (
        df.groupby("Desenvolvedor")["Bugs_Gerados"]
        .mean()
    )

    pior_dev = media_bugs.idxmax()
    maior_media = media_bugs.max()

    st.warning(
        f"{pior_dev} possui a maior média de bugs por commit: "
        f"{maior_media:.2f}"
    )

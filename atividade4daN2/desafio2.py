import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report
)

df = sns.load_dataset("titanic")

df["age"] = df.groupby(
    ["sex", "pclass"]
)["age"].transform(
    lambda x: x.fillna(x.median())
)

colunas_remover = [
    "deck",
    "embark_town",
    "alive",
    "class",
    "who",
    "adult_male",
    "alone"
]

df.drop(columns=colunas_remover, inplace=True)

df.dropna(inplace=True)

df = pd.get_dummies(
    df,
    columns=["sex", "embarked"],
    drop_first=True
)

plt.figure(figsize=(6,4))

sns.countplot(
    data=df,
    x="sex_male",
    hue="survived"
)

plt.title("Sobrevivência por Sexo")
plt.show()

plt.figure(figsize=(8,5))

plt.hist(
    [df[df["survived"] == 0]["age"],
     df[df["survived"] == 1]["age"]],
    bins=20,
    label=["Não Sobreviveu", "Sobreviveu"]
)

plt.legend()
plt.title("Distribuição de Idade")
plt.xlabel("Idade")
plt.ylabel("Frequência")

plt.show()

plt.figure(figsize=(12,8))

corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    cmap="coolwarm"
)

plt.title("Mapa de Correlação")
plt.show()

X = df.drop("survived", axis=1)
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

tree = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)

print("\n========== RESULTADOS ==========")

print("Acurácia:",
      accuracy_score(y_test, y_pred))

print("Precisão:",
      precision_score(y_test, y_pred))

print("Recall:",
      recall_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

texto_arvore = export_text(
    tree,
    feature_names=list(X.columns)
)

print("\n========== ÁRVORE ==========")
print(texto_arvore)

print("""
3 perguntas mais importantes aprendidas pela árvore:

1. O passageiro era homem ou mulher?
2. Qual era a classe do passageiro?
3. Qual era a idade do passageiro?
""")

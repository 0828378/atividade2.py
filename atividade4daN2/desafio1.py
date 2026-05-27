import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

df = pd.read_csv("winequality-red.csv", sep=";")

df["qualidade_alta"] = np.where(df["quality"] >= 7, 1, 0)

X = df.drop(["quality", "qualidade_alta"], axis=1)
y = df["qualidade_alta"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

tree = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)
tree.fit(X_train, y_train)

nb = GaussianNB()
nb.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test_scaled)
y_pred_tree = tree.predict(X_test)
y_pred_nb = nb.predict(X_test)

print("\n========== KNN ==========")
print(classification_report(y_test, y_pred_knn))

print("\n===== ÁRVORE DE DECISÃO =====")
print(classification_report(y_test, y_pred_tree))

print("\n====== NAIVE BAYES ======")
print(classification_report(y_test, y_pred_nb))

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

cm_knn = confusion_matrix(y_test, y_pred_knn)
disp_knn = ConfusionMatrixDisplay(cm_knn)
disp_knn.plot(ax=axes[0], colorbar=False)
axes[0].set_title("KNN")

cm_tree = confusion_matrix(y_test, y_pred_tree)
disp_tree = ConfusionMatrixDisplay(cm_tree)
disp_tree.plot(ax=axes[1], colorbar=False)
axes[1].set_title("Árvore")

cm_nb = confusion_matrix(y_test, y_pred_nb)
disp_nb = ConfusionMatrixDisplay(cm_nb)
disp_nb.plot(ax=axes[2], colorbar=False)
axes[2].set_title("Naive Bayes")

plt.tight_layout()
plt.show()

print("\nAnálise Final:")
print("""
O melhor modelo será aquele que apresentar:
- maior accuracy
- melhor precision e recall
- menor quantidade de erros na matriz de confusão
""")

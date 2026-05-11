import pandas as pd

# TAREFA 1 - CARGA E INSPEÇÃO INICIAL

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print("=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== SHAPE ===")
print(df.shape)


# TAREFA 2 - ESTATÍSTICAS DESCRITIVAS

print("\n=== DESCRIBE ===")
print(df.describe())

print("\n=== NÚMERO DE CLASSES ===")
print(df['Pclass'].nunique())

print("\n=== FREQUÊNCIA POR SEXO ===")
print(df['Sex'].value_counts())


# TAREFA 3 - SELEÇÃO DE DADOS COM LOC E ILOC

print("\n=== LOC (linhas 0 a 10) ===")
print(df.loc[0:10, ['Name', 'Age']])

print("\n=== ILOC (15ª linha) ===")
print(df.iloc[14])


# TAREFA 4 - FILTROS E MÁSCARAS BOOLEANAS

print("\n=== PASSAGEIROS COM MAIS DE 60 ANOS ===")
print(df[df['Age'] > 60])

print("\n=== MULHERES DA 1ª CLASSE ===")
print(df[(df['Sex'] == 'female') & (df['Pclass'] == 1)])

print("\n=== TARIFA ENTRE 50 E 100 ===")
print(df[df['Fare'].between(50, 100)])

print("\n=== EMBARQUE EM 'C' E SOBREVIVERAM ===")
print(df.query("Embarked == 'C' and Survived == 1"))

import numpy as np

# DESAFIO 1

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])

medias = notas.mean(axis=1)
print("Médias por aluno:", medias)

melhor_aluno = np.argmax(medias)
print("Aluno com maior média (índice):", melhor_aluno)
print("Maior média:", medias[melhor_aluno])

media_col = notas.mean(axis=0)
std_col = notas.std(axis=0)

notas_normalizadas = (notas - media_col) / std_col
print("\nNotas normalizadas:\n", notas_normalizadas)

aprovados = notas[medias >= 6.0]
print("\nAlunos aprovados:\n", aprovados)


# DESAFIO 2 

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

media_geral = imagem.mean()
media_linhas = imagem.mean(axis=1)
media_colunas = imagem.mean(axis=0)

print("\nBrilho médio geral:", media_geral)
print("Média por linha:", media_linhas)
print("Média por coluna:", media_colunas)

linha_escura = np.argmin(media_linhas)
print("Linha mais escura (índice):", linha_escura)

imagem_binaria = np.where(imagem >= 128, 255, 0)
print("\nImagem binária:\n", imagem_binaria)

def criar_matriz():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))

    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = input(f"Digite o valor para a posição [{i}][{j}]: ")
            linha.append(valor)
        matriz.append(linha)
    return matriz


matriz_resultado = criar_matriz()

for linha in matriz_resultado:
    print(' '.join(str(valor) for valor in linha))
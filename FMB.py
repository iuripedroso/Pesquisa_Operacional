import re

def ler_matrizes(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    A, B, C = [], [], []

    for linha in linhas:
        linha = linha.strip()

        if linha.startswith("Min Z=") or linha.startswith("Max Z="):
            C = list(map(int, re.findall(r'[-+]?\d+(?=x\d+)', linha)))
            
        elif any(op in linha for op in ["<=", ">=", "="]):
            partes = re.split(r'(<=|>=|=)', linha)
            A.append(list(map(int, re.findall(r'[-+]?\d+(?=x\d+)', partes[0]))))
            B.append(int(re.findall(r'[-+]?\d+', partes[2])[0]))

    return A, B, C

def determinante(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    det = 0
    for i in range(n):
        sub_matriz = [linha[:i] + linha[i+1:] for linha in matriz[1:]]
        det += ((-1) ** i) * matriz[0][i] * determinante(sub_matriz)
    
    return det

def inversa(matriz):
    n = len(matriz)
    det = determinante(matriz)
    if det == 0:
        raise ValueError("A matriz não possui inversa.")
    
    cofatores = []
    for i in range(n):
        linha_cofator = []
        for j in range(n):
            sub_matriz = [linha[:j] + linha[j+1:] for linha in (matriz[:i] + matriz[i+1:])]
            linha_cofator.append(((-1) ** (i + j)) * determinante(sub_matriz))
        cofatores.append(linha_cofator)

    cofatores_transposta = [[cofatores[j][i] for j in range(n)] for i in range(n)]
    inversa_matriz = [[cofatores_transposta[i][j] // det for j in range(n)] for i in range(n)]
    
    return inversa_matriz

def multiplicacao_matrizes(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
    
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def imprimir_matriz_simples(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def imprimir_vetor_simples(vetor):
    print(" ".join(map(str, vetor)))

if __name__ == "__main__":
    nome_arquivo = "problema.txt"
    A, B, C = ler_matrizes(nome_arquivo)

    print("Matriz A:")
    imprimir_matriz_simples(A)

    print("\nVetor B:")
    imprimir_vetor_simples(B)

    print("\nVetor C:")
    imprimir_vetor_simples(C)

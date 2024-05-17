import threading

M = 3  # Número de linhas
K = 2  # Número de colunas de A e linhas de B
N = 3  # Número de colunas

# Matrizes armazenadas estaticamente no código
A = [[1, 4], [2, 5], [3, 6]]  # Matriz A
B = [[8, 7, 6], [5, 4, 3]]  # Matriz B
C = [[0] * N for _ in range(M)]  # Matriz C inicializada com zeros

# Função thread para calcular um elemento da matriz C
def runner(linha, coluna):
    sum = 0
    for k in range(K):
        sum += A[linha][k] * B[k][coluna]
    C[linha][coluna] = sum

# Cria threads para cada elemento da matriz C
threads = []
for linha in range(M):
    for coluna in range(N):
        thread = threading.Thread(target=runner, args=(linha, coluna))
        threads.append(thread)
        thread.start()

# Aguarda a finalização de todas as threads
for thread in threads:
    thread.join()

# Imprime a matriz C resultante
for linha in C:
    print(*linha)

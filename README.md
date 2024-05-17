
# Multiplicação de Matrizes com Threads

## Descrição do Problema

Dadas duas matrizes, A e B, onde a matriz A contém M linhas e K colunas, e a matriz B contém K linhas e N colunas, o produto das matrizes A e B é a matriz C com M linhas e N colunas. A entrada da matriz C para a linha `i`, coluna `j` (C<sub>ij</sub>) é a soma dos produtos dos elementos da linha `i` da matriz A e coluna `j` da matriz B. Isto é,

$$C_{ij} = \sum_{n=1}^{K} A_{i,n} \times B_{n,j} $$

Por exemplo, se A for uma matriz 3 por 2 e B for uma matriz 2 por 3, o elemento C<sub>3,1</sub> será a soma de A<sub>3,1</sub> × B<sub>1,1</sub> e A<sub>3,2</sub> × B<sub>2,1</sub>.

Neste trabalho, cada elemento C<sub>ij</sub> será calculado em uma thread separada. Isso envolverá a criação de M × N threads. O thread principal – ou pai – inicializará as matrizes A, B e alocará memória suficiente para a matriz C, que conterá o produto das matrizes A e B. Essas matrizes serão declaradas como dados globais para que cada thread tenha acesso a A, B e C.

## Código

```python
import threading

M = 3  # Número de linhas de A e C
K = 2  # Número de colunas de A e número de linhas de B
N = 3  # Número de colunas de B e C

# Matrizes armazenadas estaticamente no código
A = [[1, 4], [2, 5], [3, 6]]  # Matriz A
B = [[8, 7, 6], [5, 4, 3]]    # Matriz B
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
```

## Como Funciona

1. **Inicialização das Matrizes**: As matrizes A e B são definidas estaticamente no código.
2. **Criação de Threads**: Para cada elemento da matriz C, é criada uma thread separada que calcula o valor desse elemento.
3. **Cálculo do Produto**: Cada thread executa a função `runner`, que calcula o valor do elemento C<sub>ij</sub> como a soma dos produtos correspondentes da linha `i` de A e coluna `j` de B.
4. **Sincronização das Threads**: O thread principal aguarda a finalização de todas as threads usando `thread.join()`.
5. **Resultado**: A matriz resultante C é impressa no final.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo, por exemplo, `matrix_mult.py`.
3. Execute o script com o comando:
   ```sh
   python matrix_mult.py
   ```

Este código demonstra a utilização de threads para paralelizar o cálculo do produto de duas matrizes, melhorando a eficiência em sistemas com múltiplos núcleos de processamento.

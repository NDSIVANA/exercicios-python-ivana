# 4. Listas + Loop + Operações Matemáticas

def produto_escalar(vetor_a, vetor_b):
    """
    Calcula o produto escalar de dois vetores (listas) de igual tamanho.
    """
    if len(vetor_a) != len(vetor_b):
        raise ValueError("Os vetores devem ter o mesmo tamanho.")

    resultado = 0
    # O loop percorre os índices de 0 até o tamanho do vetor - 1
    for i in range(len(vetor_a)):
        # Multiplica os elementos correspondentes e soma ao resultado
        resultado += vetor_a[i] * vetor_b[i]

    return resultado

# Exemplo de uso
A = [2, 3, 5]
B = [1, 4, 2]

try:
    saida = produto_escalar(A, B)
    print(f"Vetor A: {A}")
    print(f"Vetor B: {B}")
    print(f"Produto Escalar: {saida}") # Saída esperada: 24
except ValueError as e:
    print(f"Erro: {e}")

# Exemplo com vetores de tamanhos diferentes (para teste de erro)
# C = [1, 2]
# D = [1, 2, 3]
# try:
#     produto_escalar(C, D)
# except ValueError as e:
#     print(f"\nTeste de erro: {e}")
# 1. Listas + Compreensão de Listas + Condicionais

def is_prime(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Lista de exemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Usando Compreensão de Listas para gerar as novas listas
primos = [n for n in numeros if is_prime(n)]
nao_primos = [n for n in numeros if not is_prime(n)]

print(f"Lista original: {numeros}")
print(f"Números primos: {primos}")
print(f"Números não primos: {nao_primos}")


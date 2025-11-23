# 6. Biblioteca Externa (collections) + Contagem

from collections import Counter

def analisar_frequencia_caracteres(frase):
    """
    Analisa a frequência de caracteres em uma frase e exibe o 3º mais frequente.
    """
    # Remove espaços e converte para minúsculas para uma contagem mais precisa (opcional)
    frase_limpa = frase.lower().replace(" ", "")

    # Conta a frequência de cada caractere
    contagem = Counter(frase_limpa)

    # Obtém os 3 caracteres mais comuns e suas contagens
    # O most_common retorna uma lista de tuplas [(caractere, contagem), ...]
    top_3 = contagem.most_common(3)

    print(f"Frase analisada: '{frase}'")
    print(f"Contagem total de caracteres únicos: {len(contagem)}")

    if len(contagem) < 3:
        print("Tratamento de Erro: A frase possui menos de 3 caracteres únicos.")
        print(f"Top {len(contagem)} caracteres: {top_3}")
    else:
        # O 3º caractere mais frequente está no índice 2 (0, 1, 2)
        terceiro_caractere, frequencia = top_3[2]
        print(f"O 3º caractere mais frequente é: '{terceiro_caractere}'")
        print(f"Ele aparece: {frequencia} vezes")

# Exemplos de uso
analisar_frequencia_caracteres("banana nanica")
print("-" * 20)
analisar_frequencia_caracteres("A casa amarela")
print("-" * 20)
analisar_frequencia_caracteres("ab") # Menos de 3 caracteres únicos
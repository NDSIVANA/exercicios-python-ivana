# 5. Condicionais + Tratamento de Erros

def analisar_numero(entrada):
    """Analisa a entrada do usuário, tratando erros e exibindo informações."""
    try:
        # Tenta converter para float
        numero_float = float(entrada)
    except ValueError:
        # Caso não possa ser convertido
        print(f"ERRO: A entrada '{entrada}' não é um número válido.")
        return

    # Se a conversão for bem-sucedida
    print(f"O número '{entrada}' é um número válido (float: {numero_float}).")

    # Verifica se é inteiro ou decimal
    if numero_float == int(numero_float):
        # É inteiro
        numero_inteiro = int(numero_float)
        print(f"O número é inteiro: {numero_inteiro}")
        if numero_inteiro % 2 == 0:
            print("É um número par.")
        else:
            print("É um número ímpar.")
    else:
        # É decimal
        parte_inteira = int(numero_float)
        parte_decimal = numero_float - parte_inteira
        print(f"O número é decimal.")
        print(f"Parte inteira: {parte_inteira}")
        # Formata a parte decimal para evitar imprecisões de ponto flutuante
        print(f"Parte decimal: {parte_decimal:.10f}".rstrip('0').rstrip('.'))

# Exemplos de uso (o usuário final precisaria digitar a entrada)
# Para simular a entrada do usuário, usaremos a função com valores fixos.
print("--- Teste 1: Número Decimal ---")
analisar_numero("2.5")

print("\n--- Teste 2: Número Inteiro Par ---")
analisar_numero("10")

print("\n--- Teste 3: Número Inteiro Ímpar ---")
analisar_numero("-7")

print("\n--- Teste 4: Entrada Inválida ---")
analisar_numero("abc")
#Execute o arquivo usando o Python: python fibonacci.py.


def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_in_fibonacci(n, sequence):
    return n in sequence

# Dados fornecidos
data = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

# Número a ser verificado
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Gerar a sequência de Fibonacci até o número informado
fib_sequence = fibonacci_sequence(numero)

# Verificar se o número pertence à sequência
if is_in_fibonacci(numero, fib_sequence):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Extra: Verificar quais valores dos dados fornecidos pertencem à sequência de Fibonacci
for entry in data:
    valor = entry["valor"]
    if valor == 0.0:
        continue  # Ignorar valores zero
    fib_sequence = fibonacci_sequence(valor)
    if is_in_fibonacci(valor, fib_sequence):
        print(f"O valor {valor} do dia {entry['dia']} pertence à sequência de Fibonacci.")


        
        
#Função fibonacci_sequence(n): Gera a sequência de Fibonacci até que o último número gerado seja maior ou igual ao número n informado.

#Função is_in_fibonacci(n, sequence): Verifica se o número n está presente na sequência de Fibonacci gerada.

#Entrada de Dados: O número a ser verificado é solicitado ao usuário através da função input().

#Verificação de Pertencimento: O programa verifica se o número informado pertence à sequência de Fibonacci e imprime uma mensagem correspondente.

#Verificação dos Valores Fornecidos: O programa também verifica quais valores dos dados fornecidos pertencem à sequência de Fibonacci, ignorando os valores zero.
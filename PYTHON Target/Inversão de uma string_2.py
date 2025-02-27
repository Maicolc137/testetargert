# Função para inverter uma string
def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Exemplo de uso
string_original = "Hello, World!"
string_invertida = inverter_string(string_original)

print("String original:", string_original)
print("String invertida:", string_invertida)
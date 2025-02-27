import json

# Exemplo de dados em JSON
dados = '''
{
    "faturamento": [22174.1664, 24537.6698, 26139.6134, 0, 0, 26742.6612, 0, 42889.2258, 46251.174, 11191.4722, 0, 0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0, 0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0, 0, 25681.8318, 1718.1221, 13220.495, 8414.61]
}
'''

dados = json.loads(dados)
faturamento = [x for x in dados['faturamento'] if x > 0]

menor = min(faturamento)
maior = max(faturamento)
media = sum(faturamento) / len(faturamento)

dias_acima_media = sum(1 for x in faturamento if x > media)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias acima da média: {dias_acima_media}")
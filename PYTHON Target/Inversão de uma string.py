#código em Python para inverter uma string sem usar funções prontas
#O código usa slicing ([::-1]) para inverter a string.


def inverter_string(s):
    return s[::-1]

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")

#Se você quiser evitar o uso de slicing, pode fazer um loop manual:

def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")
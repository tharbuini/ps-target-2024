string_inicial = input()
string_invertida = ""

# Invertendo string
for indice in range(len(string_inicial), 0, -1):
    string_invertida += string_inicial[indice - 1]
    
print(string_invertida)
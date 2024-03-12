numero_informado = int(input())

if numero_informado <= 0:
    sequencia_fibonacci = [0]
elif numero_informado == 1:
    sequencia_fibonacci = [0, 1]
else:
    sequencia_fibonacci = []
    # Calculando sequência
    for indice, valor in enumerate(range(numero_informado)):
        if indice == 0 or indice == 1:
            sequencia_fibonacci.append(valor)
        else:
            valor_temporario = sequencia_fibonacci[indice - 1] + sequencia_fibonacci[indice - 2]
            sequencia_fibonacci.append(valor_temporario)

print(sequencia_fibonacci)

# Verificando se o número está na sequência
if numero_informado in sequencia_fibonacci:
    indice = sequencia_fibonacci.index(numero_informado)
    print(f"O valor {numero_informado} está na sequência de Fibonacci no índice {indice}.")
else:
    print(f"O valor {numero_informado} não está na sequência de Fibonacci.")
numeros = []
for i in range(1,4):
    numero = int(input(f"Ingresa el numero {i}: "))
    numeros.append(numero)
print(f"El promedio de los numeros es:{sum(numeros)/len(numeros)}")
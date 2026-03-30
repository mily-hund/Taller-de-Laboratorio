N = int(input("Cuantos numeros deseas ingresar?: "))

while N<0:
    N = int(input("Solo se permiten enteros positivos, intentalo de nuevo: "))

lista = []

for i in range(N):
    numeros = int(input(f"Ingresa el numero {i+1}: "))
    lista.append(numeros)

for i in range(len(lista)):
    for num in range(len(lista)):
        if i != num:
            print(f"({lista[i]}, {lista[num]})")

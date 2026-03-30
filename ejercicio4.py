N = int(input("Cuantos numeros deseas ingresar?: "))

while N<0:
    N = int(input("Solo se permiten enteros positivos, intentalo de nuevo: "))

lista = []

for i in range(N):
    numeros = int(input(f"Ingresa el numero {i+1}: "))
    lista.append(numeros)

ordenada = lista.copy()
for num in range(len(ordenada)):
    for x in range(len(ordenada) - num - 1):
        if ordenada[x] > ordenada[x + 1]:
            ordenada[x], ordenada[x + 1] = ordenada[x + 1], ordenada[x]

print(f"Lista original: {lista}")
print(f"Lista ordenada: {ordenada}")
n = int(input("cuantos numeros deseas ingresar?: "))
lista = []
for i in range(n):
    num = int(input(f"ingresa numero {i+1}: "))
    lista. append(num)
print(f"El mayor es {max (lista)}: ")
print(f"EL menor es {min(lista)}: ")
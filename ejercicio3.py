numeros= []
num = int(input("Cuantos números vas a ingresar?: "))
for i in range(num):
    num=int(input(f"Ingrese número {i+1}: "))
    numeros.append(num)
buscar=int(input("Que número desea buscar?: "))
encontrado = False

for i in range(len(numeros)):
    if numeros [i] == buscar:
        print(f"El número {buscar} fue encontrado en la posición {i+1}")
        encontrado = True
    if not encontrado:
        print(f"El número {buscar} no fue encontrado")



num = int(input("Ingresa un numero: "))

if num <= 0:
    print("Tiene que ser entero positivo.")
else:
    contador = 0
valor_actual = num

while valor_actual % 2 == 0:
    resultado = valor_actual / 2
contador += 1

print(f"Division {contador}: {valor_actual} / 2 = {resultado}")

valor_actual = resultado

print(f"Numero de divisiones: {contador}")
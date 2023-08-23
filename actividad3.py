def ordenar_numeros(num):
    num.sort()
    return num


numeros = []
for i in range(4):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)


numeros_ordenados = ordenar_numeros(numeros)

# Mostrar los números ordenados
print("Números ordenados de menor a mayor:")
for num in numeros_ordenados:
    print(num)
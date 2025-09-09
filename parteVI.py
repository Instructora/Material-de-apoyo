#vectores
numeros = [1, 2, 3]

numeros.append(4)        # [1,2,3,4] agregar
numeros.insert(1, 10)    # [1,10,2,3,4]
numeros.remove(2)        # elimina el primer 2
print(numeros)

print(numeros[0])        # acceder al primer elemento
print(numeros[-1])       # último elemento

#matrices
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][1])  # 2

# Recorrer
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")

#Diccionaris
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])
print(persona.get("edad"))

persona["edad"] = 30
persona["ciudad"] = "Bogotá"

for clave, valor in persona.items():
    print(clave, valor)


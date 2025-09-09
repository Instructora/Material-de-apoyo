# Definición de funciones

def saludar(nombre):
    """Función que retorna un saludo personalizado"""
    return f"Hola, {nombre}!"

def sumar(a, b):
    """Función que suma dos números"""
    return a + b

def es_par(numero):
    """Función que determina si un número es par"""
    return numero % 2 == 0


# Uso de las funciones en el mismo archivo
print(saludar("Isa"))  # Llamar a la función saludar

resultado = sumar(5, 7)
print("La suma es:", resultado)

numero = 8
if es_par(numero):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

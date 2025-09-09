cadena = "  Hola Python  "

print(len(cadena))        # 15 longitud
print(cadena.lower())     # "  hola python  " minuscula
print(cadena.upper())     # "  HOLA PYTHON  " mayuscula
print(cadena.strip())     # "Hola Python"
print(cadena.replace("Python", "Mundo"))  # "  Hola Mundo  "

# Slicing
print(cadena[2:6])   # "Hola"
print(cadena[::-1])  # invertir string

# Dividir y unir
palabras = cadena.split()
print(palabras)  # ["Hola", "Python"]
print("-".join(palabras))  # "Hola-Python"

"""
VARIABLE
Espacio reservado en memoria

TIPOS DE DATOS EN PYTHON:
    str: cadenas de texto
    int: enteros
    float: enteros con decimales
    bool: true/false verdadero/falso  0/1
"""
# Declarar variables
nombre_pieza = "figura picachu"
cantidad = 3
precio = 90.5
activa = True

# ver x terminal el dato almacenado en una variable
print(nombre_pieza)

# ver x terminal el dato almacenado en una variable y el tipo de dato que
print(cantidad, type(cantidad))

# Capturar un valor por terminal
precio_texto = input("Ingrese el precio del pieza: ")
print(precio_texto, type(precio_texto))

print(cantidad)

precio_numero = float(precio_texto)
print(precio_numero, type(precio_numero))


"""
1. Pide por terminal:
    - Nombre de coleccionista.
    - Edad.
2. Convierte la edad a número entero.
3. Imprime/print:
    - Valor de nombre y edad.
    - Tipo de dato de cada variable usando `type()`.
"""





nombre = input("Introduce el nombre del coleccionista: ")
edad = input("Introduce la edad: ")

edad = int(edad)

print("Nombre:", nombre)
print("Edad:", edad)

print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
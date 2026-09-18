"""
STRINGS
    Cadena de texto
        Str
        "Esto es una string"
"""
# Datos escenario
nombre_pieza = "E-T"
estado = "disponible"
precio = 250
stock = 36


# 1. Concatenación ---> unir strings con +
mensaje1 = "CONCATENACIÓN = Pieza: " + nombre_pieza + " Estado: " + estado + " Stock: " + str(stock)
print(mensaje1)
print(mensaje1)

# 2. Interpolación ---> insertar variables dentro de una string
mensaje2 = f"INTERPOLACIÓN = Pieza: {nombre_pieza} Estado: {estado} stock: {stock}"
print(mensaje2)


# 3. Separación por comas (,) ---> print recibe miltiples argumentos
print("SEPARACIÓNX COMAS = Ficha:", nombre_pieza, estado, precio)
x

# 4. split ---> Separador por comas
etiquetas = "retro, anime, musica, terror"
print(type(etiquetas))
print(etiquetas)

lista_etiquetas = etiquetas.split(",") # argumento que equivale al común denominador
print(type(lista_etiquetas))
print(lista_etiquetas)

# 5. replace
nombre_pieza_actualizado = nombre_pieza.replace("-", ".") # (valor-inicial, valor-a-cambiar)
print(nombre_pieza_actualizado)

# 6. lower / upper / title
usuario = "   BeaTriz iniGUEZ CASCALES      "
print(usuario)
print(usuario.strip().lower())
print(usuario.strip().upper())
print(usuario.strip().title())


"""
EJERCICIO
1. Pide por terminal:
    - `nombre_pieza`
    - `categoria`
2. Construye y muestra mensajes usando:
    - Concatenación (`+`)
    - Interpolación (f-string)
    - `print()` con argumentos separados por comas
3. Pide una cadena de tags separadas por coma (ejemplo: `manga,retro,figura`) y 
    conviértela a lista con `split(",")`.
4. Reemplaza en una frase la palabra `"vendida"` por `"reservada"` usando `replace()`.
5. Pide un nombre de usuario y muéstralo en:
    - minúsculas (`lower`)
    - mayúsculas (`upper`)
    - formato título (`title`)
"""

# Datos escenario
precio = 50
comision = 0.1
stock = 5
venderdor_certificado = True
pieza_autentica = False


"""
OPERADORES ARITMÉTICOS
    Operaciones matemáticas, cálculos
        + - / * % **
"""
total_venta = precio + (comision * precio)
print("Total venta", total_venta)
print("Precio cuota = " , total_venta / 3)


"""
OPERADORES COMPARACIÓN
    Comparamos una cosa con otra
        > < >= =< != ==
    Responden 
        Booleanos ---> True / False
"""

print("¿la venta es superior a 100€?",total_venta > 100)
print("¿hay stock?", stock >= 0)

nombre = "figura picachu"
print("¿El nombre es correcto?", "figura picachu" == nombre) # True
print("¿El nombre es correcto?", "Figura picachu" != nombre) # True

"""
OPERADORES LÓGICOS
    Combinar condiciones ---> tablas de la verdad (los amigos de mis amigos == mis amigos ....)
        and
        or
        not
"""

puede_publicar = venderdor_certificado and pieza_autentica
print("¿puede publicar?", puede_publicar) # True and False = False

alerta = (stock == 0) or (not pieza_autentica) # pieza_autentica == False
print("¿requiere alerta?", alerta)

"""
EJERCICIO: 
1. Pide por input():
    - precio
    - stock
    - vendedor_activo (si/no)
2. Implementa estas reglas:
    - venta_habilitada si precio > 0 and stock > 0 and vendedor_activo == "si".
    - `mostrar_alerta si stock == 0 or vendedor_activo == "no".
3. Imprime los resultados booleanos.
4. Extra: calcula total con comisión del 10% e imprime el resultado.
"""







precio="5"
stock="2"
vendedor activo=True
venta habilitada= input(precio>0 and stock) vendedor activo



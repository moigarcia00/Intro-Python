"""
DICCIONARIOS
    Colecciones, NO ordenadas, MUTABLE
    permite elementos duplicados
    permite crud
    CLAVE:VALOR
"""

pieza = {
    "id": 1,
    "nombre": "Carta Yugi oh",
    "estado": "disponible",
    "En_venta": True
}
print(pieza)

# Anadir
pieza["precio"] = 70
print(pieza)

# modificar
pieza["estado"] = "reservado"
print(pieza)

# Eliminar
del pieza["estado"]
print(pieza)

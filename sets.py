"""
SETS
    Colecciones, NO ordenadas, MUTABLE
    NO permite elementos duplicados
    permite Lectura, Creación y eliminación
    No permite la edición de elementos
"""

categorias = {"retro", "anime", "musica", "terror"}
print(categorias)

# Añadir elementos
categorias.add("comics")
print(categorias)

# Eliminar elementos
categorias.remove("terror")
print(categorias)

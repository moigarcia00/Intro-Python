"""
LISTAS ---> ARRAY
    colecciones, ordenadas, MUTABLE
    permite elementos duplicados
    permite CRUD
"""
#Ver elementos de la lista
piezas = ["Carta Yugi oh", "Vinilo Michael Jackson", "Coche lego Fast and furius", "Mario Kart Deluxe"]
print(piezas)

#Añadir elemento a la lista
piezas.append("converse gorillaz")
print(piezas)
print(piezas[0])

#Eliminar elemento
piezas.remove("Vinilo Michael Jackson")
print(piezas)
del piezas[0]
print(piezas)

#Actualizar un elemento
piezas[1] = "Coche lego F&F"
print(piezas)

print(len(piezas))
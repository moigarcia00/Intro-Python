titulo = "anime"
cantidad ="10"
nombre = "black_clover"
print(titulo, cantidad, nombre)

cantidad=int(cantidad)
print("Variables:", titulo, type(titulo)), print(cantidad, type(cantidad)), print(nombre, type(nombre))


cantidad=str(cantidad)

#concatenación
mensaje1 = "titulo " + titulo + " cantidad " + cantidad + " nombre " + nombre
print("Concatenación:", mensaje1)

#interpolación
mensaje2 = f"titulo: {titulo} cantidad: {cantidad} nombre: {nombre}"
print("Interpolación:", mensaje2)

#separación por comas
print("Separación por comas:", titulo, cantidad, nombre)

#split
nombres = "black_clover, Naruto, Boku_No_Hero, Re_Zero, Dragon_Ball "
print("Split:", nombres)


#Replace
nombre_actualizado = nombre.replace("_", " ")
print("Replace:", nombre_actualizado)


#lower / upper / title
print("titulo:", titulo)
print("lower:", titulo.strip().lower())
print("upper:", titulo.strip().upper())
print("tittle:", titulo.strip().title())

#----                   ------
#---- PUNTO 1º,2º,3º,4º ------
#----                   ------

titulo = "anime"
cantidad ="10"
nombre = "black_clover"
print(titulo, cantidad, nombre)

cantidad=int(cantidad)
print("Variables:", titulo, type(titulo)), print(cantidad, type(cantidad)), print(nombre, type(nombre))

#-----        ------
#-----PUNTO 5º------
#-----        ------

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


#-----        ------
#-----PUNTO 6º------
#-----        ------

#Ver elementos de la lista (he transformado la variable nombres del ejercicio anterior)
lista_animes = nombres.split(", ")
print("lista:", lista_animes)

#Añadir elemento a la lista
lista_animes.append(" Fullmetal_Archemist")
print("elemento añadido:", lista_animes)
print("selección de elemento:", lista_animes[2])

#Eliminar elemento
lista_animes.remove("Re_Zero")
print("elemento borrado:", lista_animes)

#Actualizar un elemento
lista_animes[2] = "BNH"
print("lista actualizada:",lista_animes)



#-----        ------
#-----PUNTO 7º------
#-----        ------


#OPERADORES COMPARATIVOS
total_animes = len(lista_animes)
print("¿la lista tiene más de 3 elementos?:", total_animes >3)
print("¿la lista tiene menos de 3 elementos?:", total_animes <3)


#OPERADORES LÓGICOS
favoritos = ("Naruto" in lista_animes) and ("black_clover" in lista_animes)
print("¿están en favoritos?:", favoritos)

taquilla = ("Dragon_Ball " in lista_animes) or ("One_Piece" in lista_animes)
print("¿están en taquilla alguno de los dos?:", taquilla)


#OPERADOREES ARITMÉTICOS
nuevos_animes = ["Pokemon_Horizontes ", "Digimon_BreakBeat"]
lista_completa = lista_animes + nuevos_animes

print("lista completa:", lista_completa)

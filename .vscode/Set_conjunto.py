"""
Es una prueba de poner comentario de varias lineas
que a veces son necesarias
"""
# uso de conjunto, en el caso hipotetico de encontrar amigos comunes de dos personas

mis_amigos ={'Juan','Pedro','Maria'}
tus_amigos={'Juan','Jacobo'}

print(mis_amigos & tus_amigos)

print(mis_amigos - tus_amigos)

print(mis_amigos | tus_amigos)

# este ejemplo crea una lista y la convierte en conjunto o set

frutas =['manzana','platano','pera','manzana','pera']
tipo= set(frutas) ## Con set lo convierto en conjunto
print(tipo)
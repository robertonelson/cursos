# Este comentario 
# uso de listas en python
r=[1,2,3,4,5,3]

print(r.index(3))

print(r.index(3,3))

print(r.count(3))

# uso de if
if 5 in r:
    print('Existe')

if 100 in r:
    print('No Existe')

# ordenando la lista en orden ascendente
r.sort()
print(r)
# ordenando la lista en orden descendente
r.sort(reverse=True)
print(r)
# También se puede realizar de la siguiente manera
r.reverse()
print(r)

# Para crear una lista
x='Mi nombre es Roberto Nelso Carias'
print(x)

to_split= x.split(' ')
print(to_split)

#También puedo unirlo
s=' '.join(to_split)
print(s)
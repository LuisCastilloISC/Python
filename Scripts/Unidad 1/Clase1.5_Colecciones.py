#Colecciones
#Tupla es una colección ordenada e inmutable. Permite datos duplicados.
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)
tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)   #(1, 2, 3)
tupla = (1, 2, 3)
#tupla[0] = 5 # Error! TypeError
tupla = 1, 2, ('a', 'b'), 3
print(tupla)   #(1, 2, ('a', 'b'), 3)
print(tupla[2][0]) #a
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)
tupla = (1, 2, 3)
for t in tupla:
    print(t) #1, 2, 3
tupla = (1, 2, 3)
x, y, z = tupla
print(x, y, z) #1 2 3
tupla = (2,)
print(type(tupla)) #<class 'tuple'>
tupla = (1, 1, 1, 3, 5)
print(tupla.count(1)) #3
tupla = (7, 7, 7, 3, 5)
print(tupla.index(5)) #4
tupla = (7, 7, 7, 3, 5)
#print(l.index(35)) #Error! ValueError
tupla = (7, 7, 7, 3, 5)
print(tupla.index(7, 2)) #2

#Lista es una colección ordenada y modificable. Permite datos duplicados.
lista = [1, 2, 3, 4]
#También se puede crear usando list y pasando un objeto iterable.
lista = list("1234")
#Una lista sea crea con [] separando sus elementos con comas ,. Una gran ventaja es que pueden almacenar tipos de datos distintos.

lista = [1, "Hola", 3.67, [1, 2, 3]]
# Algunas propiedades de las listas:

# Son ordenadas, mantienen el orden en el que han sido definidas
# Pueden ser formadas por tipos arbitrarios
# Pueden ser indexadas con [i].
# Se pueden anidar, es decir, meter una dentro de la otra.
# Son mutables, ya que sus elementos pueden ser modificados.
# Son dinámicas, ya que se pueden añadir o eliminar elementos.
# Acceder y modificar listas
# Si tenemos una lista a con 3 elementos almacenados en ella, podemos acceder a los mismos usando corchetes y un índice, que va desde 0 a n-1 siendo n el tamaño de la lista.

a = [90, "Python", 3.87]
print(a[0]) #90
print(a[1]) #Python
print(a[2]) #3.87

#Se puede también acceder al último elemento usando el índice [-1].
a = [90, "Python", 3.87]
print(a[-1]) #3.87
#De la misma manera, al igual que [-1] es el último elemento, podemos acceder a [-2] que será el penúltimo.
print(a[-2]) #Python
#Y si queremos modificar un elemento de la lista, basta con asignar con el operador = el nuevo valor.
a[2] = 1
print(a) #[90, 'Python', 1]
#Un elemento puede ser eliminado con diferentes métodos como veremos a continuación, o con del y la lista con el índice a eliminar.
l = [1, 2, 3, 4, 5]
del l[1]
print(l) #[1, 3, 4, 5]
#También podemos tener listas anidadas, es decir, una lista dentro de otra. Incluso podemos tener una lista dentro de otra lista y a su vez dentro de otra lista. Para acceder a sus elementos sólo tenemos que usar [] tantas veces como niveles de anidado tengamos.
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0])    #p
print(x[3][2][0]) #5
print(x[3][2][2]) #7
#También es posible crear sublistas más pequeñas de una más grande. Para ello debemos de usar : entre corchetes, indicando a la izquierda el valor de inicio, y a la izquierda el valor final que no está incluido. Por lo tanto [0:2] creará una lista con los elementos [0] y [1] de la original.
l = [1, 2, 3, 4, 5, 6]
print(l[0:2]) #[1, 2]
print(l[2:6]) #[3, 4, 5, 6]

#Y de la misma manera podemos modificar múltiples valores de la lista a la vez usando :.
l = [1, 2, 3, 4, 5, 6]
l[0:3] = [0, 0, 0]
print(l) #[0, 0, 0, 4, 5, 6]

#Hay ciertos operadores como el + que pueden ser usados sobre las listas.
l = [1, 2, 3]
l += [4, 5]
print(l) #[1, 2, 3, 4, 5]

#Y una funcionalidad muy interesante es que se puede asignar una lista con n elementos a n variables.
l = [1, 2, 3]
x, y, z = l
print(x, y, z) #1 2 3

#Iterar listas
#En Python es muy fácil iterar una lista, mucho más que en otros lenguajes de programación.
lista = [5, 9, 10]
for l in lista:
    print(l)
#5
#9
#10
#Si necesitamos un índice acompañado con la lista, que tome valores desde 0 hasta n-1, se puede hacer de la siguiente manera.
lista = [5, 9, 10]
for index, l in enumerate(lista):
    print(index, l)
#0 5
#1 9
#2 10
#O si tenemos dos listas y las queremos iterar a la vez, también es posible hacerlo.
lista1 = [5, 9, 10]
lista2 = ["Jazz", "Rock", "Djent"]
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)
#5 Jazz
#9 Rock
#10 Djent
#Y por supuesto, también se pueden iterar las listas usando los índices como hemos visto al principio, y haciendo uso de len(), que nos devuelve la longitud de la lista.
lista1 = [5, 9, 10]
for i in range(0, len(lista)):
    print(lista1[i])
#5
#9
#10
#Métodos listas
#append(<obj>)
#El método append() añade un elemento al final de la lista.
l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]
#extend(<iterable>)
#El método extend() permite añadir una lista a la lista inicial.
l = [1, 2]
l.extend([3, 4])
print(l) #[1, 2, 3, 4]
#insert(<index>, <obj>)
#El método insert() añade un elemento en una posición o índice determinado.
l = [1, 3]
l.insert(1, 2)
print(l) #[1, 2, 3]
#remove(<obj>)
#El método remove() recibe como argumento un objeto y lo borra de la lista.
l = [1, 2, 3]
l.remove(3)
print(l) #[1, 2]
#El método pop() elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite borrar elementos diferentes al último.
l = [1, 2, 3]
l.pop()
print(l) #[1, 2]
#reverse()
#El método reverse() inverte el órden de la lista.

l = [1, 2, 3]
l.reverse()
print(l) #[3, 2, 1]

#sort()
#El método sort() ordena los elementos de menos a mayor por defecto.

l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]
#Y también permite ordenar de mayor a menor si se pasa como parámetro reverse=True.
l = [3, 1, 2]
l.sort(reverse=True)
print(l) #[3, 2, 1]
#index(<obj>[,index])
#El método index() recibe como parámetro un objeto y devuelve el índice de su primera aparición. Como hemos visto en otras ocasiones, el índice del primer elemento es el 0.

l = ["Periphery", "Intervals", "Monuments"]
print(l.index("Intervals"))
#También permite introducir un parámetro opcional que representa el índice desde el que comenzar la búsqueda del objeto. Es como si ignorara todo lo que hay antes de ese índice para la búsqueda, en este caso el 4.

l = [1, 1, 1, 1, 2, 1, 4, 5]
print(l.index(1, 4)) #5


#Los sets en Python son una estructura de datos usada para almacenar elementos de una manera similar a las listas, pero con ciertas diferencias.
#Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.
#Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
#Sus elementos deben ser inmutables.
#Para entender mejor los sets, es necesario entender ciertos conceptos matemáticos como la teoría de conjuntos.

#Para crear un set en Python se puede hacer con set() y pasando como entrada cualquier tipo iterable, como puede ser una lista. Se puede ver como a pesar de pasar elementos duplicados como dos 8 y en un orden determinado, al imprimir el set no conserva ese orden y los duplicados se han eliminado.

s = set([5, 4, 6, 8, 8, 1])
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>
#Se puede hacer lo mismo haciendo uso de {} y sin usar la palabra set() como se muestra a continuación.

s = {5, 4, 6, 8, 8, 1}
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>

#Operaciones con sets
#A diferencia de las listas, en los set no podemos modificar un elemento a través de su índice. Si lo intentamos, tendremos un TypeError.

s = set([5, 6, 7, 8])
#s[0] = 3 #Error! TypeError

#Los elementos de un set deben ser inmutables, por lo que un elemento de un set no puede ser ni un diccionario ni una lista. Si lo intentamos tendremos un TypeError
lista = ["México", "España"]
#s = set(["USA", "Tlaxcala", lista]) #Error! TypeError

#Los sets se pueden iterar de la misma forma que las listas.
s = set([5, 6, 7, 8])
for ss in s:
    print(ss) #8, 5, 6, 7

#Con la función len() podemos saber la longitud total del set. Como ya hemos indicado, los duplicados son eliminados.
s = set([1, 2, 2, 3, 4])
print(len(s)) #4

#También podemos saber si un elemento está presente en un set con el operador in. Se el valor existe en el set, se devolverá True.
s = set(["Guitarra", "Bajo"])
print("Guitarra" in s) #True

#Los sets tienen además diferentes funcionalidades, que se pueden aplicar en forma de operador o de método. Por ejemplo, el operador | nos permite realizar la unión de dos sets, lo que equivale a juntarlos. El equivalente es el método union() que vemos a continuación.
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 | s2) #{1, 2, 3, 4, 5}




#----------------------09/01/2022------------------#
#Métodos sets
#s.add(<elem>)
#El método add() permite añadir un elemento al set.
l = set([1, 2])
l.add(3)
print(l) #{1, 2, 3}

#s.remove(<elem>)
#El método remove() elimina el elemento que se pasa como parámetro. Si no se encuentra, se lanza la excepción KeyError.
s = set([1, 2])
s.remove(2)
print(s) #{1}

#s.discard(<elem>)
#El método discard() es muy parecido al remove(), borra el elemento que se pasa como parámetro, y si no se encuentra no hace nada.
s = set([1, 2])
s.discard(3)
print(s) #{1, 2}

#s.pop()
#El método pop() elimina un elemento aleatorio del set.
s = set([1, 2])
s.pop()
print(s) #{2}
s.clear()

#El método clear() elimina todos los elementos de set.
s = set([1, 2])
s.clear()
print(s) #set()

#Otros
#Los sets cuentan con una gran cantidad de métodos que permiten realizar operaciones con dos o más, como la unión o la intersección.
#Podemos calcular la unión entre dos sets usando el método union(). Esta operación representa la “mezcla” de ambos sets. Nótese que el método puede ser llamado con más parámetros de entrada, y su resultado será la unión de todos los sets.
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2)) #{1, 2, 3, 4, 5}

#También podemos calcular la intersección entre dos o más set. Su resultado serán aquellos elementos que pertenecen a ambos sets.
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.intersection(s2)) #{3}

#NOTA {} ES UN DICCIONARIO NO UN SET UN SET NO SE PUEDE INICIALIZAR CON {} A MENOS QUE SE USE UNA CONVERSION SET({})
#Dictionary es una colección sin orden, modificable e indexada. No permite datos duplicados.
# Algunas propiedades de los diccionario en Python son las siguientes:

# Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
# Son indexados, los elementos del diccionario son accesibles a través del key.
# Y son anidados, un diccionario puede contener a otro diccionario en su campo value.
# Acceder y modificar elementos
# Se puede acceder a sus elementos con [] o también con la función get()
d1 = {
  "Nombre": "Rocio",
  "Edad": 24,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Rocio', 'Edad': 24, 'Documento': 1003882}
#Otra forma equivalente de crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis.

d2 = dict([
      ('Nombre', 'Rocio'),
      ('Edad', 24),
      ('Documento', 1003882),
])
print(d2)
#{'Nombre': 'Rocio', 'Edad': '24', 'Documento': '1003882'}
#También es posible usar el constructor dict() para crear un diccionario.

d3 = dict(Nombre='Rocio',
          Edad=24,
          Documento=1003882)
print(d3)
#{'Nombre': 'Rocio', 'Edad': 24, 'Documento': 1003882}

print(d1['Nombre'])     #Rocio
print(d1.get('Nombre')) #Rocio


#Para modificar un elemento basta con usar [] con el nombre del key y asignar el valor que queremos.
d1['Nombre'] = "Paco"
print(d1)
#{'Nombre': Rocio', 'Edad': 24, 'Documento': 1003882}

#Si el key al que accedemos no existe, se añade automáticamente.
d1['Direccion'] = "Calle 123"
print(d1)
#{'Nombre': 'Paco', 'Edad': 24, 'Documento': 1003882, 'Direccion': 'Calle 123'}

#Iterar diccionario
#Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos. Para imprimir los key.
# Imprime los key del diccionario
for x in d1:
    print(x)

#Se puede imprimir también solo el value.
# Imprime los value del diccionario
for x in d1:
    print(d1[x])

#O si queremos imprimir el key y el value a la vez.
# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)

#Diccionarios anidados
#Los diccionarios en Python pueden contener uno dentro de otro. Podemos ver como los valores anidado uno y dos del diccionario d contienen a su vez otro diccionario.

anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}

#Métodos diccionarios Python
#clear()
#El método clear() elimina todo el contenido del diccionario.

d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}
#get(<key>[,<default>])
#El método get() nos permite consultar el value para un key determinado. El segundo parámetro es opcional, y en el caso de proporcionarlo es el valor a devolver si no se encuentra la key.

d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado

#items()
#El método items() devuelve una lista con los keys y values del diccionario. Si se convierte en list se puede indexar como si de una lista normal se tratase, siendo los primeros elementos las key y los segundos los value.

d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

#keys()
#El método keys() devuelve una lista con todas las keys del diccionario.

d = {'a': 1, 'b': 2}#
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

#values()
#El método values() devuelve una lista con todos los values o valores del diccionario.
d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

#pop(<key>[,<default>])
#El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. Daría un error si se intenta eliminar una key que no existe.
d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}

#También se puede pasar un segundo parámetro que es el valor a devolver si la key no se ha encontrado. En este caso si no se encuentra no habría error.
d = {'a': 1, 'b': 2}
d.pop('c', -1)
print(d) #{'a': 1, 'b': 2}

#popitem()
#El método popitem() elimina de manera aleatoria un elemento del diccionario.

d = {'a': 1, 'b': 2}
d.popitem()
print(d)
#{'a': 1}
#update(<obj>)
#El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.

d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}
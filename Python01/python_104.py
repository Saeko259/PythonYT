import os
os.system("clear")

#07 - Listas
#Conjunto o secuencia mutable de elementos
#Las listas pueden contener distintos tipos de datos
#Se establecen con corchetes
lista1 = [1 , 2, 3, 4 ,5]
 
#Puedo contener listas dentro de listas, lo que abre la posibilidad a matrices
matriz1 = [[1,2,3], [4,5,6],[7,8,9]]

#Todos los elementos de la lista, tienen un indice segun su posicion, el primer indice es la posicion 0 y asi sucesivamente
listaE = ["Isabella", "Samuel", "Santiago"]
#Quiero imprimir el primer elemento
print(listaE[0])
#Quiero impriimr el ultimo elemento
print(listaE[-1])

#En el caso de las matrices, si quiero acceder a un elemento, debo acceder a la posicion de la lista en la que esta, y la posicion del elemento dentro de esta lista
#Es como si fueran cajones dentro de cajones
matriz1 = [[1,2,3], [4,5,6],[7,8,9]]
#Quiero acceder al numero tres, que esta en la lista en el indice 0, y dentro de la lista, el tres esta en el indice 2
print(matriz1[0][2])

#07.1 Slicing de listas
lista1 = [1 , 2, 3, 4 ,5]
#Python me permite recorrer los indices que yo quiera especificamente entre dos posiciones a y b, creando un intervalo de la forma [a, b), lo que nos retorna una nueva lista
print(lista1[1:4])
print(lista1[:]) #Una copia de la lista

#Esta manera de recorrer las listas puedo pasarle un parametro mas, que va a hacer de que manera recorre los indices en el intervalo
#Es decir, de uno en uno, de dos en dos, y asi
#lista[desde:hasta:como]
#Toda la lista, pero de dos en dos, es decir #[1,3,5], puesto que el elemento en el que inicie todo siempre cuenta
print(lista1[::2])

#Añadir elementos a una lista
lista1 = [1 , 2, 3, 4 ,5]
#Puedo concatenar listas, para asi agregar elementos
#!!FORMA NO EFICIENTE
lista1 = lista1 + [6,7,8,9]

lista1 += [6,7,8,9]

#Puedo obtener la longitud de una lista con la funcion len(lista)
len(lista1)
#08 - Metodos listas
#1. Agregar
lista1 = [1,2,3,4,5]
#Si quiero agregar un elemento al final de una lista, utilizamos lista.append(elemento)
lista1.append(6)
#Si queremos agregar un elemento a una posicion especifica, utilizamos, lista.insert(posicion, elemento)
lista1.extend([7,8,9])
#Agrega multiples elementos al final de la fila


#2. Eliminar
#remove - segun el elemento / pop - segun el indice, aparte retorna lo eliminado
#Si queremos eliminar un elemento, podemos utilzar lista1.remove(elemento), y elimina la primera vez que se encuentra ese elemento
lista1.remove(1)

#si queremos eliminar el ultimo elemento de la lista, debemos utilizar .pop

lista1.pop()
#EL .pop aparte de eliminar el utlimo elemento, lo retorna

print(lista1)
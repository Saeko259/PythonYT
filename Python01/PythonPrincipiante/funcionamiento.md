# PYTHON PRINCIPIANTEES
En este archivo encontraras las notas correpondientes a todos los programas que explican el funcionamiento basico de **python**.
## 1. Python 101
En python hay funciones que para modificar  determinado parametro, debes introducir el nombre de este, es decir, no solo especifico el valor que quiero que tome, sino que nombro el parametro especifico que quiero que tome este valor. Por ejemplo, si quiero cambiar la manera en que se separan las palabras en un print, debo usar sep = "cambio".

```python
print("Hola", "mundo", sep = "")
```

### 1.1 ```print()```

La funcion print nos permite imprimir informacion en la consola. En cuanto a los parametros que debo entregarle, por default solo debo darle lo que quiero que imprima, pueden ser varios items separados por comas. En caso de querer modificar otros parametros de esta funcion, debo utilizar el nombre del parametro, como es el caso con sep. 

```python
print("hola", "mundo", sep = "!") <- Imprimira en consola "hola!mundo!"
```

Otro parametro que es importante conocer es ```end```, que nos permite modificar la manera en que interactuan ese print y el que el sigue, este por default es un cambio de linea.

### 1.2 tipos de datos

En Python tenemos la ventaja de que no tenemos que especificarle el tipo de dato para que este lo asigna, es decir, no debemos utilizar una estrcutura con una memoria especfica "64 bits -32 bits etc". Una funcion que resulta util a la hora de comprender esto es ```type()```, que retorna el tipo de dato del dato que le pasemos como parametro.

Python maneja varios tipos de datos: Int, float, boolean, string,  complex, dict, set, etc.. En python, contamos con el ```None```, que sirve para representar la ausencia de valor. Por ejemplo, queremos que a un parámetro no pasarle ningún valor, ahí usamos none.

### 1.3 Casting de tipos - Transformar un tipo de un valor a otro

Primero que todo hay que tener presente que python es un lenguaje de tipado fuerte, es decir, no hace transformaciones automáticas entre tipos incompatibles. Es un lenguaje de tipado fuerte.
```python
#EJemplo incorrecto (Del tipado fuerte)
print("100" + 2)
```

Retorna error, puesto que el "+" es para concatenar cadenas tambien, y estas intentando operar con dos tipos incompatibles. Por esto debemos convertir el str a un entero, para esto colocaremos el tipo de dato objetivo y adentro el dato que queremos convertir. 
```python
#Ejemplo corregido:
print(int("100") + 2)
```
Hay interacciones interesantes que son validas de mencionar, como por ejemplo la de float(decimal) a int (entero), es una **funcion techo**. 

**Interacciones con bool()**: Al transformar numeros enteros a booleanos, el unico valor que nos va a retornar un valor de falso es el 0. Las cadenas de texto vacias, retornan falso, el resto de valores, incluso un espacio en blano, retornan true.

## 2. Python 102

### 2.1 Variables - guardar datos en memoria

En python es muy sencillo asignar valores de variables, solo pongo el nombre de la variable y su valor.  Como Python es de tipado dinamico, significa que el tipo de dato se determina durante el momento de ejecución, por lo que no tienes que declarar explícitamente el tipo de dato. 

```python
variable ="hola"
```
Es importante tener en cuenta que python,  no tiene constantes, es decir, no tiene variables que  no se cambien o no se dejen reasignar.

**Nota:** Si queremos documentar el tipo de dato de la variable, pongo nombre:typo = valor ; mas python no va a usarlo para anotar el tipo de dato, sino que lo asignara automáticamente.

```python
primera_varible:int ="chao" <- En documentacion sale que deberia ser int, pero la variable es de tipo str.
```

### 2.2 ```Input()```
Es una funcion que te permite obtener datos a traves de la consola. Lo que este dentro del input es lo que se muestra en consola al pedir el dato. La funcion te retorna

```python
valor = input("Ingrese su nombre: ")
```
Por default el input retornara un dato tipo str, por lo que si queremos que la variable sea de otro tipo de dato debemos hacer lo siguiente:

```python
edad = int(input("Ingresa tu edad: "))
```
## 3. Python 103

Este apartado se documentara cuando el dev no tenga pereza de comentar cosas obvias, por lo que nos centraremos en el resto y despues pondre al dia esto
### 3.1 Condicionales

## 4. Python 104 - listas

En este apartado daremos inicio a lo que son las listas, matrices (listas dentro de listas) y las diferentes maneras que podemos operar con estas.


### 4.1 Listas y matrices

Son un conjunto o secuencia mutable, la cual puede contener distintos tipos de datos, en python las listas se establecen con corchetes:

```python
mi_primera_lista = [1,2,3,"string"]
```

Puedo contener **listas dentro de listas**, lo que abre la posibilidad a matrices:

```python
mi_primera_matriz=[[0,1,2],[3,4,5],[6,7,8]]
```

Para acceder a los elementos de una lista, debo colocar la posicion del elemento al lado del nombre de la lista, asi:

```python
lista1=[1,2,3]
#Estamos imprimiendo el primer elememto
print(lista1[0])
```

Ahora, para acceder a un elemento de una lista dentro de otra, la logica se mantiene, accedo a la posicion de la lista interna, y luego a la posicion del elemento dentro de la lista interna.

```css
Lista principal (Contiene filas)
 └─ Lista interna(Contiene columnas)
    └─ Elementos dentro de esa fila
```

```python
listap = [[0,1,2],[3,4,5],[6,7,8]]
#Imprimo el elemento que esta en la tercera fila, segunda columa, es decir, el 7
print(listap[2][1])
```

Es decir, las listas son cajones organizados, y entre mas listas anidemos son cajones dentro de cajones.

### 4.2 Slicing de listas

Python me permite recorrer los indices que yo quiera especificamente entre dos posiciones a y b, creando un intervalo de la forma [a, b), lo que nos retorna una nueva lista. 

```python
lista = [1,2,3,4]
print(lista[1:3])#Imprime 2 y 3
```

A esta manera de recorrer las listas puedo agregarle un parametro mas, lo que va a hacer que no solo se limite el intervalo en el que se recorre la lista, sino que cada cuantos elementos tiene en cuenta, es decir, si va de 1 en 1, o de 2 en 2 y asi. La estrucutura que utilizamos es:

```python
lista[desde:hasta:como]
```

Si quiero recorrer toda la lista pero iterarla de manera distinta, dejo los dos primeros parametros vacios y coloco de cuanto en cuanto quiero recorrerla.

```python
lista[::2] #Recorro la lista de dos en dos
````

### 4.3 Funciones y metodos  de las listas

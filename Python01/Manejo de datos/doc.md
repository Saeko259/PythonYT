# Apuntes sobre el manejo de datos

## 1. Abrir archivos 
### 1.1 Open
Para abrir un archivo, python tiene la funcion open. la cual se usa de la siguiente  manera

```python
open("nombrearchivo.txt", "modo") 
```
Al ejecutar esta funcion  te devuelve un **objeto** archivo que se guardara en la variable asignada.
#### Nota: En python un objeto es una cosa en memoria que tiene datos (atributos) y funciones (metodos) para trabajar con estos datos

Al crear el objeto archivo f, tenemos un objeto en memoria con el que podemos modificar a traves de **metodos** especificos a la clase del objeto, y asi modificamos el archivo original. Es decir, ***creamos un objeto que nos permite utilizar metodos y modificar el archivo original***

### 1.2 Modos de apertura

Al utilizar la funcion open, debemos pasarle dos parametros, el nombre del archivo y el **modo**, pero *¿Que es esto del modo?* 

Como establecimos de manera previa, al utilizar open, python nos da un objeto archivo, pero el modo deterimnara que **metodos** u **operaciones** vas a permitir sobre el archivo, como lo son: leer, borrar, agregar, escribir, etc.

**Nota:** Si dejamos este parametro vacio, el modo por defecto es "r".
#### 1.2.0 El cursor

Antes de comprender los modos de open, debemos tener claro lo que es el cursor. El **cursor** es donde empieza en a leer o escribir en el archivo, esto sera relevante puesto que te permitira entender con que parte del texto se esta tratando, funciona de la siguiente manera:
```
Hola que 
01234567 <- Posiciones reales
```
**Nota**: Para alterar la posicion del cursor debemos utilizar el metodo seek; y si queremos ver la posicion debemos utilizar el metodo tell, se utilizan de la siguiente manera: 

```python
f.seek(0) <- El numero que va adentro sera la nueva posicion

f.tell() <- retornara la posicion actual de el cursor
```

#### 1.2.1 "r" - Read

Abres el archivo para leerlo, **no puedes** modificarlo, algunas caracteristicas de este modo son:

- EL archivo debe existir
- No puedes escribir sobre el archivo
- El **cursor** empieza al inicio

En resumen sirve para leer datos y cargar configuraciones.

#### 1.2.2 "w" - Write

Abre el archivo (o lo crea si no existe) para **escribir desde cero**, las caracteristicas de este modo son:

- Crea el archivo si no existe
- Borra todo si ya existe el archivo
- No permite leer
- Cursor inicia al principio

Sirve para guardar resultados, crear reportes y guardar modelos.

#### 1.2.3 "a" - Append

Abre el archivo para **agregar contenido**, las caracteristicas de este modo son:

- Crea el archivo si no existe
- No borra nada
- Cualquier cosa que escribe se pone al final
- No puedes leer

Sirve para logs, registros, etc.

#### 1.2.4 "r+" - Read + Write

Con este modo puedes **leer** y **escribir**, las caracteristicas de este modo son:

- El archivo debe existir
- No borra contenido
- Cursor comienza al inicio
- Al escribir, **Sobreescribe**, no inserta

Sirve para actualizar partes del archivo y editar datos.

### 1.3 Close

Al utilizar el open de esta manera, tras realizar la operacion que querramos hacer, debemos cerrar el archivo para evitar que:

- Problemas con consumo de memoria
- Archivos bloqueados
- Escritura incompleta

Entonces debemos hacerlo de la siguiente manera:

```python
f = open("nombrearchivo.txt", "r")
contenido = f.read()
f.close()
```

Asi logramos leer el archivo (lo que se explicara mas adelante),  y despues lo cerramos, pero para evitar esto debemos abrirlo de manera correcta.

## 2. Abrir archivos de "manera correcta"

No es que usar la estructura de open - close este mal, sino que cuenta con multiples problemas, como que:

- Si ocurre un error antes del close el archivo queda abierto.
- Si haces return antes queda abierto

Para evitar estos errores utilizamos ***with***

### 2.1 Que es *with* y como se utiliza ?

Basicamente, **with** es una estructura especial que le dice a python que *"Usa este recurso por un rato, y cuando termine el bloque, límpialo correctamente."* Un ejemplo como se usaria es el siguiente:

```python
with open("datos.txt") as f:
    contenido = f.read()
```

Asi podemos abrir el archivo, ejecutar el codigo y cerrar el archivo automaticamente, pase lo que pase.

**Nota:** with no se utiliza unicamente con archivos, sino con todos los objetos que sean **context managers**, que dicho de manera sencilla, son objetos que saben que hacer al entrar en un bloque with al entrar (que formalmente seria la funcion ```__enter__()```) y que hacer al salir (que formalmente seria la funcion ```__exit__()```).  Es decir ```open()``` es un **context manager**.

With es importante puesto que garantiza un **manejo seguro de recursos**, y no se utiliza unicament para archivos, sino que tambien para:

- Bases de datos
- Conexiones de red
- Archivos temporales

Podemos abrir multiples archivos con with de la siguiente forma: 

```python
with open("a.txt") as f1, open("b.txt") as f2:
    print(f1.read())
    print(f2.read())
```

**Nota***: Tras cerrado el with no puedes volver a acceder a el objeto archivo, a menos que lo vuelvas a abrir.

## 3. Metodos 
Vamos a explicar cada metodo puntual, lo que retorna y su funcionamiento 
### 3.1 Metodos de lectura
#### 3.1.1 ```read()```

Este metodo lee el archivo completo, desde la posicion del cursor hasta el final, **retorna** un ***string*** con todo el texto, y deja el cursor al **final del archivo**. Si hiciesemos dos reads seguidos, el segundo retornaria un string vacio ```""```, puesto que el cursor ya esta al final.

**Ejemplo sintaxis**:

```python 
with open("texto.txt") as f:
    strin = f.read()
```

#### 3.1.2 ```readline()```

Este metodo lee una sola linea desde donde este el cursor, es decir, donde este el primer fin de linea ```\n``` que se encuentre tras el cursor. Deja el cursor en la posicion que le sigue a ese salto de linea.

**Ejemplo sintaxis**:
```python 
with open("texto.txt") as f:
    linea1 = f.readline()
    linea2 = f.readline()
```

#### 3.1.3 ```readlines()```

Lee todas las lineas y las guarda en una lista que retorna, es decir retorna una **lista de strings** y deja el cursor al final del archivo.

**Ejemplo sintaxis**:

```python 
with open("texto.txt") as f:
    lineas = f.readlines()
```
**Nota**: Aunque este metodo es bueno si quieres de manera posterior modificar las lineas,si lo unico que quieres hacer es imprimir linea por linea lo puedes hacer con un for, de la siguiente manera:

```python
with open("texto.txt") as f:
    for lineas in f:
        print(lineas)
```

### 3.2 Metodos de escritura

#### 3.2.1 ```write()```

Escribe exactamente el string que le des en el archivo en la posicion del cursor en la que estes, retorna la cantidad de caracteres, y deja el cursor en la posicion justo despues del ultimo caracter escrito.

**Ejemplo sintaxsis**

```python
with open("texto.txt", "w") as f:
    n = f.write("Hola")
```

**Nota:** Si quieres que se escriba una nueva linea, debes escribir al inicio ```\n```.

#### 3.2.2 ```writelines(lista)```

Escribe una lista de strings en el archivo, mas no retorna nada, si no colocas el salto de linea colocara todo lo de la lista en la misma linea. El cursor queda justo en la posicion despues del ultimo caracter escrito.

---
### **Resumen de metodos**

| Metodo |  Que hace ? | Que retorna ?|
| --- | --- | --- |  
| read() | lee todo el archivo |string|
| readline() | una línea | string|
| readlines() | lee todas las lineas | lista de strings|
| write() | escribe string | retorna nº caracteres |
| writelines() | escribe lista | no retorna |
| tell() | dónde esta el cursor| int |
| seek() | mueve el cursor | null|

## Problemas Encontrados en el camino !!

### 1. Rutas y Ubicacion de archivo

Al intentar ejectuar de manera directa el siguiente bloque de codigo arroja error:

```python
with open("textop.txt","r") as f:
    contenido = f.read()
    print(contenido)
```

El error que nos arroja es que no encuentra el archivo en la supuesta carpeta que esta trabajando el archivo, pero la realidad es que python trabaja con un **directorio de trabajo** pero no necesariamente en la carpeta donde tu tengas tu archivo actual, para esto vamos a ubicar al inicio del codigo la ruta de tu archivo principal, para esto vamos a usar una variable que nos da python ```__file__```, junto a otras funciones del sistema .

1. **```__file__```** nos da la ubicacion actual del archivo que se esta ejecutando

2. **```os.path.dirname(ruta)```**: A esta funcion le das como parametro un archivo y te retorna la carpeta que lo contiene.

3. **```os.path.join("ruta","carpeta","archivo",...)```** Construye rutas con el formato correcto del sistema, con los parametros puestos la funcion retornaria lo siguiente: ruta/carpeta/archivo. Esta funcion no solo puedes unir de manera lineal las rutas, si seguido de una ruta, colocas un **".."**, sube una carpeta. Por ejemplo, en el siguiente caso:

```css
Proyecto/
 ├─ data/
 │   └─ macros.txt
 └─ src/
     └─ main.py

```

Aqui tendriamos que acceder a nuestra carpeta madre del archivo que estamos accediendo, luego acceder a data, y luego a nuestro archivo de texto, lo hariamos de la siguiente manera:

```python
#Ruta archivo prinicipal <- file
#Ruta carpeta que contiene el archivo principal <- dirname
base = os.path.dirname(__file__)
#Accedemos a la ruta de la carpeta de nuestro archivo <- base
#Subimos una carpeta <- ".."
#Accedemos a nuestro archivo de trabajo <- "data","macros.txt"
ruta = os.path.join(base,"..","data","macros.txt")
```

Ya con esto hecho el problema se fixearia asi:

```python
import os

base = os.path.dirname(__file__)
ruta = os.path.join(base,"..","data","macros.txt")
with open(ruta, "r") as f:
    contenido = f.read()
    print(contenido)
```

**Nota:** Siempre debemos importar el modulo os al inicio del codigo para poder acceder a funciones de este, utilizamos path, que es un submodulo de os, para poder acceder a las funciones de este, ya que es un modulo especializado en rutas; a conocimiento del lector, utilizamos el punto puesto que eso indica que uno esta dentro del otro ```os.path.dirname()``` os <- path <- dirname.






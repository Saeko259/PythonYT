#NOTAS GENERALES
#En python hay funciones que para acceder a determinado parametro, debes introducir el nombre del parametro que quiero alterar
#Por ejemplo, si quiero cambiar la manera en que se separan las palabras en un print, debo usar sep = "cambio"


#00 - print
#El modulo print nos permite imprimir informacion en la consola
#Sirve con una o dos comillas, dependera del contexto
print("Hola mundo")
#tambien puedo imprimir pasandolo por diferentes parametros, y por default los separa por un espacio
print("hola","mundo")
#Si quiero sobre escribir la manera en que se sobre escribe de manera determinada, puedo hacer lo siguiente
#usamos sep para el espacio entre palabras ingresadas como parametro dentro de un print
print("hola", "mundo", sep ="")
#Si quiero cambiar la manera en que interactuan dos prints, puedo utilizar end ="cambio", por default es un salto de linea


#01 - tipos de datos
#Podemos utlizar type() para que nos retone el tipo de datos de un valor
#En python NO tenemos que especificarle si es un entero , es decir, no tienes que utilizar una estructura con una memoria especifica "64 bits -32 bits etc"
print(type(1<2))
print(type(False))
#Datos tipo complejo
print(type(2 + 2j))
print(type(""))
#Elemento especial para ausencia de valor
print(type(None))


#03 - Casting de tipos - Transformar un tipo de un valor a otro
#Es un lenguaje de tipado fuerte, no va a transformar dos tipo de datos incompatibles de manera automatica
#Ejemplpo correcto
print(type(int("100")))
#EJemplo incorrecto (Del tipado fuerte)
#print("100" + 2)
#Retorna error, puesto que el mas es para concatenar cadenas tambien, y estas intentando operar con dos tipos incompatibles
#Ejemplo corregido:
print(int("100") + 2)
#Hay interacciones interesantes que son validas de mencionar, como por ejemplo la de float( decimal) a int (entero), es una funcion techo
#Al transformar numeros enteros a booleanos, el unico valor que nos va a retornar un valor de falso es el 0
#Las cadenas de texto vacias, retornan falso, el resto de valores, incluso un espacio en blano, retornan true


#BONUS MENTION
#La funcion round, que sirve para redondear, en python redondea al par mas cercano, cuando esta a la mitad entre dos enteros, sino, redondea de manera tradicional
print(round(2.5)) #Retorna 2
print(round(2.51))# Retorna 3
print(round(3.5))# Retorna 4
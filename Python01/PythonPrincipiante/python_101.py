#NOTAS GENERALES



#00 - print

print("Hola mundo")
#tambien puedo imprimir pasandolo por diferentes parametros, y por default los separa por un espacio
print("hola","mundo")
#Si quiero sobre escribir la manera en que se sobre escribe de manera determinada, puedo hacer lo siguiente
#usamos sep para el espacio entre palabras ingresadas como parametro dentro de un print
print("hola", "mundo", sep ="")
#Si quiero cambiar la manera en que interactuan dos prints, puedo utilizar end ="cambio", por default es un salto de linea


#01 - tipos de datos
#Podemos utlizar type() para que nos retone el tipo de datos de un valor
print(type(1<2))
print(type(False))
#Datos tipo complejo
print(type(2 + 2j))
print(type(""))
#Elemento especial para ausencia de valor
print(type(None))


#03 - Casting de tipos - Transformar un tipo de un valor a otro

#Ejemplpo correcto
print(type(int("100")))

#Retorna error, puesto que el mas es para concatenar cadenas tambien, y estas intentando operar con dos tipos incompatibles
#Ejemplo corregido:
print(int("100") + 2)

print(bool(0))
#BONUS MENTION
#La funcion round, que sirve para redondear, en python redondea al par mas cercano, cuando esta a la mitad entre dos enteros, sino, redondea de manera tradicional
print(round(2.5)) #Retorna 2
print(round(2.51))# Retorna 3
print(round(3.5))# Retorna 4

pr = "hola"
h= 5
#BONUS* - Fstring
#Hay veces que queremos formatear cadenas, y sobretodo escribir distintos tipos de datos
print(f"Hola me llamo {pr} y soy {h+2}")
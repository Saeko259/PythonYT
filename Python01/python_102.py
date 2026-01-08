#04 - variables - guardar datos en memoria
#En python es muy sencillo asignar valores de variables, solo pongo el nombre de la variable y su valor
#No hace falta decir que tipo de dato es y si va a ser variable o constante
primera_varible = "hola"
print(primera_varible)
primera_varible:str ="chao"
print(primera_varible)
h = 5
#Python no tiene constantes, es decir, no tiene variables que  no se cambien o no se dejen reasignar

#BONUS - Fstring
#Hay veces que queremos formatear cadenas, y sobretodo escribir distintos tipos de datos
print(f"Hola me llamo {primera_varible} y soy {h+2}")

#05 - INPUT
# Es una funcion que te permite obtener datos a traves de la consola
#Lo que este dentro del input es lo que se muestra al pedir el dato
valor = input("hola: ")
#Por default, el valor ingresado al input se categoriza como una cadena de texti
print(valor)
#Si queremos asignar varias variables a la vez, podemos usar split()
#El split por default separa por espacios
nombre,edad = input("Como te llamas y cuantos años tienes").split()
print(f"Me llamo {nombre} y tengo {edad} ")
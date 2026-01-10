#06 -CONDICIONALES
# Te dejan ejecutar determinados bloques de codigos tras que se cumplan ciertas condiciones
import os
os.system("clear")
#1. If
#Mira que no tiene punto y coma ni llaves, Funciona por IDENTACIONES
#1.1 El if puede ir acompañado de una sentencia llamada else, que seria lo que se ejecuta si no se cumple la condicion
edad = int(input("Cuantos años tienes ? "))
if ( edad >= 18):
    print("Eres mayor de edad")
else:
    print("No eres menor de edad :(")
#1.3 Elif: Cuando no se ejecuta la primera condicion, colocamos una segunda que podemos revisar para ver si esta se cumple ejecutar otro bloque de codigo
if ( edad >60):
    print("Estas viejo tio")
elif ( edad < 18):
    print("Estas joven chaval")
else:
    print("Estas en el punto perfecto bro :)")

#Tambien podemos contar con condiciones multiples, con conectores logicos como 'and' y 'or'
cosa = True
if edad >= 18 and cosa :
    print("Corre")
#Puedo usar not, para usar la negacion del resultado
#Operadores de comparacion: >, <, >=, <=, ==, !=

#Comparar cadenas
#Ejemplo:
print("locura" < "pera") 
#Esto arroja true, la razon es por que python compara letra a letra, por lo que si la primera letra tiene un indice diferente a la otra, se hace la comparacion necesaria
#Si esta es igual, pasa a la siguiente, y asi sucesivamente

#06 Condiciones ternarias
#Forma corta de if - elif - else
edad =18
#Primero escribimos el codigo que se ejecuta, despues, la condicion, y despues la condicion en caso de que arroje False
mensaje = "Eres mayor de edad" if edad >=18 else "Es menor de edad"
print ( mensaje)
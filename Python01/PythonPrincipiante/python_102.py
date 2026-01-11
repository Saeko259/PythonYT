#04 - variables - guardar datos en memoria

primera_varible = "hola"
print(primera_varible)
primera_varible:str ="chao"
print(primera_varible)
h = 5




#05 - INPUT
# Es una funcion que te permite obtener datos a traves de la consola
#Lo que este dentro del input es lo que se muestra al pedir el dato
valor = input("hola: ")

print(valor)
#Si queremos asignar varias variables a la vez, podemos usar split()
#El split por default separa por espacios
nombre,edad = input("Como te llamas y cuantos años tienes").split()
print(f"Me llamo {nombre} y tengo {edad} ")
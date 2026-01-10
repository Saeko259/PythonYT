#Programa que:
#Lea el archivo línea por línea usando readline(). Convierta cada línea en entero. Sume todos los números. Imprima el total
sum = 0
import os
base = os.path.dirname(__file__)
ruta = os.path.join(base,"ftexts","numeros.txt")

with open(ruta,"r") as f:
    lineas = f.readlines()
    
            
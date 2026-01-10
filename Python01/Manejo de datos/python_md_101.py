import os

base =os.path.dirname(__file__)
ruta = os.path.join(base,"ftexts", "textop.txt")

with open(ruta,"r") as f:
    contenido = f.read()
    print(contenido)



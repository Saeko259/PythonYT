import os

base = os.path.dirname(__file__)
ruta = os.path.join(base, "ftexts","nombres.txt")

with open(ruta, "w") as f:
    f.write("Ana \n")
    f.write("Luis \n")
    f.write("Carlos \n")
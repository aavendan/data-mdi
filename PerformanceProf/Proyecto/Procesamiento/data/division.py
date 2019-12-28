import os, shutil
"""
rutaParcial = "../detalle/"
rutasNuevas = ["../Enmanuel/", "../Diana/", "../Josue/", "../Andres/"]

ind = 0
print("Iniciando copias. . .")
for nombreArchivo in os.listdir(rutaParcial):
    print(ind)
    src = rutaParcial + nombreArchivo
    dst = rutasNuevas[ind] + nombreArchivo
    shutil.copyfile(src,dst)
    ind = ind+1 if ind < 3 else 0
print("Finaliza copias. . .")
"""
d = {'x': {'y': [1,2,3]}, 'a': {'u': [6,8,5]}}
d2= {'x': {'aa': [21,32,43]}, 'a': {'oo': [6,8,5]}}

d.update(d2)
print(d)
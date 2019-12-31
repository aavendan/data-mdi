import funciones as fn
import os
from os import path
import json
"""
for clave in dicProfs.keys():
    if clave.find("JURADO") !=-1:
        print(clave)
print(dicProfs["DAVID ALONSO JURADO MOSQUERA"])
"""

dicTPuntero = open("resultados/comentariosAnalizadosTT.txt", "r", encoding='UTF-8')
dicTexto = dicTPuntero.readline()
# dicTextoPlano = dicTexto.replace("'", "\"")
dicPC = dict(json.loads(dicTexto))

fn.comentProfbyTone("MARCO TULIO MEJIA CORONEL", "anger", dicPC)
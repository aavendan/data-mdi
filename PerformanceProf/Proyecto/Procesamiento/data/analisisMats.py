import json
from os import path
import funciones as fn

dicMaterias = {}
ruta = "resultados/rankingMatProf.txt"

if False:
    print("hola")
    archPunt = open(ruta, "r", encoding="UTF-8")
    archPunt = archPunt.readline()
    dicMaterias = dict(json.loads(archPunt))
else:
    dicTPuntero = open("resultados/comentariosAnalizadosTT.txt", "r", encoding='UTF-8')
    dicTexto = dicTPuntero.readline()
    # dicTextoPlano = dicTexto.replace("'", "\"")
    dicPC = dict(json.loads(dicTexto))
    print(len(dicPC.keys()))
    fn.rankingMats(dicPC, dicMaterias)
    print("hola")
    archPerfiles = open(ruta, "w", encoding="UTF-8")
    archPerfiles.write(json.dumps(dicMaterias))

"""
for clave in dicProfs.keys():
    if clave.find("JURADO") !=-1:
        print(clave)
print(dicProfs["DAVID ALONSO JURADO MOSQUERA"])
"""

top = 10
cc = 0
listaT = ["joy", "fear", "sadness", "anger", "confident", "analytical", "tentative"]
fn.presentRankingProf(listaT, top, dicMaterias, "top_materias")





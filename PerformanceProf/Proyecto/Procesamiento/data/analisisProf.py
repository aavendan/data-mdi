import json
from os import path
import funciones as fn

dicProfs = {}
ruta = "resultados/rankingProf.txt"

if path.exists(ruta):
    archPunt = open(ruta, "r", encoding="UTF-8")
    archPunt = archPunt.readline()
    dicProfs = dict(json.loads(archPunt))
else:
    dicTPuntero = open("resultados/comentariosAnalizadosTT.txt", "r", encoding='UTF-8')
    dicTexto = dicTPuntero.readline()
    # dicTextoPlano = dicTexto.replace("'", "\"")
    dicPC = dict(json.loads(dicTexto))
    print(len(dicPC.keys()))
    fn.rankingProf(dicPC, dicProfs)

    archPerfiles = open("resultados/rankingProf.txt", "w", encoding="UTF-8")
    archPerfiles.write(json.dumps(dicProfs))

"""
for clave in dicProfs.keys():
    if clave.find("JURADO") !=-1:
        print(clave)
print(dicProfs["DAVID ALONSO JURADO MOSQUERA"])
"""
top = 50
listaT = ["joy", "fear", "sadness", "anger", "confident", "analytical", "tentative"]
fn.presentRankingProf(listaT, top, dicProfs, "top_global")
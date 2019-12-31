import json
from os import path
import funciones as fn

dicProfs = {}
ruta = "resultados/rankingMatProf.txt"

if False:
    print("hola")
    archPunt = open(ruta, "r", encoding="UTF-8")
    archPunt = archPunt.readline()
    dicProfs = dict(json.loads(archPunt))
else:
    dicTPuntero = open("resultados/comentariosAnalizadosTT.txt", "r", encoding='UTF-8')
    dicTexto = dicTPuntero.readline()
    # dicTextoPlano = dicTexto.replace("'", "\"")
    dicPC = dict(json.loads(dicTexto))
    print(len(dicPC.keys()))
    fn.rankingSemProf(dicPC, dicProfs)
    print("hola")
    archPerfiles = open(ruta, "w", encoding="UTF-8")
    archPerfiles.write(json.dumps(dicProfs))

"""
for clave in dicProfs.keys():
    if clave.find("JURADO") !=-1:
        print(clave)
print(dicProfs["DAVID ALONSO JURADO MOSQUERA"])
"""

top = 40
cc = 0

for clave in dicProfs.keys():

    listaT = ["joy", "fear", "sadness", "anger", "confident", "analytical", "tentative"]
    anio, termino = clave.split("_")

    if (anio == "2018" or anio == "2019") and (termino == "1S" or termino == "2S"):
        print()
        print("\n\nRanking de %s" % clave)
        fn.presentRankingProf(listaT, top, dicProfs[clave], "top_sem_anio_"+clave)

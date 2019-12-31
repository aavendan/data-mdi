import json
from os import path
import funciones as fn

dicTPuntero = open("resultados/procFinalSC.txt", "r", encoding='UTF-8')
dicTexto = dicTPuntero.readline()
#dicTextoPlano = dicTexto.replace("'", "\"")
dicDinamico = json.loads(dicTexto)

listaTps = []
fn.dictToTuple(dicDinamico, listaTps)
listaTps.sort(key=lambda tup: tup[0], reverse=True)

long = len(listaTps)
nPrimeros = 100
ind = 1
b = False
extraPerf = 0
pathPerf = "resultados/top"
pathPR = fn.pathUnique(pathPerf)
if b: archioF = open(pathPR, "w", encoding="UTF-8")

while ind <= nPrimeros and long:
    punt = listaTps[ind][0]
    coment = listaTps[ind][1]
    if len(coment) < 85:
        print("Comentario N° %d \t-> %s" %(ind,listaTps[ind]))
        formt = str(listaTps[ind][0]) + "," + str(listaTps[ind][1])
        if b: archioF.write(formt+"\n")
    ind+=1

"""
for ind in range(nPrimeros):
    punt = listaTps[ind][0]
    coment = listaTps[ind][1]
    if len(coment) < 50:
        print(listaTps[ind])
"""
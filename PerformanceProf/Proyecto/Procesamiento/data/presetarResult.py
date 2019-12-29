import json
import funciones as fn

dicTPuntero = open("procFinal.txt", "r", encoding='UTF-8')
dicTexto = dicTPuntero.readline()
#dicTextoPlano = dicTexto.replace("'", "\"")
dicDinamico = json.loads(dicTexto)

listaTps = []
fn.dictToTuple(dicDinamico, listaTps)
listaTps.sort(key=lambda tup: tup[0], reverse=True)

nPrimeros = 30
for ind in range(nPrimeros):
    punt = listaTps[ind][0]
    coment = listaTps[ind][1]
    if len(coment) <= 50:
        print(listaTps[ind])
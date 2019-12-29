import funciones as fn
from nltk.tokenize import sent_tokenize, word_tokenize
import os
import math as mt
import json
import gensim as gn
from gensim.models import Word2Vec

dicTPuntero = open("comentariosAnalizadosTT.txt", "r", encoding='UTF-8')
dicTexto = dicTPuntero.readline()
dicTextoPlano = dicTexto.replace("'", "\"")
dicDinamico = json.loads(dicTexto)


listaPerf = []
fn.procesadorDic(dicDinamico, listaPerf)
cont = " ".join(listaPerf).replace("\n", " ")
#cont = " ".join(listaPerf).replace("\n", " ").replace(",", ".")

archPerfiles = open("lista_perfiles.txt", "w", encoding="UTF-8")
archPerfiles.write(str(listaPerf))
print("paso")
data = []
fn.tokenizar(cont, data)
print("paso2")
#aqui se crea el modelo segun la data ingresada
model = Word2Vec(data, min_count=1, size = 100, window = 10, sg=1)
print("Tamanio data %d" %(len(data)))

dicS = {}
similitud = 0.65
fn.evaluarSimilitud(data, dicS, model, similitud)
archioF = open("procFinal.txt", "w", encoding="UTF-8")
archioF.write(json.dumps(dicS))

listaTps = []
fn.dictToTuple(dicS, listaTps)
listaTps.sort(key=lambda tup: tup[0], reverse=True)
print(listaTps)





'''
print(data[-1])
print(data[-2])
print(model.similarity(data[-1][0], data[-2][0]))
print("-----")

similitud = 0.975
dicS = {}

fn.evaluarSim(data, dicS, model, similitud)
listaTps = []
fn.dictToTuple(dicS, listaTps)
listaTps.sort(key=lambda tup: tup[0], reverse=True)
print(listaTps)
'''


'''
archPerfiles = open("perfiles.txt", "w", encoding="UTF-8")
archPerfiles.write(str(listaPerf))
print(listaPerf)
print(listaPerf[0])
model = Word2Vec(listaPerf, min_count=1,size= 50,workers=3, window =3, sg = 1)

print(model.)


dicFrec = {}
fn.calcFrecuencia(listaPerf, dicFrec)
listTuplas = []
fn.dictToTuple(dicFrec, listTuplas)
listTuplas.sort(key=lambda tup: tup[0], reverse=True)
#sorted(listTuplas, key=fn.getKey)
print(listTuplas)

#archPerfiles = open("perfiles.txt", "w", encoding="UTF-8")
#archPerfiles.write(str(listaPerf))
'''
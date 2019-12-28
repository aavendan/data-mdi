import funciones as fn
from nltk.tokenize import sent_tokenize, word_tokenize
import os
import json
import gensim as gn
from gensim.models import Word2Vec

dicTPuntero = open("comentariosAnalizadosT.txt", "r", encoding='UTF-8')
dicTexto = dicTPuntero.readline()
dicTextoPlano = dicTexto.replace("'", "\"")
dicDinamico = json.loads(dicTexto)

print(dicDinamico)
print(type(dicDinamico))

listaPerf = []
fn.procesadorDic(dicDinamico, listaPerf)
#cont = " ".join(listaPerf).replace("\n", " ")
cont = " ".join(listaPerf).replace("\n", " ").replace(",", ".")
print(cont)
data = []
for i in sent_tokenize(cont):
    temp = []

    for j in word_tokenize(i):
        temp.append(j.lower())

    data.append(temp)

print(data[:10])
model = Word2Vec(data, min_count=1, size = 100, window = 5, sg = 1)
print("Tamanio data %d" %(len(data)))
#print(str(model[data[0]]))

similitud = 0.975

dicS = {}
fn.evaluarSim(data, dicS, model, similitud)
listaTps = []
fn.dictToTuple(dicS, listaTps)
listaTps.sort(key=lambda tup: tup[0], reverse=True)
print(listaTps)

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
import json
import funciones as fn

dicTPuntero = open("resultados/procFinalCC.txt", "r", encoding='UTF-8')
dicTexto = dicTPuntero.readline()
#dicTextoPlano = dicTexto.replace("'", "\"")
dicDinamico = json.loads(dicTexto)
dicDinamico = dict(dicDinamico)

textObjetivo = "conoce la materia de manera muy actualizada".replace(".", "").strip(" ")
pathArchPerf = "resultados/"+textObjetivo
archiCO = open("resultados/"+textObjetivo+".txt","w", encoding="UTF-8")

for clave in dicDinamico.keys():
    clave = str(clave)
    if clave.find(textObjetivo) != -1:
        print(clave)
        archiCO.write(clave)
        break
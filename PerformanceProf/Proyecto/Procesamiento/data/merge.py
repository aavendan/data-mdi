import funciones as fn
import os
import json

rutaParcial = "respaldo/"
print("Leyendo diccionarios. . .")
listDicc = []
n = 0
for nombreArchivo in os.listdir(rutaParcial):
    print()
    rutaCompleta = os.path.join(rutaParcial, nombreArchivo)
    dicPunteroArchivo = open(rutaCompleta, "r", encoding="UTF-8")
    dicTextoPlano = dicPunteroArchivo.readline()
    print(dicTextoPlano)
    dic = dicTextoPlano.replace("'", "\"")
    dicDinamico = json.loads(dicTextoPlano)
    listDicc.append(dicDinamico)

dictFinal = fn.funsionDicionarios(listDicc)
archivo = open("comentariosAnalizadosTT.txt", "w", encoding="UTF-8")
print(dictFinal)
archivo.write(json.dumps(dictFinal))
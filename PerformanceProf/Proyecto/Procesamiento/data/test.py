import funciones as fn
import os
import json

rutaParcial = "../detalle/"
dicc = {}
cantComents = 0
limite = 0
b=True
print("Leyendo archivos y creando diccionario. . .")


for nombreArchivo in os.listdir(rutaParcial):

    rutaCompleta = os.path.join(rutaParcial, nombreArchivo)
    archivo = open(rutaCompleta, "r", encoding='UTF-8')
    nombreArchivo = nombreArchivo.replace(".txt", "")
    if nombreArchivo.find("-CHECKED") == -1:
        indTermino = nombreArchivo.find("1S") if nombreArchivo.find("1S") != -1 else nombreArchivo.find("2S")

        termino = nombreArchivo[indTermino:]
        anio = nombreArchivo[indTermino-4:indTermino]
        codigoMat = nombreArchivo[:indTermino-4]
        #IDIG200710220171S
        todo = codigoMat+anio+termino
        if todo==("IDIG200710220171S") != -1:
            print(codigoMat+anio+termino)
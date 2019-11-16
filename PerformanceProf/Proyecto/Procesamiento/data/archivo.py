import funciones as fn
import os
import json
#Credenciales API SentiDetector
'''
curl -X POST -u "apikey:HGQfgUKC9Fqzjd1ByZlA2SUeovZaAz0G-veawWHILSLj" \
--header "Content-Type: application/json" \
--data-binary @{path_to_file}tone.json \
"https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21"

'''

rutaParcial = "../detalle/"
dicc = {}
cantComents = 0
limite = 0
print("Cargando y limpiando comentarios. . .")

for nombreArchivo in os.listdir(rutaParcial):

    rutaCompleta = os.path.join(rutaParcial, nombreArchivo)
    archivo = open(rutaCompleta, "r", encoding='UTF8')
    nombreArchivo = nombreArchivo.replace(".txt", "")

    indTermino = nombreArchivo.find("1S") if nombreArchivo.find("1S") != -1 else nombreArchivo.find("2S")

    termino = nombreArchivo[indTermino::]
    anio = nombreArchivo[indTermino-4:indTermino]
    codigoMat = nombreArchivo[:indTermino-4]

    profesor = archivo.readline().replace(",", " ").replace("\n", "")

    if anio == "2018":

        archivo.readline()
        archivo.readline()

        comentarios = archivo.readlines()
        comentsLimpios = []

        for comentario in comentarios:
            comentario = comentario.replace("\n", "")
            if len(comentario) > 6:
                cm =fn.separarPalabras(comentario)
                if len(cm) > 6:
                    comentsLimpios.append(cm)
        limite += len(comentsLimpios)
        if len(comentsLimpios) > 1 and limite < 15:
            cantComents += len(comentsLimpios)

            dicComents = fn.dicSentiComents(comentsLimpios)


            dicc = fn.llenarDiccionario(profesor, codigoMat, termino, anio, dicComents, dicc)


j = {"outputs":[{"output":"Hello world!","stats":{"elapsed_time":318,"nb_characters":11,"nb_tokens":3,"nb_tus":1,"nb_tus_failed":0}}]}

print(dicc)

#print(fn.traducir(["Hola mundo!", "Segunda prueba"]))
#print(dicc.get("ROCÍO ELIZABETH MERA SUÁREZ"))
#print("Cantidad de comentarios dle 2018: " + str(cantComents))


#Tambien se puede simplicar palabras como muuuuy a muy
#sin embargo creo que esto si es significativo para nuestro estudio

'''
comentsTrad = fn.traducir(comentsLimpios)
            dicComents = {}

            for i in range(len(comentsTrad["outputs"])):

                coment = comentsTrad["outputs"][i]["output"]

                print("Comentario traducido a analizar: " + coment)
                print("\n")
                
                dicSenti = fn.detectasSentimientos(coment)
                limite += 1
                dicTonoComent = {}

                for dicTono in dicSenti["document_tone"]["tones"]:
                    dicTonoComent[dicTono["tone_name"]] = dicTono["score"]

                dicComents[coment] = dicTonoComent

'''
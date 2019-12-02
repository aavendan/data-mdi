import funciones as fn
import os
import json

rutaParcial = "../detalle/"
dicc = {}
cantComents = 0
limite = 0
print("Leyendo archivos y creando diccionario. . .")

for nombreArchivo in os.listdir(rutaParcial):

    rutaCompleta = os.path.join(rutaParcial, nombreArchivo)
    archivo = open(rutaCompleta, "r", encoding='UTF8')
    nombreArchivo = nombreArchivo.replace(".txt", "")
    if nombreArchivo.find("-CHECKED") == -1:
        indTermino = nombreArchivo.find("1S") if nombreArchivo.find("1S") != -1 else nombreArchivo.find("2S")

        termino = nombreArchivo[indTermino::]
        anio = nombreArchivo[indTermino-4:indTermino]
        codigoMat = nombreArchivo[:indTermino-4]

        profesor = archivo.readline().replace(",", " ").replace("\n", "")

        if anio == "2018" or "2019":

            archivo.readline()
            archivo.readline()

            comentarios = archivo.readlines()
            comentsLimpios = []

            for comentario in comentarios:

                comentario = comentario.replace("\n", "")
                if len(comentario) > 0:
                    cm =fn.separarPalabras(comentario)
                    if len(cm) > 4:
                        comentsLimpios.append(cm)
            limite += len(comentsLimpios)

            if len(comentsLimpios) > 0 and limite < 2300:
                cantComents += len(comentsLimpios)

                dicComents = fn.dicSentiComents(comentsLimpios)
                #dicComents = {"c": comentsLimpios}
                dicc = fn.llenarDiccionario(profesor, codigoMat, termino, anio, dicComents, dicc)
        archivo.close()
        os.rename(rutaCompleta, rutaParcial + nombreArchivo + "-CHECKED.txt")
        #os.rename(rutaCompleta, rutaParcial+nombreArchivo.replace("-CHECKED", "")+".txt")

dic = open("resultados.txt", "w", encoding="UTF8")
dic.write(json.dumps(dicc))

#print(json.loads())


print("Cantidad de comentarios: %d" %cantComents)
#print(fn.traducir(["Hola mundo!", "Segunda prueba"]))
#print(dicc.get("ROCÍO ELIZABETH MERA SUÁREZ"))
#print("Cantidad de comentarios dle 2018: " + str(cantComents))
#j = {"outputs":[{"output":"Hello world!","stats":{"elapsed_time":318,"nb_characters":11,"nb_tokens":3,"nb_tus":1,"nb_tus_failed":0}}]}

#Tambien se puede simplicar palabras como muuuuy a muy
#sin embargo creo que esto si es significativo para nuestro estudio
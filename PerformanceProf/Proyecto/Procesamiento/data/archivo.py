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

    try:
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
                        comentsLimpios.append(comentario)
                limite += len(comentsLimpios)

                if len(comentsLimpios) > 0 and limite < 2400:

                    cantComents += len(comentsLimpios)
                    dicComents = fn.dicSentiComents(comentsLimpios)
                    #dicComents = {"c": comentsLimpios}

                    dicc = fn.llenarDiccionario(profesor, codigoMat, termino, anio, dicComents, dicc)
                else:
                    print("Llegue al limite: " + str(limite))
                    break
            archivo.close()
            os.rename(rutaCompleta, rutaParcial + nombreArchivo + "-CHECKED.txt")
            #os.rename(rutaCompleta, rutaParcial+nombreArchivo.replace("-CHECKED", "")+".txt")

    except Exception as ex:
        archivo.close()
        dic = open("resultados.txt", "w", encoding="UTF8")
        dic.write(json.dumps(dicc))
        print("Error en la API")
        b=False

if b:
    dic = open("resultados.txt", "w", encoding="UTF8")
    dic.write(json.dumps(dicc))

#print(json.loads())
"""

#txt = "Deber\u00eda existir mas profesores como la Miss Burgos, le gusta la catedra y da todo en cada una de sus clases, ella es consciente de que esta formando profesionales que saldr\u00e1n al exterior. La manera de dar sus clases hace que cualquiera ame la materia por mucho que no le guste. Ojala todos los profesores fueran como ella paciente, muy disciplinada, correcta y sobre todo con pasi\u00f3n por la educaci\u00f3n"



archivo = open("respaldo/resultados1.txt", "r", encoding='UTF-8')
print(archivo)
dic = json.loads(" ".join([ x.replace("\n", "") for x in archivo.readlines()]))
lista = []
fn.procesadorDic(dic, lista)
print(lista)
a = open("respaldo/perfilesTest.txt", "w", encoding='UTF-8')
a.write(" | ".join(lista))
a.close()
archivo.close()

#print(fn.traducir(["Hola mundo!", "Segunda prueba"]))
#print(dicc.get("ROCÍO ELIZABETH MERA SUÁREZ"))
#print("Cantidad de comentarios dle 2018: " + str(cantComents))
#j = {"outputs":[{"output":"Hello world!","stats":{"elapsed_time":318,"nb_characters":11,"nb_tokens":3,"nb_tus":1,"nb_tus_failed":0}}]}

#Tambien se puede simplicar palabras como muuuuy a muy
#sin embargo creo que esto si es significativo para nuestro estudio
"""
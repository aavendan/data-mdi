import funciones as fn
import os

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

print("Cargando y limpiando comentarios. . .")
'''
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
        # Comentario
        # Linea para salta los especios para llegar al primer comentario
        archivo.readline()
        archivo.readline()

        comentarios = archivo.readlines()
        comentsLimpios = []

        for comentario in comentarios:
            comentario = comentario.replace("\n", "")
            if len(comentario) > 0:
                # 1.Filto las Stopwords

                # 2.Sepracion de palabras
                comentsLimpios.append(fn.separarPalabras(comentario))

        if len(comentsLimpios) > 0:
            cantComents += len(comentsLimpios)
            dicc = fn.llenarDiccionario(profesor, codigoMat, termino, anio, comentsLimpios, dicc)
'''
#print(fn.traducir("Hello World!"))

print(fn.tra())
#print(dicc.get("ROCÍO ELIZABETH MERA SUÁREZ"))
print("Cantidad de comentarios dle 2018: " + str(cantComents))


#Tambien se puede simplicar palabras como muuuuy a muy
#sin embargo creo que esto si es significativo para nuestro estudio
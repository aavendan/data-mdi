import re
import json
import numba
import requests
import os
from os import path
import collections.abc
from numba import njit, cuda
from numba.typed import List
from numba.typed import Dict
from nltk.corpus import wordnet
from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from ibm_watson import ToneAnalyzerV3
from nltk.tokenize import word_tokenize
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Credenciales API SentiDetector

def topTono(tonoOB, dicP, dicR):

    for profesor in dicP.keys():
        for tono in dicP[profesor].keys():
            if tono.lower() == tonoOB.lower():
                dicR[profesor] = dicP[profesor][tono]


def comentProfbyTone(profesorOB, tonoOB, dic_coments):

    for profesor in dic_coments.keys():

        if profesor == profesorOB:
            for codigoMat in dic_coments[profesor].keys():

                for anio in dic_coments[profesor][codigoMat].keys():

                    for termino in dic_coments[profesor][codigoMat][anio].keys():

                        dic_comment = dic_coments[profesor][codigoMat][anio][termino]

                        for comenentario, dicTone in dic_comment.items():

                            for tono in dicTone.keys():
                                if tono.lower() == tonoOB.lower():
                                    print(comenentario)


def getKey(item):
    return item[0]


def tokenizar(text, lista):

    for i in sent_tokenize(text):
        temp = []
        for j in word_tokenize(i):
            temp.append(j.lower())
        lista.append(temp)


def pathUnique(pathArchPerf):
    extraArchPerf = 0
    while path.exists(pathArchPerf + str(extraArchPerf) + ".txt"):
        extraArchPerf += 1
    return pathArchPerf + str(extraArchPerf) + ".txt"


def evaluarSimilitud(data, dic, model, similitud):

    total = len(data)
    c = 0
    cc = 0
    for tokI in data:
        print("Porcentaje de avance %.2f" %((cc/total)*100))
        if c < 10:
            cont = 0
            for tokF in data:
                if tokI != tokF and cont < 100:
                    if similitudHibrida(tokI, tokF, model) >= similitud:
                        contDic(" ".join(tokI), dic)
                    #cont += 1
                else:
                    break
            #c += 1
        else:
            break
        cc+=1


def similitudHibrida(tokI, tokF, model):
    """
    Aqui determino cual oracion es la mas corta para limpiar las stop words y en las palabaras que "sobreviven"
    buscar si tienen sinonimos en otra oracion (que es mas corta)
    """
    long = min(len(tokI), len(tokF))
    ls1 = limpiarStopWords(" ".join(tokI)).split(" ") if len(tokI) == long \
        else limpiarStopWords(" ".join(tokF)).split(" ")
    ls2 = (" ".join(tokI)) if len(tokI) != long else (" ".join(tokF))

    #determino la similitud de palabra por palabra
    acumSimilitud = 0
    long = min(len(tokI), len(tokF))
    for i in range(long):
        acumSimilitud += model.similarity(tokI[i], tokF[i])
    """
    Itero en la lsita de palabras y busca si tiene sinonimos en la oracion, si tiene entonces al
    acumulador que tenia arrivale sumo 1 para expresar que tiene mas relevancia porque comaprte una idea con otro comentario diferente
    """
    for w1 in ls1:
        # esta funcion recibe la palabra y la oracion donde va a buscar sinonimos
        syn = get_word_synonyms_from_sent(w1, ls2)
        if len(syn) > 0:
            long += 1
            acumSimilitud += 1

    # aqui esta el promedio de similtud palabra por palabra, este es el promedio que es mas acertado, el que
    # toma toda la oracion y mira la similitud no es tan efectivo
    similitud = acumSimilitud / long
    return similitud


def totalTones(profesor, dicProfs):

    dic = dicProfs[profesor]
    total = 0
    for tono in dic.keys():
        total += dic[tono]
    return  total


def presentRankingProf(listTonos, top, dicProfs, descp):

    for tono in listTonos:
        print()
        print("Racking profesor con tono %s" %tono)
        dicRJ = {}
        topTono(tono, dicProfs, dicRJ)
        listRJ = []
        dictToTuple(dicRJ, listRJ)

        archivo = open("resultados/"+descp+"/top"+str(top)+"_"+tono+".txt", "w", encoding="UTF-8")
        listRJ2 = []
        for tupla in listRJ:
            valor = tupla[0]
            profesor = tupla[1]
            porcentaje = (valor/totalTones(profesor, dicProfs))*100
            tuplaN = (porcentaje, profesor)
            listRJ2.append(tuplaN)
        listRJ2.sort(key=lambda tup: tup[0], reverse=True)
        ind = 0
        while ind < len(listRJ2) and ind < top:
            profesor = listRJ2[ind][1]
            total = totalTones(profesor, dicProfs)
            cant = listRJ2[ind][0]*total
            t = "%"
            print("Posición N° %d es %s con %d%s tonos %s (%d)" % (ind+1, profesor, listRJ2[ind][0], t
                                                                   ,tono.upper(), cant))
            archivo.write(str(ind+1)+","+listRJ2[ind][1]+","+str(round(listRJ2[ind][0],2))+","+str(round(cant, 0))+"\n")
            ind+=1
        archivo.close()


def presentRankingProf2(listTonos, top, dicProfs, descp):

    for tono in listTonos:
        print()
        print("Racking profesor con tono %s" %tono)
        dicRJ = {}
        topTono(tono, dicProfs, dicRJ)
        listRJ = []
        dictToTuple(dicRJ, listRJ)
        if not os.path.exists("resultados/"+descp+"/"):
            os.mkdir("resultados/"+descp+"/")
            print("Directory ", "resultados/"+descp+"/", " Created ")
        else:
            print("Directory ", "resultados/"+descp+"/", " already exists")
        archivo = open("resultados/"+descp+"/top"+str(top)+"_"+tono+".txt", "w", encoding="UTF-8")
        listRJ2 = []
        for tupla in listRJ:
            valor = tupla[0]
            profesor = tupla[1]
            porcentaje = (valor/totalTones(profesor, dicProfs))*100
            tuplaN = (porcentaje, profesor)
            listRJ2.append(tuplaN)
        listRJ2.sort(key=lambda tup: tup[0], reverse=True)
        ind = 0
        while ind < len(listRJ2) and ind < top:
            profesor = listRJ2[ind][1]
            total = totalTones(profesor, dicProfs)
            cant = listRJ2[ind][0]*total
            t = "%"
            print("Posición N° %d es %s con %d%s tonos %s (%d)" % (ind+1, profesor, listRJ2[ind][0], t
                                                                   ,tono.upper(), cant))
            archivo.write(str(ind+1)+","+listRJ2[ind][1]+","+str(round(listRJ2[ind][0],2))+","+str(round(cant, 0))+"\n")
            ind+=1
        archivo.close()


def evaluarSimDEPRECATED(data, dic, model, similitud):

    c = 0
    for tokI in data:

        if c < 15:
            cont = 0
            for tokF in data:
                if tokI != tokF and cont < 50:
                    sim = model.n_similarity(tokI, tokF)
                    print(sim)
                    if sim > similitud:
                        contDic(" ".join(tokI), dic)
                    cont+=1
                else:
                    break
            c+=1
        else: break


def contDic(tok, dic):

    if tok in dic:
        dic[tok] = dic[tok] + 1
    else:
        dic[tok] = 1


def calcFrecuencia(listTexto, d):

    for line in listTexto:


        line = line.strip()
        line = line.lower()
        listaPalabra = line.split(" ")

        for palabra in listaPalabra:

            if palabra in d:
                d[palabra] = d[palabra] + 1
            elif len(palabra) > 2:
                d[palabra] = 1


def dictToTuple(dic, listTuplas):

    dic = dict(dic)

    for clave in dic.keys():
        valor = dic.get(clave)
        tupla = (valor, clave)
        listTuplas.append(tupla)
    sorted(listTuplas)

def dictToTuple2(dic, listTuplas):

    dic = dict(dic)

    for clave in dic.keys():
        valor = dic.get(clave)
        tupla = (valor, clave)
        listTuplas.append(tupla)
    sorted(listTuplas)


def get_word_synonyms_from_sent(word, sent):
    word_synonyms = []
    for synset in wordnet.synsets(word, lang='spa'):
        for lemma in synset.lemma_names(lang='spa'):
            if lemma in sent and lemma != word:
                word_synonyms.append(lemma)
    return word_synonyms


def limpiarStopWords(comentario):
    # Coloco aqui esta linea para que no se ejecute cada vez que se llama a la funcion
    stop_words = set(stopwords.words('spanish'))
    comentario = comentario.replace("\n", "")
    oraciones = word_tokenize(comentario)
    comentFiltrado = [w for w in oraciones if not w in stop_words]
    return " ".join(comentFiltrado)


def separarPalabras(comentFiltrado):

    return " ".join(re.findall("[A-Z][^A-Z]*", comentFiltrado))


def llenarDiccionario(profesor, codigoMat, termino, anio, comentsLimpios, dicc):

    if profesor not in dicc.keys():
        dicc[profesor] = {codigoMat: {anio: {termino: comentsLimpios}}}
    else:
        if codigoMat not in dicc[profesor].keys():
            dicc[profesor][codigoMat] = {anio: {termino: comentsLimpios}}
        else:
            if anio not in dicc[profesor][codigoMat].keys():
                dicc[profesor][codigoMat][anio] = {termino: comentsLimpios}
            else:
                if termino not in dicc[profesor][codigoMat][anio].keys():
                    dicc[profesor][codigoMat][anio][termino] = comentsLimpios
                else:
                    dicc[profesor][codigoMat][anio][termino].extend(comentsLimpios)

    return dicc


def dicSentiComents(comentsLimpios):
    print(comentsLimpios)
    comentsTrad = traducir(comentsLimpios)
    dicComents = {}
    print(comentsTrad)
    cant = len(comentsTrad["outputs"])

    for i in range(cant):

        coment = comentsTrad["outputs"][i]["output"]

        print("Comentario traducido a analizar: " + coment)
        print("\n")

        dicSenti = detectasSentimientos(coment)

        dicTonoComent = {}

        for dicTono in dicSenti["document_tone"]["tones"]:
            dicTonoComent[dicTono["tone_name"]] = dicTono["score"]

        dicComents[comentsLimpios[i]] = dicTonoComent

    return dicComents


def detectasSentimientos(comentario):

    authenticator = IAMAuthenticator('iY5ckIMqjpE0I6WHh39IYqt-1we_ehOsbLu8T2K4sxIQ')

    tone_analyzer = ToneAnalyzerV3(version='2017-09-21',authenticator=authenticator)
    tone_analyzer.set_service_url("https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/6034d1f9-1d05-49b3-b712-4c31cf658c02")
    try:

        tone_analysis = tone_analyzer.tone({'text': comentario},content_type='application/json').get_result()
    except Exception as ex:
        raise Exception("Error Detectar Sentimientos")

    #result = json.dumps(tone_analysis, indent=2)
    return tone_analysis


def traducir(text):


    url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"

    querystring = {"source": "es", "target": "en", "input": text}

    headers = {
        'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
        'x-rapidapi-key': "164510071emsh408bcd356f7658fp101d89jsn0c050d7a8c78"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def procesadorDic(dic_coments, lista_comments):
    #cojer a todos los quer tiene analitico o critico
    for profesor in dic_coments.keys():

        for codigoMat in dic_coments[profesor].keys():

            for anio in dic_coments[profesor][codigoMat].keys():

                for termino in dic_coments[profesor][codigoMat][anio].keys():

                    dic_comment = dic_coments[profesor][codigoMat][anio][termino]

                    for comenentario,dicTone in dic_comment.items():
                        if "Analytical" in dicTone.keys() or "Confident" in dicTone.keys():
                            comenentario = str(comenentario).replace("'", "")
                            listaOraciones = []
                            lT = []
                            if comenentario.find(".") != -1:
                                l1 = comenentario.split(".")

                                if len(l1) >= 2:
                                    for oracion in l1:
                                        if oracion.find(",") != 1:
                                            l2 = oracion.split(",")
                                            lT.extend(l2)
                                        else:
                                            lT.extend(oracion)
                                else:
                                    lT.extend(l1)
                            else:
                                lT = [comenentario]
                            lista_comments.extend(lT)
                            #lista_comments.append(str(comenentario).lower()) #Extraer adjetivos


def procesadorDic2(dic_coments, lista_comments):
    #cojer a todos los quer tiene analitico o critico
    for profesor in dic_coments.keys():

        for codigoMat in dic_coments[profesor].keys():

            for anio in dic_coments[profesor][codigoMat].keys():

                for termino in dic_coments[profesor][codigoMat][anio].keys():

                    dic_comment = dic_coments[profesor][codigoMat][anio][termino]

                    for comenentario,dicTone in dic_comment.items():
                        if "Analytical" in dicTone.keys() or "Confident" in dicTone.keys():
                            comenentario = str(comenentario).replace("'", "")
                            
                            lista_comments.append(str(comenentario).lower()) #Extraer adjetivos


def llenarRanking(profesor, dicTones, dicT):

    if profesor not in dicT.keys():

        dicT[profesor] = {}
        for tono in dicTones.keys():
            dicT[profesor][tono] = 1
    else:
        for tono in dicTones.keys():
            if tono not in dicT[profesor].keys():
                dicT[profesor][tono] = 1
            else:
                dicT[profesor][tono] = dicT[profesor][tono] + 1


def rankingProf(dic_coments, dicTonesProf):

    # cojer a todos los quer tiene analitico o critico
    for profesor in dic_coments.keys():

        for codigoMat in dic_coments[profesor].keys():

            for anio in dic_coments[profesor][codigoMat].keys():

                for termino in dic_coments[profesor][codigoMat][anio].keys():

                    dic_comment = dic_coments[profesor][codigoMat][anio][termino]

                    for comenentario, dicTone in dic_comment.items():

                        llenarRanking(profesor, dicTone, dicTonesProf)


def llenarRankingSem(anio, termino, profesor, dicTones, dicT):

    termino = anio+"_"+termino
    if termino not in dicT:
        dicT[termino] = {profesor : {}}

        for tono in dicTones.keys():
            dicT[termino][profesor][tono] = 1
    else:
        if profesor not in dicT[termino].keys():

            dicT[termino][profesor] = {}
            for tono in dicTones.keys():
                dicT[termino][profesor][tono] = 1
        else:

            for tono in dicTones.keys():
                if tono not in dicT[termino][profesor].keys():
                    dicT[termino][profesor][tono] = 1
                else:
                    dicT[termino][profesor][tono] = dicT[termino][profesor][tono] + 1


def rankingSemProf(dic_coments, dicTonesProf):

    # cojer a todos los quer tiene analitico o critico
    for profesor in dic_coments.keys():

        for codigoMat in dic_coments[profesor].keys():

            for anio in dic_coments[profesor][codigoMat].keys():

                for termino in dic_coments[profesor][codigoMat][anio].keys():

                    dic_comment = dic_coments[profesor][codigoMat][anio][termino]

                    for comenentario, dicTone in dic_comment.items():

                        llenarRankingSem(anio, termino, profesor, dicTone, dicTonesProf)


def obtenerNombreMat(codigoMat):
    archivo = open("CodigoMateriJSON.txt", "r", encoding="UTF-8")
    lineasArchivo = archivo.readline()
    archivo.close()

    dicci = dict(json.loads(lineasArchivo))
    materia = "NO EXISTE"
    for clave in dicci.keys():
        if codigoMat.find(clave) != -1:
            materia = dicci[clave]

    #if materia == "NO EXISTE":
        #print("No se encontro el codigo %s" %codigoMat)

    return materia

def llenarRankingMats(codigoMat, dicTone, dicTonesMat):

    materia = obtenerNombreMat(codigoMat)
    if materia not in dicTonesMat:
        dicTonesMat[materia] = {}
        for tono in dicTone.keys():
            dicTonesMat[materia][tono] = 1
    else:
        for tono in dicTone.keys():
            if tono not in dicTonesMat[materia].keys():
                dicTonesMat[materia][tono] = 1
            else:
                dicTonesMat[materia][tono] =  dicTonesMat[materia][tono] + 1



def rankingMats(dic_coments, dicTonesMat):

    # cojer a todos los quer tiene analitico o critico
    for profesor in dic_coments.keys():

        for codigoMat in dic_coments[profesor].keys():

            for anio in dic_coments[profesor][codigoMat].keys():

                for termino in dic_coments[profesor][codigoMat][anio].keys():

                    dic_comment = dic_coments[profesor][codigoMat][anio][termino]

                    for comenentario, dicTone in dic_comment.items():

                        llenarRankingMats(codigoMat, dicTone, dicTonesMat)


def obtenerNombreFact(codgio):

    nombre = ""
    for letra in codgio:
        letra = str(letra)
        if not letra.isdigit():
            nombre += letra
        else:
            break
    return nombre


def llenarRankingFact(codigo, profesor, dicTones, dicT):

    termino = obtenerNombreFact(codigo)
    if termino not in dicT:
        dicT[termino] = {profesor : {}}

        for tono in dicTones.keys():
            dicT[termino][profesor][tono] = 1
    else:
        if profesor not in dicT[termino].keys():

            dicT[termino][profesor] = {}
            for tono in dicTones.keys():
                dicT[termino][profesor][tono] = 1
        else:

            for tono in dicTones.keys():
                if tono not in dicT[termino][profesor].keys():
                    dicT[termino][profesor][tono] = 1
                else:
                    dicT[termino][profesor][tono] = dicT[termino][profesor][tono] + 1


def rankingFactProf(dic_coments, dicTonesProf):

    # cojer a todos los quer tiene analitico o critico
    for profesor in dic_coments.keys():

        for codigoMat in dic_coments[profesor].keys():

            for anio in dic_coments[profesor][codigoMat].keys():

                for termino in dic_coments[profesor][codigoMat][anio].keys():

                    dic_comment = dic_coments[profesor][codigoMat][anio][termino]

                    for comenentario, dicTone in dic_comment.items():

                        llenarRankingFact(codigoMat, profesor, dicTone, dicTonesProf)


def update(dictDest, dictSrc):
    for clave, valor in dictSrc.items():
        if isinstance(valor, collections.abc.Mapping):
            dictDest[clave] = update(dictDest.get(clave, {}), valor)
        else:
            dictDest[clave] = valor
    return dictDest


def funsionDicionarios(listaDics):

    result = {}
    for dicUpdate in listaDics:
        update(result, dicUpdate)
    return result
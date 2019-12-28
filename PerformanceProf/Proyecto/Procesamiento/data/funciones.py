import re
import json
import requests
import collections.abc
from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from ibm_watson import ToneAnalyzerV3
from nltk.tokenize import word_tokenize
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Credenciales API SentiDetector

def getKey(item):
    return item[0]

def evaluarSim(data, dic, model, similitud):

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

def tra(text):
    #"https://gateway.watsonplatform.net/language-translator/api/v3/identify?version=2018-05-01"

    authenticator = IAMAuthenticator('wmFyRWgaNLIIlZ6DHVkC41j6ZvUWdZrO3mWsBgggSgs5')

    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)

    language_translator.set_service_url('https://gateway.watsonplatform.net/language-translator/api/v3/identify?version=2018-05-01')

    translation = language_translator.translate(text=text, model_id='en-es',content_type='application/json').get_result()
    print(json.dumps(translation, indent=2))

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
import re
import json
import requests
from nltk.corpus import stopwords
from ibm_watson import ToneAnalyzerV3
from nltk.tokenize import word_tokenize
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Credenciales API SentiDetector
'''
curl -X POST -u "apikey:HGQfgUKC9Fqzjd1ByZlA2SUeovZaAz0G-veawWHILSLj" \
--header "Content-Type: application/json" \
--data-binary @{path_to_file}tone.json \
"https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21"

'''

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

    authenticator = IAMAuthenticator('KSq_GkAjahiOw2cp2jIQs_5E-sQXm5CxZ66_vC5yxOEo')

    tone_analyzer = ToneAnalyzerV3(version='2017-09-21',authenticator=authenticator)
    tone_analyzer.set_service_url("https://gateway.watsonplatform.net/tone-analyzer/api")
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
                            lista_comments.append(limpiarStopWords(comenentario)) #Extraer adjetivos

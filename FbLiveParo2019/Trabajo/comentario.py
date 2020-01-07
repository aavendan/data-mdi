import pickle
from datetime import datetime
from pickle import Pickler, Unpickler
import os.path
import json
import requests
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

ruta = "C:\\Users\\CORE I7\\Documents\\FbLiveParo2019\\"
sub = 'CLEAN_'
lista_archivos = ['397393044507256', '400986694185111', '419397588682810', '434584940509838',
                  '435667513820648', '439692923349814', '440949333193574', '449254902234199',
                  '470984136825431', '476340549762452', '494724017797129', '511908212961170',
                  '527422304726461', '723574001389336', '916830508688464', '923913571312203',
                  '1247776452097309', '1368421709973017', '1458939510911376',
                  '2111187462511299', '2129766937328183', '2287979277998232',
                  '2338233763157683', '2359787117607181']
extension = '.txt'
archivos_tag = ['Allison', 'gaby', 'Video19', 'Video19', 'Video20', 'Video21', 'Video22', 'Video23', 'Video24']


class Comentario:

    def __init__(self, name, time, comentary, feeling=[]):
        self.name = name
        self.comentary = comentary
        self.time = time
        self.feeling = []
        if len(feeling) > 0:
            for feel in feeling:
                feel = feel.split(" ", 1)
                if feel[0] != '':
                    self.feeling.append(Value(feel[1], feel[0]))

        self.polarity = ""
        self.subjetivity = ""
        self.confidence = ""
        self.agreement = ""
        self.irony = ""
        self.category = ""

    def to_String(self):
        trama = ""
        trama += self.name + "\n"
        trama += self.time + "\n"
        trama += self.comentary + "\n"
        if self.polarity != "":
            trama += str(self.polarity) + "\n"
        if self.subjetivity != "":
            trama += str(self.subjetivity) + "\n"
        if self.confidence != "":
            trama += str(self.confidence) + "\n"
        trama += str(self.irony) + "\n"
        trama += str(self.agreement) + "\n"
        trama += str(self.category) + "\n"
        trama += "Reacciones: " + "\n"
        for emotion in self.feeling:
            trama += emotion.to_String()
        trama += "=========================" + "\n"
        return trama


class Value:
    def __init__(self, emotion, number):
        self.emotion = emotion
        self.number = int(number)

    def to_String(self):
        trama = ""
        trama += self.emotion + " "
        trama += str(self.number) + "\n"
        return trama


class Extra:

    def __init__(self, category, tiempoini, tiempof):
        self.category = category
        self.tiempoinicio = getdateTime(tiempoini)
        self.tiempofin = getdateTime(tiempof)


def getCategoria(tiempo, textfile, d={}):
    categoria = ""
    temp = getdateTime(tiempo)
    if textfile in d:
        for i in d[textfile]:
            if isinstance(i, Extra):
                if temp >= i.tiempoinicio:
                    if temp < i.tiempofin:
                        categoria = i.category
                        break
        if categoria == "":
            list = d[textfile]
            temo = list[len(d[textfile]) - 1]
            if isinstance(temo, Extra):
                categoria = temo.category

    return categoria


def getdateTime(time):
    formato = ""
    m = len(time)
    if m >= 7:
        formato = '%H:%M:%S'
    else:
        formato = '%M:%S'
    tiempo = datetime.strptime(time, formato)
    return tiempo


url = "https://api.meaningcloud.com/sentiment-2.1"
key = "99e7e3ef98d2e865106547746bb2aa6d"
key2 = "4c2ca5c6eb7602c464663014a56e8916"
key3 = "c95d7b50fa314cebdf900d3bce0da0ff"
keys = [key, key2, key3]
control = [15972, 20000, 20000]
i = 0
texto = "a"
numero = {}
autor = {}


comments = []
apodos = {}
c = 0
reactions = []
medias = []
mediasPos = []
mediasNeg = []
varianzas = []
tags = {}
tagsR = {}
tagsRR = {}
usuarios = {}
q = 0

for a in archivos_tag:
    file = open(ruta + a + extension, "r", encoding="utf8")
    i = 0
    for linea in file.readlines():
        linea = linea.split("|")
        if linea[0] not in tags:
            list = []
            tags[linea[0]] = list
        if linea[1] not in tagsR:
            li = ["N+", "N", "NEU", "P", "P+"]
            for s in li:
                tagsRR[linea[1]+s] = 0
            tagsR[linea[1]] = i
            i += 1
        var = Extra(linea[1], linea[2], linea[3])
        tags[linea[0]].append(var)
    file.close()


for textfile in lista_archivos:
    number = {}
    results = {}
    trat = {"N+": 0, "N": 0, "P": 0, "P+": 0, "NEU": 0, "NONE": 0}
    print("**************************************************************")
    archivo = open(ruta + sub + textfile + extension, "r", encoding="utf8")
    arch = open(ruta + "ex" + sub + textfile + extension, "w", encoding="utf8")
    if os.path.exists(ruta + sub + textfile):
        dbfile = open(ruta + sub + textfile, 'rb')
        db = Unpickler(dbfile).load()
        comments.append(db)

        for comment in db:
            if isinstance(comment, Comentario):
                if comment.name not in usuarios:
                    usuarios[comment.name] = 1
                else:
                    usuarios[comment.name] += 1

                trat[comment.polarity] += 1
                comment.category = getCategoria(comment.time, textfile, tags)
                a = comment.category != ""
                b = comment.polarity != "NONE"
                if a & b:
                    tagsRR[comment.category + comment.polarity] += 1

                if len(comment.feeling) > 0:
                    for feel in comment.feeling:
                        if feel.emotion not in number:
                            number[feel.emotion] = feel.number
                            results[feel.emotion] = comment
                        else:
                            if feel.number > number[feel.emotion]:
                                number[feel.emotion] = feel.number
                                results[feel.emotion] = comment
        '''
        dbfile2 = open(ruta + sub + textfile, 'ab')
        Pickler(dbfile2).dump(db)
        dbfile2.close()
        '''

        message = ""

        sum = 0
        sumPos = 0
        sumNeg = 0
        negM = trat["N+"]
        sum += negM
        sumNeg += negM
        negM *= -1
        neg = trat["N"]
        sum += neg
        sumNeg += neg
        neg *= -0.5
        neu = trat["NONE"]
        sum += neu
        neu *= 0
        pos = trat["P"]
        sum += pos
        sumPos += pos
        pos *= 0.5
        posM = trat["P+"]
        sum += posM
        sumPos += posM
        posM *= 1

        media = negM + neg + pos + posM
        media /= sum
        medias.append(media)

        mediaPos = pos + posM
        mediaPos /= sumPos
        mediasPos.append(mediaPos)

        mediaNeg = negM + neg
        mediaNeg /= sumNeg
        mediasNeg.append(mediaNeg)

        message += "Media: " + str(media) + "\n"

        varianza = (trat["N+"]*((-1-media)**2)) + (trat["N"]*((-0.5-media)**2)) + (trat["NEU"]*((-media)**2)) + (trat["P"] * ((0.5 - media) ** 2))+ (trat["P+"]*((1-media)**2))
        varianza /= (sum-1)
        varianzas.append(varianza)

        message += "Varianza: " + str(varianza) + "\n\n"

        for polarity in trat:
            message += polarity + ": " + str(trat[polarity]) + "\n"

        message += "\n"

        for emotion in number:
            message += emotion + "\n"
            message += results[emotion].to_String()
            if emotion not in numero:
                numero[emotion] = number[emotion]
                autor[emotion] = results[emotion]
            else:
                if number[emotion] > numero[emotion]:
                    numero[emotion] = number[emotion]
                    autor[emotion] = results[emotion]

        arch.write(message)
    else:
        comentarios = []
        file4 = open(ruta + "2" + sub + textfile + extension,  "w", encoding="utf8")
        for linea in archivo.readlines():
            cont = 0;
            word = ""
            linea = linea.split("|")
            if linea[0] not in apodos:
                word = "Anonymous"+str(c)
                apodos[linea[0]] = word
                c+=1
            else:
                word = apodos[linea[0]]

            lista = []
            for part in linea:
                if cont >= 3:
                    lista.append(part)
                    feel = part.split(" ", 1)
                    if feel[1] not in reactions:
                        reactions.append(feel[1])
                cont += 1
            comentario = Comentario(word, linea[1], linea[2], lista)
            payload = "key=" + keys[i] + "&lang=es&txt=" + comentario.comentary + "&txtf=plain&encoding=utf8"
            headers = {'content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

            response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
            test = json.loads(response.text)
            print(test)
            comentario.polarity = test.get('score_tag')
            comentario.confidence = test.get('confidence')
            comentario.subjetivity = test.get('subjectivity')
            comentario.agreement = test.get('agreement')
            comentario.irony = test.get('irony')
            trama = comentario.to_String()
            file4.write(trama)
            comentarios.append(comentario)
            control[i] -= 1
            if control[i] == 0:
                i += 1

        file4.close()
        dbfile = open(ruta + sub + textfile, 'ab')
        Pickler(dbfile).dump(comentarios)
        dbfile.close()
        comments.append(comentarios)

arch2 = open(ruta + "exa" + sub + extension, "w", encoding="utf8")
mess = ""
users = sorted(usuarios.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
i = 0
for p in users:
    if i < 10:
        mess += "Usuario " + str(p) + "\n"
        i += 1
    else:
        break

for emotion in number:
        mess += emotion + "\n"
        mess += autor[emotion].to_String()

arch2.write(mess)
#'''
label = ['N+', 'N', 'NEU', 'P', 'P+']
lista1 = [[], [], [], [], [], []]
tagX = []
k = 0
for j in tagsR:
    tagX.append(j)
    for z in label:
        lista1[k].append(tagsRR[j+z])
    k += 1

print(len(tagX))
print(len(lista1[0]))
width = 0.15
fig, ax = plt.subplots()
x = np.arange(len(label))


rect1 = ax.bar(x - 4*(width/2), lista1[0], width, label=tagX[0])
rect2 = ax.bar(x - 2*(width/2), lista1[1], width, label=tagX[1])
rect3 = ax.bar(x - 1*(width/2), lista1[2], width, label=tagX[2])
rect4 = ax.bar(x + 1*(width/2), lista1[3], width, label=tagX[3])
rect5 = ax.bar(x + 2*(width/2), lista1[4], width, label=tagX[4])
rect6 = ax.bar(x + 4*(width/2), lista1[5], width, label=tagX[5])

ax.set_ylabel('Cantidad de comentarios')
ax.set_xlabel('Polaridad')
ax.set_title('Cantidad de comentarios de categorias segun su polaridad')
ax.set_xticks(x)
ax.set_xticklabels(label)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 5, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rect1)
autolabel(rect2)
autolabel(rect3)
autolabel(rect4)
autolabel(rect5)
autolabel(rect6)

fig.tight_layout()

plt.show()
#'''





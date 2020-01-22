import pickle
from matplotlib.ticker import MaxNLocator
from datetime import datetime
from pickle import Pickler, Unpickler
import os.path
import json
import requests
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import indicoio
import xlwt
from xlwt import Workbook
import xlsxwriter

indicoio.config.api_key = '6207934408bdd7511b0fd343580587f3';

ruta = "C:\\Users\\CORE I7\\Documents\\FbLiveParo2019\\"
sub = 'CLEAN_'
lista_archivos = ['397393044507256', '400986694185111', '419397588682810', '434584940509838',
                  '435667513820648', '439692923349814', '440949333193574', '449254902234199',
                  '470984136825431', '476340549762452', '494724017797129', '511908212961170',
                  '527422304726461', '723574001389336', '916830508688464', '923913571312203',
                  '1247776452097309', '1368421709973017', '1458939510911376',
                  '2111187462511299', '2129766937328183', '2287979277998232',
                  '2338233763157683', '2359787117607181']

lista_archivos2 = ['923913571312203', '1247776452097309', '1368421709973017', '1458939510911376','2111187462511299',
                   '2129766937328183', '2287979277998232', '2338233763157683', '2359787117607181']
extension = '.txt'
archivos_tag = ['Allison', 'gaby', 'Video19', 'Video19', 'Video20', 'Video21', 'Video22', 'Video23', 'Video24', 'videosMA']


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

    def to_String2(self):
        trama = ""
        trama += self.name + "|"
        trama += self.time + "|"
        tra = self.comentary.rstrip("\n")
        trama += tra + "|"
        trama += str(self.category) + "|"
        trama += str(self.polarity) + "|"
        trama += str(self.subjetivity) + "|"
        trama += str(self.confidence) + "|"
        trama += str(self.irony) + "|"
        trama += str(self.agreement) + "\n"
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

    def __init__(self, category, tiempoini, tiempof, pos):
        self.category = category
        self.tiempoinicio = getdateTime(tiempoini)
        self.tiempofin = getdateTime(tiempof)
        self.pos = pos


class Extra2:

    def __init__(self, tiempoini, tiempof, pos):
        self.tiempoinicio = getdateTime(tiempoini)
        self.tiempofin = getdateTime(tiempof)
        self.pos = pos


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


def getPos(tiempo, textfile, d={}):
    pos = -1
    categoria = ""
    temp = getdateTime(tiempo)
    if textfile in d:
        for i in d[textfile]:
            if isinstance(i, Extra):
                if temp >= i.tiempoinicio:
                    if temp < i.tiempofin:
                        categoria = i.category
                        pos = i.pos
                        break
        if categoria == "":
            list = d[textfile]
            temo = list[len(d[textfile]) - 1]
            if isinstance(temo, Extra):
                pos = temo.pos

    return pos


def getPos2(tiempo, lista34=[]):
    pos = -1
    temp = getdateTime(tiempo)
    for element in lista34:
        if isinstance(element, Extra2):
            if temp >= element.tiempoinicio:
                if temp < element.tiempofin:
                    pos = element.pos
    return pos


def getdateTime(time):
    formato = ""
    m = len(time)
    if m >= 7:
        formato = '%H:%M:%S'
    else:
        formato = '%M:%S'
    tiempo = datetime.strptime(time, formato)
    return tiempo


def getS(result):
    temporal1 = float(result)
    if (temporal1 >= 0.495) & (temporal1 < 0.505):
        return "NEU";
    if (temporal1 >= 0.505) & (temporal1 < 0.75):
        return "P";
    if temporal1 >= 0.75:
        return "P+";
    if (temporal1 >= 0.25) & (temporal1 < 0.495):
        return "N";
    if temporal1 < 0.25:
        return "N+";


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
numero2 = {}
autor2 = {}

video = '400986694185111'
tiempos = ['0:00', '20:00', '40:00', '1:00:00', '1:20:00', '1:40:00', '2:00:00', "2:20:00", "2:40:00"]
tiempos2 = []
dicc = {}
comments = []
apodos = {}
c = 0
reactions = []
medias = []
mediasPos = []
mediasNeg = []
varianzas = []
extra = []
pos = {}
tags = {}
tagsR = {}
tagsRR = {}
usuarios = {}
top10 = ['Anonymous893', 'Anonymous777', 'Anonymous811', 'Anonymous861', 'Anonymous1828', 'Anonymous2243',
         'Anonymous786', 'Anonymous54', 'Anonymous2931', 'Anonymous221']
tagU = {}
top = {}
q = 0

for i in range(len(tiempos) - 1):
    intervalo = Extra2(tiempos[i], tiempos[i+1], i)
    tiempos2.append(intervalo)
    li2 = ["N+", "N", "NEU", "P", "P+"]
    for j in li2:
        sr = j + str(i)
        dicc[sr] = 0

for a in archivos_tag:
    file = open(ruta + a + extension, "r", encoding="utf8")
    i = 0
    for linea in file.readlines():
        linea = linea.split("|")
        if linea[0] not in tags:
            list = []
            tags[linea[0]] = list
            pos[linea[0]] = 0
        if linea[1] not in tagsR:
            li = ["N+", "N", "NEU", "P", "P+"]
            for s in li:
                tagsRR[linea[1]+s] = 0
            tagsR[linea[1]] = i
            i += 1
        var = Extra(linea[1], linea[2], linea[3], pos[linea[0]])
        if linea[0] == video:
            extra.append(var)
        pos[linea[0]] += 1
        tags[linea[0]].append(var)
    file.close()

users = ""
work = []
workP = {}
workN = {}
workNEU = {}
sumadorW = {}
sumadorW2 = {}
#wb = xlsxwriter.Workbook('Usuarios1.xlsx')
contador = 0;
#sheet1 = wb.add_worksheet('Sheet 1')
#sheet1.write(contador, 0, 'Id video')
#sheet1.write(contador, 1, 'Id User')
#sheet1.write(contador, 2, 'Category')
#sheet1.write(contador, 3, 'Time')
#sheet1.write(contador, 4, 'Polarity')
#sheet1.write(contador, 5, 'Subjetivity')
#sheet1.write(contador, 6, 'Confidence')
#sheet1.write(contador, 7, 'Agreement')
#sheet1.write(contador, 8, 'Irony')

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
                q += 1
                contador += 1
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
                    if comment.name in top10:
                        a = comment.name + comment.category + comment.polarity
                        o = comment.name + comment.category
                        if a not in top:
                            top[a] = 1
                            if o not in tagU:
                                tagU[o] = comment.category
                        else:
                            top[a] += 1
                #users += comment.to_String()
                #sheet1.write(contador, 0, textfile)
                #sheet1.write(contador, 1, str(comment.name))
                #sheet1.write(contador, 2, str(comment.category))
                #sheet1.write(contador, 3, str(comment.time))
                #sheet1.write(contador, 4, str(comment.polarity))
                #sheet1.write(contador, 5, str(comment.subjetivity))
                #sheet1.write(contador, 6, str(comment.confidence))
                #sheet1.write(contador, 7, str(comment.agreement))
                #sheet1.write(contador, 8, str(comment.irony))

                users += textfile + "|" + comment.to_String2()
                if textfile == video:
                    t1 = getPos(comment.time, video, tags)
                    t2 = comment.category + str(t1)
                    t3 = getPos2(comment.time,tiempos2)
                    if comment.polarity != "NONE":
                        sr1 = comment.polarity + str(t3)
                        dicc[sr1] += 1
                    if t2 not in work:
                        work.append(t2)
                        workN[t2] = 0
                        workP[t2] = 0
                        workNEU[t2] = 0
                        sumadorW[t2] = 0
                        sumadorW2[t2] = 1
                    else:
                        sumadorW2[t2] += 1
                    n1 = comment.polarity == "N+"
                    n2 = comment.polarity == "N"
                    neu = comment.polarity == "NEU"
                    p1 = comment.polarity == "P"
                    p2 = comment.polarity == "P+"
                    a = 0
                    if n1 | n2:
                        workN[t2] += 1
                        if n1:
                            sumadorW[t2] += -1
                        else:
                            sumadorW[t2] += -0.5

                    if p1 | p2:
                        workP[t2] += 1
                        if p1:
                            sumadorW[t2] += 1
                        else:
                            sumadorW[t2] += 0.5

                    if neu:
                        workNEU[t2] += 1

                if len(comment.feeling) > 0:
                    for feel in comment.feeling:
                        emo = feel.emotion.rstrip()
                        if emo not in number:
                            number[emo] = feel.number
                            results[emo] = comment
                        else:
                            if feel.number > number[emo]:
                                number[emo] = feel.number
                                results[emo] = comment
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
            message += emotion + " " + str(number[emotion]) + "\n"
            message += results[emotion].to_String2()
            if emotion not in numero:
                numero[emotion] = number[emotion]
                autor[emotion] = results[emotion]
            else:
                if number[emotion] > numero[emotion]:
                    numero[emotion] = number[emotion]
                    autor[emotion] = results[emotion]
            if emotion not in numero2:
                list = []
                numero2[emotion] = list
            else:
                numero2[emotion].append((results[emotion], number[emotion]))

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
            if comentario.polarity == "NONE":
                tempo2 = indicoio.sentiment(comentario.comentary)
                comentario.polarity = getS(tempo2)
            comentario.confidence = test.get('confidence')
            comentario.subjetivity = test.get('subjectivity')
            comentario.agreement = test.get('agreement')
            comentario.irony = test.get('irony')
            comentario.category = getCategoria(comentario.time, textfile, tags)
            trama = comentario.to_String2()
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

arch3 = open(ruta + "usuarios" + extension, "w", encoding="utf8")
arch3.write(users)
arch3.close()
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

for emotion in numero:
        mess += emotion + " " + str(numero[emotion])+"\n"
        mess += autor[emotion].to_String2()

arch2.write(mess)
#wb.close()
#'''

#'''
fig, ax = plt.subplots()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def autolabel2(rects,i):
    cont1 = 0
    for rect in rects:
        print(str(cont1))
        height = rect.get_height()
        ax.annotate(up[i][cont1]+"\n"+'{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=7, rotation=0)
        cont1+=1

'''
'''
print(tagU)
print(top)
t = 2
label = ['N+', 'N', 'NEU', 'P', 'P+']
lista1 = []
up = {}
tagX = []
'''

for j in tagsR:
    listado = []
    o = top10[t] + j
    '''
'''
    tagX.append(j)
    for z in label:
        o = j + z
       listado.append(tagsRR[o])
    '''
'''
    
    '''
'''
    #if o in tagU:
       # tagX.append(tagU[o])
        #for z in label:
            #f = 0
            #check = o + z
            #if check in top:
               # f = top[check]
            #listado.append(f)
    '''
'''
'''
'''
    if len(listado) > 0:
        lista1.append(listado)
    '''
'''
label3 = []
cuenta = 0
#for emotion in numero2:
for i in range(3):
    listado1 = []
    for emotion in numero2:
        if cuenta not in up:
            temporal5 = []
            up[cuenta] = temporal5
        numero2[emotion].sort(key=lambda tup: tup[1], reverse=True)
        if emotion not in tagX:
            tagX.append(emotion)
            label3.append(emotion)
        listado1.append(numero2[emotion][i][1])
        sa = numero2[emotion][i][0].name.split("Anonymous", 1)[1]
        sa1 = 'A' + sa
        up[cuenta].append(sa1)
    cuenta += 1
    lista1.append(listado1)


print(len(tagX))
print(len(lista1))
print((tagX))
print((lista1))
width = 0.25
# fig, ax = plt.subplots()
x = np.arange(len(label3))

factor = []
zero = len(lista1)%2
g = 0
if zero == 1:
    g = len(lista1) - 1
else:
    g = len(lista1)

g /= 2
fac = 0
for rf in range(len(lista1)):
    factor.append(fac)
    fac += 1


rects = []
fasda = 0
for rf in range(len(lista1)):
    print(str(fasda))
    rect = ax.bar(x + (factor[rf] * width), lista1[rf], width)
    autolabel2(rect, rf)
    fasda += 1


ax.set_ylabel('Cantidad de reacciones', fontsize=10)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel('Emoción', fontsize=10)
ax.set_title('Diagrama de los 3 comentarios que más reacciones han generado según su tipo de emoción', fontsize=10)
ax.set_xticks(x + 1*width)
ax.set_xticklabels(label3)
#ax.legend()
#fig.tight_layout()


plt.show()
#'''
'''
'''
'''
rect1 = ax.bar(x - 2 * (width / 2), lista1[0], width, label=tagX[0])
rect2 = ax.bar(x - 1 * (width / 2), lista1[1], width, label=tagX[1])
rect3 = ax.bar(x + 1 * (width / 2), lista1[2], width, label=tagX[2])
rect4 = ax.bar(x + 2 * (width / 2), lista1[3], width, label=tagX[3])
#rect5 = ax.bar(x + 2 * (width / 2), lista1[4], width, label=tagX[4])
#rect6 = ax.bar(x + 4 * (width / 2), lista1[5], width, label=tagX[5])

autolabel(rect1)
autolabel(rect2)
autolabel(rect3)
autolabel(rect4)
#autolabel(rect5)
#autolabel(rect6)
'''

'''
'''
tabla = "**************************************************************\n" + video + "\n\n"
tabla += "Hora Inicio|Hora Fin|Categoria|PolaridadPositiva|PolaridadNegativa|PolaridadNeutra\n"
neg = 0
pos = 0
neu = 0
time = ['0:00:00']
time2 = []
listaN = [0]
listaP = [0]
listaNEU = [0]
mediasW = [0]
m = 0
for k in work:
    neg += workN[k]
    pos += workP[k]
    neu += workNEU[k]

    med = sumadorW[k]/sumadorW2[k]
    mediasW.append(med)

    t4 = neg
    listaN.append(t4)
    t5 = pos
    listaP.append(t5)
    t6 = neu
    listaNEU.append(t6)

    tie = str(extra[m].tiempofin.hour) + ":" + str(extra[m].tiempofin.minute) + ":" + \
             str(extra[m].tiempofin.second)
    time.append(tie)

    tabla += str(extra[m].tiempoinicio.hour) + ":" + str(extra[m].tiempoinicio.minute) + ":" + \
             str(extra[m].tiempoinicio.second) + "|" + str(extra[m].tiempofin.hour) + ":" + str(extra[m].tiempofin.minute) + ":" + \
             str(extra[m].tiempofin.second) + "|" + extra[m].category + "|" + str(pos) + "|" + str(neg) + "|" + \
             str(neu) + "\n"

    time2.append(extra[m].category[0])

    m += 1


sol = open(ruta + "table" + extension, "w", encoding="utf8")
sol.write(tabla)
sol.close()

sr3 = "**************************************************************\n" + video + "\n\n"
sr3 += "Hora Inicio|Hora Fin|Categoria|PolaridadN+|PolaridadN|PolaridadNEU|PolaridadP|PolaridadP+\n"
li2 = ["N+", "N", "NEU", "P", "P+"]
for i in range(len(tiempos2)):
    interval = tiempos2[i]
    if isinstance(interval,Extra2):
        sr3 += str(interval.tiempoinicio.hour) + ":" + str(interval.tiempoinicio.minute) + ":" + \
               str(interval.tiempoinicio.second) + "|" + str(interval.tiempofin.hour) + ":" + str(interval.tiempofin.minute) + \
               ":" + str(interval.tiempofin.second) + "|"
        for j in li2:
            sr = j + str(i)
            sr3 += str(dicc[sr]) + "|"
        sr3 += "\n"

sol2 = open(ruta + "nuevo" + extension, "w", encoding="utf8")
sol2.write(sr3)
sol2.close()

x = np.arange(len(time))
x2 = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
fig, ay = plt.subplots()

ay.plot(x, mediasW)
#ay.plot(x, listaP, label='Polaridad Positiva')
#ay.plot(x, listaNEU, label='Polaridad Neutra')
ay.yaxis.set_major_locator(MaxNLocator(integer=True))
ay.set_xlabel("Línea de Tiempo", fontsize=10)
ay.set_ylabel("Polaridad", fontsize=10)
ay.set_title('Diagrama de polaridad según el tiempo de video que aparecen en '
             'el vídeo de Teleamazonas del 9 de octubre del 2019', fontsize=10)
ay.set_xticks(x)
ay.set_xticklabels(time)
secax = ay.twiny()
secax.set_xticks(x2)
secax.set_xticklabels(time2)
secax.set_xlabel("Categoría de sección del tiempo", fontsize=10)

textstr = '\n'.join((
    r'R: Reportajes',
    r'M: Manifestaciones',
    r'C: Comunicados Oficiales'))

props = dict(boxstyle='round', facecolor='white', alpha=0.5)

# place a text box in upper left in axes coords
plt.text(0.05, 0.977, textstr, transform=ay.transAxes, fontsize=10, verticalalignment='top', bbox=props)

#ay.legend()
plt.show()


#'''





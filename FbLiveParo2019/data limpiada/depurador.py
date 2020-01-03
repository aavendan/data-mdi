# coding=utf-8
import fnmatch
import re
ruta="C:\\Users\\allis\\git\\data-mdi\\FbLiveParo2019\data limpiada\\"
lista_archivos=['1247776452097309.txt','2359787117607181.txt','2338233763157683.txt','2287979277998232.txt','2129766937328183.txt','2111187462511299.txt','1458939510911376.txt','1368421709973017.txt','434584940509838.txt','419397588682810.txt','400986694185111.txt','397393044507256.txt']
for textfile in lista_archivos:
    print("**************************************************************")
    archivo=open(ruta+textfile,"r",encoding="utf8")
    lista=[]
    cadena=""
    temp=[]
    #crea una lista anidada
    cont=0
    for linea in archivo.readlines():
        linea=linea.split("=========================")
        linea=linea[0].rstrip("\n")
        if(linea!=""):
            temp.append(linea)
        else:
            cont=cont+1
            lista.append(temp)
            temp=[]
    print("Hay "+ str(cont)+" comentarios en "+textfile)
    p=0
    r=0
    archivo=open(ruta+"D"+textfile,"w",encoding="utf8")
    nuevalista = []
    for i in lista:
        if (i[2]).find("Ver más") != -1:
            lista.pop(lista.index(i))
            p=p+1
        else:
            nuevalista.append(i)
            trama = str(i) + "\n"
            archivo.write(trama)
            r=r+1

    print("Se eliminó "+str(p)+" comentarios incompletos y se los guardó en D"+textfile)
    otrotemp=[]
    listaN=[]
    o=0
    acum=0
    for j in nuevalista:
        if(j not in otrotemp):
            o=o+1
            otrotemp.append(j)
        else:
            acum=acum+1
    print("Hay "+str(acum)+" comentarios repetidos en D"+textfile)
    print("Hay "+str(o)+" comentarios sin repetir")

    t=0
    dataLimpia=open(ruta+"CLEAN"+textfile,"w",encoding="utf8")
    for w in otrotemp:
        if(len(w)==3):
            trama=w[0]+"|"+w[1]+"|"+w[2]+"\n"
        elif(len(w)==4):
            trama = w[0] + "|" + w[1] + "|" + w[2] + "|" + w[3] + "\n"
        elif(len(w)==5):
            trama = w[0] + "|" + w[1] + "|" + w[2] + "|" + w[3] + "|" + w[4] + "\n"
        elif(len(w)==6):
            trama = w[0] + "|" + w[1] + "|" + w[2] + "|" + w[3] + "|" + w[4] + "|" + w[5] + "\n"
        elif(len(w)==7):
            trama = w[0] + "|" + w[1] + "|" + w[2] + "|" + w[3] + "|" + w[4] + "|" + w[5] + "|" + w[6] + "\n"
        elif(len(w)==8):
            trama = w[0] + "|" + w[1] + "|" + w[2] + "|" + w[3] + "|" + w[4] + "|" + w[5] + "|" + w[6] + "|" + w[7] + "\n"
        t=t+1
        dataLimpia.write(trama)
    print("Hay "+ str(t)+" comentarios guardados en CLEAN"+textfile)
    dataLimpia.close()

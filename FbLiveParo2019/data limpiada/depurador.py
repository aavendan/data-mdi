# coding=utf-8
import fnmatch
import re
dir="C:\\Users\\allis\\git\\data-mdi\\FbLiveParo2019\\"
ruta_delete="C:\\Users\\allis\\git\\data-mdi\\FbLiveParo2019\\data limpiada\\comentarios_borrados\\"
ruta="C:\\Users\\allis\\git\\data-mdi\\FbLiveParo2019\\data limpiada\\"
ruta2="C:\\Users\\allis\\git\\data-mdi\\FbLiveParo2019\\data limpiada\\CLEAN"
lista_archivos=['1247776452097309.txt','2359787117607181.txt','2338233763157683.txt',
                '2287979277998232.txt','2129766937328183.txt','2111187462511299.txt',
                '1458939510911376.txt','1368421709973017.txt','434584940509838.txt',
                '419397588682810.txt','400986694185111.txt','397393044507256.txt',
                '923913571312203.txt','916830508688464.txt','723574001389336.txt',
                '527422304726461.txt','511908212961170.txt','494724017797129.txt',
                '476340549762452.txt','470984136825431.txt','449254902234199.txt',
                '440949333193574.txt','439692923349814.txt','435667513820648.txt']
for textfile in lista_archivos:
    print("**************************************************************")
    archivo=open(dir+textfile,"r",encoding="utf8")
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
    archivo=open(ruta_delete+"D"+textfile,"w",encoding="utf8")
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
        dataLimpia.write(trama.upper())
    print("Hay "+ str(t)+" comentarios guardados en CLEAN"+textfile)
    dataLimpia.close()

for f in lista_archivos:
    total=i = 0
    h1 = h2 = h3 = h4 = h5 = h6 = h7 = h8 = h9 = h10 = h11=h12=h13=h14=h15=h16=h17=h18=h19=h20=h21=h22=h23=h24=h25=0
    h26=h27=h28=h29=h30=h31=h32=h33=h34=h35=h36=h37=h38=h39=h40=h41=h42=h43=h44=h45=h46=h47=h48=0
    archivo = open(ruta2 + f, "r", encoding="utf8")
    narchivo = open(ruta2+"_" + f, "w", encoding="utf8")
    for linea in archivo.readlines():
        cadena=linea.split("|")
        if(cadena[2].upper().find("#PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA")!=-1):
            h1=h1+1
        #    print(cadena[2])
        elif(cadena[2].upper().find("#PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA")!=-1):
            h2 = h2 + 1
        #    print(cadena[2])
        elif (cadena[2].upper().find("PRENSAVENDIDAPRENSAVENDIDAPRENSAVENDIDA")!=-1):
             h3=h3+1
             print(cadena[2])
        elif(cadena[2].upper().find("#PRENSACORRUPTA!!#PRENSACORRUPTA!!#PRENSACORRUPTA!!#PRENSACORRUPTA!!#PRENSACORRUPTA!!")!=-1):
            h4 = h4 + 1

        elif (cadena[2].upper().find("ESTÁN INVOLUCRADOS LAS FARC, LATIN KINGS, CUMBIA KINGS, DON GATO Y SU PANDILLA") != -1):
            h5 = h5 + 1

        elif (cadena[2].upper().find("#PRENSACORRUPTA#PRENSACORRUPTA#PRENSACORRUPTA#PRENSACORRUPTA#PRENSACORRUPTA")!=-1 or cadena[2]==("#PRENSACORRUPTA#PRENSACORRUCTAPRENSACORRUPTA#PRENSACORRUCTAPRENSACORRUPTA#PRENSACORRUCTAPRENSACORRUPTA#PRENSACORRUCTAPRENSACORRUPTA#PRENSACORRUCTAPRENSACORRUPTA#PRENSACORRUCTA\n")):
            h6 = h6 + 1
        #    print(cadena[2])
        elif(cadena[2].upper().find("#PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA #PRENSAVENDIDAYNEFASTA ")!=-1):
            h7=h7+1

        elif(cadena[2].upper().find("HTTP")!=-1 or cadena[2].find("://FACEBOOK.COM/.../UZPFSTEWNZGYMDI2NJU1MZAXMTE6VKS6NDE0.../")!=-1):
            h8=h8+1
         #   print(cadena[2])

        elif(cadena[2].upper().find("#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA ")!=-1):
            h9=h9+1
        #    print(cadena[2])
        elif(cadena[2].find("#PRENSAVENDIDA# PRENSAVENDIDA#PRENSAVENDIDA")!=-1):
            h10=h10+1
        #    print(cadena[2])
        elif(cadena[2].find("#PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA ")!=-1):
            h11=h11+1

        elif(cadena[2].find(" MIS APRECIADOS MEDIOS DE COMUNICACIÓN ")!=-1 or cadena[2].find(" MIS APRECIADOS  MEDIOS DE COMUNICACIÓN DEL ECUADOR")!=-1 or cadena[2].find("🐀🐀 APRECIADA #PRENSAVENDIDA/︶\.")!=-1 or cadena[2].find("APRECIADOS MEDIOS DE COMUNICACIÓN /︶\#PRENSAVENDIDA#PRENSAVENDIDA#PRENSAVENDIDA")!=-1):
            h12=h12+1
         #   print(cadena[2])
        elif(cadena[2].find(" MI APRECIADO PRESIDENTE ")!=-1):
            h13=h13+1
            #print(cadena[2])
        elif(cadena[2].find("#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA")!=-1):
            h14=h14+1
            #print(cadena[2])
        elif(cadena[2].find("#PRENSAVENDIDA#PRENSAVENDIDA#PRENSAVENDIDA#PRENSAVENDIDA#PRENSAVENDIDA")!=-1 or cadena[2]==("#PRENSA VENDIDA#PRENSA VENDIDA#PRENSA VENDIDA#PRENSA VENDIDA#PRENSA VENDIDA\n") or cadena[2]==("PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA\n")):
            h15=h15+1
        #    print(cadena[2])
        elif(cadena[2].find("#PRENSAVENDIGA #PRENSAVENDIGA #PRENSAVENDIGA #PRENSAVENDIGA #PRENSAVENDIGA")!=-1 or cadena[2].find("#PRENDAVENDIDA#PRENDAVENDIDA#PRENDAVENDIDA#PRENDAVENDIDA#PRENDAVENDIDA")!=-1 ):
            h16=h16+1
        elif(cadena[2].find("# PRENSAVENDIDA # PRENSAVENDIDA # PRENSAVENDIDA # PRENSAVENDIDA # PRENSAVENDIDA")!=-1):
        #    print(cadena[2])
            h17=h17+1
        elif(cadena[2].find("#PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA #PRENSABASURA ")!=-1):
            h18=h18+1
        elif(cadena[2].find("#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA#PRENSAVENDIDA #PRENSABASURA")!=-1):
            h19=h19+1
        #    print(cadena[2])
        elif(cadena[2].find("#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE #PRENSAVENDIDA #NADIELESCREE #PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE#PRENSAVENDIDA #NADIELESCREE #PRENSAVENDIDA #NADIELESCREE")!=-1):
            h20=h20+1
         #   print(cadena[2])
        elif(cadena[2].find("#PRENSAHPTA  #PRENSAHPTA  #PRENSAHPTA  #PRENSAHPTA #PRENSAHPTA  ")!=-1):
            h21=h21+1
        elif (cadena[2].find("#LENINTUNOERESMIPRESIDENTE #LENINTUNOERESMIPRESIDENTE#LENINTUNOERESMIPRESIDENTE#LENINTUNOERESMIPRESIDENTE") != -1):
            h22 = h22 + 1
         #   print
        elif(cadena[2]==("#PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSACORRUPTA#PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSACORRUPTA\n")
        or cadena[2].find("#PRENSAVENDIDA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA") != -1):
            h23=h23+1
         #   print(cadena[2])
        elif(cadena[2].find("#PRENSACORRUPTA #PRENSACORRUPTA  #PRENSACORRUPTA #PRENSACORRUPTA  #PRENSACORRUPT #PRENSACORRUPTA  #PRENSACORRUPTA #PRENSACORRUPTA  #PRENSACORRUPTA #PRENSACORRUPTA  ")!=-1):
            h24=h24+1
            '''elif (cadena[2]==("#PRENSAVENDIDA\n") or cadena[2]==("PRENSAVENDIDA\n") or cadena[2]==("PRENSA VENDIDA\n")
              or cadena[2]==("PRENSA  VENDIDAPRENSA  VENDIDA PRENSA  VENDIDA PRENSA VENDIDAPRENSA VENDIDA\n")
              or cadena[2]==("PRENSA VENDIDA  PRENSA VENDIDA PRENSA VENDIDA\n") or cadena[2]==("#PRENSAVENDIDA 😠😠🤬🤬🤬🤬🖕🖕🖕🖕🖕\n")
                or cadena[2]==("PRENSA VENDIDA") or cadena[2]==("PRENSA VENDIDA!\n") or cadena[2]==("¡PRENSA VENDIDA!")
              or cadena[2]==("¡PRENSA VENDIDA!\n") or cadena[2]==("#PRESAVENDIDA\n") or cadena[2]==("#PRENSAVENDIDA")
              or cadena[2]==("PRENSA VENDIDA  PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDAPRENSA VENDIDA\n")
                or cadena[2]==("#PRENSA#VENDIDA\n")):'''
        elif(cadena[2].find("RENUNCIA MORENO# RENUNCIA MORE # RENUNCIA MORENO # RENUNCIA MORENO# RENUNCIA MORE # RENUNCIA MORENO# RENUNCIA MORENO# RENUNCIA MORE # RENUNCIA MORENO# RENUNCIA MORENO# RENUNCIA MORE # RENUNCIA MORENO# RENUNCIA MORENO# RENUNCIA MORE # RENUNCIA MORENO# RENUNCIA MORENO# RENUNCIA MORE # RENUNCIA MORENO")!=-1 or
        cadena[2].find("#RENUNCIAMORENO #RENUNCIAMORENO #RENUNCIAMORENO #RENUNCIAMORENO #RENUNCIAMORENO") != -1):
        #    print(cadena[2])
            h25 = h25 + 1
        elif(cadena[2]==("#PRENSACORRUPTA\n")):
            h26=h26+1
        elif(cadena[2].find("#LENINEBOTLAMISMACOSASON #LENINEBOTLAMISMACOSASON #LENINEBOTLAMISMACOSASON")!=-1):
            h27=h27+1
        elif(cadena[2].find("#PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA #PRENSACORRUPTA#PRENSACORRUPTA #PRENSACORRUPTA #PRENSAVENDIDA #PRENSACORRUPTA #PRENSAVENDIDA#PRENSAVENDIDA#PRENSACORRUPTA")!=-1):
            h28=h28+1
        elif (cadena[2].find("#NOSVALEVERGATELEAMAZONAS #NOSVALEVERGATELEAMAZONAS #NOSVALEVERGATELEAMAZONAS #NOSVALEVERGATELEAMAZONAS #NOSVALEVERGATELEAMAZONAS #NOSVALEVERGATELEAMAZONAS #NOSVALEVERGATELEAMAZONAS")!=-1):
            h29 = h29 + 1
            #print(cadena[2])
        elif(cadena[2].find("#FUERALENIN #FUERALENIN #FUERALENIN #FUERALENIN #FUERALENIN")!=-1):
            h30=h30+1
           # print(cadena[2])
        elif(cadena[2]==("#DIALOGOANTESDELASMUERTESNODESPUES #DIALOGOANTESDELASMUERTESNODESPUES #DIALOGOANTESDELASMUERTESNODESPUES #DIALOGOANTESDELASMUERTESNODESPUES #DIALOGOANTESDELASMUERTESNODESPUES\n")):
            h31=h31+1
        #    print(cadena[2])
        elif (cadena[2].find("MI APRECIADA INSIGNIA") != -1):
            h32 = h32 + 1
        elif(cadena[2].find("MI APRECIADA PRENSA") != -1):
            h33 = h33 + 1
        elif(cadena[2]==("😡😡😡😡😡😡\n") or cadena[2]==("😡😡😡😡\n") or
             cadena[2]==("👎👎👎👎👎👎👎👎👎👎\n") or cadena[2]==("🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬\n") or
            cadena[2]==("🤮🤮🤮🤮\n") or cadena[2]==("🤬🤬🤬🤬🤬\n")  or cadena[2]==("😠😠😠😠😠\n")  or
            cadena[2]==("👏👏👏👏👏\n") or cadena[2]==("😤😤😤😤😤😤😤😤\n") or cadena[2]==("🤬🤬🖕🖕🤬🖕\n") or
            cadena[2]==("😠🤬😡😠😡😡😠😡😡🤬🤬🤬") or cadena[2]==("🤑🤑🤑🤑🤑🤑🤑🤑") or cadena[2]==("🤢🤢🤢🤢🤢🤢🤢\n")
        or cadena[2]==("😠😠😠😤😤😠😠\n") or cadena[2]==("😡😡😡😡😠😠\n") or cadena[2]==("🖕🖕🖕🖕\n") or cadena[2]==("😨😨😠😠😱\n")
            or cadena[2]==("🐁🐁🐁🐁🤬🤬🤬\n") or cadena[2]==(", 💩💩💩👹👹👺\n") or cadena[2]==("👎👎👎👎\n") or cadena[2]==("🐀🐀🐀🐀🐀🐀🐀🐀\n")
        or cadena[2]==("🐀🐀🐀🐀") or cadena[2]==("🤬🤬🤬🤬🤬🤬🤬🤬\n") or cadena[2]==("🐀🐀🐀🐀🐀\n") or cadena[2]==("🐀🐀🐀🐀🐀🐀🐀🐀🐀🐀\n")
            or cadena[2]==("🐀🐀🐀🐀🐀🐀🐁🐁🐁🐁🐭🐭🐭\n") or cadena[2]==("🐁🐁🐁🐁🐀🐀🐀🐀🐀\n") or cadena[2]==("💩💩💩💩💩\n") or
        cadena[2]==("🤮🤮🤮🤮🤮🤮🤮🤮🤮\n") or cadena[2]==("🐀🐀🐀🦎🦂🦟🦞🐜\n") or cadena[2]==("😡😡😡😡😡")
                or cadena[2]==("😤🤬😡🤬🤬🤬🤬🤬\n") or cadena[2]==("🤬😤🤬🤬🤬\n") or cadena[2]==("🖕🖕🖕💩💩💩\n")
             or cadena[2]==("😡🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮\n") or cadena[2]==("😄😄😄😄😄😄😄\n") or cadena[2]==("💪💪💪💪💪\n")
        or cadena[2]==("👏🏻👏🏻👏🏻👏🏻👏🏻\n") or cadena[2]==("😜😜😜😜\n") or cadena[2]==("😮😮😮😮😮\n") or cadena[2]==("😧😧😱😭😮🤐🤬😡🤬😱😰🤢\n")
        or cadena[2]==("🇪🇨🇪🇨🇪🇨👍👍👍💪💪💪\n") or cadena[2]==("😂😂😂😂\n") or cadena[2]==("😱😱😱😱\n") or cadena[2]==("🙏🙏🙏🙏\n")
             or cadena[2]==("😮😮😮😮🍻") or cadena[2]==("👌👌💪💪💪🇪🇨🇪🇨🇪🇨💪💪💪💪\n") or cadena[2]==("😥😥😥😥😥😥😥😪😪😪😪😪\n")
        or cadena[2]==("🤬🤬🤬🤬🤬🤬\n") or cadena[2]==("👏👏👏👏👏👏\n") or cadena[2]==("🙏🙏🙏🙏🙏\n") or cadena[2]==("🤮🤮🤮🤮🤮🤮🤮🤮\n")
        or cadena[2]==("🤮🤮🤮🤮🤮🤮\n") or cadena[2]==("🐀🐀🐀🐀\n") or cadena[2]==("😡😡😡😡😡\n") or cadena[2]==("🐀🐀🐀🐀🐀🐀\n")
        or cadena[2]==("😂🤣😭😭🤣😂🤣😂😂😂😂\n") or cadena[2]==("😡😡😡😡😡👿👿👿👿\n") or cadena[2]==("😡😡😡🤬🤬🤬🤬🤮🤮🤮")
        or cadena[2]==("😡😡😡🤬🤬🤬🤬🤮🤮🤮\n") or cadena[2]==("👉🏼🤥🐀💰💰💰\n") or cadena[2]==("😨😨😠😠😱\n") or cadena[2]==("👏🏼👏🏼👏🏼👏🏼👏🏼\n")
        or cadena[2]==("🤬🤬🤬🤬😠😤\n") or cadena[2]==("😡😡😡😡👹\n") or cadena[2]==("♿♿♿♿👈👉😠😠😠😠\n") or cadena[2]==("👏👏👏👏\n")
             or cadena[2]==("🤬🤬😡😡🤨😡🤬👩‍✈️👨‍✈️🤦‍♀️🖕🖕\n") or cadena[2]==("😠😠😠😠🤬🤬🤬\n") or cadena[2]==("🇪🇨🇪🇨🇪🇨🇪🇨\n")
        or cadena[2]==("🖕🖕🖕🖕🖕\n") or cadena[2]==("😡😡😡😠😠😠😠\n") or cadena[2]==("♿♿♿♿👈💀💀💀👉👍👍👍👍\n") or cadena[2]==("🏽👏🏽👏🏽👏🏽👏🏽👏🏽👏🏽👏\n")
        or cadena[2]==("🤬🤬🤬🤬\n") or cadena[2]==("💪👉💪👉\n") or cadena[2]==("💩💩💩💩💩💩💩💩💩💩💩\n") or cadena[2]==("😣😣😣😣😣😣\n")
        or cadena[2] == ("👏🏽👏🏽👏🏽👏🏽👏🏽👏🏽👏🏽👏🏽\n") or cadena[2] == ("😲😲😲😲\n") or cadena[2] == ("😒😡😠💩\n") or cadena[2] == ("💩💩💩💩💩💩\n")
        or cadena[2] == ("🐁🐁🐁🤮🤮\n") or cadena[2] == ("💥💥💥💥💥💥💥\n") or cadena[2] == ("👿👿👿👹👹👿👹\n") or cadena[2] == ("🤮🤮🤮🤮🤧🤮🤮🤮🤮\n")
        or cadena[2]==("🐁🐁🐁🐁🐁🐁\n") or cadena[2]==("🐀🐁🐁🐁🐁🐁🐁🐁🐁\n") or cadena[2]==("👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏\n") or cadena[2]==("😩😩😩😩\n")
        or cadena[2]==("😡😡😡😡🤬🤬🤬🤬\n") or cadena[2]==("🐷🐷🐷🐷\n") or cadena[2]==("🤮🤮🤮🤧🤮\n") or cadena[2]==("👎👎👎👎👎👎👎👎\n")
        or cadena[2]==("🤢🤢🤢🤢\n") or cadena[2]==("👎👎👎👎👎👎\n") or cadena[2]==("🇪🇨😭😭😭😭😭\n") or cadena[2]==("🤬🤬🤬🤬🤬🤬🤬🤬🤬\n")
        or cadena[2]==("😡😡😡😡😡😡😡🤬\n") or cadena[2]==("😎😎😎😎😎😎😎😎😎\n") or cadena[2]==("😡😡😠😠😠😠😠😡😡🤬🤬\n")
        or cadena[2]==("😤😤😤😤\n") or cadena[2]==("🤣🤣🤣🤣\n") or cadena[2]==("😤😤😤😤😤🤮🤮🤮\n") or cadena[2]==(".................\n")
        or cadena[2]==("🙃🙃🙃🙃🙃🙃🙃\n") or cadena[2]==("😡😡😡😡😡😡😡\n") or cadena[2]==(":=====================D\n") or cadena[2]==("😡😡😡😡😡😡😡😡😡🤬🤬🤬🤬🤬🤬\n")
        or cadena[2]==("👀👀👀👀🤔🤔🤔\n") or cadena[2]==("😃😃😃😃\n") or cadena[2]==("????????\n") or cadena[2]==("🤮🤮🤮🐀🐀🐀\n")
        or cadena[2]==("😭😭😭😭😭😭\n") or cadena[2]==("😬😬😬😬😬😬\n") or cadena[2]==("🤢🤢🤮🤮🤮🤮🤮\n") or cadena[2]==("🤗🤗🤗😍😍😍\n")
        or cadena[2]==("🤑🤑🤑🤑🤑\n") or cadena[2]==("🤔😠😠😡😡😡\n") or cadena[2]==("😈👿😈😈👿😈😈\n") or cadena[2]==("😘😘😘😘😘😘😘\n")
        or cadena[2]==("😝😝😝😝\n") or cadena[2]==("🤢🤢🤮🤮🤮🤮👎👎\n") or cadena[2]==("😤💪💪💪💪😤😤😤😤🖕🖕🖕🖕🖕\n") or cadena[2]==("🤢🤢🤢🤮🤮🤮🤮💩💩")
        or cadena[2]==("😒😒😒😒😒\n") or cadena[2]==("🥰😀😀😀☺️🥰🥰🥰🥰🥰\n") or cadena[2]==("🤔🤔🤔🤔🤔🤔🤔\n") or cadena[2]==("👍👍👍✋👌👌👌\n")
        or cadena[2]==("C\n") or cadena[2]==("PTRRR\n") or cadena[2]==("😡😡😡😡😡😡😡😡\n") or cadena[2]==("🖕🖕🖕🖕🖕🖕\n") or cadena[2]==("😡😡😡😡😡😡🤮🤮🤮🤮🤮🤮🤮🤮🤮\n")
        or cadena[2]==("🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮🤮\n") or cadena[2]==("😠🤬😡😠😡😡😠😡😡🤬🤬🤬\n") or cadena[2]==("M\n") or cadena[2]==("🤑🤑🤑🤑🤑🤑🤑🤑\n")
        or cadena[2]==(":P\n") or cadena[2]==("🤑🤮🤮🤮🤮🤮🤮🤮\n") or cadena[2]==("👏👏👏👏👏👏👏👏") or cadena[2]==("🇪🇨🥰🥰🥰🥰🥰🥰🇪🇨🥰\n")
        or cadena[2]==("😮😮😮😮🍻\n") or cadena[2]==(":(\n") or cadena[2]==(":3\n") or cadena[2]==("...\n") or cadena[2]==("MMMM\n") or cadena[2]==(":3")
        or cadena[2]==("💩💩💩🐀🐀🐀🐀🐀\n") or cadena[2]==("🙏🙏🙏🙏🙏🙏🙏🙏🙏\n") or cadena[2]==("👎👊👎👎👎👎👎🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕\n") or cadena[2]==("😈😈😈😈😈😈😈\n")
        or cadena[2]==("15$$👊🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️\n") or cadena[2]==("😵😡😡😡\n") or cadena[2]==("🦓🦓🦓🦓🦓🦓🦓🦓🦓🦓🦓🦓🦓🦓\n")
        or cadena[2]==("😠😡😠😡\n") or cadena[2]==("👣👣👣👀👀🥊\n") or cadena[2]==("😴😝😤😠\n") or cadena[2]==("😥😣😭😢\n") or cadena[2]==("🙏🙏🇪🇨😘💪👍❤🇪🇸\n")
        or cadena[2]==("😤😤😤😤😤\n") or cadena[2]==("😫😫😫😖😖\n") or cadena[2]==("🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡\n") or cadena[2]==(":V\n") or cadena[2]==(":V")
        or cadena[2]==("😒😒😒😒\n") or cadena[2]==("😡😡😡😡😡😡😡😡😡😡😡😡\n") or cadena[2]==("😏😏😏😏😏😏😏😏\n") or cadena[2]==("😒😒😒😒😒😒😒😒😕😕😕😕😕😯😕\n")
        or cadena[2]==("MMMMMM\n") or cadena[2]==("MOR :3\n") or cadena[2]==("BBÉ\n")):
            h34=h34+1
        #    print(cadena[2])
        elif(cadena[2].find("PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA!PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA!PRENSA VENDIDA! PRENSA VENDIDA! PRENSA VENDIDA! DIGAN LA VERDAD DE LO QUE ESTÁ PASANDO EN NUESTRO PAÍS")!=-1
        or cadena[2]==("PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA PRENSA VENDIDA\n")
        or cadena[2]==("#PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS  #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA #PRENSAVENDIDA #PRENSAVENDIDA #NOTICIASFALSAS #PRENSAVENDIDA\n")):
            h35=h35+1
         #   print(cadena[2])
        elif(cadena[2].find("#PRENSAVENDIDA, #PRENSAVENDIDA #PRENSAVENDIDA , #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA,#PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA, #PRENSAVENDIDA,#PRENSAVENDIDA, #PRENSAVENDIDA")!=-1):
            h36=h36+1
        elif(cadena[2].find("#TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ #TARTAMUDOGILJORGEORTIZ")!=-1):
            h37=h37+1
        elif(cadena[2].find("#PRENSAVENDIDA #PRENSAVENDIDA #PRENSACORRUPTA#FALTADEETICAPROFESIONAL#PROFESIONALESMEDIOCRES")!=-1):
        #    print(cadena[2])
            h38=h38+1
        elif(cadena[2].find("#PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA #PRENSAVENDIDAYCORRUPTA")!=-1):
            h39=h39+1
        elif(cadena[2].find("#PRENSAVENDIDA #PRENSACORRUPTA #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO #PRENSAVENDIDA #PRENSACORRUPTA  #NOALCERCOMEDIÁTICO")!=-1):
            h40=h40+1
        elif(cadena[2].find("#PRENSA #VENDIDA #CORRUPTA#PRENSA #VENDIDA #CORRUPTA#PRENSA #VENDIDA #CORRUPTA#PRENSA #VENDIDA #CORRUPTA#PRENSA #VENDIDA #CORRUPTA")!=-1):
            h41=h41+1
        elif(cadena[2].find("#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA\n")!=-1 or
        cadena[2]==("#PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA #PRENSAVENDIDA#PRENSAVENDIDA")):
            h42=h42+1
         #   print(cadena[2])
        elif(cadena[2]==("#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS#NOCREOENLOSMEDIOS")):
            h43=h43+1
        elif (cadena[2]==("#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA\n") or cadena[2]==("#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA#PRESOCORREA\n")):
            h44=h44+1
        elif(cadena[2]==("#VITERIASESINA #VITERIASESINA#VITERIASESINA #VITERIASESINA#VITERIASESINA #VITERIASESINA#VITERIASESINA #VITERIASESINA#VITERIASESINA #VITERIASESINA#VITERIASESINA #VITERIASESINA#VITERIASESINA #VITERIASESINA#VITERIASESINA #VITERIASESINA\n")):
            h45=h45+1
        elif(cadena[2]==("#PRENSAVENDIDA #DENUNCIAESTAPAGINA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA #DENUNCIAESTAPAGINA#PRENSAVENDIDA\n")
        or cadena[2]==("#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA#DENUNCIAESTAPAGINA #SPAMPRENSAVENDIDA\n")):
            h46=h46+1
        #    print(cadena[2])
        elif(cadena[2].find("PUBLICARÉ LO Q' ME PIDAN/︶\#PRENSAVENDIDA ES #PRENSACORRUPTA#PRENSAVENDIDA ES #PRENSACORRUPTA#PRENSAVENDIDA ES #PRENSACORRUPTA#PRENSAVENDIDA ES #PRENSACORRUPTA#PRENSAVENDIDA ES #PRENSACORRUPTA#PRENSAVENDIDA ES #PRENSACORRUPTA #PRENSAVENDIDA ES #PRENSACORRUPTA")!=-1):
            h47=h47+1
        elif(cadena[2]==("#NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTESI NOS ACORDAMOS DE LAS MALAS ACCIONES DE SU PASADO ESO NO SE OLVIDA#NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE\n") or cadena[2]==("#NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTESI NOS ACORDAMOS DE LAS MALAS ACCIONES DE SU PASADO ESO NO SE OLVIDA#NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE #NEBOTNOSERAPRESIDENTE\n")):
            h48=h48+1
         #   print(cadena[2])
        else:
            i = i + 1
          #  print(cadena)
            narchivo.write(str(linea))
           # print(str(i)+"trama"+str(linea))

    total=h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12+h13+h14+h15+h16+h17+h18+h19+h20+h21+h22+h23+h24+h25+h26+h27+h28+h29+h30+h31+h32+h33+h34+h35+h36+h37+h38+h39+h40+h41+h42+h43+h44+h45+h46+h47+h48
    print("Nombre de archivo: ",f,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24,"h25",h25,h26,h27,h28,h29,h30,h31,h32,h33,h34,h35,h36,h37,h38,h39,h40,h41,h42,h43,h44,h45,h46,h47,h48,"total de comentarios borrados: ",total,"n° comentarios limpiados: ",i)
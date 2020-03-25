import os
import glob
import os.path

listEntree = []
listSortie = []

# TODO apres :
# Decouper chaque fichier pour verifier qu'il correspond a un certain
#formalisme
#si le fichie correspond a un certain formalisme
# on compare les N groupes de la chaine de caractere : line 72



# du cote verification, il y a autant de # que de parties à vérifier

def listdirectory(path):
    print(path)
    fichier=[]
    l = glob.glob(path+'\\*')
    for i in l:
        if os.path.isdir(i): fichier.extend(listdirectory(i))
        else: fichier.append(i)
    return fichier

def listfiles(path):
    print(path)
    fichier=[]
    l = glob.glob(path+'\\*')
    for i in l:
        if os.path.isdir(i): fichier.extend(listfiles(i))
        else: fichier.append(i)
    return fichier

def verifType(chaineA,type) :
# doit prendre en compte les
# [a) : doit commencer par le caractere a
# (b] : doit finir par le caractere b
# type a,b ou n
# les eventuels formalismes
# ^ : peut contenir des espaces
# ~ : peut contenir des points
# ~^ : peut contenir des points et des espaces
# (x) : doit contenir x caracteres

    varA = 0
    return varA


def changementType (chaineA, typeVers):
# |~ : doit contenir des points à la place d'eventuels espaces
# |^ : doit contenir des espaces à la place d'eventuels points
    varW = 0
    return varW

def testFormalisme(chaine2,formalisme):
    varZ = 0
    return varZ


def renLikeSortie(chaineaRen, formalismeCorrespondant ) :
    varY = 0
    return varY





def decoupeFichier (chainedeCaracte,chaineformalisme):
# pour chague formalisme défini on verifie si le fichier et toutes
# ses parties correspondent à un formalisme présent dans la liste des formalismes recerhcés
# en partant du dernier formalisme pour arriver au debut
# si le fichier correspond alors on le transforme selon le formalisme defini
# On teste chaque listEntree pour verifier si le fichier peut deja correspondre

# On cherche le nombre de parties du formalisme

    pos = 0
    lastpos = 0
    trigg = 0
    nbForm = 0
    tFrSS = 0
    listFormalismePresent = []
    listResultsFindForminChaine = []

    while pos < len(chaineformalisme):
        if chaineformalisme[pos] == '#':
            nbForm = nbForm + 1
            trigg = pos
            listFormalismePresent.append(chaineformalisme[lastpos:pos])
            listResultsFindForminChaine.append("42")
            lastpos = pos + 1
        pos = pos + 1

    print(listFormalismePresent)

    # trigg : derniere position du # (normalement en derniere position)
    # nbForm : nombre de chaines dans le formalisme

    print (trigg)
    print (nbForm)
    tFrSS = nbForm
    # On va donc verifier qu'il est possible de faire nbForm parties avec la chaine de caracteres testee
    # selon le formalisme de chaque partie


    while tFrSS > 0 :
        # On decoupe correctement la chaine de caractere du formalisme
        chercheandCompare(chainedeCaracte,listFormalismePresent[tFrSS - 1])
        tFrSS = tFrSS - 1


    varYI= 0
    return varYI

def chercheandCompare(chaineIn, boutdeformalisme):

    varT= 0
    chaineRecherchee = 0

    #etat initial : 42
    # etat chaine de caractere trouve : 0
    # etat hesitation : 1
    # etat Non trouvé : 100


    # doit prendre en compte les
    # $a$ : doit commencer par le caractere a
    # £b£ : doit finir par le caractere b
    # {a} : caracteres purement alpha
    # {b} : caracteres alpha et numerique
    # {n} : caracteres purement numerique
    # ^ : peut contenir des espaces
    # ~ : peut contenir des points
    # ~^ : peut contenir des points et des espaces
    # (x) : doit contenir exactement x caracteres

    print("####################################")

    print("bout de formalisme : ", boutdeformalisme)
  #  print("##############")


    #determination du type

    typerecherch = boutdeformalisme[boutdeformalisme.find('{')+1:boutdeformalisme.find('}')]
    print("typerecherch : ", typerecherch)

    if typerecherch.startswith('a'):
        chaineRecherchee = chaineRecherchee + 1
    if typerecherch.startswith('b'):
        chaineRecherchee = chaineRecherchee + 2
    if typerecherch.startswith('n'):
        chaineRecherchee = chaineRecherchee + 3

    #determination du contenu

    contenurecherch = boutdeformalisme[:boutdeformalisme.find('{')]
    print("contenurecherch : ", contenurecherch)

    if contenurecherch == "" :
        chaineRecherchee = chaineRecherchee + 10
    if contenurecherch == "~" :
        chaineRecherchee = chaineRecherchee + 20
    if contenurecherch == "^" :
        chaineRecherchee = chaineRecherchee + 30
    if contenurecherch == "~^" :
        chaineRecherchee = chaineRecherchee + 40


    #determination du debut ou de la fin
    if boutdeformalisme.find('&') != -1 :
        startwithrecher = boutdeformalisme[boutdeformalisme.find('&')+1:][:boutdeformalisme[boutdeformalisme.find('&')+1:].find('&')]
        print("startwithrecher : ", startwithrecher)
        chaineRecherchee = chaineRecherchee + 200
    else :
        chaineRecherchee = chaineRecherchee + 100

    #determination du debut ou de la fin
    if boutdeformalisme.find('£') != -1 :
        endwithrecher = boutdeformalisme[boutdeformalisme.find('£') + 1:][:boutdeformalisme[boutdeformalisme.find('£') + 1:].find('£')]
        print("endwithrecher : ", endwithrecher)
        chaineRecherchee = chaineRecherchee + 2000
    else :
        chaineRecherchee = chaineRecherchee + 1000

    #determination de la taille
    # TODO : determination de la taille : du meme type que les 2 précédents
    taillerecherch = boutdeformalisme[boutdeformalisme.find('(')+1:boutdeformalisme.find(')')]
    print("taillerecherch : ", taillerecherch)

    if boutdeformalisme.find('(') == -1 :
        chaineRecherchee = chaineRecherchee + 10000
    if boutdeformalisme.find(')') == -1 :
        chaineRecherchee = chaineRecherchee + 10000
    else:
        chaineRecherchee = chaineRecherchee + 20000

    print("chaineRecherchee global : ", chaineRecherchee)

    return varT



def decoupeFormalisme (chainedeCaractere):
#coupe la chaine formalisme
# pour definir la liste des elements entrees
# et la liste des elements sorties
    varYI= 0

    pos = 0
    trigg = 0
    while pos < len(chainedeCaractere):
        if chainedeCaractere[pos] == '>':
            trigg = pos
        pos = pos + 1

    print(trigg)
    listEntree.append(chainedeCaractere[:trigg-1])
    listSortie.append(chainedeCaractere[trigg+1:])
    print(listEntree)
    print(listSortie)
    return varYI

def listFormalismeDispo():
    varNbForm = 0

    file = open('conf/formalisme.nhi', "r")
    # utiliser readlines pour lire toutes les lignes du fichier
    # La variable "lignes" est une liste contenant toutes les lignes du fichier
    lines = file.readlines()
    # fermez le fichier après avoir lu les lignes
    file.close()
    # Itérer sur les lignes
    for line in lines:
       # print(line.strip())
        decoupeFormalisme(line.strip())
        varNbForm += 1
    print(varNbForm)




file = open('conf/rep.nhi', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
line = file.readline()
# fermez le fichier après avoir lu les lignes
file.close()
# Itérer sur les lignes
variaREP = line.strip()

#listFormalismeDispo()


for root, directories, files in os.walk(variaREP):
    for file in files:
        print(file)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

decoupeFichier("[Test1]Foo.Test.2111.1980.Cop2 - Copie.txt", "~^{b0}&[&£]£#~^{b1}#{n0}&19&(4)#~^{b2}#{b3}&.&(4)#")



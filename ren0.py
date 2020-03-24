import os
import glob
import os.path

listEntree = []
listSortie = []

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

def decoupeFichier (nomduFichier):
# pour chague formalisme défini on verifie si le fichier et toutes
# ses parties correspondent à un formalisme présent dans la liste des formalismes recerhcés
# en partant du dernier formalisme pour arriver au debut
# si le fichier correspond alors on le transforme selon le formalisme defini
    varYI= 0
    return varYI

def decoupeFormalisme (chainedeCaractere):
#coupe la chaine formalisme
# pour definir la liste des elements entrees
# et la liste des elements sorties
    varYI= 0

    print(chainedeCaractere.find('#'))
    listEntree.append(chainedeCaractere[:chainedeCaractere.find('#')])
   # listSortie.append
    print(listEntree)
    #print (listSortie)
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
        print(line.strip())
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

listFormalismeDispo()


for root, directories, files in os.walk(variaREP):
    for file in files:
        print(file)




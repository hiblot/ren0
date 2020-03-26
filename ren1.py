import os
import glob
import os.path

listTentative = []
listFilesBefore = []
listFilesAfter = []
listRename = []

def listTargetRep():
    file = open('conf/rep.nhi', "r")
    # utiliser readlines pour lire toutes les lignes du fichier
    # La variable "lignes" est une liste contenant toutes les lignes du fichier
    line = file.readline()
    # fermez le fichier après avoir lu les lignes
    file.close()
    # Itérer sur les lignes
    variaREP = line.strip()
    return variaREP

def datATr(fileNametoTr,indexGil):

    # Etape 1 : on remplace tous les caracteres d'espace, de - et de _ par des.
    fileNametoTr = fileNametoTr.replace(' ','.')
    fileNametoTr = fileNametoTr.replace('-','.')
    fileNametoTr = fileNametoTr.replace('_','.')
    listFilesAfter[indexGil] = fileNametoTr
    print(listFilesAfter)
    print("~~~~~~~~~~~~~~~ EO STEP 1 ~~~~~~~~~~~~~~~~~~~~~~~~")

    #Etape 2 : on remplace tous les n+1 points qui se suivent par un .
    pos = fileNametoTr.find('..')
    if pos != -1:
        while pos != -1:
            fileNametoTr = fileNametoTr[:pos] + fileNametoTr[pos+1:]
            pos = fileNametoTr.find('..')
    listFilesAfter[indexGil] = fileNametoTr
    print(listFilesAfter)
    print("~~~~~~~~~~~~~~~ EO STEP 2 ~~~~~~~~~~~~~~~~~~~~~~~~")

    # Etape 3 : chercher une date entre 2. commencant par 19 ou 20 en 4 chiffres
    # Substring du dernier . pour l'extension
    # Substring entre date et position du dernier. pour l'extension

    indexC = len(fileNametoTr)-1
    while indexC > 0:
        if fileNametoTr[indexC] == '.':
            posextension = indexC
            break
        else:
            indexC = indexC - 1

    posdate19 = fileNametoTr.find('.19')
    if posdate19 != -1:
        if fileNametoTr[posdate19+1].isdigit() and fileNametoTr[posdate19+2].isdigit():
            fileNametoTr = fileNametoTr[:posdate19] + fileNametoTr[posextension:]

    posdate20 = fileNametoTr.find('.20')
    if posdate20 != -1:
        if fileNametoTr[posdate20+1].isdigit() and fileNametoTr[posdate20+2].isdigit():
            fileNametoTr = fileNametoTr[:posdate20] + fileNametoTr[posextension:]

    listFilesAfter[indexGil] = fileNametoTr
    print(listFilesAfter)
    print("~~~~~~~~~~~~~~~ EO STEP 3 ~~~~~~~~~~~~~~~~~~~~~~~~")

    # Etape 4 : chercher si le debut du fichier commence par () ou {} ou []
    # Verifier  le pos + 1  si c'est un point si c'est un point on supprime egalement le point

    if fileNametoTr.startswith('('):
        poscar1 = fileNametoTr.find(')')
        if poscar1 != -1:
            if fileNametoTr[poscar1+1] == '.':
                poscar1 = poscar1 + 2
            fileNametoTr = fileNametoTr[poscar1:]

    if fileNametoTr.startswith('['):
        poscar2 = fileNametoTr.find(']')
        if poscar2 != -1:
            if fileNametoTr[poscar2+1] == '.':
                poscar2 = poscar2 + 2
            fileNametoTr = fileNametoTr[poscar2:]

    if fileNametoTr.startswith('{'):
        poscar3 = fileNametoTr.find('}')
        if poscar3 != -1:
            if fileNametoTr[poscar3+1] == '.':
                poscar3 = poscar3 + 2
            fileNametoTr = fileNametoTr[poscar3:]

    listFilesAfter[indexGil] = fileNametoTr
    print(listFilesAfter)
    print("~~~~~~~~~~~~~~~ EO STEP 4 ~~~~~~~~~~~~~~~~~~~~~~~~")


    # Etape 5  : On renomme donc tous les fichiers de la listeAvant par les noms de la listeBefore
    # Meme si ceux ci n'ont pas ete modifies par datATr


def mainFunc():
    variaREP = listTargetRep()
    indexFile = 0
    for root, directories, files in os.walk(variaREP):
        for file in files:
            listFilesBefore.append(file)
            listFilesAfter.append(file)
            datATr(listFilesAfter[indexFile],indexFile)
            indexFile = indexFile + 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(listFilesBefore)
    print(listFilesAfter)


mainFunc()

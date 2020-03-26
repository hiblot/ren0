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
    print("~~~~~~~~~~~~~~~ STEP 1 ~~~~~~~~~~~~~~~~~~~~~~~~")

    #Etape 2 : on remplace tous les n+1 points qui se suivent par un .
    pos = fileNametoTr.find('..')
    if pos != -1:
        while pos != -1:
            fileNametoTr = fileNametoTr[:pos] + fileNametoTr[pos+1:]
            pos = fileNametoTr.find('..')
    listFilesAfter[indexGil] = fileNametoTr
    print(listFilesAfter)
    print("~~~~~~~~~~~~~~~ STEP 2 ~~~~~~~~~~~~~~~~~~~~~~~~")

    # Etape 3 : chercher une date entre 2. commencant par 19 ou 20 en 4 chiffres
    # Substring du dernier . pour l'extension
    # Substring entre date et position du dernier. pour l'extension







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

import os

import morph
import utils
from constants import *

def createCollection (articlesPath=ARTICLES_DIR_NAME):
    if not os.path.exists(articlesPath):
        print('ОШИБКА: не получается найти статьи')
        return -1
    normalizedArrayOfDocRes, tfCounter = morph.normalizeArrayOfDoc(extractText(articlesPath).split(SPLIT_SENTENCES))
    utils.writeToFile(COLLECTIONS_FILE_NAME, normalizedArrayOfDocRes)
    utils.writeToFile(TF_FILE_NAME, tfCounter)
    return 0

def extractText (dirName):
    resultText = ''
    for dirItem in os.listdir(dirName):
        pathToItem = os.path.join(dirName, dirItem)
        if os.path.isdir(pathToItem):
            resultText += extractText(pathToItem)
        _, fileExtension = os.path.splitext(pathToItem)
        if fileExtension == TXT_ETENSION:
            file = open(pathToItem, FILE_MODE_READ)
            resultText += file.read()
            file.close()
    return resultText
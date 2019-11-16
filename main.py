import os
import sys
import math
from collections import Counter

from numpy import dot
from numpy.linalg import norm

import morph
import search
import gencollection
import utils
from constants import *


def checkCollections ():
    if ((not os.path.exists(COLLECTIONS_FILE_NAME)) or
            (not os.path.exists(TF_FILE_NAME)) or
                (PARAM_UPDATE_COLLECTIONS in sys.argv)):
        print('Обновление коллекций ...')
        if gencollection.createCollection() == -1:
            return -1
        print('Коллекции обновлены')

def getCollections ():
    if checkCollections() == -1:
        print('ОШИБКА: коллекции не прошли проверку')
        return -1
    return eval(utils.readFromFile(COLLECTIONS_FILE_NAME)), eval(utils.readFromFile(TF_FILE_NAME))

def getQuery ():
    return input('Введите запрос >>> ')

def cmpKey (x):
    return x['weight']

def main ():
    mode = ''
    if PARAM_SEARCH_MODEL_TFIDF in sys.argv:
        mode = SEARCH_MODEL_TFIDF
    elif PARAM_SEARCH_MODEL_VECT in sys.argv:
        mode = SEARCH_MODEL_VECT
    else:
        print('Выберите параметры поиска:')
        print('\t' + PARAM_SEARCH_MODEL_TFIDF + ' для использования tfidf модели')
        print('\t' + PARAM_SEARCH_MODEL_VECT + ' для использования векторной модели')
        return
    collections, termsCounter = getCollections()
    query = getQuery()
    query = morph.normalizeDoc(query)
    collections = search.getSearchResults(query, collections, termsCounter, mode)

    if collections == -1:
        return

    lim = RECORDS_LIMIT
    
    for record in sorted(collections, key = cmpKey, reverse = True):
        print('ДОКУМЕНТ: ' + record['src'])
        print('ВЕС: ' + str(record['weight']))
        print('\n========================================\n')
        if lim <= 0:
            break
        lim -= 1
    print('Показано первых ' + str(RECORDS_LIMIT) + ' записей')


if __name__ == "__main__":
    main()
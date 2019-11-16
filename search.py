import math
from collections import Counter, defaultdict

from constants import *

def cosBetweenVectors (v1, v2):
    res = 0
    for i in range(min(len(v1), len(v2))):
        res += v1[i] * v2[i]
    mulRes = vectorLen(v1) * vectorLen(v2)
    if mulRes == 0:
        return 0
    res /= mulRes
    return res

def vectorLen (vector):
    res = 0
    for i in vector:
        res += i * i
    return math.sqrt(res)

def tfidfModelSearch (query, collections, termsCounter):
    print('tfidf model')
    for record in collections:
        queryVector = []
        docVector = []
        docCounter = record['dst']
        for word in (docCounter + query):
            idf = termsCounter[word]['idf'] if word in termsCounter else 0
            queryVector.append(query[word] * idf)
            docVector.append(docCounter[word] * idf)
        record['weight'] = cosBetweenVectors(queryVector, docVector)
    return collections

def vectModelSearch (query, collections):
    print('vector model')
    for record in collections:
        queryVector = []
        docVector = []
        docCounter = record['dst']
        for word in (docCounter + query):
            queryVector.append(query[word])
            docVector.append(docCounter[word])
        record['weight'] = cosBetweenVectors(queryVector, docVector)
    return collections

def getSearchResults (query, collections, termsCounter, mode):
    if mode == SEARCH_MODEL_VECT:
        return vectModelSearch(query, collections)
    return tfidfModelSearch(query, collections, termsCounter)
import pymorphy2
import math

from constants import *
from collections import Counter, defaultdict


def noramlizeWord (word):
    morphAnalyzer = pymorphy2.MorphAnalyzer()
    word = word.lower()
    word = ''.join(filter(lambda x: x in ALLOWED_CHARS, word))
    if len(word) > 0:
        return morphAnalyzer.parse(word)[0].normal_form
    return ''

def normalizeDoc (doc):
    resultDoc = ''
    for word in doc.split(SPLIT_WORDS):
        noramlizedWordRes = noramlizeWord(word)
        if len(noramlizedWordRes) > 0:
            resultDoc += noramlizedWordRes + SPLIT_WORDS
    resultDoc = resultDoc.strip()
    return Counter(defaultdict(list)) + Counter(resultDoc.split(SPLIT_WORDS))

def normalizeArrayOfDoc (arrayOfDoc):
    resultArray = []
    resultDict = {}
    docsNum = len(arrayOfDoc)
    for i, doc in enumerate(arrayOfDoc):
        print(str(i+1) + ' / ' + str(docsNum))
        normalizedDocRes = normalizeDoc(doc)
        if len(normalizedDocRes) > 0:
            for key in normalizedDocRes:
                if key in resultDict:
                    resultDict[key]['tf'] += normalizedDocRes[key]
                    resultDict[key]['df'] += 1
                else:
                    resultDict[key] = {
                        'tf': normalizedDocRes[key],
                        'df': 1,
                        'idf': 0
                    }
            resultArray.append({
                'src': doc.strip(), 
                'dst': normalizedDocRes,
            })
    for key in resultDict:
        resultDict[key]['idf'] = math.log10(docsNum / resultDict[key]['df'])
    return resultArray, resultDict

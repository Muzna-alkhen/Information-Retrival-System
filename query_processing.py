import math
import string
from collections import Counter

from autocorrect import Speller
from numpy import linalg as LA
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

import date_processing
import dictionary_processing
import numbers_processing
import vector_model

spell = Speller(lang='en')
def process(query):

    count = 0
    ps = PorterStemmer()
    wl = WordNetLemmatizer()
    table = str.maketrans(dict.fromkeys(string.punctuation))

    stop_words = stopwords.words("english")
    for i in stop_words:
        i.lower()

    query = query.lower()
    query = spell(query)
    query = date_processing.date_regex(query)
    query = numbers_processing.formatNumbers(query)
    query = dictionary_processing.dictionaryFormat(query)
    query = word_tokenize(query)

    query = [item for item in query if item not in stop_words]
    query = [item.translate(table) for item in query]
    query = [ps.stem(item) for item in query]
    query = [wl.lemmatize(item, 'v') for item in query]

    return query

def tf_idf(query,total_vocab,N,df_map):
    tf_idf = {}
    counter = Counter(query)
    words_count = len(query)
    for token in np.unique(query):
        tf = counter[token] / words_count
        if (token in total_vocab):
            df = df_map[token]
        else:
            df=1
        idf = math.log((N+1)/(df+1))
        tf_idf[token] = tf * idf


    return tf_idf


def build_vector(n,total_vocab,tf_idf):
    vector = np.zeros((1, len(total_vocab)))
    for i in tf_idf:
        if (i in total_vocab):
            ind = total_vocab.index(i)
            vector[0][ind] = tf_idf[i]

    return vector


def cos_similarity(a, b):
    # return (np.sum(vector*matrix,axis=1) / (np.sqrt(np.sum(matrix**2,axis=1)) * np.sqrt(np.sum(vector**2))))[::-1]
    return np.dot(a,b,out=None) / float(LA.norm(a) * LA.norm(b))


def similarity(doc_vectors,query_vector,docs_num):
    similarity_array =[]
    for i in range (0,docs_num):
        similarity = cos_similarity(query_vector,doc_vectors[i])
        similarity_array.insert(i, (" similarity {} , document {}".format(float(similarity), i+1)))
    return similarity_array

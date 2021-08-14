from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import date_processing
import numbers_processing
import dictionary_processing


def listToString(s):
    listToStr = ' '.join([str(elem) for elem in s])
    return listToStr

def textprocessing(files):
    stop_words = stopwords.words("english")
    for i in stop_words:
        i.lower()
    # print(stop_words)
    count=0
    for i in files:
        files[count] = files[count].lower()
        count += 1

    count = 0
    for i in files:
        files[count] = date_processing.date_regex(files[count])
        files[count] = numbers_processing.formatNumbers(files[count])
        count += 1

    count = 0
    for i in files:
        files[count] = dictionary_processing.dictionaryFormat(files[count])
        count += 1

    table = str.maketrans(dict.fromkeys(string.punctuation))
    # count = 0
    # for i in files:
    #     files[count] = files[count].translate(table)
    #     count+=1

    count = 0
    ps = PorterStemmer()
    wl = WordNetLemmatizer()

    for i in files:
        files[count] = word_tokenize(i)
        files[count] = [item for item in files[count] if item not in stop_words]
        files[count] = [item.translate(table) for item in files[count]]
        files[count] = [ps.stem(item) for item in files[count]]
        files[count] = [wl.lemmatize(item, 'v') for item in files[count]]
#        files[count] = listToString(files[count])

        count += 1

    # print(files)

    return files


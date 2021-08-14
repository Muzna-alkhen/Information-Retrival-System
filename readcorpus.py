import os
from nltk.tokenize import word_tokenize

def read_corpus_files ():
    # os.listdir : returns the names of the files in the directory data as a list
    list_of_files = os.listdir("C:\\Users\\HP\\Desktop\\ir\\Lab4\\corpus\\")

    # Remove the ext ".txt" from the names of the files in the list
    for i in range(0, len(list_of_files)):
        list_of_files[i] = list_of_files[i].split('.')[0]

    # converted the names of the files from string to int to sort the list in order
    for i in range(0, len(list_of_files)):
        list_of_files[i] = int(list_of_files[i])

    # sort the names of the files
    sorted_list_of_files = sorted(list_of_files)

    # converted the names of the files from int to string after sorting
    for i in range(0, len(sorted_list_of_files)):
        sorted_list_of_files[i] = str(sorted_list_of_files[i])
    files = []
    pre = "C:\\Users\\HP\\Desktop\\ir\\Lab4\\corpus\\"
    post = ".txt"

    for file in sorted_list_of_files:
        f = open(pre + file + post, "r")
        files.append(f.read())

    f.close()
    return files


def read_stopwords():
    stop = open("C:\\Users\\HP\\Desktop\\ir\\Lab4\\stop words.txt", "r")
    stop_words_str = stop.read()
    stop_words = word_tokenize(stop_words_str)
    # print(stop_words)
    return stop_words



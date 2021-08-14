from nltk import word_tokenize


def read_queries():
    listt = []
    lin=""
    f = open('C:\\Users\\HP\\Desktop\\ir\\Lab4\\IR Homework\\Queries.txt', 'r')
    liness = f.readlines()
    for line in liness:
        liness.remove("\n")
    liness =[item.replace("\n","") for item in liness]
    for line in liness:
                if '*' not in line:
                    lin += line
                    lin+=" "
                else:
                 listt.append(lin)
                 lin = ""
    listt.pop(0)
    return listt


def read_relevance():
    f = open('C:\\Users\\HP\\Desktop\\ir\\Lab4\\IR Homework\\relevance.txt', 'r')
    lines = f.readlines()

    for line in lines:
        lines.remove("\n")
    lines = [item.replace('\n', '') for item in lines]
    splitedlines = [word_tokenize(item) for item in lines]
    for i in splitedlines:
         i.pop(0)
    return splitedlines


def Union(list1, list2):
    ln = []
    for i in list1:
        if i in list2:
            ln.append(i)
    return len(ln)

#
# t = read_queries()
# print (read_relevance())

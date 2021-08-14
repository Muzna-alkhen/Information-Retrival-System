from collections import Counter
import np
def df(processed_text) :
    DF = {}
    for i in range(len(processed_text)):
        tokens = processed_text[i]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}
    for i in DF:
        DF[i] = len(DF[i])

    return DF


def tf_idf(processed_text,df_map):
    tf_idf = {}
    N=len(processed_text)
    with open("C:\\Users\\HP\\Desktop\\ir\\Lab4\\test.txt", 'w') as fw:
        for i in range(N):
            tokens = processed_text[i]
            counter = Counter(tokens)
            words_count=len(np.unique(tokens))
            for token in np.unique(tokens):
                tf = counter[token]/words_count
                df = df_map[token]
                idf = np.log(N/(df+1))
                tf_idf[i, token] = tf*idf
                fw.write(str(i))
                fw.write(',')
                fw.write(token)
                fw.write('-->')
                fw.write(str(tf_idf[i, token]))
                fw.write("\n")
        return(tf_idf)

# Document Vectorization
def build_docs_vectors(n,total_vocab,tf_idf):
    docs_vectors = np.zeros((n, len(total_vocab)))
    for i in tf_idf:
        ind = total_vocab.index(i[1])
        docs_vectors[i[0]][ind] = tf_idf[i]
    return docs_vectors


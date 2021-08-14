import numpy

import corpus_processing as process
import evalution
import query_processing
import readcorpus as read
import vector_model
from sklearn import metrics
import time


print('\n','Starting the offline processing !!! . . . . . . . .  ','\n')
#offline
print('reading corpus . . . . . . . .  ','\n')
files = read.read_corpus_files()
print('processing corpus . . . . . . . .  ','\n')
corpus_tokens = process.textprocessing(files)
print('---->finish with total time :', int(time.time() % 60),' seconds','\n')
print('calculating df for corpus terms . . . . . . . .  ','\n')
df = vector_model.df(corpus_tokens)
print('---->finish with total time :', int(time.time() % 60),'seconds','\n')
print('building index . . . . . . . .  ','\n')
index_terms= [x for x in df]
print('---->finish with total time :', int(time.time() % 60),'seconds','\n')
print('calculating tf_idf values for index terms . . . . . . . .  ','\n')
tf_idf_matrix =vector_model.tf_idf(corpus_tokens,df)
docs_num= len(files)
print('---->finish with total time :', int(time.time() % 60),'seconds','\n')
print('building documents vector . . . . . . . .  ','\n')
doc_vectors=vector_model.build_docs_vectors(docs_num, index_terms, tf_idf_matrix)
print('---->finish with total time :', int(time.time() % 60),'seconds','\n')


with open("C:\\Users\\HP\\Desktop\\ir\\Lab4\\index_terms.txt", 'w') as fw:
    fw.write('Index terms : ')
    fw.write('\n')
    for i in range(0,len(index_terms)):
        fw.write('index ')
        fw.write(str(i))
        fw.write('-->')
        fw.write(index_terms[i])
        fw.write('\n')

with open("C:\\Users\\HP\\Desktop\\ir\\Lab4\\doc_vectors.txt", 'w') as fw1:
    fw1.write('doc_vectors : ')
    fw1.write('\n')
    for i in doc_vectors:
        fw1.write(str(i))
        fw1.write('\n')


print('Starting the online processing !!! . . . . . . . .  ','\n')
#online
print('reading queries file . . . . . . . .  ','\n')
query_list = evalution.read_queries()
print('---->finish with total time :', int(time.time() % 60),'seconds','\n')
print('reading relevance file . . . . . . . .  ','\n')
relevance_list=evalution.read_relevance()
my_relevence_list= []
precision=numpy.zeros(len(query_list))
recall=numpy.zeros(len(query_list))
counter = 0
print('---->finish with total time :', int(time.time() % 60),'seconds','\n')
print('matching and calculating recision and recall for each query  . . . . . . . .  ','\n')
for query in query_list:
    query = query_processing.process(query)
    tf_idf_query = query_processing.tf_idf(query, index_terms, docs_num, df)
    query_vector = query_processing.build_vector(docs_num, index_terms, tf_idf_query)
    similarity_map = query_processing.similarity(doc_vectors, query_vector, docs_num)
    sorted_similarity_array = sorted(similarity_map, reverse=True)
    query_result = []
    for i in range(0,17):
      res = sorted_similarity_array[i].split(' ')
      doc = res[len(res) - 1]
      query_result.append(doc)
    precision[counter]=evalution.Union(query_result,relevance_list[counter])/len(query_result)
    recall[counter]=evalution.Union(query_result,relevance_list[counter])/len(relevance_list[counter])
    print('query ',counter+1,':','precision:',precision[counter],'recall:',recall[counter],'\n')
    my_relevence_list.append(query_result)
    counter= counter + 1

sorted_precision = sorted(precision, reverse=True)
sorted_recall = sorted(recall, reverse=True)
auc=metrics.auc(sorted_precision, sorted_recall)

for i in range(0,len(my_relevence_list)):
    print ('query: ',i+1,' ',my_relevence_list[i],'\n')

print('----> FINISH !!!!!!  total time :', int(time.time() % 60),'seconds','\n')
print('AREA UNDER CURVE (AUC) = ')
print(auc)


# while True:
#         try:
#
#             print('//////////////')
#             query = input()
#             query = query_processing.process(query)
#
#             tf_idf_query = query_processing.tf_idf(query, index_terms, docs_num, df)
#
#             query_vector = query_processing.build_vector(docs_num, index_terms, tf_idf_query)
#
#             similarity_map = query_processing.similarity(doc_vectors, query_vector, docs_num)
#
#             sorted_similarity_array = sorted(similarity_map, reverse=True)
#             query_result=[]
#             for i in range(0,17):
#                 print(i, '--->', sorted_similarity_array[i])
#                 res = sorted_similarity_array[i].split(' ')
#                 doc = res[len(res) - 1]
#                 query_result.append(doc)
#
#
#             print('// NEW QUERY ///// ')
#         except EOFError:
#             break

#
#
# with open("C:\\Users\\HP\\Desktop\\ir\\Lab4\\test1.txt", 'w') as fw1:
#     for i in range (0,len(index_terms)):
#         fw1.write(index_terms[i])
#         fw1.write(' : ')
#         fw1.write(str(query_vector[0][i]))
#         fw1.write('\n')









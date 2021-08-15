*General Description:* 

An information retrieval system capable of adding documents and performing text processing to them then you can retrieve documents throw writing queries.
The current documents (corpus) is list of articles (NEWYORK-TIMES journal).

*The project performs offline operations as follows:*

1. Read the files (corpus).

2. Text processing.

3. Build index terms.

4. Calculate the tf-idf for each term in the index for each file.

5. Document vectorization (Vector Model)


*The project performs online operations as follows:*

1. Read the queries file (queries.txt)

2. Read the correct results file (relevance.txt)

3. For each individual query: 
     1. Query text processing (in the same way as word processing in files while offline).

     2. Calculate the tf-idf values for each term in the query.

     3. Building the query vectorization.

    4. matching, which is the percentage of similarity of the query with each file in the  corpus by calculating the cos similarity with each vector representing a file.

    5. Save the first 18 identical results between query and files.

    6. Calculate the precision of the query based on the correct results in the file relevance.txt

    7. Calculate the recall rate for the query based on the correct results in the relevance.txt file

4. Aggregate match results for all queries.

5. calculate area under curve “according to the values of precision and recall”.

*Implementation Details:*

- Programming language:  Python 

- Tokenization : word_tokenize  | nltk.tokenize

- Stemming : PorterStemmer |  nltk.tokenize

- Lemmatization : WordNetLemmatizer | nltk.tokenize

- Access to idioms that have different forms (dates) : By writing regular expressions manually and capturing the matches with methods from the re . library
Convert the corresponding dates into a standard format with the strftime method.

- Access to expressions that have different forms (numbers) : Manually searching for the numbers and convert them into a standard text format using the num2words function from the num2words library.

- Correcting words in case of entering an incorrect query : Using the Speller English dictionary from the autocorrect library.

- Access to names in different ways of written representation: Manually define a group of words in the corpus that appear in more than one way, by building a map

- Building Index : manually using the unique terminologies for each corpus. 

-Model Type : (Building a vector model) manually for each file (the terms in the index) and manually calculating the tf_idf values through the map data structure.

-Matching : Manually calculate the cos similarity value of the query with each file using mathematical functions np.dot and LA from numpy . library

*Results :*
 
- The entire application (offline and online processing) was executed with a time of 55 seconds.

- The value for area under curve is 0.6411 .



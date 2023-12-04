# import all the necessary modules
import math
import re as re  # import the regular expression module as 're'
import sys  # import the sys module
import statistics  # import the statistics module
import nltk  # import the Natural Language Toolkit (nltk) module
# import the stopwords from the nltk.corpus module
from nltk.corpus import stopwords
# import the WordNetLemmatizer class from the nltk.stem module
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet  # import the wordnet from the nltk.corpus module
import matplotlib.pyplot as plt  # import the matplotlib.pyplot module as 'plt'
# import the tabulate function from the tabulate module
from tabulate import tabulate
import time  # import the time module
import os
from itertools import islice



# download all the necessary resources
nltk.download('stopwords')  # download the 'stopwords' resource from nltk
nltk.download('punkt')  # download the 'punkt' resource from nltk
# download the 'averaged_perceptron_tagger' resource from nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')  # download the 'wordnet' resource from nltk
nltk.download('omw-1.4')  # download the 'omw-1.4' resource from nltk
# create a sorted set of the English stopwords from the nltk.corpus module
stopwords_nltk = sorted(set(stopwords.words('english')))

with open(os.path.join('.','Dickens','library.txt')) as l:  # open the file 'Library.txt' in read mode and store the file object in 'l'
    library = l.read()  # read the contents of the file and store it in the 'library' variable
    index_list = []  # initialize an empty list called 'index_list'
    year_list = []  # initialize an empty list called 'year_list'
    title_list = []  # initialize an empty list called 'title_list'
    counter = 0  # initialize a counter variable to 0
    l.seek(0)  # reset the file cursor to the beginning of the file
    for line in l.readlines():  # iterate over the lines in the file
        counter += 1  # increment the counter variable by 1
        # skip first 2 iterations of the loop (to skip header and blank line)
        if counter <= 2:
            continue
        index_list.append(
            line.split()[0])  # append the first element of the list returned by 'line.split()' to 'index_list'
        year_list.append(
            line.split()[-1])  # append the last element of the list returned by 'line.split()' to 'year_list'
        title_list.append(line.split()[
                          1:-1])  # append all elements of the list returned by 'line.split()' except the first and last elements to 'title_list'

title = []  # initialize an empty list called 'title'
for t in title_list:  # iterate over the elements in 'title_list'
    title.append(
        ' '.join(t))  # join the elements in 't' with a space character and append the resulting string to 'title'
year = [y.replace('(', '').replace(')', '') for y in
        year_list]  # create a new list called 'year' by replacing '(' and ')' with an empty string in each element of 'year_list'
index = [i.replace('.', '') for i in
         index_list]  # create a new list called 'index' by replacing '.' with an empty string in each element of 'index_list'
# delete the variables 'index_list', 'year_list', and 'title_list'
del index_list, year_list, title_list

table_book = []  # initialize an empty list called 'table_book'
for i in range(len(index)):  # iterate over the indices in the range of the length of 'index'
    table_book.append([index[i], title[i], year[
        i]])  # append a list containing the i-th elements of 'index', 'title', and 'year' to 'table_book'
print(tabulate(table_book, headers=['Index', 'Title',
                                    'Year']))  # print a formatted table using 'table_book' as the data and ['Index', 'Title', 'Year'] as the headers

# Choose the books to analyze
choices = input(
    'Choose the books (insert numbers separated by a whitespace) that you want to compare: \n')  # prompt the user to input a string of numbers separated by whitespaces
# split the string into a list of strings using whitespace as the separator
choices_list = choices.split()
library_chosen = []  # initialize an empty list called 'library_chosen'

# exclude values that are not numbers
for x in choices_list:  # iterate over the elements in 'choices_list'
    try:
        x = int(x)  # try to convert 'x' to an integer
    except ValueError:  # if the conversion fails, print an error message and exit the program
        sys.exit('Input error')
        break
    # if the conversion succeeds, append 'x' to 'library_chosen'
    library_chosen.append(x)
library_chosen.sort()  # sort the elements in 'library_chosen' in ascending order
# delete the variables 'choices_list', 'choices', and 'library'
del choices_list, choices, library

for value in library_chosen:  # iterate over the elements in 'library_chosen'
    if value not in range(1, 23):  # if the value is not in the range 1-23
        sys.exit('No book with the chosen index!')  # print an error message and exit the program
        break

library_chosen_titles = [title[b - 1] for b in
                         library_chosen]  # create a new list called 'library_chosen_titles' by selecting the (b-1)-th element of 'title' for each element 'b' in 'library_chosen'

# Choose parameters
with open(os.path.join('.','Dickens','parameters1.txt')) as p:  # open the file 'parameters1.txt' in read mode and store the file object in 'p'
    # read the contents of the file and store it in the 'parameters_txt' variable
    parameters_txt = p.read()
    p_index_list = []  # initialize an empty list called 'p_index_list'
    p_name = []  # initialize an empty list called 'p_name'
    counter = 0  # initialize a counter variable to 0
    p.seek(0)  # reset the file cursor to the beginning of the file
    for line in p.readlines():  # iterate over the lines in the file
        counter += 1  # increment the counter variable by 1
        # skip the first two iterations of the loop (to skip header and blank line)
        if counter <= 2:
            continue
        p_index_list.append(
            line.split()[0])  # append the first element of the list returned by 'line.split()' to 'p_index_list'
        p_name.append(' '.join(line.split()[
                               1:-1]))  # append the result of joining the elements in the list returned by 'line.split()' except the first and last elements with a space character to 'p_name'
p_index_total = [int(i.replace('.', '')) for i in
                 p_index_list]  # create a new list called 'p_index_total' by replacing '.' with an empty string in each element of 'p_index_list' and converting the resulting strings to integers

index_table = []  # initialize an empty list called 'index_table'
for i in range(len(p_name)):  # iterate over the indices in the range of the length of 'p_name'
    index_table.append([p_index_total[i], p_name[
        i]])  # append a list containing the i-th elements of 'p_index_total' and 'p_name' to 'index_table'
print(tabulate(index_table, headers=['Index',
                                     'Parameter']))  # print a formatted table using 'index_table' as the data and ['Index', 'Parameter'] as the headers
# Choose parameters
parameter_chosen = input('\nChoose the PARAMETER(/s) you want to visualize for the book(/s) chosen '
                         '(insert numbers separated by a whitespace): \n ')
# prompt the user to input a string of numbers separated by whitespaces
# take only numeric values and convert them in int
p_chosen = []  # initialize an empty list called 'p_chosen'
for y in parameter_chosen:  # iterate over the characters in 'parameter_chosen'
    try:
        y = int(y)  # try to convert 'y' to an integer
        # if the conversion succeeds, append 'y' to 'p_chosen'
        p_chosen.append(y)
    except ValueError:  # if the conversion fails, do nothing
        pass  # exclude values that are not numbers

if len(p_chosen) == 0: #if list not empty
    sys.exit('Insert at least one numeric value!')
else:
    p_chosen.sort()  # sort the elements in 'p_chosen' in ascending order


# check that p_chosen in range
for value in p_chosen:  # iterate over the elements in 'p_chosen'
    if value not in range(1, 9):  # if the value is not in the range 1-9
        sys.exit('The parameter chosen is not in the list!')  # print an error message and exit the loop
        break

p_chosen.sort()  # sort the elements in 'p_chosen' in ascending order

print('The program is loading, please wait ...\n')

#### FUNCTIONS ####

threshold = 29000 # tokens threshold

# Remove the header and the footer from the book
def read_this(file_path):  # define a function that takes in a single argument 'file_path'
    book = []  # initialize an empty list called 'book'
    with open(file_path, 'r',
              encoding='utf-8') as f:  # open the file with the given 'file_path' in read mode and store the file object in 'f'
        initiation = None  # initialize a variable called 'initiation' to None
        ending = None  # initialize a variable called 'ending' to None
        # iterate over the lines in 'f' and their indices
        for i, line in enumerate(f):
            if '*** START OF THE PROJECT GUTENBERG EBOOK' in line or '*** START OF THIS PROJECT GUTENBERG EBOOK' in line or '***START OF THE PROJECT' in line:
                # if any of the given strings is in 'line'
                initiation = i  # set 'initiation' to the index 'i'
            if '*** END OF THE PROJECT GUTENBERG EBOOK' in line or '*** END OF THIS PROJECT GUTENBERG EBOOK' in line or '***END OF THE PROJECT' in line:
                # if any of the given strings is in 'line'
                ending = i  # set 'ending' to the index 'i'

        if initiation is not None and ending is not None:  # if both 'initiation' and 'ending' have been set
            f.seek(0)  # reset the file cursor to the beginning of the file
            # iterate over the lines in 'f' and their indices
            for i, line in enumerate(f):
                if i >= initiation and i <= ending:  # if 'i' is within the range of 'initiation' and 'ending'
                    book.append(line)  # append 'line' to 'book'
        else:  # if either 'initiation' or 'ending' or both are not set
            # set 'book' to the list of lines in the file (to avoid blank books in dataset)
            book = f.readlines()
    book = ' '.join(book)  # join the elements in 'book' with a space character
    book = book.lower()  # convert the characters in 'book' to lowercase
    return book

# Clean the book
def clean_book(book):  # define a function that takes in a single argument 'book'
    # replace all the line breaks with a space
    book = book.replace('\r', ' ').replace('\n', ' ')
    words = book.split()
    book = " ".join(islice(words, threshold)) #islice can be used to slice an iterable, skipping for loop
    return book


# Split the book into sentences
def find_sentences(book):  # define a function that takes in a single argument 'book'
    sentences = []  # initialize an empty list called 'sentences'
    # split 'book' into a list of sentences using the regular expression 'r'
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', book)
    # (?<!\w.\w.) -> (?<!) is a negative lookbehind assertion. Means do not split when (\w.\w.) pattern is found = do not split
    # when there is any alphanumerical character (\w) followed by a period (.) followed by another alphanumerical character (\w).
    # In general this component is important because it allows us to avoid cases like (Dr. or Mr.) to cause the sentence detection.
    # N.B. It's avoiding the point to have its "splitting properties".

    # (?<![A-Z][a-z].) -> Again another negative lookbehind that ensures that the split does not occur if the preceding
    # characters (of the point) are uppercase letters followed by a lower case letter and a period (e.g Dr.). Problem with 'Mrs.'

    # (?<=.|?) -> Positive lookbehind assertion (?<=). It looks for whitespace characters (\s) only if it is preceded by a period (.)
    # or (|) a question mark (?)

    # \s -> After the points we want a whitespace

    # To sum up: the first two components make sure that we escape the situations of Dr. or Mr. (negative lookbehind) while the
    # third one is specifying what cases we want to match and split.
    return sentences


# Tokenize the book
def find_tokens(book):  # define a function that takes in a single argument 'book'
    tokens = []  # initialize an empty list called 'tokens'
    tokens = re.findall('[a-zA-Z]+',
                        book)  # find all alphabetic characters in 'book' using the regular expression '[a-zA-Z]+'
    # it looks for one or more consecutive occurrences of an uppercase or lowercase letter 'a-zA-Z'
    return tokens


# Find the uniquewords in the book
def find_uniquewords(book):  # define a function that takes in a single argument 'book'
    unique_words = []  # initialize an empty list called 'unique_words'
    unique_words = sorted(set(find_tokens(
        book)))  # nested function: find all unique tokens in 'book' using the 'find_tokens' function and sort the resulting list in alphabetical order
    return unique_words


# define a function that takes in a single argument 'book'
def dictionary_ordered(book):
    dict_uniq = {}  # initialize an empty dictionary called 'dict_uniq'
    words = []  # initialize an empty list called 'words'
    tmp = []  # initialize an empty list called 'tmp'

    # iterate over the tokens in 'book' returned by the 'find_tokens' function
    for w in find_tokens(book):
        if w in words:  # if 'w' is already in 'words'
            # increment the value in 'dict_uniq' corresponding to the key 'w' by 1
            dict_uniq[w] += 1
        else:  # if 'w' is not in 'words'
            words.append(w)  # append 'w' to 'words'
            # set the value in 'dict_uniq' corresponding to the key 'w' to 1
            dict_uniq[w] = 1
    # sort dictionary and set type to tuple
    for key, value in dict_uniq.items():  # iterate over the key-value pairs in 'dict_uniq'
        couple = (
            value, key)  # create a tuple called 'couple' with 'value' as the first element and 'key' as the second element
        # assign to each position of the list tmp a couple of value+key
        tmp.append(couple)
    tmp = sorted(tmp, reverse=True)  # sort 'tmp' in reverse order
    return tmp


# Find stopwords in the book
def stopwords_in_book(book):  # define a function that takes in a single argument 'book'
    counter = 0  # initialize a counter variable to 0
    stopwords_book_list = []  # initialize an empty list called 'stopwords_book_list'

    for w in tokens:  # iterate over the elements in the list 'tokens'
        if w in stopwords_nltk:  # if 'w' is in the list 'stopwords_nltk'
            counter = counter + 1  # increment the counter by 1
            # append 'w' to 'stopwords_book_list'
            stopwords_book_list.append(w)

    return stopwords_book_list


# Find the average length of the sentences in the book
# define a function that takes in a single argument 'book'
def mean_sentence_length(book):
    sentence_length_value = []  # initialize an empty list called 'sentence_length_value'
    for sentence in sentences:  # iterate over the elements in the list 'sentences'
        sentence_length_value.append(
            len(sentence.split()))  # append the length of the list returned by 'sentence.split()' to 'sentence_length_value'
    mean_sentence_length = sum(sentence_length_value) / len(
        sentences)  # calculate the mean sentence length by dividing the sum of 'sentence_length_value' by the length of 'sentences'
    return mean_sentence_length


# Find the standard deviation of the sentence length
# define a function that takes in a single argument 'book'
def sd_sentence_length(book):
    sentence_length_value = []  # initialize an empty list called 'sentence_length_value'
    for sentence in sentences:  # iterate over the elements in the list 'sentences'
        sentence_length_value.append(
            len(sentence.split()))  # append the length of the list returned by 'sentence.split()' to 'sentence_length_value'
    sd_sentence_length = statistics.stdev(
        sentence_length_value)  # calculate the standard deviation of 'sentence_length_value' using the 'stdev' function from the 'statistics' module
    return sd_sentence_length


# Calculate the type - token ratio
def type_token_ratio(book):  # define a function that takes in a single argument 'book'
    type_token_ratio = len(unique_words) / len(
        tokens)  # calculate the type-token ratio by dividing the length of 'unique_words' by the length of 'tokens'
    return type_token_ratio


# Calculate the filler words - token ratio
# define a function that takes in a single argument 'book'
def filler_token_ratio(book):
    filler_token_ratio = len(stopwords) / len(
        tokens)  # calculate the filler-token ratio by dividing the length of 'stopwords' by the length of 'tokens'
    return filler_token_ratio


# Find only the content words in the book
def filter_words(book):  # define a function that takes in a single argument 'book'
    dictionary = {value: key for key, value in
                  d}  # create a dictionary using a dictionary comprehension, where the keys are the values in 'd' and the values are the corresponding keys in 'd'
    content_words_unsorted = [word for word in unique_words if
                              word not in stopwords_nltk]  # create a list of words in 'unique_words' that are not in 'stopwords_nltk'
    content_words_sorted = sorted(content_words_unsorted, key=dictionary.get,
                                  reverse=True)  # sort 'content_words_unsorted' in descending order based on the values in 'dictionary'
    return (content_words_sorted)


lemmatizer = WordNetLemmatizer()  # create an instance of WordNetLemmatizer


# Redefine the part of speech tags
def pos_tagger(nltk_tag):  # define a function that takes in a single argument 'nltk_tag'
    if nltk_tag.startswith('J'):  # if 'nltk_tag' starts with 'J'
        return wordnet.ADJ  # return the constant for adjective from the wordnet module
    elif nltk_tag.startswith('V'):  # if 'nltk_tag' starts with 'V'
        return wordnet.VERB  # return the constant for verb from the wordnet module
    elif nltk_tag.startswith('N'):  # if 'nltk_tag' starts with 'N'
        return wordnet.NOUN  # return the constant for noun from the wordnet module
    elif nltk_tag.startswith('R'):  # if 'nltk_tag' starts with 'R'
        return wordnet.ADV  # return the constant for adverb from the wordnet module
    else:
        return  # return None in all other cases


# Lemmatize the book
def lemmatize(book):  # define a function that takes in a single argument 'book'
    # find the POS tag for each word in the 'content_words' list
    pos_tagged = nltk.pos_tag(content_words)
    wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])),
                              pos_tagged))  # it maps the POS tags to the corresponding wordnet tag using the 'pos_tagger()' function
    # initialize an empty list called 'lemmatized_content_words'
    lemmatized_content_words = []
    for word, tag in wordnet_tagged:  # for each word-tag pair in wordnet_tagged
        if tag is None:  # if there is no available tag, append the content word as it is
            lemmatized_content_words.append(word)
        else:  # if the tag is not 'None'
            lemmatized_content_words.append(lemmatizer.lemmatize(word,
                                                                 tag))  # the function lemmatizes the word using the 'WordNetLemmatizer' object's 'lemmatize()' method and appends the lemmatized word to the 'lemmatized_content_words' list
    # the function joins the words in the 'lemmatized_content_words list' into a single string and returns the result
    return lemmatized_content_words

# Remove duplicates from the 'lemmatized_content_words' list


def unique_lemmas(book):
    # get the set of all lemmas in the book and convert it to a list to deduplicate it
    unique_lemmas = [*set(lemm)]
    unique_lemmas.sort()  # sort the list of unique lemmas in alphabetical order
    return unique_lemmas  # return the sorted list of unique lemmas


# Calculate the lemma - token ratio
def lemma_token_ratio(book):
    tokens = find_tokens(book)
    # calculate the ratio of unique lemmas to total number of tokens
    lemma_token_ratio = len(uniq_lemmas) / len(tokens)
    return lemma_token_ratio


# Find the average length of the words in the book
def mean_word_length(book):
    word_lengths = 0  # initialize a variable to store the total length of all words in the book
    for t in tokens:  # iterate through each token in the book
        # add the length of the current token to the total word length
        word_lengths += len(t)
    mean_word_length = word_lengths / len(
        tokens)  # calculate the mean word length by dividing the total word length by the number of tokens
    return mean_word_length  # return the mean word length

    #### LIST OF VARIABLES ####


book = []  # list of words in a book
tok = []  # list of tokens in a book
sent = []  # list of sentences in a book
uniq_words = []  # list of unique words in a book
dic = []  # list of tuples representing the dictionary with unique_words and their frequency
stopw = []  # list of stop words
mean_s_l = []  # list of mean sentence lengths
sd_s_length = []  # list of standard deviations of sentence lengths
typetoken_ratio = []  # list of type-token ratios for a book
fillertoken_ratio = []  # list of filler-token ratios for a book
lemmas = []  # list of lemmas in a book
content_w = []  # list of content words in a book
u_lemm = []  # list of unique lemmas in a book
lemm_tok_r = []  # list of lemma-token ratios for a book
mean_w_l = []  # list of mean word lengths for a book

# Compute the parameters for each book in the list.
# N.B. This process is done only for the chosen books (hence, less books means less time to compute)
for i in library_chosen:  # iterate for each book in the 'library_chosen' list
    # read each book in the list
    book = read_this(os.path.join('.','Dickens', f'{i}.txt'))
    book = clean_book(book) # remove \n and \r and apply threshold
    tokens = find_tokens(
        book)  # process the 'book' string to find and return a list of tokens and store it in the 'tokens' variable
    sentences = find_sentences(
        book)  # process the 'book' string to find and return a list of sentences and store it in the 'sentences' variable
    unique_words = find_uniquewords(
        book)  # process the 'book' string to find and return a list of unique words and store it in the 'unique_words' variable
    d = dictionary_ordered(
        book)  # process the 'book' string to create and return a dictionary of words and their frequencies, with the words ordered by frequency and store it in the 'd' variable
    stopwords = stopwords_in_book(
        book)  # process the 'book' string to find and return a list of stop words and store it in the 'stop_words' variable
    mean_sent_length = mean_sentence_length(
        book)  # process the 'book' string to calculate and return the mean sentence length and store it in the 'mean_sent_length' variable
    sd_sent_length = sd_sentence_length(
        book)  # process the 'book' string to calculate and return the standard deviation of sentence length and store it in the 'sd_sent_length' variable
    type_token_r = type_token_ratio(
        book)  # process the 'book' string to calculate and return the type-token ratio and store it in the 'type_token_r' variable
    filler_token_r = filler_token_ratio(
        book)  # process the 'book' string to calculate and return the filler-token ratio and store it in the 'filler_token_r' variable
    content_words = filter_words(
        book)  # process the 'book' string to find and return a list of content words and store it in the 'content_words' variable
    lemm = lemmatize(
        book)  # process the 'book' string to find and return a list of lemmas for the words in the book and store it in the 'lemm' variable
    uniq_lemmas = unique_lemmas(
        book)  # process the 'book' string to find and return a list of unique lemmas and store it in the 'uniq_lemmas' variable
    lemmas_token_r = lemma_token_ratio(
        book)  # process the 'book' string to calculate and return the lemma-token ratio and store it in the 'lemmas_token_r' variable
    mean_word_l = mean_word_length(
        book)  # process the 'book' string to calculate and return the mean word length and store it in the 'mean_word_l' variable

    # This code appends the values of the variables to the corresponding lists
    # This allows you to store the values for each book in a list, so that you can easily access and compare the values for different books.

    # the value of the 'tokens' variable is appended to the 'tok' list
    tok.append(tokens)
    # the value of the 'sentences' variable is appended to the 'sent' list
    sent.append(sentences)
    # the value of the 'unique_words' variable is appended to the 'uniq_words' list
    uniq_words.append(unique_words)
    dic.append(d)  # the value of the 'd' variable is appended to the 'dic' list
    # the value of the 'stopwords' variable is appended to the 'stopw' list
    stopw.append(stopwords)
    # the value of the 'mean_sent_length' variable is appended to the 'mean_s_l' list
    mean_s_l.append(mean_sent_length)
    sd_s_length.append(
        sd_sent_length)  # the value of the 'sd_sent_length' variable is appended to the 'sd_s_length' list
    typetoken_ratio.append(
        type_token_r)  # the value of the 'type_token_r' variable is appended to the 'typetoken_ratio' list
    fillertoken_ratio.append(
        filler_token_r)  # the value of the 'filler_token_r' variable is appended to the 'fillertoken_ratio' list
    # the value of the 'content_words' variable is appended to the 'content_w' list
    content_w.append(content_words)
    # the value of the 'lemm' variable is appended to the 'lemmas' list
    lemmas.append(lemm)
    # the value of the 'uniq_lemmas' variable is appended to the 'u_lemm' list
    u_lemm.append(uniq_lemmas)
    # the value of the 'lemmas_token_r' variable is appended to the 'lemm_tok_r' list
    lemm_tok_r.append(lemmas_token_r)
    # the value of the 'mean_word_l' variable is appended to the 'mean_w_l' list
    mean_w_l.append(mean_word_l)

    # This code deletes the variables that were used to store the values calculated in the previous code block
    del tokens, sentences, unique_words, stopwords, mean_sent_length, sd_sent_length, \
        type_token_r, filler_token_r, lemm, uniq_lemmas, lemmas_token_r, mean_word_l

# Choose the display mode of the data
while True:  # prompt the user to choose how they want the data to be shown
    data_type = input('How do you want the data to be shown?:\n'
                      '1. Tabulate\n'  # if '1' is chosen, the data will show in a table
                      '2. Graph\n'  # if '2' is chosen, the data will show in a graph
                      '[N.B. Parameter 1 and 2 can\'t be shown in visually in a graph]\n')
    # The data referring to the frequency of words are not shown in graphs, but in a table
    if data_type == '1' or data_type == '2':
        break  # if the user inputs a valid option, break the loop
    else:  # if the user inputs an invalid option,
        # print an error message and continue the loop
        print('Insert either 1 or 2 !\n')
        # pause the program for 2 seconds before continuing in order for the warning message to be read
        time.sleep(2)

if data_type == '2':  # if the user chose to show the data as a graph
    # if the user chose to show the frequency of words (parameter 1)
    if 1 in p_chosen:
        # the data will be shown in a table
        print('The values of par. 1 will be shown in a tabulate form')
        # Prompt the user to input the number of top words they want to be shown
        while True:  # while loop checks that top_n is a digit
            top_n_1 = input(
                'What are the top N words that you want to be shown? (Insert a number): ')
            # takes only the first digit/value (avoid crash if more than one digit)
            top_n_1 = top_n_1.split()[0]
            if top_n_1.isdigit():  # verify that top_n_1 is a digit (similar to isinstance(x, int))
                # the input is in string form, so convert into an integer
                top_n_1 = int(top_n_1)
                break
            else:  # if top_n_1 is not a digit, print an error message and continue the loop
                print('Insert a number!')
                time.sleep(2)  # pause program for 2 seconds

        # create a counter to select the elements of the parameter that have been computed (idx starts from 0 and increase by 1)
        i = 0
        for b in library_chosen:  # iterate through each book in the library_chosen list
            # print the top top_n_1 words of the book and its title
            print(f'The top {top_n_1} words of the book \"{title[b - 1]}\" are:\n'
                  f'{dic[i][:top_n_1]}\n')  # select first the dictionary of the book and then the number of element that have to be printed
            # increase the counter (is used to select the correct instances of the variables referring to the parameters)
            i += 1

    # similar procedure for the 2nd parameter
    # if the user chose to show the top content words (parameter 2)
    if 2 in p_chosen:
        print('The values of par. 2 will be shown in a tabulate form')
        time.sleep(2)
        # Prompt the user to input the number of top content words they want to be shown
        while True:  # while loop checks that top_n is a digit
            top_n_2 = input('What are the top N content words that you want to be shown? (Insert a number): ')
            # takes only the first digit/value (avoid crash if more than one digit)
            top_n_2 = top_n_2.split()[0]
            if top_n_2.isdigit():  # if top_n_2 is a digit, convert it to an integer and break the loop
                top_n_2 = int(top_n_2)
                break
            else:  # if top_n_2 is not a digit, print an error message and continue the loop
                print('Insert a number!')
                time.sleep(2)

        # create a counter to select the elements of the parameter that have been computed (idx starts from 0 and increase by 1)
        i = 0
        for b in library_chosen:
            print(f'The top {top_n_2} content words of the book \"{title[b - 1]}\" are:\n'
                  f'{content_w[i][:top_n_2]}\n')  # select first the list of the book and then the number of element that have to be printed
            i += 1
    # declare a list called `parameter_list, in order to use a single for loop for all the remaining parameters
    # The first 2 parameters have been already computed, so they are substituted with None in the paramter_list
    parameter_list = [None, None, mean_w_l, mean_s_l, sd_s_length,
                      typetoken_ratio, fillertoken_ratio, lemm_tok_r]
    # check if the user has chosen one or more parameters that are not 1 and 2
    if any(p >= 3 for p in p_chosen):
        #  for each parameter in the list `p_chosen`
        for p in p_chosen:
            # Check if the element at the index `p - 1` in the list `parameter_list` is not `None`
            # avoids picking up the first two 'None' parameters
            if parameter_list[p - 1] != None:
                # plot a line chart with `library_chosen` on the x-axis, `parameter_list[p - 1]` on the y-axis,
                # and the label `p_name[p - 1]` using markers
                plt.plot(library_chosen, parameter_list[p - 1], label=p_name[p - 1],
                         marker='o')  # different color assigned in different iterations
        plt.xlabel('Books\' year')  # set the x-axis label to "Books' year"
        # set the x-axis tick labels to the elements in the list `year` with indices specified by `library_chosen`,
        # rotated 90 degrees and with a font size of 8
        plt.xticks(library_chosen, [year[b - 1]
                   for b in library_chosen], rotation=90, fontsize=8)
        plt.legend()  # add a legend to the plot
        plt.show()  # display the plot


if data_type == '1':  # if the user chose to show the data as a table
    if 1 in p_chosen:  # if parameter 1 is chosen
        print('Values will be shown in a tabulate form')
        while True:  # while loop checks that top_n is a digit
            top_n_1 = input(
                'What are the top N words that you want to be shown? (Insert a number): ')
            # takes only the first digit/value (avoid crash if more than one digit)
            top_n_1 = top_n_1.split()[0]
            if top_n_1.isdigit():  # verify that top_n_1 is a digit (similar to isinstance(x, int))
                # the input is in string form, so convert into int
                top_n_1 = int(top_n_1)
                break
            else:
                print('Insert a number!')
                time.sleep(2)  # Pause program for 2 seconds

        # Create a counter to select the elements of the parameter that have been computed (idx starts from 0 and increase by 1)
        i = 0
        for b in library_chosen:
            print(f'The top {top_n_1} words of the book \"{title[b - 1]}\" are:\n'
                  f'{dic[i][:top_n_1]}\n')  # Select first the list of the book and then the number of element that have to be printed
            # Increase the counter (is used to select the correct istances of the variables referring to the paramters)
            i += 1

    if 2 in p_chosen:  # Similar procedure if the '2' parameter is chosen
        print('Values will be shown in a tabulate form')
        while True:  # while loop checks that top_n is a digit
            top_n_2 = input(
                'What are the top N content words that you want to be shown? (Insert a number): ')
            # takes only the first digit/value (avoid crash if more than one digit)
            top_n_2 = top_n_2.split()[0]
            if top_n_2.isdigit():
                top_n_2 = int(top_n_2)
                break
            else:
                print('Insert a number!')
                time.sleep(2)

        # create a counter to select the elements of the parameter that have been computed (idx starts from 0 and increase by 1)
        i = 0
        for b in library_chosen:
            print(f'The top {top_n_2} content words of the book \"{title[b - 1]}\" are:\n'
                  f'{content_w[i][:top_n_2]}\n')  # select first the list of the book and then the number of element that have to be printed
            i += 1

    parameter_list = [None, None, mean_w_l, mean_s_l, sd_s_length,
                      # declaring what the parameters list is, this in order to use a single for loop for all the remaining paramters
                      typetoken_ratio, fillertoken_ratio, lemm_tok_r]

    # p_chosen_list = [parameter_list[p] for p in p_chosen]
    results = []  # create a list called 'results'
    for p in p_chosen:  # for each element `p` in the list `p_chosen`
        for b in range(
                len(library_chosen)):  # for each element `b` in the range from 0 to the length of `library_chosen`
            if parameter_list[
                    p - 1] != None:  # condition != parameter 1 and 2 (already computed in earlier loops) # Check if the element at the index `p - 1` in the list `parameter_list` is not `None`
                # Print a message with the book title and the value of the element at the index `b` in the list `parameter_list[p - 1]`
                #print(
                    #f'In the book {library_chosen_titles[b]} the {p_name[p - 1]} is = {parameter_list[p - 1][b]}')
                # N.B parameter_list is a list made of lists. Thus, the first list is accessed with the parameter coming from 'p' (p-1).
                # The second list is accessed with the parameter coming from b (which is an index starting from 0 to len(library_chosen))
                t = (library_chosen_titles[b], parameter_list[p - 1][
                    b])  # create a tuple with the book title and the value of the element at the index `b` in the list `parameter_list[p - 1]`
                results.append(t)  # append the tuple to the list `results`

    # The list of tuples is not formatted correctly since we have (title, value) but title is repeated in n tuples based on the number of parameters, thus we need to create a dictionary
    # create an empty dictionary called `results_dict`
    results_dict = {}
    for title, value in results:  # iterate each value in the original tuple
        if title not in results_dict:
            results_dict[title] = [
                value]  # if title is not in dictionary, then the element is created: its key is the title, while its value is a list
        else:
            results_dict[title].append(
                value)  # if the key is already in the dictionary, then to the pre-existing list (its value) is added the second value
    result = []

    header_table = [p_name[i-1] for i in p_chosen if i != 1 and i != 2]

    for key, values in results_dict.items():
        result.append([key, *values])

    print(tabulate(result,headers=header_table))

time.sleep(3)
sys.exit('\nThanks for using our program, have a good day ;)\n\nEdoardo\nSofia')
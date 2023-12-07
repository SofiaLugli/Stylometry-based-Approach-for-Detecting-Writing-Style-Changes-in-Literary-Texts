# Stylometry-based Approach for Detecting Writing Style Changes in Literary Texts

### Edoardo Sebastiano De Duro, Sofia Lugli
-----
This project aims to conduct a text analysis of a selection of 22 books by Charles Dickens to identify changes in his writing style over time. By using a system that enables users to select the books and parameters they wish to analyze, we can provide visual representations of the author's style evolution.

## Background 
The project falls within the general framework of stylometry, which is the quantitative study of literary style. It is based on the observation that authors tend to write in relatively consistent, recognizable and unique ways. The identification of writing style changes have many applications, for instance it can be used to study early detection of diseases related to semantic and syntactic deficits; moreover it can be used in authorship attribution task; finally it is also used to expose plagiarism, by detecting a sudden change of style. 
## Materials
In the zip-folder of this project, the user will find the following files: 
1. **README file**: this is what to read first, in order to follow the instructions correctly. 
2. **main. py**: this file contains the actual code of the project. To run the program it is important to open this file directly from the project's folder, and to avoid copying and pasting it into another file.
3. **Dickens**: this is the folder that contains the 22 books of Charles Dickens saved as txt file, each of them is named with a ascending number following the date of writing. The books have been freely downloaded from The Project Gutenberg. Moreover, it contains the **library.txt** file, containing the title and the dates of the 22 books found in the folder; finally it also includes the **parameters1.txt** file, which contains the lits of the eight parameters. 

## Parameters 
With reference to the literature, our feature set is composed of eight writing-style parameters considered as important indicators of the writing style of an author. 
1. **N Highest Frequency Words**: indicates the words with highest frequency in the text, both content and filler words are shown. 
2. **N Highest Frequency Unique Content Words**: indicates only the content words with highest frequency, only content words are shown, the filler words are exlcuded. 
3. **Mean Word Lenght**: measures the average length of words. Longer words are traditionally associated with more pedantic and formal styles, whereas shorter words are a typical feature of informal language.
4. **Mean Sentence Length**: measures the average number of words in a sentence. Some stylistic choices, like the use of simple or complex sentence structure, can influence the mean length of sentences. In addition, it can also indicate a text's difficulty level, a text with shorter sentences tend to be easier to read and understand than a text with longer sentences.
5. **Sentence Length Standard Deviation**: indicates the variation of sentence length, which is an important marker of style.
6. **Type/Token Ratio**: indicates the proportion of unique words (types) to the total number of words (tokens). 
7. **Filler/Token Ratio**: indicates the proportion of the filler words (e.g., a, and, in, to, we ...) to the total number of words.
8. **Lemma/Token Ratio**: indicates the proportion of the unique lemmatized word-types (lemma) to the total number of words. It is an indicatore of the richness of the author's vocabulary: the higher the ratio, the more varied the vocabulary.

Some of the above parameters are sensitive to text lenght, therefore we had to establish a cut-off treshold. Since each book in our dataset contains at least 29,000 tokens, we considered only the first 29,000 tokens of each book.

## Prerequisites
Before starting, it is necessary to import the following modules. If they are not present, they must be installed using the *pip* command

    import math
    import re as re 
    import statistics  
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import wordnet
    import matplotlib.pyplot as plt
    from tabulate import tabulate
    import time
    import os
    from itertools import islice

And the following resources:

    nltk.download('stopwords') 
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger') 
    nltk.download('wordnet') 
    nltk.download('omw-1.4') 

## Usage
After downloading all the packages, the program will show a table containg the books of Charles Dickens saved in the folder: 

    Index       Title                             Year

      1  The Pickwick Papers                      1837
      2  Oliver Twist                             1838
      3  Nicholas Nickleby                        1839
      4  The Old Curiosity Shop                   1841
      5  Barnaby Rudge                            1841
      6  Martin Chuzzlewit                        1842-1844
      7  A Christmas Carol                        1843
      8  The Chimes                               1844
      9  The Cricket on the Hearth                1845
     10  The Battle of Life                       1846
     11  The Haunted Man and the Ghost's Bargain  1848
     12  Dombey and Son                           1848
     13  David Copperfield                        1850
     14  A Child's History of England             1851-1854
     15  Bleak House                              1853
     16  Hard Times                               1854
     17  Little Dorrit                            1857
     18  A Tale of Two Cities                     1859
     19  Great Expectations                       1861
     20  Our Mutual Friend                        1865
     21  No Thoroughfare                          1867
     22  The Mystery of Edwin Drood               1870

Referring to the table above, the program will then ask the user to choose one or more books they want to analyse by inserting their index numbers separated by a white space. The user can decide to analyse only one book, in this case, they will insert the corresponding index of the book. Alternatively, the user can decide to do a comparative analysis, in this case they can choose more books to be analysed at the same time by inserting their corresponding index numbers. In the example below the user chose to analyse book 1 and book 15, which are *The Pickwick Papers* and *Bleak House*:

    Choose the book (insert numbers separated by a whitespace) you want to compare: 
        1  15 

Afterwards, the program will print the list of the eight parameters:

    Index  Parameter
      1  N Highest Frequency
      2  N Highest Frequency Unique Content
      3  Mean Word
      4  Mean Sentence
      5  Sentence Length Standard
      6  Type/Token
      7  Filler/Token
      8  Lemma/Token

From these parameters, the user is then asked to choose which parameters they want to see for the chosen book(s). In the example below the user chose parameters number 1 (N Highest Frequency), 2 (N Highest Frequency Unique Content), 7 (Filler/Token), 8 (Lemma/Token):
   
    Choose the PARAMETER(/s) you want to visualize for the book(/s) chosen (insert numbers separated by a whitespace):
    1 2 7 8 

Depending on the number of books chosen, this process might take a few moments to complete. 
The user now has to choose the display mode of the data, in other words they have to decide whether they want the data to be shown in a tabulate form or in a graph, by inserting number 1 (tabulate) or 2 (graph). 

    How do you want the data to be shown?:
    1. Tabulate
    2. Graph
    [N.B. Parameter 1 and 2 can't be shown in visually in a graph]

It is important to note that parameters 1 and 2 can be shown only in a tabulate form, that means that the choice of the display mode is valid for all the parameters but the 1 and 2 parameters, which will be always displayed in a tabulate form. 

For both the parameters 1 and 2, the user is asked to choose the number of words they want to be shown. In the example, the user chose to see the 10 most frequent words:
    
    Values will be shown in a tabulate form
    What are the top N words that you want to be shown? (Insert a number)
    10 
    
The program will then print the reseults for both the two chosen books:

    The top 10 words of the book "The Pickwick Papers" are:
    [(18353, 'the'), (9934, 'and'), (8211, 'of'), (7500, 'a'), (7136, 'to'), (5747, 'mr'), (4817, 'in'), (4440, 'his'), (3861, 'i'), (3812, 'he')]

    The top 10 words of the book "Bleak House" are:
    [(14987, 'the'), (12748, 'and'), (10228, 'to'), (9487, 'i'), (8523, 'of'), (7728, 'a'), (6293, 'in'), (5470, 'it'), (5055, 'that'), (4657, 'he')]

Concerning the second parameters, the user chose to see the 10 most frequent content words:

    What are the top N content words that you want to be shown? (Insert a number)
    10 

Results: 

    The top 10 content words of the book "The Pickwick Papers" are:
    ['mr', 'said', 'pickwick', 'sir', 'sam', 'replied', 'weller', 'man', 'old', 'one']
    The top 10 content words of the book "Bleak House" are:
    ['mr', 'said', 'little', 'sir', 'one', 'know', 'would', 'says', 'upon', 'old']
    

For completeness purposes, we will see here how the results will look like if the user choose option number 1 Tabulate or option number 2 for the modes of visualization of the data. 

If the user answers with 1 to the previous question, all the parameters will be shown as a tabulate form:

    How do you want the data to be shown?:
    1. Tabulate
    2. Graph
    [N.B. Parameter 1 and 2 can't be shown in visually in a graph]
    1 
The output will be: 
    
                              Filler/Token    Lemma/Token
        -------------------  --------------  -------------
        The Pickwick Papers        0.489406    8.68916e-05
        Bleak House                0.541265    7.45156e-05
   
   Whereas, if the user chooses 2, all the parameters (besides paramters 1 and 2, which will be shown in the tabulate form as in the previous condition) will be shown in a graph
   
       How do you want the data to be shown?:
        1. Tabulate
        2. Graph
        [N.B. Parameter 1 and 2 can't be shown in visually in a graph]
        2

[![Click here to see the graph of parameters 7 and 8](C:\Users\sofia\Desktop\graph.png "Graph 1 2")](https://www.dropbox.com/s/lqatpyx6rzmjbn6/graph78.png?dl=0)

## Conclusion 
In conclusion, this project used text analysis to examine the writing style of Charles Dickens over time. By utilizing a system that allows for user input and the visualization of key parameters, we have gained a deeper understanding of how the author's style evolved. This project falls within the realm of stylometry, which has important applications in literary research.

## References 
- Can, Fazli & Patton, Jon. (2004). *Change of Writing Style with Time*. Computers and the Humanities. 38. 61-82. 10.1023/B:CHUM.0000009225.28847.77.

- Project Gutenberg. (n.d.). *Project Gutenberg*. Retrieved from http://www.gutenberg.org/

- Xuan Le, Ian Lancashire, Graeme Hirst, Regina Jokel, *Longitudinal detection of dementia through lexical and syntactic changes in writing: a case study of three British novelists*, Literary and Linguistic Computing, Volume 26, Issue 4, December 2011, Pages 435–461, https://doi.org/10.1093/llc/fqr013










 
  







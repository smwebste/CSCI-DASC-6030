# CSCI 4130 & CSCI/DASC 6030 Programming assignment 3
# This program implements the Vector Space Information
# Retrieval Model on the Cranfield Corpus
# Authors: Seymone Gugneja, Zachary Sherman-Burke,
# Justin Stempin, Sydney Webster

# Preliminaries: get imports
import sys
import os
import re
from nltk.stem import PorterStemmer

def readFile(filename):
    with open(filename, "r", encoding='mac_roman') as f:
        content = f.read()
    f.close()

    return content

# def normalizeTxt(data):
#     stemming = PorterStemmer()
#
#     lowerCasing = dirtyTxt.lower()
#     cleanPunct = re.sub('[^A-Za-z]+', ' ', lines)
#     tokens = lowerCasing.split()
#     #Tokenization
#     tokenList = word_tokenize(dirtyTxt)
#     # stemming the tokens
#     stemedList = [ps.stem(word) for word in tokenList]
# 
#     # converting list of tokens to string
#     tokenList = [word for word in tokenList if word.isalpha()]
#
#     # # removing tokens with one or two characters length
#     # clean_stem_tokens = shortword.sub('', clean_stem_tokens)
#     return tokenList




def writeFile(filename):
    pass

def main():

    # COMPLETE: get the directory through the command line
    print('Command line correct usage: python3 progAssg3.py <path-to-input-files>')

    corpusDir = ' '

    if len(sys.argv) == 2:
        corpusDir = sys.argv[1]
        print(f"The directory is {corpusDir}")
    else:
        sys.exit('Exiting now: Insufficient number of arguments.')

    # COMPLETE: Read files
    corpusArr = []
    arr = os.listdir(corpusDir)
    for i in arr:
        corpusArr.append(i)

    corpus = corpusDir+'/cran.all.1400'

    # TODO: build 2 zonal indexes (title and abstract).
    # use tf x idf weighting to construct

    titles = re.findall(r".T/n (.*)/n", readFile(corpus))
    abstracts = re.findall(r".A/n (.*)/n", readFile(corpus))
    # print(titles)
    # titlesList = []
    # for i in readFile(corpus):
    #     titlesList.append(titles)
    # print(titlesList)
    # for i in readFile(corpus):
    #     text =

    # TODO: develop simple UI to prompt user for query
    # and information need. allow for boost values

    # TODO: compute similarity of query with corpus documents

    # TODO: show titles of ranked documents that are relevant
    # to the query

    # TODO: design test cases and execute them. document
    # execution results, compare answers with expert-provided
    # answers

if __name__ == '__main__':
    main()

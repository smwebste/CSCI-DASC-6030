# CSCI 4130 & CSCI/DASC 6030 Programming assignment 3
# This program implements the Vector Space Information
# Retrieval Model on the Cranfield Corpus
# Authors: Seymone Gugneja, Zachary Sherman-Burke,
# Justin Stempin, Sydney Webster

# Preliminaries: get imports
import sys
import os

def main():

    # COMPLETE: get the directory through the command line
    print('Command line correct usage: python3 progAssg3.py <path-to-input-files>')

    corpusDir = ' '

    if len(sys.argv) == 2:
        corpusDir = sys.argv[1]
        print(f"The directory is {corpusDir}")
    else:
        sys.exit('Exiting now: Insufficient number of arguments.')

    # COMPLETE: read documents
    corpusArr = []
    arr = os.listdir(corpusDir)
    for i in arr:
        corpusArr.append(i)

    f = open(corpusDir+'/cran.all.1400', "r")
    print(f.read())

    # TODO: build 2 zonal indexes (title and abstract).
    # use tf x idf weighting to construct

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

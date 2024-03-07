import json, os, re, numpy, nltk
from nltk.corpus import stopwords
import openai


def main():
   
    stopWords = set(stopwords.words('english'))
    VOCAB = 'vocab.json'
    CORPUS = 'Man Loan Wong.txt'
    if os.path.exists(VOCAB):
        with open(VOCAB, 'r') as f:
            index = json.load(f)
    else:
        index = {}

    if os.path.exists(CORPUS):
        with open(CORPUS, 'r') as g:
            cleanWords = []
            for line in g:
                line = line.lower().split()
                cleanWords.extend(tokenize(line)) 
    else:
        cleanWords = tokenize(['dog', 'cat', 'animal', 'chair','table', 'furniture'])
    index = indexing(cleanWords, index, stopWords)

    with open(VOCAB, 'w') as f:
        json.dump(index, f)


def tokenize(inputs):
    cleanWords = []
    for word in inputs:
        if word.isalpha() == False:
            cleaning = re.sub('[^a-z]+', ' ', word).split()
            cleanWords.extend(cleaning)
        else:
            cleanWords.append(word)
    return cleanWords
    

def indexing(cleanWords, index=None, stopWords=None):
    if index == None:
        index = {}
    
    for word in set(cleanWords):
        if word not in index and word not in stopWords:
            index[word] = len(index)
    
    return index


if __name__ == '__main__':
    main()
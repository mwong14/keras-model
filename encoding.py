import numpy as np
from dictionary import tokenize
import json, os

def main ():
    with open('vocab.json', 'r') as f:
        index = json.load(f)

    cleanWords = tokenize(['dog', 'chair', 'cat', 'table', 'animal', 'furniture'])
    
    one_hot = one_hot_vector(cleanWords, index)
    print(one_hot)
    np.save('vectors.npy', one_hot)


def one_hot_vector (cleanWords, index):
    one_hot_vector = np.zeros((len(cleanWords), len(index)))

    for i, word in enumerate(cleanWords):
        if word in index:
            one_hot_vector[i][index[word]] = 1
    return one_hot_vector
        
if __name__ == "__main__":
    main()
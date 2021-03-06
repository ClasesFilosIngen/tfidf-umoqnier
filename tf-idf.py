#!/usr/bin/python3
from math import log
import os
from string import punctuation

# TODO: Documentar funciones
# TODO: Normalizar los documentos 

def remove_punctuation(string):
    """
    
    """
    return string.translate(string.maketrans('', '', punctuation))


def tf(term, doc):
    """
    term frecuency ajusted for document length. This function get a term to count
    how many times appear on document doc
    :param term: string to count frecuency at doc
    :param doc: document represent as list of strings
    """
    return doc.count(term) / len(doc)


def idf(term, docs):
    total_docs = len(docs)
    count = 0
    for doc in docs:
        if term in doc:
            count += 1
            continue
    return log(total_docs / (count + 1), 10)


def ccleaner_doc(text):
    data = text.split()
    return [remove_punctuation(word) for word in data]


def get_documents(folder):
    documents = []
    themes = []
    print(">>> Current documents <<<")
    for root, dirs, files in os.walk(folder):
        for name in files:
            print("\t->", name)
            themes.append(name[:-4])
            with open(os.path.join(root, name)) as f:
                data = f.read()
            documents.append(ccleaner_doc(data))
    return documents, themes


def main():
    results = {}
    documents, themes = get_documents("documents")
    print("Enter the word to be tf-idfizer")
    query = input("root@machine# ")
    for i, doc in enumerate(documents):
        results[themes[i]] = tf(query, doc) * idf(query, doc)
    print("Results >>", results)


if __name__ == "__main__":
    main()

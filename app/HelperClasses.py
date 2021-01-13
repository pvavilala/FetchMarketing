from abc import ABC, abstractmethod
from os import path
from stop_words import get_stop_words
import re

"""Class to hold the methods common to both similarity methods"""

stop_words = get_stop_words('english')

class DocumentSimilarityHelper(ABC):

    def __init__(self,doc1,doc2,*args,**kwargs):
        self._doc1 = doc1 #first document
        self._doc2 = doc2 #second document

        self._cosineSimilarity = None
        self._ngramSimilarity = None

        """eliminate all special characters except for period and comma"""

        self._regex = kwargs.get('regex', r'[^a-zA-Z0-9\'\,\.\s]')
        return

    def _prepDoc(self,doc):
        """remove stop words"""
        text = ""
        for word in doc.split():
            if word not in stop_words:
                text = text + " " + word
        return text

    def _removePunc(self,doc):
        """clean up punctuation except for , . and numbers"""
        doc = doc.lower()
        doc = re.sub(self._regex, ' ', doc)

        return doc


    def _similarityGenerator(self):
        """place holder method to be implemented in the similarity classes"""
        pass

    def _performCompare(self,simStyle):
        """
            arguments:
            simStyle - string indicating the type of comparision to perform
                cos - perform CosineSimilarity
                ngram - perform ngram similarity
        """
        doc1 = self._removePunc(self._doc1)
        doc1 = self._prepDoc(doc1)

        self._doc1 = doc1
        #print(self._doc1)
        doc2 = self._removePunc(self._doc2)
        doc2 = self._prepDoc(doc2)

        self._doc2 = doc2
        #print(self._doc2)

        if(simStyle == "cos"):
            self._cosineSimilarity = self._similarityGenerator()
            return(self._cosineSimilarity)

        if(simStyle == "ngram"):
            self._ngramSimilarity = self._similarityGenerator()
            return(self._ngramSimilarity)

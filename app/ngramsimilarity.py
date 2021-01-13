from HelperClasses import DocumentSimilarityHelper
import re
from collections import Counter
from math import sqrt

""" class which encapsualtes a very simple method to calculate ngram similarity"""
""" The document is transformed into ngrams and the ngram similarity is calculated based on these"""

class ngramSimilarity(DocumentSimilarityHelper):
    def __init__(self,doc1,doc2,ngramSize,**kwargs):
        """initialize the variables needed to calculate ngram similarity"""
        super().__init__(doc1, doc2, kwargs)
        self._ngramSize = ngramSize

    def _decomposeText(self,doc,nGramSize):
        """break down the text into ngrams"""
        traverseLength = len(doc) - nGramSize +1
        return [doc[i:i+nGramSize] for i in range(traverseLength)]

    def _calcNgramSimilarity(self,ngram1,ngram2):
        """get the intersection of the two ngrams"""
        ngramIntersection = [ngram for ngram in ngram1 if ngram in ngram2 ]
        #print("intersection Length",len(ngramIntersection),"ng1 len",len(ngram1))
        return float(len(ngramIntersection)/len(ngram1))


    def _similarityGenerator(self):

        """overloaded parent method for generating similarity"""
        ng1 = self._decomposeText(self._doc1,self._ngramSize)
        ng2 = self._decomposeText(self._doc2,self._ngramSize)

        return(self._calcNgramSimilarity(ng1,ng2))

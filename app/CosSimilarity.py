from HelperClasses import DocumentSimilarityHelper
import re
from collections import Counter
from math import sqrt

rexp = re.compile(r'\w+')

class cosSimilarity(DocumentSimilarityHelper):

    def __init__(self,doc1,doc2,*args,**kwargs):
        """initialize the variables needed to calculate cosine similarity"""
        super().__init__(doc1, doc2, kwargs)

    def _vectorizeDocs(self,doc):
        """create the Term Frequency vectors for the documents"""
        words = rexp.findall(doc)
        return Counter(words)

    def _calcCosineSimilarity(self,docVec1,docVec2):
        """calculate the cosine similarity
           cosine similarity is calculated as
           the dot product of the two document count vectors
           divided by the product of the  mean squares of the
           document count vectors"""

        """get the intersection of the two documents so that we can perform the similarity on the same words in the doc"""

        commonWords = set(docVec1.keys()).intersection(set(docVec2.keys()))

        """numerator in cosine similarity is the dot product of the term
               frequency vectors"""

        dProduct = sum(docVec1[i] * docVec2[i] for i in commonWords)

        sumSquaresVec1 = sum(docVec1[i] * docVec1[i] for i in commonWords)
        sumSquaresVec2 = sum(docVec2[i] * docVec2[i] for i in commonWords)

        denom = sqrt(sumSquaresVec1) * sqrt(sumSquaresVec2)

        print("sim" , float(dProduct)/denom)

        print("denom:" ,denom)

        if not denom:
            return 0.0
        else:
            return float(dProduct)/denom

    def _similarityGenerator(self):

        docVec1 = self._vectorizeDocs(self._doc1)
        print(docVec1)
        docVec2 = self._vectorizeDocs(self._doc2)
        print(docVec2)

        cosSim = self._calcCosineSimilarity(docVec1,docVec2)

        return cosSim

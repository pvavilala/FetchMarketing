from CosSimilarity import cosSimilarity
from ngramsimilarity import ngramSimilarity
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

""" the class to receive inputs, based on the FastAPI example code"""
class Input(BaseModel):
    doc1: str
    doc2: str
    simStyle: str
    ngramSize : Optional[int] = None


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"} #just for test


@app.post("/fetch/textsimilarity")
async def performTextSimilarityMeasure(docs:Input):
    """ for testing cosine similarity"""
    if docs.simStyle == "cos":
        return{'CosineSimilarity':cosSimilarity(docs.doc1,docs.doc2)._performCompare(docs.simStyle)}
    elif docs.simStyle == "ngram":
        return{'NGramSimilarity of doc1 with doc2':ngramSimilarity(docs.doc1,docs.doc2,docs.ngramSize)._performCompare(docs.simStyle)}

# FetchMarketing code test
Created a simple program to calculate text similarity. There are two similarity measures in the program, Cosine Similarity and Ngram Similarity.
The cosine similarity method converts the documents into a term frequency vector and calculates the cosine distance between the documents.
The Ngram method breaks the words in the document into ngrams of a specified size and then calculates a similarity measure based on how many common ngrams there are in the two documents.

The design considerations are listed below

**Do you count punctuation or only words?**

Inlcuded commas,periods and alpha numerics
  
**Which words should matter in the similarity comparison?**

  I used the stop-words library to eliminate all stop words.
  
**Do you care about the ordering of words?**

  For the cosine similarity method the order of the words does not matter since the document is converted into term frequency vectors and then evaluated. For the ngram method 
    the order matters because it affects the way the ngrams are created
    
**What metric do you use to assign a numerical value to the similarity?**

   For Cosine similarity the similarity is measured as the cosine angle derived from  dot product of the two document vectors. 
   For the Ngram method the similarity is the ratio of the common ngrams in the documents and the number of ngrams in the first document.
   
        
**What type of data structures should be used?**

mostly lists and list comprehension and the occasional set. Dictionary was used when the term frequency for the documents was calculated.

## Future improvements that can be made

both methods are pretty basic similarity measures and neither of them can account for sentiment. For the cosine similarity a more accurate similarity measure can be calculated if a td-idf method is used. The ngram method is restricted to only one direction (as in similarity of doc1 with respect to doc2 only).

## Running this program

pull down the repo and then

docker build -t fetchrewardsimage .
docker run -d --name fetchrewards -p 80:80 fetchrewardsimage

The image can be pulled from docker hub too

docker pull pvavilala/fetchrewards:version1
docker run -d --name fetchrewards -p 80:80 pvavilala/fetchrewardsimage:version1

I wasn't able to test on fastapi's gui at 192.168.99.100/docs because i was on Dockers for windows but it should work. I verified it on the local host at http://127.0.0.1/docs , in the gui api choose between "cos" and "ngram" for the simStyle field. The ngramSize of greater than 0 must be provided when trying to test the ngram similarity measure.

if you want use curl these are the commands to use

**For Cosine Similarity**

curl -X POST "http://127.0.0.1/fetch/textsimilarity" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"doc1\":\"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.\",\"doc2\":\"We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way.\",\"simStyle\":\"cos\",\"ngramSize\":0}"

**For ngram similarity**

curl -X POST "http://127.0.0.1/fetch/textsimilarity" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"doc1\":\"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.\",\"doc2\":\"We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way.\",\"simStyle\":\"ngram\",\"ngramSize\":2}"






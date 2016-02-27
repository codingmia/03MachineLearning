## Clustering and Similarity
* Task of retrieving documents of interest
** Currently reading article you like
** Goal: want to find similar article

* Question:
Measure similarity and Search over documents

# Bag of words model
* count # of instances of each word in vocabulary
* ignore order of words
* Get a very long sparse vector

# Similary:
Element wise product and add up
- Bias towards long article
- Normalize the sum - normalized count vector

# Issue with word count:
Common words dominate rare words

- upweight the rare words

#Tradeoff:
Local frequency v.s global rarity

# tf-idf
term frequency - inverse document frequency

term frequency: word count in the current article you are reading

idf: look at all docs in the corpus

idf = log( (# of doc) / 1 + (# of docs using the word))

then do vector product

# Search:
Scan over certain classifications. Will need to classify by clustering

# Cluster:
defined by center & shape/spread
- distance between this observation to different cluster centers

k means:
Similar metric = distance to cluster center

0. Initialize cluster centers
1. Assign observations to closest cluster center
2. Revise cluster centers as mean of assigned observations
3. Repeat step 1 and step 2 until convergence


# coding: utf-8

# # Document retrieval from wikipedia data

# ## Fire up GraphLab Create

# In[1]:

import graphlab


# # Load some text data - from wikipedia, pages on people

# In[2]:

people = graphlab.SFrame('people_wiki.gl/')


# Data contains:  link to wikipedia article, name of person, text of article.

# In[3]:

people.head()


# In[5]:

len(people)


# # Explore the dataset and checkout the text it contains
# 
# ## Exploring the entry for Elton John

# In[6]:

john = people[people['name'] == 'Elton John']


# In[7]:

john


# In[8]:

john['text']


# # Get the word counts for John article

# In[9]:

john['word_count'] = graphlab.text_analytics.count_words(john['text'])


# In[10]:

print john['word_count']


# ## Sort the word counts for the John article

# ### Turning dictonary of word counts into a table

# In[11]:

john_word_count_table = john[['word_count']].stack('word_count', new_column_name = ['word','count'])


# ### Sorting the word counts to show most common words at the top

# In[12]:

john_word_count_table.head()


# In[17]:

john_word_count_table.sort('count',ascending=False)


# Most common words include uninformative words like "the", "in", "and",...

# # Compute TF-IDF for the corpus 
# 
# To give more weight to informative words, we weigh them by their TF-IDF scores.

# In[18]:

people['word_count'] = graphlab.text_analytics.count_words(people['text'])
people.head()


# In[19]:

tfidf = graphlab.text_analytics.tf_idf(people['word_count'])

# Earlier versions of GraphLab Create returned an SFrame rather than a single SArray
# This notebook was created using Graphlab Create version 1.7.1
if graphlab.version <= '1.6.1':
    tfidf = tfidf['docs']

tfidf


# In[20]:

people['tfidf'] = tfidf


# ## Examine the TF-IDF for the John article

# In[21]:

john = people[people['name'] == 'Elton John']


# In[22]:

john[['tfidf']].stack('tfidf',new_column_name=['word','tfidf']).sort('tfidf',ascending=False)


# Words with highest TF-IDF are much more informative.

# # Manually compute distances between a few people
# 
# Let's manually compare the distances between the articles for a few famous people.  

# In[40]:

vbeckham = people[people['name'] == 'Victoria Beckham']
mcCartney = people[people['name'] == 'Paul McCartney']


# ## Is John closer to Beckham or McCartney?
# 
# We will use cosine distance, which is given by
# 
# (1-cosine_similarity) 
# 
# hint: smaller distance wins

# In[45]:

graphlab.distances.cosine(john['tfidf'][0],vbeckham['tfidf'][0])


# In[46]:

graphlab.distances.cosine(john['tfidf'][0],mcCartney['tfidf'][0])


# # Build a nearest neighbor model for document retrieval
# 
# We now create a nearest-neighbors model and apply it to document retrieval.  

# In[32]:

simple_knn_model = graphlab.nearest_neighbors.create(people,features=['word_count'],distance='cosine', label='name')
knn_model = graphlab.nearest_neighbors.create(people,features=['tfidf'],distance='cosine', label='name')


# In[33]:

simple_knn_model.query(john)


# # Applying the nearest-neighbors model for retrieval

# ## Who is closest to John?

# In[34]:

knn_model.query(john)


# As we can see, president Obama's article is closest to the one about his vice-president Biden, and those of other politicians.  

# ## Other examples of document retrieval

# In[43]:

simple_knn_model.query(vbeckham)


# In[44]:

knn_model.query(vbeckham)


# In[ ]:





# coding: utf-8

# In[4]:

import graphlab


# # Read product review data

# In[2]:

products = graphlab.SFrame('amazon_baby.gl/')


# #Explore data

# In[5]:

products.head()


# #Build the workd count vector

# In[6]:

# Add new columns
products['word_count'] = graphlab.text_analytics.count_words(products['review'])


# In[8]:

products.head()


# In[7]:

# show canvas inside the page
graphlab.canvas.set_target('ipynb')


# In[8]:

products['name'].show()


# #Explore the Best Seller (Vulli Sophie)

# In[9]:

giraffe_reviews = products[products['name'] == 'Vulli Sophie the Giraffe Teether']


# In[10]:

len(giraffe_reviews)


# #Build a sentiment classifier

# In[11]:

products['rating'].show(view='Categorical')


# # Define positive and negative sentiment

# ##Ignore rating 3

# In[12]:

products = products[products['rating'] != 3]


# In[13]:

# positive sentiment = 4 star or 5 star
products['sentiment'] = products['rating'] >= 4


# In[14]:

products.head()


# ## Train the sentiment classifier

# In[15]:

train_data, test_data = products.random_split(.8, seed = 0)


# In[16]:

sentiment_model = graphlab.logistic_classifier.create(train_data, 
                                                      target='sentiment',
                                                features = ['word_count'],
                                                     validation_set = test_data)


# In[18]:

sentiment_model.evaluate(test_data, metric='roc_curve')


# In[19]:

sentiment_model.show(view="Evaluation")


# ## Apply the learned model to Giraffe

# In[20]:

giraffe_reviews['predicted_sentiment'] = sentiment_model.predict(giraffe_reviews, output_type='probability')


# In[21]:

giraffe_reviews.head()


# ## Sort the reviews based on predicted sentiment

# In[22]:

giraffe_reviews = giraffe_reviews.sort('predicted_sentiment', ascending=False)


# In[23]:

giraffe_reviews.head()


# In[30]:

giraffe_reviews[0]['review']


# In[24]:

giraffe_reviews[1]['review']


# In[25]:

giraffe_reviews[-1]['review']


# In[26]:

giraffe_reviews[0]['word_count']['babies']


# In[47]:

def awesome_count(args):
    if 'awesome' in args:
        return args['awesome']
    else:
        return 0
    


# In[48]:

products['awesome'] = products['word_count'].apply(awesome_count)


# #Define multiple key_word_count functions

# In[49]:

def awesome_count(args):
    if 'awesome' in args:
        return args['awesome']
    else:
        return 0
def great_count(args):
    if 'great' in args:
        return args['great']
    else:
        return 0
def fantastic_count(args):
    if 'fantastic' in args:
        return args['fantastic']
    else:
        return 0
def amazing_count(args):
    if 'amazing' in args:
        return args['amazing']
    else:
        return 0
def love_count(args):
    if 'love' in args:
        return args['love']
    else:
        return 0
def horrible_count(args):
    if 'horrible' in args:
        return args['horrible']
    else:
        return 0
def bad_count(args):
    if 'bad' in args:
        return args['bad']
    else:
        return 0
def terrible_count(args):
    if 'terrible' in args:
        return args['terrible']
    else:
        return 0
def awful_count(args):
    if 'awful' in args:
        return args['awful']
    else:
        return 0
def wow_count(args):
    if 'wow' in args:
        return args['wow']
    else:
        return 0
def hate_count(args):
    if 'hate' in args:
        return args['hate']
    else:
        return 0


# In[50]:

products['awesome'] = products['word_count'].apply(awesome_count)
products['great'] = products['word_count'].apply(great_count)
products['fantastic'] = products['word_count'].apply(fantastic_count)
products['amazing'] = products['word_count'].apply(amazing_count)
products['love'] = products['word_count'].apply(love_count)
products['horrible'] = products['word_count'].apply(horrible_count)
products['bad'] = products['word_count'].apply(bad_count)
products['terrible'] = products['word_count'].apply(terrible_count)
products['awful'] = products['word_count'].apply(awful_count)
products['wow'] = products['word_count'].apply(wow_count)
products['hate'] = products['word_count'].apply(hate_count)


# # Sum up keyword column values

# In[54]:

selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']
for key in selected_words:
    print products[key].sum()


# # Train the data with selected words

# In[55]:

train_data,test_data = products.random_split(.8, seed=0)


# In[56]:

selected_words_model = graphlab.logistic_classifier.create(train_data, 
                                                      target='sentiment',
                                                features = selected_words,
                                                     validation_set = test_data)


# # Compare weight of selected words

# In[62]:

selected_words_model['coefficients'].print_rows(12)


# # Compare two models and their accuracies

# In[65]:

selected_words_model.evaluate(test_data)
selected_words_model.show(view="Evaluation")


# # Majority Class model based on occurence count

# In[66]:

majority_class_model = graphlab.logistic_classifier.create(train_data, 
                                                      target='sentiment',
                                                features = ['love'],
                                                     validation_set = test_data)


# In[67]:

majority_class_model.evaluate(test_data)


# # Gather reviews for diapers

# In[68]:

diaper_champ_reviews = products[products['name'] == 'Baby Trend Diaper Champ']


# # Predict with sentiment_model

# In[71]:

diaper_champ_reviews['predicted_sentiment'] = sentiment_model.predict(diaper_champ_reviews, output_type='probability')


# In[72]:

diaper_champ_reviews = diaper_champ_reviews.sort('predicted_sentiment', ascending=False)


# In[73]:

diaper_champ_reviews[0]['predicted_sentiment']


# # Predict with selected_words_model

# In[88]:

diaper_champ_reviews['predicted_sentiment'] = selected_words_model.predict(diaper_champ_reviews, output_type='probability')


# In[89]:

diaper_champ_reviews = diaper_champ_reviews.sort('predicted_sentiment', ascending=False)


# In[90]:

diaper_champ_reviews[0]['predicted_sentiment']


# In[83]:

diaper_champ_reviews['predicted_sentiment'] = selected_words_model.predict(diaper_champ_reviews, output_type='probability')


# In[80]:

diaper_champ_reviews[0]['predicted_sentiment']


# In[ ]:




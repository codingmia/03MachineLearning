
# coding: utf-8

# # Predicting house prices

# In[6]:

import graphlab


# ##Load some house sales data

# In[7]:

sales = graphlab.SFrame('home_data.gl/')


# In[8]:

# display sales
sales


# In[9]:

# Canvas visualize inside the page
graphlab.canvas.set_target('ipynb')
sales.show(view="Scatter Plot", x="sqft_living", y="price")


# ##Create a Regression Model of sqft_living to price

# In[10]:

# splitting data into training data and test data
train_data, test_data = sales.random_split(.8, 0)


# ##Build the regression model

# In[11]:

# train_data, target, features
sqft_model = graphlab.linear_regression.create(train_data, target='price', features=['sqft_living'])


# ## Evaluate the simple regression model

# In[25]:

print test_data['price'].mean()
# Evaluate the squarefoot_model with the test_data
print sqft_model.evaluate(test_data)


# ## Visualize our predictions

# In[12]:

import matplotlib.pyplot as plt
# makes the plot prints inside the page
get_ipython().magic(u'matplotlib inline')


# In[13]:

# x axis - sqft_living, y axis - price, scatter plot
# x asis - sqft_living, y axis - predicted price, linear single line
plt.plot(test_data['sqft_living'], test_data['price'], '.', test_data['sqft_living'], sqft_model.predict(test_data), '-')


# In[14]:

# weights
sqft_model.get('coefficients')


# ## Explore other features and Build another regression model

# In[15]:

my_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']
sales[my_features].show()
sales.show(view='BoxWhisker Plot', x='zipcode', y='price')
# Build a regression model with other features
my_features_model = graphlab.linear_regression.create(train_data,target='price',features=my_features)


# In[16]:

print my_features
# Compare the performance of different models
print sqft_model.evaluate(test_data)
print my_features_model.evaluate(test_data)
# Apply learned models to predict prices of 3 houses
house1 = sales[sales['id'] == '5309101200']
house1
print house1['price']
print sqft_model.predict(house1)
print my_features_model.predict(house1)


# # Assignment Tasks
# 
# ## Selection and summary statistics:
# Get the average price of houses whose zip code is 98039

# In[45]:

listHouses = sales[sales['zipcode']=='98039'] 
listHouses.show()


# In[44]:

listHouses['price'].mean()
    


# # Filter all houses (sales data) based on sqft

# In[27]:

sales.num_rows


# In[50]:

filterHouses = sales[(sales['sqft_living'] > 2000) & (sales['sqft_living'] <= 4000)]


# In[51]:

filterHouses.num_rows


# In[52]:

len(filterHouses)


# In[53]:

9118/21613


# In[ ]:




# ## Build original train set and test set with Seed 0

# In[34]:

train_data,test_data = sales.random_split(.8,seed=0)


# ## Square foot model

# In[36]:

sqft_model = graphlab.linear_regression.create(train_data, target='price', features=['sqft_living'],validation_set=None)


# ## Evaluate the model

# In[37]:

print test_data["price"].mean()


# In[ ]:

print sqft_model.evaluate(test_data)


# In[39]:

print sqft_model.evaluate(test_data)


# ## Build an Advanced features model

# In[1]:

print my_features_model.evaluate(test_data)


# In[55]:

advanced_features = [
'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode',
'condition', # condition of house				
'grade', # measure of quality of construction				
'waterfront', # waterfront property				
'view', # type of view				
'sqft_above', # square feet above ground				
'sqft_basement', # square feet in basement				
'yr_built', # the year built				
'yr_renovated', # the year renovated				
'lat', 'long', # the lat-long of the parcel				
'sqft_living15', # average sq.ft. of 15 nearest neighbors 				
'sqft_lot15', # average lot size of 15 nearest neighbors 
]


# In[56]:

adv_features_model = graphlab.linear_regression.create(train_data,target='price',features=advanced_features,validation_set=None)


# In[43]:

print adv_features_model.evaluate(test_data)


# In[17]:

print my_features_model.evaluate(test_data)


# In[ ]:




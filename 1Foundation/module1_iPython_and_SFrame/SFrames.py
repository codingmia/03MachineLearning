
# coding: utf-8

# #Fire up GraphLab Create
# 
# We always start with this line before using any part of GraphLab Create
# 
# - "esc + m" to enter the wiki page mode
# 
# - "shift + enter" to commit your commands 

# In[2]:

import graphlab


# #Load a tabular data set from disk 
# (The file does not have to fit in memory, hence supporting scalability)

# In[7]:

# find a people-example.csv in the same directory
sf = graphlab.SFrame('people-example.csv')


# #SFrame basics

# In[5]:

sf #we can view first few lines of table


# In[8]:

sf.tail()  # view end of the table, sf.head() show head of the table


# #GraphLab Canvas

# In[9]:

# .show() visualizes any data structure in GraphLab Create
sf.show()


# In[10]:

# If you want Canvas visualization to show up in this page
#(on this notebook), rather than popping up a new window, add this line:
graphlab.canvas.set_target('ipynb')


# In[11]:

sf['age'].show(view='Categorical')


# #Inspect columns of dataset

# In[12]:

sf['Country']


# In[13]:

sf['age']


# Some simple columnar operations

# In[14]:

sf['age'].mean()


# In[15]:

sf['age'].max()


# #Create new columns in our SFrame

# In[16]:

sf


# In[18]:

sf['Full Name'] = sf['First Name'] + ' ' + sf['Last Name']


# In[19]:

sf


# In[21]:

sf['age'] * sf['age']


# #Use the apply function to do a advance transformation of our data

# In[22]:

sf['Country']


# In[17]:

sf['Country'].show()


# In[24]:

def transform_country(country):
    if country == 'USA':
        return 'United States'
    else:
        return country


# In[25]:

transform_country('Brazil')


# In[26]:

transform_country('Brasil')


# # apply()

# In[1]:

# transform_country is our previously defined functions
sf['Country'].apply(transform_country)


# In[29]:

sf['Country'] = sf['Country'].apply(transform_country)


# In[30]:

sf


# In[ ]:




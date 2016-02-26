
# coding: utf-8

# #Installing Python and GraphLab Create

# Please follow the installation instructions here before getting started:
# 
# 
# ##We have done
# * Installed Python
# * Started Ipython Notebook

# #Getting started with Python

# In[1]:

print 'Hello World!'


# ##Create some variables in Python

# In[2]:

i = 4  #int


# In[3]:

type(i)


# In[4]:

f = 4.1  #float


# In[5]:

type(f)


# In[6]:

b = True  #boolean variable


# In[7]:

s = "This is a string!"


# In[8]:

print s


# ##Advanced python types

# In[9]:

l = [3,1,2]  #list


# In[10]:

print l


# In[11]:

d = {'foo':1, 'bar':2.3, 's':'my first dictionary'}  #dictionary


# In[12]:

print d


# In[13]:

print d['foo']  #element of a dictionary


# In[14]:

n = None  #Python's null type


# In[15]:

type(n)


# ##Advanced printing

# In[16]:

print "Our float value is %s. Our int value is %s." % (f,i)  #Python is pretty good with strings


# ##Conditional statements in python

# In[17]:

if i == 1 and f > 4:
    print "The value of i is 1 and f is greater than 4."
elif i > 4 or f > 4:
    print "i or f are both greater than 4."
else:
    print "both i and f are less than or equal to 4"


# ##Conditional loops

# In[18]:

print l


# In[19]:

for e in l:
    print e


# Note that in Python, we don't use {} or other markers to indicate the part of the loop that gets iterated.  Instead, we just indent and align each of the iterated statements with spaces or tabs. (You can use as many as you want, as long as the lines are aligned.)

# In[20]:

counter = 6
while counter < 10:
    print counter
    counter += 1


# #Creating functions in Python
# 
# Again, we don't use {}, but just indent the lines that are part of the function.

# In[21]:

def add2(x):
    y = x + 2
    return y


# In[22]:

i = 5


# In[23]:

add2(i)


# We can also define simple functions with lambdas:

# In[24]:

square = lambda x: x*x


# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits_tup = ("apple", "banana", "cherry")


# In[2]:


#1 
fruits_tup[0]


# In[3]:


#2
len(fruits_tup)


# In[4]:


#3
fruits_tup[-1]


# In[ ]:





# In[5]:


fruits_tup1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon",
"mango")


# In[6]:


#4
fruits_tup1[2:5]


# In[ ]:





# In[7]:


fruits_set = {"apple", "banana", "cherry"}


# In[8]:


#5
fruits_set.add("orange")


# In[9]:


fruits_set = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]


# In[10]:


#6
fruits_set.update(more_fruits)


# In[11]:


#7
fruits_set.remove('banana')


# In[12]:


#8
fruits_set = {"apple", "banana", "cherry"}
fruits_set.discard('banana')


# In[ ]:





# In[13]:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


# In[14]:


#9
car["model"]


# In[15]:


#10
car["year"] = 2020


# In[16]:


#11
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["color"] = "Red"


# In[17]:


#12
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car.pop("model")


# In[1]:


#13
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car.clear()


# In[ ]:


'''link to meduim post on collection data types in python
 = https://medium.com/@enoch-lamikanra/collection-data-types-in-python-3a3f9c0b554'''


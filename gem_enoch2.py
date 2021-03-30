#!/usr/bin/env python
# coding: utf-8

# """
# Write a python program that does this;
# It collects a user’s
# - name
# - age
# - sex
# 
# Prints out a welcome message like below.
# “Hi {user’s name}, you are welcome. In 10 years time, you will be {age in 10 years time} years old and very old by then.”
# 
# The python program then asks for 2 or more favorites fruits separated by comma and prints the result to a list.
# 
# The python program then asks for 2 or more favorite numbers separated by comma and prints the result to a sorted list in
# descending order.
# """

# In[1]:


name = input("Enter username ")
age = input("Enter age ")
age = int(age) + 10
sex = input("Enter sex ")

print("Hi {}, you are welcome, in 10 years time, you will be {} years " 
      "old and very old by then.".format(name, age))


# In[3]:


#The python program then asks for 2 or more favorites fruits separated by comma and prints the result to a list.
fav_fruits = input("Enter at least 2 favourite fruits, separated by a comma: ")
fruits_list = fav_fruits.split(",")

print(fruits_list)


# In[4]:


'''The python program then asks for 2 or more favorite numbers separated by comma and prints the result 
to a sorted list  in Descending order.'''
fav_no = input('Enter at least 2 favourite numbers separated by a comma ')
split_list = fav_no.split(',')

sorted_list = []
for i in split_list:
    sorted_list.append(int(i))
    sorted_list.sort(reverse=True)

print(sorted_list)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
i = 0 
while i <= 10:
    print (i)
    i += 1    


# In[2]:


#2
i = 1

while i <= 5:
    i += 1
    print (list(range(1, i)))


# In[ ]:


#3
#program that calculates sum of the range of numbers between 1 and user's inputted number
x = 1
def range_sum():
    y = int(input('Enter a random number: '))
    result = sum(range(x, y+1))
    return (result)    


# In[ ]:


range_sum()


# In[1]:


#4
def multiptab_n():
    input_no = int(input('Enter number to prepare multiplication table: '))
    for a in range(1, 13):
        result = input_no * a
        print(result)


# In[3]:


multiptab_n()


# In[ ]:


#5
def count_digits():
    digits = input('Enter any number: ')
    return len(digits)


# In[7]:


count_digits()


# In[8]:


#6
def divisible_by_5():
    list_no = input('Enter list of numbers e.g 5, 10, 24: ')
    list_no = [int(i) for i in list_no.split(',')]
    for no in list_no:
        if no > 150:
            break
        else:
            if no % 5 == 0:
                print(no)


# In[ ]:


divisible_by_5()


# In[ ]:


#7
def reverse_sort():
    numbers_list = input('Enter list of numbers e.g 5, 10, 24: ')
    numbers_list = [int(i) for i in numbers_list.split(',')]
    numbers_list.sort(reverse = True)
    print(numbers_list)


# In[ ]:


reverse_sort()


# In[ ]:


#8
def factorial():
    factorial = 1
    n = int(input('Enter any number: '))
    if n >= 1:
        for i in range(1, n+1):
            factorial = factorial * i
        print ('Factorial of {} is {}'.format(n, factorial))


# In[ ]:


factorial()


# In[ ]:


#9

def pattern():
    s = 0
    while s < 5:
        s += 1
        t = '*' 
        print (t * s)
    else:
        while s > 1:
            s -= 1
            print (t * s)


# In[ ]:


pattern()


# In[ ]:


#10
def calculation():
    var1 = int(input('Enter variable 1: '))
    var2 = int(input('Enter variable 2: '))
    return (var1 + var2, var1 - var2)


# In[ ]:


calculation()


# In[ ]:


#11
def showEmployee():
    name = input('Employee name: ')
    salary = input('Employee monthly salary: ')
    if len(salary) > 0:
        print ('Employee name is {} and has a monthly salary of {}'.format(name,salary))
    else:
        print ('Employee name is {} and has a monthly salary of 9000'.format(name))


# In[ ]:


showEmployee()


# In[ ]:


#12
def calc_area():
    diameter = input('Enter diameter of circle in m^2: ')
    if len(diameter) > 0:
        return (3.142 * int(diameter))
    else:
        radius = int(input('Enter radius of circle in m^2: '))
        return (3.142 * radius**2)


# In[ ]:


calc_area()


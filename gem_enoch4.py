#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input('Input name: ')
matric_no =  input('Input matric number: ')
dept = input('Name of department: ')
tot_units = float(input('Total number of units this semester? '))
no_courses = int(input('How many courses are you taking this semsester? '))
courses = input('Input main course codes e.g pol104, del309- ')
courses_list = courses.split(',')

tnu_total = 0
a = 0  

for x in (courses_list):
    b = courses_list[a]
    c = float(input('How many units is ' + b + ' '))
    a += 1
    
    score = int(input('Enter your score in course  ' + b + ' '))
    
    if 70 <= score < 100:
        score = 5
    elif 60 <= score < 70:
        score = 4
    elif 50 <= score < 60:
        score = 3
    elif 45 <= score < 50:
        score = 2
    elif 41 <= score < 45:
        score = 1
    elif  score < 40:
        score = 0
     
    tnu = score * c
    tnu_total = tnu_total + tnu
    
gpa = tnu_total / tot_units
gpa = round(gpa,2)

def grade_desc(gpa):
    if 4.5 <= gpa <= 5.0:
        return 'First Class Honors'
    elif 3.5 <= gpa < 4.5 :
        return 'Second Class Upper Division'
    elif 2.5 <= gpa < 3.5:
        return 'Second Class Lower Division'
    elif 1.5 <= gpa < 2.5:
        return 'Third Class'
    elif 1.0 <= gpa < 1.5:
        return 'Pass Degree'
    elif gpa < 1.0:
        return'Failure!!!'


def greetings(gpa):
    if 4.5 <= gpa <= 5.0:
        return 'Excellent job!'
    elif 3.5 <= gpa < 4.5 :
        return 'Very god job!'
    elif 2.5 <= gpa < 3.5:
        return 'Good job!'
    elif 1.5 <= gpa < 2.5:
        return 'Fair job'
    elif 1.0 <= gpa < 1.5:
        return ' Bad job!'
    elif gpa < 1.0:
        return 'Very bad job!'    
        

print ('{} At the end of this semester alone, {} with the matric number {},'
       ' from {} has a total grade of {} and is in {}.'.format(greetings(gpa), name, matric_no, dept, gpa, grade_desc(gpa)))


# In[ ]:





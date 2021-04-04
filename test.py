#!/usr/bin/env python
# coding: utf-8

# In[273]:


class Shape():
    def __init__(self, color, fill):
        self.color = color
        self.fill = fill
        
    def getColor(self):
        print('Color of shape is', self.color)
        
    def setColor(self, newColor):
        print('New color of shape is', newColor)
        
    def getFill(self):
        return self.fill
    
    def setFill(self, newFill):
        self.fill = newFill
        
    


# In[274]:


circle = Shape('blue', 'x')


# In[275]:


circle.getColor()


# In[272]:


circle.setColor('yellow')


# In[ ]:





# In[260]:


class Circle(Shape):
    def __init__(self, color, fill, radius, angle):
        self.radius = radius
        self.angle = angle
        super().__init__(color, fill)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def area(self):
        radius = self.radius
        return 3.142 * radius * radius


# In[261]:


circle_ = Circle('blue', 'x', 5.2, 360)


# In[262]:


circle_.area()


# In[ ]:





# In[ ]:





# In[263]:


class Rectangle(Shape):
    def __init__(self, color, fill, length, width, angle):
        self.length = length
        self.width = width
        self.angle = angle
        super().__init__(color, fill)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def area(self):
        length = self.length
        width = self.width
        print ('Area of rectangle is', length * width)


# In[264]:


rect = Rectangle('red', 'x', 2, 5, 360)


# In[265]:


rect.area()


# In[ ]:





# In[ ]:





# In[266]:


class Triangle(Shape):
    def __init__(self, color, fill, base, height, angle):
        self.base = base
        self.height = height
        super().__init__(color, fill)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def area(self):
        base = self.base
        height = self.height
        print ('Area of triangle is', 0.5 * base * height)


# In[267]:


tringle = Triangle('blue', 'x', 5, 7, 180)


# In[268]:


tringle.area()


# In[ ]:





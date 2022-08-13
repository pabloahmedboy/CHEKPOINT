#!/usr/bin/env python
# coding: utf-8

# In[10]:




class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def AHMED(self):
        return   (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)

print (my_point.AHMED())


# In[11]:


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())


# In[2]:


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# In[2]:


class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposit & Withdrawal Machine!")


#!/usr/bin/env python
# coding: utf-8

# In[12]:


#inheritance
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def printname(self):
        print(self.fname,self.lname)
        
        
class Student(Person):
    def disp(self):
        print('hello '+self.fname)
        
       
        
x=Student('Gayathri','Menon')    
x.printname()
x.disp()


# In[18]:


#polymorphism
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname       
    def disp(self):
        print(self.fname)
        
class Student :    
    def disp(self):
        print('hello student')
    
        
x=Person('Gayathri','Menon')
x.disp()
x=Student()
x.disp()


# In[21]:


#json
import json
my_dict={
    "name":"ram",
    "age":28
}
x=json.dumps(my_dict)
print(x)
print(type(x))

x='{"name":"ram","age":30}'
y=json.loads(x)
print(y)
print(type(y))


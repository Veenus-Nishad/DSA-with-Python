# Class is a description of an Object or A Common Noun
# Has two things properties i.e variable and methods i.e function together they are called attributes 
# Defining a class is creating a data type
# Syntax : class Class_Name: attributes
class Test:
  marks=5
  def calculate_rank():
    #some code
    grade="A"
    

# Object is a proper Noun 
# No new Keyword is used to create objects in python 
# Instance (Example) of a Class it is of two types
##### 1.Instance Object , initially empty 

t1=Test() # sirf aise () use karne se hi object banega

##### 2.Class Object , there can only be one class object
# Bina () ke Class ka naam use karna is creating reference of it
# ye class bante hi banjata hai

# What is encapsulation ? An act of combining properties and methods related to same object 
# Class is a way to implement Encapsulation

# Class Object variable vs Instance Object variable
# Jo Class Object ke under bane ho COV or static variable
# Jo Instance Obejct ke under Bane ho IOV impossible to be made directly inside class body  

# Ways to make instance method
#           __init__() method , takes atleast one argument compulsarily
# python mein "this" keyword nahi hota hai bananan padta hai 
# gets automatically called when you try to make instance object

class Test2:
  def __init__(self): # "self" keyword acts as "this" keyword
    self.a=5   # instance object variable
    self.b=6

t1=Test2() # immediately calls init() with t1 as argument
print(t1.a,t1.b)

class Test3:
  def __init__(self,a,b): 
    self.a=a  # a and b are local variable to init method
    self.b=b  # self.a is instance Object variables

x1=Test3(34,35)
x2=Test3(5,9)
print("x1 instance object are ",x1.a,x1.b,end="\n")
print("x2 instance object are ",x2.a,x2.b,end="\n")

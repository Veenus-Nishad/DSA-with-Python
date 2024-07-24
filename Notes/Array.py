#Disadvantage : Doesnot support some data types thats why we use numpy array
#             : is Growable
# TO use array we need to import array , * means everything 
from array import * 
# syntax : 
# my_array = array (type code , [elements])

my_array=array("i",[34,35,36])

print(my_array) # prints the above line only 

# to print elements 

print("My second elemen is ",my_array[2])

for x in my_array:
  print("h",x)

for x in range(3):
  print(my_array[x])

# Array Methods
#.append(element) : adds elements
#.count(element)  : array ke andar element kiti baar ara
#.extend(iterable_structure_var)        : add methods From an Iterable structure

elements_to_add=[23,34,45]

my_array.extend(elements_to_add)
print("elments after extend")
for x in my_array:
  print(x)

#.index(element)  : tell the first occurence of element
#.pop(index)    : delets elements from last if index not specified
#.remove(value)  : deletes the value specified
#.tolist()  : converts to list 

# Array vs Numpy Array
# Numpy array is of fixed length 
# Better suited for mathematical calculations
# pre-defined class similar to array
# list is a dynamic array : resizable
# can store heteregenous elements and of custom type also
# syntax : my_list=[elements or null]

my_list1=[1,2,3,"abc","x",3.14,False]

# List Methods
#.append(element) : adds elements
#.count(element)  : List ke andar element kiti baar ara
#.extend(iterable_structure_var)        : add elements From an Iterable structure
#.index(element)  : tell the first occurence of element
#.pop(index)    : delets elements from last if index not specified
#.remove(value)  : deletes the value specified
#.sort(key=None, reverse=False):

my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]

#.reverse() method in Python is used to reverse the order of elements in a list in-place. 
#does not create a new copy

original_list = [1, 2, 3, 4, 5]

# Reverse the list
original_list.reverse()
print(original_list)  # Output: [5, 4, 3, 2, 1]

# Original list is modified (demonstrates in-place modification)
print(original_list)  # Output: [5, 4, 3, 2, 1] (same as before)

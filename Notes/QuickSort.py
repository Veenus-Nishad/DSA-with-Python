# Divide and Conquer based on a pivot element
# ek array mein ek pivot choose karna generally pehla number then two sublist banana ek jisme pivot
# se saare chote aur ek jisme pivot se bade and repaeat until sorted and concatenate lists
arr=[5,8,1,2,6,3,9]

def quick_sort(arr):
  if len(arr)<=1:
    return arr
  else:
    pivot=arr[0]
    #list comprehension
    lesser=[x for x in arr[1:] if x<=pivot]
    greater=[x for x in arr[1:] if x>pivot]
    # recursive method
    return quick_sort(lesser)+[pivot]+quick_sort(greater)
  
mylist=quick_sort(arr)
print(mylist)
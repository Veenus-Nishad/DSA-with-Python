# Divide and Conquer based on a pivot element

arr=[5,8,1,2,6,3,9]

def quick_sort(arr,low,high):
  if low < high :
    pivot=partition(arr,low,high) # pivot ke left mein jitte honge vo usse small and right wale bade
    quick_sort(arr,low,pivot-1)
    quick_sort(arr,pivot+1,high)

def partition(arr,low,high):
  p=arr[low]
  i=low+1
  j=high
  while True:
    while i<=j and arr[i]<=p: # goes left to righ and looks for the element greater than pivot 
      i+=1
    while i<=j and arr[j]>=p: # goes right to left and looks for the element smaller than pivot
      j-=1
    if i<=j: #swapping takes place here
      arr[i],arr[j]=arr[j],arr[i]
    else:
      break
    arr[low],arr[j]=arr[j],arr[low]
    return j
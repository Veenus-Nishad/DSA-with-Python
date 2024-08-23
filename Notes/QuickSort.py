def partition(arr,low,high):
  pivot=arr[low]
  i=low
  j=high
  while i<j:
    while arr[i] <= pivot and i<= high-1:
      i+=1
    while arr[j]>pivot and j>=low+1:
      j-=1
    if i<j:
      arr[i],arr[j]=arr[j],arr[i]
  arr[low],arr[j]=arr[j],arr[low]
  return j 

def QuickSort(arr,low,high):
  if low<high:
    partitionIndex=partition(arr,low,high)
    QuickSort(arr,low,partitionIndex-1)
    QuickSort(arr,partitionIndex+1,high)


def main():
 Array=[13,46,24,52,20,9]
 n=6
 QuickSort(Array,0,n-1)
 print(Array)
if __name__ == "__main__":
  main()
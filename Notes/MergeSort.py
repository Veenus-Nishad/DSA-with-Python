# time complexity for all the three cases is O(N*logN)

def Merge(arr,low,mid,high):
  left=low
  right=mid+1
  tempArray=[]
  while left<=mid and right<=high:
    if arr[left]<=arr[right]:
      tempArray.append(arr[left])
      left+=1
    else:
      tempArray.append(arr[right])
      right+=1
  while left<=mid:
     tempArray.append(arr[left])
     left+=1
  while right<=high:
    tempArray.append(arr[right])
    right+=1
  for i in range(low,high+1):
    arr[i]=tempArray[i-low]
    

def MergeSort(arr,low,high):
  if low < high :
    mid =(low + high)//2
    MergeSort(arr,low,mid)
    MergeSort(arr,mid+1,high)
    Merge(arr,low,mid,high)
 
  



def main():
 Array=[13,46,24,52,20,9]
 n=6
 MergeSort(Array,0,n-1)
 print(Array)

if __name__ == "__main__":
  main()
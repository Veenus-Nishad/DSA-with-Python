def RecurisveInsertionSort(arr,n,i):
    if i>n-1:
      return
    j=i
    while j>0 and arr[j-1]>arr[j]:
      arr[j-1],arr[j]=arr[j],arr[j-1]
      j-=1
    RecurisveInsertionSort(arr,n,i+1)
    



def main():
 Array=[13,46,24,52,20,9]
 RecurisveInsertionSort(Array,6,0)
 print(Array)

if __name__ == "__main__":
  main()
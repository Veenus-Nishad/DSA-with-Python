def RecursiveBubbleSort(arr,s,n):
  if n==1:
    return arr
  isSwapped=0
  while s<n:
    for i in range(n-1):
      if arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
        isSwapped+=1
    if isSwapped==0:
        break
    n-=1
    RecursiveBubbleSort(arr,s,n)


def main():
 Array=[13,46,24,52,20,9]
 n=6
 RecursiveBubbleSort(Array,0,6)
 print(Array)

if __name__ == "__main__":
  main()

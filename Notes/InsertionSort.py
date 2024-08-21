 # best complexity is O(N)

def InsertionSort(arr,n):
  for i in range(n):
    j=i
    while j>0 and arr[j-1]>arr[j]:
      arr[j-1],arr[j]=arr[j],arr[j-1]
      j-=1
  return arr
 
def main():
 Array=[13,46,24,52,20,9]
 n=6
 print(InsertionSort(Array,n))

if __name__ == "__main__":
  main()
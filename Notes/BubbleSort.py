
def BubbleSort(arr,n):
  for i in range(n):
    didSwap=0  # due to this  best complexity is O(N) otherwise O(N^2) as what if the array is sorted
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
    if didSwap==0:
      break
  return arr

def main():
 Array=[13,46,24,52,20,9]
 n=6
 print(BubbleSort(Array,n))

if __name__ == "__main__":
  main()

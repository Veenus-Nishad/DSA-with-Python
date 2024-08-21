
def SelectionSort(arr,n):
  for i in range(n-1):
    mini=i
    for j in range(i,n):
      mini=j
    arr[i],arr[mini]=arr[mini],arr[i]
  return arr

def main():
 Array=[13,46,24,52,20,9]
 n=6
 print(SelectionSort(Array,n))

if __name__ == "__main__":
  main()
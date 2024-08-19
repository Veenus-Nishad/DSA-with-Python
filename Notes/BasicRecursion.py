# Print Name N times
def printNTimes(i,n):
  if i>n : return 
  print("Poonam")
  printNTimes(i+1,n) #recursive function call

#Print from N to 1 ( by backtracking) and dont use " i-1 "
def printNtoOne(i,n):
  if i>n: return
  printNtoOne(i+1,n)
  print(i)


def main():
  n=int(input("Enter the No. of Times You want to print the Name: "))
 #
 #  printNTimes(1,n)
  printNtoOne(1,n)

if __name__ == "__main__":
  main()
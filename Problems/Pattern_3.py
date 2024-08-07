"""
  *  
 ***
***** 
*****  
 ***
  *   
"""

def printupper(n:int):
  for i in range(n):
    for j in range(n-i-1):
      print(" ",end="")
    for j in range(2*i+1):
      print("*",end="")
    for j in range(n-1-i):
      print(" ",end="")
    print("")

def printlower(n:int):
  for i in range(n):
    for j in range(i):
      print(" ",end="")
    for j in range(2*n-2*i-1):
      print("*",end="")
    for j in range(i): 
      print(" ",end="")
    print("")

def printpattern(n:int):
  n=n//2
  printupper(n)
  printlower(n)


def main():
  rows = int(input("Enter no of rows: "))
  printpattern(rows)

if __name__ == "__main__":
  main()
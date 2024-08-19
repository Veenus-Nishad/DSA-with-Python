# SUM OF N NUMBERS
#parameterized Recursion
def parameterizedRecursion(i,sum):
  if i<1:
    print(sum)
    return 
  parameterizedRecursion(i-1,sum+i)

#functional Recursion
def functionalRecursion(n):
  if(n==0):
    return 0
  return n + functionalRecursion(n-1)

#Factorial Of N
def Factorial(n):
  if n==0:return 1
  return n*Factorial(n-1)

#Reverse An Array Using Recurion with Two Pointers
def Reverse(Arr,l,r):
  if l>=r:
    return Arr
  Arr[l],Arr[r]=Arr[r],Arr[l]
  return  Reverse(Arr,l+1,r-1)

#Check For Palindrome
def Palindrome(str,l):
  if l>=len(str)/2:
    return True
  if str[l]!=str[len(str)-l-1]:
    return False
  return Palindrome(str,l+1)

#Fibonacci series
def Fibonacci(n):
  if n<=1:return n
  return Fibonacci(n-1)+Fibonacci(n-2)
def main():
  parameterizedRecursion(5,0) 
  print(functionalRecursion(6))
  print(Factorial(5))
  Arr=[1,2,3,4,5]
  print(Reverse(Arr,0,len(Arr)-1))
  str="MADAM"
  print(Palindrome(str,0))
  n=6
  print(Fibonacci(n))
if __name__ == "__main__":
  main()
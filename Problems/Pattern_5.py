"""
1          1
12        21
123      321
1234    4321
12345  54321
123456654321
"""
n=6
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end="")
  for x in range(2*(n-i)):
    print(" ",end="")
  for y in range(i,0,-1):
    print(y,end="")
  print("")
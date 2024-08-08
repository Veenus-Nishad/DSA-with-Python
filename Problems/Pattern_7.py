"""
*    *
**  **
******
**  **
*    *
"""

flipfrom=3
for i in range(1,2*flipfrom):
  stars=i
  if i>flipfrom:stars=2*flipfrom-i
  for j in range(stars):
    print("*",end="")
  for j in range(abs(2*(flipfrom-i))):
    print(" ",end="")
  for j in range(stars):
    print("*",end="")
  print("")
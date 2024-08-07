"""
*
**
*** 
****
*****
******  
*****
****
***    
**
*
"""

flipfrom=6
for i in range(1,2*flipfrom-1+1):
  stars=i
  if i>flipfrom:
    stars=2*flipfrom-i
  for j in range(stars):
    print("*",end="")
  print("")
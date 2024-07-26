from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        ans=[]
        for x in range(n):
            index=arr[x]%n
            arr[index]+=n
        for x in range(n):
            if arr[x]//n >=2:
                ans.append(x)# kyunki element ko as index refer kar rahe hai isliye x add kiya
        if not ans:
            return [-1]
        
        return ans
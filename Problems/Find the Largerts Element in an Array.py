# Brute force is sort array and tell the last index tc->O(nlogn)
# Optimal is Use a temp variable to compare and swap the greater Number tc->O(N)
from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        if len(arr)==0:
            return 
        if len(arr)==1:
            return arr[0]
        largestEle=arr[0]
        for i in range(len(arr)):
            if arr[i]>largestEle:
                largestEle=arr[i]
        return largestEle
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.largest(arr)

        print(res)

# } Driver Code Ends
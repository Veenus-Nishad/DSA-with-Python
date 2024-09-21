# Optimal -> use kadane's algorithm which says we carry a subarray sum as long it gives 
# positive suum  initialize sum=0 and max=a[0] then iterate over the loop with a
# pointer and update sum and use max function to maximize
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=-sys.maxsize
        for i in nums:
            sum+=i
            maxi=max(sum,maxi)
            if sum<0 : sum=0
        return maxi


       

        
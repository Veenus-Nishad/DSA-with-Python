class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #used Kaden's Algorithm
        #if subpart gives negative array we discard it,
        currSum=maxSum=nums[0]
       
        for x in range(1,len(nums)):
            currSum=max(nums[x],currSum+nums[x])
            #   if all elements are negative, the algorithm still works because currSum will
            #   be updated to the maximum of a single element in each iteration, 
            #   and maxSum will correctly retain the maximum value encountered.
            maxSum=max(maxSum,currSum)
        return maxSum

        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp=[None]*len(nums) # creating empty array so that values are not overwritten by logic
        for x in range(len(nums)):
            newIndex=(k+x)%len(nums)
            temp[newIndex]=nums[x]
        nums[:]=temp[:]
        
        """
        Do not return anything, modify nums in-place instead.
        """
        
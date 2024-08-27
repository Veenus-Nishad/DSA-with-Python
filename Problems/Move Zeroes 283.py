# Move all the zeroes to the end 
# Brute force -> Iterate the array store all the non negatives in temp[] and assign it back to arr and assign 
#                 remaining index zero 
# T.C=> O(2N) , S.C->O(N)

# Optimal ->  two pointer approach a pointer at the first zero (say j) and a pointer one ahead of it (say i)
#   now start iterating and whenever i is at not zero swap with j which should always be at zero 
# T.C => O(N) with no extra space


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                j=i
                break
        
        if j==-1:return 
        
        for i in range(j+1,n):
            if nums[i]!=0:
                    nums[j],nums[i]=nums[i],nums[j]
                    i+=1
                    j+=1
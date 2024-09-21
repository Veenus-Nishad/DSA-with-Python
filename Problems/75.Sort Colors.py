# Brute force -> Use merge Sort
# Better -> count 1's 0's and 2's and reinitialize array or return new array
#           T.C => O(2N)
# Optimal -> Dutch National Flag Algo 
#            we take three pointers low , mid , high 
#            fill 0's in 0 to low-1 
#            fill 1's in low to mid -1
#            random numbers unsorted in mid to high
#            fill 2's in high+1 to n-1
# the question we get lies in the mid to high part

class Solution:
    def sortColors(self, nums: List[int]) -> None:
      low=0
      high=len(nums)-1
      mid=0
      while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[high],nums[mid]=nums[mid],nums[high]
            high-=1

       
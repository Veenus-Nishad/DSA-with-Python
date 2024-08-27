# Brute Force -> We can take another dummy array of the same length and then shift all elements in the array
#  toward the left and then at the last element store the index of 0th index of the array and print it.
# T.C -> O(N) and S.C -> O(N)

#Opitmal -> Reverse the array and then reverse it till 0 to k-1 and k+1 to n-1
# T.C -> O(N) and S.C -> O(1) 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=len(nums)
        def reverse(arr,startIndex,endIndex):
            while startIndex<endIndex:
                temp=nums[startIndex]
                nums[startIndex]=nums[endIndex]
                nums[endIndex]=temp
                startIndex+=1
                endIndex-=1
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)

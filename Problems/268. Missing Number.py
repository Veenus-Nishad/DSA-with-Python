# optimal solution 1 -> through sum but if the numbers are to greay we will not be able to store the sum in int

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=(n*(n+1))/2
        sum1=0
        for i in range(n):
            sum1+=nums[i]
        return int(sum-sum1)

#optimal solution 2 -> using xor as 1^1 = 0 otherwise 1 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1,xor2=0,0
        n=len(nums)
        for i in range(n):
            xor2=xor2^nums[i]
            xor1=xor1^i
        xor2=xor2^n
        return xor1 ^ xor2

        
        
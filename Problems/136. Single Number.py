# Better -> to use hashing but we need to find the max element in the array first so that you can define your hash array
#           then iterate in nums and do hash[nums]++ then another loop to find out the hash with value 1
#           and you also cant use hash for negatives and very large numbers
# T.C -> O(3N) 

# Opitmal -> use xor , O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for num in nums:
            xor=xor ^ num
        return xor
        
# Brute -> generate all sub array using two nested loops and calc summation of numbers inside sub array ( check strivers video ) 
#           then check if sum=k and return the longest lenght of the array 
# T.C -> O(N^2)

# IF THE ARRAY CONTAINS NEGATIVE THIS IS THE OPTIMAL 
#Better -> Hashing so  for genreating the sub array i will put a pointer anywhere on the array and then calc the sum of element say X
#       that is my prefix sum now if there exist a sub array with sum K in the generated arrays (assuming that we are getting the subarray)
#       with sum k by fixing the random element pointer as the last element of the subarray we are generating ) then if we iterate from
#       the front then we say the sum we will be getting is K-X 
#       now use hash map and key will be the sum and value will be the last index of sub array now from i =0 to n making subarrays and 
#       checking if we are getting sub array with sum k and compare with hashmap if there exist some subarray whose length is greater
# T.C -> O(N^2)

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        
        preSumMap = {}
        Sum = 0
        maxLen = 0

        # Handle empty array or target sum of 0
        if n == 0 or k == 0:
            return 0

        for i in range(n):
            Sum += arr[i]

            if Sum == k:
                maxLen = max(maxLen, i + 1)

            rem = Sum - k
            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxLen = max(maxLen, length)

            if Sum not in preSumMap:
                preSumMap[Sum] = i

        return maxLen
for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))

# Optimal -> The steps are as follows:

#First, we will take two pointers: left and right, initially pointing to the index 0.
#The sum is set to a[0] i.e. the first element initially.
#Now we will run a while loop until the right pointer crosses the last index i.e. n-1.
#Inside the loop, we will do the following:
#We will use another while loop and it will run until the sum is lesser or equal to k.
#Inside this second loop, from the sum, we will subtract the element that is pointed by the left pointer and increase the left pointer by 1.
#After this loop gets completed, we will check if the sum is equal to k. If it is, we will compare the length of the current subarray i.e. (right-left+1) with the existing one and consider the maximum one.
#Then we will move forward the right pointer by 1. If the right pointer is pointing to a valid index(< n) after the increment, we will add the element i.e. a[right] to the sum.
#Finally, we will return the maximum length




from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]

    return maxLen


if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")







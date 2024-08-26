# Brute -> use a set to idenitfy the uniques ele then place them in array
# and return the index when there is no item left in set
# T.C => nlogn for insertion in set and n for the second step i.e O(NlogN+N) 
# S.C => O(N)

# Optimal -> USE A TWO POINTER APPROACH AND RETURN K 
# T.C => O(n)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        k=1
        while k<len(nums)-1:
            while nums[i]==nums[k]:
                k+=1
            if nums[i]!=nums[k]:
                nums[i+1]=nums[k]
                i=k
                k+=1
        return i+1
        

        


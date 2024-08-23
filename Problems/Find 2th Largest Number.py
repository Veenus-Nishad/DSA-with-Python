class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
# Convert to int array using list comprehension
        int_array = [int(x) for x in nums]
# Sorting the Array in reverse order so that kth largest can be fetched directly
        int_array.sort(reverse=True)
# Conerting int array to string array
        str_array=[str(x) for x in int_array]
        return str_array[k-1]

        
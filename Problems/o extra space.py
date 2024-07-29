class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for x in range(m,m+n):
            nums1.pop(m) # Pop the zeros that should ignored 
        nums1+=nums2
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
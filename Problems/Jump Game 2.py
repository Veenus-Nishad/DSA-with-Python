class Solution:
    def jump(self, nums: List[int]) -> int:
        totalJumps=0
        #last index
        destination=len(nums)-1
        coverage,lastJumpIdx=0,0
        #base case
        if len(nums)==1:
            return 0
        #Greedy Strategy : extend coverage as much as possible
        for x in range(len(nums)):
            coverage=max(coverage,x+nums[x])
            if x==lastJumpIdx: # to ensure whole window is visited 
                lastJumpIdx=coverage
                totalJumps+=1
                # check if we reached destiantion already
                if coverage>=destination:
                    return totalJumps
        return totalJumps

        
class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        ans=arr[n-1]-arr[0]
        # calculate smallest and largest after change 
        smallest=arr[0]+k
        largest=arr[n-1]-k
        maxi,mini=None,None
        for x in range(n-1):
            # as the best option to get the min difference is changes in consecutive elements
            mini=min(smallest,arr[x+1]-k)
            maxi=max(largest,arr[x]+k)
            if mini<0:
                continue
            ans=min(ans,maxi-mini)
        return ans

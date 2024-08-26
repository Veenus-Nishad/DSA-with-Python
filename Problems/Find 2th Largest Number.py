# Brute Force -> Sort the Array and then iterate from n-2th index to find the  2th 
# largest element ,
# TC=> O(n + nlogn)

# better ->  find the largest , take a second var secondlargest= -1 or int min check 
# arr[i] > second largest and < largest if yes swapp 
# T.C -> O(2N)

# Optimal solution take two var s largest and largest  
# T.C =>O(N)

#User function Template for python3
class Solution:
    def print2largest(self, arr):
        largest=arr[0]
        slargest=-sys.maxsize
        for i in range(1,len(arr)):
            if arr[i]>largest:
                slargest=largest
                largest=arr[i]
            if arr[i]>slargest and arr[i]<largest:
                slargest=arr[i]
        return slargest
                
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends
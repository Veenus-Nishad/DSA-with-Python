# Given a number n. Count the number of digits in n which evenly divide n. 
# Return an integer, total number of digits of n which divides n evenly.



class Solution:
    def evenlyDivides (self, N):
        count=0
        x=N
        while x>0:
            c=x%10
            if c!=0 :
                if N%c==0:
                    count+=1
            x=x//10
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends
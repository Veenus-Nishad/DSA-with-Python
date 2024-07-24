class Solution(object):
    def reverseString(self, s):  
        if len(s)>=1 and len(s)<=pow(10,5): #boundary check
            for i in range(len(s)):
                if i<(len(s)/2): # main coindition
                    temp=s[i]
                    s[i]=s[len(s)-1-i]
                    s[len(s)-1-i]=temp
             

# Better approach Two pointer method
     
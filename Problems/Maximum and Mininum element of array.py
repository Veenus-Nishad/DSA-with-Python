import sys
class Solution:
    def get_min_max(self, arr):
        setmaxi=-sys.maxsize-1
        setmini=sys.maxsize
        if len(arr)==1 :
            return [arr[0],arr[0]]
        else:
            for i in range(len(arr)):
                if(arr[i]>setmaxi):
                    setmaxi=arr[i]
                if(arr[i]<setmini):
                    setmini=arr[i]
                
            return [setmini,setmaxi]

class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        c=0
        for i in arr:
            if i[:k]==s[:k] and len(i)>=k:
                c+=1
        return c

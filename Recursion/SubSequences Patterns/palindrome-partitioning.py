class Solution:
    def isPalindrome(self,s,start,end):
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    def func(self,ind,s,path,res):
        if ind==len(s):
            res.append(path[:])
            return 
        for i in range(ind,len(s)):
            if self.isPalindrome(s,ind,i):
                path.append(s[ind:i+1])
                self.func(i+1,s,path,res)
                path.pop()
    def partition(self, s: str):
        #your code goes here
        res=[]
        path=[]
        self.func(0,s,path,res)
        return res

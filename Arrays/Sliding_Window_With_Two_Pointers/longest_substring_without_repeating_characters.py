
#Using brute force
for(i=0;i<n;i++)
{
  hash[256]={0}
  for(j=i;j<n;j++)
  {
    if(hash[s[j])==1) break
    len=j-i+1
    maxlen=max(len,maxlen)
    hash[s[j]]=1
  }
}

print(maxlen)



#Optimal Using Sliding Window with two pointers
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        HashLen=256
        hash=[-1]*HashLen
        l=0
        r=0
        maxlen=0
        while r<n:
            """ If current character s[r] 
                is already in the substring """
            if hash[ord(s[r])] != -1:
                """ Move left pointer to the right
                    of the last occurrence of s[r] """
                l=max(hash[ord(s[r])]+1,l)
            # Calculate the current substring length
            curr_len=r-l+1
            maxlen=max(curr_len,maxlen)
            """ Store the index of the current
                character in the hash table """
            hash[ord(s[r])]=r
            r+=1
        return maxlen    

        

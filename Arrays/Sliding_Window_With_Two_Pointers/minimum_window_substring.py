# Brute

## Generate all substrings and find the occurences of t in string s using hashmap

# Optimal (Using Sliding Window with two pointers)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen=float('inf')
        start_idx=0
        hash_arr=[0]*128
        cnt=0
        l=0
        r=0
        for ch in t:
            hash_arr[ord(ch)]+=1
        
        while r<len(s):
            ch=s[r]
            if hash_arr[ord(ch)]>0:
                cnt+=1
            hash_arr[ord(ch)]-=1
            # Shrink window when we have all required characters
            while cnt==len(t):
                if r-l+1<minlen:
                    minlen=r-l+1
                    start_idx=l
                hash_arr[ord(s[l])]+=1
                if hash_arr[ord(s[l])]>0:
                    cnt-=1
                l+=1
            r+=1

            # Step 4: Return result
        if minlen == float('inf'):
            return ""
        return s[start_idx:start_idx +minlen]
        
        


        

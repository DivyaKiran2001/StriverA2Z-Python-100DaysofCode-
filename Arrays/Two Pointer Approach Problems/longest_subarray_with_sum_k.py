



#Maximum length of Longest Subarray With Sum K Using Two pointer approach

#Brute
## Store all subarrays with Sum K and return the subarray which has maximum length

#Optimal
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    n=len(a)
    l=0
    r=0
    sum=0
    maxlen=0
    while r<n:
        sum=sum+a[r]
        while sum>k:
            sum=sum-a[l]
            l=l+1
        if sum==k:
            # print("yes")
            print("before",maxlen)
            maxlen=max(maxlen,r-l+1)
            print("after",maxlen)
        r=r+1
    return maxlen

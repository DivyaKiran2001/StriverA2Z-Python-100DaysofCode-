	# Print the Longest Subarrays With Sum K Using Two pointer approach 
	def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    n=len(a)
    l=0
    r=0
    sum=0
    maxlen=0
    sub_arr=[]
    while r<n:
        sum=sum+a[r]
        while sum>k:
            sum=sum-a[l]
            l=l+1
        if sum==k:
            # print("yes")
            print("before",maxlen)
            maxlen=max(maxlen,r-l+1)
            st=l
            en=r
            print(st,en)
            lis=[]
            for i in range(st,en+1):
                lis.append(a[i])
            sub_arr.append(lis)
            print("after",maxlen)
        r=r+1
    print(sub_arr)
    return maxlen

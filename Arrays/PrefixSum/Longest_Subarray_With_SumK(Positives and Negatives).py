# Longest Subarray with Sum K

# Brute
### Generate all subarrays and find the subarray with sum K

# Better and Optimal - Using the concept of Prefix sum

## Prefix sum at index i = sum of elements from index 0 to i

class Solution:
    def longestSubarray(self, nums, k):
        n=len(nums)
        pre_sum_map={}
        sum_so_far=0
        max_length=0
        for i in range(n):
            sum_so_far+=nums[i]
            # Case 1: Entire subarray from index 0 to i has sum = k
            if sum_so_far==k:
                max_length=i+1
            # Case 2: If (sum_so_far - k) exists in map, we found a valid subarray
            rem = sum_so_far-k
            if rem in pre_sum_map:
                length=i-pre_sum_map[rem]
                max_length=max(max_length,length)
            
            # Store the first occurrence of the current prefix sum
            if sum_so_far not in pre_sum_map:
                pre_sum_map[sum_so_far]=i
        return max_length

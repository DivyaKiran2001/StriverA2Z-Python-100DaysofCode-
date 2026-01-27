class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        pre_sum_map = {}
        sum_so_far = 0
        max_length = 0
        sub_arrays = []

        for i in range(n):
            sum_so_far += nums[i]

            # Case 1: subarray from index 0
            if sum_so_far == k:
                sub_arrays.append(nums[0:i+1])
                max_length = i + 1

            # Case 2: subarray ending at i
            rem = sum_so_far - k
            if rem in pre_sum_map:
                start = pre_sum_map[rem]
                sub_arrays.append(nums[start + 1 : i + 1])
                max_length = max(max_length, i - start)

            # store first occurrence
            if sum_so_far not in pre_sum_map:
                pre_sum_map[sum_so_far] = i

        print("All subarrays with sum =", k)
        for arr in sub_arrays:
            print(arr)

        return max_length

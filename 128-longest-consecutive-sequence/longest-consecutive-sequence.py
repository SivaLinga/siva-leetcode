class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums.sort()
        max_count = 1
        curr_count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: continue
            if nums[i] - nums[i-1] == 1:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 1
        return max(max_count, curr_count)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        start, end = 0, len(sorted_nums) - 1
        while start < end:
            sum = sorted_nums[start] + sorted_nums[end]
            if sum == target:
                start_idx = nums.index(sorted_nums[start])
                end_idx = nums.index(sorted_nums[end])
                if end_idx == start_idx:
                    end_idx = nums.index(sorted_nums[end], end_idx + 1)
                return [start_idx, end_idx]
            elif sum > target:
                end -= 1
            else:
                start += 1
        return [-1, -1]

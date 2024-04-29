from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        counter_map = {}
        for num in nums:
            if num not in counter_map:
                counter_map[num] = False
        max_count = 1
        for num in nums:
            curr_count = 1
            if counter_map[num] == True: continue
            counter_map[num] = True
            right_elem = num + 1
            left_elem = num - 1
            while right_elem in counter_map:
                counter_map[right_elem] = True
                curr_count += 1
                right_elem += 1
            while left_elem in counter_map:
                counter_map[left_elem] = True
                curr_count += 1
                left_elem -= 1
            max_count = max(max_count, curr_count)
        return max_count
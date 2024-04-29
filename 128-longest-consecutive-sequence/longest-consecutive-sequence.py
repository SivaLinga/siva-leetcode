class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        numSet = {}
        max_length = 0

        for num in nums:
            if num not in numSet:
                numSet[num] = False

        for num in nums:
            if numSet[num] == True: continue
            # check if num is start of a sequence
            if num - 1 not in numSet:
                numSet[num] = True
                curr_length = 0
                while num + curr_length in numSet:
                    numSet[num + curr_length] = True
                    curr_length += 1
                max_length = max(curr_length, max_length)
        return max_length
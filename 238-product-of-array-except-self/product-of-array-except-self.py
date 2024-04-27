class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix_val = 1
        for i in range(n):
            answer[i] = prefix_val
            prefix_val *= nums[i]

        postfix_val = 1
        for i in range(n-1, -1, -1):
            answer[i] *= postfix_val
            postfix_val *= nums[i]
        return answer
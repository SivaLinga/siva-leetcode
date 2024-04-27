class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # check if there is 0 in the input
        zero_elem_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_elem_index = i
        
        prod_result = 1
        answer = []
        if zero_elem_index > -1:
            answer = [0] * len(nums)
            for idx, num in enumerate(nums):
                if idx == zero_elem_index: continue
                prod_result = num * prod_result
            answer[zero_elem_index] = prod_result
        else:
            answer = [nums[0]] * len(nums)
            for num in nums:
                prod_result = num * prod_result
            for i in range(len(nums)):
                answer[i] = prod_result // nums[i]
        return answer
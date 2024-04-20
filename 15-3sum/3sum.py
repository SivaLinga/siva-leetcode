class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_res = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            first_num = nums[i]
            
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                second_num = nums[j]
                third_num = nums[k]
                sum = first_num + second_num + third_num
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    final_res.add((first_num, second_num, third_num))
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return final_res

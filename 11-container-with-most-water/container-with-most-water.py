class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0
        if n == 1: return 1 * height[0]
        
        # initialization
        left = 0
        right = n - 1
        max_area = 0
 
        while(left < right):
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area
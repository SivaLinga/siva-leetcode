from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. if triplet contains 0
        if z:
            if len(z) >= 3:
                res.add((0, 0, 0))
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for x, y in combinations(n, 2):
            target = -(x + y)
            if -(x + y) in P:
                res.add(tuple(sorted([x, y, target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for x, y in combinations(p, 2):
            target = -(x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))

        return list(res)
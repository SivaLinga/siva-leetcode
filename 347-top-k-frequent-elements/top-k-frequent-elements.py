from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final_res = []
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        
        count_in_order = sorted(countMap.values())

        while(len(final_res) < k):
            curr_count = count_in_order.pop()
            for elem, cnt in countMap.items():
                if curr_count == cnt:
                    if len(final_res) < k and elem not in final_res:
                        final_res.append(elem)
        return final_res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        
        count_in_order = sorted(countMap.values(), reverse = True)
        
        final_res = []
        for curr_count in count_in_order:
            if len(final_res) == k:
                    return final_res
            for elem, v in countMap.items():
                if len(final_res) < k and v == curr_count and elem not in final_res:
                   final_res.append(elem)
        return final_res

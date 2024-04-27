from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #populate hashmap
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
                
        # create list of buckets
        bucket = []
        for i in range(len(nums)):
            bucket.append([])
        
        # populate buckets
        for c_k, c_v in countMap.items():
            bucket[c_v - 1].append(c_k)
        
        final_res = []
        # loop through each list in the bucket
        for b1 in reversed(bucket):
            if len(final_res) == k: return final_res
            if len(b1) == 0: continue
            for b2 in b1:
                if len(final_res) < k and b2 not in final_res:
                    final_res.append(b2)
        return final_res

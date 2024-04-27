from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #populate hashmap
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
                
        
        # create list of buckets
        buckets = [[] for i in range(len(nums) + 1)]

        # populate each bucket with freq_map keys
        for item, number in freq_map.items():
            buckets[number].append(item)
        
        final_res = []
        # loop through each list in the bucket
        for bucket in reversed(buckets):
            for bucket_item in bucket:
                if bucket_item not in final_res:
                    final_res.append(bucket_item)
                if len(final_res) == k: 
                    return final_res

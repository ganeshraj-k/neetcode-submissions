from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1_counts=defaultdict(int)

        for num in nums:
            dict1_counts[num]+=1

        heap = []

        for num in dict1_counts.keys():
            heapq.heappush(heap, (dict1_counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        

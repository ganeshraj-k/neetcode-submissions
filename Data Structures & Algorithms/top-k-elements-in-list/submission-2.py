from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1_counts=defaultdict(int)

        for num in nums:
            dict1_counts[num]+=1

        dict1_counts = dict(sorted(dict1_counts.items(), key = lambda item: (-item[1], item[0] )  ))  


        return list(dict1_counts.keys())[0:k]

        

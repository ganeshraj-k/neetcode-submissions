from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Provide `list` as the factory function
        groups_dict = defaultdict(list)
        res = []
        for string in strs:
            # 2. Join sorted characters into a clean string key
            counts_list = [0] * 26
            for c in string:
                counts_list[ord(c) - ord('a')]+=1


            groups_dict[tuple(counts_list)].append(string)

        for val in groups_dict.values():
            res.append(val)

        return res
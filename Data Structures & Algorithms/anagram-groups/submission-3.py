from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            mp[tuple(sorted(word))].append(word)

        return list(mp.values())
        
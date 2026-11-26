from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str_ in strs:
            count = [0] * 26
            for ch in str_:
                count[ord(ch) - ord("a")] += 1
            map[tuple(count)].append(str_)

        return list(map.values())
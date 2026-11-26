from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = defaultdict(list)
        
        for word in strs:
            sig = [0]*26
            for c in word:
                sig[ord(c.lower()) - ord('a')] += 1
            resMap[tuple(sig)].append(word)
        
        return list(resMap.values())
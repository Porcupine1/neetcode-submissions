from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = defaultdict(list)

        for word in strs:
            sig = [0]*26
            for char in word:
                sig[ord(char) - ord("a")] += 1
            anags[tuple(sig)].append(word)

        return list(anags.values())
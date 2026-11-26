from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        for word in strs:
            crypt = [0] * 26
            for char in word:
                crypt[ord(char) - ord('a')] += 1
            grams[tuple(crypt)].append(word)

        return([x for x in grams.values()])
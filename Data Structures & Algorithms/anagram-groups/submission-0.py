from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            if len(s) != len(t):
                return False

            count_s, count_t = defaultdict(int), defaultdict(int)

            for i in range(len(s)):
                count_s[s[i]] += 1
                count_t[t[i]] += 1
            
            return count_s == count_t

        res = [[strs[0]]]
        for word in strs[1:]:
            index = None
            for i, anags in enumerate(res):
                if isAnagram(word, anags[0]):
                    index = i
                    break
            if index is not None:
                res[index].append(word)
            else:
                res.append([word])

        return res
                
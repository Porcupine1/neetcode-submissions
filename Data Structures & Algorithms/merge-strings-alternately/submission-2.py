class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=r = 0
        len1, len2 = len(word1), len(word2)
        n = 2*min(len1, len2)
        arr = [None]*n

        for i in range(n):
            if i%2 == 0:
                arr[i] = word1[l]
                l+=1
            else:
                arr[i] = word2[r]
                r+=1
        return ''.join(arr) + word1[n//2:] + word2[n//2:]
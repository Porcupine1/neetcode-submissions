class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def getCombo(curr, currSum, i):
            if currSum == target:
                res.append(curr[:])

            for j in range(i, len(candidates)):
                val = candidates[j]
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if currSum + val > target:
                    return 
                getCombo(curr + [val], currSum+val, j+1)

        getCombo([], 0, 0)
        return res
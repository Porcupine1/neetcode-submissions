class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def find_combo(curr, ind, total):
            if total == target:
                res.append(curr[:])
                return

            for j in range(ind, len(candidates)):
                if j> ind and candidates[j] == candidates[j-1]:
                    continue
                
                curr.append(candidates[j])
                find_combo(curr, j+1, total+candidates[j])
                curr.pop()

        find_combo([], 0, 0)
        return res
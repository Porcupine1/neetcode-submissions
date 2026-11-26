class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def find_combo(curr, ind, rem):
            if rem == 0:
                res.append(curr[:])
                return

            for j in range(ind, len(candidates)):
                if j > ind and candidates[j] == candidates[j-1]:
                    continue
                if rem-candidates[j] < 0:
                    return
                
                curr.append(candidates[j])
                find_combo(curr, j+1, rem-candidates[j])
                curr.pop()

            

        find_combo([], 0, target)
        return res
            
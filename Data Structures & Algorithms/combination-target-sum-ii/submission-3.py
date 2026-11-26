class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def find_combo(curr, ind, rem):
            if rem == 0:
                res.append(curr[:])
                return
            if rem < 0 or ind >= len(candidates):
                return

            curr.append(candidates[ind])
            find_combo(curr, ind+1, rem-candidates[ind])
            curr.pop()
            
            while ind+1 < len(candidates) and candidates[ind] == candidates[ind+1]:
                ind+=1

            find_combo(curr, ind+1, rem)
            

        find_combo([], 0, target)
        return res
            
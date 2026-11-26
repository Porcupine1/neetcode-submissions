class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def find_combo(i, curr, total):
            if total == target:
                if curr not in res:
                    res.append(curr[:])
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                curr.append(candidates[j])
                find_combo(j+1, curr, total+candidates[j])
                curr.pop()
                find_combo(j+1, curr, total)

        
        find_combo(0, [], 0)
        return res
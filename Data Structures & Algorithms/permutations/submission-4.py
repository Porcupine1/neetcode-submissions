class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            new = []
            for e in res:
                #new.append([num]+e)
                for i in range(len(e)+1):
                    new.append(e[:i]+[num]+e[i:])
                    print(new)
                res = new
        return res
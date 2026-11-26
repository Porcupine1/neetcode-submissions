class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l + 1, r + 1]
            elif currSum < target:
                l += 1
            else:
                r -= 1

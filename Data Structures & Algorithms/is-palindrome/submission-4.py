class Solution:
    def isPalindrome(self, s: str) -> bool:
        val_chars = [char.lower() for char in s if char.isalnum()]
        return val_chars == val_chars[::-1]
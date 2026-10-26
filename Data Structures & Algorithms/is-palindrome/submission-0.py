class Solution:
    def isPalindrome(self, s: str) -> bool:

        text = "".join([char.lower() for char in s if char.isalnum()])

        if text == text[::-1]:
            return True
        else:
            return False
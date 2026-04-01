class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ''.join(char for char in s if char.isalnum()).lower()
        print(l)
        return True if l[::-1] == l else False
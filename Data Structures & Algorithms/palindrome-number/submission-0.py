class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_int = str(x)
        reversed_string = string_int[::-1]

        if reversed_string == string_int:
            return True
        else:
            return False
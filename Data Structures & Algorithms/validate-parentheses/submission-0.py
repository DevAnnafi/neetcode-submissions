class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            # Opening Bracket
            if char in "({[":
                stack.append(char)
            # Closing Bracket
            else:
                if not stack:
                    return False

                top = stack.pop()
                if pairs[char] != top:
                    return False
        
        return not stack
           
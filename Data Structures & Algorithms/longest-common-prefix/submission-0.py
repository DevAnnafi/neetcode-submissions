class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Use first string as a reference
        for i in range(len(strs[0])):
            first = strs[0][i]
            
            # Compare the string with the other strings
            for s in strs:
                if s in strs[1:]:
                    if i == len(s) or s[i] != first:
                        return strs[0][:i]

        return strs[0]



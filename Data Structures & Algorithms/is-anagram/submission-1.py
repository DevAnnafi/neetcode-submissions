class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Convert both strings to lowercase and remove spaces
        s = Counter(s.lower().replace(" ", ""))
        t = Counter(t.lower().replace(" ", ""))
  
        # Check if the character counts are equal
        return s == t
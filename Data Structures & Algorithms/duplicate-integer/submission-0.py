class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set
        seen = {}
        # Iterate through the array
        for i in nums:
            if i in seen:
                return True
            seen[i] = 1
        return False
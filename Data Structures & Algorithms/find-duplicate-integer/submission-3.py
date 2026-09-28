class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [False] * len(nums)
        
        for num in nums:
            # If the number has been seen before, it's the duplicate
            if seen[num]:
                return num
            # Mark the current number as seen
            seen[num] = True
            
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            # if target is less than the middle element, ignore the right half
            if nums[mid] > target:
                right = mid - 1

            # if target is greater than the middle element, ignore the left half
            if nums[mid] < target:
                left = mid + 1
        
        return -1

            
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize the variables
        left = 0
        right = len(numbers) - 1

        # Loop through the array
        while left < right:
            # Compute the sum
            sum = numbers[left] + numbers[right]

            # if sum is less than target, move left pointer to the right
            if sum < target:
                left += 1
            # if sum is greater than target, move right pointer to the left
            elif sum > target:
                right -= 1
            else:
                # if sum is equal to target, return indices + 1
                return [left + 1, right + 1]

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize left, right indices and then max_area
        left = 0
        right = len(heights) - 1
        max_area = 0

        # Loop through the array
        while left < right:
            # Compute width
            width = right - left
            # Compute area
            area = width * min(heights[left], heights[right])
            # Compute max_area
            max_area = max(max_area, area)

            # Moving the pointers left and right till we find the container with the most water
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
            
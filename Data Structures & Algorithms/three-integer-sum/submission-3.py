class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()

        # Initialize answer variable
        res = []

        # Initialize n 
        n = len(nums)

        # Initialize the fixed variable 
        for i in range(n-2):
            # skip duplicate and continue to the next pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize the variables
            left = i + 1
            right = n - 1

            # Loop through nums
            while left < right:
                # Compute sum
                sum = nums[i] + nums[left] + nums[right]
                # If sum is less than zero, move left pointer to the right
                if sum < 0:
                    left += 1
                # If sum is greater than zero, move right pointer to the left
                elif sum > 0:
                    right -= 1
                # if sum is equal to zero, return the triplets and remove the duplicates
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # skip duplicates of the left side and move the left pointer to the right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # skip duplicates on the right and move the right pointer to the right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move pointers after removing the duplicates
                    left += 1
                    right -= 1

        return res

                



        
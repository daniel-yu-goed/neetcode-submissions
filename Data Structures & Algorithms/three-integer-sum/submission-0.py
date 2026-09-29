class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        results = []

        # 1. Sort the array to handle duplicates and enable two-pointer logic.
        nums.sort()

        # 2. Loop through the array using index i
        #   Let a = nums[i].
        #   If a > 0, break (all remaining numbers are positive).
        #   Skip duplicate values for the first number.
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue

            # 3. Use two-pointer
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1 # too large, move "right" left
                if three_sum < 0:
                    left += 1 # too small, move "left" right
                if three_sum == 0:
                    results.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip the duplicates for the second number, i.e. nums[left]
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return results
        
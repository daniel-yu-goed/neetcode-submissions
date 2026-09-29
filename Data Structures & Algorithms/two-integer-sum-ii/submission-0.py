class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two-pointer solution
        # Time complexity: O(n)
        # Space complexity: O(1)

        """ We keep two pointers, one at the start and the other at the end of the array.
        If the sum of the numbers at the two pointers is greater than the target,
        decrement the right pointer (because the right one is too large).
        Else, increment the left pointer (because the left one is too small).
        Repeat this process until you find a valid pair."""

        left, right = 0, len(numbers) - 1
        
        while left < right:
            num_sum = numbers[left] + numbers[right]
            if num_sum == target:
                return [left+1, right+1]

            if num_sum > target:
                right -= 1
            else:
                left += 1

        
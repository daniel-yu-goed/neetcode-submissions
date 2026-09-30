class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## Two-pointer solution
        ## Time complexity: O(n)
        ## Space complexity: O(1)
        """
        Using two pointers lets us efficiently search for the maximum area
        without checking every pair.
        We start with the widest container (left at start, right at end).
        The height is limited by the shorter line,
        so to potentially increase the area,
        we must move the pointer at the shorter line inward.
        Moving the taller line never helps
        because it keeps the height the same but reduces the width.
        By always moving the shorter side, we explore all meaningful possibilities.
        """

        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            result = max(result, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result
        
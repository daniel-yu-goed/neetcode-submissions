class Solution:
    def trap(self, height: List[int]) -> int:
        ## Two-pointer solution
        ## Time complexity: O(n)
        ## Space complexity: O(1)

        """
        Water at any position depends on the "shorter" wall
        between the left and right sides.
        So if the left wall is shorter, the right wall can't help us
        because water is limited by the left side.
        That means we safely move the left pointer inward and
        calculate how much water can be trapped there.
        Similarly, if the right wall is shorter, we move the right pointer left.
        
        As we move the pointers,
        we keep track of the highest wall seen so far on each side (leftMax and rightMax).
        The water at each position is simply:
        (max wall on that side) - (height at that position)
        """
        if len(height) == 0:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += (rightMax - height[right])

        return result
        
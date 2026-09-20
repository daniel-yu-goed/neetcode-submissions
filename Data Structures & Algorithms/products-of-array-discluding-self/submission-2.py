class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can use the prefix and suffix technique.
        # First, we iterate from left to right and
        # store the prefix products for each index in a prefix array,
        # excluding the current index's number.
        # Then, we iterate from right to left and
        # store the suffix products for each index in a suffix array,
        # also excluding the current index's number.
        # Finally, we simply multiply the prefix and suffix products at each index.

        # Time complexity: O(n)
        # Space complexity: O(n)

        prefix_products = [1] * len(nums) # initilization for all 1
        for i in range(len(nums)):
            # special case
            if i == 0:
                prefix_products[i] = 1
            else:
                prefix_products[i] = prefix_products[i-1] * nums[i-1]

        suffix_products = [1] * len(nums) # initilization for all 1
        for i in reversed(range(len(nums))):
            # special case
            if i == len(nums) - 1:
                suffix_products[i] = 1
            else:
                suffix_products[i] = suffix_products[i+1] * nums[i+1]

        products = [1] * len(nums) # initilization for all 1
        for i in range(len(nums)):
            products[i] = prefix_products[i] * suffix_products[i]

        return products
        
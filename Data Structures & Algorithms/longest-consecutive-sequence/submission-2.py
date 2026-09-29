class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## 1. convert to set to remove duplicates
        num_set = set(nums)

        ## 2. find the starting element(s), e.g. n, of the consecutive sequences
        ## if and only if n-1 does not exist
        starting_elements = [n for n in num_set if n-1 not in num_set]

        ## 3. find the max length
        max_length = 0 # if nums is empty
        for n in starting_elements:
            length = 1
            while n+1 in num_set:
                length += 1
                n += 1
            
            if length > max_length:
                max_length = length

        return max_length


        
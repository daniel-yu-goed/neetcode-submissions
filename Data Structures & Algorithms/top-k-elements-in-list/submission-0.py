class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use bucket sort
        # Time complexity: O(n)
        # Space complexity: O(n)

        # 1. Build a frequency map that counts how many times each number appears.
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 2. Create a list of groups freq,
        # where freq[i] will store all numbers that appear exactly i times.
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        # 3. Initialize an empty result list, and 
        # Loop from the largest possible frequency down to 1
        res = []
        for i in reversed(range(len(nums) + 1)): # count down
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
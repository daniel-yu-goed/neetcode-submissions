class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Sliding window (optimal)
        ## Time complexity: O(n), n is the length of the string
        ## Space complexity: O(m), m is the total number of unique chars
        
        # Algorithem
        # 1. Create a dict to store the last index of each char 
        lastIndexMp = defaultdict(int)

        # 2. initialize
        left = 0
        maxLength = 0

        # 3. Loop through the string with index right
        # If s[right] is already in lastIndexMp, move left to mp[s[right]] + 1, but never backward.
        # Update lastIndexMp[s[right]] = right.
        # Update the longest length: maxLength = max(maxLength, r - l + 1).

        for right in range(len(s)):
            if s[right] in lastIndexMp:
                left = max(lastIndexMp[s[right]] + 1, left)

            lastIndexMp[s[right]] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength


        


        
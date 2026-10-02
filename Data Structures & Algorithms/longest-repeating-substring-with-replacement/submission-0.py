class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxWindowSize = 0

        left = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            windowSize = right - left + 1
            
            # check if windowSize is valid
            # if not, shrink it
            while windowSize > max(freq.values()) + k:
                freq[s[left]] -= 1
                left += 1
                windowSize -= 1

            validWindowSize = right - left + 1
            maxWindowSize = max(validWindowSize, maxWindowSize)

        return maxWindowSize
        
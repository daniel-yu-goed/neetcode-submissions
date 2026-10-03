class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## Sliding Window (Optimal)
        ## Time compexlity: O(n)
        ## Space complexity: O(m)
        # Where n is the length of the string, and 
        # m is the total number of unique chars in the string
        """
        We want the longest window where we can make all characters the same 
        using at most k replacements.
        Using the true current maximum frequency,
        the window is valid as long as:

        window size ≤ count of the most frequent character + k

        Why?
        Because the characters that aren't the most frequent 
        are the ones we would need to replace.

        So while expanding the window, we track:
        - the frequency of each character,
        - the max window size

        During expanding, always check if the window size is valid or not
        - If not, shrink it until it is valid and update window size
        
        If it is valid, update window size and max window size
        """
        freq = defaultdict(int)
        maxWindowSize = 0

        left = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            windowSize = right - left + 1
            
            # check if windowSize is valid
            # if not, shrink it
            # Note: time complexity of "freq.values()" is O(1)
            while windowSize > max(freq.values()) + k:
                freq[s[left]] -= 1
                left += 1
                windowSize -= 1

            validWindowSize = right - left + 1
            maxWindowSize = max(validWindowSize, maxWindowSize)

        return maxWindowSize
        
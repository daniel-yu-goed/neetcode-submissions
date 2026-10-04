class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## Sliding window
        # Time complexity: O(n)
        # Space complexity: O(m)
        # n: the length of s2
        # m: the length of s1

        """
        Since a permutation of s1 must have the same character counts,
        we can use a fixed-size sliding window over s2 whose length is exactly len(s1).


        We maintain two frequency arrays:
        - one for s1
        - one for the current window in s2

        If these two arrays ever match, the window is a valid permutation.
        As we slide the window forward,
        we update counts by removing the left character and adding the new right character — 
        no need to rebuild the counts each time.
        This makes the solution fast and efficient.
        """
        if len(s2) < len(s1):
            return False

        charFreqS1 = defaultdict(int)
        charFreqWindow = defaultdict(int)

        ## fill charFreqS1
        for i in range(len(s1)):
            charFreqS1[s1[i]] = charFreqS1.get(s1[i], 0) + 1

        windowSize = len(s1)

        # fill charFreqWindow
        for i in range(windowSize):
            charFreqWindow[s2[i]] = charFreqWindow.get(s2[i], 0) + 1

        left = 0
        right = windowSize - 1
        while right < len(s2):
            # found the answer
            if charFreqS1 == charFreqWindow:
                return True
            
            # cannot slide anymore because right is at the end
            if right == len(s2) - 1:
                break

            # slide the window to the right
            charFreqWindow[s2[left]] -= 1
            if charFreqWindow[s2[left]] == 0:
                del charFreqWindow[s2[left]]
            left += 1

            right += 1
            charFreqWindow[s2[right]] = charFreqWindow.get(s2[right], 0) + 1

        return False




        
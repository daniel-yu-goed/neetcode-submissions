class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "":
            return ""

        charFreqT = defaultdict(int)
        charFreqWindow = defaultdict(int)

        # fill charFreqT
        for i in range(len(t)):
            charFreqT[t[i]] = charFreqT.get(t[i], 0) + 1

        need = len(charFreqT) # number of distinct chars in t
        have = 0 # number of chars in window which meet the required count in t

        left = 0
        right = 0
        
        foundWindow = [-1, -1]
        for right in range(len(s)):
            charFreqWindow[s[right]] = charFreqWindow.get(s[right], 0) + 1

            if s[right] in charFreqT and charFreqWindow[s[right]] == charFreqT[s[right]]:
                have += 1

            while have == need:
                # found for the first time
                if foundWindow == [-1, -1]:
                    foundWindow = [left, right]
                else:
                    newWindowSize = right - left + 1
                    curWindowSize = foundWindow[1] - foundWindow[0] + 1
                    if newWindowSize < curWindowSize:
                        foundWindow = [left, right]

                # shink from the left
                charFreqWindow[s[left]] -= 1
                if s[left] in charFreqT and charFreqWindow[s[left]] < charFreqT[s[left]]:
                    have -= 1
                left += 1

        return s[foundWindow[0]: foundWindow[1] + 1] if foundWindow != [-1, -1] else ""
                


            
        

        
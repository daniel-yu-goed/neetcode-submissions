class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # 1. Count frequency using a map
            char_count = {}

            for char in s:
                char_count[char] = char_count.get(char, 0) + 1

            # 2. Convert the counts into a standardized, sorted tuple of items
            # Sorting the unique characters present is highly efficient because 
            # unique characters (U) <= total length of string (K).
            # We use tuple as a key because it is immutable
            key = tuple(sorted(char_count.items()))

            anagram_map[key].append(s)

        return list(anagram_map.values())
        
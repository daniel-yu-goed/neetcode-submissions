class Solution:
    # We can use an encoding approach 
    # where we start with a number representing the length of the string,
    # followed by a separator character (let's use # for simplicity),
    # and then the string itself.
    
    # To decode, we read the number until we reach a #,
    # then use that number to read the specified number of characters as the string.

    # Time complexity: O(m)
    # Space complexity: O(m+n)
    # m: the sum of lengths of all the strings
    # n: the number of strings
    def encode(self, strs: List[str]) -> str:
        encoded_strings = [f"{len(a_str)}#{a_str}" for a_str in strs]
        return "".join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        valid_nums = [str(i) for i in range(10)]

        num_start_at = 0
        num_end_at = 0
        results = []

        i = 0
        while i < len(s):
            if i != len(s) - 1 and s[i] in valid_nums and s[i+1] == "#":
                num_end_at = i
                string_length = int(s[num_start_at:num_end_at + 1])
                
                string_start_at = num_end_at + 2
                string_end_at = string_start_at + string_length - 1
                results.append(s[string_start_at:string_end_at + 1])

                #i = i + 1 + string_length + 1
                i = i + string_length + 2
                num_start_at = i

            else:
                i = i + 1
        
        return results


            

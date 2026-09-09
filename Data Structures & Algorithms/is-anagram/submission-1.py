class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # quick fail if length differs
        if len(s) != len(t):
            return False

        s_freq = self.get_frequency_dict(s)
        t_freq = self.get_frequency_dict(t)

        # quick fail if char set differs
        if len(s_freq) != len(t_freq):
            return False

        for key in s_freq:
            if key not in t_freq:
                return False
            if s_freq[key] != t_freq[key]:
                return False

        return True

        
    def get_frequency_dict(self, my_str: str) -> dict:
        my_dict = {}
        for s in my_str:
            if s in my_dict:
                my_dict[s] += 1
            else:
                my_dict[s] = 1
        
        return my_dict

        
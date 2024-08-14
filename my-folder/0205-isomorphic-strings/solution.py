class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create two dictionaries to store the character mappings
        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check if there is a mapping from s -> t
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t

            # Check if there is a mapping from t -> s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s

        return True


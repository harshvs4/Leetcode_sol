class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string into words
        words = s.split()
        
        # If pattern length and number of words do not match, return False
        if len(pattern) != len(words):
            return False
        
        # Dictionaries to maintain the mappings
        map_x_to_t = {}
        map_t_to_x = {}

        # Iterate through characters in pattern and corresponding words
        for char_x, word_y in zip(pattern, words):
            # Check if current pattern character is already mapped
            if char_x in map_x_to_t:
                if map_x_to_t[char_x] != word_y:
                    return False
            else:
                map_x_to_t[char_x] = word_y
            
            # Check if current word is already mapped to another pattern character
            if word_y in map_t_to_x:
                if map_t_to_x[word_y] != char_x:
                    return False
            else:
                map_t_to_x[word_y] = char_x

        return True


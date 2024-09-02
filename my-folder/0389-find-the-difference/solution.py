class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize the hashmap
        hashmap = {}
        
        # Count the frequency of each character in string s
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        
        # Decrease the frequency based on characters in string t
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
                # If a character's count goes to zero, remove it from the hashmap
                if hashmap[char] == 0:
                    del hashmap[char]
            else:
                # If the character is not in hashmap, it means this is the extra character
                return char

        # At this point, the hashmap should be empty if all characters in t were matched
        # If there is still a character left, return it (this handles the last character)
        for char in hashmap:
            return char


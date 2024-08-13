from typing import List
import itertools

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Edge case: If there are no words or the string is empty
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        res = []
        word_count = len(words)
        
        # Create a dictionary to count the occurrences of each word in the words list
        word_map = {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        
        # Iterate over every possible starting point in s
        for i in range(len(s) - total_len + 1):
            seen_words = {}
            j = 0
            # Check if the substring of total length is a valid concatenation of all words
            while j < word_count:
                word = s[i + j * word_len: i + (j + 1) * word_len]
                if word in word_map:
                    seen_words[word] = seen_words.get(word, 0) + 1
                    if seen_words[word] > word_map[word]:
                        break
                else:
                    break
                j += 1
            if j == word_count:
                res.append(i)
        
        return res


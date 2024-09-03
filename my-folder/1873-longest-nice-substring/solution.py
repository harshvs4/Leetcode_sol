class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""

        def is_nice(sub):
            chars = set(sub)
            for char in chars:
                if char.swapcase() not in chars:
                    return False
            return True

        max_len = 0
        max_substr = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if is_nice(substr) and len(substr) > max_len:
                    max_len = len(substr)
                    max_substr = substr

        return max_substr


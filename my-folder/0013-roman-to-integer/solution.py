class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        dict1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0

        while i < n:
            if i + 1 < n and dict1[s[i]] < dict1[s[i + 1]]:
                total += dict1[s[i + 1]] - dict1[s[i]]
                i += 2  # Skip the next character as it is already processed
            else:
                total += dict1[s[i]]
                i += 1

        return total


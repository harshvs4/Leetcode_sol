from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterr = Counter(ransomNote)
        counterm = Counter(magazine)

        return counterr <= counterm

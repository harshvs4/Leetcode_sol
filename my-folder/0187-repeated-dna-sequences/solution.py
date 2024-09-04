class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        arr = []
        n = len(s)
        visited = set()

        for right in range(n-9):
            substr = s[right:right+10]

            if substr in visited:
                arr.append(substr)

            visited.add(substr)

        return set(arr)



        

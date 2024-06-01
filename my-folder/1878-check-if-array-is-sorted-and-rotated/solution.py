class Solution:
    def check(self, arr: List[int]) -> bool:
        op = 0
        for i in range(len(arr)):
            if arr[(i+1)%len(arr)]>=arr[i]:
                pass
            else:
                op+=1
                if op > 1:
                    return False
        return True

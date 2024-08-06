class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for i in details:
            x = int(i[11:13])
            if x > 60:
                cnt += 1

        return cnt
        

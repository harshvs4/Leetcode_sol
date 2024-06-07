class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for i in range(0, numRows):
            if i==0:
                l.append([1])
            elif i==1:
                l.append([1,1])
            else:
                x = [0]*(i+1)
                x[0] = x[-1] = 1
                for j in range(1, i):
                    x[j] = l[i-1][j-1] + l[i-1][j]
                l.append(x)
        return l

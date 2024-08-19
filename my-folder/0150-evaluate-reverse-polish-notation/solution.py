class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+","-","*","/"}:
                x = stack.pop()
                y = stack.pop()
                if t == "+":
                    stack.append(y+x)
                elif t == "-":
                    stack.append(y-x)
                elif t == "*":
                    stack.append(y*x)
                else:
                    stack.append(int(y/x))
            else:
                stack.append(int(t))
        
        return stack[-1]
        

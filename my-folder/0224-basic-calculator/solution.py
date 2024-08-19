class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        result = 0
        operation = 1  # 1 for '+', -1 for '-'

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in {"+", "-"}:
                result += operation * current_number
                operation = 1 if char == "+" else -1
                current_number = 0
            elif char == "(":
                stack.append(result)
                stack.append(operation)
                result = 0
                operation = 1
            elif char == ")":
                result += operation * current_number
                result *= stack.pop()  # Pop the operation before '('
                result += stack.pop()  # Pop the result before '('
                current_number = 0

        return result + operation * current_number


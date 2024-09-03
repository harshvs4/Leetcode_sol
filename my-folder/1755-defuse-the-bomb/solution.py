from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n  # Initialize the result array with zeros

        if k == 0:
            return result

        if k > 0:
            for i in range(n):
                total_sum = 0
                for j in range(1, k + 1):
                    total_sum += code[(i + j) % n]
                result[i] = total_sum
        else:
            for i in range(n):
                total_sum = 0
                for j in range(1, abs(k) + 1):
                    total_sum += code[(i - j) % n]
                result[i] = total_sum

        return result


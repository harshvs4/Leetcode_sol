class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If digits is empty, return an empty list
        if not digits:
            return []

        # Mapping of digits to their corresponding letters
        dict1 = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # Result list to store all the combinations
        res = []

        # Helper function for backtracking
        def backtrack(index, current_combination):
            # Base case: If the current combination length matches the digits length
            if index == len(digits):
                res.append(''.join(current_combination))  # Join list to form a string and add to result
                return

            # Get the digit at the current index
            current_digit = digits[index]

            # Iterate over all possible letters for this digit
            for letter in dict1[current_digit]:
                # Append the letter to the current combination and move to the next digit
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                # Backtrack by removing the last added letter
                current_combination.pop()

        # Start the backtracking process
        backtrack(0, [])

        return res


class Solution:
    def isHappy(self, n: int) -> bool:
        current_number = n
        number = 0
        seen_numbers = set()
        
        while True:
            for i in str(current_number):
                number += int(i) ** 2
            if number == 1:
                return True
            if number in seen_numbers:
                return False
            seen_numbers.add(number)
            current_number = number
            number = 0


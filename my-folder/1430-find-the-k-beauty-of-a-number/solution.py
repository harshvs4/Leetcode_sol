class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)  # Convert the number to a string
        tcount = 0  # Total count of valid substrings

        for i in range(len(num_str) - k + 1):  # Sliding window approach
            substring = num_str[i:i + k]  # Extract substring of length k
            substring_int = int(substring)  # Convert substring to integer

            # Check if the substring is a divisor of num
            if substring_int != 0 and num % substring_int == 0:
                tcount += 1

        return tcount


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0  # Pointer to write compressed characters in-place
        i = 0  # Pointer to traverse the list

        while i < n:
            char = chars[i]
            j = i

            # Count consecutive characters
            while j < n and chars[j] == char:
                j += 1

            # Write the current character
            chars[write] = char
            write += 1

            # Write the count if it's more than 1
            count = j - i
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            # Move to the next different character
            i = j

        # The list `chars` is modified in place, return the new length
        return write


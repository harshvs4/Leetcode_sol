import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def sieve(n):
            is_prime = [True] * (n + 1)
            p = 2
            while (p * p <= n):
                if (is_prime[p] == True):
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
            return prime_numbers
        
        # Calculate the range and the limit for prime numbers
        limit = int(math.sqrt(r)) + 1
        primes = sieve(limit)
        
        # Calculate special numbers in the range [l, r]
        special_count = 0
        for p in primes:
            p_squared = p * p
            if l <= p_squared <= r:
                special_count += 1
        
        # Total numbers in range [l, r]
        total_numbers = r - l + 1
        
        # Non-special numbers
        non_special_count = total_numbers - special_count
        
        return non_special_count


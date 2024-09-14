class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            # Handle collisions
            while stack and stack[-1] > 0 and i < 0:
                # If the previous asteroid is larger, the current asteroid is destroyed
                if stack[-1] > abs(i):
                    i = 0  # Current asteroid gets destroyed
                # If both are equal, destroy both
                elif stack[-1] == abs(i):
                    stack.pop()  # Both asteroids get destroyed
                    i = 0  # Current asteroid gets destroyed
                # If the current asteroid is larger, pop the last one and continue checking
                else:
                    stack.pop()

            # If the current asteroid wasn't destroyed, add it to the stack
            if i != 0:
                stack.append(i)

        return stack


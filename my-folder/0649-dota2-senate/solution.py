from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Initialize deques to store the positions of Radiant (R) and Dire (D) senators
        r_positions = deque([i for i, s in enumerate(senate) if s == 'R'])
        d_positions = deque([i for i, s in enumerate(senate) if s == 'D'])
        n = len(senate)

        while r_positions and d_positions:
            # Compare the current positions of Radiant and Dire senators
            r_senator = r_positions.popleft()
            d_senator = d_positions.popleft()
            
            if r_senator < d_senator:
                # Radiant senator votes first, they get to ban the Dire senator
                r_positions.append(r_senator + n)
            else:
                # Dire senator votes first, they get to ban the Radiant senator
                d_positions.append(d_senator + n)

        # Whoever has remaining senators wins
        return 'Radiant' if r_positions else 'Dire'


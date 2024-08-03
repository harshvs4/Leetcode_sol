from typing import List
from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # Dictionary to hold the count of balls of each color for each player
        player_color_count = defaultdict(lambda: defaultdict(int))

        # Fill the dictionary with the counts
        for player, color in pick:
            player_color_count[player][color] += 1

        # Count the number of players who win the game
        winning_count = 0
        for player in range(n):
            for color, count in player_color_count[player].items():
                if count > player:
                    winning_count += 1
                    break  # No need to check other colors for this player

        return winning_count


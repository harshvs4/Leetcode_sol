from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # If there are no balloons, no arrows are needed
        if not points:
            return 0

        # Sort points based on their end coordinates
        points.sort(key=lambda x: x[1])

        # Initialize the count of arrows
        arrows = 1
        # Track the end of the first interval
        end = points[0][1]

        for i in range(1, len(points)):
            # If the start of the current balloon is after the end of the last burst one
            if points[i][0] > end:
                # Increment the arrow count
                arrows += 1
                # Update the end to the current balloon's end
                end = points[i][1]

        return arrows


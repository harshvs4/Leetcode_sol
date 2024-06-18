class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            # Get the last interval in the merged list
            last_interval = merged_intervals[-1]
            
            # Check if the current interval overlaps with the last merged interval
            if intervals[i][0] <= last_interval[1]:
                # Merge intervals
                last_interval[1] = max(last_interval[1], intervals[i][1])
            else:
                # If no overlap, add the current interval to the merged list
                merged_intervals.append(intervals[i])
        
        return merged_intervals
        

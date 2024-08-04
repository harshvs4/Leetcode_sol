from typing import List, Tuple
import heapq

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Function to run Dijkstra's algorithm from city 0 to city n-1
        def dijkstra(graph: List[List[Tuple[int, int]]], start: int, end: int) -> int:
            min_heap = [(0, start)]
            distances = [float('inf')] * n
            distances[start] = 0
            
            while min_heap:
                current_distance, current_node = heapq.heappop(min_heap)
                
                if current_node == end:
                    return current_distance
                
                if current_distance > distances[current_node]:
                    continue
                
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor))
                        
            return distances[end]
        
        # Initialize the graph with the existing roads
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append((i + 1, 1))
        
        result = []
        for ui, vi in queries:
            graph[ui].append((vi, 1))
            shortest_path_length = dijkstra(graph, 0, n - 1)
            result.append(shortest_path_length)
        
        return result

# Example usage:
# n = 5
# queries = [[0, 2], [2, 4], [0, 3]]
# sol = Solution()
# print(sol.shortestDistanceAfterQueries(n, queries))
# This should output the shortest path length from 0 to 4 after each query.


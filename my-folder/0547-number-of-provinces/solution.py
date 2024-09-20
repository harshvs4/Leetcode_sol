class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)  # Number of cities (nodes)
        visited = set()       # To track visited cities
        provinces = 0         # Count of provinces
        
        # Helper function to perform DFS
        def dfs(city):
            # Mark the current city as visited
            visited.add(city)
            # Explore all connected cities
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        # Visit each city
        for i in range(n):
            if i not in visited:
                # Start a new DFS for an unvisited city, which means a new province
                dfs(i)
                provinces += 1
        
        return provinces


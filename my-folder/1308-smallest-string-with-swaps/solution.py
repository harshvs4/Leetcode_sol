class Solution:
    def __init__(self):
        self.N = 10**5 + 1
        self.adj = [[] for _ in range(self.N)]
        self.visited = [False] * self.N
    
    def DFS(self, s, i, chars, indices):
        chars.append(s[i])
        indices.append(i)
        self.visited[i] = True
        
        for neighbour in self.adj[i]:
            if not self.visited[neighbour]:
                self.DFS(s, neighbour, chars, indices)
    
    def smallestStringWithSwaps(self, s, pairs):
        # Build the adjacency list
        for src, dst in pairs:
            self.adj[src].append(dst)
            self.adj[dst].append(src)
        
        s = list(s)  # Convert string to list for mutability
        
        for i in range(len(s)):
            if not self.visited[i]:
                chars = []
                indices = []
                
                # Perform DFS to find connected components
                self.DFS(s, i, chars, indices)
                
                # Sort characters and their indices
                chars.sort()
                indices.sort()
                
                # Place sorted characters back into the string
                for j in range(len(chars)):
                    s[indices[j]] = chars[j]
        
        return ''.join(s)

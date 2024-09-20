class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Set to keep track of visited rooms
        visited = set()

        # Helper function for DFS traversal
        def dfs(room):
            # Mark the current room as visited
            visited.add(room)
            # Go through all keys in the current room
            for key in rooms[room]:
                # If the room that the key opens hasn't been visited, visit it
                if key not in visited:
                    dfs(key)

        # Start DFS from room 0
        dfs(0)

        # If we have visited all rooms, return True; otherwise, return False
        return len(visited) == len(rooms)


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")  # Split the path by "/"
        #print(parts)
        for s in parts:
            if s == "" or s == ".":  # Skip empty parts and single dots
                continue
            elif s == "..":  # Handle ".."
                if stack:
                    stack.pop()
            else:  # Add valid directory names to the stack
                stack.append(s)
        
        return "/" + "/".join(stack)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the emptty adjacency matrix
        adjacency = {}
        for i in range(numCourses):
            adjacency[i] = []
        
        # Fill the edges
        for k, v in prerequisites:
            adjacency[k].append(v)

        # Visited set
        visited = set()

        # Check if that course requires itself
        def DFS_detect_cycle(course):
            # Base case
            if course in visited:
                return True
            
            # Add the course to the visited list
            visited.add(course)

            # Continue the path with the neighbours
            for req in adjacency[course]:
                if DFS_detect_cycle(req):
                    return True
            visited.remove(course)
            adjacency[course] = []
            return False

        # For ech course check if it is posible to execute
        for i in range(numCourses):
            if DFS_detect_cycle(i):
                return False
        
        # If no cycles have been detected return True
        return True


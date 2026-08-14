class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Corner case to prevent using visited
        oldC = image[sr][sc]
        if oldC == color:
            return image

        # Get the image size
        n_rows = len(image)
        n_cols = len(image[0])

        # Add the original pixel into the queue
        q = deque([(sr, sc)])
        image[sr][sc] = color

        # Define the directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Process all the pixels in the queue
        while q:
            # Remove a pixel from the queue
            r, c = q.popleft()

            # Add its neighbours
            for dr, dc in directions:
                # Get neighbour coordinates
                nr = r + dr
                nc = c + dc

                # Check if this neighbour is valid
                if nr>=0 and nr<n_rows and nc>=0 and nc<n_cols and image[nr][nc]==oldC:
                    # Change its color and add it to the queue
                    image[nr][nc]=color
                    q.append((nr,nc))
            
        # Return the image
        return image







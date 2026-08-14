class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Corner case to prevent using visited
        oldC = image[sr][sc]
        if oldC == color:
            return image
        
        # Get the image size
        n_rows = len(image)
        n_cols = len(image[0])

        def DFS(r, c):
            # Base case
            if r<0 or c<0 or r>=n_rows or c>=n_cols or image[r][c]!=oldC:
                return
            
            # Change this pixel color
            image[r][c]=color
            
            # Visit neighbours
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r+1, c)
            DFS(r, c-1)
            return
        
        # Visit neighbours changing colors
        DFS(sr, sc)

        # Return the flooded image
        return image
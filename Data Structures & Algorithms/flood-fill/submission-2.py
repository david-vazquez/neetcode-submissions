class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def DFS(image, r, c, oldC, newC, visited):
            n_rows = len(image)
            n_cols = len(image[0])

            # Base case
            if r<0 or c<0 or r>=n_rows or c>=n_cols or image[r][c]!=oldC or (r,c) in visited:
                return
            else:
                image[r][c]=newC
                visited.add((r,c))
            
            # Visit neighbours
            DFS(image, r-1, c, oldC, newC, visited)
            DFS(image, r, c+1, oldC, newC, visited)
            DFS(image, r+1, c, oldC, newC, visited)
            DFS(image, r, c-1, oldC, newC, visited)
            return

        if image[sr][sc] == color:
            return image
        else:
            DFS(image, sr, sc, image[sr][sc], color, set())
            return image
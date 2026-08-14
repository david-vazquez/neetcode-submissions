class Solution:
    def to2d(self, m, n, i):
        y = i // n
        x = i - y*n
        return x, y

    def binarySearch(self, matrix, m, n, target, L, R):

        if L>R:
            return -1
        
        M=L+(R-L)//2
        x, y = self.to2d(m, n, M)
        if matrix[y][x]>target:
            R=M-1
            return self.binarySearch(matrix, m, n, target, L, R)
        elif matrix[y][x]<target:
            L=M+1
            return self.binarySearch(matrix, m, n, target, L, R)
        else:
            return M
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if self.binarySearch(matrix, m, n, target, 0, m*n-1)>=0:
            return True
        return False
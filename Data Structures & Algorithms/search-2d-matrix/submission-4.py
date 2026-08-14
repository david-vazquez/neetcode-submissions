class Solution:
    def binarySearch(self, row, target, L, R):
        if L>R:
            return -1
        
        M=L+(R-L)//2
        if row[M]>target:
            R=M-1
            return self.binarySearch(row, target, L, R)
        elif row[M]<target:
            L=M+1
            return self.binarySearch(row, target, L, R)
        else:
            return M
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binarySearch(row, target, 0, len(row)-1)>=0:
                return True
        return False
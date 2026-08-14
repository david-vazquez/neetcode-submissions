class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        M=L+(R-L)//2
        while L<=R:
            if nums[M]>target:
                R = M-1
                M=L+(R-L)//2
            elif nums[M]<target:
                L = M+1
                M=L+(R-L)//2
            else:
                return M
        return -1
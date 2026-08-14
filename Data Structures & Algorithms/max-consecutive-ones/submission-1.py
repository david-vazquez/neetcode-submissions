class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        for k, g in groupby(nums):
            if k==1:
                max_count=max(max_count,len(list(g)))
        return max_count

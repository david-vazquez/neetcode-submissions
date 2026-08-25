class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Look for the pivot
        presum = 0
        postsum = sum(nums)
        for i in range(len(nums)):
            postsum -= nums[i]
            if postsum==presum:
                return i
            presum += nums[i]
        
        # Not found
        return -1

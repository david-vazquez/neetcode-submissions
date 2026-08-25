class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # # Compute the presum
        # presum = []
        # total = 0
        # for num in nums:
        #     total += num
        #     presum.append(total)

        # Compute the postsum
        postsum = [0]*(len(nums)+1)
        total = 0
        for i in range(len(nums)-1, -1, -1):
            total += nums[i]
            postsum[i] = total
        
        # Look for the pivot
        presum = 0
        for i in range(len(nums)):
            if postsum[i+1]==presum:
                return i
            presum += nums[i]
        
        # Not found
        return -1

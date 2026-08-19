class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Start variables
        globMax = nums[0]
        globMin = nums[0]
        curMax = 0
        curMin = 0
        total = 0

        for num in nums:
            curMax = max(curMax+num, num)
            curMin = min(curMin+num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
        
        if globMax>0:
            return max(globMax, total-globMin)
        else:
            return globMax

        

            

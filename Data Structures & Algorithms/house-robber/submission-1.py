class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def DFS(nums, i):
            if i>=n:
                return 0
            
            if i in cache:
                return cache[i]
            
            # If I rob this one
            rob_money = nums[i] + DFS(nums, i+2)

            # If I do not rob this one
            no_rob_money = DFS(nums, i+1)

            # Return the max of bought
            max_return = max(rob_money, no_rob_money)
            cache[i] = max_return
            return max_return
        
        return DFS(nums, 0)
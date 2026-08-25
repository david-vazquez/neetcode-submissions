class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Prefix
        prefix = [1]*(len(nums))
        total = 1
        for i in range(len(nums)):
            prefix[i] = total
            total *= nums[i]
        
        # Sufix
        sufix = [1]*(len(nums))
        total = 1
        for i in range(len(nums)-1, -1, -1):
            sufix[i] = total
            total *= nums[i]

        # Output
        out = []
        for i in range(len(nums)):
            out.append(prefix[i]*sufix[i])
        
        return out




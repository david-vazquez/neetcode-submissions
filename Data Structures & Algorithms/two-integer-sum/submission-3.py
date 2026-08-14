class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums = sorted(nums)

        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:]):
                sum = n+m
                if sum == target:
                    return [i,i+j+1]
                # if sum > target:
                #     break
        return []
        
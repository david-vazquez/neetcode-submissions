class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums = sorted(nums)
        seen_dict = {}

        for i, n in enumerate(nums):
            look_for = target - n
            if look_for in seen_dict:
                return [seen_dict[look_for], i]
            else:
                seen_dict[n] = i
            # for j, m in enumerate(nums[i+1:]):
            #     sum = n+m
            #     if sum == target:
            #         return [i,i+j+1]
            #     # if sum > target:
            #     #     break
        return []
        
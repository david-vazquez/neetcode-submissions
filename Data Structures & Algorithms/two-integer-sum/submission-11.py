class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, n in enumerate(nums):
            comp = target-n
            if comp in complements:
                return [complements[comp], i]
            else:
                complements[n]=i
        return []
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dup = {}
        for num in nums:
            if num in non_dup:
                return True
            else:
                non_dup[num] = 1

        return False
        

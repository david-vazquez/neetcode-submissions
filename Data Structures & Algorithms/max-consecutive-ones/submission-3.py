class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        best_streak = 0
        for num in nums:
            current_streak = current_streak + 1 if num == 1 else 0
            if current_streak > best_streak:
                best_streak = current_streak
        return best_streak
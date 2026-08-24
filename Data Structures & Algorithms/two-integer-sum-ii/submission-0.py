class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Start the poonters on the extremes of the array
        L = 0
        R = len(numbers)-1

        # Move the pointers
        while L<R:
            curSum = numbers[L]+numbers[R]
            if curSum == target:
                # Return 1-inded
                return [L+1, R+1]
            elif curSum>target:
                R -= 1
            else:
                L += 1


        
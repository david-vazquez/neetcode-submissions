class NumArray:

    def __init__(self, nums: List[int]):
        # Save the actual numbers
        self.nums = nums

        # Create the prefix sum
        self.prefixSum = [0]
        total = 0
        for num in nums:
            total += num
            self.prefixSum.append(total)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
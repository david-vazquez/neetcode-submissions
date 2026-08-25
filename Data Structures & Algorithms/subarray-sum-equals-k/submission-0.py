class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presumCount = {}
        presumCount[0] = 1
        totalSum = 0
        out = 0
        for num in nums:
            # Check if num-k is in the hash
            totalSum += num
            if totalSum-k in presumCount:
                out += presumCount[totalSum-k]

            # Add the value to the hash
            if totalSum in presumCount:
                presumCount[totalSum] += 1
            else:
                presumCount[totalSum] = 1
            
        return out

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket sort algorithm

        # Count how many repetition of each color
        # count = [0,0,0]
        # for i in nums:
        #     count[i]+=1
        count = Counter(nums)
        
        # Fill the values
        k = 0
        for i in range(3):
            for j in range(count[i]):
                nums[k] = i
                k+=1
        
        

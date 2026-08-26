# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Convert into an array
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        n = len(arr)
        
        # Compute the twin sums
        maxSum = 0
        for i in range(n//2):
            maxSum = max(maxSum, arr[i] + arr[n-i-1])
        
        # Return the maxSum
        return maxSum


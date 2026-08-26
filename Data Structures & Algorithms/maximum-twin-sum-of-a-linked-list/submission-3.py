# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the middle of the list with fast-slow pointers
        fast = head
        slow = head
        while fast:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half
        prev = None
        while slow.next:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        slow.next = prev
        
        # Compute the max sum
        maxSum = 0
        while slow:
            maxSum = max(maxSum, head.val+slow.val)
            head = head.next
            slow = slow.next
        
        # Return the maxSum
        return maxSum


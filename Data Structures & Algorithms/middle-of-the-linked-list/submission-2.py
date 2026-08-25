# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start the fast and slow nodes at the head of the list
        fast = slow = head

        # Iterate
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Return the slow node
        return slow
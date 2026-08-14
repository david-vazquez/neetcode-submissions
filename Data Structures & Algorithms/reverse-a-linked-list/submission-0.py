# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        the_current = head
        while the_current:
            the_next = the_current.next
            the_current.next = previous
            previous = the_current
            the_current = the_next
        return previous
            


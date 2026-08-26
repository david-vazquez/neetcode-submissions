# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use a set
        visited_nodes = set()

        # Traverse the list
        cur = head
        while cur:
            if cur in visited_nodes:
                return True
            else:
                visited_nodes.add(cur)
                cur = cur.next
        
        # No cycles found
        return False
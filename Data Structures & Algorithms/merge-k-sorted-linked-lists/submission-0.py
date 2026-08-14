# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res

        while True:
            # Find the list that has the smaller number
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[i].val < lists[minNode].val:
                    minNode = i
            
            # If we finished all the list we are done
            if minNode == -1:
                break
            
            # Add the node from the selected list to the result and remove it from the selected list
            cur.next = lists[minNode]
            cur = cur.next
            lists[minNode] = lists[minNode].next

        # return the next to res
        return res.next



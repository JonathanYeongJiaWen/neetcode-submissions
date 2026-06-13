# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = slow = ListNode(0,head)
        cur = head
        while n>0:
            cur = cur.next
            n -= 1
        start = head
        while cur:
            slow = slow.next
            cur = cur.next
        if slow and slow.next:
            slow.next = slow.next.next
            return dummy.next
        else:
            return []
        
        
        
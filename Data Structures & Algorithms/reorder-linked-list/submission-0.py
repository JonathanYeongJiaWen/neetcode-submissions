# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Reverse 2nd half
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        head2 = prev #head of reversed 2nd half
        while head and head2:
            head.next, head = head2, head.next
            head2.next, head2 = head, head2.next
        

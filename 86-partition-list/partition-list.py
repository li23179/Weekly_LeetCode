# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        l_dummy, g_dummy = ListNode(), ListNode()
        l_curr, g_curr = l_dummy, g_dummy

        while head:
            if head.val < x:
                l_curr.next = head
                l_curr = l_curr.next
            else:
                g_curr.next = head
                g_curr = g_curr.next

            head = head.next
        
        l_curr.next = g_dummy.next
        g_curr.next = None

        return l_dummy.next

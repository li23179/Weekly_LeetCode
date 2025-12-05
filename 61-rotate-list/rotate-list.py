# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        
        # find the length of the current linked list
        length = 0
        curr = head
        
        while curr:
            length += 1
            curr = curr.next

        # k can be > length of the list if k > length
        # we can just use the remainder to find the actual rotation
        k = k % length
        if k == 0:
            return head

        # find the position where the cut should be at
        t = length - k - 1
        curr = head

        for _ in range(t):
            curr = curr.next

        # cut 
        new_head = curr.next
        curr.next = None

        tail = new_head
        # find the tail of the current segment
        while tail.next:
            tail = tail.next

        tail.next = head

        return new_head
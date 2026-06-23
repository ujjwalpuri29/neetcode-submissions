# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = front = ListNode(0, head)
        i = 0
        while i < n:
            front = front.next
            i += 1
        tail = newHead
        while front.next:
            front = front.next
            tail = tail.next
        
        print(front.val, tail.val)
        tail.next = tail.next.next
        return newHead.next

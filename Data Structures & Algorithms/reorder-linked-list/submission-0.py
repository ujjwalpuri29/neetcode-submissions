# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = self.reverseList(slow.next)
        slow.next = None

        first = head
        while second:
            temp = first.next
            first.next = second
            second = second.next
            first.next.next = temp
            first = first.next.next
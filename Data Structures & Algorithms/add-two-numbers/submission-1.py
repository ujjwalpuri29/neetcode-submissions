# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp1, temp2 = l1, l2
        newHead = ListNode()
        temp = newHead
        while temp1 or temp2 or carry:
            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0
            curr_sum = val1 + val2 + carry 
            temp.next = ListNode(curr_sum % 10)
            temp = temp.next
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
            carry = curr_sum // 10
            
        return newHead.next
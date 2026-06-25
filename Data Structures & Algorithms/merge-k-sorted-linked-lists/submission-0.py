# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2Lists(self, list1, list2):
        newHead = ListNode()
        temp = newHead
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        temp.next = list1 or list2
        return newHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(1, len(lists)):
            lists[i] = self.merge2Lists(lists[i], lists[i-1])
        return lists[-1] if lists else None

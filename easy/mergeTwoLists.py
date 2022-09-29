# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        head = ptr = None
        while list1 and list2:
            if list1.val < list2.val:
                if not head:
                    head = ptr = list1
                else:
                    ptr.next = list1
                    ptr = ptr.next
                list1 = list1.next
            else:
                if not head:
                    head = ptr = list2
                else:
                    ptr.next = list2
                    ptr = ptr.next
                list2 = list2.next
        if list1: ptr.next = list1
        elif list2: ptr.next = list2
        return head

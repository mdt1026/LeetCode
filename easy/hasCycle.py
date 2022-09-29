# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ ALTERNATIVE SOLUTION
        if not head: return False
        d = {head: 0}
        cur = head
        i = 1
        while cur.next:
            cur = cur.next
            if cur in d: return True
            else: d[cur] = i
            i += 1
            
        return False
        """

        # O(1) Space
        # Tortoise and Hare Algorithm
        try:
            slow = head.next
            fast = head.next.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True

        except: return False

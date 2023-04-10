# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        former = latter = head
        if not latter.next:
            return head.next
        if not head.next:
            return None
        while latter.next.next:
            latter = latter.next
            former = former.next
        former.next = former.next.next
        return head
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        former = latter = head
        for node in range(n):
            latter = latter.next
        if not latter:
            return head.next
        while latter.next:
            latter = latter.next
            former = former.next
        former.next = former.next.next
        return head
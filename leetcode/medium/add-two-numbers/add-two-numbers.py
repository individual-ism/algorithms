'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        establishment = ListNode()
        current = establishment
        unincorporated = 0

        while (l1 != None or l2 != None or unincorporated != 0):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            value = val1 + val2 + unincorporated
            unincorporated, nextValue = divmod(value, 10)

            current.next = ListNode(nextValue)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        return establishment.next
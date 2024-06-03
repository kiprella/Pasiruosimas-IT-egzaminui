# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Floyd's Cycle finding algo
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowPntr = head
        fastPntr = head

        while fastPntr is not None and fastPntr.next is not None:
            fastPntr = fastPntr.next.next
            slowPntr = slowPntr.next
        return slowPntr

        
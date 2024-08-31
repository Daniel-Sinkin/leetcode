# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Usually this tortoise, hare approach is to find loops, then we'd check for tortoise == hare
        # Fast Runner
        hare = head
        # Slow Runner
        tortoise = head

        while True:
            if hare is None:
                break
            hare = hare.next
            if hare is None:
                break
            hare = hare.next

            tortoise = tortoise.next

        return tortoise

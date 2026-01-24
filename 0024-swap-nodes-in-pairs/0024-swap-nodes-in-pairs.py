# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head):
        # Create a dummy node to simplify swapping at the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Traverse while there are at least two nodes to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # Perform the swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev two nodes ahead
            prev = first
        
        return dummy.next

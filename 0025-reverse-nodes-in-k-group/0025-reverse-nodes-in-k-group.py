# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        # Count total nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        # Dummy node to simplify head operations
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Reverse in chunks of k
        while count >= k:
            curr = prev.next
            next_node = curr.next
            
            # Reverse k nodes
            for _ in range(k - 1):
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = curr.next
            
            prev = curr
            count -= k
        
        return dummy.next

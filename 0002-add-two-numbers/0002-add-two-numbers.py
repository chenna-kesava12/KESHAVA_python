# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()   # Dummy node to simplify list creation
        current = dummy
        carry = 0

        # Traverse both linked lists and process them one digit at a time
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 if exists, otherwise 0
            val2 = l2.val if l2 else 0  # Get value from l2 if exists, otherwise 0

            total = val1 + val2 + carry  # Add values and carry
            carry = total // 10  # Compute the carry for next iteration
            current.next = ListNode(total % 10)  # Create new node with the result digit
            current = current.next  # Move the pointer to the newly created node

            # Move forward in l1 and l2 if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the next of the dummy node (i.e., the actual head of the result)
        return dummy.next

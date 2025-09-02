# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
 
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val      # The value of the node (a single digit 0–9)
        self.next = next    # Pointer to the next node in the linked list

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]  -> First input linked list
        :type l2: Optional[ListNode]  -> Second input linked list
        :rtype: Optional[ListNode]    -> The resulting linked list
        """
        
        # Create a dummy node to simplify handling the head of the result list.
        dummy = ListNode()
        
        # 'current' will move along the result list as we build it.
        current = dummy
        
        # 'carry' will store any value we need to carry over to the next digit.
        carry = 0
        
        # Loop while there are still nodes in l1 or l2, OR a carry remains.
        while l1 or l2 or carry:
            
            # Get the value from l1 if it exists, else use 0.
            val1 = l1.val if l1 else 0
            
            # Get the value from l2 if it exists, else use 0.
            val2 = l2.val if l2 else 0
            
            # Add the two values plus any carry from the previous step.
            total = val1 + val2 + carry
            
            # Update carry for the next iteration (only the tens digit).
            carry = total // 10
            
            # The new digit to store in the result list (only the ones digit).
            digit = total % 10
            
            # Create a new node with the computed digit and attach it to result.
            current.next = ListNode(digit)
            
            # Move 'current' forward to the new node.
            current = current.next
            
            # Move l1 forward if possible.
            if l1:
                l1 = l1.next
                
            # Move l2 forward if possible.
            if l2:
                l2 = l2.next
        
        # Return the head of the new list (skip the dummy node).
        return dummy.next

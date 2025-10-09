# 143. Reorder List
# Medium
# Topics
# premium lock icon
# Companies
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


# LeetCode provides the ListNode class definition:
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        LeetCode 143 — Reorder List

        :type head: ListNode
        :rtype: None  (modifies the list in place)

        Approach:
          1) Use slow/fast pointers to find the middle of the list.
          2) Reverse the second half starting from the node after the middle.
          3) Merge the first half and the reversed second half by alternating nodes.

        Constraints respected:
          - We only rearrange pointers (do not modify node values).
          - O(1) extra space, O(n) time.
        """
        # Edge cases: 0 or 1 or 2 nodes — already "reordered".
        if not head or not head.next or not head.next.next:
            return

        # -----------------------------
        # 1) Find the middle (slow/fast)
        # -----------------------------
        slow, fast = head, head            # both start at head
        while fast and fast.next:          # advance fast 2 steps, slow 1 step
            slow = slow.next
            fast = fast.next.next
        # After the loop, 'slow' points to the middle node (for even length, it's the left middle)

        # Split the list into two halves:
        # head .. slow is the first half (but we'll break after slow)
        second = slow.next                  # second half starts AFTER the middle
        slow.next = None                    # terminate first half

        # -----------------------------
        # 2) Reverse the second half
        # -----------------------------
        prev, curr = None, second          # standard in-place reverse
        while curr:
            nxt = curr.next                # save next
            curr.next = prev               # reverse pointer
            prev = curr                    # advance prev
            curr = nxt                     # advance curr
        # When done, 'prev' is the head of the reversed second half

        # -----------------------------
        # 3) Merge the two halves
        #    (first: head, second: prev)
        # -----------------------------
        first, second = head, prev         # pointers to current nodes in both halves
        while second:                      # second half is equal or shorter; stop when it runs out
            # Save next pointers
            tmp1 = first.next
            tmp2 = second.next

            # Link one node from second after one from first
            first.next = second
            second.next = tmp1

            # Advance both pointers
            first = tmp1
            second = tmp2

        # No return needed; list is modified in place.

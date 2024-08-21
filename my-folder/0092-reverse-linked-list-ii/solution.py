# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: If head is None or no need to reverse (left == right)
        if not head or left == right:
            return head
        
        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node before the `left`th node
        for _ in range(left - 1):
            prev = prev.next
        
        # Start the reversal process
        curr = prev.next  # The `left`th node
        after = curr.next  # The node after `curr`
        
        # Reverse the nodes between `left` and `right`
        for _ in range(right - left):
            curr.next = after.next  # Point `curr.next` to the node after `after`
            after.next = prev.next  # Move `after` node to the front of the reversed section
            prev.next = after  # Connect `prev` to the newly moved node
            after = curr.next  # Move `after` forward to the next node to be reversed
        
        # Return the new head of the list
        return dummy.next


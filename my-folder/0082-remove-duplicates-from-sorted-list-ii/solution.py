# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getHead(self, current):
        d = current
        while d.next and d.val == d.next.val:  # Corrected condition to check for duplicates
            d = d.next
        return d.next  # Return the next distinct node (or None if at the end)

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head  # Ensure dummy node points to the head of the list
        prev = dummy  # Initialize prev to the dummy node
        current = head  # Start current from the head

        while current:
            if current.next and current.val == current.next.val:  # Corrected condition for duplicates
                h = self.getHead(current)
                prev.next = h  # Skip all duplicates
                current = h  # Move current to the next distinct node
            else:
                prev = current  # Move prev to current
                current = current.next  # Move current to the next node

        return dummy.next  # Return the new head of the list


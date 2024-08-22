# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to start the two lists
        before_head = ListNode(0)
        after_head = ListNode(0)

        # Pointers to the end of the 'before' and 'after' lists
        before = before_head
        after = after_head

        current = head

        while current:
            if current.val < x:
                before.next = current  # Add current node to the 'before' list
                before = before.next  # Move the 'before' pointer
            else:
                after.next = current  # Add current node to the 'after' list
                after = after.next  # Move the 'after' pointer

            current = current.next  # Move to the next node

        after.next = None  # Important: terminate the 'after' list to avoid cycles
        before.next = after_head.next  # Connect the 'before' list with the 'after' list

        return before_head.next  # The head of the new list is the start of the 'before' list


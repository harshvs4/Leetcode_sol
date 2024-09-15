# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node, return head
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even lists
        odd = head
        even = head.next
        even_head = even  # We need to link the end of the odd list to the head of the even list

        # Traverse the list
        while even and even.next:
            # Link odd nodes
            odd.next = even.next
            odd = odd.next

            # Link even nodes
            even.next = odd.next
            even = even.next

        # Connect the end of odd list to the head of even list
        odd.next = even_head

        return head


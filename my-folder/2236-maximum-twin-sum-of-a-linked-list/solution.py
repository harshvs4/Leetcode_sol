# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Use two pointers to find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Calculate the twin sums and find the maximum
        maxi = float('-inf')
        while prev:  # `prev` is the head of the reversed second half
            s = prev.val + head.val
            maxi = max(maxi, s)
            prev = prev.next
            head = head.next

        return maxi


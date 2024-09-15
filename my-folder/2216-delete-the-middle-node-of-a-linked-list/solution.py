# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list contains only one node, return None
        if not head or not head.next:
            return None

        # Step 1: Count the total number of nodes
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        
        # Step 2: Find the middle node's index
        middle_index = count // 2

        # Step 3: Remove the middle node
        current = head
        prev = None
        for i in range(middle_index):
            prev = current
            current = current.next
        
        # Now 'current' is pointing to the middle node
        # Remove the middle node by skipping it in the linked list
        prev.next = current.next

        return head


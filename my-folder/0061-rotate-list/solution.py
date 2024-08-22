# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self, head: ListNode) -> int:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        # Step 1: Get the length of the list
        length = self.getLength(head)
        
        # Step 2: Adjust k
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find the new tail (which will be at position length - k)
        new_tail_pos = length - k
        current = head
        for _ in range(new_tail_pos - 1):
            current = current.next
        
        # Step 4: Set the new head and rearrange pointers
        new_head = current.next
        current.next = None  # Break the list
        
        # Step 5: Find the end of the rotated part and link it to the original head
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        
        return new_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head) -> None:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def findMiddleNode(self, head) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1.locate the mid node
        mid = self.findMiddleNode(head)

        # 2.reverse the second half
        head2 = self.reverseList(mid)

        # 3.merge the first and second half one by one

        while head2.next:
            nxt1= head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt1

            head = nxt1
            head2 = nxt2
        


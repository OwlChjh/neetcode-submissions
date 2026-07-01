# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, l: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = l
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1.locate the mid node
        mid = self.middleNode(head)

        # 2.reverse the second half
        head2 = self.reverseList(mid)

        # 3.merge the first and second half one by one

        while head2.next:
            nxt1 = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt1
            # update head of two lists
            head = nxt1
            head2 = nxt2



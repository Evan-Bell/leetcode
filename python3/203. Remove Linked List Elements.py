# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = ListNode()
        res = ListNode(0,cur)
        while(head):
            if head.val != val:
                cur.next = ListNode(head.val)
                head = head.next
                cur = cur.next
            else:
                head = head.next
        return res.next.next

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
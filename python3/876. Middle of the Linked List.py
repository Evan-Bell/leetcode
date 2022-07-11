# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        """
        nodes = set()
        while(head):
            if(head in nodes):
                return head
            nodes.add(head)
            head = head.next


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
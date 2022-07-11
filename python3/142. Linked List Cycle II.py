# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        while(head):
            if(head in nodes):
                return head
            nodes.add(head)
            head = head.next

                



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
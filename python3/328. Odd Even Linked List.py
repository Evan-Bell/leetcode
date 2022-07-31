# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        
    #FOUND SOL IN DISCUSS, WORKS WELL
        if not head:
            return head
        
        odd = head
        evenHead = even = head.next
        
        while(even and even.next):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = evenHead
        return head
        
        #--------------------------------------------------------------
        #SOLUTION WITH PYTH LISTS, NOT LINKEDLIST MODIFICATION
        odd = []
        even = []
        flag = True
        while(head):
            if(flag):
                odd += [head.val]
            else:
                even += [head.val]
            flag = not flag
            head = head.next
        
        for e in even[::-1]:
            head = ListNode(e, head)
        for o in odd[::-1]:
            head = ListNode(o, head)
        
        return head
        
        
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
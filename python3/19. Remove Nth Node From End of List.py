# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        #Linked Solution
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while(fast.next):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
    
    
    
        #----------------------------------------------------------------------
        #GOOD SOL, REVERSE LIST, THEN REBUILD
        res = []
        while(head):
            res.insert(0,head.val)
            head = head.next
        
        for i in range(len(res)):
            if(i != n-1):
                head = ListNode(res[i], head)
        return head
    
        #------------------------------------------------------------------------------
        #GOOD SOL, STORES VALUES
        nodes = {}
        i = 0
        while(head):
            nodes[i] = head
            i+=1
            head = head.next
        if n>= i:
            return nodes[0].next
        nodes[i-n-1].next = nodes[i-n-1].next.next
        return nodes[0]
    
    


        return low
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
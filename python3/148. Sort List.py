# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

    
        def merge(l, r):
            if not l:
                return r
            if not r:
                return l
            res = None
            if l.val < r.val:
                res = l
                res.next = merge(l.next, r)
            else:
                res = r
                res.next = merge(l,r.next)
                    
            return res
                    
            
            
        def split(inp):
            if not inp or not inp.next:
                return inp
            
            fast = slow = inp
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            right = slow.next
            slow.next = None
            
            l = split(inp)
            r = split(right)
            
            return merge(l, r)
        
        return split(head)
        
        
        #--------------------------------------------------
        #SOL IS TOO SLOW
            
        fast = head
        if not fast:
            return head
        flag = False
        while(not flag):
            flag = True
            while(fast.next):
                if(fast.val > fast.next.val):
                    temp = fast.val
                    fast.val = fast.next.val
                    fast.next.val = temp
                    flag = False
                fast = fast.next
            fast = head
        return head
        
            
            
        
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
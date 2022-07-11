# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = ListNode()
        res = ListNode(0,cur)
        seen = set()
        while(head):
            if(head.val not in seen):
                seen.add(head.val)
                cur.next = ListNode(head.val)
                cur = cur.next
                
            head = head.next
            
        return res.next.next
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
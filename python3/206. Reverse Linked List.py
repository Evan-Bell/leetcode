# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head):
            cur = None
            while head:
                cur = ListNode(head.val, cur)
                head = head.next
            return cur
        return None
                 
    
#         if(not head or not head.next):
#             return head
        
#         ans = Solution.reverseList(self, head.next)
#         head.next.next = head
#         head.next = None
#         return ans

            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
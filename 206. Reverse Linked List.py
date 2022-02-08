

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode): # -> Optional[ListNode]:        
    
        if head == None:
            return None
        
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
        
            
            
   

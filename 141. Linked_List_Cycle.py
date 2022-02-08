# https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head):
        self.head = head
    
        slow = self.head
        fast = self.head.next
        
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
    
        return False
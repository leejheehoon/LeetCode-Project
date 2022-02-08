# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None)

from email import header
import pandas as pd
import numpy as np
import matplotlib as plt



"""
pascal's traingle
https://www.youtube.com/watch?v=nPVEaB3AjUM


1. create odd and even linked list

2. go through the linked list one by one using '.next' method

3. if even number '.next' to previous 'even' node
   if odd number '.next' to previous 'odd' node
   
4. tail of 'odd' node points to head of the 'even' node
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def oddEvenList(self, head: ListNode):# -> Optional[ListNode]:

        if head == None:
            return None
        odd = head
        even = head.next
        even_head = even # to save even head

        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
    
        return head
            



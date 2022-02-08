# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem\


# Creating Linked Lists
# https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python 
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class LinkedLists:
    def __init__(self):
        self.head = None
        
    def insert(self, val):
        newNode = Node(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printl1(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next
            
l1 = LinkedLists()           
l1.insert(1)
l1.insert(2)
l1.insert(4)


l2 = LinkedLists()
l2.insert(1)
l2.insert(3)
l2.insert(4)



#----------------------------------------------------------------------


#? line 9, Why use a dummy varaible
#A To avoid insertion into an empty list

class Solution:
    def mergeTwoLists(self, l1 = ListedNode, l2 = ListedNode):
        dummy = ListedNode()
        tail = dummy
        
        while l1 and l2 :
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1 :
            tail.next = l1
        elif l2 :
            tail.next = l2
            
        return dummy.next

    

    



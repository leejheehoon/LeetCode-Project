""" 232. Implement Queue using Stacks """

class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
            
        self.stack_1.append(x)
        
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def pop(self) -> int:
        return self.stack_1.pop()
    
    def peek(self) -> int:
        return self.stack_1[-1]

    def empty(self) -> bool:
        return not self.stack_1
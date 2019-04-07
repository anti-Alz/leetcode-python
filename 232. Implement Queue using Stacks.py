'''
232. Implement Queue using Stacks
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
You must use only standard operations of a stack -- which means only push 
to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may 
simulate a stack by using a list or deque (double-ended queue), as long as 
you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek 
operations will be called on an empty queue).
'''

class MyQueue:

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.array = []
        self.head, self.tail = 0, 0
        

    def push(self, x):
        '''
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        '''
        self.array.append(x)
        self.tail += 1

    def pop(self):
        '''
        Removes the element from in front of queue and returns that element.
        :rtype: int
        '''
        if self.tail > self.head:
            self.head += 1
            return self.array[self.head-1]
        else:
            return None
        
    def peek(self):
        '''
        Get the front element.
        :rtype: int
        '''
        if self.tail > self.head:
            return self.array[self.head]
        else:
            return None

    def empty(self):
        '''
        Returns whether the queue is empty.
        :rtype: bool
        '''
        if self.tail==self.head:
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.array[self.head:self.tail])

obj = MyQueue()
obj.push(3)
obj.push(4)
obj.push(5)
print(obj)
obj.pop()
print(obj)
obj.peek()
print(obj)
obj.push(6)
print(obj)
obj.empty()

'''

'''
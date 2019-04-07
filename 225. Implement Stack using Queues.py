'''
225. Implement Stack using Queues
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''

class MyStack:

    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.array = []
        self.head, self.tail = 0, 0

    def push(self, x):
        '''
        Push element x onto stack.
        :type x: int
        :rtype: void
        '''
        if len(self.array)==self.tail:
            self.array.append(x)
        else:
            self.array[self.tail] = x

        self.tail +=1

    def pop(self):
        '''
        Removes the element on top of the stack and returns that element.
        :rtype: int
        '''
        if self.tail>0:
            self.tail -=1
            return self.array[self.tail]
        else:
            return None

    def top(self):
        '''
        Get the top element.
        :rtype: int
        '''
        if self.tail >0:
            return self.array[self.tail-1]
        else:
            return None

    def empty(self):
        '''
        Returns whether the stack is empty.
        :rtype: bool
        '''
        if self.tail==0:
            return True
        
        return False


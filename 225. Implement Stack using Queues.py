‘’‘
用双队列实现栈
’‘’

import Queue
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self, queue):
        self.queue1=Queue.Queue()
        self.queue2=Queue.Queue()
        
    def push(self, x):
        # write your code here
        self.queue1.put(x)

    """
    @return: nothing
    """
    def pop(self):`
        # write your code here
        while self.queue1.qsize()>1:
            self.queue2.put(self.queue1.get())
        item=self.queue1.get()
        self.queue1, self.queue2=self.queue2,self.queue1
        return item

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.queue1.qsize()>1:
            self.queue2.put(self.queue1.get())
        item=self.queue1.get()
        self.queue1, self.queue2=self.queue2,self.queue1
        self.queue1.put(item)
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.queue1.empty()
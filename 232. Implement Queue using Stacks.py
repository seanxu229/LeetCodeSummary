'''
写类的时候别忘了写self！
self
self
后一种方法要更好一点点，因为pop和peek方法中可以少一步，判断stack2是否为空，
如果不为空，其实没必要交换stack1和stack2，直接操作stack2直至stack2为空，
把stack1再慢慢加入到stack2中
'''
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack1!=[]:
            self.stack2.append(self.stack1.pop())
        item=self.stack2.pop()
        while self.stack2!=[]:
            self.stack1.append(self.stack2.pop())
        return item

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.stack1!=[]:
            self.stack2.append(self.stack1.pop())
        item=self.stack2.pop()
        self.stack1.append(item)
        while self.stack2!=[]:
            self.stack1.append(self.stack2.pop())  
        return item
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1==[]





class MyQueue(object):
    def __init__(self):
        self.input = []
        self.output = []
        
    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()
        
    def peek(self):
        if(self.output == []):
            while(self.input != []):
                self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self):
        return self.input == [] and self.output == []

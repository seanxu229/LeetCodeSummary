'''单链表的实现'''


class singlenode(object):
	def __init__(self,item):
		self.item=item
		self.next=None

class SinglelinkList(object):
	"""docstring for SinglelinkList"""
	def __init__(self):
		self._head=None
	def is_empty(self):
		return self._head==None
	def length(self):
		cur=self._head
		count=0
		while cur!=None:
			count+=1
			cur=cur.next
		return count
	def travel(self):
		cur=self._head
		while cur!=None:
			print cur.item,
			cur=cur.next
		print('')
	def add(self,item):
		node=singlenode(item)
		node.next=self._head
		self._head=node
	def append(self,item):
		node=singlenode(item)
		if self.is_empty():
			self._head=node
		else:
			cur=self._head
			while cur.next!=None:
				cur=cur.next
			cur.next=node
	def insert(self,pos,item):
		if pos<=0:
			self.add(item)
		elif pos>(self.length()-1):
			self.append(item)
		else:
			node=singlenode(item)
			count=0
			pre=self._head
			while count<pos-1:
				count+=1
				pre=pre.next
			node.next=pre.next
			pre.next=node
    def remove(self,item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False		


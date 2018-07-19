    def mergeTwoLists(self, l1, l2):
        # write your code here
        newNode=ListNode(-1)
        res=newNode
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                newNode.next=l1
                l1=l1.next
            else:
                newNode.next=l2
                l2=l2.next
            newNode=newNode.next
        if l1==None:
            newNode.next=l2
        else:
            newNode.next=l1
        return res.next
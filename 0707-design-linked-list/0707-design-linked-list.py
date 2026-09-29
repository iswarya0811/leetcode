class MyLinkedList:
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        
        while index:
            index-=1
            if temp is None:
                return -1
            temp=temp.next
        if temp== None:
            return -1
        return temp.val

    def addAtHead(self, val: int) -> None:
        newnode = self.Node(val)
        newnode.next = self.head
        self.head = newnode
        
    def addAtTail(self, val: int) -> None:
        newnode = self.Node(val)
        temp = self.head
        if self.head is None:
            self.head = newnode
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
        
    def addAtIndex(self, index: int, val: int) -> None:
        newnode = self.Node(val)

        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        for _ in range(index-1):
            if temp is None:
                return 
            temp = temp.next
        if temp is None:
            return
        newnode.next = temp.next
        temp.next = newnode

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(index-1):
            if temp is None or temp.next is None:
                return
            temp = temp.next
        if temp.next is None:
            return
        temp.next = temp.next.next

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
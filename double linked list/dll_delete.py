class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        

class dll:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty list")
        else:
            temp = self.head
            while temp:
                print(temp.data , " --> " ,end = " ")
                temp = temp.next

    def delete_at_beg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def delete_at_end(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None

    def delete_at_pos(self,pos):
        temp = self.head.next
        before = self.head
        for i in range(1,pos-1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None

l = dll()
n1 = node(100)
l.head = n1
n2 = node(200)
n1.next = n2
n2.prev = n1
n3 = node(300)
n2.next = n3
n3.prev = n2
n4 = node(400)
n3.next = n4
n4.prev = n3
l.display()
#l.delete_at_beg()
#l.delete_at_end()
l.delete_at_pos(3)
print()
l.display()

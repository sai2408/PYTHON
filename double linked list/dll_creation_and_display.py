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
print()

l.display()

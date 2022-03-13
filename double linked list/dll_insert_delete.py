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

    def insert_at_beg(self,data):
        ne = node(data)
        temp = self.head
        temp.prev = ne
        ne.next = temp
        self.head = ne

    def insert_at_end(self,data):
        ne = node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = ne
        ne.prev = temp

    def insert_at_pos(self,pos,data):
        ne = node(data)
        temp = self.head
        for u in range(1,pos-1):
            temp = temp.next
        ne.prev = temp
        ne.next = temp.next
        temp.next.prev = ne
        temp.next = ne
        
            
        

l = dll()
n1 = node(100)
l.head = n1
n2 = node(200)
n1.next = n2
n2.prev = n1
n3 = node(300)
n2.next = n3
n3.prev = n2
l.display()
#l.insert_at_beg(90)
#l.insert_at_end(400)
l.insert_at_pos(3,190)
print()
l.display()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class single_linked_list:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Emty linked list")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end = " ")
                temp = temp.next

    def delete_begg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        
    def delete_pos(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next


l = single_linked_list()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5
l.display()
#l.delete_begg()
#l.delete_end()
l.delete_pos(3)
print("\n")
l.display()

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head == None:
            print("Linked list is emty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end = " ")
                temp = temp.next

    def insert_beg(self,data):
        ne = node(data)
        ne.next = self.head
        self.head = ne

    def insert_end(self,data):
        ne = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_pos(self,pos,data):
        ne = node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        ne.data = data
        ne.next = temp.next
        temp.next = ne

    def delete_beg(self):
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

    def count(self):
        tem = self.head
        c = 0
        while tem:
            c = c+1
            tem = tem.next
        return c


l = sll()
while True:
    print("1 for Insert")
    print("2 for Delete")
    print("3 for Display")
    print("4 for Quit")
    x = input()
    if x == "1":
        while True:
            print("1 to insert at beginning")
            print("2 to insert at ending")
            print("3 to insert at certain position")
            y = input()
            if y == "1":
                print("Enter the value to insert at beginning: ")
                a = input()
                l.insert_beg(a)
                break
            elif y == "2":
                print("Enter the value to insert at ending: ")
                a = input()
                l.insert_end(a)
                break
            elif y == "3":
                print("Enter the value to insert at ending: ")
                a = input()
                print("Enter the value of position: ")
                b = int(input())
                l.insert_pos(b,a)
                break
            else:
                print("Enter the correct value: ")
    elif x == "2":
        while True:
            print("1 to delete at beginning")
            print("2 to delete at ending")
            print("3 to delete at certain position")
            y = input()
            if y == "1":
                l.delete_beg()
                break
            elif y == "2":
                l.delete_end()
                break
            elif y == "3":
                print("Enter the position value to delete\n")
                j = l.count()
                while True:
                    a = int(input())
                    if a < j or a == j:
                        l.delete_pos(a)
                        break
                    else:
                        print("Enter the valid position")
                break
                    
    elif x == "3":
        l.display()
        break
    else:
        print("Enter the correct option")
        

                
                
            
    





    
    

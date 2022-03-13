class SinglyLinkedList:
    class _Node :
        def __init__( self, e ) :
            self._element = e
            self._next = None
    def __init__( self) :
        self._head = None
        self._size = 0 

    def traversal(self):
        curNode = self._head
        while curNode is not None :
            print(curNode._element)
            curNode = curNode._next

    def add_first(self,e):
        newNode =self._Node(e) 
        newNode._next = self._head
        self._head = newNode
        self._size +=1

    def add_last(self,e):
        newNode =self._Node(e)
        preNode=None
        curNode=self._head
        if self._head is None:
            self._head=newNode
        else:
            while curNode is not None:
                preNode = curNode
                curNode = curNode._next
            preNode._next=newNode
        self._size = self._size+1

    def remove_first(self):
        if self._head is None:
            print("list is empty.")
        else:
            self._head = self._head.next 
        self._size -=1

    def remove(self,target):
        predNode = None
        curNode =self._head
        while curNode is not None and curNode._element != target :
            predNode = curNode
            curNode = curNode._next
        if curNode is not None :
            if curNode is self._head:
                self._head = curNode._next
            else :
                predNode._next = curNode._next
        else:
            print("Invalid target")

slist=SinglyLinkedList()
while True:
    print("1.Insert First")
    print("2.Insert Last")
    print("3.Remove")
    print("4. Display")
    print("5. Quit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        item=input("Enter the element to insert :")
        slist.add_first(item)
        print("The element "+item+" inserted successfully");
    elif ch==2:
        item=input("Enter the element to insert :")
        slist.add_last(item)
        print("The element "+item+" inserted successfully");
    elif ch==3:
        item=input("Enter the element to delete :")
        slist.remove(item)
    elif ch==4:
        slist.traversal()
    else:
        print("Exit")
        break

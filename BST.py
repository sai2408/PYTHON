class bst:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        #for dulicate values
        if self.key == data:
            return
        #Insertion at left child
        if self.key > data :
            #if the lchild has any data
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = bst(data)

        #Insertion ar Right child
        else:
            #if the rchild has any data
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = bst(data)
                
#INSEERTION
'''
root = bst(10)
root.insert(20)
root.insert(5)
print(root.key)
print(root.lchild.key)
print(root.rchild.key)
'''


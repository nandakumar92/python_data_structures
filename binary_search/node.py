class Node:

    def __init__(self,val):
        self.val=val
        self.leftChild=None
        self.rightChild=None
        self.parent=None

    ##insert iterative
    def insert(self,val):
        current=self
        parent=None
        while current:
            parent=current
            if val<current.val:
                current=current.leftChild
            else:
                current=current.rightChild          
        if val<parent.val:
            parent.leftChild=Node(val)

        else:
            parent.rightChild=Node(val)

    ##insert recursive
    def insert_recursive(self,val):
        if val<self.val:
            if self.leftChild:
                self.leftChild.insert_recursive(val)
            else:
                self.leftChild=Node(val)
                return
        else:          
           if self.rightChild:
               self.rightChild.insert_recursive(val)
           else:
                self.rightChild=Node(val)
                return

    ##search iterative
    def search(self,val):
        current=self
        while current:
            if val<self.val:
                current=current.leftChild
            elif val>self.val:
                current=current.rightChild
            else:
                return True
        return False

    ### search recursive
    def search_recursive(self,val):
        if val<self.val:
            if self.leftChild:               
                return self.leftChild.search_recursive(val)
            else: 
                return False
        elif val>self.val:
            if self.rightChild:
                return self.rightChild.search_recursive(val)
            else: 
                return False
        else:
            return True

    ## delete
    def delete(self,val):
        if val<self.val:
            if self.leftChild:
                self.leftChild=self.leftChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return None       
        elif val>self.val:
            if self.rightChild:
                self.rightChild=self.rightChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return None
        else:
            ## deleting node with no child
            if self.leftChild is None and self.rightChild is None:
                self=None
                return None
            ##deleting node with right child
            if self.leftChild is None:
                tmp=self.rightChild
                self=None
                return tmp
            ##deleting node with left child
            if self.rightChild is None:
                tmp=self.leftChild
                self=None
                return tmp
             # deleting node with two children
            else:
                # first get the inorder successor
                current = self.rightChild
                # loop down to find the leftmost leaf
                while(current.leftChild is not None):
                    current = current.leftChild
                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)

        return self


            

            





        

            



        


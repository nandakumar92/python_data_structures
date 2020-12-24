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


        

            



        


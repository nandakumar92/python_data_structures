from node import Node

class search:

    def __init__(self,val):
        self.root=Node(val)

    ## insert iterative
    def insert(self,val):

        if self.root:
            self.root.insert(val)
            return
        
        else:
            self.root=Node(val)
            return

    ## insert recursive
    def insert_recursive(self,val):

        if self.root:
            self.root.insert(val)
            return
        
        else:
            self.root=Node(val)
            return

    ## search iterative
    def search(self,val):
        return self.root.search(val)
    
    
    ##search recursive
    def search_recursive(self,val):

        return self.root.search_recursive(val)

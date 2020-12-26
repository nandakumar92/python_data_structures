class List:
    def __init__(self):
        self.header=None

    def is_empty(self):
        if self.header==None:
            return True        
        else: return False

    def get_head(self):
        return self.header
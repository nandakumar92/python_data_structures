class node:
    def __init__(self,char=''):
        self.char=char
        self.children=[None]*26
        self.is_end_word=False

    def mark_as_leaf(self):
        self.is_end_word=True

    def mark_as_not_leaf(self):
        self.is_end_word=False
    
    
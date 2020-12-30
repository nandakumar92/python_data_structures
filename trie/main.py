from node import node
class trie:
    def __init__(self):
        self.root=node()

    def get_index(self,str):
        return ord(str)-ord('a')

    
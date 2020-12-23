from node import Node
from search import search
import random


bst=search(50)

for _ in range(15):
    ele = random.randint(0, 100)
    print("Inserting "+str(ele)+":")
    bst.insert(ele)


for _ in range(15):
    ele = random.randint(0, 100)
    print("Inserting "+str(ele)+":")
    bst.insert_recursive(ele)

print(bst.root.val)
print(bst.root.leftChild.val)
print(bst.root.rightChild.val)
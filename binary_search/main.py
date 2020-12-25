from node import Node
from search import search
import random

## pre order traversal - root->left child->right child
def preOrderPrint(node):
    if node is not None:
        print(node.val)
        preOrderPrint(node.leftChild)
        preOrderPrint(node.rightChild)

## post order traversal - left child->right child-->root
def postOrderPrint(node):
    if node is not None:
        postOrderPrint(node.leftChild)
        postOrderPrint(node.rightChild)
        print(node.val)

## In order traversal - left child->root-->right child
def inOrderPrint(node):
    if node is not None:
        inOrderPrint(node.leftChild)
        print(node.val)
        inOrderPrint(node.rightChild)
    
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
preOrderPrint(bst.root)
postOrderPrint(bst.root)
inOrderPrint(bst.root)
bst.delete_recursive(50)
print(bst.root.val)
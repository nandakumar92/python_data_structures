from node import node
from linked_list import List


def insert_at_head(list,value):   
    temp=node(value)   
    temp.next_element=list.header
    list.header=temp


def insert_at_tail(list,value):
    new_node=node(value)   
    if list.is_empty():
        list.header=new_node
        return
    temp=list.get_head()
    while temp.next_element:           
           temp=temp.next_element  
    temp.next_element=new_node
    return

def search(list,value):
     if list.is_empty():
         return False
     temp=list.get_head()
     while temp.next_element:
         if temp.data==value:
             return True
         temp=temp.next_element    
     return False

def delete_at_head(list,value):
     tmp=list.get_head()
     list.header=tmp.next_element()
     tmp.next_element=None

def delete_value(list,value):
    current=list.get_head()
    prev=None
    if current.data==value:
        delete_at_head(list,value)
    while current.next_element is not None:
        if current.data==value:
            prev.next_element=current.next_element
            current.next_element=None       
        prev=current
        current=current.next_element

def get_count(list):
    tmp=list.get_head()
    i=0
    while tmp is not None:
        i=i+1
        tmp=tmp.next_element   
    return i                  
list=List()


for i in range(10):
    insert_at_tail(list,i)

print(list.get_head().data)
print(get_count(list))




    
from node import node
from list import List

def insert_at_head(list,value):
        temp_node=node(value)       
        if list.is_empty():
           list.header=temp_node
           return
        temp_node.next_element=list.header
        list.header.prev_element=temp_node
        list.header=temp_node
        return 

def insert_at_tail(list,value):
    new_node=node(value)   
    if list.is_empty():
        list.header=new_node
        return
    temp=list.get_head()
    while temp.next_element:           
           temp=temp.next_element  
    temp.next_element=new_node
    new_node.prev_element=temp
    return

def search(list,value):
    if list.header==value:
        return True
    curr=list.get_head()
    while curr:
        if curr.data==value:
            return True
        curr=curr.next_element
    return False    

def delete_at_head(list):
     tmp=list.get_head()
     list.header=tmp.next_element
     tmp.next_element.prev_element=None
     
def delete_value(list,value):
    current=list.get_head()
    if current.data==value:
        delete_at_head(list)
    while current.next_element is not None:
        if current.data==value:
            current.prev_element.next_element=current.next_element
            current.next_element.prev_element=current.prev_element
        current=current.next_element
   
lst=List()

for i in range(10):
    insert_at_tail(lst,i)


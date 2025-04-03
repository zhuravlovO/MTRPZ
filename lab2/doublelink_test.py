import pytest
from doublelink import DoublyLinkedList 

def test_new_list_length_is_zero():
    my_list = DoublyLinkedList()
    assert my_list.length() == 0

def test_new_list_head_is_none():
    my_list = DoublyLinkedList()
    assert my_list.head is None

def test_new_list_tail_is_none():
    my_list = DoublyLinkedList()
    assert my_list.tail is None


def test_append_to_empty_list():
    my_list = DoublyLinkedList()
    my_list.append('a')

    assert my_list.length() == 1
    assert my_list.head is not None       
    assert my_list.tail is not None       
    assert my_list.head is my_list.tail  

    node = my_list.head
    assert node.data == 'a'
    assert node.next is None              
    assert node.prev is None              

def test_append_to_non_empty_list():
    my_list = DoublyLinkedList()
    my_list.append('a') 
    first_node = my_list.head

    my_list.append('b') 

    assert my_list.length() == 2
    assert my_list.head is first_node     
    assert my_list.tail is not first_node 
    assert my_list.tail.data == 'b'      

    second_node = my_list.tail
    assert first_node.next is second_node 
    assert second_node.prev is first_node 
    assert second_node.next is None       
    assert first_node.prev is None      

    my_list.append('c') 

    third_node = my_list.tail
    assert my_list.length() == 3
    assert my_list.tail.data == 'c'
    assert second_node.next is third_node 
    assert third_node.prev is second_node 
    assert third_node.next is None       
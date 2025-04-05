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

def test_insert_into_empty_list_at_zero():
    my_list = DoublyLinkedList()
    my_list.insert('a', 0)
    assert my_list.length() == 1
    assert my_list.head is not None
    assert my_list.head is my_list.tail
    assert my_list.head.data == 'a'
    assert my_list.head.next is None
    assert my_list.head.prev is None

def test_insert_at_beginning():
    my_list = DoublyLinkedList()
    my_list.append('b')
    my_list.append('c')
    old_head = my_list.head
    my_list.insert('a', 0)
    assert my_list.length() == 3
    assert my_list.head is not None
    assert my_list.head.data == 'a'
    assert my_list.head.next is old_head
    assert old_head.prev is my_list.head
    assert my_list.head.prev is None

def test_insert_at_end():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    old_tail = my_list.tail
    my_list.insert('c', 2)
    assert my_list.length() == 3
    assert my_list.tail is not None
    assert my_list.tail.data == 'c'
    assert my_list.tail.prev is old_tail
    assert old_tail.next is my_list.tail
    assert my_list.tail.next is None

def test_insert_in_middle():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('c')
    node_a = my_list.head
    node_c = my_list.tail
    my_list.insert('b', 1)
    assert my_list.length() == 3
    node_b = node_a.next
    assert node_b is not None
    assert node_b.data == 'b'
    assert node_a.next is node_b
    assert node_b.prev is node_a
    assert node_b.next is node_c
    assert node_c.prev is node_b

def test_insert_index_out_of_bounds_negative():
    my_list = DoublyLinkedList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.insert('x', -1)

def test_insert_index_out_of_bounds_too_large():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    with pytest.raises(IndexError):
        my_list.insert('x', 3)

def test_insert_index_out_of_bounds_empty_list():
    my_list = DoublyLinkedList()
    with pytest.raises(IndexError):
        my_list.insert('x', 1)
    with pytest.raises(IndexError):
        my_list.insert('x', -1)

def test_delete_from_list_with_one_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    deleted_value = my_list.delete(0)
    assert deleted_value == 'a'
    assert my_list.length() == 0
    assert my_list.head is None
    assert my_list.tail is None

def test_delete_first_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    node_b = my_list.head.next
    deleted_value = my_list.delete(0)
    assert deleted_value == 'a'
    assert my_list.length() == 2
    assert my_list.head is node_b
    assert my_list.head.data == 'b'
    assert my_list.head.prev is None
    assert my_list.tail.data == 'c'

def test_delete_last_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    node_b = my_list.tail.prev
    deleted_value = my_list.delete(2)
    assert deleted_value == 'c'
    assert my_list.length() == 2
    assert my_list.tail is node_b
    assert my_list.tail.data == 'b'
    assert my_list.tail.next is None
    assert my_list.head.data == 'a'

def test_delete_middle_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    node_a = my_list.head
    node_c = my_list.tail
    deleted_value = my_list.delete(1)
    assert deleted_value == 'b'
    assert my_list.length() == 2
    assert my_list.head is node_a
    assert my_list.tail is node_c
    assert node_a.next is node_c
    assert node_c.prev is node_a

def test_delete_index_out_of_bounds_negative():
    my_list = DoublyLinkedList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.delete(-1)

def test_delete_index_out_of_bounds_equal_length():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    with pytest.raises(IndexError):
        my_list.delete(2)

def test_delete_index_out_of_bounds_too_large():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    with pytest.raises(IndexError):
        my_list.delete(3)

def test_delete_from_empty_list():
    my_list = DoublyLinkedList()
    with pytest.raises(IndexError):
        my_list.delete(0)

def test_get_first_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.get(0) == 'a'

def test_get_last_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c') 
    assert my_list.get(2) == 'c'

def test_get_middle_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.get(1) == 'b'

def test_get_from_list_with_one_element():
    my_list = DoublyLinkedList()
    my_list.append('z')
    assert my_list.get(0) == 'z'

def test_get_index_out_of_bounds_negative():
    my_list = DoublyLinkedList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.get(-1)

def test_get_index_out_of_bounds_equal_length():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b') 
    with pytest.raises(IndexError):
        my_list.get(2) 

def test_get_index_out_of_bounds_too_large():
    my_list = DoublyLinkedList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.get(5) 

def test_get_from_empty_list():
    my_list = DoublyLinkedList()
    with pytest.raises(IndexError):
        my_list.get(0)   

def test_delete_all_element_not_found():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    initial_length = my_list.length()
    my_list.deleteAll('x')
    assert my_list.length() == initial_length
    assert my_list.get(0) == 'a'
    assert my_list.get(1) == 'b'
    assert my_list.get(2) == 'c'

def test_delete_all_single_occurrence_first():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.deleteAll('a')
    assert my_list.length() == 2
    assert my_list.get(0) == 'b'
    assert my_list.get(1) == 'c'
    assert my_list.head.data == 'b'
    assert my_list.head.prev is None

def test_delete_all_single_occurrence_last():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.deleteAll('c')
    assert my_list.length() == 2
    assert my_list.get(0) == 'a'
    assert my_list.get(1) == 'b'
    assert my_list.tail.data == 'b'
    assert my_list.tail.next is None

def test_delete_all_single_occurrence_middle():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.deleteAll('b')
    assert my_list.length() == 2
    assert my_list.get(0) == 'a'
    assert my_list.get(1) == 'c'
    assert my_list.head.next is my_list.tail
    assert my_list.tail.prev is my_list.head

def test_delete_all_multiple_occurrences():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('a')
    my_list.append('c')
    my_list.append('a')
    my_list.deleteAll('a')
    assert my_list.length() == 2
    assert my_list.get(0) == 'b'
    assert my_list.get(1) == 'c'
    assert my_list.head.data == 'b'
    assert my_list.tail.data == 'c'
    assert my_list.head.next is my_list.tail
    assert my_list.tail.prev is my_list.head
    assert my_list.head.prev is None
    assert my_list.tail.next is None

def test_delete_all_when_all_elements_match():
    my_list = DoublyLinkedList()
    my_list.append('x')
    my_list.append('x')
    my_list.append('x')
    my_list.deleteAll('x')
    assert my_list.length() == 0
    assert my_list.head is None
    assert my_list.tail is None

def test_delete_all_from_empty_list():
    my_list = DoublyLinkedList()
    my_list.deleteAll('a')
    assert my_list.length() == 0
    assert my_list.head is None
    assert my_list.tail is None     

def test_clear_non_empty_list():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.length() == 3
    my_list.clear()
    assert my_list.length() == 0
    assert my_list.head is None
    assert my_list.tail is None

def test_clear_empty_list():
    my_list = DoublyLinkedList()
    assert my_list.length() == 0
    my_list.clear()
    assert my_list.length() == 0
    assert my_list.head is None
    assert my_list.tail is None   

def test_find_first_not_found():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findFirst('x') == -1

def test_find_first_empty_list():
    my_list = DoublyLinkedList()
    assert my_list.findFirst('a') == -1

def test_find_first_first_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findFirst('a') == 0

def test_find_first_last_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findFirst('c') == 2

def test_find_first_middle_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findFirst('b') == 1

def test_find_first_with_duplicates():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('a')
    my_list.append('c')
    assert my_list.findFirst('a') == 0 

def test_find_last_not_found():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findLast('x') == -1

def test_find_last_empty_list():
    my_list = DoublyLinkedList()
    assert my_list.findLast('a') == -1

def test_find_last_first_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findLast('a') == 0

def test_find_last_last_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findLast('b') == 1

def test_find_last_middle_element():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findLast('b') == 1

def test_find_last_with_duplicates():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b') 
    my_list.append('a') 
    my_list.append('c') 
    assert my_list.findLast('a') == 2 

def test_clone_empty_list():
    original_list = DoublyLinkedList()
    cloned_list = original_list.clone()
    assert isinstance(cloned_list, DoublyLinkedList)
    assert cloned_list is not original_list
    assert cloned_list.length() == 0
    assert cloned_list.head is None
    assert cloned_list.tail is None

def test_clone_single_element_list():
    original_list = DoublyLinkedList()
    original_list.append('a')
    cloned_list = original_list.clone()
    assert cloned_list is not original_list
    assert cloned_list.length() == 1
    assert cloned_list.get(0) == 'a'
    assert cloned_list.head is not None
    assert cloned_list.head is cloned_list.tail
    assert cloned_list.head is not original_list.head

def test_clone_multiple_elements_list():
    original_list = DoublyLinkedList()
    original_list.append('a')
    original_list.append('b')
    original_list.append('c')
    cloned_list = original_list.clone()
    assert cloned_list is not original_list
    assert cloned_list.length() == 3
    assert cloned_list.get(0) == 'a'
    assert cloned_list.get(1) == 'b'
    assert cloned_list.get(2) == 'c'
    assert cloned_list.head is not original_list.head
    assert cloned_list.tail is not original_list.tail
    assert cloned_list.head.next is not original_list.head.next

def test_clone_is_independent():
    original_list = DoublyLinkedList()
    original_list.append('a')
    original_list.append('b')
    cloned_list = original_list.clone()
    original_list.append('c')
    original_list.delete(0)
    assert cloned_list.length() == 2
    assert cloned_list.get(0) == 'a'
    assert cloned_list.get(1) == 'b'
    cloned_list.insert('x', 1)
    cloned_list.append('y')
    assert original_list.length() == 2
    assert original_list.get(0) == 'b'
    assert original_list.get(1) == 'c'

def test_extend_empty_list_with_non_empty():
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()
    list2.append('a')
    list2.append('b')
    list1.extend(list2)
    assert list1.length() == 2
    assert list1.get(0) == 'a'
    assert list1.get(1) == 'b'
    assert list1.head is not None
    assert list1.tail is not None
    assert list1.head.data == 'a'
    assert list1.tail.data == 'b'
    assert list1.head is not list2.head

def test_extend_non_empty_list_with_empty():
    list1 = DoublyLinkedList()
    list1.append('a')
    list1.append('b')
    list2 = DoublyLinkedList()
    initial_length = list1.length()
    list1.extend(list2)
    assert list1.length() == initial_length
    assert list1.get(0) == 'a'
    assert list1.get(1) == 'b'

def test_extend_non_empty_with_non_empty():
    list1 = DoublyLinkedList()
    list1.append('a')
    list1.append('b')
    list2 = DoublyLinkedList()
    list2.append('c')
    list2.append('d')
    list1.extend(list2)
    assert list1.length() == 4
    assert list1.get(0) == 'a'
    assert list1.get(1) == 'b'
    assert list1.get(2) == 'c'
    assert list1.get(3) == 'd'
    assert list1.head.data == 'a'
    assert list1.tail.data == 'd'

def test_extend_independence():
    list1 = DoublyLinkedList()
    list1.append('a')
    list2 = DoublyLinkedList()
    list2.append('b')
    list2.append('c')
    list1.extend(list2)
    list2.append('d')
    list2.delete(0)
    assert list1.length() == 3
    assert list1.get(0) == 'a'
    assert list1.get(1) == 'b'
    assert list1.get(2) == 'c'

def test_extend_with_wrong_type():
    list1 = DoublyLinkedList()
    list1.append('a')
    not_a_list = ['b', 'c']
    with pytest.raises(TypeError):
        list1.extend(not_a_list)

def test_reverse_empty_list():
    my_list = DoublyLinkedList()
    my_list.reverse()
    assert my_list.length() == 0
    assert my_list.head is None
    assert my_list.tail is None

def test_reverse_single_element_list():
    my_list = DoublyLinkedList()
    my_list.append('a')
    old_head = my_list.head
    my_list.reverse()
    assert my_list.length() == 1
    assert my_list.head is old_head
    assert my_list.tail is old_head
    assert my_list.get(0) == 'a'
    assert my_list.head.next is None
    assert my_list.head.prev is None

def test_reverse_multiple_elements():
    my_list = DoublyLinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    original_head = my_list.head
    original_tail = my_list.tail
    original_length = my_list.length()
    my_list.reverse()
    assert my_list.length() == original_length
    assert my_list.head is original_tail
    assert my_list.tail is original_head
    assert my_list.head.data == 'c'
    assert my_list.tail.data == 'a'
    assert my_list.get(0) == 'c'
    assert my_list.get(1) == 'b'
    assert my_list.get(2) == 'a'
    node_c = my_list.head
    node_b = node_c.next
    node_a = node_b.next
    assert node_c.prev is None
    assert node_c.next is node_b
    assert node_b.prev is node_c
    assert node_b.next is node_a
    assert node_a.prev is node_b
    assert node_a.next is None
    assert my_list.tail is node_a

def test_reverse_two_elements():
    my_list = DoublyLinkedList()
    my_list.append('x')
    my_list.append('y')
    original_head = my_list.head
    original_tail = my_list.tail
    my_list.reverse()
    assert my_list.length() == 2
    assert my_list.head is original_tail
    assert my_list.tail is original_head
    assert my_list.head.data == 'y'
    assert my_list.tail.data == 'x'
    assert my_list.get(0) == 'y'
    assert my_list.get(1) == 'x'
    assert my_list.head.next is my_list.tail
    assert my_list.tail.prev is my_list.head
    assert my_list.head.prev is None
    assert my_list.tail.next is None
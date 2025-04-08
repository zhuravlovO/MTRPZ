import pytest
from builtin import BuiltinList

def test_new_list_length_is_zero():
    my_list = BuiltinList()
    assert my_list.length() == 0

def test_append_to_empty_list():
    my_list = BuiltinList()
    my_list.append('a')
    assert my_list.length() == 1

def test_append_to_non_empty_list():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.length() == 2
    my_list.append('c')
    assert my_list.length() == 3

def test_insert_into_empty_list_at_zero():
    my_list = BuiltinList()
    my_list.insert('a', 0)
    assert my_list.length() == 1

def test_insert_at_beginning():
    my_list = BuiltinList()
    my_list.append('b')
    my_list.append('c')
    my_list.insert('a', 0)
    assert my_list.length() == 3

def test_insert_at_end():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.insert('c', 2)
    assert my_list.length() == 3

def test_insert_in_middle():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('c')
    my_list.insert('b', 1)
    assert my_list.length() == 3

def test_insert_index_out_of_bounds_negative():
    my_list = BuiltinList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.insert('x', -1)

def test_insert_index_out_of_bounds_too_large():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    with pytest.raises(IndexError):
        my_list.insert('x', 3)

def test_insert_index_out_of_bounds_empty_list():
    my_list = BuiltinList()
    with pytest.raises(IndexError):
        my_list.insert('x', 1)
    with pytest.raises(IndexError):
        my_list.insert('x', -1)

def test_delete_from_list_with_one_element():
    my_list = BuiltinList()
    my_list.append('a')
    deleted_value = my_list.delete(0)
    assert deleted_value == 'a'
    assert my_list.length() == 0

def test_delete_first_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    deleted_value = my_list.delete(0)
    assert deleted_value == 'a'
    assert my_list.length() == 2

def test_delete_last_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    deleted_value = my_list.delete(2)
    assert deleted_value == 'c'
    assert my_list.length() == 2

def test_delete_middle_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    deleted_value = my_list.delete(1)
    assert deleted_value == 'b'
    assert my_list.length() == 2

def test_delete_index_out_of_bounds_negative():
    my_list = BuiltinList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.delete(-1)

def test_delete_index_out_of_bounds_equal_length():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    with pytest.raises(IndexError):
        my_list.delete(2)

def test_delete_index_out_of_bounds_too_large():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    with pytest.raises(IndexError):
        my_list.delete(3)

def test_delete_from_empty_list():
    my_list = BuiltinList()
    with pytest.raises(IndexError):
        my_list.delete(0)

def test_get_first_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.get(0) == 'a'

def test_get_last_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.get(2) == 'c'

def test_get_middle_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.get(1) == 'b'

def test_get_from_list_with_one_element():
    my_list = BuiltinList()
    my_list.append('z')
    assert my_list.get(0) == 'z'

def test_get_index_out_of_bounds_negative():
    my_list = BuiltinList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.get(-1)

def test_get_index_out_of_bounds_equal_length():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    with pytest.raises(IndexError):
        my_list.get(2)

def test_get_index_out_of_bounds_too_large():
    my_list = BuiltinList()
    my_list.append('a')
    with pytest.raises(IndexError):
        my_list.get(5)

def test_get_from_empty_list():
    my_list = BuiltinList()
    with pytest.raises(IndexError):
        my_list.get(0)

def test_delete_all_element_not_found():
    my_list = BuiltinList()
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
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.deleteAll('a')
    assert my_list.length() == 2
    assert my_list.get(0) == 'b'
    assert my_list.get(1) == 'c'

def test_delete_all_single_occurrence_last():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.deleteAll('c')
    assert my_list.length() == 2
    assert my_list.get(0) == 'a'
    assert my_list.get(1) == 'b'

def test_delete_all_single_occurrence_middle():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.deleteAll('b')
    assert my_list.length() == 2
    assert my_list.get(0) == 'a'
    assert my_list.get(1) == 'c'

def test_delete_all_multiple_occurrences():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('a')
    my_list.append('c')
    my_list.append('a')
    my_list.deleteAll('a')
    assert my_list.length() == 2
    assert my_list.get(0) == 'b'
    assert my_list.get(1) == 'c'

def test_delete_all_when_all_elements_match():
    my_list = BuiltinList()
    my_list.append('x')
    my_list.append('x')
    my_list.append('x')
    my_list.deleteAll('x')
    assert my_list.length() == 0

def test_delete_all_from_empty_list():
    my_list = BuiltinList()
    my_list.deleteAll('a')
    assert my_list.length() == 0

def test_clear_non_empty_list():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.length() == 3
    my_list.clear()
    assert my_list.length() == 0

def test_clear_empty_list():
    my_list = BuiltinList()
    assert my_list.length() == 0
    my_list.clear()
    assert my_list.length() == 0

def test_find_first_not_found():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findFirst('x') == -1

def test_find_first_empty_list():
    my_list = BuiltinList()
    assert my_list.findFirst('a') == -1

def test_find_first_first_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findFirst('a') == 0

def test_find_first_last_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findFirst('c') == 2

def test_find_first_middle_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findFirst('b') == 1

def test_find_first_with_duplicates():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('a')
    my_list.append('c')
    assert my_list.findFirst('a') == 0

def test_find_last_not_found():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findLast('x') == -1

def test_find_last_empty_list():
    my_list = BuiltinList()
    assert my_list.findLast('a') == -1

def test_find_last_first_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findLast('a') == 0

def test_find_last_last_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    assert my_list.findLast('b') == 1

def test_find_last_middle_element():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    assert my_list.findLast('b') == 1

def test_find_last_with_duplicates():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('a')
    my_list.append('c')
    assert my_list.findLast('a') == 2

def test_clone_empty_list():
    original_list = BuiltinList()
    cloned_list = original_list.clone()
    assert isinstance(cloned_list, BuiltinList)
    assert cloned_list is not original_list
    assert cloned_list.length() == 0

def test_clone_single_element_list():
    original_list = BuiltinList()
    original_list.append('a')
    cloned_list = original_list.clone()
    assert isinstance(cloned_list, BuiltinList)
    assert cloned_list is not original_list
    assert cloned_list.length() == 1
    assert cloned_list.get(0) == 'a'

def test_clone_multiple_elements_list():
    original_list = BuiltinList()
    original_list.append('a')
    original_list.append('b')
    original_list.append('c')
    cloned_list = original_list.clone()
    assert isinstance(cloned_list, BuiltinList)
    assert cloned_list is not original_list
    assert cloned_list.length() == 3
    assert cloned_list.get(0) == 'a'
    assert cloned_list.get(1) == 'b'
    assert cloned_list.get(2) == 'c'

def test_clone_is_independent():
    original_list = BuiltinList()
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
    list1 = BuiltinList()
    list2 = BuiltinList()
    list2.append('a')
    list2.append('b')
    list1.extend(list2)
    assert list1.length() == 2
    assert list1.get(0) == 'a'
    assert list1.get(1) == 'b'

def test_extend_non_empty_list_with_empty():
    list1 = BuiltinList()
    list1.append('a')
    list1.append('b')
    list2 = BuiltinList()
    initial_length = list1.length()
    list1.extend(list2)
    assert list1.length() == initial_length
    assert list1.get(0) == 'a'
    assert list1.get(1) == 'b'

def test_extend_non_empty_with_non_empty():
    list1 = BuiltinList()
    list1.append('a')
    list1.append('b')
    list2 = BuiltinList()
    list2.append('c')
    list2.append('d')
    list1.extend(list2)
    assert list1.length() == 4
    assert list1.get(0) == 'a'
    assert list1.get(1) == 'b'
    assert list1.get(2) == 'c'
    assert list1.get(3) == 'd'

def test_extend_independence():
    list1 = BuiltinList()
    list1.append('a')
    list2 = BuiltinList()
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
    list1 = BuiltinList()
    list1.append('a')
    not_a_list = ['b', 'c']
    with pytest.raises(TypeError):
        list1.extend(not_a_list)

def test_reverse_empty_list():
    my_list = BuiltinList()
    my_list.reverse()
    assert my_list.length() == 0

def test_reverse_single_element_list():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.reverse()
    assert my_list.length() == 1
    assert my_list.get(0) == 'a'

def test_reverse_multiple_elements():
    my_list = BuiltinList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    original_length = my_list.length()
    my_list.reverse()
    assert my_list.length() == original_length
    assert my_list.get(0) == 'c'
    assert my_list.get(1) == 'b'
    assert my_list.get(2) == 'a'

def test_reverse_two_elements():
    my_list = BuiltinList()
    my_list.append('x')
    my_list.append('y')
    my_list.reverse()
    assert my_list.length() == 2
    assert my_list.get(0) == 'y'
    assert my_list.get(1) == 'x'
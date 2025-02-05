from lib.most_often import *

"""
Given that we have an empty list 
returns no clear winner
"""
def test_an_empty_list_returns_no_clear_winner():
    most_often = MostOften([])
    assert most_often.get_most_often() == "no clear winner"

"""
Given an initial starting list of one item 
it returns the item as a winner for most often
"""
def test_get_most_often_returns_single_item():
    most_often = MostOften([1])
    assert most_often.get_most_often() == 1

"""
Given a list with a clear winner 
return the winner
"""
def test_list_with_clear_winner_returns_winner():
    most_often = MostOften([1, 1, "a"])
    assert most_often.get_most_often() == 1

"""
Given a list with a reversed order
return the winner
"""
def test_list_with_reverse_order_returns_winner():
    most_often = MostOften(["a", 1, 1])
    assert most_often.get_most_often() == 1

"""
Given a list with two that are equal 
return no clear winner
"""
def test_list_with_equal_items_returns_no_winner():
    most_often = MostOften([1, 1, "a", "a"])
    assert most_often.get_most_often() == "no clear winner"

"""
Given a list with two that are equal and an extra item
return no clear winner
"""
def test_list_with_equal_items_and_extra_item_returns_no_winner():
    most_often = MostOften([1, 1, "a", "a", False])
    assert most_often.get_most_often() == "no clear winner"

"""
Given an empty list where we add an item
list updates with the item
"""
def test_add_item_adds_to_list():
    most_often = MostOften([])
    most_often.add_new(False)
    assert most_often.starting_list == [False]

"""
Given a populated list where we add an item
list updates with the item
"""
def test_add_item_to_populated_list():
    most_often = MostOften([1, 2, 3, "4"])
    most_often.add_new(4)
    assert most_often.starting_list == [1, 2, 3, "4", 4]

"""
Given a populated list where we add a list
list updates with the item and most often returns new item
"""
def test_add_list_item_to_populated_list():
    most_often = MostOften([[1, 2, 3, "4"]])
    most_often.add_new([1, 2, 3, "4"])
    assert most_often.starting_list == [[1, 2, 3, "4"], [1, 2, 3, "4"]]
    assert most_often.get_most_often() == [1, 2, 3, "4"]


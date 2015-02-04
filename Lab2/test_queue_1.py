__author__ = 'horton'

from ourqueue import Ourqueue

def test_front_empty():
    """Q1: test calling front on empty queue"""
    q1 = Ourqueue()
    res = q1.front()
    assert res == None

def test_remove_empty():
    """Q2: test calling remove on empty queue"""
    q1 = Queue()
    res = q1.remove()
    assert res == None, "removing from empty Queue should return None"
    assert len(q1) == 0,  "removing from empty Queue should leave len==0"

def test_remove_size1():
    """Q3: test calling remove on queue of size 1"""
    q1 = Queue([1])
    res = q1.remove()
    assert res == 1
    assert len(q1) == 0
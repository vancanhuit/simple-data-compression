import pytest
from huffman import compress
from queue import PriorityQueue
from huffman.node import Node


class TestCompress(object):
    def test_create_queue_from_data(self):
        data = {'a': 1, 'b': 2}
        q = compress.create_queue_from_data(data)
        assert not q.empty()
        assert q.qsize() == 2
        assert q.get()[1] == Node('a', 1)
        assert q.get()[1] == Node('b', 2)

    def test_get_code(self):
        child1 = Node('a', 1)
        child2 = Node('b', 2)
        child3 = Node('', 3, child1, child2)
        child4 = Node('c', 4)
        root = Node('', 7, child3, child4)

        codes = compress.get_codes(root)
        assert type(codes) is dict
        assert 'a' in codes.keys()
        assert 'b' in codes.keys()
        assert 'c' in codes.keys()
        assert codes['a'] == '00'
        assert codes['b'] == '01'
        assert codes['c'] == '1'

    def test_compress(self):
        data = {'a': 1, 'b': 2}
        codes = compress.compress(data)
        assert type(codes) is dict
        assert 'a' in codes.keys()
        assert 'b' in codes.keys()
        assert codes['a'] == '0'
        assert codes['b'] == '1'
